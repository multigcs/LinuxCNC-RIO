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
    makefile_data.append("# Toolchain: Gowin and Icestorm")
    makefile_data.append("")
    makefile_data.append("PROJECT  := rio")
    makefile_data.append("TOP      := rio")
    makefile_data.append(f"FAMILY   := {family}")
    makefile_data.append(f"FAMILY_GOWIN := {family_gowin}")
    makefile_data.append(f"DEVICE   := {ftype}")
    makefile_data.append(f"VERILOGS := {verilogs}")
    makefile_data.append("")
    makefile_data.append("all: $(PROJECT).fs")
    makefile_data.append("")
    makefile_data.append(f"$(PROJECT).json: $(VERILOGS)")
    makefile_data.append(
        "	yosys -q -l yosys.log -p 'synth_gowin -noalu -nowidelut -top $(TOP) -json $(PROJECT).json' $(VERILOGS)"
    )
    makefile_data.append("")
    makefile_data.append("$(PROJECT)_pnr.json: $(PROJECT).json pins.cst")
    makefile_data.append(
        f"	nextpnr-gowin --seed 0 --json $(PROJECT).json --write $(PROJECT)_pnr.json --freq {float(project['jdata']['clock']['speed']) / 1000000} --enable-globals --enable-auto-longwires --device $(DEVICE) --cst pins.cst"
    )
    makefile_data.append("")
    makefile_data.append("$(PROJECT).fs: $(PROJECT)_pnr.json")
    makefile_data.append(
        "	gowin_pack -d ${FAMILY} -o $(PROJECT).fs $(PROJECT)_pnr.json"
    )
    makefile_data.append("")
    makefile_data.append("load: $(PROJECT).fs")
    makefile_data.append(f"	openFPGALoader -b {board.lower()} $(PROJECT).fs -f")
    makefile_data.append("")
    makefile_data.append("clean:")
    makefile_data.append(
        "	rm -rf $(PROJECT).fs $(PROJECT).json $(PROJECT)_pnr.json $(PROJECT).tcl abc.history impl yosys.log"
    )
    makefile_data.append("")
    makefile_data.append("gowin_build: impl/pnr/project.fs")
    makefile_data.append("")
    makefile_data.append("$(PROJECT).tcl: pins.cst $(VERILOGS)")
    makefile_data.append(
        '	@echo "set_device -name $(FAMILY_GOWIN) $(DEVICE)" > $(PROJECT).tcl'
    )
    makefile_data.append(
        '	@for VAR in $?; do echo $$VAR | grep -s -q "\.v$$" && echo "add_file $$VAR" >> $(PROJECT).tcl; done'
    )
    makefile_data.append('	@echo "add_file pins.cst" >> $(PROJECT).tcl')
    makefile_data.append('	@echo "set_option -top_module $(TOP)" >> $(PROJECT).tcl')
    makefile_data.append('	@echo "set_option -verilog_std v2001" >> $(PROJECT).tcl')
    makefile_data.append('	@echo "set_option -vhdl_std vhd2008" >> $(PROJECT).tcl')
    set_options = project["jdata"].get(
        "set_options",
        (
            "use_sspi_as_gpio",
            "use_mspi_as_gpio",
            "use_done_as_gpio",
            "use_ready_as_gpio",
            "use_reconfign_as_gpio",
            "use_i2c_as_gpio",
        ),
    )
    for set_option in set_options:
        makefile_data.append(f'	@echo "set_option -{set_option} 1" >> $(PROJECT).tcl')
    makefile_data.append('	@echo "run all" >> $(PROJECT).tcl')
    makefile_data.append("")
    makefile_data.append("impl/pnr/project.fs: $(PROJECT).tcl")
    makefile_data.append("	gw_sh $(PROJECT).tcl")
    makefile_data.append("")
    makefile_data.append("gowin_load: impl/pnr/project.fs")
    makefile_data.append(f"	openFPGALoader -b {board.lower()} impl/pnr/project.fs -f")
    makefile_data.append("")
    makefile_data.append("")
    open(f"{project['GATEWARE_PATH']}/Makefile", "w").write("\n".join(makefile_data))

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
    elif family == "GW2A-18C":
        prj_data.append('    <Device name="" pn="">gw2a18c-011</Device>')
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
    open(f"{project['GATEWARE_PATH']}/rio.gprj", "w").write("\n".join(prj_data))

    os.system(f"mkdir -p {project['GATEWARE_PATH']}/impl")
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
    open(f"{project['GATEWARE_PATH']}/impl/project_process_config.json", "w").write(
        pps_data
    )


