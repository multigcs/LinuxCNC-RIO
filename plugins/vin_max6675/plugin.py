class Plugin:
    ptype = "vin_max6675"

    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vin",
                "subtype": self.ptype,
                "comment": "LM65 temperature sensor",
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
                    "pins": {
                        "type": "dict",
                        "name": "pin config",
                        "options": {
                            "MISO": {
                                "type": "input",
                                "name": "MISO input",
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

    def calculation_vin(self, setup, value):
        unit = "°C"
        value = value * 0.25
        return (value, unit)

    def pinlist(self):
        pinlist_out = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                pullup = data.get("pullup", True)
                pinlist_out.append(
                    (f"VIN{num}_MISO", data["pins"]["MISO"], "INPUT", pullup)
                )
                pinlist_out.append(
                    (f"VIN{num}_SCLK", data["pins"]["SCLK"], "OUTPUT", pullup)
                )
                pinlist_out.append(
                    (f"VIN{num}_CS", data["pins"]["CS"], "OUTPUT", pullup)
                )
        return pinlist_out

    def vinnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                function = data.get("function")

                data["_bits"] = 16
                data["_name"] = name + ".0"
                data["_prefix"] = nameIntern + "_0"
                if isinstance(function, list):
                    data["function"] = function[0]
                ret.append(data.copy())
        return ret

    def funcs(self):
        func_out = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                spi_clk_speed = 100000 # 100kHz
                divider = int(self.jdata["clock"]["speed"]) // spi_clk_speed // 4
                
                func_out.append(f"    vin_max6675 #({divider}) vin_max6675{num} (")
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .spi_miso (VIN{num}_MISO),")
                func_out.append(f"        .spi_sclk (VIN{num}_SCLK),")
                func_out.append(f"        .spi_cs (VIN{num}_CS),")
                func_out.append(f"        .temperature ({nameIntern}_0)")
                func_out.append("    );")
        return func_out

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                return ["vin_max6675.v"]
        return []
