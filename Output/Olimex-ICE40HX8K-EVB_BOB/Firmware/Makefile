
FAMILY  := ice40
TYPE    := hx8k
PACKAGE := ct256

all: rio.bin

rio.json: vin_quadencoder.v interface_spislave.v expansion_shiftreg.v vout_pwm.v vin_pulsecounter.v vout_frequency.v vin_pwmcounter.v quad_encoder.v joint_stepper.v joint_stepper_nf.v vin_sonar.v vin_frequency.v joint_rcservo.v vout_sinepwm.v debouncer.v blink.v rio.v
	yosys -q -l yosys.log -p 'synth_${FAMILY} -top rio -json rio.json' vin_quadencoder.v interface_spislave.v expansion_shiftreg.v vout_pwm.v vin_pulsecounter.v vout_frequency.v vin_pwmcounter.v quad_encoder.v joint_stepper.v joint_stepper_nf.v vin_sonar.v vin_frequency.v joint_rcservo.v vout_sinepwm.v debouncer.v blink.v rio.v

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
