# Cyclone IV FPGA EP4CE6E22C8N Development Board USB V2


## some links

http://land-boards.com/blwiki/index.php?title=Cyclone_IV_FPGA_EP4CE6E22C8N_Development_Board_USB_V2
https://github.com/grepz/quartus_makefile_stub
https://github.com/andykarpov/radio-86rk-wxeda



## devboard pinout

```
#set_global_assignment -name FAMILY "Cyclone IV E"
#set_global_assignment -name DEVICE EP4CE6E22C8
set_global_assignment -name STRATIX_DEVICE_IO_STANDARD "3.3-V LVTTL"
# Clock and Reset switch
set_location_assignment PIN_24 -to clk
set_location_assignment PIN_89 -to n_reset
# Serial no handshake
set_location_assignment PIN_87 -to rxd
set_location_assignment PIN_86 -to txd
# PS/2
set_location_assignment PIN_99 -to ps2Clk
set_location_assignment PIN_98 -to ps2Data
# Video
set_location_assignment PIN_100 -to hSync
set_location_assignment PIN_101 -to vSync
set_location_assignment PIN_120 -to videoR0
set_location_assignment PIN_121 -to videoR1
set_location_assignment PIN_124 -to videoR2
set_location_assignment PIN_125 -to videoR3
set_location_assignment PIN_126 -to videoR4
set_location_assignment PIN_111 -to videoG0
set_location_assignment PIN_112 -to videoG1
set_location_assignment PIN_113 -to videoG2
set_location_assignment PIN_114 -to videoG3
set_location_assignment PIN_115 -to videoG4
set_location_assignment PIN_119 -to videoG5
set_location_assignment PIN_103 -to videoB0
set_location_assignment PIN_104 -to videoB1
set_location_assignment PIN_105 -to videoB2
set_location_assignment PIN_106 -to videoB3
set_location_assignment PIN_110 -to videoB4
# LEDs and Switches
set_location_assignment PIN_1 -to LED1
set_location_assignment PIN_2 -to LED2
set_location_assignment PIN_3 -to LED3
set_location_assignment PIN_144 -to LED4
set_location_assignment PIN_88 -to switch0
set_location_assignment PIN_91 -to switch1
set_location_assignment PIN_90 -to switch2
# Buzzer
set_location_assignment PIN_85 -to BUZZER
#
set_location_assignment PIN_13 -to ~ALTERA_DATA0~
set_location_assignment PIN_6 -to ~ALTERA_ASDO_DATA1~
set_location_assignment PIN_8 -to ~ALTERA_FLASH_nCE_nCSO~
set_location_assignment PIN_12 -to ~ALTERA_DCLK~
```
