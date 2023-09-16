
import os
from .pins import *

def buildsys_gowin(project):
    board = project["jdata"].get("board")
    family = project["jdata"]["family"]
    ftype = project["jdata"]["type"]
    if family == "GW1N-9C":
        family_gowin = "GW1NR-9C"
    else:
        family_gowin = family

    pins_cst(project)

    verilogs = " ".join(project["verilog_files"])
    makefile_data = []
    makefile_data.append("")
    makefile_data.append(f"FAMILY={family}")
    makefile_data.append(f"DEVICE={ftype}")
    makefile_data.append("")

    if board == "TangNano9K":
        makefile_data.append("all: rio.fs")
        makefile_data.append("")
        makefile_data.append(f"rio.json: {verilogs}")
        makefile_data.append(
            f"	yosys -q -l yosys.log -p 'synth_gowin -noalu -nowidelut -top rio -json rio.json' {verilogs}"
        )
        makefile_data.append("")
        makefile_data.append("rio_pnr.json: rio.json pins.cst")
        makefile_data.append(
            f"	nextpnr-gowin --seed 0 --json rio.json --write rio_pnr.json --freq {float(project['jdata']['clock']['speed']) / 1000000} --enable-globals --enable-auto-longwires --device ${{DEVICE}} --family ${{FAMILY}} --cst pins.cst"
        )
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
    elif board == "TangNano20K":
        makefile_data.append("all: impl/pnr/project.fs")
        makefile_data.append("")
        makefile_data.append("clean:")
        makefile_data.append("	rm -rf impl/pnr/project.fs")
        makefile_data.append("")
        makefile_data.append("load: gowin_load")
        makefile_data.append("")

    makefile_data.append("gowin_build: impl/pnr/project.fs")
    makefile_data.append("")
    makefile_data.append(f"impl/pnr/project.fs: rio.tcl pins.cst {verilogs}")
    makefile_data.append("	gw_sh rio.tcl")
    makefile_data.append("")
    makefile_data.append("gowin_load: impl/pnr/project.fs")
    makefile_data.append("	openFPGALoader -b tangnano9k impl/pnr/project.fs -f")
    makefile_data.append("")

    open(f"{project['FIRMWARE_PATH']}/Makefile", "w").write(
        "\n".join(makefile_data)
    )

    # generating project file for the gowin toolchain
    prj_data = []
    prj_data.append('<?xml version="1" encoding="UTF-8"?>')
    prj_data.append("<!DOCTYPE gowin-fpga-project>")
    prj_data.append("<Project>")
    prj_data.append("    <Template>FPGA</Template>")
    prj_data.append("    <Version>5</Version>")
    if family == "GW1N-9C":
        prj_data.append(
            f'    <Device name="{family_gowin}" pn="{ftype}">gw1nr9c-004</Device>'
        )
    elif family == "GW2AR-18":
        prj_data.append('    <Device name="" pn="">gw2ar18c-000</Device>')
    else:
        prj_data.append(
            f'    <Device name="{family_gowin}" pn="{ftype}">gw2ar-18-004</Device>'
        )
    prj_data.append("    <FileList>")
    for verilog in verilogs.split():
        prj_data.append(
            f'        <File path="{verilog}" type="file.verilog" enable="1"/>'
        )
    prj_data.append('    <File path="pins.cst" type="file.cst" enable="1"/>')
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

    open(f"{project['FIRMWARE_PATH']}/impl/project_process_config.json", "w").write(
        pps_data
    )

    # generating tcl script for the gowin toolchain
    tcl_data = []
    tcl_data.append(f"set_device -name {family_gowin} {ftype}")
    for verilog in verilogs.split():
        tcl_data.append(f"add_file {verilog}")
    tcl_data.append("add_file pins.cst")
    tcl_data.append("")
    tcl_data.append("set_option -use_sspi_as_gpio 1")
    tcl_data.append("")
    tcl_data.append("run all")
    open(f"{project['FIRMWARE_PATH']}/rio.tcl", "w").write("\n".join(tcl_data))


