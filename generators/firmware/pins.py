def pins_lpf(project):
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
            options = ""
            # if len(pin) > 3 and pin[3]:
            #    options += " -pullup yes"
            data.append(f"set_property LOC {pin[1]} [get_ports {pin[0]}]")
            data.append(f"set_property IOSTANDARD LVCMOS33 [get_ports {pin[0]}]")
        data.append("")
    open(f"{project['PINS_PATH']}/pins.xdc", "w").write("\n".join(data))
