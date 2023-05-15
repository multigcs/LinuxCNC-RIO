#ifndef RIO_H
#define RIO_H

#define JOINTS               5
#define JOINT_ENABLE_BYTES   1
#define VARIABLE_OUTPUTS     2
#define VARIABLE_INPUTS      0
#define VARIABLES            2
#define DIGITAL_OUTPUTS      8
#define DIGITAL_OUTPUT_BYTES 1
#define DIGITAL_INPUTS       8
#define DIGITAL_INPUT_BYTES  1
#define SPIBUFSIZE           34

#define PRU_DATA            0x64617461
#define PRU_READ            0x72656164
#define PRU_WRITE           0x77726974
#define PRU_ESTOP           0x65737470
#define STEPBIT             22
#define STEP_MASK           (1L<<STEPBIT)
#define STEP_OFFSET         (1L<<(STEPBIT-1))
#define PRU_BASEFREQ        120000
#define PRU_OSC             100000000


#define VOUT_TYPE_PWM  0
#define VOUT_TYPE_RCSERVO 1
#define VOUT_TYPE_SINE 2
#define VOUT_TYPE_FREQ 3
float vout_min[VARIABLE_OUTPUTS] = {-100, -10};
float vout_max[VARIABLE_OUTPUTS] = {100.0, +10};
float vout_freq[VARIABLE_OUTPUTS] = {10000, 10000};
uint8_t vout_type[VARIABLE_OUTPUTS] = {VOUT_TYPE_PWM, VOUT_TYPE_PWM};

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
