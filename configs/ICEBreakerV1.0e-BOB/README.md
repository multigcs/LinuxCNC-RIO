# ICEBreakerV1.0e with 5axis-BOB

https://github.com/icebreaker-fpga/icebreaker

## flash command
sudo openFPGALoader -b ice40_generic rio.bin -f

## ICEBreaker SPI-Pins:

| PMOD2 | FUNC | FPGA-Pin |Raspberry-GPIO | Raspberry-Pin |
| --- | --- | --- | --- | --- |
| 1 | MOSI | 27 | GPIO10 (MOSI) | 19 |
| 2 | MISO |  25 |GPIO9 (MISO) | 21 |
| 3 | SCK |  21 |GPIO11 (SCLK) | 23 |
| 4 | CS |  19 |GPIO7 (CE1) | 26 |
| 5 | GND | | | 6 |
| 6 | 5V |  |  | 2 |


## Mapping: 5Axis-BOB to FPGA 

| BOB5X | FUNC | FPGA-Pin |
| --- | --- | --- |
| P1 | PWM | 4 |
| P2 | STP_X | 2 |
| P3 | DIR_X | 47 |
| P4 | STP_Y | 45 |
| P5 | DIR_Y | 28 |
| P6 | STP_Z | 32 |
| P7 | DIR_Z | 36 |
| P8 | STP_A | 42 |
| P9 | DIR_A | 43 |
| P10 | DIN1 | 38 |
| P11 | DIN2 | 34 |
| P12 | DIN3 | 31 |
| P13 | DIN4 | - |
| P14 | EN | 3 |
| P15 | DIN5 | 48 |
| P16 | STP_B | 46 |
| P17 | DIR_B | 44 |


## ICEBreaker Expansion-Pins:
| PMOD2 | FUNC | FPGA-Pin | 
| --- | --- | --- |
| 7 | OUT | 26 |
| 8 | IN | 23 |
| 9 | CLK | 20 |
| 10 | LOAD | 18 |
| 11 | 3.3V | |
| 12 | GND | |