def buildsys_icestorm(project):
    if project["jdata"]["family"] == "ecp5":
        pins_lpf(project)
        bitfileName = "$(PROJECT).bit"
    else:
        pins_pcf(project)
        bitfileName = "$(PROJECT).bin"

    verilogs = " ".join(project["verilog_files"])
    makefile_data = []
    makefile_data.append("")
    makefile_data.append("# Toolchain: Icestorm")
    makefile_data.append("")
    makefile_data.append("PROJECT  := rio")
    makefile_data.append("TOP      := rio")
    makefile_data.append(f"FAMILY   := {project['jdata']['family']}")
    makefile_data.append(f"TYPE     := {project['jdata']['type']}")
    makefile_data.append(f"PACKAGE  := {project['jdata']['package']}")
    makefile_data.append(f"VERILOGS := {verilogs}")
    makefile_data.append("")
    makefile_data.append(f"all: {bitfileName}")
    makefile_data.append("")
    makefile_data.append("$(PROJECT).json: $(VERILOGS)")
    if project["jdata"]["type"] == "up5k":
        makefile_data.append(
            "	yosys -q -l yosys.log -p 'synth_$(FAMILY) -dsp -top $(TOP) -json $(PROJECT).json' $(VERILOGS)"
        )
    else:
        makefile_data.append(
            "	yosys -q -l yosys.log -p 'synth_$(FAMILY) -top $(TOP) -json $(PROJECT).json' $(VERILOGS)"
        )
    makefile_data.append("")
    if project["jdata"]["family"] == "ecp5":
        makefile_data.append("$(PROJECT).config: $(PROJECT).json pins.lpf")
        makefile_data.append(
            "	nextpnr-${FAMILY} -q -l nextpnr.log --${TYPE} --package ${PACKAGE} --json $(PROJECT).json --lpf pins.lpf --textcfg $(PROJECT).config"
        )
        makefile_data.append('	@echo ""')
        makefile_data.append('	@grep -B 1 "%$$" nextpnr.log')
        makefile_data.append('	@echo ""')
        makefile_data.append("")
        makefile_data.append(f"{bitfileName}: $(PROJECT).config")
        makefile_data.append(
            f"	ecppack --svf $(PROJECT).svf $(PROJECT).config {bitfileName}"
        )
        makefile_data.append("")
        makefile_data.append(f"$(PROJECT).svf: {bitfileName}")
        makefile_data.append("")
        makefile_data.append("clean:")
        makefile_data.append(
            f"	rm -rf {bitfileName} $(PROJECT).svf $(PROJECT).config $(PROJECT).json yosys.log nextpnr.log"
        )
        makefile_data.append("")
    else:
        makefile_data.append("$(PROJECT).asc: $(PROJECT).json pins.pcf")
        makefile_data.append(
            "	nextpnr-${FAMILY} -q -l nextpnr.log --${TYPE} --package ${PACKAGE} --json $(PROJECT).json --pcf pins.pcf --asc $(PROJECT).asc"
        )
        makefile_data.append('	@echo ""')
        makefile_data.append('	@grep -B 1 "%$$" nextpnr.log')
        makefile_data.append('	@echo ""')
        makefile_data.append("")
        makefile_data.append(f"{bitfileName}: $(PROJECT).asc")
        makefile_data.append(f"	icepack $(PROJECT).asc {bitfileName}")
        makefile_data.append("")
        makefile_data.append("clean:")
        makefile_data.append(
            f"	rm -rf {bitfileName} $(PROJECT).asc $(PROJECT).json yosys.log nextpnr.log"
        )
        makefile_data.append("")
    makefile_data.append("check:")
    makefile_data.append("	verilator --top-module $(PROJECT) --lint-only -Wall *.v")
    makefile_data.append("")
    makefile_data.append(f"sim: $(VERILOGS)")
    makefile_data.append(
        f"	verilator --cc --exe --build -j 0 -Wall --top-module $(PROJECT) sim_main.cpp $(VERILOGS)"
    )
    makefile_data.append("")
    makefile_data.append(f"tinyprog: {bitfileName}")
    makefile_data.append(f"	tinyprog -p {bitfileName}")
    makefile_data.append("")
    flashcmd = project["jdata"].get("flashcmd")
    if flashcmd:
        makefile_data.append(f"load: {bitfileName}")
        makefile_data.append(f"	{flashcmd}")
    else:
        makefile_data.append(f"load: {bitfileName}")
        makefile_data.append(f"	 openFPGALoader -b ice40_generic {bitfileName}")
    makefile_data.append("")
    makefile_data.append("")
    open(f"{project['GATEWARE_PATH']}/Makefile", "w").write("\n".join(makefile_data))


