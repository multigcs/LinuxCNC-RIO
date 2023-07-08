
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

    if project["internal_clock"]:
        pass
    elif project['osc_clock']:
        if project['jdata']['family'] == "ecp5":
            os.system(
                f"ecppll -f '{project['SOURCE_PATH']}/pll.v' -i {float(project['osc_clock']) / 1000000} -o {float(project['jdata']['clock']['speed']) / 1000000}"
            )
        elif project['jdata']['type'] == "up5k":
            os.system(
                f"icepll -p -m -f '{project['SOURCE_PATH']}/pll.v' -i {float(project['osc_clock']) / 1000000} -o {float(project['jdata']['clock']['speed']) / 1000000}"
            )
        elif project['jdata']['family'] == "GW1N-9C":
            os.system(
                f"python3 files/gowin-pll.py -d 'GW1NR-9 C6/I5' -f '{project['SOURCE_PATH']}/pll.v' -i {float(project['osc_clock']) / 1000000} -o {float(project['jdata']['clock']['speed']) / 1000000}"
            )
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

    if project["internal_clock"]:
        top_data.append("    // using internal oscillator")
        top_data.append("    wire sysclk;")
        top_data.append("    OSC osc(")
        top_data.append("    	.OSCOUT(sysclk)")
        top_data.append("    );")
        top_data.append("    defparam osc.FREQ_DIV=10;")
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
        top_data.append(f"    blink #({int(project['jdata']['clock']['speed']) // 1 // 2}) blink1 (")
        top_data.append("        .clk (sysclk),")
        top_data.append("        .led (BLINK_LED)")
        top_data.append("    );")
        top_data.append("")
        project['verilog_files'].append("blink.v")
        os.system(f"cp -a generators/firmware/blink.v* {project['SOURCE_PATH']}/blink.v")

    if "error" in project['jdata']:
        if project['jdata']["error"].get("invert"):
            top_data.append("    assign ERROR_OUT = ~ERROR;")
        else:
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




    # plugins wire/register definitions
    for plugin in project['plugins']:
        if hasattr(project['plugins'][plugin], "defs"):
            defs = project['plugins'][plugin].defs()
            top_data.append("\n".join(defs))
            top_data.append("")


    # expansion wires
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
    top_data.append("    // expansion I/O's (wire)")
    for pname, pins in project['pinlists'].items():
        for pin in pins:
            if pin[1].startswith("EXPANSION"):
                if pin[2] == "OUTPUT":
                    top_data.append(f"    wire {pin[0]};")
                else:
                    top_data.append(f"    wire {pin[0]};")
    top_data.append("")



    jointEnables = []
    for num in range(project['joints']):
        top_data.append(f"    wire jointEnable{num};")
        jointEnables.append(f"jointEnable{num}")
    top_data.append("")

    if "enable" in project['jdata']:
        jointEnablesStr = " || ".join(jointEnables)
        if project['jdata']["enable"].get("invert", False):
            top_data.append(f"    wire ENA_INV;")
            top_data.append(f"    assign ENA = ~ENA_INV;")
            top_data.append(f"    assign ENA_INV = ({jointEnablesStr}) && ~ERROR;")
        else:
            top_data.append(f"    assign ENA = ({jointEnablesStr}) && ~ERROR;")
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
            bitnum = num + (dbyte * 8)
            if bitnum < project['douts']:
                dname = project['doutnames'][bitnum]
                if bitnum in project['jdata']["dout"] and project['jdata']["dout"][bitnum].get("invert", False):
                    top_data.append(f"    assign {dname} = ~rx_data[{pos-1}];")
                else:
                    top_data.append(f"    assign {dname} = rx_data[{pos-1}];")
            else:
                top_data.append(
                    f"    // assign DOUTx = rx_data[{pos-1}];"
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

    ldin = len(project['jdata']["din"])
    for dbyte in range(project['dins_total'] // 8):
        for num in range(8):
            bitnum = num + (dbyte * 8)
            if bitnum < project['dins']:
                dname = project['dinnames'][bitnum]
                if bitnum < ldin and project['jdata']["din"][bitnum].get("invert", False):
                    tdins.append(f"~{dname}")
                else:
                    tdins.append(f"{dname}")
            else:
                tdins.append(f"1'd0")

    fill = project['data_size'] - project['tx_data_size']

    if fill > 0:
        top_data.append(f"        {', '.join(tdins)},")
        top_data.append(f"        {fill}'d0")
    else:
        top_data.append(f"        {', '.join(tdins)}")
    top_data.append("    };")
    top_data.append("")




    top_data.append("    // expansion I/O's (assigne)")
    for pname, pins in project['pinlists'].items():
        for pin in pins:
            if pin[1].startswith("EXPANSION"):
                if pin[2] == "INPUT":
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

    # testbench
    testb_data = []
    testb_data.append("`timescale 1ns/100ps")
    testb_data.append("")
    testb_data.append("module testb;")
    testb_data.append("")

    for arg in top_arguments:
        arg_dir = arg.split()[0]
        arg_name = arg.split()[1]
        if arg_dir == "input":
            testb_data.append(f"    reg {arg_name} = 0;")

    testb_data.append("")
    for arg in top_arguments:
        arg_dir = arg.split()[0]
        arg_name = arg.split()[1]
        if arg_dir == "output":
            testb_data.append(f"    wire {arg_name};")

    testb_data.append("")
    testb_data.append("    always #2 sysclk = !sysclk;")
    testb_data.append("")
    testb_data.append("    initial begin")
    testb_data.append("        $dumpfile(\"testb.vcd\");")

    for anum, arg in enumerate(top_arguments):
        arg_dir = arg.split()[0]
        arg_name = arg.split()[1]

        testb_data.append(f"        $dumpvars({anum}, {arg_name});")

    testb_data.append("")
    testb_data.append("        # 100000 $finish;")
    testb_data.append("    end")
    testb_data.append("")
    testb_data.append("    rio rio1 (")

    alen = len(top_arguments)
    for anum, arg in enumerate(top_arguments):
        arg_dir = arg.split()[0]
        arg_name = arg.split()[1]
        if anum == alen-1:
            testb_data.append(f"        .{arg_name} ({arg_name})")
        else:
            testb_data.append(f"        .{arg_name} ({arg_name}),")
    testb_data.append("    );")
    testb_data.append("")
    testb_data.append("endmodule")
    testb_data.append("")

    open(f"{project['SOURCE_PATH']}/testb.v", "w").write("\n".join(testb_data))

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
                    lpf_data.append(f'IO_PORT "{pin[0]}" IO_TYPE=LVCMOS33 PULL_MODE=UP;')
                else:
                    lpf_data.append(f'IO_PORT "{pin[0]}" IO_TYPE=LVCMOS33;')

            lpf_data.append("")
        lpf_data.append("")
        open(f"{project['PINS_PATH']}/pins.cst", "w").write("\n".join(lpf_data))

        verilogs = " ".join(project['verilog_files'])
        makefile_data = []
        makefile_data.append("")
        makefile_data.append(f"FAMILY={family}")
        makefile_data.append(f"DEVICE={ftype}")
        makefile_data.append("")
        makefile_data.append("all: rio.fs")
        makefile_data.append("")
        makefile_data.append(f"rio.json: {verilogs}")
        makefile_data.append(f"	yosys -q -l yosys.log -p 'synth_gowin -noalu -nowidelut -top rio -json rio.json' {verilogs}")
        makefile_data.append("")
        makefile_data.append("rio_pnr.json: rio.json")
        makefile_data.append(f"	nextpnr-gowin --seed 0 --json rio.json --write rio_pnr.json --freq {float(project['jdata']['clock']['speed']) / 1000000} --enable-globals --enable-auto-longwires --device ${{DEVICE}} --family ${{FAMILY}} --cst pins.cst")
        makefile_data.append("")
        makefile_data.append("rio.fs: rio_pnr.json")
        makefile_data.append("	gowin_pack -d ${FAMILY} -o rio.fs rio_pnr.json")
        makefile_data.append("")
        makefile_data.append("load: rio.fs")
        makefile_data.append("	openFPGALoader -b tangnano9k rio.fs -f")
        makefile_data.append("")
        makefile_data.append("")
        makefile_data.append("clean:")
        makefile_data.append("	rm -rf rio.fs rio.json rio_pnr.json")
        makefile_data.append("")
        makefile_data.append("testb:")
        makefile_data.append(f"	iverilog -Wall -o testb.out testb.v {verilogs}")
        makefile_data.append("	vvp testb.out")
        makefile_data.append("	gtkwave testb.vcd")
        makefile_data.append("")
        makefile_data.append("gowin_build: impl/pnr/project.fs")
        makefile_data.append("impl/pnr/project.fs: rio.tcl")
        makefile_data.append("	gw_sh rio.tcl")
        makefile_data.append("")
        makefile_data.append("gowin_load: impl/pnr/project.fs")
        makefile_data.append("	openFPGALoader -b tangnano9k impl/pnr/project.fs -f")
        makefile_data.append("")
        open(f"{project['FIRMWARE_PATH']}/Makefile", "w").write("\n".join(makefile_data))

        # generating project file for the gowin toolchain
        prj_data = []
        prj_data.append("<?xml version=\"1\" encoding=\"UTF-8\"?>")
        prj_data.append("<!DOCTYPE gowin-fpga-project>")
        prj_data.append("<Project>")
        prj_data.append("    <Template>FPGA</Template>")
        prj_data.append("    <Version>5</Version>")
        prj_data.append("    <Device name=\"GW1NR-9C\" pn=\"GW1NR-LV9QN88PC6/I5\">gw1nr9c-004</Device>")
        prj_data.append("    <FileList>")
        for verilog in verilogs.split():
            prj_data.append(f"        <File path=\"{verilog}\" type=\"file.verilog\" enable=\"1\"/>")
        prj_data.append("    <File path=\"pins.cst\" type=\"file.cst\" enable=\"1\"/>")
        prj_data.append("    </FileList>")
        prj_data.append("</Project>")
        open(f"{project['FIRMWARE_PATH']}/rio.gprj", "w").write("\n".join(prj_data))

        os.system(f"mkdir -p {project['FIRMWARE_PATH']}/impl")
        pps_data = """{
 "Allow_Duplicate_Modules" : false,
 "Annotated_Properties_for_Analyst" : true,
 "BACKGROUND_PROGRAMMING" : "",
 "COMPRESS" : false,
 "CRC_CHECK" : true,
 "Clock_Conversion" : true,
 "Clock_Route_Order" : 0,
 "Correct_Hold_Violation" : true,
 "DONE" : false,
 "DOWNLOAD_SPEED" : "",
 "Default_Enum_Encoding" : "default",
 "Disable_Insert_Pad" : false,
 "ENCRYPTION_KEY" : false,
 "ENCRYPTION_KEY_TEXT" : "00000000000000000000000000000000",
 "FORMAT" : "txt",
 "FSM Compiler" : true,
 "Fanout_Guide" : 10000,
 "Frequency" : "Auto",
 "Generate_Constraint_File_of_Ports" : false,
 "Generate_IBIS_File" : false,
 "Generate_Plain_Text_Timing_Report" : false,
 "Generate_Post_PNR_Simulation_Model_File" : false,
 "Generate_Post_Place_File" : false,
 "Generate_SDF_File" : false,
 "Generate_VHDL_Post_PNR_Simulation_Model_File" : false,
 "GwSyn_Loop_Limit" : 2000,
 "HOTBOOT" : false,
 "I2C" : false,
 "I2C_SLAVE_ADDR" : "",
 "Implicit_Initial_Value_Support" : false,
 "IncludePath" : [],
 "Incremental_Compile" : "",
 "Initialize_Primitives" : false,
 "JTAG" : false,
 "MODE_IO" : false,
 "MSPI" : false,
 "Multiple_File_Compilation_Unit" : true,
 "Number_of_Critical_Paths" : "",
 "Number_of_Start/End_Points" : "",
 "OUTPUT_BASE_NAME" : "rio",
 "POWER_ON_RESET_MONITOR" : false,
 "PRINT_BSRAM_VALUE" : true,
 "PROGRAM_DONE_BYPASS" : false,
 "Pipelining" : true,
 "PlaceInRegToIob" : true,
 "PlaceIoRegToIob" : true,
 "PlaceOutRegToIob" : true,
 "Place_Option" : "0",
 "Process_Configuration_Verion" : "1.0",
 "Promote_Physical_Constraint_Warning_to_Error" : true,
 "Push_Tristates" : true,
 "READY" : false,
 "RECONFIG_N" : false,
 "Ram_RW_Check" : true,
 "Report_Auto-Placed_Io_Information" : false,
 "Resolve_Mixed_Drivers" : false,
 "Resource_Sharing" : true,
 "Retiming" : false,
 "Route_Maxfan" : 23,
 "Route_Option" : "0",
 "Run_Timing_Driven" : true,
 "SECURE_MODE" : false,
 "SECURITY_BIT" : true,
 "SPI_FLASH_ADDR" : "",
 "SSPI" : true,
 "Show_All_Warnings" : false,
 "Synthesis On/Off Implemented as Translate On/Off" : false,
 "Synthesize_tool" : "GowinSyn",
 "TclPre" : "",
 "TopModule" : "",
 "USERCODE" : "default",
 "Unused_Pin" : "As_input_tri_stated_with_pull_up",
 "Update_Compile_Point_Timing_Data" : false,
 "Use_Clock_Period_for_Unconstrainted IO" : false,
 "VCCAUX" : 3.3,
 "VHDL_Standard" : "VHDL_Std_1993",
 "Verilog_Standard" : "Vlg_Std_2001",
 "WAKE_UP" : "0",
 "Write_Vendor_Constraint_File" : true,
 "dsp_balance" : false,
 "show_all_warnings" : false,
 "turn_off_bg" : false
}"""

        open(f"{project['FIRMWARE_PATH']}/impl/project_process_config.json", "w").write(pps_data)

        # generating tcl script for the gowin toolchain
        tcl_data = []
        tcl_data.append("set_device -name GW1NR-9C GW1NR-LV9QN88PC6/I5")
        for verilog in verilogs.split():
            tcl_data.append(f"add_file {verilog}")
        tcl_data.append("add_file pins.cst")
        tcl_data.append("")
        tcl_data.append("set_option -use_sspi_as_gpio 1")
        tcl_data.append("")
        tcl_data.append("run all")
        open(f"{project['FIRMWARE_PATH']}/rio.tcl", "w").write("\n".join(tcl_data))

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

        flashcmd = project['jdata'].get("flashcmd")
        if flashcmd:
            makefile_data.append("load: rio.bin")
            makefile_data.append(f"	{flashcmd}")
            makefile_data.append("")
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

        flashcmd = project['jdata'].get("flashcmd")
        if flashcmd:
            makefile_data.append("load: rio.bin")
            makefile_data.append(f"	{flashcmd}")
            makefile_data.append("")
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

