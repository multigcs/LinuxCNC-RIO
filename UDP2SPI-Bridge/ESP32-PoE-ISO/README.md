# UDP2SPI Bridge

based on Olimex ESP32-PoE-ISO board

https://www.olimex.com/Products/IoT/ESP32/ESP32-POE-ISO/open-source-hardware

## Pinout:

### UEXT1:
Signal | pin | pin | Signal |
---(3V3)    | 1 | | 2  | GND(GND)  |
---(GPIO04) | 3 | | 4  | ---(GPIO36)  |
MISO(GPIO16)| 5 | | 6  | MOSI(GPIO13) |
CS(GPIO15)  | 7 | | 8  | ---(GPIO02)  |
SCLK(GPIO14)| 9 | | 10 | ---(GPIO05)  |
