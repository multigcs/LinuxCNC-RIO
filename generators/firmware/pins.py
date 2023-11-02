def pins_lpf(project):
    data = []

    lpf_data = []
    for pname, pins in project['pinlists'].items():
        if not pins:
            continue
        lpf_data.append(f"### {pname} ###")
        for pin in pins:
            if pin[1].startswith("EXPANSION"):
                continue
            if pin[1] == "USRMCLK":
                lpf_data.append(f'# this pin ({pin[0]}) is not available in the lpf file, have to use the USRMCLK primitive in the verilog')
                continue

            extra = ""
            if len(pin) > 4:
                extra += f" {pin[4]}"

            lpf_data.append(f'LOCATE COMP "{pin[0]}"           SITE "{pin[1]}";')
            lpf_data.append(f'IOBUF PORT "{pin[0]}" IO_TYPE=LVCMOS33{extra};')

        lpf_data.append("")
    lpf_data.append("")
    open(f"{project['PINS_PATH']}/pins.lpf", "w").write("\n".join(lpf_data))


def pins_cst(project):
    data = []
    for pname, pins in project["pinlists"].items():
        if not pins:
            continue
        data.append(f"// ### {pname} ###")
        for pin in pins:
            if pin[1].startswith("EXPANSION"):
                continue

            data.append(f'IO_LOC "{pin[0]}" {pin[1]};')
            # data.append(f'IO_PORT "{pin[0]}" IO_TYPE=LVCMOS33;')
            if len(pin) > 3 and pin[3]:
                data.append(f'IO_PORT "{pin[0]}" IO_TYPE=LVCMOS33 PULL_MODE=UP;')
            else:
                data.append(f'IO_PORT "{pin[0]}" IO_TYPE=LVCMOS33;')

        data.append("")
    data.append("")
    open(f"{project['PINS_PATH']}/pins.cst", "w").write("\n".join(data))


def pins_pcf(project):
    data = []
    for pname, pins in project["pinlists"].items():
        if not pins:
            continue
        data.append(f"### {pname} ###")
        for pin in pins:
            if pin[1].startswith("EXPANSION"):
                continue
            options = ""
            if len(pin) > 3 and pin[3]:
                options += " -pullup yes"

            data.append(f"set_io {options} {pin[0]} {pin[1]}")
        data.append("")
    open(f"{project['PINS_PATH']}/pins.pcf", "w").write("\n".join(data))


def pins_xdc(project):
    # vivado style
    data = []
    for pname, pins in project["pinlists"].items():
        if not pins:
            continue
        data.append(f"### {pname} ###")
        for pin in pins:
            if pin[1].startswith("EXPANSION"):
                continue
            data.append(f"set_property LOC {pin[1]} [get_ports {pin[0]}]")
            data.append(f"set_property IOSTANDARD LVCMOS33 [get_ports {pin[0]}]")
            if len(pin) > 3 and pin[3]:
                data.append(f"set_property PULLUP TRUE [get_ports {pin[0]}]")
        data.append("")
    open(f"{project['PINS_PATH']}/pins.xdc", "w").write("\n".join(data))

def pins_qdf(project):
    data = []
    data.append(f"set_global_assignment -name STRATIX_DEVICE_IO_STANDARD \"3.3-V LVTTL\"")
    for pname, pins in project["pinlists"].items():
        if not pins:
            continue
        data.append(f"### {pname} ###")
        for pin in pins:
            if pin[1].startswith("EXPANSION"):
                continue
            data.append(f"set_location_assignment {pin[1]} -to {pin[0]}")
            if len(pin) > 3 and pin[3]:
                data.append(f"set_instance_assignment -name WEAK_PULL_UP_RESISTOR ON -to {pin[0]}")

        data.append("")
    open(f"{project['PINS_PATH']}/pins.qdf", "w").write("\n".join(data))