def buildsys_ise(project):
    pins_ucf(project)

    verilogs = " ".join(project["verilog_files"])
    makefile_data = []
    makefile_data.append("")
    makefile_data.append("# Toolchain: ISE/Webpack")
    makefile_data.append("")
    makefile_data.append("PROJECT  := rio")
    makefile_data.append("TOP      := rio")
    makefile_data.append(f"PART     := {project['jdata']['type']}")
    makefile_data.append(f"VERILOGS := {verilogs}")
    makefile_data.append("")
    makefile_data.append("all: $(PROJECT).bit")
    makefile_data.append("")
    makefile_data.append("$(PROJECT)-modules.v: $(VERILOGS)")
    makefile_data.append("	cat $(VERILOGS) > $(PROJECT)-modules.v")
    makefile_data.append("")
    makefile_data.append("$(PROJECT).ngc: $(PROJECT)-modules.v")
    makefile_data.append(
        "	echo 'run -ifn $(PROJECT)-modules.v -ifmt Verilog -ofn $(PROJECT).ngc -top $(TOP) -p $(PART) -opt_mode Speed -opt_level 1' | xst"
    )
    makefile_data.append("")
    makefile_data.append("$(PROJECT).ngd: $(PROJECT).ngc pins.ucf")
    makefile_data.append("	ngdbuild -p $(PART) -uc pins.ucf $(PROJECT).ngc")
    makefile_data.append("")
    makefile_data.append("$(PROJECT).ncd: $(PROJECT).ngd")
    makefile_data.append("	map -detail -pr b $(PROJECT).ngd")
    makefile_data.append("")
    makefile_data.append("parout.ncd: $(PROJECT).ncd $(PROJECT).pcf")
    makefile_data.append("	par -w $(PROJECT).ncd parout.ncd $(PROJECT).pcf")
    makefile_data.append("")
    makefile_data.append("$(PROJECT).bit: parout.ncd $(PROJECT).pcf")
    makefile_data.append(
        "	bitgen -w -g StartUpClk:CClk -g CRC:Enable parout.ncd $(PROJECT).bit $(PROJECT).pcf"
    )
    makefile_data.append("")
    makefile_data.append("clean:")
    makefile_data.append(
        "	rm -rf $(PROJECT).ngc $(PROJECT).ngd $(PROJECT).ncd parout.ncd $(PROJECT).bit"
    )
    makefile_data.append("")
    makefile_data.append("load: $(PROJECT).bit")
    makefile_data.append("	openFPGALoader -v -c usb-blaster $(PROJECT).bit")
    makefile_data.append("")
    makefile_data.append("")
    open(f"{project['GATEWARE_PATH']}/Makefile", "w").write("\n".join(makefile_data))


