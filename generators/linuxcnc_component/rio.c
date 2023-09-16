/********************************************************************
* Description:  rio.c
*               This file, 'rio.c', is a HAL component that
*               provides an SPI connection to a external FPGA-Board running RIO firmware.
*
*				Initially developed for RaspberryPi -> Arduino Due.
*				Further developed for RaspberryPi -> Smoothieboard and clones (LPC1768).
*
* Author: Scott Alford
* Modified by: Oliver Dippel
* License: GPL Version 2
*
*		Credit to GP Orcullo and PICnc V2 which originally inspired this
*		and portions of this code is based on stepgen.c by John Kasunich
*		and hm2_rpspi.c by Matsche
*
* Copyright (c) 2021	All rights reserved.
*
* Last change:
********************************************************************/


#include "rtapi.h"			/* RTAPI realtime OS API */
#include "rtapi_app.h"		/* RTAPI realtime module decls */
#include "hal.h"			/* HAL public API decls */

#include <math.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

#include "rio.h"


#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>

#ifdef TRANSPORT_UDP
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#endif
#ifdef TRANSPORT_SERIAL
#include <fcntl.h> 
#include <termios.h>
#endif
#ifdef TRANSPORT_SPI
#include "bcm2835.h"
#include "bcm2835.c"
#endif

#define MODNAME "rio"
#define PREFIX "rio"

MODULE_AUTHOR("Oliver Dippel (based on code from Scott Alford AKA scotta)");
MODULE_DESCRIPTION("Driver for RIO FPGA boards");
MODULE_LICENSE("GPL v2");

char *ctrl_type[JOINTS] = { "p" };
RTAPI_MP_ARRAY_STRING(ctrl_type, JOINTS, "control type (pos or vel)");

/***********************************************************************
*                STRUCTURES AND GLOBAL VARIABLES                       *
************************************************************************/

typedef struct {
    hal_bit_t		*SPIenable;
    hal_bit_t		*SPIreset;
    hal_bit_t		*PRUreset;
    bool			SPIresetOld;
    hal_bit_t		*SPIstatus;
    hal_bit_t 		*stepperEnable[JOINTS];
    int				pos_mode[JOINTS];
    hal_float_t 	*pos_cmd[JOINTS];			// pin: position command (position units)
    hal_float_t 	*vel_cmd[JOINTS];			// pin: velocity command (position units/sec)
    hal_float_t 	*pos_fb[JOINTS];			// pin: position feedback (position units)
    hal_s32_t		*count[JOINTS];				// pin: psition feedback (raw counts)
    hal_float_t 	pos_scale[JOINTS];			// param: steps per position unit
    hal_float_t 	fb_scale[JOINTS];			// param: steps per position unit
    float 			freq[JOINTS];				// param: frequency command sent to PRU
    hal_float_t 	*freq_cmd[JOINTS];			// pin: frequency command monitoring, available in LinuxCNC
    hal_float_t 	maxvel[JOINTS];				// param: max velocity, (pos units/sec)
    hal_float_t 	maxaccel[JOINTS];			// param: max accel (pos units/sec^2)
    hal_float_t		*pgain[JOINTS];
    hal_float_t		*ff1gain[JOINTS];
    hal_float_t		*deadband[JOINTS];
    float 			old_pos_cmd[JOINTS];		// previous position command (counts)
    float 			old_pos_cmd_raw[JOINTS];		// previous position command (counts)
    float 			old_scale[JOINTS];			// stored scale value
    float 			scale_recip[JOINTS];		// reciprocal value used for scaling
    float			prev_cmd[JOINTS];
    float			cmd_d[JOINTS];					// command derivative
    hal_float_t 	*setPoint[VARIABLE_OUTPUTS];
    hal_float_t 	*setPointOffset[VARIABLE_OUTPUTS];
    hal_float_t 	*setPointScale[VARIABLE_OUTPUTS];
    hal_float_t 	*processVariable[VARIABLE_INPUTS];
    hal_s32_t 	    *processVariableS32[VARIABLE_INPUTS];
    hal_bit_t   	*outputs[DIGITAL_OUTPUT_BYTES * 8];
    hal_bit_t   	*inputs[DIGITAL_INPUT_BYTES * 8 * 2]; // for not pins * 2
    hal_float_t 	*processVariableScale[VARIABLE_INPUTS];
    hal_float_t 	*processVariableOffset[VARIABLE_INPUTS];
    hal_float_t 	*processVariableExtra[VARIABLE_INPUTS][2];
#ifdef INDEX_MAX
    hal_bit_t   	*index_enable[INDEX_MAX];
#endif
} data_t;

static data_t *data;
static txData_t txData;
static rxData_t rxData;

long stamp = 0;


/* other globals */
#ifdef INDEX_MAX
float index_enable_in[INDEX_MAX] = {0.0};
#endif
static int 			comp_id;				// component ID
static const char 	*modname = MODNAME;
static const char 	*prefix = PREFIX;
static int 			num_chan = 0;			// number of step generators configured
static long 		old_dtns;				// update_freq function period in nsec - (THIS IS RUNNING IN THE PI)
static double		dt;						// update_freq period in seconds  - (THIS IS RUNNING IN THE PI)
static double 		recip_dt;				// recprocal of period, avoids divides

static int64_t 		accum[JOINTS] = { 0 };
static int32_t 		old_count[JOINTS] = { 0 };
static int32_t		accum_diff = 0;

typedef enum CONTROL { POSITION, VELOCITY, INVALID } CONTROL;

static int reset_gpio_pin = 25;				// RPI GPIO pin number used to force watchdog reset of the PRU



#ifdef TRANSPORT_UDP
#define DST_PORT 2390
#define SRC_PORT 2390
#define SEND_TIMEOUT_US 10
#define RECV_TIMEOUT_US 10
#define READ_PCK_DELAY_NS 10000

