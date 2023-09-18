#ifndef RIO_H
#define RIO_H

#define TRANSPORT_SPI
#define SPI_SPEED BCM2835_SPI_CLOCK_DIVIDER_256

#define JOINTS               5
#define JOINT_ENABLE_BYTES   1
#define VARIABLE_OUTPUTS     1
#define VARIABLE_INPUTS      1
#define VARIABLES            1
#define DIGITAL_OUTPUTS      12
#define DIGITAL_OUTPUT_BYTES 2
#define DIGITAL_INPUTS       21
#define DIGITAL_INPUT_BYTES  3
#define SPIBUFSIZE           31

#define PRU_DATA            0x64617461
#define PRU_READ            0x72656164
#define PRU_WRITE           0x77726974
#define PRU_ESTOP           0x65737470
#define STEPBIT             22
#define STEP_MASK           (1L<<STEPBIT)
#define STEP_OFFSET         (1L<<(STEPBIT-1))
#define PRU_BASEFREQ        100000000
#define PRU_OSC             27000000

#define TYPE_VOUT_RAW  0
#define TYPE_VOUT_PWM  1
#define TYPE_VOUT_PWMDIR  2
#define TYPE_VOUT_RCSERVO 3
#define TYPE_VOUT_SINE 4
#define TYPE_VOUT_FREQ 5
#define TYPE_VOUT_UDPOTI 6
#define TYPE_VIN_RAW  0
#define TYPE_VIN_FREQ 1
#define TYPE_VIN_TIME 2
#define TYPE_VIN_SONAR 3
#define TYPE_VIN_ADC 4
#define TYPE_VIN_ENCODER 5
#define TYPE_VIN_NTC 6
#define JOINT_FB_REL 0
#define JOINT_FB_ABS 1
#define JOINT_STEPPER 0
#define JOINT_RCSERVO 1
#define JOINT_PWMDIR  2
#define DTYPE_IO 0
#define DTYPE_INDEX 1
float vout_min[VARIABLE_OUTPUTS] = {0};
float vout_max[VARIABLE_OUTPUTS] = {10.0};
float vout_freq[VARIABLE_OUTPUTS] = {10000};
uint8_t vout_type[VARIABLE_OUTPUTS] = {TYPE_VOUT_PWM};
uint8_t vin_type[VARIABLE_INPUTS] = {TYPE_VIN_RAW};

uint8_t joints_fb_type[JOINTS] = {JOINT_FB_REL, JOINT_FB_REL, JOINT_FB_REL, JOINT_FB_REL, JOINT_FB_REL};

uint8_t joints_type[JOINTS] = {JOINT_STEPPER, JOINT_STEPPER, JOINT_STEPPER, JOINT_STEPPER, JOINT_STEPPER};

typedef union {
    struct {
        uint8_t txBuffer[SPIBUFSIZE];
    };
    struct {
        int32_t header;
        int32_t jointFreqCmd[JOINTS];
        int32_t setPoint[VARIABLE_OUTPUTS];
        uint8_t jointEnable[JOINT_ENABLE_BYTES];
        uint8_t outputs[DIGITAL_OUTPUT_BYTES];
    };
} txData_t;

typedef union
{
    struct {
        uint8_t rxBuffer[SPIBUFSIZE];
    };
    struct {
        int32_t header;
        int32_t jointFeedback[JOINTS];
        int32_t processVariable[VARIABLE_INPUTS];
        uint8_t inputs[DIGITAL_INPUT_BYTES];
    };
} rxData_t;

#endif

const char vin_names[][32] = {
    "VIN0",
};

const char vout_names[][32] = {
    "VOUT0",
};

const char din_names[][32] = {
    "DIN0",
    "DIN1",
    "DIN2",
    "DIN3",
    "DIN4",
    "DIN5",
    "DIN6",
    "DIN7",
    "DIN8",
    "DIN9",
    "DIN10",
    "DIN11",
    "DIN12",
    "DIN13",
    "DIN14",
    "DIN15",
    "DIN16",
    "DIN17",
    "DIN18",
    "DIN19",
    "DIN20",
};

const char dout_names[][32] = {
    "DOUT0",
    "DOUT1",
    "DOUT2",
    "DOUT3",
    "DOUT4",
    "DOUT5",
    "DOUT6",
    "DOUT7",
    "DOUT8",
    "DOUT9",
    "DOUT10",
    "DOUT11",
};

const char din_types[] = {
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
};

const char dout_types[] = {
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
    DTYPE_IO,
};
