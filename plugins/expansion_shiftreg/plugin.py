class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "expansion",
                "subtype": "shiftreg",
                "comment": "to expand the number of IO's via fast shiftregisters like 74hc595(8 outputs) / 74hc165(8 inputs)",
                "options": {
                    "bits": {
                        "type": "int",
                        "default": 8,
                        "name": "number of bits",
                        "comment": "total number of bits to send/receive N = max(8bit * num input-devices, 8bit * num output-devices)",
                    },
                    "speed": {
                        "type": "int",
                        "default": 100000,
                        "name": "clock speed",
                        "comment": "the clock-speed in Hz",
                    },
                    "pins": {
                        "type": "dict",
                        "name": "pin config",
                        "options": {
                            "clock": {
                                "type": "output",
                                "name": "clock pin",
                                "comment": "used for input and output expansions",
                            },
                            "load": {
                                "type": "output",
                                "name": "load pin",
                                "comment": "used for input and output expansions",
                            },
                            "in": {
                                "type": "input",
                                "name": "input data",
                                "comment": "used only for the input expansions",
                            },
                            "out": {
                                "type": "output",
                                "name": "output data",
                                "comment": "used only for the output expansions",
                            },
                        },
                    },
                },
            }
        ]

    def pinlist(self):
        pinlist_out = []
        for num, expansion in enumerate(self.jdata.get("expansion", [])):
            if expansion["type"] in ["shiftreg"]:
                pullup = expansion.get("pullup", True)
                pinlist_out.append(
                    (
                        f"EXPANSION{num}_SHIFTREG_CLOCK",
                        expansion["pins"]["clock"],
                        "OUTPUT",
                    )
                )
                pinlist_out.append(
                    (
                        f"EXPANSION{num}_SHIFTREG_LOAD",
                        expansion["pins"]["load"],
                        "OUTPUT",
                    )
                )
                if "out" in expansion["pins"]:
                    pinlist_out.append(
                        (
                            f"EXPANSION{num}_SHIFTREG_OUT",
                            expansion["pins"]["out"],
                            "OUTPUT",
                        )
                    )
                if "in" in expansion["pins"]:
                    pinlist_out.append(
                        (
                            f"EXPANSION{num}_SHIFTREG_IN",
                            expansion["pins"]["in"],
                            "INPUT",
                            pullup,
                        )
                    )
        return pinlist_out

    def expansions(self):
        expansions = {}
        for num, expansion in enumerate(self.jdata.get("expansion", [])):
            if expansion["type"] == "shiftreg":
                bits = int(expansion.get("bits", 8))
                expansions[f"EXPANSION{num}_OUTPUT"] = bits
                expansions[f"EXPANSION{num}_INPUT"] = bits
        return expansions

    def defs(self):
        func_out = []
        for num, expansion in enumerate(self.jdata.get("expansion", [])):
            if expansion["type"] == "shiftreg":
                bits = int(expansion.get("bits", 8))
                invert = expansion.get("invert", False)
                func_out.append(f"    wire [{bits - 1}:0] EXPANSION{num}_INPUT;")
                func_out.append(f"    wire [{bits - 1}:0] EXPANSION{num}_OUTPUT;")
                if "out" not in expansion["pins"]:
                    if invert:
                        func_out.append(
                            f"    wire EXPANSION{num}_SHIFTREG_OUT_INV; // fake output pin"
                        )
                    else:
                        func_out.append(
                            f"    wire EXPANSION{num}_SHIFTREG_OUT; // fake output pin"
                        )
                elif invert:
                    func_out.append(f"    wire EXPANSION{num}_SHIFTREG_OUT_INV;")
                    func_out.append(
                        f"    assign EXPANSION{num}_SHIFTREG_OUT = ~EXPANSION{num}_SHIFTREG_OUT_INV;"
                    )

                if "in" not in expansion["pins"]:
                    if invert:
                        func_out.append(
                            f"    reg EXPANSION{num}_SHIFTREG_IN_INV = 0; // fake input pin"
                        )
                    else:
                        func_out.append(
                            f"    reg EXPANSION{num}_SHIFTREG_IN = 0; // fake input pin"
                        )
                elif invert:
                    func_out.append(f"    wire EXPANSION{num}_SHIFTREG_IN_INV;")
                    func_out.append(
                        f"    assign EXPANSION{num}_SHIFTREG_IN_INV = ~EXPANSION{num}_SHIFTREG_IN;"
                    )

                if invert:
                    func_out.append(f"    wire EXPANSION{num}_SHIFTREG_CLOCK_INV;")
                    func_out.append(
                        f"    assign EXPANSION{num}_SHIFTREG_CLOCK = ~EXPANSION{num}_SHIFTREG_CLOCK_INV;"
                    )
                    func_out.append(f"    wire EXPANSION{num}_SHIFTREG_LOAD_INV;")
                    func_out.append(
                        f"    assign EXPANSION{num}_SHIFTREG_LOAD = ~EXPANSION{num}_SHIFTREG_LOAD_INV;"
                    )

        return func_out

    def funcs(self):
        func_out = []
        for num, expansion in enumerate(self.jdata.get("expansion", [])):
            if expansion["type"] == "shiftreg":
                bits = int(expansion.get("bits", 8))
                invert = expansion.get("invert", False)
                speed = int(expansion.get("speed", 100000))
                divider = int(self.jdata["clock"]["speed"]) // speed // 2

                func_out.append(f"    wire [{bits-1}:0] EXPANSION{num}_INPUT_RAW;")
                mapping_inputs = expansion.get("mapping", {}).get("inputs")
                if mapping_inputs:
                    mappings = []
                    for index, offset in enumerate(mapping_inputs):
                        mappings.append(f"EXPANSION{num}_INPUT_RAW[{index + offset}]")
                    func_out.append(
                        f"    assign EXPANSION{num}_INPUT = {{{', '.join(reversed(mappings))}}};"
                    )
                else:
                    func_out.append(
                        f"    assign EXPANSION{num}_INPUT = EXPANSION{num}_INPUT_RAW;"
                    )

                func_out.append(f"    wire [{bits-1}:0] EXPANSION{num}_OUTPUT_RAW;")
                func_out.append(
                    f"    assign EXPANSION{num}_OUTPUT_RAW = EXPANSION{num}_OUTPUT;"
                )

                func_out.append(
                    f"    expansion_shiftreg #({bits}, {divider}) expansion_shiftreg{num} ("
                )
                func_out.append("       .clk (sysclk),")
                if invert:
                    func_out.append(
                        f"       .SHIFT_OUT (EXPANSION{num}_SHIFTREG_OUT_INV),"
                    )
                    func_out.append(
                        f"       .SHIFT_IN (EXPANSION{num}_SHIFTREG_IN_INV),"
                    )
                    func_out.append(
                        f"       .SHIFT_CLK (EXPANSION{num}_SHIFTREG_CLOCK_INV),"
                    )
                    func_out.append(
                        f"       .SHIFT_LOAD (EXPANSION{num}_SHIFTREG_LOAD_INV),"
                    )
                else:
                    func_out.append(f"       .SHIFT_OUT (EXPANSION{num}_SHIFTREG_OUT),")
                    func_out.append(f"       .SHIFT_IN (EXPANSION{num}_SHIFTREG_IN),")
                    func_out.append(
                        f"       .SHIFT_CLK (EXPANSION{num}_SHIFTREG_CLOCK),"
                    )
                    func_out.append(
                        f"       .SHIFT_LOAD (EXPANSION{num}_SHIFTREG_LOAD),"
                    )

                func_out.append(f"       .data_in (EXPANSION{num}_INPUT_RAW),")
                func_out.append(f"       .data_out (EXPANSION{num}_OUTPUT_RAW)")
                func_out.append("    );")
        return func_out

    def ips(self):
        for num, expansion in enumerate(self.jdata.get("expansion", [])):
            if expansion["type"] in ["shiftreg"]:
                return ["expansion_shiftreg.v"]
        return []
