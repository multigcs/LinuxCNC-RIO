# LinuxCNC-RIO

RealtimeIO for LinuxCNC based on an FPGA

* no Soft-Core
* logic only
* no jitter
* fast and small
* communication via SPI (with Raspberry PI 4 or Ethernet-Bridge)
* generated verilog-code / setup via json files (free pin-selection)
* using free FPGA-Toolchain
* tested on ICE40UP5K, ICE40LP8K, ICE40HX8K, ECP5 and TangNano9K boards

![tango](https://raw.githubusercontent.com/multigcs/LinuxCNC-RIO/main/files/tango.jpg)


## Sample-Configs:
| Name | Description |
| --- | --- |
| [TangNano9K](configs/TangNano9K) | Tang Nano 9K with 5axis-BOB |
| [Tango-Board](configs/Tangoboard) | Tango-Board with Tang Nano 9K |
| [Olimex-ICE40HX8K-EVB_BOB](configs/Olimex-ICE40HX8K-EVB_BOB) | Olimex ICE40HX8K-EVB with 5axis-BOB |
| [TinyFPGA-BX_BOB](configs/TinyFPGA-BX_BOB) | TinyFPGA-BX with 5axis-BOB |
| [ICEBreakerV1.0e](configs/ICEBreakerV1.0e) | ICEBreakerV1.0e tests |
| [Lattice-iCE40HX8K_BOB](configs/Lattice-iCE40HX8K_BOB) | Lattice  iCE40HX8K with custom bob |
| [Colorlight5A-75E](configs/Colorlight5A-75E) | Colorlight5A-75E tests |
| [Alhambra-II](configs/Alhambra-II) | Alhambra II FPGA board with 3 Axis SPI |


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

for the TangNano9K, you can also using the Gowin-IDE or Gowin-Shell (it's faster)


## interfacing with the raspberry

* Interface: SPI

* Chipselect: CE_1

* do not reuse the chipselect pin of your SPI-Flash !!!

## interfacing via Ethernet

you can also use UDP2SPI bridge to communicate via Ethernet (UDP)

* [WT32-ETH01](UDP2SPI-Bridge/WT32-ETH01)

* [ESP32-PoE-ISO](UDP2SPI-Bridge/ESP32-PoE-ISO)


## test-tool
if you want to test the connection without LinuxCNC, you can use
the python test-tool:

```
python3 Output/BOARD_NAME/Firmware/qt_spitest.py [IP]
```


## some hints
at the moment, you need at least configure one item of each of the following sections:
 vin, vout, din, dout, joints


## buildtool

you can select a config via make argument:

```
make CONFIG=configs/TinyFPGA-BX_BOB/config.json build
```

## Structure:

* buildtool.py plugins:  python scripts to generates the verilog files from a configuration

* configs: here are the config files for a specific setup (Target-FPGA / Pins)

* Output: the generated files per config


## some demo videos

### LinuxCNC-RIO with TinyFPGA-BX and 5Axis BOB - ATC-Test
https://www.youtube.com/shorts/G5V5OM_ORsk

### linuxcnc with tinyfpga-bx
https://www.youtube.com/shorts/0nTmo4afwWs

### Mini Closed-Loop DC-Servo on LinuxCNC-RIO
https://www.youtube.com/shorts/0cOvUS33U_s

### Linuxcnc RIO with ICEBreaker FPGA
https://www.youtube.com/watch?v=58RNJSGD0qs

### LinuxCNC-RIO mixed joint types (on TangNano9K - FPGA)
https://www.youtube.com/shorts/ZfTr1BNUK_0

### LinuxCNC-RIO with TinyFPGA-BX and 5Axis BOB
https://www.youtube.com/watch?v=urRHtw4bcsI

### LinuxCNC with ICE40 for stepgen
https://www.youtube.com/shorts/m4zXuHERiFU


---
Thanks to the https://github.com/scottalford75/Remora Project, i'm using a modified version of it's Linux-Component
