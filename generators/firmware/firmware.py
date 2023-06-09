
import sys
import os

def generate(project):
    print("generating firmware")

    top_arguments = []

    for pname in sorted(list(project['pinlists'])):
        pins = project['pinlists'][pname]
        for pin in pins:
            if pin[1].startswith("EXPANSION"):
                continue
            top_arguments.append(f"{pin[2].lower()} {pin[0]}")

    top_data = []
    top_data.append("/*")
    top_data.append(f"    ######### {project['jdata']['name']} #########")
    top_data.append("*/")
    top_data.append("")

    # general verilog-files
    project['verilog_files'].append("debouncer.v")
    os.system(f"cp -a generators/firmware/debouncer.v* {project['SOURCE_PATH']}/debouncer.v")

    if project['osc_clock']:
        if project['jdata']['family'] == "ecp5":
            os.system(
                f"ecppll -f '{project['SOURCE_PATH']}/pll.v' -i {float(project['osc_clock']) / 1000000} -o {float(project['jdata']['clock']['speed']) / 1000000}"
            )
        elif project['jdata']['type'] == "up5k":
            os.system(
                f"icepll -p -m -f '{project['SOURCE_PATH']}/pll.v' -i {float(project['osc_clock']) / 1000000} -o {float(project['jdata']['clock']['speed']) / 1000000}"
            )

        elif project['jdata']['family'] == "GW1N-9C":
            if project['jdata']['clock']['speed'] != "108000000":
                print("ERROR: only 108Mhz clock is supported at the moment")
                sys.exit(1)
            pll_v = """
module pll(
        input  clock_in,
        output clock_out,
        output locked
	);

    // https://juj.github.io/gowin_fpga_code_generators/pll_calculator.html
    rPLL #( // For GW1NR-9C C6/I5 (Tang Nano 9K proto dev board)
      .FCLKIN("27"),
      .IDIV_SEL(0), // -> PFD = 27 MHz (range: 3-400 MHz)
      .FBDIV_SEL(3), // -> CLKOUT = 108 MHz (range: 3.125-600 MHz)
      .ODIV_SEL(4) // -> VCO = 432 MHz (range: 400-1200 MHz)
    ) pll (.CLKOUTP(), .CLKOUTD(), .CLKOUTD3(), .RESET(1'b0), .RESET_P(1'b0), .CLKFB(1'b0), .FBDSEL(6'b0), .IDSEL(6'b0), .ODSEL(6'b0), .PSDA(4'b0), .DUTYDA(4'b0), .FDLY(4'b0),
      .CLKIN(clock_in), // 27 MHz
      .CLKOUT(clock_out), // 108 MHz
      .LOCK(locked)
    );

endmodule

"""
            open(f"{project['SOURCE_PATH']}/pll.v", "w").write(pll_v)

        else:
            os.system(
                f"icepll -q -m -f '{project['SOURCE_PATH']}/pll.v' -i {float(project['osc_clock']) / 1000000} -o {float(project['jdata']['clock']['speed']) / 1000000}"
            )
        project['verilog_files'].append("pll.v")

    top_data.append("")
    argsstr = ",\n        ".join(top_arguments)
    top_data.append(f"module rio (\n        {argsstr}")
    top_data.append("    );")
    top_data.append("")
    top_data.append("")

    top_data.append("    reg ESTOP = 0;")
    top_data.append("    wire ERROR;")
    top_data.append("    wire INTERFACE_TIMEOUT;")
    top_data.append("    assign ERROR = (INTERFACE_TIMEOUT | ESTOP);")

    if project['osc_clock']:
        top_data.append("    wire sysclk;")
        top_data.append("    wire locked;")
        top_data.append("    pll mypll(sysclk_in, sysclk, locked);")
        top_data.append("")


    if project['jdata']["toolchain"] == "diamond":
        top_data.append("    // Internal Oscillator")
        top_data.append('    defparam OSCH_inst.NOM_FREQ = "133.00";')
        top_data.append("    OSCH OSCH_inst ( ")
        top_data.append("        .STDBY(1'b0),")
        top_data.append("        .OSC(sysclk),")
        top_data.append("        .SEDSTDBY()")
        top_data.append("    );")
        top_data.append("")


    if "blink" in project['jdata']:
        top_data.append("    blink blink1 (")
        top_data.append("        .clk (sysclk),")
        top_data.append(f"        .speed ({int(project['jdata']['clock']['speed']) // 1 // 2}),")
        top_data.append("        .led (BLINK_LED)")
        top_data.append("    );")
        top_data.append("")
        project['verilog_files'].append("blink.v")
        os.system(f"cp -a generators/firmware/blink.v* {project['SOURCE_PATH']}/blink.v")


    if "error" in project['jdata']:
        top_data.append("    assign ERROR_OUT = ERROR;")
        top_data.append("")


    top_data.append(f"    parameter BUFFER_SIZE = {project['data_size']};")
    top_data.append("")

    top_data.append(f"    wire[{project['data_size'] - 1}:0] rx_data;")
    top_data.append(f"    wire[{project['data_size'] - 1}:0] tx_data;")
    top_data.append("")

    top_data.append("    reg signed [31:0] header_tx;")
    top_data.append("    always @(posedge sysclk) begin")
    top_data.append("        if (ESTOP) begin")
    top_data.append("            header_tx <= 32'h65737470;")
    top_data.append("        end else begin")
    top_data.append("            header_tx <= 32'h64617461;")
    top_data.append("        end")
    top_data.append("    end")
    top_data.append("")

    jointEnables = []
    for num in range(project['joints']):
        top_data.append(f"    wire jointEnable{num};")
        jointEnables.append(f"jointEnable{num}")
    top_data.append("")

    if "enable" in project['jdata']:
        jointEnablesStr = " || ".join(jointEnables)
        top_data.append(f"    assign ENA = ({jointEnablesStr}) && ~ERROR;")
        top_data.append("")


    if project['dins_total'] > project['dins']:
        top_data.append("    // fake din's to fit byte")
        for num in range(project['dins_total'] - project['dins']):
            top_data.append(f"    reg DIN{project['dins'] + num} = 0;")
        top_data.append("")


    top_data.append(f"    // vouts {project['vouts']}")
    for num in range(project['vouts']):
        top_data.append(f"    wire signed [31:0] setPoint{num};")
    top_data.append("")
    top_data.append(f"    // vins {project['vins']}")
    for num in range(project['vins']):
        top_data.append(f"    wire signed [31:0] processVariable{num};")
    top_data.append("")
    top_data.append(f"    // joints {project['joints']}")
    for num in range(project['joints']):
        top_data.append(f"    wire signed [31:0] jointFreqCmd{num};")

    for num in range(project['joints']):
        top_data.append(f"    wire signed [31:0] jointFeedback{num};")
    top_data.append("")


    top_data.append(f"    // rx_data {project['rx_data_size']}")
    pos = project['data_size']

    top_data.append("    wire [31:0] header_rx;")
    top_data.append(
        f"    assign header_rx = {{rx_data[{pos-3*8-1}:{pos-3*8-8}], rx_data[{pos-2*8-1}:{pos-2*8-8}], rx_data[{pos-1*8-1}:{pos-1*8-8}], rx_data[{pos-1}:{pos-8}]}};"
    )
    pos -= 32

    for num in range(project['joints']):
        top_data.append(
            f"    assign jointFreqCmd{num} = {{rx_data[{pos-3*8-1}:{pos-3*8-8}], rx_data[{pos-2*8-1}:{pos-2*8-8}], rx_data[{pos-1*8-1}:{pos-1*8-8}], rx_data[{pos-1}:{pos-8}]}};"
        )
        pos -= 32

    for num in range(project['vouts']):
        top_data.append(
            f"    assign setPoint{num} = {{rx_data[{pos-3*8-1}:{pos-3*8-8}], rx_data[{pos-2*8-1}:{pos-2*8-8}], rx_data[{pos-1*8-1}:{pos-1*8-8}], rx_data[{pos-1}:{pos-8}]}};"
        )
        pos -= 32


    for dbyte in range(project['joints_en_total'] // 8):
        for num in range(8):
            bitnum = dbyte * 8 + (7 - num)
            if bitnum < project['joints']:
                top_data.append(f"    assign jointEnable{bitnum} = rx_data[{pos-1}];")
            else:
                top_data.append(f"    // assign jointEnable{bitnum} = rx_data[{pos-1}];")
            pos -= 1

    for dbyte in range(project['douts_total'] // 8):
        for num in range(8):
            bitnum = dbyte * 8 + (7 - num)
            if bitnum < project['douts']:
                if project['jdata']["dout"][bitnum].get("invert", False):
                    top_data.append(f"    assign DOUT{bitnum} = ~rx_data[{pos-1}];")
                else:
                    top_data.append(f"    assign DOUT{bitnum} = rx_data[{pos-1}];")
            else:
                top_data.append(
                    f"    // assign DOUT{bitnum} = rx_data[{pos-1}];"
                )
            pos -= 1


    top_data.append("")
    top_data.append(f"    // tx_data {project['tx_data_size']}")
    top_data.append("    assign tx_data = {")
    top_data.append(
        "        header_tx[7:0], header_tx[15:8], header_tx[23:16], header_tx[31:24],"
    )

    for num in range(project['joints']):
        top_data.append(
            f"        jointFeedback{num}[7:0], jointFeedback{num}[15:8], jointFeedback{num}[23:16], jointFeedback{num}[31:24],"
        )

    for num in range(project['vins']):
        top_data.append(f"        processVariable{num}[7:0], processVariable{num}[15:8], processVariable{num}[23:16], processVariable{num}[31:24],")

    tdins = []


    for dbyte in range(project['dins_total'] // 8):
        for num in range(8):
            bitnum = (8 - 1 - num) + (project['dins_total'] // 8 - 1 - dbyte) * 8
            if bitnum < project['dins'] and project['jdata']["din"][bitnum].get("invert", False):
                tdins.append(f"~DIN{bitnum}")
            else:
                tdins.append(f"DIN{bitnum}")


    fill = project['data_size'] - project['tx_data_size']

    if fill > 0:
        top_data.append(f"        {', '.join(tdins)},")
        top_data.append(f"        {fill}'d0")
    else:
        top_data.append(f"        {', '.join(tdins)}")
    top_data.append("    };")
    top_data.append("")



    expansion_size = {}
    for expansions in project["expansions"].values():
        for enum, size in expansions.items():
            expansion_size[enum] = size

    expansion_ports = {}
    for pname, pins in project['pinlists'].items():
        for pin in pins:
            if pin[1].startswith("EXPANSION"):
                port = pin[1].split("[")[0]
                pnum = int(pin[1].split("[")[1].split("]")[0])
                size = expansion_size[port]
                if port.endswith("_OUTPUT"):
                    if port not in expansion_ports:
                        expansion_ports[port] = {}
                        for n in range(size):
                            expansion_ports[port][n] = "1'd0"
                if pin[2] == "OUTPUT":
                    if "_OUTPUT" not in pin[1]:
                        print("ERROR: pin-direction do not match:", pin)
                        exit(1)
                    expansion_ports[port][pnum] = pin[0]
                else:
                    if "_INPUT" not in pin[1]:
                        print("ERROR: pin-direction do not match:", pin)
                        exit(1)

    top_data.append("    // expansion I/O's")
    for pname, pins in project['pinlists'].items():
        for pin in pins:
            if pin[1].startswith("EXPANSION"):
                if pin[2] == "OUTPUT":
                    top_data.append(f"    wire {pin[0]};")
                else:
                    top_data.append(f"    wire {pin[0]};")
                    top_data.append(f"    assign {pin[0]} = {pin[1]};")

    for port, pins in expansion_ports.items():
        assign_list = []
        size = expansion_size[port]
        for n in range(size):
            assign_list.append(f"{pins[size - 1 - n]}")
        top_data.append(f"    assign {port} = {{{', '.join(assign_list)}}};")

    top_data.append("")


    for plugin in project['plugins']:
        if hasattr(project['plugins'][plugin], "funcs"):
            funcs = project['plugins'][plugin].funcs()
            top_data.append("\n".join(funcs))
            top_data.append("")

    top_data.append("endmodule")
    top_data.append("")
    open(f"{project['SOURCE_PATH']}/rio.v", "w").write("\n".join(top_data))
    project['verilog_files'].append("rio.v")
    board = project['jdata'].get("board")

    if board == "TangNano9K":
        family = project['jdata']["family"]
        ftype = project['jdata']["type"]

        lpf_data = []
        lpf_data.append("")
        lpf_data.append("")
        for pname, pins in project['pinlists'].items():
            lpf_data.append(f"// ### {pname} ###")
            for pin in pins:
                if pin[1].startswith("EXPANSION"):
                    continue

                lpf_data.append(f'IO_LOC "{pin[0]}" {pin[1]};')
                #lpf_data.append(f'IO_PORT "{pin[0]}" IO_TYPE=LVCMOS33;')
                if len(pin) > 3 and pin[3]:
                    lpf_data.append(f'IO_PORT "{pin[0]}" PULL_MODE=UP;')


            lpf_data.append("")
        lpf_data.append("")
        open(f"{project['PINS_PATH']}/pins.cst", "w").write("\n".join(lpf_data))

        verilogs = " ".join(project['verilog_files'])
        makefile_data = []
        makefile_data.append("")
        makefile_data.append(f"BOARD={family}")
        makefile_data.append(f"FAMILY=GW1N-9C")
        makefile_data.append(f"DEVICE={ftype}")
        makefile_data.append("")
        makefile_data.append("all: rio.fs")
        makefile_data.append("")
        makefile_data.append(f"rio.json: {verilogs}")
        makefile_data.append(f"	yosys -q -l yosys.log -p 'synth_gowin -top rio -json rio.json' {verilogs}")
        makefile_data.append("")
        makefile_data.append("rio_pnr.json: rio.json")
        makefile_data.append("	nextpnr-gowin --json rio.json --write rio_pnr.json --freq 27 --device ${DEVICE} --family ${FAMILY} --cst pins.cst")
        makefile_data.append("")
        makefile_data.append("rio.fs: rio_pnr.json")
        makefile_data.append("	gowin_pack -d ${FAMILY} -o rio.fs rio_pnr.json")
        makefile_data.append("")
        makefile_data.append("load: rio.fs")
        makefile_data.append("	sudo openFPGALoader -b tangnano9k rio.fs -f")
        makefile_data.append("")
        open(f"{project['FIRMWARE_PATH']}/Makefile", "w").write("\n".join(makefile_data))


    elif project['jdata']["toolchain"] == "icestorm" and project['jdata']["family"] == "ecp5":

        lpf_data = []
        lpf_data.append("")

        lpf_data.append("")
        for pname, pins in project['pinlists'].items():
            lpf_data.append(f"### {pname} ###")
            for pin in pins:
                if pin[1].startswith("EXPANSION"):
                    continue
                lpf_data.append(f'LOCATE COMP "{pin[0]}"           SITE "{pin[1]}";')
                lpf_data.append(f'IOBUF PORT "{pin[0]}" IO_TYPE=LVCMOS33;')

            lpf_data.append("")
        lpf_data.append("")
        open(f"{project['PINS_PATH']}/pins.lpf", "w").write("\n".join(lpf_data))

        verilogs = " ".join(project['verilog_files'])
        makefile_data = []
        makefile_data.append("")
        makefile_data.append(f"FAMILY  := {project['jdata']['family']}")
        makefile_data.append(f"TYPE    := {project['jdata']['type']}")
        makefile_data.append(f"PACKAGE := {project['jdata']['package']}")
        makefile_data.append("")

        makefile_data.append("")
        makefile_data.append("all: rio.bit")
        makefile_data.append("")
        makefile_data.append(f"rio.json: {verilogs}")
        makefile_data.append(
            f"	yosys -q -l yosys.log -p 'synth_${{FAMILY}} -top rio -json rio.json' {verilogs}"
        )
        makefile_data.append("")
        makefile_data.append("rio.config: rio.json pins.lpf")
        makefile_data.append(
            "	nextpnr-${FAMILY} -q -l nextpnr.log --${TYPE} --package ${PACKAGE} --json rio.json --lpf pins.lpf --textcfg rio.config"
        )
        makefile_data.append('	@echo ""')
        makefile_data.append('	@grep -B 1 "%$$" nextpnr.log')
        makefile_data.append('	@echo ""')
        makefile_data.append("")
        makefile_data.append("rio.bit: rio.config")
        makefile_data.append(
            "	ecppack --svf rio.svf rio.config rio.bit"
        )
        makefile_data.append("	")
        makefile_data.append("rio.svf: rio.bit")
        makefile_data.append("")
        makefile_data.append("check:")
        makefile_data.append("	verilator --top-module rio --lint-only -Wall *.v")
        makefile_data.append("")
        makefile_data.append("clean:")
        makefile_data.append(
            "	rm -rf rio.bit rio.svf rio.config rio.json yosys.log nextpnr.log"
        )
        makefile_data.append("")
        makefile_data.append("tinyprog: rio.bin")
        makefile_data.append("	tinyprog -p rio.bin")
        makefile_data.append("")
        open(f"{project['FIRMWARE_PATH']}/Makefile", "w").write("\n".join(makefile_data))


    elif project['jdata']["toolchain"] == "icestorm":
        # pins.pcf (icestorm)
        pcf_data = []
        for pname, pins in project['pinlists'].items():
            pcf_data.append(f"### {pname} ###")
            for pin in pins:
                if pin[1].startswith("EXPANSION"):
                    continue
                options = ""
                if len(pin) > 3 and pin[3]:
                    options += " -pullup yes"

                pcf_data.append(f"set_io {options} {pin[0]} {pin[1]}")
            pcf_data.append("")
        open(f"{project['PINS_PATH']}/pins.pcf", "w").write("\n".join(pcf_data))

        verilogs = " ".join(project['verilog_files'])
        makefile_data = []
        makefile_data.append("")
        makefile_data.append(f"FAMILY  := {project['jdata']['family']}")
        makefile_data.append(f"TYPE    := {project['jdata']['type']}")
        makefile_data.append(f"PACKAGE := {project['jdata']['package']}")
        makefile_data.append("")
        makefile_data.append("all: rio.bin")
        makefile_data.append("")
        makefile_data.append(f"rio.json: {verilogs}")
        makefile_data.append(
            f"	yosys -q -l yosys.log -p 'synth_${{FAMILY}} -top rio -json rio.json' {verilogs}"
        )
        makefile_data.append("")
        makefile_data.append("rio.asc: rio.json pins.pcf")
        makefile_data.append(
            "	nextpnr-${FAMILY} -q -l nextpnr.log --${TYPE} --package ${PACKAGE} --json rio.json --pcf pins.pcf --asc rio.asc"
        )
        makefile_data.append('	@echo ""')
        makefile_data.append('	@grep -B 1 "%$$" nextpnr.log')
        makefile_data.append('	@echo ""')
        makefile_data.append("")
        makefile_data.append("rio.bin: rio.asc")
        makefile_data.append("	icepack rio.asc rio.bin")
        makefile_data.append("")
        makefile_data.append("check:")
        makefile_data.append("	verilator --top-module rio --lint-only -Wall *.v")
        makefile_data.append("")
        makefile_data.append("clean:")
        makefile_data.append(
            "	rm -rf rio.bin rio.asc rio.json yosys.log nextpnr.log"
        )
        makefile_data.append("")

        makefile_data.append(f"sim: {verilogs}")
        makefile_data.append(f"	verilator --cc --exe --build -j 0 -Wall --top-module rio sim_main.cpp {verilogs}")
        makefile_data.append("")

        makefile_data.append("tinyprog: rio.bin")
        makefile_data.append("	tinyprog -p rio.bin")
        makefile_data.append("")
        open(f"{project['FIRMWARE_PATH']}/Makefile", "w").write("\n".join(makefile_data))


    elif project['jdata']["toolchain"] == "diamond":
        os.system(f"cp files/pif21.sty {project['FIRMWARE_PATH']}/")

        ldf_data = []
        ldf_data.append('<?xml version="1.0" encoding="UTF-8"?>')
        ldf_data.append(
            f'<BaliProject version="3.2" title="rio" device="{project["jdata"]["type"]}" default_implementation="impl1">'
        )
        ldf_data.append("    <Options/>")
        ldf_data.append(
            '    <Implementation title="impl1" dir="impl1" description="impl1" synthesis="lse" default_strategy="Strategy1">'
        )
        ldf_data.append('        <Options def_top="rio"/>')
        for vfile in project['verilog_files']:
            ldf_data.append(
                f'        <Source name="impl1/source/{vfile}" type="Verilog" type_short="Verilog">'
            )
            ldf_data.append("            <Options/>")
            ldf_data.append("        </Source>")
        ldf_data.append(
            '        <Source name="impl1/source/pins.lpf" type="Logic Preference" type_short="LPF">'
        )
        ldf_data.append("            <Options/>")
        ldf_data.append("        </Source>")
        ldf_data.append("    </Implementation>")
        ldf_data.append('    <Strategy name="Strategy1" file="pif21.sty"/>')
        ldf_data.append("</BaliProject>")
        ldf_data.append("")
        open(f"{project['FIRMWARE_PATH']}/rio.ldf", "w").write("\n".join(ldf_data))

        # pins.lpf (diamond)
        pcf_data = []
        pcf_data.append("")
        pcf_data.append("BLOCK RESETPATHS;")
        pcf_data.append("BLOCK ASYNCPATHS;")
        pcf_data.append("")
        pcf_data.append("BANK 0 VCCIO 3.3 V;")
        pcf_data.append("BANK 1 VCCIO 3.3 V;")
        pcf_data.append("BANK 2 VCCIO 3.3 V;")
        pcf_data.append("BANK 3 VCCIO 3.3 V;")
        pcf_data.append("BANK 5 VCCIO 3.3 V;")
        pcf_data.append("BANK 6 VCCIO 3.3 V;")
        pcf_data.append("")
        pcf_data.append('TRACEID "00111100" ;')
        pcf_data.append("IOBUF ALLPORTS IO_TYPE=LVCMOS33 ;")
        # pcf_data.append('SYSCONFIG JTAG_PORT=DISABLE  SDM_PORT=PROGRAMN  I2C_PORT=DISABLE  SLAVE_SPI_PORT=ENABLE  MCCLK_FREQ=10.23 ;')
        pcf_data.append(
            "SYSCONFIG JTAG_PORT=ENABLE  SDM_PORT=PROGRAMN  I2C_PORT=DISABLE  SLAVE_SPI_PORT=DISABLE  MCCLK_FREQ=10.23 ;"
        )
        pcf_data.append('USERCODE ASCII  "PIF2"      ;')
        pcf_data.append("")
        pcf_data.append('# LOCATE COMP "FDONE"           SITE "109";')
        pcf_data.append('# LOCATE COMP "FINITn"          SITE "110";')
        pcf_data.append('# LOCATE COMP "FPROGn"          SITE "119";')
        pcf_data.append('# LOCATE COMP "FJTAGn"          SITE "120";')
        pcf_data.append('# LOCATE COMP "FTMS"            SITE "130";')
        pcf_data.append('# LOCATE COMP "FTCK"            SITE "131";')
        pcf_data.append('# LOCATE COMP "FTDI"            SITE "136";')
        pcf_data.append('# LOCATE COMP "FTDO"            SITE "137";')
        pcf_data.append("")
        pcf_data.append('LOCATE COMP "GSRn"              SITE "136";')
        pcf_data.append('LOCATE COMP "LEDR"              SITE "112";')
        pcf_data.append('LOCATE COMP "LEDG"              SITE "113";')
        pcf_data.append('LOCATE COMP "SDA"               SITE "125";')
        pcf_data.append('LOCATE COMP "SCL"               SITE "126";')
        pcf_data.append('IOBUF  PORT "GSRn"              IO_TYPE=LVCMOS33 PULLMODE=UP;')
        pcf_data.append('IOBUF  PORT "LEDR"              IO_TYPE=LVCMOS33 PULLMODE=DOWN;')
        pcf_data.append('IOBUF  PORT "LEDG"              IO_TYPE=LVCMOS33 PULLMODE=DOWN;')
        pcf_data.append('IOBUF  PORT "SCL"               IO_TYPE=LVCMOS33 PULLMODE=UP;')
        pcf_data.append('IOBUF  PORT "SDA"               IO_TYPE=LVCMOS33 PULLMODE=UP;')
        pcf_data.append("")
        for pname, pins in project['pinlists'].items():
            pcf_data.append(f"### {pname} ###")
            for pin in pins:
                if pin[1].startswith("EXPANSION"):
                    continue
                pcf_data.append(f'LOCATE COMP "{pin[0]}"           SITE "{pin[1]}";')
            pcf_data.append("")
        pcf_data.append("")
        open(f"{project['PINS_PATH']}/pins.lpf", "w").write("\n".join(pcf_data))

