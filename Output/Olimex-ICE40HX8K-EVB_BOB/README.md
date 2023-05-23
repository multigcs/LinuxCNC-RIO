# Olimex-ICE40HX8K-EVB_BOB

Generated Output of [configs/Olimex-ICE40HX8K-EVB_BOB/config.json](/configs/Olimex-ICE40HX8K-EVB_BOB/config.json)



## Build-Options:

| Name | Wert |
| --- | --- |
| Name | Olimex-ICE40HX8K-EVB_BOB |
| Description | Olimex-ICE40HX8K-EVB with cheap 5axis-BOB |
| Toolchain | icestorm |
| Family | ice40 |
| Type | hx8k |
| Package | ct256 |

## Files:
| Name | Wert |
| --- | --- |
| Bitstream | [rio.bin](Firmware/rio.bin) |
| LinuxCNC Components | [Components](LinuxCNC/Components/) |
| LinuxCNC ConfigSample | [ConfigSample](LinuxCNC/ConfigSamples/rio/) |

## Pins:
| Name | Pin | Direction |
| --- | --- | --- |
| BLINK_LED | M12 | OUTPUT |
| DIN0 | H6 | INPUT |
| DIN1 | F2 | INPUT |
| DIN2 | H3 | INPUT |
| DIN3 | F3 | INPUT |
| DIN4 | B1 | INPUT |
| DOUT0 | F4 | OUTPUT |
| DOUT1 | D2 | OUTPUT |
| DOUT2 | G5 | OUTPUT |
| DOUT3 | D1 | OUTPUT |
| ENA | F5 | OUTPUT |
| ERROR_OUT | R16 | OUTPUT |
| INTERFACE_SPI_MOSI | P12 | INPUT |
| INTERFACE_SPI_MISO | P11 | OUTPUT |
| INTERFACE_SPI_SCK | R11 | INPUT |
| INTERFACE_SPI_SSEL | L11 | INPUT |
| JOINT0_STEPPER_STP | H1 | OUTPUT |
| JOINT0_STEPPER_DIR | G1 | OUTPUT |
| JOINT1_STEPPER_STP | J5 | OUTPUT |
| JOINT1_STEPPER_DIR | H2 | OUTPUT |
| JOINT2_STEPPER_STP | J4 | OUTPUT |
| JOINT2_STEPPER_DIR | G2 | OUTPUT |
| JOINT3_STEPPER_STP | H4 | OUTPUT |
| JOINT3_STEPPER_DIR | F1 | OUTPUT |
| JOINT4_STEPPER_STP | C2 | OUTPUT |
| JOINT4_STEPPER_DIR | C1 | OUTPUT |
| sysclk | J3 | INPUT |
| VOUT0_PWM_PWM | J2 | OUTPUT |
| VOUT1_PWM_PWM | H5 | OUTPUT |

## RX-Data:
| Name | Size |
| --- | --- |
| jointFreqCmd0 | 32bit |
| jointFreqCmd1 | 32bit |
| jointFreqCmd2 | 32bit |
| jointFreqCmd3 | 32bit |
| jointFreqCmd4 | 32bit |
| setPoint0 | 32bit |
| setPoint1 | 32bit |
| jointEnable0 | 1bit |
| jointEnable1 | 1bit |
| jointEnable2 | 1bit |
| jointEnable3 | 1bit |
| jointEnable4 | 1bit |
| DOUT0 | 1bit |
| DOUT1 | 1bit |
| DOUT2 | 1bit |
| DOUT3 | 1bit |

## TX-Data:
| Name | Wert |
| --- | --- |
| jointFeedback0 | 32bit |
| jointFeedback1 | 32bit |
| jointFeedback2 | 32bit |
| jointFeedback3 | 32bit |
| jointFeedback4 | 32bit |
| DIN0 | 1bit |
| DIN1 | 1bit |
| DIN2 | 1bit |
| DIN3 | 1bit |
| DIN4 | 1bit |

## Plugins:
### Modul: interface_spislave:
files: [interface_spislave.v](Firmware/interface_spislave.v) 

#### spi1
| Name | Direction |
| --- | --- |
| sysclk | from PINS |
| INTERFACE_SPI_SCK | from PINS |
| INTERFACE_SPI_SSEL | from PINS |
| INTERFACE_SPI_MOSI | from PINS |
| INTERFACE_SPI_MISO | to PINS |
| rx_data | from RX_DATA |
| tx_data | to TX_DATA |
| INTERFACE_TIMEOUT | --- |

### Modul: vout_pwm:
files: [vout_pwm.v](Firmware/vout_pwm.v) 

#### vout_pwm0
| Name | Direction |
| --- | --- |
| sysclk | from PINS |
| setPoint0 | from RX_DATA |
| ERROR | --- |
| VOUT0_PWM_DIR | --- |
| VOUT0_PWM_PWM | to PINS |

#### vout_pwm1
| Name | Direction |
| --- | --- |
| sysclk | from PINS |
| setPoint1 | from RX_DATA |
| ERROR | --- |
| VOUT1_PWM_DIR | --- |
| VOUT1_PWM_PWM | to PINS |

### Modul: joint_stepper:
files: [quad_encoder.v](Firmware/quad_encoder.v) [joint_stepper.v](Firmware/joint_stepper.v) [joint_stepper_nf.v](Firmware/joint_stepper_nf.v) 

#### joint_stepper0
| Name | Direction |
| --- | --- |
| sysclk | from PINS |
| jointEnable0 | from RX_DATA |
| jointFreqCmd0 | from RX_DATA |
| jointFeedback0 | to TX_DATA |
| JOINT0_STEPPER_DIR | to PINS |
| JOINT0_STEPPER_STP | to PINS |

#### joint_stepper1
| Name | Direction |
| --- | --- |
| sysclk | from PINS |
| jointEnable1 | from RX_DATA |
| jointFreqCmd1 | from RX_DATA |
| jointFeedback1 | to TX_DATA |
| JOINT1_STEPPER_DIR | to PINS |
| JOINT1_STEPPER_STP | to PINS |

#### joint_stepper2
| Name | Direction |
| --- | --- |
| sysclk | from PINS |
| jointEnable2 | from RX_DATA |
| jointFreqCmd2 | from RX_DATA |
| jointFeedback2 | to TX_DATA |
| JOINT2_STEPPER_DIR | to PINS |
| JOINT2_STEPPER_STP | to PINS |

#### joint_stepper3
| Name | Direction |
| --- | --- |
| sysclk | from PINS |
| jointEnable3 | from RX_DATA |
| jointFreqCmd3 | from RX_DATA |
| jointFeedback3 | to TX_DATA |
| JOINT3_STEPPER_DIR | to PINS |
| JOINT3_STEPPER_STP | to PINS |

#### joint_stepper4
| Name | Direction |
| --- | --- |
| sysclk | from PINS |
| jointEnable4 | from RX_DATA |
| jointFreqCmd4 | from RX_DATA |
| jointFeedback4 | to TX_DATA |
| JOINT4_STEPPER_DIR | to PINS |
| JOINT4_STEPPER_STP | to PINS |


![Flowchart](doc/flowchart.png)



