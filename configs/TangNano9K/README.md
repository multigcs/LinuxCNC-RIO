# Tang Nano 9K

https://wiki.sipeed.com/hardware/en/tang/Tang-Nano-9K/Nano-9K.html

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
| P10 | DIN1 | 33 |
| P11 | DIN2 | 30 |
| P12 | DIN3 | 29 |
| P13 | DIN4 | 28 |
| P14 | EN | 69 |
| P15 | DIN5 | 68 |
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


## HowTo:

get the Sources:
```
git clone https://github.com/multigcs/LinuxCNC-RIO
cd LinuxCNC-RIO
```

### Generate the Project-Files

first you need to install the oss-cad-suite: https://github.com/YosysHQ/oss-cad-suite-build

then you can generate all needed files:
```
make CONFIG=configs/TangNano9K/config.json build
```

after that, you have a new folder named Output/TangNano9K/ with all needed sources and sample configs

#### build and load the FPGA-Bitstream

connect the TangNano9K board to your USB-Port and run:
```
cd Output/TangNano9K/Firmware
make all load
```
this will need some time

#### compile and install the hal-component

please copy the folder Output/TangNano9K/LinuxCNC/Components to your target system where LinuxCNC is running,
then you can compile and install the component:

```
halcompile --install  Output/TangNano9K/LinuxCNC/Components/rio.c
```

#### sample config for LinuxCNC

there are also a sample configuration in Output/TangNano9K/LinuxCNC/ConfigSamples/rio/

you can copy this folder to your LinuxCNC machine and start it:

```
linuxcnc Output/TangNano9K/LinuxCNC/ConfigSamples/rio/rio.ini
```



### Connection to the Raspberry-PI

you can use a Raspberry-PI 4 with direct SPI connection to the FPGA-Board,
you can find the pinout above (BOB-Adapter SPI-Pins)


### Build and Flash the optional Ethernet-Board

https://www.olimex.com/Products/IoT/ESP32/ESP32-POE-ISO/open-source-hardware

first you have to install the PlatformIO Core: https://platformio.org/install

then go into Folder: UDP2SPI-Bridge/ESP32-PoE-ISO and run the build process:

```
cd UDP2SPI-Bridge/ESP32-PoE-ISO
make build
```

then connect the Ethernet-Board to your USB and flash the Firmware:

```
make upload
```