static int udpSocket;
static int errCount;
struct sockaddr_in dstAddr, srcAddr;
struct hostent *server;
static const char *dstAddress = UDP_IP;
static int UDP_init(void);
#endif


#ifdef TRANSPORT_SERIAL
int serial_fd = -1;
#endif

/***********************************************************************
*                  LOCAL FUNCTION DECLARATIONS                         *
************************************************************************/
static int rt_bcm2835_init(void);

static void update_freq(void *arg, long period);
static void rio_readwrite();
static void rio_transfer();
static CONTROL parse_ctrl_type(const char *ctrl);

/***********************************************************************
*                       INIT AND EXIT CODE                             *
************************************************************************/


#ifdef TRANSPORT_SERIAL

int set_interface_attribs (int fd, int speed, int parity) {
        struct termios tty;
        if (tcgetattr (fd, &tty) != 0) {
            rtapi_print("ERROR: can't setup usb: %s\n", strerror(errno));
            return errno;
        }
        cfsetospeed (&tty, speed);
        cfsetispeed (&tty, speed);
        tty.c_cflag = (tty.c_cflag & ~CSIZE) | CS8;     // 8-bit chars
        tty.c_iflag &= ~IGNBRK;         // disable break processing
        tty.c_lflag = 0;                // no signaling chars, no echo,
        tty.c_oflag = 0;                // no remapping, no delays
        tty.c_cc[VMIN]  = 0;            // read doesn't block
        tty.c_cc[VTIME] = 0;            // 0.5 seconds read timeout
        tty.c_iflag &= ~(IXON | IXOFF | IXANY); // shut off xon/xoff ctrl
        tty.c_cflag |= (CLOCAL | CREAD);// ignore modem controls, enable reading
        tty.c_cflag &= ~(PARENB | PARODD);      // shut off parity
        tty.c_cflag |= parity;
        tty.c_cflag &= ~CSTOPB;
        tty.c_cflag &= ~CRTSCTS;

        if (tcsetattr (fd, TCSANOW, &tty) != 0) {
            rtapi_print("ERROR: can't setup usb: %s\n", strerror(errno));
            return errno;
        }
        return 0;
}

#endif


