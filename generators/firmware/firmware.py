import sys
import os
from .buildsys import *
from .testbench import testbench


def verilog_top(project):
    top_arguments = []
    for pname in sorted(list(project["pinlists"])):
        pins = project["pinlists"][pname]
        for pin in pins:
            if pin[1].startswith("EXPANSION"):
                continue
            top_arguments.append(f"{pin[2].lower()} {pin[0]}")

    top_data = []
    top_data.append("/*")
    top_data.append(f"    ######### {project['jdata']['name']} #########")
    top_data.append("*/")
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

    if project["osc_clock"]:
        top_data.append("    wire sysclk;")
        top_data.append("    wire locked;")
        top_data.append("    pll mypll(sysclk_in, sysclk, locked);")
        top_data.append("")

    if project["jdata"].get("toolchain") == "diamond":
        top_data.append("    // Internal Oscillator")
        top_data.append('    defparam OSCH_inst.NOM_FREQ = "133.00";')
        top_data.append("    OSCH OSCH_inst ( ")
        top_data.append("        .STDBY(1'b0),")
        top_data.append("        .OSC(sysclk),")
        top_data.append("        .SEDSTDBY()")
        top_data.append("    );")
        top_data.append("")

    if "blink" in project["jdata"]:
        top_data.append(
            f"    blink #({int(project['jdata']['clock']['speed']) // 1 // 2}) blink1 ("
        )
        top_data.append("        .clk (sysclk),")
        top_data.append("        .led (BLINK_LED)")
        top_data.append("    );")
        top_data.append("")
        project["verilog_files"].append("blink.v")
        os.system(
            f"cp -a generators/firmware/blink.v* {project['SOURCE_PATH']}/blink.v"
        )

    if "error" in project["jdata"]:
        if project["jdata"]["error"].get("invert"):
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
    for plugin in project["plugins"]:
        if hasattr(project["plugins"][plugin], "defs"):
            defs = project["plugins"][plugin].defs()
            if defs:
                top_data.append("")
                top_data.append("")
                top_data.append(f"    // {plugin}")
                top_data += defs

    # expansion wires
    expansion_size = {}
    for expansions in project["expansions"].values():
        for enum, size in expansions.items():
            expansion_size[enum] = size
    expansion_ports = {}
    for pname, pins in project["pinlists"].items():
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
    #top_data.append("")

    for pname, pins in project["pinlists"].items():
        for pin in pins:
            if pin[1].startswith("EXPANSION"):
                if pin[2] == "OUTPUT":
                    top_data.append(f"    wire {pin[0]};")
                else:
                    top_data.append(f"    wire {pin[0]};")

    jointEnables = []
    for num, joint in enumerate(project["jointnames"]):
        top_data.append(f"    wire {joint['_prefix']}Enable;")
        jointEnables.append(f"{joint['_prefix']}Enable")

    if "enable" in project["jdata"]:
        jointEnablesStr = " || ".join(jointEnables)
        if project["jdata"]["enable"].get("invert", False):
            top_data.append(f"    wire ENA_INV;")
            top_data.append(f"    assign ENA = ~ENA_INV;")
            top_data.append(f"    assign ENA_INV = ({jointEnablesStr}) && ~ERROR;")
        else:
            top_data.append(f"    assign ENA = ({jointEnablesStr}) && ~ERROR;")
        top_data.append("")

    if project["voutnames"]:
        top_data.append(f"    // vouts {project['vouts']}")
        for num, vout in enumerate(project["voutnames"]):
            top_data.append(f"    wire signed [31:0] {vout['_prefix']};")
        top_data.append("")

    if project["vinnames"]:
        top_data.append(f"    // vins {project['vins']}")
        for num, vin in enumerate(project["vinnames"]):
            top_data.append(f"    wire signed [31:0] {vin['_prefix']};")
        top_data.append("")

    if project["jointnames"]:
        top_data.append(f"    // joints {project['joints']}")
        for num, joint in enumerate(project["jointnames"]):
            top_data.append(f"    wire signed [31:0] {joint['_prefix']}FreqCmd;")
        for num, joint in enumerate(project["jointnames"]):
            top_data.append(f"    wire signed [31:0] {joint['_prefix']}Feedback;")
        top_data.append("")

    top_data.append(f"    // rx_data {project['rx_data_size']}")
    pos = project["data_size"]

    top_data.append("    wire [31:0] header_rx;")
    top_data.append(
        f"    assign header_rx = {{rx_data[{pos-3*8-1}:{pos-3*8-8}], rx_data[{pos-2*8-1}:{pos-2*8-8}], rx_data[{pos-1*8-1}:{pos-1*8-8}], rx_data[{pos-1}:{pos-8}]}};"
    )
    pos -= 32

    for num, joint in enumerate(project["jointnames"]):
        top_data.append(
            f"    assign {joint['_prefix']}FreqCmd = {{rx_data[{pos-3*8-1}:{pos-3*8-8}], rx_data[{pos-2*8-1}:{pos-2*8-8}], rx_data[{pos-1*8-1}:{pos-1*8-8}], rx_data[{pos-1}:{pos-8}]}};"
        )
        pos -= 32

    for num, vout in enumerate(project["voutnames"]):
        top_data.append(
            f"    assign {vout['_prefix']} = {{rx_data[{pos-3*8-1}:{pos-3*8-8}], rx_data[{pos-2*8-1}:{pos-2*8-8}], rx_data[{pos-1*8-1}:{pos-1*8-8}], rx_data[{pos-1}:{pos-8}]}};"
        )
        pos -= 32

    for dbyte in range(project["joints_en_total"] // 8):
        for num in range(8):
            bitnum = dbyte * 8 + (7 - num)
            if bitnum < project["joints"]:
                jname = project["jointnames"][bitnum]["_prefix"]
                top_data.append(f"    assign {jname}Enable = rx_data[{pos-1}];")
            pos -= 1

    for dbyte in range(project["douts_total"] // 8):
        for num in range(8):
            bitnum = num + (dbyte * 8)
            if bitnum < project["douts"]:
                dname = project["doutnames"][bitnum]["_prefix"]
                if project["doutnames"][bitnum].get("invert", False):
                    top_data.append(f"    assign {dname} = ~rx_data[{pos-1}];")
                else:
                    top_data.append(f"    assign {dname} = rx_data[{pos-1}];")
            else:
                top_data.append(f"    // assign DOUTx = rx_data[{pos-1}];")
            pos -= 1

    #top_data.append("")
    top_data.append(f"    // tx_data {project['tx_data_size']}")
    top_data.append("    assign tx_data = {")
    top_data.append(
        "        header_tx[7:0], header_tx[15:8], header_tx[23:16], header_tx[31:24],"
    )

    for num, joint in enumerate(project["jointnames"]):
        top_data.append(
            f"        {joint['_prefix']}Feedback[7:0], {joint['_prefix']}Feedback[15:8], {joint['_prefix']}Feedback[23:16], {joint['_prefix']}Feedback[31:24],"
        )

    for num, vin in enumerate(project["vinnames"]):
        top_data.append(
            f"        {vin['_prefix']}[7:0], {vin['_prefix']}[15:8], {vin['_prefix']}[23:16], {vin['_prefix']}[31:24],"
        )

    tdins = []
    ldin = project["dins"]
    for dbyte in range(project["dins_total"] // 8):
        for num in range(8):
            bitnum = num + (dbyte * 8)
            if bitnum < project["dins"]:
                dname = project["dinnames"][bitnum]["_prefix"]
                din_data = project["dinnames"][bitnum]
                if bitnum < ldin and din_data.get("invert", False):
                    tdins.append(f"~{dname}")
                else:
                    tdins.append(f"{dname}")
            else:
                tdins.append(f"1'd0")

    fill = project["data_size"] - project["tx_data_size"]

    if fill > 0:
        top_data.append(f"        {', '.join(tdins)},")
        top_data.append(f"        {fill}'d0")
    else:
        top_data.append(f"        {', '.join(tdins)}")
    top_data.append("    };")
    #top_data.append("")

    for pname, pins in project["pinlists"].items():
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
    #top_data.append("")

    for plugin in project["plugins"]:
        if hasattr(project["plugins"][plugin], "funcs"):
            funcs = project["plugins"][plugin].funcs()
            if funcs:
                top_data.append("")
                top_data.append(f"    // {plugin}")
                top_data += funcs

    top_data.append("endmodule")
    top_data.append("")
    open(f"{project['SOURCE_PATH']}/rio.v", "w").write("\n".join(top_data))
    project["verilog_files"].append("rio.v")


def generate(project):
    print("generating firmware")

    # general verilog-files
    project["verilog_files"].append("debouncer.v")
    os.system(
        f"cp -a generators/firmware/debouncer.v* {project['SOURCE_PATH']}/debouncer.v"
    )

    # system clock (pll setup)
    if project["internal_clock"]:
        pass
    elif project["osc_clock"]:
        if project["jdata"]["family"] == "ecp5":
            os.system(
                f"ecppll -f '{project['SOURCE_PATH']}/pll.v' -i {float(project['osc_clock']) / 1000000} -o {float(project['jdata']['clock']['speed']) / 1000000}"
            )
        elif project["jdata"]["type"] == "up5k":
            os.system(
                f"icepll -p -m -f '{project['SOURCE_PATH']}/pll.v' -i {float(project['osc_clock']) / 1000000} -o {float(project['jdata']['clock']['speed']) / 1000000}"
            )
        elif project["jdata"]["family"] == "GW1N-9C":
            os.system(
                f"python3 files/gowin-pll.py -d 'GW1NR-9 C6/I5' -f '{project['SOURCE_PATH']}/pll.v' -i {float(project['osc_clock']) / 1000000} -o {float(project['jdata']['clock']['speed']) / 1000000}"
            )
        else:
            os.system(
                f"icepll -q -m -f '{project['SOURCE_PATH']}/pll.v' -i {float(project['osc_clock']) / 1000000} -o {float(project['jdata']['clock']['speed']) / 1000000}"
            )
        project["verilog_files"].append("pll.v")

    verilog_top(project)
    testbench(project)


    # build files (makefiles/scripts/projects)
    board = project["jdata"].get("board")

    if board == "TangNano9K" or board == "TangNano20K":
        buildsys_gowin(project)

    elif project["jdata"].get("toolchain") == "icestorm":
        buildsys_icestorm(project)

    elif project["jdata"].get("toolchain") == "vivado":
        buildsys_vivado(project)

    elif project["jdata"].get("toolchain") == "diamond":
        buildsys_diamond(project)
