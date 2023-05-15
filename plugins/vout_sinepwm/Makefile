
all: testb

testb:
	iverilog -Wall -o testb.out testb.v sine_pwm.v
	vvp testb.out
	gtkwave testb.vcd

clean:
	rm -rf testb.out testb.vcd