def buildsys_vivado(project):
    pins_xdc(project)

    verilogs = " ".join(project["verilog_files"])
    makefile_data = []
    makefile_data.append("")
    makefile_data.append("# Toolchain: Vivado")
    makefile_data.append("")
    makefile_data.append("PROJECT  := rio")
    makefile_data.append("TOP      := rio")
    makefile_data.append(f"PART     := {project['jdata']['type']}")
    makefile_data.append(f"VERILOGS := {verilogs}")
    makefile_data.append("")
    makefile_data.append("all: build/$(PROJECT).bit")
    makefile_data.append("")
    makefile_data.append("$(PROJECT).tcl: pins.xdc $(VERILOGS)")
    makefile_data.append('	@echo "set outputDir ./build" > $(PROJECT).tcl')
    makefile_data.append('	@echo "file mkdir \$$outputDir" >> $(PROJECT).tcl')
    makefile_data.append('	@echo "" >> $(PROJECT).tcl')
    makefile_data.append(
        '	@for VAR in $?; do echo $$VAR | grep -s -q "\.v$$" && echo "read_verilog $$VAR" >> $(PROJECT).tcl; done'
    )
    makefile_data.append('	@echo "read_xdc pins.xdc" >> $(PROJECT).tcl')
    makefile_data.append("	@echo " " >> $(PROJECT).tcl")
    makefile_data.append(
        '	@echo "synth_design -top $(TOP) -part $(PART)" >> $(PROJECT).tcl'
    )
    makefile_data.append(
        '	@echo "write_checkpoint -force \$$outputDir/post_synth.dcp" >> $(PROJECT).tcl'
    )
    makefile_data.append(
        '	@echo "report_timing_summary -file \$$outputDir/post_synth_timing_summary.rpt" >> $(PROJECT).tcl'
    )
    makefile_data.append(
        '	@echo "report_utilization -file \$$outputDir/post_synth_util.rpt" >> $(PROJECT).tcl'
    )
    makefile_data.append('	@echo "" >> $(PROJECT).tcl')
    makefile_data.append('	@echo "opt_design" >> $(PROJECT).tcl')
    makefile_data.append('	@echo "place_design" >> $(PROJECT).tcl')
    makefile_data.append(
        '	@echo "report_clock_utilization -file \$$outputDir/clock_util.rpt" >> $(PROJECT).tcl'
    )
    makefile_data.append('	@echo "" >> $(PROJECT).tcl')
    makefile_data.append(
        '	@echo "write_checkpoint -force \$$outputDir/post_place.dcp" >> $(PROJECT).tcl'
    )
    makefile_data.append(
        '	@echo "report_utilization -file \$$outputDir/post_place_util.rpt" >> $(PROJECT).tcl'
    )
    makefile_data.append(
        '	@echo "report_timing_summary -file \$$outputDir/post_place_timing_summary.rpt" >> $(PROJECT).tcl'
    )
    makefile_data.append('	@echo "" >> $(PROJECT).tcl')
    makefile_data.append('	@echo "route_design" >> $(PROJECT).tcl')
    makefile_data.append(
        '	@echo "write_checkpoint -force \$$outputDir/post_route.dcp" >> $(PROJECT).tcl'
    )
    makefile_data.append(
        '	@echo "report_route_status -file \$$outputDir/post_route_status.rpt" >> $(PROJECT).tcl'
    )
    makefile_data.append(
        '	@echo "report_timing_summary -file \$$outputDir/post_route_timing_summary.rpt" >> $(PROJECT).tcl'
    )
    makefile_data.append(
        '	@echo "report_power -file \$$outputDir/post_route_power.rpt" >> $(PROJECT).tcl'
    )
    makefile_data.append(
        '	@echo "report_drc -file \$$outputDir/post_imp_drc.rpt" >> $(PROJECT).tcl'
    )
    makefile_data.append('	@echo "" >> $(PROJECT).tcl')
    makefile_data.append(
        '	@echo "write_verilog -force \$$outputDir/impl_netlist.v -mode timesim -sdf_anno true" >> $(PROJECT).tcl'
    )
    makefile_data.append('	@echo "" >> $(PROJECT).tcl')
    makefile_data.append(
        '	@echo "write_bitstream -force \$$outputDir/$(PROJECT).bit" >> $(PROJECT).tcl'
    )
    makefile_data.append('	@echo "" >> $(PROJECT).tcl')
    makefile_data.append('	@echo "exit" >> $(PROJECT).tcl')
    makefile_data.append("")
    makefile_data.append("build/$(PROJECT).bit: $(PROJECT).tcl")
    makefile_data.append("	vivado -mode batch -source $(PROJECT).tcl")
    makefile_data.append("")
    makefile_data.append("clean:")
    makefile_data.append("	rm -rf build $(PROJECT).tcl *.jou *.log .Xil")
    makefile_data.append("")
    makefile_data.append("xc3sprog: build/$(PROJECT).bit")
    makefile_data.append("	xc3sprog -c nexys4 build/$(PROJECT).bit")
    makefile_data.append("")
    makefile_data.append("load: build/$(PROJECT).bit")
    makefile_data.append("	openFPGALoader -b arty -f build/$(PROJECT).bit")
    makefile_data.append("")
    makefile_data.append("")
    open(f"{project['GATEWARE_PATH']}/Makefile", "w").write("\n".join(makefile_data))


