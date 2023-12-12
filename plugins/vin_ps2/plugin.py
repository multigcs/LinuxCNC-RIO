class Plugin:
    ptype = "vin_ps2"

    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vin",
                "subtype": self.ptype,
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
                        "comment": "the target net of the signal in the hal",
                        "default": "",
                    },
                    "pins": {
                        "type": "dict",
                        "options": {
                            "clk": {
                                "type": "input",
                                "name": "PS2 clock input pin",
                            },
                            "data": {
                                "type": "input",
                                "name": "PS2 data input pin",
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
                pins = data["pins"]
                pinlist_out.append((f"VIN{num}_CLK", pins["clk"], "INPUT"))
                pinlist_out.append((f"VIN{num}_DATA", pins["data"], "INPUT"))
        return pinlist_out

    def vinnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data)
        return ret

    def funcs(self):
        func_out = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                name = data.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()

                speed = int(self.jdata["clock"]["speed"]) // 1000000 // 2

                func_out.append(f"    vin_ps2 #({speed}) vin_ps2{num} (")
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .code ({nameIntern}),")
                func_out.append(f"        .ps2_clk (VIN{num}_CLK),")
                func_out.append(f"        .ps2_data (VIN{num}_DATA)")
                func_out.append("    );")
        return func_out

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                return ["vin_ps2.v"]
        return []