def buildsys_icestorm(project):
    if project["jdata"]["family"] == "ecp5":
        pins_lpf(project)
        bitfileName = "rio.bit"
    else:
        pins_pcf(project)
        bitfileName = "rio.bin"

    verilogs = " ".join(project["verilog_files"])
    makefile_data = []
    makefile_data.append("")
    makefile_data.append(f"FAMILY  := {project['jdata']['family']}")
    makefile_data.append(f"TYPE    := {project['jdata']['type']}")
    makefile_data.append(f"PACKAGE := {project['jdata']['package']}")
    makefile_data.append("")

    makefile_data.append(f"all: {bitfileName}")
    makefile_data.append("")
    makefile_data.append(f"rio.json: {verilogs}")
    makefile_data.append(f"	yosys -q -l yosys.log -p 'synth_${{FAMILY}} -top rio -json rio.json' {verilogs}")
    makefile_data.append("")

    if project["jdata"]["family"] == "ecp5":
        makefile_data.append("rio.config: rio.json pins.lpf")
        makefile_data.append("	nextpnr-${FAMILY} -q -l nextpnr.log --${TYPE} --package ${PACKAGE} --json rio.json --lpf pins.lpf --textcfg rio.config")
        makefile_data.append('	@echo ""')
        makefile_data.append('	@grep -B 1 "%$$" nextpnr.log')
        makefile_data.append('	@echo ""')
        makefile_data.append("")
        makefile_data.append(f"{bitfileName}: rio.config")
        makefile_data.append(f"	ecppack --svf rio.svf rio.config {bitfileName}")
        makefile_data.append("")
        makefile_data.append(f"rio.svf: {bitfileName}")
        makefile_data.append("")
        makefile_data.append("clean:")
        makefile_data.append(f"	rm -rf {bitfileName} rio.svf rio.config rio.json yosys.log nextpnr.log")
        makefile_data.append("")
    else:
        makefile_data.append("rio.asc: rio.json pins.pcf")
        makefile_data.append("	nextpnr-${FAMILY} -q -l nextpnr.log --${TYPE} --package ${PACKAGE} --json rio.json --pcf pins.pcf --asc rio.asc")
        makefile_data.append('	@echo ""')
        makefile_data.append('	@grep -B 1 "%$$" nextpnr.log')
        makefile_data.append('	@echo ""')
        makefile_data.append("")
        makefile_data.append(f"{bitfileName}: rio.asc")
        makefile_data.append(f"	icepack rio.asc {bitfileName}")
        makefile_data.append("")
        makefile_data.append("clean:")
        makefile_data.append(f"	rm -rf {bitfileName} rio.asc rio.json yosys.log nextpnr.log")
        makefile_data.append("")

    makefile_data.append("check:")
    makefile_data.append("	verilator --top-module rio --lint-only -Wall *.v")
    makefile_data.append("")

    makefile_data.append(f"sim: {verilogs}")
    makefile_data.append(
        f"	verilator --cc --exe --build -j 0 -Wall --top-module rio sim_main.cpp {verilogs}"
    )
    makefile_data.append("")

    makefile_data.append(f"tinyprog: {bitfileName}")
    makefile_data.append(f"	tinyprog -p {bitfileName}")
    makefile_data.append("")

    flashcmd = project["jdata"].get("flashcmd")
    if flashcmd:
        makefile_data.append(f"load: {bitfileName}")
        makefile_data.append(f"	{flashcmd}")
        makefile_data.append("")
    makefile_data.append("")

    open(f"{project['FIRMWARE_PATH']}/Makefile", "w").write(
        "\n".join(makefile_data)
    )

