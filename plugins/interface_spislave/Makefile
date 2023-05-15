
all: testb

testb:
	iverilog -Wall -o testb.out testb.v spi_slave.v
	vvp testb.out

wave:
	gtkwave testb.vcd

clean:
	rm -rf testb.out testb.vcd