int rtapi_app_main(void)
{
    char name[HAL_NAME_LEN + 1];
    int n = 0;
    int bn = 0;
    int retval = 0;

    for (n = 0; n < JOINTS; n++) {
        if(parse_ctrl_type(ctrl_type[n]) == INVALID) {
            rtapi_print_msg(RTAPI_MSG_ERR,
                            "STEPGEN: ERROR: bad control type '%s' for axis %i (must be 'p' or 'v')\n",
                            ctrl_type[n], n);
            return -1;
        }
    }

    // connect to the HAL, initialise the driver
    comp_id = hal_init(modname);
    if (comp_id < 0) {
        rtapi_print_msg(RTAPI_MSG_ERR, "%s ERROR: hal_init() failed \n", modname);
        return -1;
    }

    // allocate shared memory
    data = hal_malloc(sizeof(data_t));
    if (data == 0) {
        rtapi_print_msg(RTAPI_MSG_ERR,
                        "%s: ERROR: hal_malloc() failed\n", modname);
        hal_exit(comp_id);
        return -1;
    }


#ifdef TRANSPORT_UDP
    // Initialize the UDP socket
    rtapi_print("Info: Initialize the UDP socket\n");
    if (UDP_init() < 0) {
        rtapi_print_msg(RTAPI_MSG_ERR, "Error: The board is unreachable\n");
        return -1;
    }
#endif

#ifdef TRANSPORT_SERIAL
    rtapi_print("Info: Initialize serial connection\n");
    serial_fd = open (SERIAL_PORT, O_RDWR | O_NOCTTY | O_SYNC);
    if (serial_fd < 0) {
        rtapi_print_msg(RTAPI_MSG_ERR,"usb setup error\n");
        return errno;
    }
    set_interface_attribs (serial_fd, SERIAL_SPEED, 0);
#endif

#ifdef TRANSPORT_SPI
    rtapi_print("Info: Initialize SPI connection\n");
    // Map the RPi BCM2835 peripherals - uses "rtapi_open_as_root" in place of "open"
    if (!rt_bcm2835_init()) {
        rtapi_print_msg(RTAPI_MSG_ERR,"rt_bcm2835_init failed. Are you running with root privlages??\n");
        return -1;
    }

    // Set the SPI0 pins to the Alt 0 function to enable SPI0 access, setup CS register
    // and clear TX and RX fifos
    if (!bcm2835_spi_begin()) {
        rtapi_print_msg(RTAPI_MSG_ERR,"bcm2835_spi_begin failed. Are you running with root privlages??\n");
        return -1;
    }

    // Configure SPI0
    bcm2835_spi_setBitOrder(BCM2835_SPI_BIT_ORDER_MSBFIRST);
    bcm2835_spi_setDataMode(BCM2835_SPI_MODE0);
    bcm2835_spi_setClockDivider(SPI_SPEED);
    bcm2835_spi_chipSelect(BCM2835_SPI_CS_NONE);
    bcm2835_gpio_set_pud(RPI_GPIO_P1_19, BCM2835_GPIO_PUD_DOWN);	// MOSI
    bcm2835_gpio_set_pud(RPI_GPIO_P1_21, BCM2835_GPIO_PUD_DOWN);	// MISO
    bcm2835_gpio_set_pud(RPI_GPIO_P1_24, BCM2835_GPIO_PUD_UP);		// CS0

#endif

    retval = hal_pin_bit_newf(HAL_IN, &(data->SPIenable),
                              comp_id, "%s.SPI-enable", prefix);
    if (retval != 0) goto error;

    retval = hal_pin_bit_newf(HAL_IN, &(data->SPIreset),
                              comp_id, "%s.SPI-reset", prefix);
    if (retval != 0) goto error;

    retval = hal_pin_bit_newf(HAL_OUT, &(data->SPIstatus),
                              comp_id, "%s.SPI-status", prefix);
    if (retval != 0) goto error;

    //bcm2835_gpio_fsel(reset_gpio_pin, BCM2835_GPIO_FSEL_OUTP);
    retval = hal_pin_bit_newf(HAL_IN, &(data->PRUreset),
                              comp_id, "%s.PRU-reset", prefix);
    if (retval != 0) goto error;


    // export all the variables for each joint
    for (n = 0; n < JOINTS; n++) {
        // export pins

        data->pos_mode[n] = (parse_ctrl_type(ctrl_type[n]) == POSITION);

        retval = hal_pin_bit_newf(HAL_IN, &(data->stepperEnable[n]),
                                  comp_id, "%s.joint.%01d.enable", prefix, n);
        if (retval != 0) goto error;

        retval = hal_pin_float_newf(HAL_IN, &(data->pos_cmd[n]),
                                    comp_id, "%s.joint.%01d.pos-cmd", prefix, n);
        if (retval < 0) goto error;
        *(data->pos_cmd[n]) = 0.0;

        if (data->pos_mode[n] == 0) {
            retval = hal_pin_float_newf(HAL_IN, &(data->vel_cmd[n]),
                                        comp_id, "%s.joint.%01d.vel-cmd", prefix, n);
            if (retval < 0) goto error;
            *(data->vel_cmd[n]) = 0.0;
        }

        retval = hal_pin_float_newf(HAL_OUT, &(data->freq_cmd[n]),
                                    comp_id, "%s.joint.%01d.freq-cmd", prefix, n);
        if (retval < 0) goto error;
        *(data->freq_cmd[n]) = 0.0;

        retval = hal_pin_float_newf(HAL_OUT, &(data->pos_fb[n]),
                                    comp_id, "%s.joint.%01d.pos-fb", prefix, n);
        if (retval < 0) goto error;
        *(data->pos_fb[n]) = 0.0;

        retval = hal_param_float_newf(HAL_RW, &(data->pos_scale[n]),
                                      comp_id, "%s.joint.%01d.scale", prefix, n);
        if (retval < 0) goto error;
        data->pos_scale[n] = 1.0;

        retval = hal_param_float_newf(HAL_RW, &(data->fb_scale[n]),
                                      comp_id, "%s.joint.%01d.fb-scale", prefix, n);
        if (retval < 0) goto error;
        data->fb_scale[n] = 0.0;

        retval = hal_pin_s32_newf(HAL_OUT, &(data->count[n]),
                                  comp_id, "%s.joint.%01d.counts", prefix, n);
        if (retval < 0) goto error;
        *(data->count[n]) = 0;

        retval = hal_pin_float_newf(HAL_IN, &(data->pgain[n]),
                                    comp_id, "%s.joint.%01d.pgain", prefix, n);
        if (retval < 0) goto error;
        *(data->pgain[n]) = 0.0;

        retval = hal_pin_float_newf(HAL_IN, &(data->ff1gain[n]),
                                    comp_id, "%s.joint.%01d.ff1gain", prefix, n);
        if (retval < 0) goto error;
        *(data->ff1gain[n]) = 0.0;

        retval = hal_pin_float_newf(HAL_IN, &(data->deadband[n]),
                                    comp_id, "%s.joint.%01d.deadband", prefix, n);
        if (retval < 0) goto error;
        *(data->deadband[n]) = 0.0;

        retval = hal_param_float_newf(HAL_RW, &(data->maxaccel[n]),
                                      comp_id, "%s.joint.%01d.maxaccel", prefix, n);
        if (retval < 0) goto error;
        data->maxaccel[n] = 1.0;
    }

    for (n = 0; n < VARIABLE_OUTPUTS; n++) {
        retval = hal_pin_float_newf(HAL_IN, &(data->setPoint[n]),
                                    comp_id, "%s.%s", prefix, vout_names[n]);
        if (retval < 0) goto error;
        *(data->setPoint[n]) = 0.0;

		retval = hal_pin_float_newf(HAL_IN, &(data->setPointScale[n]),
									comp_id, "%s.%s-scale", prefix, vout_names[n]);
        if (retval < 0) goto error;
        *(data->setPointScale[n]) = 1.0;

		retval = hal_pin_float_newf(HAL_IN, &(data->setPointOffset[n]),
									comp_id, "%s.%s-offset", prefix, vout_names[n]);
        if (retval < 0) goto error;
        *(data->setPointOffset[n]) = 0.0;
    }

    for (n = 0; n < VARIABLE_INPUTS; n++) {
		retval = hal_pin_float_newf(HAL_OUT, &(data->processVariable[n]), comp_id, "%s.%s", prefix, vin_names[n]);
        if (retval < 0) goto error;
        *(data->processVariable[n]) = 0.0;

		retval = hal_pin_s32_newf(HAL_OUT, &(data->processVariableS32[n]), comp_id, "%s.%s-s32", prefix, vin_names[n]);
        if (retval < 0) goto error;
        *(data->processVariableS32[n]) = 0;

		retval = hal_pin_float_newf(HAL_IN, &(data->processVariableScale[n]), comp_id, "%s.%s-scale", prefix, vin_names[n]);
        if (retval < 0) goto error;
        *(data->processVariableScale[n]) = 1.0;

		retval = hal_pin_float_newf(HAL_IN, &(data->processVariableOffset[n]), comp_id, "%s.%s-offset", prefix, vin_names[n]);
        if (retval < 0) goto error;
        *(data->processVariableOffset[n]) = 0.0;

        if (vin_type[n] == TYPE_VIN_ENCODER) {
            retval = hal_pin_float_newf(HAL_IN, &(data->processVariableExtra[n][0]), comp_id, "%s.%s-rpm", prefix, vin_names[n]);
            if (retval < 0) goto error;
            *(data->processVariableExtra[n][0]) = 0.0;

            retval = hal_pin_float_newf(HAL_IN, &(data->processVariableExtra[n][1]), comp_id, "%s.%s-last", prefix, vin_names[n]);
            if (retval < 0) goto error;
            *(data->processVariableExtra[n][1]) = 0.0;
        }
    }

    int index_num = 0;
    for (bn = 0; bn < DIGITAL_OUTPUT_BYTES; bn++) {
        for (n = 0; n < 8; n++) {
            if (bn * 8 + n < DIGITAL_OUTPUTS) {
                if (dout_types[bn * 8 + n] != DTYPE_INDEX) {
                    retval = hal_pin_bit_newf(HAL_IN, &(data->outputs[bn * 8 + n]), comp_id, "%s.%s", prefix, dout_names[bn * 8 + n]);
                    if (retval != 0) goto error;
                    *(data->outputs[bn * 8 + n]) = 0;
                } else {
#ifdef INDEX_MAX
                    retval = hal_pin_bit_newf(HAL_IO, &(data->index_enable[index_num]), comp_id, "%s.%s", prefix, dout_names[bn * 8 + n]);
                    if (retval != 0) goto error;
                    index_num++;
#endif
                }
            }
        }
    }

    for (bn = 0; bn < DIGITAL_INPUT_BYTES; bn++) {
        for (n = 0; n < 8; n++) {
            if (bn * 8 + n < DIGITAL_INPUTS) {
                if (din_types[bn * 8 + n] != DTYPE_INDEX) {
                    retval = hal_pin_bit_newf(HAL_OUT, &(data->inputs[(bn * 8 + n) * 2]), comp_id, "%s.%s", prefix, din_names[bn * 8 + n]);
                    if (retval != 0) goto error;
                    *(data->inputs[(bn * 8 + n) * 2]) = 0;
                    retval = hal_pin_bit_newf(HAL_OUT, &(data->inputs[(bn * 8 + n) * 2 + 1]), comp_id, "%s.%s-not", prefix, din_names[bn * 8 + n]);
                    if (retval != 0) goto error;
                    *(data->inputs[(bn * 8 + n) * 2 + 1]) = 1;
                }
            }
        }
    }



error:
    if (retval < 0) {
        rtapi_print_msg(RTAPI_MSG_ERR,
                        "%s: ERROR: pin export failed with err=%i\n",
                        modname, retval);
        hal_exit(comp_id);
        return -1;
    }


    // Export functions
    rtapi_snprintf(name, sizeof(name), "%s.update-freq", prefix);
    retval = hal_export_funct(name, update_freq, data, 1, 0, comp_id);
    if (retval < 0) {
        rtapi_print_msg(RTAPI_MSG_ERR,
                        "%s: ERROR: update function export failed\n", modname);
        hal_exit(comp_id);
        return -1;
    }

    rtapi_snprintf(name, sizeof(name), "%s.readwrite", prefix);
    retval = hal_export_funct(name, rio_readwrite, data, 1, 0, comp_id);
    if (retval < 0) {
        rtapi_print_msg(RTAPI_MSG_ERR,
                        "%s: ERROR: read function export failed\n", modname);
        hal_exit(comp_id);
        return -1;
    }

    rtapi_print_msg(RTAPI_MSG_INFO, "%s: installed driver\n", modname);
    hal_ready(comp_id);
    return 0;
}

