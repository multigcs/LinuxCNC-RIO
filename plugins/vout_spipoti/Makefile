
all: testb

testb:
	iverilog -Wall -o testb.out testb.v vout_spipoti.v
	vvp testb.out
	#gtkwave testb.vcd
	gtkwave test.gtkw

clean:
	rm -rf testb.out testb.vcd
