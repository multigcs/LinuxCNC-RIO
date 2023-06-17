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
