
all: testb

testb:
	iverilog -Wall -o testb.out testb.v pwm_counter.v
	vvp testb.out
	gtkwave testb.vcd

clean:
	rm -rf testb.out testb.vcd
