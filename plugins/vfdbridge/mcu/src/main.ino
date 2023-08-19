
#include <Crc16.h>
#include <SoftwareSerial.h>
#include <Wire.h>

#define I2C_DEV_ADDR  64

#define	FUNCTION_READ			0x01
#define	FUNCTION_WRITE			0x02
#define	WRITE_CONTROL_DATA		0x03
#define	READ_CONTROL_STATUS		0x04
#define	WRITE_FREQ_DATA			0x05
#define	LOOP_TEST				0x08
#define	FUNCTION_PD005  		5
#define	FUNCTION_PD011  		11
#define	FUNCTION_PD144  		144
#define CONTROL_Run_Fwd		0x01
#define CONTROL_Run_Rev		0x11
#define CONTROL_Stop		0x08
#define CONTROL_Run			0x01
#define CONTROL_Jog			0x02
#define CONTROL_Command_rf	0x04
#define CONTROL_Running		0x08
#define CONTROL_Jogging		0x10
#define CONTROL_Running_rf	0x20
#define CONTROL_Bracking	0x40
#define CONTROL_Track_Start	0x80

SoftwareSerial myserial(16, 17); // RX, TX
Crc16 crc; 

byte spindle_start_fwd[] = { 0x01, WRITE_CONTROL_DATA, 0x01, CONTROL_Run_Fwd };
byte spindle_start_rev[] = { 0x01, WRITE_CONTROL_DATA, 0x01, CONTROL_Run_Rev };
byte spindle_stop[] =  { 0x01, WRITE_CONTROL_DATA, 0x01, CONTROL_Stop };
byte spindle_speed[] = { 0x01, WRITE_FREQ_DATA, 0x02, 0x0, 0x0 };
byte spindle_PD005[] = { 0x01, FUNCTION_READ, 0x03, 5, 0x00, 0x00 };
byte spindle_PD011[] = { 0x01, FUNCTION_READ, 0x03, 11, 0x00, 0x00 };
byte spindle_PD144[] = { 0x01, FUNCTION_READ, 0x03, 144, 0x00, 0x00 };
byte spindle_status_frq_set[] = { 0x01, READ_CONTROL_STATUS, 0x03, 0x00, 0x00, 0x00 };
byte spindle_status_frq_get[] = { 0x01, READ_CONTROL_STATUS, 0x03, 0x01, 0x00, 0x00 };
byte spindle_status_ampere[] = { 0x01, READ_CONTROL_STATUS, 0x03, 0x02, 0x00, 0x00 };
byte spindle_status_rpm[] = { 0x01, READ_CONTROL_STATUS, 0x03, 0x03, 0x00, 0x00 };
byte spindle_status_dc_volt[] = { 0x01, READ_CONTROL_STATUS, 0x03, 0x04, 0x00, 0x00 };
byte spindle_status_ac_volt[] = { 0x01, READ_CONTROL_STATUS, 0x03, 0x05, 0x00, 0x00 };
byte spindle_status_condition[] = { 0x01, READ_CONTROL_STATUS, 0x03, 0x06, 0x00, 0x00 };
byte spindle_status_temp[] = { 0x01, READ_CONTROL_STATUS, 0x03, 0x07, 0x00, 0x00 };
uint16_t maxFrequency = 0;
uint16_t minFrequency = 0;
uint16_t maxRpmAt50Hz = 0;
uint16_t min_rpm = 0;
uint16_t max_rpm = 0;
uint16_t rpm = 6000;
uint16_t frq_set = 0;
uint16_t frq_get = 0;
uint16_t ampere = 0;
uint16_t srpm = 0;
uint16_t dc_volt = 0;
uint16_t ac_volt = 0;
uint16_t condition = 0;
uint16_t temp = 0;
uint8_t waitflag = 0;
int32_t new_speed = 0;
int32_t last_speed = 0;
uint16_t stat_n = 0;
uint16_t stat_counter = 0;
int32_t set_speed = 0;


void onRequest(){
    Wire.write((srpm) & 0xFF);
    Wire.write((srpm>>8) & 0xFF);
    Wire.write((srpm>>16) & 0xFF);
    Wire.write((srpm>>24) & 0xFF);
}

void onReceive(int len){
    int32_t val = 0;
    while (Wire.available()) {
        val = val<<8;
        val += Wire.read();
    }
    if (val > -30000 && val < 30000) {
        new_speed = val;
    }
}

void setup() {
    Serial.begin(115200);
    myserial.begin(9600);
    pinMode(18, OUTPUT);
    digitalWrite(18, LOW);

    delay(1000);
    Serial.println("vfdbridge controller");

    Wire.onReceive(onReceive);
    Wire.onRequest(onRequest);
    while (Wire.begin((uint8_t)I2C_DEV_ADDR) == 0) {
        Serial.println("I2C: error: retry...");
        delay(200);
    }
    Serial.println("I2C: ok");

}

void send_msg(byte *data, byte dlen) {
    unsigned short crcsum;
    crcsum = crc.Modbus(data, 0, dlen);
    digitalWrite(18, HIGH);
    delay(2);
    byte i;
    for(byte i = 0; i < dlen; i++) {
        myserial.write(data[i]);
    }
    byte cs1 = (crcsum>>8) & 0xFF;
    byte cs2 = crcsum & 0xFF;
    myserial.write(cs2);
    myserial.write(cs1);
    delay(2);
    digitalWrite(18, LOW);
    delay(50);
    rec_msg();
}


