
FAMILY  := ice40
TYPE    := lp8k
PACKAGE := cm81

all: rio.bin

rio.json: interface_spislave.v vout_pwm.v quad_encoder.v joint_stepper.v joint_stepper_nf.v vin_frequency.v debouncer.v pll.v rio.v
	yosys -q -l yosys.log -p 'synth_${FAMILY} -top rio -json rio.json' interface_spislave.v vout_pwm.v quad_encoder.v joint_stepper.v joint_stepper_nf.v vin_frequency.v debouncer.v pll.v rio.v

rio.asc: rio.json pins.pcf
	nextpnr-${FAMILY} -q -l nextpnr.log --${TYPE} --package ${PACKAGE} --json rio.json --pcf pins.pcf --asc rio.asc
	@echo ""
	@grep -B 1 "%$$" nextpnr.log
	@echo ""

rio.bin: rio.asc
	icepack rio.asc rio.bin

check:
	verilator --top-module rio --lint-only -Wall *.v

clean:
	rm -rf rio.bin rio.asc rio.json yosys.log nextpnr.log

tinyprog: rio.bin
	tinyprog -p rio.bin
