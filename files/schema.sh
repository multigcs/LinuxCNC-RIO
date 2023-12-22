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

	subgraph cluster_0 {
        "FPGA" [shape=Msquare]
        "STEP/DIR" [shape=square]
        "PWM/DIR" [shape=square]
        "PWM" [shape=square]
        "GPIO" [shape=square]
        "MODBUS" [shape=square]
        "COUNTER" [shape=square]
        "SPI" [shape=square]
        "SPI/I2C/1Wire" [shape=square]

        "STEP/DIR" -> "FPGA" [dir=back]
        "PWM/DIR" -> "FPGA" [dir=back]
        "PWM" -> "FPGA" [dir=back]
        "GPIO" -> "FPGA" [dir=both]
        "MODBUS" -> "FPGA" [dir=both]
        "COUNTER" -> "FPGA"
        "SPI/I2C/1Wire" -> "FPGA" [dir=both]
        "FPGA" -> "SPI" [dir=both]
    }

    "STEPPER" -> "Stepper-Driver" -> "STEP/DIR" [dir=back]
    "UNIPOLAR" -> "ULN2803" -> "GPIO" [dir=back]
    "DC-Servo" -> "H-Bridge" -> "PWM/DIR" [dir=back]
    "RC-Servo" -> "PWM" [dir=back]

    "HY-VFD" -> "MAX485" -> "MODBUS" [dir=both]

    "Encoder\nOptical for joint feedback (closed-loop)\nmechanical for user inputs" -> "COUNTER"
    "ADC\n(tlc549c / ads1115)" -> "SPI/I2C/1Wire"
    "Sensors\n(ds18b20 / lm75)" -> "SPI/I2C/1Wire"
    "Counter\n(up/down/reset)" -> "COUNTER"
    "Digial-Input\n(switches/buttons/sensors/...)" -> "GPIO"
    "Digial-Output\n(spindle/flood/LED's/...)" -> "GPIO" [dir=back]
    "PWM-Output\n(spindle-speed/...)" -> "PWM/DIR" [dir=back]

    "extra GPIO's\n(Buttons/LED's)\n(do not use for realtime stuff)" -> "IO-Extensions\n(shiftreg/pcf8574)\n(for extra Digital-Ports)" -> "SPI/I2C/1Wire" [dir=both]

    "SPI" -> "W5500"[dir=both,color=lightgray, label=spi]
    "W5500" -> "LinuxCNC\n(RPI4/PC/Laptop)"[dir=both,color=lightgray, label=udp]
    "SPI" -> "UDP2SPI Bridge" [dir=both,color=lightgray, label=spi]
    "UDP2SPI Bridge" -> "LinuxCNC\n(RPI4/PC/Laptop)"[dir=both,color=lightgray, label=udp]

    "SPI" -> "LinuxCNC\n(RPI4/PC/Laptop)" [dir=both,color=lightgray, label=spi]

}

EOF

