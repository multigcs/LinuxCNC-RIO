#!/bin/sh
#
#

CFLAGS="-DMEM_TOTAL=0x80"
CROSS="/opt/riscv/bin/riscv32-unknown-elf-"
CROSS="riscv64-unknown-elf-"


${CROSS}cpp -P -DICEBREAKER -o firmware.lds sections.lds

${CROSS}gcc ${CFLAGS} -mabi=ilp32 -march=rv32ic -Wl,-Bstatic,-T,firmware.lds,--strip-debug -ffreestanding -nostdlib -o firmware.elf start.s firmware.c

${CROSS}objcopy -O verilog firmware.elf firmware.hex

${CROSS}objcopy -O binary firmware.elf firmware.bin

python3 progmem.py


