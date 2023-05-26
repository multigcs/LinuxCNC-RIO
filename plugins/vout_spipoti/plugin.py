class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vout",
                "subtype": "spipoti",
                "comment": "variable output via spi-poti like (MCP4151)",
                "options": {
                    "bits": {
                        "type": "int",
                        "name": "resolution in bits",
                        "default": "8",
                        "comment": "resolution of the poti in bits",
                    },
                    "speed": {
                        "type": "int",
                        "name": "speed",
                        "default": "1000000",
                        "comment": "spi clock speed",
                    },
                    "pins": {
                        "type": "dict",
                        "name": "pin config",
                        "options": {
                            "MOSI": {
                                "type": "output",
                                "name": "MOSI output",
                            },
                            "SCLK": {
                                "type": "output",
                                "name": "SCLK output",
                            },
                            "CS": {
                                "type": "output",
                                "name": "CS output",
                            },
                        },
                    },
                },
            }
        ]

    def pinlist(self):
        pinlist_out = []
        for num, vout in enumerate(self.jdata["vout"]):
            if vout["type"] in ["spipoti"]:
                pinlist_out.append((f"VOUT{num}_SPIPOTI_MOSI", vout["pins"]["MOSI"], "OUTPUT"))
                pinlist_out.append((f"VOUT{num}_SPIPOTI_SCLK", vout["pins"]["SCLK"], "OUTPUT"))
                pinlist_out.append((f"VOUT{num}_SPIPOTI_CS", vout["pins"]["CS"], "OUTPUT"))
        return pinlist_out

    def vouts(self):
        vouts_out = 0
        for _num, vout in enumerate(self.jdata["vout"]):
            if vout["type"] in ["spipoti"]:
                vouts_out += 1
        return vouts_out

    def funcs(self):
        func_out = ["    // vout_spipoti's"]
        for num, vout in enumerate(self.jdata["vout"]):
            if vout["type"] in ["spipoti"]:
                bits = int(vout.get("bits", 8))
                speed = int(vout.get("speed", 100000))
                divider = int(self.jdata["clock"]["speed"]) // speed
                func_out.append(f"    vout_spipoti #({bits}, {divider}) vout_spipoti{num} (")
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .value (setPoint{num}),")
                func_out.append(f"        .MOSI (VOUT{num}_SPIPOTI_MOSI),")
                func_out.append(f"        .SCLK (VOUT{num}_SPIPOTI_SCLK),")
                func_out.append(f"        .CS (VOUT{num}_SPIPOTI_CS)")
                func_out.append("    );")

        return func_out

    def ips(self):
        for num, vout in enumerate(self.jdata["vout"]):
            if vout["type"] in ["spipoti"]:
                return ["vout_spipoti.v"]
        return []