void rtapi_app_exit(void)
{
    hal_exit(comp_id);
}


/***********************************************************************
*                   LOCAL FUNCTION DEFINITIONS                         *
************************************************************************/


// This is the same as the standard bcm2835 library except for the use of
// "rtapi_open_as_root" in place of "open"

#ifdef TRANSPORT_UDP
int UDP_init(void)
{
    int ret;

    // Create a UDP socket
    udpSocket = socket(PF_INET, SOCK_DGRAM, IPPROTO_UDP);
    if (udpSocket < 0) {
        rtapi_print("ERROR: can't open socket: %s\n", strerror(errno));
        return -errno;
    }

    bzero((char*) &dstAddr, sizeof(dstAddr));
    dstAddr.sin_family = AF_INET;
    dstAddr.sin_addr.s_addr = inet_addr(dstAddress);
    dstAddr.sin_port = htons(DST_PORT);

    bzero((char*) &srcAddr, sizeof(srcAddr));
    srcAddr.sin_family = AF_INET;
    srcAddr.sin_addr.s_addr = htonl(INADDR_ANY);
    srcAddr.sin_port = htons(SRC_PORT);

    // bind the local socket to SCR_PORT
    ret = bind(udpSocket, (struct sockaddr *) &srcAddr, sizeof(srcAddr));
    if (ret < 0) {
        rtapi_print("ERROR: can't bind: %s\n", strerror(errno));
        return -errno;
    }

    // Connect to send and receive only to the server_addr
    ret = connect(udpSocket, (struct sockaddr*) &dstAddr, sizeof(struct sockaddr_in));
    if (ret < 0) {
        rtapi_print("ERROR: can't connect: %s\n", strerror(errno));
        return -errno;
    }

    struct timeval timeout;
    timeout.tv_sec = 0;
    timeout.tv_usec = RECV_TIMEOUT_US;

    ret = setsockopt(udpSocket, SOL_SOCKET, SO_RCVTIMEO, (char*) &timeout, sizeof(timeout));
    if (ret < 0) {
        rtapi_print("ERROR: can't set receive timeout socket option: %s\n", strerror(errno));
        return -errno;
    }

    timeout.tv_usec = SEND_TIMEOUT_US;
    ret = setsockopt(udpSocket, SOL_SOCKET, SO_SNDTIMEO, (char*) &timeout,
                     sizeof(timeout));
    if (ret < 0) {
        rtapi_print("ERROR: can't set send timeout socket option: %s\n", strerror(errno));
        return -errno;
    }

    return 0;
}

#endif