def buildsys_diamond(project):
    pins_lpf(project, diamond=True)

    verilogs = " ".join(project["verilog_files"])
    makefile_data = []
    makefile_data.append("")
    makefile_data.append("# Toolchain: Diamond")
    makefile_data.append("")
    makefile_data.append("PROJECT  := rio")
    makefile_data.append("TOP      := rio")
    makefile_data.append(f"PART     := {project['jdata']['type']}")
    makefile_data.append(f"VERILOGS := {verilogs}")
    makefile_data.append("")
    makefile_data.append("all: build/$(PROJECT)_build.bit")
    makefile_data.append("")
    makefile_data.append("")
    makefile_data.append("$(PROJECT).tcl: $(VERILOGS)")
    makefile_data.append(
        '	@echo "prj_project new -name $(PROJECT) -impl build -dev $(PART) -lpf pins.lpf" > $(PROJECT).tcl'
    )
    makefile_data.append(
        '	@for VAR in $?; do echo $$VAR | grep -s -q "\.v$$" && echo "prj_src add $$VAR" >> $(PROJECT).tcl; done'
    )
    makefile_data.append('	@echo "prj_impl option top $(TOP)" >> $(PROJECT).tcl')
    makefile_data.append('	@echo "prj_project save" >> $(PROJECT).tcl')
    makefile_data.append('	@echo "prj_project close" >> $(PROJECT).tcl')
    makefile_data.append("")
    makefile_data.append("syn.tcl: $(PROJECT).tcl")
    makefile_data.append('	@echo "prj_project open $(PROJECT).ldf" >> syn.tcl')
    makefile_data.append('	@echo "prj_run Synthesis -impl build" >> syn.tcl')
    makefile_data.append('	@echo "prj_run Translate -impl build" >> syn.tcl')
    makefile_data.append('	@echo "prj_run Map -impl build" >> syn.tcl')
    makefile_data.append('	@echo "prj_run PAR -impl build" >> syn.tcl')
    makefile_data.append('	@echo "prj_run PAR -impl build -task PARTrace" >> syn.tcl')
    makefile_data.append('	@echo "prj_run Export -impl build -task Bitgen" >> syn.tcl')
    makefile_data.append(
        '	@echo "prj_run Export -impl build -task Jedecgen" >> syn.tcl'
    )
    makefile_data.append('	@echo "prj_project close" >> syn.tcl')
    makefile_data.append("")
    makefile_data.append("$(PROJECT).ldf: syn.tcl")
    makefile_data.append("	diamondc $(PROJECT).tcl")
    makefile_data.append("")
    makefile_data.append("build/$(PROJECT)_build.bit: $(PROJECT).ldf")
    makefile_data.append("	diamondc syn.tcl")
    makefile_data.append("")
    makefile_data.append("load:")
    makefile_data.append("	openFPGALoader -c usb-blaster build/$(PROJECT)_build.bit")
    makefile_data.append("")
    makefile_data.append("clean:")
    makefile_data.append("	rm -rf build $(PROJECT).ldf $(PROJECT).tcl syn.tcl")
    makefile_data.append("")
    makefile_data.append("")
    open(f"{project['GATEWARE_PATH']}/Makefile", "w").write("\n".join(makefile_data))


