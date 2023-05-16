
all: testb

testb:
	iverilog -Wall -o testb.out testb.v interface_spislave.v
	vvp testb.out

wave:
	gtkwave testb.vcd

clean:
	rm -rf testb.out testb.vcd
