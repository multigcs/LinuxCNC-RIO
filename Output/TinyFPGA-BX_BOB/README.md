# TinyFPGA-BX_BOB

Generated Output of [configs/TinyFPGA-BX_BOB/config.json](/configs/TinyFPGA-BX_BOB/config.json)



## Build-Options:

| Name | Wert |
| --- | --- |
| Name | TinyFPGA-BX_BOB |
| Description | TinyFPGA-BX_BOB with cheap 5axis-BOB |
| Toolchain | icestorm |
| Family | ice40 |
| Type | lp8k |
| Package | cm81 |

## Files:
| Name | Wert |
| --- | --- |
| Bitstream | [rio.bin](Firmware/rio.bin) |
| LinuxCNC Components | [Components](LinuxCNC/Components/) |
| LinuxCNC ConfigSample | [ConfigSample](LinuxCNC/ConfigSamples/rio/) |

## PLL:
| Signal | Frequency |
| --- | --- |
|sysclk_in | 16.0MHz |
| sysclk | 48.0MHz |

## Pins:
| Name | Pin | Direction |
| --- | --- | --- |
| DIN0 | C2 | INPUT |
| DIN1 | B1 | INPUT |
| DIN2 | A1 | INPUT |
| DIN3 | A2 | INPUT |
| DIN4 | J4 | INPUT |
| DIN5 | D9 | INPUT |
| DIN6 | C9 | INPUT |
| DOUT0 | A6 | OUTPUT |
| DOUT1 | B6 | OUTPUT |
| DOUT2 | A7 | OUTPUT |
| ENA | G9 | OUTPUT |
| ERROR_OUT | B3 | OUTPUT |
| INTERFACE_SPI_MOSI | G6 | INPUT |
| INTERFACE_SPI_MISO | H7 | OUTPUT |
| INTERFACE_SPI_SCK | G7 | INPUT |
| INTERFACE_SPI_SSEL | G1 | INPUT |
| JOINT0_STEPPER_STP | J1 | OUTPUT |
| JOINT0_STEPPER_DIR | H1 | OUTPUT |
| JOINT1_STEPPER_STP | G2 | OUTPUT |
| JOINT1_STEPPER_DIR | E1 | OUTPUT |
| JOINT2_STEPPER_STP | E2 | OUTPUT |
| JOINT2_STEPPER_DIR | D1 | OUTPUT |
| JOINT3_STEPPER_STP | D2 | OUTPUT |
| JOINT3_STEPPER_DIR | C1 | OUTPUT |
| JOINT4_STEPPER_STP | J9 | OUTPUT |
| JOINT4_STEPPER_DIR | J3 | OUTPUT |
| sysclk_in | B2 | INPUT |
| VIN0_FREQUENCY | H9 | INPUT |
| VOUT0_PWM_PWM | H2 | OUTPUT |

## RX-Data:
| Name | Size |
| --- | --- |
| jointFreqCmd0 | 32bit |
| jointFreqCmd1 | 32bit |
| jointFreqCmd2 | 32bit |
| jointFreqCmd3 | 32bit |
| jointFreqCmd4 | 32bit |
| setPoint0 | 32bit |
| jointEnable0 | 1bit |
| jointEnable1 | 1bit |
| jointEnable2 | 1bit |
| jointEnable3 | 1bit |
| jointEnable4 | 1bit |
| DOUT0 | 1bit |
| DOUT1 | 1bit |
| DOUT2 | 1bit |

## TX-Data:
| Name | Wert |
| --- | --- |
| jointFeedback0 | 32bit |
| jointFeedback1 | 32bit |
| jointFeedback2 | 32bit |
| jointFeedback3 | 32bit |
| jointFeedback4 | 32bit |
| processVariable0 | 32bit |
| DIN0 | 1bit |
| DIN1 | 1bit |
| DIN2 | 1bit |
| DIN3 | 1bit |
| DIN4 | 1bit |
| DIN5 | 1bit |
| DIN6 | 1bit |

## Plugins:
### Modul: interface_spislave:
files: [interface_spislave.v](Firmware/interface_spislave.v) 

#### spi1
| Name | Direction |
| --- | --- |
| sysclk | --- |
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
| sysclk | --- |
| setPoint0 | from RX_DATA |
| ERROR | --- |
| VOUT0_PWM_DIR | --- |
| VOUT0_PWM_PWM | to PINS |
| VOUT0_PWM_PWM_INVERTED | to PINS |

### Modul: joint_stepper:
files: [quad_encoder.v](Firmware/quad_encoder.v) [joint_stepper.v](Firmware/joint_stepper.v) [joint_stepper_nf.v](Firmware/joint_stepper_nf.v) 

#### joint_stepper0
| Name | Direction |
| --- | --- |
| sysclk | --- |
| jointEnable0 | from RX_DATA |
| jointFreqCmd0 | from RX_DATA |
| jointFeedback0 | to TX_DATA |
| JOINT0_STEPPER_DIR | to PINS |
| JOINT0_STEPPER_STP | to PINS |

#### joint_stepper1
| Name | Direction |
| --- | --- |
| sysclk | --- |
| jointEnable1 | from RX_DATA |
| jointFreqCmd1 | from RX_DATA |
| jointFeedback1 | to TX_DATA |
| JOINT1_STEPPER_DIR | to PINS |
| JOINT1_STEPPER_DIR_INVERTED | to PINS |
| JOINT1_STEPPER_STP | to PINS |

#### joint_stepper2
| Name | Direction |
| --- | --- |
| sysclk | --- |
| jointEnable2 | from RX_DATA |
| jointFreqCmd2 | from RX_DATA |
| jointFeedback2 | to TX_DATA |
| JOINT2_STEPPER_DIR | to PINS |
| JOINT2_STEPPER_STP | to PINS |

#### joint_stepper3
| Name | Direction |
| --- | --- |
| sysclk | --- |
| jointEnable3 | from RX_DATA |
| jointFreqCmd3 | from RX_DATA |
| jointFeedback3 | to TX_DATA |
| JOINT3_STEPPER_DIR | to PINS |
| JOINT3_STEPPER_DIR_INVERTED | to PINS |
| JOINT3_STEPPER_STP | to PINS |

#### joint_stepper4
| Name | Direction |
| --- | --- |
| sysclk | --- |
| jointEnable4 | from RX_DATA |
| jointFreqCmd4 | from RX_DATA |
| jointFeedback4 | to TX_DATA |
| JOINT4_STEPPER_DIR | to PINS |
| JOINT4_STEPPER_STP | to PINS |

### Modul: vin_frequency:
files: [vin_frequency.v](Firmware/vin_frequency.v) 

#### vin_frequency0
| Name | Direction |
| --- | --- |
| sysclk | --- |
| processVariable0 | to TX_DATA |
| VIN0_FREQUENCY | from PINS |


![Flowchart](doc/flowchart.png)



