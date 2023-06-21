# Tang Nano 9K

https://wiki.sipeed.com/hardware/en/tang/Tang-Nano-9K/Nano-9K.html

![test](https://raw.githubusercontent.com/multigcs/LinuxCNC-RIO/main/configs/TangNano9K/bob9k.jpg)
![adapter-top](https://raw.githubusercontent.com/multigcs/LinuxCNC-RIO/main/configs/TangNano9K/tangnano9k-bob-adapter2-top.png)



## BOB-Adapter SPI-Pins:

| FPGA-Pin | BOB-Adapter | FUNC | Raspberry |
| --- | --- | --- | --- |
|  | 1 | 5V |  |
| 48 | 2 | MOSI |  |
| 49 | 3 | MISO |  |
| 31 | 4 | SCK |  |
| 32 | 5 | CS |  |
| - | 6 | GND |  |


## BOB-Adapter Expansion-Pins:
| FPGA-Pin | BOB-Adapter | FUNC |
| --- | --- | --- |
| 73 | 1 | OUT |
| 72 | 2 | IN |
| 71 | 3 | CLK |
| 70 | 4 | LOAD |
| - | 5 | 5V |
| - | 6 | GND |


## BOB-Adapter extra Input-Pins:
| FPGA-Pin | BOB-Adapter | FUNC |
| --- | --- | --- |
| - | 1 | 5V |
| 79 | 2 | DIN6 |
| 80 | 3 | DIN7 |
| 81 | 4 | DIN8 |
| 82 | 5 | DIN9 |
| 83 | 6 | DIN10 |
| 84 | 7 | DIN11 |
| 85 | 8 | DIN12 |
| 86 | 9 | DIN13 |
| - | 10 | GND |


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

