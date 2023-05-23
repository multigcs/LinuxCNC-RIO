class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "expansion",
                "subtype": "shiftreg",
                "options": {
                    "bits": {
                        "type": "int",
                        "name": "number of bits",
                    },
                    "speed": {
                        "type": "int",
                        "name": "clock speed",
                    },
                    "pins": {
                        "type": "dict",
                        "name": "pin config",
                        "options": {
                            "clock": {
                                "type": "output",
                                "name": "clock pin",
                            },
                            "load": {
                                "type": "output",
                                "name": "load pin",
                            },
                            "in": {
                                "type": "input",
                                "name": "input data",
                            },
                            "out": {
                                "type": "output",
                                "name": "output data",
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
                pinlist_out.append((f"EXPANSION{num}_SHIFTREG_CLOCK", expansion["pins"]["clock"], "OUTPUT"))
                pinlist_out.append((f"EXPANSION{num}_SHIFTREG_LOAD", expansion["pins"]["load"], "OUTPUT"))
                if "out" in expansion["pins"]:
                    pinlist_out.append((f"EXPANSION{num}_SHIFTREG_OUT", expansion["pins"]["out"], "OUTPUT"))
                if "in" in expansion["pins"]:
                    pinlist_out.append((f"EXPANSION{num}_SHIFTREG_IN", expansion["pins"]["in"], "INPUT"))
        return pinlist_out

    def expansions(self):
        expansions = {}
        for num, expansion in enumerate(self.jdata.get("expansion", [])):
            if expansion["type"] == "shiftreg":
                bits = int(expansion.get("bits", 8))
                expansions[f"EXPANSION{num}_OUTPUT"] = bits
                expansions[f"EXPANSION{num}_INPUT"] = bits
        return expansions

    def funcs(self):
        func_out = ["    // expansion_shiftreg's"]
        for num, expansion in enumerate(self.jdata.get("expansion", [])):
            if expansion["type"] == "shiftreg":
                bits = int(expansion.get("bits", 8))
                speed = int(expansion.get("speed", 100000))
                divider = int(self.jdata["clock"]["speed"]) // speed // 2
                func_out.append(f"    wire [{bits - 1}:0] EXPANSION{num}_INPUT;")
                func_out.append(f"    wire [{bits - 1}:0] EXPANSION{num}_OUTPUT;")
                if "out" not in expansion["pins"]:
                    func_out.append(f"    wire EXPANSION{num}_SHIFTREG_OUT; // fake output pin")
                if "in" not in expansion["pins"]:
                    func_out.append(f"    reg EXPANSION{num}_SHIFTREG_IN = 0; // fake input pin")
                func_out.append(f"    expansion_shiftreg #({bits}, ({divider})) expansion_shiftreg{num} (")
                func_out.append("       .clk (sysclk),")
                func_out.append(f"       .SHIFT_OUT (EXPANSION{num}_SHIFTREG_OUT),")
                func_out.append(f"       .SHIFT_IN (EXPANSION{num}_SHIFTREG_IN),")
                func_out.append(f"       .SHIFT_CLK (EXPANSION{num}_SHIFTREG_CLOCK),")
                func_out.append(f"       .SHIFT_LOAD (EXPANSION{num}_SHIFTREG_LOAD),")
                func_out.append(f"       .data_in (EXPANSION{num}_INPUT),")
                func_out.append(f"       .data_out (EXPANSION{num}_OUTPUT)")
                func_out.append("    );")
        return func_out

    def ips(self):
        files = ["expansion_shiftreg.v"]
        return files
