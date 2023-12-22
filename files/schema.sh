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

        "FPGA" -> "STEP/DIR" [dir=forward]
        "FPGA" -> "PWM/DIR" [dir=forward]
        "FPGA" -> "PWM" [dir=forward]
        "FPGA" -> "GPIO" [dir=both]
        "FPGA" -> "MODBUS" [dir=both]
        "FPGA" -> "COUNTER" [dir=back]
        "FPGA" -> "SPI/I2C/1Wire" [dir=both]
        "SPI" -> "FPGA" [dir=both]
    }

    "STEP/DIR" -> "Stepper-Driver" -> "STEPPER" [dir=forward]
    "GPIO" -> "ULN2803" -> "UNIPOLAR" [dir=forward]
    "PWM/DIR" -> "H-Bridge" -> "DC-Servo" [dir=forward]
    "PWM" -> "RC-Servo" [dir=forward]

    "MODBUS" -> "MAX485" -> "HY-VFD" [dir=both]

    "COUNTER" -> "Encoder\nOptical for joint feedback (closed-loop)\nmechanical for user inputs" [dir=back]
    "SPI/I2C/1Wire" -> "ADC\n(tlc549c / ads1115)" [dir=back]
    "SPI/I2C/1Wire" -> "Sensors\n(ds18b20 / lm75)" [dir=back]
    "COUNTER" -> "Counter\n(up/down/reset)" [dir=back]
    "GPIO" -> "Digial-Input\n(switches/buttons/sensors/...)" [dir=back]
    "GPIO" -> "Digial-Output\n(spindle/flood/LED's/...)" [dir=forward]
    "PWM/DIR" -> "PWM-Output\n(spindle-speed/...)" [dir=forward]

    "SPI/I2C/1Wire" -> "IO-Extensions\n(shiftreg/pcf8574)\n(for extra Digital-Ports)" -> "extra GPIO's\n(Buttons/LED's)\n(do not use for realtime stuff)" [dir=both]

    "W5500" -> "SPI" [dir=both,color=lightgray, label=spi]
    "LinuxCNC\n(RPI4/PC/Laptop)" -> "W5500" [dir=both,color=lightgray, label=udp]
    "UDP2SPI Bridge" -> "SPI" [dir=both,color=lightgray, label=spi]
    "LinuxCNC\n(RPI4/PC/Laptop)" -> "UDP2SPI Bridge" [dir=both,color=lightgray, label=udp]
    "LinuxCNC\n(RPI4/PC/Laptop)" -> "SPI" [dir=both,color=lightgray, label=spi]

}

EOF

