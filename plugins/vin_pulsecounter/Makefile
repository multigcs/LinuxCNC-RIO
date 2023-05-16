
all: testb

testb:
	iverilog -Wall -o testb.out testb.v vin_pulsecounter.v
	vvp testb.out
	gtkwave testb.vcd

clean:
	rm -rf testb.out testb.vcd
