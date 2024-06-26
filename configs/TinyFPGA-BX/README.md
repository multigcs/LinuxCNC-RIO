# TinyFPGA-BX with 5axis-BOB

https://tinyfpga.com/

https://github.com/tinyfpga/TinyFPGA-BX/tree/master/board

![test](https://raw.githubusercontent.com/multigcs/LinuxCNC-RIO/main/configs/TinyFPGA-BX_BOB/tinybx-bob.jpg)

![test](https://raw.githubusercontent.com/multigcs/LinuxCNC-RIO/main/configs/TinyFPGA-BX_BOB/bob5.png)

### LinuxCNC-RIO with TinyFPGA-BX and 5Axis BOB - ATC-Test
[![LinuxCNC-RIO with TinyFPGA-BX and 5Axis BOB - ATC-Test](https://img.youtube.com/vi/G5V5OM_ORsk/0.jpg)](https://www.youtube.com/shorts/G5V5OM_ORsk "LinuxCNC-RIO with TinyFPGA-BX and 5Axis BOB - ATC-Test")

### linuxcnc with tinyfpga-bx
[![linuxcnc with tinyfpga-bx](https://img.youtube.com/vi/0nTmo4afwWs/0.jpg)](https://www.youtube.com/shorts/0nTmo4afwWs "linuxcnc with tinyfpga-bx")

### LinuxCNC-RIO with TinyFPGA-BX and 5Axis BOB
[![LinuxCNC-RIO with TinyFPGA-BX and 5Axis BOB](https://img.youtube.com/vi/urRHtw4bcsI/0.jpg)](https://www.youtube.com/watch?v=urRHtw4bcsI "LinuxCNC-RIO with TinyFPGA-BX and 5Axis BOB")

# Pinouts:
```
# Left side of board
set_io --warn-no-port PIN_1 A2
set_io --warn-no-port PIN_2 A1
set_io --warn-no-port PIN_3 B1
set_io --warn-no-port PIN_4 C2
set_io --warn-no-port PIN_5 C1
set_io --warn-no-port PIN_6 D2
set_io --warn-no-port PIN_7 D1
set_io --warn-no-port PIN_8 E2
set_io --warn-no-port PIN_9 E1
set_io --warn-no-port PIN_10 G2
set_io --warn-no-port PIN_11 H1
set_io --warn-no-port PIN_12 J1
set_io --warn-no-port PIN_13 H2

# Right side of board
set_io --warn-no-port PIN_14 H9
set_io --warn-no-port PIN_15 D9
set_io --warn-no-port PIN_16 D8
set_io --warn-no-port PIN_17 C9
set_io --warn-no-port PIN_18 A9
set_io --warn-no-port PIN_19 B8
set_io --warn-no-port PIN_20 A8
set_io --warn-no-port PIN_21 B7
set_io --warn-no-port PIN_22 A7
set_io --warn-no-port PIN_23 B6
set_io --warn-no-port PIN_24 A6

# SPI flash interface on bottom of board
set_io --warn-no-port SPI_SS F7
set_io --warn-no-port SPI_SCK G7
set_io --warn-no-port SPI_IO0 G6
set_io --warn-no-port SPI_IO1 H7
set_io --warn-no-port SPI_IO2 H4
set_io --warn-no-port SPI_IO3 J8

# General purpose pins on bottom of board
set_io --warn-no-port PIN_25 G1
set_io --warn-no-port PIN_26 J3
set_io --warn-no-port PIN_27 J4
set_io --warn-no-port PIN_28 G9
set_io --warn-no-port PIN_29 J9
set_io --warn-no-port PIN_30 E8
set_io --warn-no-port PIN_31 J2

# LED
set_io --warn-no-port LED B3

# USB
set_io --warn-no-port USBP B4
set_io --warn-no-port USBN A4
set_io --warn-no-port USBPU A3

# 16MHz clock
set_io --warn-no-port CLK B2 # input

```


