
import os
import graphviz

def generate(project):
    print("generating doc")

    s = graphviz.Digraph('firmware', filename=f'{project["DOC_PATH"]}/flowchart.gv', node_attr={'shape': 'plaintext'})
    s.attr(rankdir='LR', size='15')

    rxdata = []
    txdata = []
    pins_input = []
    pins_output = []

    innerhtml = "<<TABLE bgcolor=\"#fffd7a\" BORDER=\"0\" CELLBORDER=\"1\" CELLSPACING=\"0\">"
    innerhtml += "<TR>"
    innerhtml += f"<TD PORT=\"rx_data\"><B>RX_DATA</B></TD>"
    innerhtml += "</TR>"
    rxdata.append(f"rx_data")
    for num in range(project['joints']):
        innerhtml += "<TR>"
        innerhtml += f"<TD PORT=\"jointFreqCmd{num}\">jointFreqCmd{num}</TD>"
        innerhtml += "</TR>"
        rxdata.append(f"jointFreqCmd{num}")
    for num in range(project['vouts']):
        innerhtml += "<TR>"
        innerhtml += f"<TD PORT=\"setPoint{num}\">setPoint{num}</TD>"
        innerhtml += "</TR>"
        rxdata.append(f"setPoint{num}")
    for num in range(project['joints']):
        innerhtml += "<TR>"
        innerhtml += f"<TD PORT=\"jointEnable{num}\">jointEnable{num}</TD>"
        innerhtml += "</TR>"
        rxdata.append(f"jointEnable{num}")
    for num in range(project['douts']):
        innerhtml += "<TR>"
        innerhtml += f"<TD PORT=\"DOUT{num}\">DOUT{num}</TD>"
        innerhtml += "</TR>"
        rxdata.append(f"DOUT{num}")
        s.edge(f'rx_data:DOUT{num}', f'pins:DOUT{num}', color="blue")
    innerhtml += f"</TABLE>>"
    s.node('rx_data', innerhtml)

    innerhtml = "<<TABLE bgcolor=\"#fffd7a\" BORDER=\"0\" CELLBORDER=\"1\" CELLSPACING=\"0\">"
    innerhtml += "<TR>"
    innerhtml += f"<TD PORT=\"tx_data\"><B>TX_DATA</B></TD>"
    innerhtml += "</TR>"
    txdata.append(f"tx_data")
    for num in range(project['joints']):
        innerhtml += "<TR>"
        innerhtml += f"<TD PORT=\"jointFeedback{num}\">jointFeedback{num}</TD>"
        innerhtml += "</TR>"
        txdata.append(f"jointFeedback{num}")
    for num in range(project['vins']):
        innerhtml += "<TR>"
        innerhtml += f"<TD PORT=\"processVariable{num}\">processVariable{num}</TD>"
        innerhtml += "</TR>"
        txdata.append(f"processVariable{num}")
    for num in range(project['dins']):
        innerhtml += "<TR>"
        innerhtml += f"<TD PORT=\"DIN{num}\">DIN{num}</TD>"
        innerhtml += "</TR>"
        txdata.append(f"DIN{num}")
        s.edge(f'pins:DIN{num}', f'tx_data:DIN{num}', color="green")
    innerhtml += f"</TABLE>>"
    s.node('tx_data', innerhtml)


    innerhtml = "<<TABLE bgcolor=\"#a2c635\" BORDER=\"0\" CELLBORDER=\"1\" CELLSPACING=\"0\">"
    innerhtml += "<TR>"
    innerhtml += f"<TD><B>{project['jdata']['family']} - {project['jdata']['type']}</B></TD>"
    innerhtml += "</TR>"
    for pname in sorted(list(project['pinlists'])):
        pins = project['pinlists'][pname]
        for pin in pins:
            if pin[2] == "INPUT":
                pins_input.append(pin[0])
            else:
                pins_output.append(pin[0])
            innerhtml += "<TR>"
            if pin[2] == "INPUT":
                innerhtml += f"<TD PORT=\"{pin[0]}\">{pin[0]} &lt;- {pin[1]}</TD>"
            else:
                innerhtml += f"<TD PORT=\"{pin[0]}\">{pin[0]} -&gt; {pin[1]}</TD>"
            innerhtml += "</TR>"
    innerhtml += f"</TABLE>>"
    s.node('pins', innerhtml)

    if project['osc_clock']:
        innerhtml = "<<TABLE bgcolor=\"#bca0cc\" BORDER=\"0\" CELLBORDER=\"1\" CELLSPACING=\"0\">"
        innerhtml += "<TR>"
        innerhtml += f"<TD><B>PLL</B></TD>"
        innerhtml += "</TR>"
        innerhtml += "<TR>"
        innerhtml += f"<TD PORT=\"sysclk_in\">sysclk_in {float(project['osc_clock']) // 1000000}MHz</TD>"
        innerhtml += "</TR>"
        innerhtml += "<TR>"
        innerhtml += f"<TD PORT=\"sysclk\">sysclk {float(project['jdata']['clock']['speed']) // 1000000}MHz</TD>"
        innerhtml += "</TR>"
        innerhtml += f"</TABLE>>"
        s.node('pll', innerhtml)
        s.edges([('pins:sysclk_in', 'pll:sysclk_in')])


    for plugin in project['plugins']:
        if hasattr(project['plugins'][plugin], "funcs"):
            module_name = ""
            module_id = ""
            mapping = {}
            module_wires = {}
            funcs = project['plugins'][plugin].funcs()
            code = "\n".join(funcs)
            for line in code.split("\n"):
                line = line.strip()
                if line.endswith("("):
                    module_name = line.split()[0]
                    module_id = line.split()[-2]
                    module_wires[module_id] = []
                elif line.startswith("assign "):
                    wire_to = line.split()[1]
                    wire_from = line.split()[3].strip("!;")
                    mapping[wire_from] = wire_to
                elif line.startswith("."):
                    wire = line.split("(")[1].split(")")[0].split()[0]
                    wire_org = wire
                    if wire in mapping:
                        wire = mapping[wire]
                    if module_id:
                        if wire in pins_input:
                            module_wires[module_id].append((wire, wire_org))
                            s.edge(f'pins:{wire}', f'{module_id}:{wire}', color="green")
                        elif wire in pins_output:
                            module_wires[module_id].append((wire, wire_org))
                            s.edge(f'{module_id}:{wire}', f'pins:{wire}', color="blue")
                        elif wire in txdata:
                            module_wires[module_id].append((wire, wire_org))
                            s.edge(f'{module_id}:{wire}', f'tx_data:{wire}', color="green")
                        elif wire in rxdata:
                            module_wires[module_id].append((wire, wire_org))
                            s.edge(f'rx_data:{wire}', f'{module_id}:{wire}', color="blue")
                        else:
                            module_wires[module_id].append((wire, wire_org))
                    s.node(module_id, module_id)

            for module, wires in module_wires.items():
                innerhtml = "<<TABLE bgcolor=\"#41ad4c\" BORDER=\"0\" CELLBORDER=\"1\" CELLSPACING=\"0\">"
                innerhtml += "<TR>"
                innerhtml += f"<TD><B>{module}</B></TD>"
                innerhtml += "</TR>"
                for wire in wires:
                    innerhtml += "<TR>"
                    innerhtml += f"<TD PORT=\"{wire[0]}\">{wire[0]}</TD>"
                    innerhtml += "</TR>"
                    if wire[1] != wire[0]:
                        innerhtml += "<TR>"
                        innerhtml += f"<TD PORT=\"{wire[1]}\">{wire[1]}</TD>"
                        innerhtml += "</TR>"
                        #s.edges([(f'{module}:{wire[1]}', f'{module}:{wire[0]}')])
                innerhtml += f"</TABLE>>"
                s.node(module, innerhtml)


    s.save()
    os.system(f"dot -Tpng {project['DOC_PATH']}/flowchart.gv > {project['DOC_PATH']}/flowchart.png")




    # index
    innerhtml = "<html>"
    innerhtml += "<img src=\"flowchart.png\" style=\"float:right\"/>"
    innerhtml += f"<H2>General:</H2>"
    innerhtml += "<TABLE>"
    for key in ("name", "description", "toolchain", "family", "type", "package"):
        if key in project['jdata']:
            innerhtml += "<TR>"
            innerhtml += f"<TD>{key.title()}</TD><TD>{project['jdata'][key]}</TD>"
            innerhtml += "</TR>"
    innerhtml += "</TABLE>"


    innerhtml += f"<H2>Files:</H2>"
    innerhtml += "<TABLE>"

    if project['jdata']["toolchain"] == "icestorm" and project['jdata']["family"] == "ecp5":
        innerhtml += "<TR>"
        innerhtml += f"<TD>Bitstream</TD>"
        innerhtml += f"<TD><a href=\"../Firmware/rio.bit\">rio.bit</a></TD>"
        innerhtml += "</TR>"
    elif project['jdata']["toolchain"] == "icestorm":
        innerhtml += "<TR>"
        innerhtml += f"<TD>Bitstream</TD>"
        innerhtml += f"<TD><a href=\"../Firmware/rio.bin\">rio.bin</a></TD>"
        innerhtml += "</TR>"

    innerhtml += "<TR>"
    innerhtml += f"<TD>LinuxCNC Components</TD>"
    innerhtml += f"<TD><a href=\"../LinuxCNC/Components/\">Components</a></TD>"
    innerhtml += "</TR>"

    innerhtml += "<TR>"
    innerhtml += f"<TD>LinuxCNC ConfigSample</TD>"
    innerhtml += f"<TD><a href=\"../LinuxCNC/ConfigSamples/rio/\">ConfigSample</a></TD>"
    innerhtml += "</TR>"

    innerhtml += f"</TABLE>"
    innerhtml += f"<br/>"


    if project['osc_clock']:
        innerhtml += f"<H2>PLL:</H2>"
        innerhtml += "<TABLE>"
        innerhtml += "<TR>"
        innerhtml += f"<TD>sysclk_in {float(project['osc_clock']) // 1000000}MHz</TD>"
        innerhtml += "</TR>"
        innerhtml += "<TR>"
        innerhtml += f"<TD>sysclk {float(project['jdata']['clock']['speed']) // 1000000}MHz</TD>"
        innerhtml += "</TR>"
        innerhtml += f"</TABLE>"
        innerhtml += f"<br/>"

    innerhtml += f"<H2>Pins:</H2>"
    innerhtml += "<TABLE>"
    for pname in sorted(list(project['pinlists'])):
        pins = project['pinlists'][pname]
        for pin in pins:
            if pin[2] == "INPUT":
                pins_input.append(pin[0])
            else:
                pins_output.append(pin[0])
            innerhtml += "<TR>"
            innerhtml += f"<TD>{pin[0]}</TD>"
            innerhtml += f"<TD>{pin[1]}</TD>"
            innerhtml += f"<TD>{pin[2]}</TD>"
            innerhtml += "</TR>"
    innerhtml += f"</TABLE>"
    innerhtml += f"<br/>"


    innerhtml += f"<H2>RX-Data:</H2>"
    innerhtml += "<TABLE>"
    rxdata.append(f"rx_data")
    for num in range(project['joints']):
        innerhtml += "<TR>"
        innerhtml += f"<TD>jointFreqCmd{num}</TD>"
        innerhtml += f"<TD>32bit</TD>"
        innerhtml += "</TR>"
        rxdata.append(f"jointFreqCmd{num}")
    for num in range(project['vouts']):
        innerhtml += "<TR>"
        innerhtml += f"<TD>setPoint{num}</TD>"
        innerhtml += f"<TD>32bit</TD>"
        innerhtml += "</TR>"
        rxdata.append(f"setPoint{num}")
    for num in range(project['joints']):
        innerhtml += "<TR>"
        innerhtml += f"<TD>jointEnable{num}</TD>"
        innerhtml += f"<TD>1bit</TD>"
        innerhtml += "</TR>"
        rxdata.append(f"jointEnable{num}")
    for num in range(project['douts']):
        innerhtml += "<TR>"
        innerhtml += f"<TD>DOUT{num}</TD>"
        innerhtml += f"<TD>1bit</TD>"
        innerhtml += "</TR>"
        rxdata.append(f"DOUT{num}")
    innerhtml += f"</TABLE>"
    innerhtml += f"<br/>"

    innerhtml += f"<H2>TX-Data:</H2>"
    innerhtml += "<TABLE>"
    txdata.append(f"tx_data")
    for num in range(project['joints']):
        innerhtml += "<TR>"
        innerhtml += f"<TD>jointFeedback{num}</TD>"
        innerhtml += f"<TD>32bit</TD>"
        innerhtml += "</TR>"
        txdata.append(f"jointFeedback{num}")
    for num in range(project['vins']):
        innerhtml += "<TR>"
        innerhtml += f"<TD>processVariable{num}</TD>"
        innerhtml += f"<TD>32bit</TD>"
        innerhtml += "</TR>"
        txdata.append(f"processVariable{num}")
    for num in range(project['dins']):
        innerhtml += "<TR>"
        innerhtml += f"<TD>DIN{num}</TD>"
        innerhtml += f"<TD>1bit</TD>"
        innerhtml += "</TR>"
        txdata.append(f"DIN{num}")
    innerhtml += f"</TABLE>"
    innerhtml += f"<br/>"


    innerhtml += f"<H2>Plugins:</H2>"
    for plugin in project['plugins']:
        if hasattr(project['plugins'][plugin], "funcs"):
            module_name = ""
            module_id = ""
            mapping = {}
            module_wires = {}
            funcs = project['plugins'][plugin].funcs()
            code = "\n".join(funcs)
            for line in code.split("\n"):
                line = line.strip()
                if line.endswith("("):
                    module_name = line.split()[0]
                    module_id = line.split()[-2]
                    module_wires[module_id] = []
                elif line.startswith("assign "):
                    wire_to = line.split()[1]
                    wire_from = line.split()[3].strip("!;")
                    mapping[wire_from] = wire_to
                elif line.startswith("."):
                    wire = line.split("(")[1].split(")")[0].split()[0]
                    wire_org = wire
                    if wire in mapping:
                        wire = mapping[wire]
                    if module_id:
                        if wire in pins_input:
                            module_wires[module_id].append((wire, wire_org, "from PINS"))
                        elif wire in pins_output:
                            module_wires[module_id].append((wire, wire_org, "to PINS"))
                        elif wire in txdata:
                            module_wires[module_id].append((wire, wire_org, "to TX_DATA"))
                        elif wire in rxdata:
                            module_wires[module_id].append((wire, wire_org, "from RX_DATA"))
                        else:
                            module_wires[module_id].append((wire, wire_org, "---"))

            if module_wires:
                innerhtml += f"<H3>Modul: {plugin}:</H3>"
                for module, wires in module_wires.items():
                    innerhtml += "<TABLE>"
                    innerhtml += "<TR>"
                    innerhtml += f"<TD><B>{module}</B></TD>"
                    innerhtml += "</TR>"
                    for wire in wires:
                        innerhtml += "<TR>"
                        innerhtml += f"<TD>{wire[0]}</TD>"
                        innerhtml += f"<TD>{wire[2]}</TD>"
                        innerhtml += "</TR>"
                        if wire[1] != wire[0]:
                            innerhtml += "<TR>"
                            innerhtml += f"<TD>{wire[1]}</TD>"
                            innerhtml += f"<TD>{wire[2]}</TD>"
                            innerhtml += "</TR>"
                    innerhtml += f"</TABLE>"
                    innerhtml += "<br/>"

    innerhtml += "<br/>"
    innerhtml += "<br/>"
    innerhtml += "</html>"

    open(f"{project['DOC_PATH']}/README.html", "w").write(innerhtml)









    # markdown
    innerhtml = ""
    innerhtml += f"# {project['jdata']['name']}\n\n"

    innerhtml += f"Generated Output of [{project['config']}](/{project['config']})\n"
    innerhtml += "\n"
    innerhtml += "\n"
    innerhtml += "\n"


    innerhtml += f"## Build-Options:\n\n"
    innerhtml += f"| Name | Wert |\n"
    innerhtml += f"| --- | --- |\n"
    for key in ("name", "description", "toolchain", "family", "type", "package"):
        if key in project['jdata']:
            innerhtml += f"| {key.title()} | {project['jdata'][key]} |\n"
    innerhtml += "\n"

    innerhtml += f"## Files:\n"
    innerhtml += f"| Name | Wert |\n"
    innerhtml += f"| --- | --- |\n"
    if project['jdata']["toolchain"] == "icestorm" and project['jdata']["family"] == "ecp5":
        innerhtml += f"| Bitstream | [rio.bit](Firmware/rio.bit) |\n"
    elif project['jdata']["toolchain"] == "icestorm":
        innerhtml += f"| Bitstream | [rio.bin](Firmware/rio.bin) |\n"
    innerhtml += f"| LinuxCNC Components | [Components](LinuxCNC/Components/) |\n"
    innerhtml += f"| LinuxCNC ConfigSample | [ConfigSample](LinuxCNC/ConfigSamples/rio/) |\n"
    innerhtml += "\n"

    if project['osc_clock']:
        innerhtml += f"## PLL:\n"
        innerhtml += f"| Signal | Frequency |\n"
        innerhtml += f"| --- | --- |\n"
        innerhtml += f"|sysclk_in | {float(project['osc_clock']) // 1000000}MHz |\n"
        innerhtml += f"| sysclk | {float(project['jdata']['clock']['speed']) // 1000000}MHz |\n"
        innerhtml += "\n"


    innerhtml += f"## Pins:\n"
    innerhtml += f"| Name | Pin | Direction |\n"
    innerhtml += f"| --- | --- | --- |\n"
    for pname in sorted(list(project['pinlists'])):
        pins = project['pinlists'][pname]
        for pin in pins:
            if pin[2] == "INPUT":
                pins_input.append(pin[0])
            else:
                pins_output.append(pin[0])
            innerhtml += f"| {pin[0]} | {pin[1]}</TD> | {pin[2]} |\n"
    innerhtml += "\n"


    innerhtml += f"## RX-Data:\n"
    rxdata.append(f"rx_data")
    innerhtml += f"| Name | Size |\n"
    innerhtml += f"| --- | --- |\n"
    for num in range(project['joints']):
        innerhtml += f"| jointFreqCmd{num} | 32bit |\n"
        rxdata.append(f"jointFreqCmd{num}")
    for num in range(project['vouts']):
        innerhtml += f"| setPoint{num} | 32bit |\n"
        rxdata.append(f"setPoint{num}")
    for num in range(project['joints']):
        innerhtml += f"| jointEnable{num} | 1bit |\n"
        rxdata.append(f"jointEnable{num}")
    for num in range(project['douts']):
        innerhtml += f"| DOUT{num} | 1bit |\n"
        rxdata.append(f"DOUT{num}")
    innerhtml += "\n"

    innerhtml += f"## TX-Data:\n"
    txdata.append(f"tx_data")
    innerhtml += f"| Name | Wert |\n"
    innerhtml += f"| --- | --- |\n"
    for num in range(project['joints']):
        innerhtml += f"| jointFeedback{num} | 32bit |\n"
        txdata.append(f"jointFeedback{num}")
    for num in range(project['vins']):
        innerhtml += f"| processVariable{num} | 32bit |\n"
        txdata.append(f"processVariable{num}")
    for num in range(project['dins']):
        innerhtml += f"| DIN{num} | 1bit |\n"
        txdata.append(f"DIN{num}")
    innerhtml += "\n"


    innerhtml += f"## Plugins:\n"
    for plugin in project['plugins']:
        if hasattr(project['plugins'][plugin], "funcs"):
            module_name = ""
            module_id = ""
            mapping = {}
            module_wires = {}
            funcs = project['plugins'][plugin].funcs()
            code = "\n".join(funcs)
            for line in code.split("\n"):
                line = line.strip()
                if line.endswith("("):
                    module_name = line.split()[0]
                    module_id = line.split()[-2]
                    module_wires[module_id] = []
                elif line.startswith("assign "):
                    wire_to = line.split()[1]
                    wire_from = line.split()[3].strip("!;")
                    mapping[wire_from] = wire_to
                elif line.startswith("."):
                    wire = line.split("(")[1].split(")")[0].split()[0]
                    wire_org = wire
                    if wire in mapping:
                        wire = mapping[wire]
                    if module_id:
                        if wire in pins_input:
                            module_wires[module_id].append((wire, wire_org, "from PINS"))
                        elif wire in pins_output:
                            module_wires[module_id].append((wire, wire_org, "to PINS"))
                        elif wire in txdata:
                            module_wires[module_id].append((wire, wire_org, "to TX_DATA"))
                        elif wire in rxdata:
                            module_wires[module_id].append((wire, wire_org, "from RX_DATA"))
                        else:
                            module_wires[module_id].append((wire, wire_org, "---"))

            if module_wires:
                innerhtml += f"### Modul: {plugin}:\n"

                if hasattr(project['plugins'][plugin], "ips"):
                    for ipv in project["plugins"][plugin].ips():
                        innerhtml += f"files: [{ipv}](Firmware/{ipv})\n"

                for module, wires in module_wires.items():

                    innerhtml += f"#### {module}\n"

                    innerhtml += f"| Name | Direction |\n"
                    innerhtml += f"| --- | --- |\n"
                    for wire in wires:
                        innerhtml += f"| {wire[0]} | {wire[2]} |\n"
                        if wire[1] != wire[0]:
                            innerhtml += f"| {wire[1]} | {wire[2]} |\n"
                    innerhtml += "\n"

    innerhtml += "\n"

    innerhtml += "![Flowchart](doc/flowchart.png)\n"
    innerhtml += "\n\n\n"

    open(f"{project['OUTPUT_PATH']}/README.md", "w").write(innerhtml)