#ifdef TRANSPORT_SPI
int rt_bcm2835_init(void)
{
    int  memfd;
    int  ok;
    FILE *fp;

    if (debug) {
        bcm2835_peripherals = (uint32_t*)BCM2835_PERI_BASE;

        bcm2835_pads = bcm2835_peripherals + BCM2835_GPIO_PADS/4;
        bcm2835_clk  = bcm2835_peripherals + BCM2835_CLOCK_BASE/4;
        bcm2835_gpio = bcm2835_peripherals + BCM2835_GPIO_BASE/4;
        bcm2835_pwm  = bcm2835_peripherals + BCM2835_GPIO_PWM/4;
        bcm2835_spi0 = bcm2835_peripherals + BCM2835_SPI0_BASE/4;
        bcm2835_bsc0 = bcm2835_peripherals + BCM2835_BSC0_BASE/4;
        bcm2835_bsc1 = bcm2835_peripherals + BCM2835_BSC1_BASE/4;
        bcm2835_st   = bcm2835_peripherals + BCM2835_ST_BASE/4;
        bcm2835_aux  = bcm2835_peripherals + BCM2835_AUX_BASE/4;
        bcm2835_spi1 = bcm2835_peripherals + BCM2835_SPI1_BASE/4;

        return 1; /* Success */
    }

    /* Figure out the base and size of the peripheral address block
    // using the device-tree. Required for RPi2/3/4, optional for RPi 1
    */
    if ((fp = fopen(BMC2835_RPI2_DT_FILENAME, "rb"))) {
        unsigned char buf[16];
        uint32_t base_address;
        uint32_t peri_size;
        if (fread(buf, 1, sizeof(buf), fp) >= 8) {
            base_address = (buf[4] << 24) |
                           (buf[5] << 16) |
                           (buf[6] << 8) |
                           (buf[7] << 0);

            peri_size = (buf[8] << 24) |
                        (buf[9] << 16) |
                        (buf[10] << 8) |
                        (buf[11] << 0);

            if (!base_address) {
                /* looks like RPI 4 */
                base_address = (buf[8] << 24) |
                               (buf[9] << 16) |
                               (buf[10] << 8) |
                               (buf[11] << 0);

                peri_size = (buf[12] << 24) |
                            (buf[13] << 16) |
                            (buf[14] << 8) |
                            (buf[15] << 0);
            }
            /* check for valid known range formats */
            if ((buf[0] == 0x7e) &&
                    (buf[1] == 0x00) &&
                    (buf[2] == 0x00) &&
                    (buf[3] == 0x00) &&
                    ((base_address == BCM2835_PERI_BASE) || (base_address == BCM2835_RPI2_PERI_BASE) || (base_address == BCM2835_RPI4_PERI_BASE))) {
                bcm2835_peripherals_base = (off_t)base_address;
                bcm2835_peripherals_size = (size_t)peri_size;
                if( base_address == BCM2835_RPI4_PERI_BASE ) {
                    pud_type_rpi4 = 1;
                }
            }

        }

        fclose(fp);
    }
    /* else we are prob on RPi 1 with BCM2835, and use the hardwired defaults */

    /* Now get ready to map the peripherals block
     * If we are not root, try for the new /dev/gpiomem interface and accept
     * the fact that we can only access GPIO
     * else try for the /dev/mem interface and get access to everything
     */
    memfd = -1;
    ok = 0;
    if (geteuid() == 0) {
        /* Open the master /dev/mem device */
        if ((memfd = rtapi_open_as_root("/dev/mem", O_RDWR | O_SYNC) ) < 0) {
            fprintf(stderr, "bcm2835_init: Unable to open /dev/mem: %s\n",
                    strerror(errno)) ;
            goto exit;
        }

        /* Base of the peripherals block is mapped to VM */
        bcm2835_peripherals = mapmem("gpio", bcm2835_peripherals_size, memfd, bcm2835_peripherals_base);
        if (bcm2835_peripherals == MAP_FAILED) goto exit;

        /* Now compute the base addresses of various peripherals,
        // which are at fixed offsets within the mapped peripherals block
        // Caution: bcm2835_peripherals is uint32_t*, so divide offsets by 4
        */
        bcm2835_gpio = bcm2835_peripherals + BCM2835_GPIO_BASE/4;
        bcm2835_pwm  = bcm2835_peripherals + BCM2835_GPIO_PWM/4;
        bcm2835_clk  = bcm2835_peripherals + BCM2835_CLOCK_BASE/4;
        bcm2835_pads = bcm2835_peripherals + BCM2835_GPIO_PADS/4;
        bcm2835_spi0 = bcm2835_peripherals + BCM2835_SPI0_BASE/4;
        bcm2835_bsc0 = bcm2835_peripherals + BCM2835_BSC0_BASE/4; /* I2C */
        bcm2835_bsc1 = bcm2835_peripherals + BCM2835_BSC1_BASE/4; /* I2C */
        bcm2835_st   = bcm2835_peripherals + BCM2835_ST_BASE/4;
        bcm2835_aux  = bcm2835_peripherals + BCM2835_AUX_BASE/4;
        bcm2835_spi1 = bcm2835_peripherals + BCM2835_SPI1_BASE/4;

        ok = 1;
    } else {
        /* Not root, try /dev/gpiomem */
        /* Open the master /dev/mem device */
        if ((memfd = open("/dev/gpiomem", O_RDWR | O_SYNC) ) < 0) {
            fprintf(stderr, "bcm2835_init: Unable to open /dev/gpiomem: %s\n",
                    strerror(errno)) ;
            goto exit;
        }

        /* Base of the peripherals block is mapped to VM */
        bcm2835_peripherals_base = 0;
        bcm2835_peripherals = mapmem("gpio", bcm2835_peripherals_size, memfd, bcm2835_peripherals_base);
        if (bcm2835_peripherals == MAP_FAILED) goto exit;
        bcm2835_gpio = bcm2835_peripherals;
        ok = 1;
    }

exit:
    if (memfd >= 0)
        close(memfd);

    if (!ok)
        bcm2835_close();

    return ok;
}