void rec_msg() {
    byte rec_n = 0;
    byte rec[255];
    //Serial.print("rec:");
    while (myserial.available() > 0) {
        byte incomingByte = myserial.read();
        rec[rec_n] = incomingByte;
        // Serial.print(" 0x");
        // Serial.print(incomingByte, HEX);
        rec_n++;
    }
    // Serial.println("");
    //Serial.print("rec_len: ");
    //Serial.println(rec_n);

    if (rec[1] == READ_CONTROL_STATUS && rec[2] == 0x03) {
        uint16_t value = (rec[4] << 8) | rec[5];
        if (rec[3] == 0x00) {
            frq_set = value;
        } else if (rec[3] == 0x01) {
            frq_get = value;
        } else if (rec[3] == 0x02) {
            ampere = value;
        } else if (rec[3] == 0x03) {
            srpm = value;
        } else if (rec[3] == 0x04) {
            dc_volt = value;
        } else if (rec[3] == 0x05) {
            ac_volt = value;
        } else if (rec[3] == 0x06) {
            condition = value;
        } else if (rec[3] == 0x07) {
            temp = value;
        }

    } else if (rec[1] == FUNCTION_READ && rec[2] == 0x03) {
        uint16_t value = (rec[4] << 8) | rec[5];
        if (rec[3] == FUNCTION_PD005) {
            maxFrequency = value;
        } else if (rec[3] == FUNCTION_PD011) {
            minFrequency = value;
        } else if (rec[3] == FUNCTION_PD144) {
            maxRpmAt50Hz = value;
        }

        if (minFrequency > maxFrequency) {
            minFrequency = maxFrequency;
        }
        min_rpm = uint32_t(minFrequency) * uint32_t(maxRpmAt50Hz) / 5000;
        max_rpm = uint32_t(maxFrequency) * uint32_t(maxRpmAt50Hz) / 5000;
    }
}


void loop() {
    if (stat_counter == 3) {
        stat_counter = 0;
        if (stat_n == 1) {
            send_msg(spindle_PD005, sizeof(spindle_PD005));
        } else if (stat_n == 2) {
            send_msg(spindle_PD011, sizeof(spindle_PD011));
        } else if (stat_n == 3) {
            send_msg(spindle_PD144, sizeof(spindle_PD144));
        } else if (stat_n == 4) {
            send_msg(spindle_status_ampere, sizeof(spindle_status_ampere));
        } else if (stat_n == 5) {
            send_msg(spindle_status_rpm, sizeof(spindle_status_rpm));
        } else if (stat_n == 6) {
            send_msg(spindle_status_frq_set, sizeof(spindle_status_frq_set));
        } else if (stat_n == 7) {
            send_msg(spindle_status_frq_get, sizeof(spindle_status_frq_get));
        } else if (stat_n == 8) {
            send_msg(spindle_status_ac_volt, sizeof(spindle_status_ac_volt));
        } else if (stat_n == 9) {
            send_msg(spindle_status_dc_volt, sizeof(spindle_status_dc_volt));
        } else if (stat_n == 10) {
            send_msg(spindle_status_condition, sizeof(spindle_status_condition));
        } else if (stat_n == 11) {
            send_msg(spindle_status_temp, sizeof(spindle_status_temp));
        } else {
            stat_n = 0;
        }
        stat_n++;
    } else {
        send_msg(spindle_status_rpm, sizeof(spindle_status_rpm));
    }
    stat_counter++;

    if (maxRpmAt50Hz > 0) {
        if (new_speed != last_speed) {
            last_speed = new_speed;
            set_speed = new_speed;
            if (set_speed == 0) {
                Serial.println("MODBUS: stop spindle");
                send_msg(spindle_stop, sizeof(spindle_stop));
                send_msg(spindle_stop, sizeof(spindle_stop));
                send_msg(spindle_stop, sizeof(spindle_stop));
                send_msg(spindle_stop, sizeof(spindle_stop));
            } else {
                uint8_t dir = 0;
                Serial.print("MODBUS: set spindle speed: ");
                Serial.println(set_speed);

                if (set_speed < 0) {
                    dir = 1;
                    set_speed *= -1;
                }
                if (set_speed >= max_rpm) {
                    set_speed = max_rpm;
                } else if (set_speed <= min_rpm) {
                    set_speed = min_rpm;
                }
                rpm = (uint16_t)set_speed;
                uint16_t value = rpm * 5000 / maxRpmAt50Hz;
                spindle_speed[3] = (value >> 8) & 0xFF;
                spindle_speed[4] = (value & 0xFF);

                send_msg(spindle_speed, sizeof(spindle_speed));
                send_msg(spindle_speed, sizeof(spindle_speed));
                send_msg(spindle_speed, sizeof(spindle_speed));
                send_msg(spindle_speed, sizeof(spindle_speed));
                if (dir == 0) {
                    send_msg(spindle_start_fwd, sizeof(spindle_start_fwd));
                    send_msg(spindle_start_fwd, sizeof(spindle_start_fwd));
                    send_msg(spindle_start_fwd, sizeof(spindle_start_fwd));
                    send_msg(spindle_start_fwd, sizeof(spindle_start_fwd));
                } else {
                    send_msg(spindle_start_rev, sizeof(spindle_start_rev));
                    send_msg(spindle_start_rev, sizeof(spindle_start_rev));
                    send_msg(spindle_start_rev, sizeof(spindle_start_rev));
                    send_msg(spindle_start_rev, sizeof(spindle_start_rev));
                }
            }
        }
    } else {
        Serial.println("MODBUS: wait for setup data..");
    }
}
