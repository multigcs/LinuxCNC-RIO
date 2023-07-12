# UDP2SPI Bridge

based on WT32-ETH01

## Install Firmware:

Needed: FTDI or other USB2Serial adapter

please install platformio on you system and run:

```
pio run
pio run --target upload
```


## Case:

[case-stl](wt32eth0-case.stl)
[case-scad](wt32eth0-case.scad)
![CAse](wt32eth0-case.jpg?raw=true "Case")

## Pinout:

| Signal | Pin |
| --- | --- |
| MOSI | 15 |
| MISO | 35 |
| SCLK | 14 |
| CS | 4 |

Please use this pinout for the SPI, all other combinations have problems if the FPGA is connected at boottime or while flashing

![Pinout](pinout.jpg?raw=true "Pinout")

## FTDI-Programmer:

to enter programming mode, connect IO0 to GND before switching on the power supply

| FTDI Pin | WT32-ETH01 Pin |
| --- | --- |
| RX (IO1) | TX0 |
| TX (IO3) | RX0 |
| GND | GND |
| VCC | 5V |

![jumperwires](wt32-eth01-jumperwires.jpg?raw=true "jumperwires")

