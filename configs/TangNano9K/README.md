# Tang Nano 9K

https://wiki.sipeed.com/hardware/en/tang/Tang-Nano-9K/Nano-9K.html

![test](https://raw.githubusercontent.com/multigcs/LinuxCNC-RIO/main/configs/TangNano9K/bob9k.jpg)
![adapter-top](https://raw.githubusercontent.com/multigcs/LinuxCNC-RIO/main/configs/TangNano9K/tangnano9k-bob-adapter2-top.png)



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
| 2 | DIN6 | 79 |
| 3 | DIN7 | 80 |
| 4 | DIN8 | 81 |
| 5 | DIN9 | 82 |
| 6 | DIN10 | 83 |
| 7 | DIN11 | 84 |
| 8 | DIN12 | 85 |
| 9 | DIN13 | 86 |
| 10 | GND | |


## Mapping: 5Axis-BOB to FPGA 

| BOB5X | FUNC | FPGA |
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
| P10 | DIN1 | 33 |
| P11 | DIN2 | 30 |
| P12 | DIN3 | 29 |
| P13 | DIN4 | 28 |
| P14 | EN | 69 |
| P15 | DIN5 | 68 |
| P16 | STP_B | 57 |
| P17 | DIR_B | 56 |
|   | LED1 | 10 |
|   | LED2 | 11 |
|   | LED3 | 13 |
|   | LED4 | 14 |
|   | LED5 | 15 |
|   | LED6 | 16 |
|   | BTN_S1 | 4 |
|   | BTN_S2 | 3 |