#endif

void update_freq(void *arg, long period)
{
    int i;
    data_t *data = (data_t *)arg;
    double max_ac, vel_cmd, dv, new_vel, max_freq, desired_freq;

    double error, command, feedback;
    double periodfp, periodrecip;
    float pgain, ff1gain, deadband;

    // precalculate timing constants
    periodfp = period * 0.000000001;
    periodrecip = 1.0 / periodfp;

    // calc constants related to the period of this function (LinuxCNC SERVO_THREAD)
    // only recalc constants if period changes
    if (period != old_dtns) {		// Note!! period = LinuxCNC SERVO_PERIOD
        old_dtns = period;				// get ready to detect future period changes
        dt = period * 0.000000001; 		// dt is the period of this thread, used for the position loop
        recip_dt = 1.0 / dt;			// calc the reciprocal once here, to avoid multiple divides later
    }

    // loop through generators
    for (i = 0; i < JOINTS; i++) {
        // check for scale change
        if (data->pos_scale[i] != data->old_scale[i]) {
            data->old_scale[i] = data->pos_scale[i];		// get ready to detect future scale changes
            // scale must not be 0
            if ((data->pos_scale[i] < 1e-20) && (data->pos_scale[i] > -1e-20))	// validate the new scale value
                data->pos_scale[i] = 1.0;										// value too small, divide by zero is a bad thing
            // we will need the reciprocal, and the accum is fixed point with
            //fractional bits, so we precalc some stuff
            data->scale_recip[i] = (1.0 / STEP_MASK) / data->pos_scale[i];
        }

        // calculate frequency limit
        //max_freq = PRU_BASEFREQ/(4.0); 			//limit of DDS running at 80kHz
        max_freq = PRU_BASEFREQ/(2.0);


        // check for user specified frequency limit parameter
        if (data->maxvel[i] <= 0.0) {
            // set to zero if negative
            data->maxvel[i] = 0.0;
        } else {
            // parameter is non-zero, compare to max_freq
            desired_freq = data->maxvel[i] * fabs(data->pos_scale[i]);

            if (desired_freq > max_freq) {
                // parameter is too high, limit it
                data->maxvel[i] = max_freq / fabs(data->pos_scale[i]);
            } else {
                // lower max_freq to match parameter
                max_freq = data->maxvel[i] * fabs(data->pos_scale[i]);
            }
        }

        /* set internal accel limit to its absolute max, which is
        zero to full speed in one thread period */
        max_ac = max_freq * recip_dt;

        // check for user specified accel limit parameter
        if (data->maxaccel[i] <= 0.0) {
            // set to zero if negative
            data->maxaccel[i] = 0.0;
        } else {
            // parameter is non-zero, compare to max_ac
            if ((data->maxaccel[i] * fabs(data->pos_scale[i])) > max_ac) {
                // parameter is too high, lower it
                data->maxaccel[i] = max_ac / fabs(data->pos_scale[i]);
            } else {
                // lower limit to match parameter
                max_ac = data->maxaccel[i] * fabs(data->pos_scale[i]);
            }
        }

        /* at this point, all scaling, limits, and other parameter
        changes have been handled - time for the main control */

        if (data->pos_mode[i]) {
            /* POSITION CONTROL MODE */
            // use Proportional control with feed forward (pgain, ff1gain and deadband)
            if (*(data->pgain[i]) != 0) {
                pgain = *(data->pgain[i]);
            } else {
                pgain = 1.0;
            }

            if (*(data->ff1gain[i]) != 0) {
                ff1gain = *(data->ff1gain[i]);
            } else {
                ff1gain = 1.0;
            }

            if (*(data->deadband[i]) != 0) {
                deadband = *(data->deadband[i]);
            } else {
                deadband = 1 / data->pos_scale[i];
            }

            // read the command and feedback
            command = *(data->pos_cmd[i]);
            feedback = *(data->pos_fb[i]);

            // calcuate the error
            error = command - feedback;

            // apply the deadband
            if (error > deadband) {
                error -= deadband;
            } else if (error < -deadband) {
                error += deadband;
            } else {
                error = 0;
            }

            // calcuate command and derivatives
            data->cmd_d[i] = (command - data->prev_cmd[i]) * periodrecip;

            // save old values
            data->prev_cmd[i] = command;

            // calculate the output value
            vel_cmd = pgain * error + data->cmd_d[i] * ff1gain;

        } else {
            /* VELOCITY CONTROL MODE */
            // calculate velocity command in counts/sec
            vel_cmd = *(data->vel_cmd[i]);
        }

        vel_cmd = vel_cmd * data->pos_scale[i];

        // apply frequency limit
        if (vel_cmd > max_freq) {
            vel_cmd = max_freq;
        } else if (vel_cmd < -max_freq) {
            vel_cmd = -max_freq;
        }

        // calc max change in frequency in one period
        dv = max_ac * dt;

        // apply accel limit
        if ( vel_cmd > (data->freq[i] + dv) ) {
            new_vel = data->freq[i] + dv;
        } else if ( vel_cmd < (data->freq[i] - dv) ) {
            new_vel = data->freq[i] - dv;
        } else {
            new_vel = vel_cmd;
        }

        // test for disabled stepgen
        if (*data->stepperEnable == 0) {
            // set velocity to zero
            new_vel = 0;
        }

        data->freq[i] = new_vel;				// to be sent to the PRU
        *(data->freq_cmd[i]) = data->freq[i];	// feedback to LinuxCNC
    }

}


