# LinuxCNC-RIO

RealtimeIO for LinuxCNC based on an FPGA

* no Soft-Core
* logic only
* no jitter
* fast and small
* communication via SPI (with Raspberry PI 4)
* generated verilog-code / setup via json files (free pin-selection)
* using free FPGA-Toolchain

!! work in progress / untested on real machines !!

## FPGA-Toolchain:

 https://github.com/YosysHQ/oss-cad-suite-build


## Structure:

buildtool.py plugins:  this are python scripts to generates the verilog files from a configuration

configs: here are the config files for a specific setup (Target-FPGA / Pins)

Output: the generated files per config


## Demo-Video on TinyFPGA-BX board:

https://www.youtube.com/shorts/0nTmo4afwWs


## TinyFPGA-BX board with 5axis BOB:

![test](https://raw.githubusercontent.com/multigcs/LinuxCNC-RIO/main/files/4x.jpg)


