
all: testb

testb:
	iverilog -Wall -o testb.out testb.v joint_rcservo.v
	vvp testb.out
	gtkwave testb.vcd

clean:
	rm -rf testb.out testb.vcd
