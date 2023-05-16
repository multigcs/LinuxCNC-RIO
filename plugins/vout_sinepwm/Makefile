
all: testb

testb:
	iverilog -Wall -o testb.out testb.v vout_sinepwm.v
	vvp testb.out
	gtkwave testb.vcd

clean:
	rm -rf testb.out testb.vcd
