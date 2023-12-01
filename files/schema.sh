#!/bin/bash
#
#

cat <<EOF | dot -Tsvg

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
