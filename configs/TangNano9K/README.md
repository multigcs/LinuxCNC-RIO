# Tang Nano 9K with 5axis-BOB

https://wiki.sipeed.com/hardware/en/tang/Tang-Nano-9K/Nano-9K.html

Install: see INSTALL.md


## BOB-Adapter SPI-Pins:

| BOB-Adapter | FUNC | FPGA-Pin |Raspberry-GPIO | Raspberry-Pin |
| --- | --- | --- | --- | --- |
| 1 | 5V |  |  | 2 |
| 2 | MOSI | 48 | GPIO10 (MOSI) | 19 |
| 3 | MISO |  49 |GPIO9 (MISO) | 21 |
| 4 | SCK |  31 |GPIO11 (SCLK) | 23 |
| 5 | CS |  32 |GPIO7 (CE1) | 26 |
| 6 | GND | | | 6 |


## BOB-Adapter Expansion-Pins:
| BOB-Adapter | FUNC | FPGA-Pin | 
| --- | --- | --- |
| 1 | OUT | 73 |
| 2 | IN | 72 |
| 3 | CLK | 71 |
| 4 | LOAD | 70 |
| 5 | 5V | |
| 6 | GND | |


## BOB-Adapter extra Input-Pins:
| BOB-Adapter | FUNC | FPGA-Pin |
| --- | --- | --- |
| 1 | 5V | |
| 2 | DIN5 | 79 |
| 3 | DIN6 | 80 |
| 4 | DIN7 | 81 |
| 5 | DIN8 | 82 |
| 6 | DIN9 | 83 |
| 7 | DIN10 | 84 |
| 8 | DIN11 | 85 |
| 9 | DIN12 | 86 |
| 10 | GND | |


## Mapping: 5Axis-BOB to FPGA 

| BOB5X | FUNC | FPGA-Pin |
| --- | --- | --- |
| P1 | PWM | 55 |
| P2 | STP_X | 54 |
| P3 | DIR_X | 53 |
| P4 | STP_Y | 51 |
| P5 | DIR_Y | 42 |
| P6 | STP_Z | 41 |
| P7 | DIR_Z | 35 |
| P8 | STP_A | 40 |
| P9 | DIR_A | 34 |
| P10 | DIN0 | 33 |
| P11 | DIN1 | 30 |
| P12 | DIN2 | 29 |
| P13 | DIN3 | 28 |
| P14 | EN | 69 |
| P15 | DIN4 | 68 |
| P16 | STP_B | 57 |
| P17 | DIR_B | 56 |


## Mapping: FPGA Onboard Components

| Component | FUNC | FPGA-Pin |
| --- | --- | --- |
| LED1 | BLINK | 10 |
| LED2 | ERROR | 11 |
| LED3 | DOUT1 | 13 |
| LED4 | DOUT2 | 14 |
| LED5 | DOUT3 | 15 |
| LED6 | DOUT4 | 16 |
| BTN_S1 | VIN1+ | 4 |
| BTN_S2 | VIN1- | 3 |


![adapter-top](https://raw.githubusercontent.com/multigcs/LinuxCNC-RIO/main/configs/TangNano9K/tangnano9k-bob-adapter2-top.png)
![test](https://raw.githubusercontent.com/multigcs/LinuxCNC-RIO/main/configs/TangNano9K/bob9k.jpg)


