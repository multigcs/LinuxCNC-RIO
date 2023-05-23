# LinuxCNC-RIO

RealtimeIO for LinuxCNC based on an FPGA

* no Soft-Core
* logic only
* no jitter
* fast and small
* communication via SPI (with Raspberry PI 4)
* generated verilog-code / setup via json files (free pin-selection)
* using free FPGA-Toolchain

!! work in progress !!

## FPGA-Toolchain:

 https://github.com/YosysHQ/oss-cad-suite-build


## interfacing with the raspberry

* Interface: SPI

* Chipselect: CE_1

* do not reuse the chipselect pin of your SPI-Flash !!!


## test-tool

python3 Output/BOARD_NAME/Firmware/qt_spitest.py


## buildtool

you can select a config via make argument:

```
make CONFIG=configs/TinyFPGA-BX_BOB/config.json build
```



## Structure:

buildtool.py plugins:  this are python scripts to generates the verilog files from a configuration

configs: here are the config files for a specific setup (Target-FPGA / Pins)

Output: the generated files per config


## Demo-Video on TinyFPGA-BX board:

https://youtube.com/shorts/G5V5OM_ORsk

https://youtube.com/shorts/0nTmo4afwWs


## TinyFPGA-BX board with 5axis BOB:

![test](https://raw.githubusercontent.com/multigcs/LinuxCNC-RIO/main/files/4x.jpg)
![test](https://raw.githubusercontent.com/multigcs/LinuxCNC-RIO/main/files/schema.svg)


Thanks to the https://github.com/scottalford75/Remora Project, i'm using a modified version of it's Linux-Component