def buildsys_vivado(project):
    pins_xdc(project)

    verilogs = " ".join(project["verilog_files"])
    makefile_data = []
    makefile_data.append("")
    makefile_data.append("all: build/rio.bit")
    makefile_data.append("")
    makefile_data.append(f"build/rio.bit: rio.tcl pins.xdc {verilogs}")
    makefile_data.append("	vivado -mode tcl -source rio.tcl")
    makefile_data.append("")
    makefile_data.append("clean:")
    makefile_data.append("	rm -rf build")
    makefile_data.append("")
    makefile_data.append("xc3sprog: build/rio.bit")
    makefile_data.append("	xc3sprog -c nexys4 build/rio.bit")
    makefile_data.append("")
    makefile_data.append("load: build/rio.bit")
    makefile_data.append("	openFPGALoader -b arty -f build/rio.bit")
    makefile_data.append("")
    makefile_data.append("")
    open(f"{project['FIRMWARE_PATH']}/Makefile", "w").write(
        "\n".join(makefile_data)
    )

    tcl_data = []
    tcl_data.append("")
    tcl_data.append("set outputDir ./build")
    tcl_data.append("file mkdir $outputDir")
    tcl_data.append("")
    for verilog in project["verilog_files"]:
        tcl_data.append(f"read_verilog {verilog}")
    tcl_data.append("read_xdc pins.xdc")
    tcl_data.append("")
    tcl_data.append(f"synth_design -top rio -part {project['jdata']['type']}")
    tcl_data.append("write_checkpoint -force $outputDir/post_synth.dcp")
    tcl_data.append(
        "report_timing_summary -file $outputDir/post_synth_timing_summary.rpt"
    )
    tcl_data.append("report_utilization -file $outputDir/post_synth_util.rpt")
    tcl_data.append("")
    tcl_data.append("opt_design")
    tcl_data.append("place_design")
    tcl_data.append("report_clock_utilization -file $outputDir/clock_util.rpt")
    tcl_data.append("")
    tcl_data.append(
        "# Optionally run optimization if there are timing violations after placement"
    )
    tcl_data.append(
        "#if {[get_property SLACK [get_timing_paths -max_paths 1 -nworst 1 -setup]] < 0} {"
    )
    tcl_data.append(
        '#    puts "Found setup timing violations => running physical optimization"'
    )
    tcl_data.append("#    phys_opt_design")
    tcl_data.append("#}")
    tcl_data.append("write_checkpoint -force $outputDir/post_place.dcp")
    tcl_data.append("report_utilization -file $outputDir/post_place_util.rpt")
    tcl_data.append(
        "report_timing_summary -file $outputDir/post_place_timing_summary.rpt"
    )
    tcl_data.append("")
    tcl_data.append("route_design")
    tcl_data.append("write_checkpoint -force $outputDir/post_route.dcp")
    tcl_data.append("report_route_status -file $outputDir/post_route_status.rpt")
    tcl_data.append(
        "report_timing_summary -file $outputDir/post_route_timing_summary.rpt"
    )
    tcl_data.append("report_power -file $outputDir/post_route_power.rpt")
    tcl_data.append("report_drc -file $outputDir/post_imp_drc.rpt")
    tcl_data.append("")
    tcl_data.append(
        "write_verilog -force $outputDir/impl_netlist.v -mode timesim -sdf_anno true"
    )
    tcl_data.append("")
    tcl_data.append("write_bitstream -force $outputDir/rio.bit")
    tcl_data.append("")
    tcl_data.append("exit")
    tcl_data.append("")
    open(f"{project['FIRMWARE_PATH']}/rio.tcl", "w").write("\n".join(tcl_data))


def buildsys_diamond(project):
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
    for vfile in project["verilog_files"]:
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
    pcf_data.append(
        'IOBUF  PORT "LEDR"              IO_TYPE=LVCMOS33 PULLMODE=DOWN;'
    )
    pcf_data.append(
        'IOBUF  PORT "LEDG"              IO_TYPE=LVCMOS33 PULLMODE=DOWN;'
    )
    pcf_data.append('IOBUF  PORT "SCL"               IO_TYPE=LVCMOS33 PULLMODE=UP;')
    pcf_data.append('IOBUF  PORT "SDA"               IO_TYPE=LVCMOS33 PULLMODE=UP;')
    pcf_data.append("")
    for pname, pins in project["pinlists"].items():
        pcf_data.append(f"### {pname} ###")
        for pin in pins:
            if pin[1].startswith("EXPANSION"):
                continue
            pcf_data.append(f'LOCATE COMP "{pin[0]}"           SITE "{pin[1]}";')
        pcf_data.append("")
    pcf_data.append("")
    open(f"{project['PINS_PATH']}/pins.lpf", "w").write("\n".join(pcf_data))
