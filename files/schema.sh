#!/bin/bash
#
#

cat <<EOF | dot -Tsvg > files/schema.svg

digraph {
    "json-config" -> "buildtool.py"

    "plugins" -> "buildtool.py"
    "buildtool.py" -> "Output/TARGET"

    "Output/TARGET" -> "Gateware"
    "Gateware" -> "Verilog Source-Files"
    "Gateware" -> "Pin-Definitions"
    "Gateware" -> "Makefile"

    "Verilog Source-Files" -> "Bitstream"
    "Pin-Definitions" -> "Bitstream"
    "Makefile" -> "Bitstream"
    "IceStorm" -> "Bitstream"

    "Bitstream" -> "FPGA"

    "Output/TARGET" -> "LinuxCNC"
    "LinuxCNC" -> "c-header"
    "LinuxCNC" -> "c-sources"
    "c-header" -> "HAL-Component"
    "c-sources" -> "HAL-Component"
    "halcompile" -> "HAL-Component"

    "HAL-Component" -> "RaspberryPI"

    "RaspberryPI" -> "SPI" -> "FPGA" [style=bold,color=blue]
    "FPGA" -> "SPI" -> "RaspberryPI" [style=bold,color=blue]

    "RaspberryPI" [shape=box,color=red]
    "FPGA" [shape=box,color=red]
    
    "IceStorm" [shape=box,color=green]
    "halcompile" [shape=box,color=green]
    
}

EOF

cat <<EOF | dot -Tsvg > files/overview.svg

digraph {
    rankdir=LR;

    "STEPPER" -> "STEP/DIR\nstepper-driver" -> "FPGA" [dir=back]
    "UNIPOLAR" -> "GPIO\nuln2803" -> "FPGA" [dir=back]
    "DC-Servo" -> "PWM/DIR\nh-bridge" -> "FPGA" [dir=back]
    "RC-Servo" -> "PWM" -> "FPGA" [dir=back]

    "HY-VFD" -> "MODBUS\nlevel-converter\n(MAX485)" -> "FPGA" [dir=both]

    "Encoder\nOptical for joint feedback (closed-loop)\nmechanical for user inputs" -> "FPGA"
    "ADC\n(tlc549c / ads1115)" -> "FPGA"
    "Sensors\n(ds18b20 / lm75)" -> "FPGA"
    "Counter\n(up/down/reset)" -> "FPGA"
    "Digial-Input\n(switches/buttons/sensors/...)" -> "FPGA"
    "Digial-Output\n(spindle/flood/LED's/...)" -> "FPGA" [dir=back]
    "PWM-Output\n(spindle-speed/...)" -> "FPGA" [dir=back]

    "extra GPIO's\n(Buttons/LED's)\n(do not use for realtime stuff)" -> "IO-Extensions\n(shiftreg/pcf8574)\n(for extra Digital-Ports)" -> "FPGA" [dir=both]

    "FPGA" -> "SPI" [dir=both]

    "FPGA" -> "Ethernet\n(optional)" -> "LinuxCNC\n(RPI4/PC/Laptop)"[dir=both,color=lightgray]
    "Ethernet\n(optional)" [color=lightgray]

    "SPI" -> "LinuxCNC\n(RPI4/PC/Laptop)"[dir=both]

}

EOF

