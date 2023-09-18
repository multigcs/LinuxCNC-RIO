class Plugin:
    ptype = "vout_spipoti"

    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vout",
                "subtype": self.ptype,
                "comment": "variable output via spi-poti like (MCP4151)",
                "options": {
                    "name": {
                        "type": "str",
                        "name": "pin name",
                        "comment": "the name of the pin",
                        "default": "",
                    },
                    "net": {
                        "type": "vtarget",
                        "name": "net target",
                        "comment": "the target net of the pin in the hal",
                        "default": "",
                    },
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
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                pinlist_out.append(
                    (f"VOUT{num}_SPIPOTI_MOSI", data["pins"]["MOSI"], "OUTPUT")
                )
                pinlist_out.append(
                    (f"VOUT{num}_SPIPOTI_SCLK", data["pins"]["SCLK"], "OUTPUT")
                )
                pinlist_out.append(
                    (f"VOUT{num}_SPIPOTI_CS", data["pins"]["CS"], "OUTPUT")
                )
        return pinlist_out

    def voutnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"SP.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data)
        return ret

    def funcs(self):
        func_out = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                name = data.get("name", f"SP.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                bits = int(data.get("bits", 8))
                speed = int(data.get("speed", 100000))
                divider = int(self.jdata["clock"]["speed"]) // speed
                func_out.append(
                    f"    vout_spipoti #({bits}, {divider}) vout_spipoti{num} ("
                )
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .value ({nameIntern}),")
                func_out.append(f"        .MOSI (VOUT{num}_SPIPOTI_MOSI),")
                func_out.append(f"        .SCLK (VOUT{num}_SPIPOTI_SCLK),")
                func_out.append(f"        .CS (VOUT{num}_SPIPOTI_CS)")
                func_out.append("    );")

        return func_out

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                return ["vout_spipoti.v"]
        return []
