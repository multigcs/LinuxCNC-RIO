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

## Plugins:

| Type | Name | Description |
| --- | --- | --- |
| joint | [pwmdir](plugins/joint_pwmdir) | PWM Joint Output with DIR-Pin |
| joint | [rcservo](plugins/joint_rcservo) | RCSERVO Joint Output |
| joint | [stepper](plugins/joint_stepper) | Stepper Joint Output with STEP/DIR/ENABLE(optional) pins |
| vin | [frequency](plugins/vin_frequency) | Variable-Input for frequency measurement |
| vin | [pulsecounter](plugins/vin_pulsecounter) | Variable-Input for pulse counting with up to 3 pins (all optional) |
| vin | [pwmcounter](plugins/vin_pwmcounter) | Variable-Input for pulse width measurement |
| vin | [quadencoder](plugins/vin_quadencoder) | Variable-Input for Quad-Encoder (int32_t) |
| vin | [sonar](plugins/vin_sonar) | Variable-Input for distance measurement via ultrasonic sonar sensor (HC-SR04) |
| vout | [frequency](plugins/vout_frequency) | Variable-Output for frequencys |
| vout | [pwm](plugins/vout_pwm) | Variable-Output for PWM-Signals with optional DIR pin |
| vout | [sinepwm](plugins/vout_sinepwm) | Variable-Output for Sine-Waves via PWM-Signal |
| vout | [spipoti](plugins/vout_spipoti) | Variable-Output using digital poti with SPI Interface (like MCP413X/415X/423X/425X) |
| vout | [udpoti](plugins/vout_udpoti) | Variable-Output using digital poti with UpDown/Incr. Interface (like X9C104) |
| din | [bit](plugins/din_bit) | Digital Input Pin (1bit) |
| dout | [bit](plugins/dout_bit) | Digital Output Pin (1bit) |
| expansion | [shiftreg](plugins/expansion_shiftreg) | Expansion to add I/O's via shiftregister's |
| interface | [spislave](plugins/interface_spislave) | communication interface ( RPI(Master) <-SPI-> FPGA(Slave) ) |


## FPGA-Toolchain:

 https://github.com/YosysHQ/oss-cad-suite-build


## interfacing with the raspberry

* Interface: SPI

* Chipselect: CE_1

* do not reuse the chipselect pin of your SPI-Flash !!!


## test-tool

python3 Output/BOARD_NAME/Firmware/qt_spitest.py


## some hints
at the moment, you need at least configure one item of each of the following sections:
 vin, vout, din, dout, joints


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