void rio_readwrite()
{
    int i = 0;
    int bi = 0;
    double curr_pos;
    long new_stamp;
    long duration;

    new_stamp = rtapi_get_time();
    duration = new_stamp - stamp;
    stamp = new_stamp;

    // Data header
    txData.header = PRU_READ;

    if (*(data->SPIenable)) {
        if( (*(data->SPIreset) && !(data->SPIresetOld)) || *(data->SPIstatus) ) {
            // reset rising edge detected, try SPI transfer and reset OR PRU running
            int i = 0;
            // Data header
            txData.header = PRU_WRITE;

            // Joint frequency commands
            for (i = 0; i < JOINTS; i++) {
                if (joints_type[i] == JOINT_PWMDIR) {
                    txData.jointFreqCmd[i] = data->freq[i];
                } else if (joints_type[i] == JOINT_STEPPER) {
                    txData.jointFreqCmd[i] = PRU_OSC / data->freq[i] / 2;
                } else {
                    txData.jointFreqCmd[i] = PRU_OSC / data->freq[i];
                }
            }

            for (bi = 0; bi < JOINT_ENABLE_BYTES; bi++) {
                txData.jointEnable[bi] = 0;
                for (i = 0; i < JOINTS; i++) {
                    if (*(data->stepperEnable[bi * 8 + i]) == 1) {
                        txData.jointEnable[bi] |= (1 << i);
                    }
                }
            }

            // Set points
            for (i = 0; i < VARIABLE_OUTPUTS; i++) {

                float value = *(data->setPoint[i]);
                value *= *(data->setPointScale[i]);
                value += *(data->setPointOffset[i]);

                if (vout_type[i] == TYPE_VOUT_SINE) {
                    txData.setPoint[i] = PRU_OSC / value / vout_freq[i];
                } else if (vout_type[i] == TYPE_VOUT_PWMDIR) {
                    if (value > vout_max[i]) {
                        value = vout_max[i];
                    }
                    if (value < -vout_max[i]) {
                        value = -vout_max[i];
                    }
                    txData.setPoint[i] = (value) * (PRU_OSC / vout_freq[i]) / (vout_max[i]);
                } else if (vout_type[i] == TYPE_VOUT_PWM) {
                    if (value > vout_max[i]) {
                        value = vout_max[i];
                    }
                    if (value < vout_min[i]) {
                        value = vout_min[i];
                    }
                    txData.setPoint[i] = (value - vout_min[i]) * (PRU_OSC / vout_freq[i]) / (vout_max[i] - vout_min[i]);
                } else if (vout_type[i] == TYPE_VOUT_RCSERVO) {
                    txData.setPoint[i] = (value + 200 + 100) * (PRU_OSC / 200000);
                } else {
                    txData.setPoint[i] = value;
                }
            }

            // Outputs
            int byte_out = 0;
            int index_num = 0;
            for (byte_out = 0; byte_out < DIGITAL_OUTPUT_BYTES; byte_out++) {
                txData.outputs[byte_out] = 0;
                for (i = 0; i < 8; i++) {
                    if (byte_out * 8 + i < DIGITAL_OUTPUTS) {
                        if (dout_types[byte_out * 8 + i] != DTYPE_INDEX) {
                            if (*(data->outputs[byte_out * 8 + i]) == 1) {
                                txData.outputs[byte_out] |= (1 << (7-i));		// output is high
                            }
                        } else {
#ifdef INDEX_MAX
                            if (*(data->index_enable[index_num]) == 1) {
                                txData.outputs[byte_out] |= (1 << (7-i));
                            }
                            index_num++;
#endif
                        }
                    }
                }
            }

            rio_transfer();

            switch (rxData.header) {	// only process valid SPI payloads. This rejects bad payloads
            case PRU_DATA:
                // we have received a GOOD payload from the PRU
                *(data->SPIstatus) = 1;

                for (i = 0; i < JOINTS; i++) {
                    if (data->fb_scale[i] == 0.0) {
                        data->fb_scale[i] = data->pos_scale[i];
                    }

                    if (joints_fb_type[i] == JOINT_FB_ABS) {
                        *(data->pos_fb[i]) = (float)(rxData.jointFeedback[i]) / data->fb_scale[i];
                    } else {
                        accum_diff = rxData.jointFeedback[i] - old_count[i];
                        old_count[i] = rxData.jointFeedback[i];
                        accum[i] += accum_diff;
                        *(data->count[i]) = accum[i];
                        data->scale_recip[i] = data->fb_scale[i];
                        curr_pos = (double)(accum[i]);
                        *(data->pos_fb[i]) = (float)((curr_pos+0.5) / data->fb_scale[i]);
                    }
                }

                // Feedback
                for (i = 0; i < VARIABLE_INPUTS; i++) {
                    float value = rxData.processVariable[i];
                    if (vin_type[i] == TYPE_VIN_FREQ) {
                        if (value != 0) {
                            value = (float)PRU_OSC / value;
                        }
                        value += *(data->processVariableOffset[i]);
                        value *= *(data->processVariableScale[i]);
                        *(data->processVariable[i]) = value;
                        *(data->processVariableS32[i]) = (int)value;
                    } else if (vin_type[i] == TYPE_VIN_TIME) {
                        if (value != 0) {
                            value = 1000.0 / ((float)PRU_OSC / value);
                        }
                        value += *(data->processVariableOffset[i]);
                        value *= *(data->processVariableScale[i]);
                        *(data->processVariable[i]) = value;
                        *(data->processVariableS32[i]) = (int)value;
                    } else if (vin_type[i] == TYPE_VIN_SONAR) {
                        if (value != 0) {
                            value = 1000.0 / (float)PRU_OSC / 20.0 * value * 343.2;
                        }
                        value += *(data->processVariableOffset[i]);
                        value *= *(data->processVariableScale[i]);
                        *(data->processVariable[i]) = value;
                        *(data->processVariableS32[i]) = (int)value;
                    } else if (vin_type[i] == TYPE_VIN_ADC) {
                        value /= 1000.0; // to Volt
                        value += *(data->processVariableOffset[i]);
                        value *= *(data->processVariableScale[i]);
                        *(data->processVariable[i]) = value;
                        *(data->processVariableS32[i]) = (int)(value * 100); // to mV


                    } else if (vin_type[i] == TYPE_VIN_NTC) {

                        value /= 1000.0;
                        float Rt = 10.0 * value / (3.3 - value);
                        float tempK = 1.0 / (log(Rt / 10.0) / 3950.0 + 1.0 / (273.15 + 25.0));
                        float tempC = tempK - 273.15;
                        value = tempC;

                        value += *(data->processVariableOffset[i]);
                        value *= *(data->processVariableScale[i]);
                        *(data->processVariable[i]) = value;
                        *(data->processVariableS32[i]) = (int)(value);



                    } else if (vin_type[i] == TYPE_VIN_ENCODER) {
                        value += *(data->processVariableOffset[i]);
                        value /= *(data->processVariableScale[i]);
                        *(data->processVariable[i]) = value;
                        *(data->processVariableS32[i]) = (int)value;

                        // calc RPM
                        float last = *(data->processVariableExtra[i][1]);
                        *(data->processVariableExtra[i][0]) = (value - last) * (1000000000.0 / (float)duration) * 60;
                        *(data->processVariableExtra[i][1]) = value;


                    } else {
                        value += *(data->processVariableOffset[i]);
                        value *= *(data->processVariableScale[i]);
                        *(data->processVariable[i]) = value;
                        *(data->processVariableS32[i]) = (int)value;
                    }
                }

                // Inputs
                int index_num = 0;
                for (bi = 0; bi < DIGITAL_INPUT_BYTES; bi++) {
                    for (i = 0; i < 8; i++) {
                        if (bi * 8 + i < DIGITAL_INPUTS) {
                            if (din_types[bi * 8 + i] != DTYPE_INDEX) {
                                if ((rxData.inputs[bi] & (1 << (7-i))) != 0) {
                                    *(data->inputs[(bi * 8 + i) * 2]) = 1; 		// input is high
                                    *(data->inputs[(bi * 8 + i) * 2 + 1]) = 0;  // not
                                } else {
                                    *(data->inputs[(bi * 8 + i) * 2]) = 0;			// input is low
                                    *(data->inputs[(bi * 8 + i) * 2 + 1]) = 1;  // not
                                }
                            } else {
                                float ibit = 0;
                                if ((rxData.inputs[bi] & (1 << (7-i))) != 0) {
                                    ibit = 1;
                                }
#ifdef INDEX_MAX
                                if (ibit != index_enable_in[index_num]) {
                                    index_enable_in[index_num] = ibit;
                                    if (index_enable_in[index_num] == 0) {
                                        *(data->index_enable[index_num]) = 0;
                                    }
                                }
                                index_num++;
#endif
                            }
                        }
                    }
                }


                break;

            case PRU_ESTOP:
                // we have an eStop notification from the PRU
                *(data->SPIstatus) = 0;
                rtapi_print_msg(RTAPI_MSG_ERR, "An E-stop is active");

            default:
                // we have received a BAD payload from the PRU
                *(data->SPIstatus) = 0;

                rtapi_print("Bad interface payload = %x\n", rxData.header);
                for (i = 0; i < SPIBUFSIZE; i++) {
                	rtapi_print("%d\n",rxData.rxBuffer[i]);
                }
                break;
            }
        }
    } else {
        *(data->SPIstatus) = 0;
    }

    data->SPIresetOld = *(data->SPIreset);
}


