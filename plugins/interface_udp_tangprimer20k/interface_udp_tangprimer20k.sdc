
create_clock -name sysclk -period 37.037 -waveform {0 18.518} [get_ports {sysclk}]
create_clock -name clk50 -period 20 -waveform {0 10} [get_ports {netrmii_clk50m}]
create_clock -name clk1 -period 1000 -waveform {0 500} [get_nets {netrmii_mdc_d}]
set_false_path -from [get_clocks {clk1}] -to [get_clocks {clk50}] 
set_false_path -from [get_clocks {clk50}] -to [get_clocks {clk1}] 
