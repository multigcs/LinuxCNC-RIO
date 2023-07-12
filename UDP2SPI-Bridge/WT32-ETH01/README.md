# UDP2SPI Bridge

based on WT32-ETH01

Helpfull: https://github.com/ldijkman/WT32-ETH01-LAN-8720-RJ45-

## Pinout:

| Signal | Pin |
| --- | --- |
| MOSI | 15 |
| MISO | 35 |
| SCLK | 14 |
| CS | 4 |

Please use this pinout for the SPI, all other combinations have problems if the FPGA is connected at boottime or while flashing

## FTDI-Programmer:

to enter programming mode, connect IO0 to GND before switching on the power supply

| FTDI Pin | WT32-ETH01 Pin |
| --- | --- |
| RX (IO1) | TX0 |
| TX (IO3) | RX0 |
| GND | GND |
| VCC | 5V |