void rio_transfer()
{

#ifdef TRANSPORT_UDP
    int ret;
    long t1;
    long t2;

    // Send datagram
    ret = send(udpSocket, txData.txBuffer, SPIBUFSIZE, 0);

    // Receive incoming datagram
    t1 = rtapi_get_time();
    do {
        ret = recv(udpSocket, rxData.rxBuffer, SPIBUFSIZE, 0);
        if(ret < 0) {
            rtapi_delay(READ_PCK_DELAY_NS);
        }
        t2 = rtapi_get_time();
    }
    while ((ret < 0) && ((t2 - t1) < 20*1000*1000));

    if (ret > 0) {
        errCount = 0;
    } else {
        errCount++;
        rtapi_print("Ethernet ERROR: N = %d\n", errCount);
    }

    if (errCount > 2) {
        *(data->SPIstatus) = 0;
        rtapi_print("Ethernet ERROR: %s\n", strerror(errno));
    }
#endif

#ifdef TRANSPORT_SERIAL

    uint8_t rxBufferTmp[SPIBUFSIZE];

    tcflush(serial_fd, TCIOFLUSH);
    write(serial_fd, txData.txBuffer, SPIBUFSIZE);
    tcdrain(serial_fd);
    int cnt = 0;
    int rec = 0;
    while((rec = read(serial_fd, rxBufferTmp, SPIBUFSIZE)) != SPIBUFSIZE && cnt++ < 190) {
        usleep(100);
    }
    if (rec == SPIBUFSIZE) {
        memcpy(rxData.rxBuffer, rxBufferTmp, SPIBUFSIZE);
    }

    /*
    write(serial_fd, txData.txBuffer, SPIBUFSIZE);
    read(serial_fd, rxData.rxBuffer, SPIBUFSIZE);
    */

#endif

#ifdef TRANSPORT_SPI
    int i;

    bcm2835_gpio_fsel(RPI_GPIO_P1_26, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_write(RPI_GPIO_P1_26, LOW);

    for (i = 0; i < SPIBUFSIZE; i++) {
        rxData.rxBuffer[i] = bcm2835_spi_transfer(txData.txBuffer[i]);
    }
    bcm2835_gpio_write(RPI_GPIO_P1_26, HIGH);
#endif

}

static CONTROL parse_ctrl_type(const char *ctrl)
{
    if(!ctrl || !*ctrl || *ctrl == 'p' || *ctrl == 'P') return POSITION;
    if(*ctrl == 'v' || *ctrl == 'V') return VELOCITY;
    return INVALID;
}