def buildsys_quartus(project):
    pins_qdf(project)

    if project["osc_clock"]:
        clkname = "sysclk_in"
    else:
        clkname = "sysclk"

    family = project["jdata"]["family"]
    ftype = project["jdata"]["type"]
    verilogs = " ".join(project["verilog_files"])
    makefile_data = []
    makefile_data.append("")
    makefile_data.append("# Toolchain: Quartus")
    makefile_data.append("")
    makefile_data.append("PROJECT   := rio")
    makefile_data.append("TOP       := rio")
    makefile_data.append(f"PART      := {ftype}")
    makefile_data.append(f'FAMILY    := "{family}"')
    makefile_data.append(f"VERILOGS  := {verilogs}")
    makefile_data.append("")
    makefile_data.append("QC   = quartus_sh")
    makefile_data.append("QP   = quartus_pgm")
    makefile_data.append("QM   = quartus_map")
    makefile_data.append("QF   = quartus_fit")
    makefile_data.append("QA   = quartus_asm")
    makefile_data.append("QS   = quartus_sta")
    makefile_data.append("ECHO = echo")
    makefile_data.append("Q   ?= @")
    makefile_data.append("")
    makefile_data.append("STAMP = echo done >")
    makefile_data.append("")
    makefile_data.append("QCFLAGS = --flow compile")
    makefile_data.append("QPFLAGS =")
    makefile_data.append(
        "QMFLAGS = --read_settings_files=on $(addprefix --source=,$(VERILOGS))"
    )
    makefile_data.append("QFFLAGS = --part=$(PART) --read_settings_files=on")
    makefile_data.append("")
    makefile_data.append("ASIGN = $(PROJECT).qsf $(PROJECT).qpf")
    makefile_data.append("")
    makefile_data.append("all: $(PROJECT)")
    makefile_data.append("")
    makefile_data.append("map: smart.log $(PROJECT).map.rpt")
    makefile_data.append("fit: smart.log $(PROJECT).fit.rpt")
    makefile_data.append("asm: smart.log $(PROJECT).asm.rpt")
    makefile_data.append("sta: smart.log $(PROJECT).sta.rpt")
    makefile_data.append("smart: smart.log")
    makefile_data.append("")
    makefile_data.append("$(ASIGN):")
    makefile_data.append('	$(Q)$(ECHO) "Generating asignment files."')
    makefile_data.append("	$(QC) --prepare -f $(FAMILY) -t $(TOP) $(PROJECT)")
    makefile_data.append("	echo >> $(PROJECT).qsf")
    makefile_data.append("	cat pins.qdf >> $(PROJECT).qsf")
    makefile_data.append("")
    makefile_data.append("smart.log: $(ASIGN)")
    makefile_data.append('	$(Q)$(ECHO) "Generating smart.log."')
    makefile_data.append("	$(QC) --determine_smart_action $(PROJECT) > smart.log")
    makefile_data.append("")
    makefile_data.append("$(PROJECT): smart.log $(PROJECT).asm.rpt $(PROJECT).sta.rpt")
    makefile_data.append("")
    makefile_data.append("$(PROJECT).map.rpt: map.chg $(VERILOGS)")
    makefile_data.append("	$(QM) $(QMFLAGS) $(PROJECT)")
    makefile_data.append("	$(STAMP) fit.chg")
    makefile_data.append("")
    makefile_data.append("$(PROJECT).fit.rpt: fit.chg $(PROJECT).map.rpt")
    makefile_data.append("	$(QF) $(QFFLAGS) $(PROJECT)")
    makefile_data.append("	$(STAMP) asm.chg")
    makefile_data.append("	$(STAMP) sta.chg")
    makefile_data.append("")
    makefile_data.append("$(PROJECT).asm.rpt: asm.chg $(PROJECT).fit.rpt")
    makefile_data.append("	$(QA) $(PROJECT)")
    makefile_data.append("")
    makefile_data.append("$(PROJECT).sta.rpt: sta.chg $(PROJECT).fit.rpt")
    makefile_data.append("	$(QS) $(PROJECT)")
    makefile_data.append("")
    makefile_data.append("map.chg:")
    makefile_data.append("	$(STAMP) map.chg")
    makefile_data.append("fit.chg:")
    makefile_data.append("	$(STAMP) fit.chg")
    makefile_data.append("sta.chg:")
    makefile_data.append("	$(STAMP) sta.chg")
    makefile_data.append("asm.chg:")
    makefile_data.append("	$(STAMP) asm.chg")
    makefile_data.append("")
    makefile_data.append("clean:")
    makefile_data.append('	$(Q)$(ECHO) "Cleaning."')
    makefile_data.append("	rm -rf db incremental_db")
    makefile_data.append(
        "	rm -f smart.log *.rpt *.sof *.chg *.qsf *.qpf *.summary *.smsg *.pin *.jdi"
    )
    makefile_data.append("")
    makefile_data.append("load: prog")
    makefile_data.append("prog: $(PROJECT).sof")
    makefile_data.append('	$(Q)$(ECHO) "Programming."')
    makefile_data.append('	$(QP) --no_banner --mode=jtag -o "P;$(PROJECT).sof"')
    makefile_data.append("")
    makefile_data.append("")
    open(f"{project['GATEWARE_PATH']}/Makefile", "w").write("\n".join(makefile_data))

    clock = project['jdata']['clock'].get('osc', project['jdata']['clock']['speed'])
    sdc_data = []
    sdc_data.append("")
    sdc_data.append(f"create_clock -name {clkname} -period \"{float(clock) / 1000000} MHz\" [get_ports {clkname}]")
    sdc_data.append("derive_pll_clocks")
    sdc_data.append("derive_clock_uncertainty")
    sdc_data.append("")
    open(f"{project['GATEWARE_PATH']}/rio.sdc", "w").write("\n".join(sdc_data))


