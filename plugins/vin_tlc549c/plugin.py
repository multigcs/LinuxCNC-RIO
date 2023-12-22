class Plugin:
    ptype = "vin_tlc549c"

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
                            "miso": {
                                "type": "input",
                                "name": "SPI-Data input pin",
                            },
                            "sclk": {
                                "type": "input",
                                "name": "SPI-Clock pin",
                            },
                            "cs": {
                                "type": "input",
                                "name": "SPI-CS pin",
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
                pinlist_out.append((f"VIN{num}_MISO", pins["miso"], "INPUT"))
                pinlist_out.append((f"VIN{num}_SCLK", pins["sclk"], "OUTPUT"))
                pinlist_out.append((f"VIN{num}_CS", pins["cs"], "OUTPUT"))
        return pinlist_out

    def vinnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_bits"] = 8
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

                func_out.append(f"    vin_tlc549c #({speed}) vin_tlc549c{num} (")
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .adc_data ({nameIntern}),")
                func_out.append(f"        .adc_data_in (VIN{num}_MISO),")
                func_out.append(f"        .adc_clk (VIN{num}_SCLK),")
                func_out.append(f"        .adc_cs_n (VIN{num}_CS)")
                func_out.append("    );")
        return func_out

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                return ["vin_tlc549c.v"]
        return []
