
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
    expansion_input = []
    expansion_output = []


    innerhtml = "<<TABLE bgcolor=\"#a2c635\" BORDER=\"0\" CELLBORDER=\"1\" CELLSPACING=\"0\">"
    innerhtml += "<TR>"
    innerhtml += f"<TD><B>{project['jdata']['family']} - {project['jdata']['type']}</B></TD>"
    innerhtml += "</TR>"
    for pname in sorted(list(project['pinlists'])):
        pins = project['pinlists'][pname]
        for pin in pins:
            if pin[1].startswith("EXPANSION"):
                if pin[2] == "INPUT":
                    expansion_input.append(pin[0])
                else:
                    expansion_output.append(pin[0])
            else:
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
        wire = f"DOUT{num}"
        rxdata.append(wire)
        if wire in expansion_output:
            s.edge(f'rx_data:{wire}', f'expansion_shiftreg0:EXPANSION0_OUTPUT', color="red")
        else:
            s.edge(f'rx_data:{wire}', f'pins:{wire}', color="blue")
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
        wire = f"DIN{num}"
        txdata.append(wire)
        if wire in expansion_input:
            s.edge(f'expansion_shiftreg0:EXPANSION0_INPUT', f'tx_data:{wire}', color="red")
        else:
            s.edge(f'pins:{wire}', f'tx_data:{wire}', color="green")
    innerhtml += f"</TABLE>>"
    s.node('tx_data', innerhtml)


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
                        if wire in expansion_input:
                            module_wires[module_id].append((wire, wire_org))
                            s.edge(f'expansion_shiftreg0:EXPANSION0_INPUT', f'{module_id}:{wire}', color="red")
                        elif wire in expansion_output:
                            module_wires[module_id].append((wire, wire_org))
                            s.edge(f'{module_id}:{wire}', f'expansion_shiftreg0:EXPANSION0_OUTPUT', color="red")
                        elif wire in pins_input:
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
            if pin[1].startswith("EXPANSION"):
                if pin[2] == "INPUT":
                    expansion_input.append(pin[0])
                else:
                    expansion_output.append(pin[0])
            else:
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
                        if wire in expansion_input:
                            module_wires[module_id].append((wire, wire_org, "EXPANSION0_INPUT"))
                        elif wire in expansion_output:
                            module_wires[module_id].append((wire, wire_org, "EXPANSION0_OUTPUT"))
                        elif wire in pins_input:
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
                    innerhtml += f"files: "
                    for ipv in project["plugins"][plugin].ips():
                        innerhtml += f"[{ipv}](Firmware/{ipv}) "
                    innerhtml += "\n"

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