def buildsys_verilator(project):
    pins_qdf(project)

    verilogs = " ".join(project["verilog_files"])
    makefile_data = []
    makefile_data.append("")
    makefile_data.append("PROJECT   := rio")
    makefile_data.append("TOP       := rio")
    makefile_data.append(f"VERILOGS  := {verilogs}")
    makefile_data.append("")
    makefile_data.append("all: obj_dir/V$(TOP)")
    makefile_data.append("")
    makefile_data.append("obj_dir/V$(TOP): $(VERILOGS)")
    makefile_data.append("	verilator --cc --exe --build -j 0 -Wall main.cpp $(TOP).v")
    makefile_data.append("")
    makefile_data.append("clean:")
    makefile_data.append("	rm -rf obj_dir")
    makefile_data.append("")
    makefile_data.append("")
    open(f"{project['GATEWARE_PATH']}/Makefile", "w").write("\n".join(makefile_data))

    top_arguments = []
    for pname in sorted(list(project["pinlists"])):
        pins = project["pinlists"][pname]
        for pin in pins:
            if pin[1].startswith("EXPANSION"):
                continue
            if pin[1] == "USRMCLK":
                continue

            top_arguments.append(
                {
                    "dir": pin[2].lower(),
                    "name": pin[0],
                }
            )

    print(top_arguments)

    main_cpp = []
    main_cpp.append('#include "Vrio.h"')
    main_cpp.append('#include "verilated.h"')
    main_cpp.append("")
    main_cpp.append("#include <stdio.h>")
    main_cpp.append("#include <sys/types.h>")
    main_cpp.append("#include <sys/stat.h>")
    main_cpp.append("#include <fcntl.h>")
    main_cpp.append("#include <unistd.h>")
    main_cpp.append("")
    main_cpp.append(f"#define BUFFER_BIT {project['data_size']}")
    main_cpp.append("#define BUFFER_BYTES (BUFFER_BIT / 8)")
    main_cpp.append("")
    main_cpp.append("int main(int argc, char** argv) {")
    main_cpp.append("")
    main_cpp.append("    uint8_t spi_tx[BUFFER_BYTES] = {0x74, 0x69, 0x72, 0x77};")
    main_cpp.append("    uint8_t spi_rx[BUFFER_BYTES];")
    main_cpp.append("    int spi_rx_num = 0;")
    main_cpp.append("    int spi_rx_bit = 0;")
    main_cpp.append("    int spi_rx_cs = 1;")
    main_cpp.append("")
    main_cpp.append("    VerilatedContext* contextp = new VerilatedContext;")
    main_cpp.append("    contextp->commandArgs(argc, argv);")
    main_cpp.append("    Vrio* rio = new Vrio{contextp};")
    for argument in top_arguments:
        main_cpp.append(f"    rio->{argument['name']} = 0;")
    main_cpp.append("    rio->eval();")
    main_cpp.append("")
    main_cpp.append("    int counter = 0;")
    main_cpp.append("    int last = 0;")
    main_cpp.append("    while (!contextp->gotFinish()) {")
    main_cpp.append("        rio->sysclk = 1 - rio->sysclk;")
    main_cpp.append("        rio->eval();")
    main_cpp.append("        rio->sysclk = 1 - rio->sysclk;")
    main_cpp.append("        rio->eval();")
    main_cpp.append("")
    main_cpp.append("        if (rio->BLINK_LED != last) {")
    for argument in top_arguments:
        if argument["dir"] == "output":
            main_cpp.append(
                f"            fprintf(stdout, \"{argument['name']}=%i \", rio->{argument['name']});"
            )
    main_cpp.append(f'            fprintf(stdout, "\\n");')
    main_cpp.append("        }")
    main_cpp.append("        last = rio->BLINK_LED;")
    main_cpp.append("        ")
    main_cpp.append("        if (counter++ > 10000) {")
    main_cpp.append("            counter = 0;")
    main_cpp.append("            if (rio->INTERFACE_SPI_SSEL == 0) {")
    main_cpp.append("                if (rio->INTERFACE_SPI_SCK == 0) {")
    main_cpp.append("                    if (spi_rx_bit < 8) {")
    main_cpp.append(
        "                        if ((spi_tx[spi_rx_num] & (1<<(7-spi_rx_bit))) > 0) {"
    )
    main_cpp.append("                            rio->INTERFACE_SPI_MOSI = 1;")
    main_cpp.append("                        } else {")
    main_cpp.append("                            rio->INTERFACE_SPI_MOSI = 0;")
    main_cpp.append("                        }")
    main_cpp.append("                    }")
    main_cpp.append("                    rio->INTERFACE_SPI_SCK = 1;")
    main_cpp.append("                } else if (spi_rx_num < BUFFER_BYTES) {")
    main_cpp.append("                    if (spi_rx_bit < 8) {")
    main_cpp.append(
        "                        spi_rx[spi_rx_num] |= (rio->INTERFACE_SPI_MISO<<(7-spi_rx_bit));"
    )
    main_cpp.append("                        spi_rx_bit++;")
    main_cpp.append("                    }")
    main_cpp.append("                    if (spi_rx_bit == 8) {")
    main_cpp.append(
        '                        //printf("#spi_rx_num: %i 0x%X %i\\n", spi_rx_num, spi_rx[spi_rx_num], 0);'
    )
    main_cpp.append("")
    main_cpp.append(
        '                        int fd_rx = open("/dev/shm/verilog.rx", O_WRONLY);'
    )
    main_cpp.append("                        write(fd_rx, spi_rx, BUFFER_BYTES);")
    main_cpp.append("                        close(fd_rx);")
    main_cpp.append("                        ")
    main_cpp.append("                        spi_rx_bit = 0;")
    main_cpp.append("                        spi_rx_num++;")
    main_cpp.append("                    }")
    main_cpp.append("                    if (spi_rx_num < BUFFER_BYTES) {")
    main_cpp.append("                        rio->INTERFACE_SPI_SCK = 0;")
    main_cpp.append("                    }")
    main_cpp.append("                } else {")
    main_cpp.append("                    rio->INTERFACE_SPI_SSEL = 1;")
    main_cpp.append("                    spi_rx_bit = 0;")
    main_cpp.append("                    spi_rx_num = 0;")
    main_cpp.append("                }")
    main_cpp.append("            } else if (rio->INTERFACE_SPI_SSEL == 1) {")
    main_cpp.append(
        '                int fd_tx = open("/dev/shm/verilog.tx", O_RDONLY);'
    )
    main_cpp.append("                read(fd_tx, spi_tx, BUFFER_BYTES);")
    main_cpp.append("                close(fd_tx);")
    main_cpp.append("")
    main_cpp.append("                spi_rx_bit = 0;")
    main_cpp.append("                spi_rx_num = 0;")
    main_cpp.append("                rio->INTERFACE_SPI_SSEL = 0;")
    main_cpp.append("                rio->INTERFACE_SPI_SCK = 0;")
    main_cpp.append("            }")
    main_cpp.append("")
    main_cpp.append("        }")
    main_cpp.append("")
    main_cpp.append("    }")
    main_cpp.append("")
    main_cpp.append("    delete rio;")
    main_cpp.append("    delete contextp;")
    main_cpp.append("    return 0;")
    main_cpp.append("}")
    main_cpp.append("")
    main_cpp.append("")

    open(f"{project['GATEWARE_PATH']}/main.cpp", "w").write("\n".join(main_cpp))
