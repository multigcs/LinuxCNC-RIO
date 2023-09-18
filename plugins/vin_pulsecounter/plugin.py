class Plugin:
    ptype = "vin_counter"

    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vin",
                "subtype": self.ptype,
                "comment": "counting signals on the input pins (up/down), can be reset by the reset-pin",
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
                        "options": {
                            "up": {
                                "type": "input",
                                "name": "up pin",
                                "comment": "to count up",
                            },
                            "down": {
                                "type": "input",
                                "name": "down pin",
                                "comment": "to count down",
                            },
                            "reset": {
                                "type": "input",
                                "name": "reset pin",
                                "comment": "reset the counter to zero",
                            },
                        },
                    },
                },
            }
        ]

    def pinlist(self):
        pinlist_out = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                pullup = data.get("pullup", False)
                if "up" in data["pins"]:
                    pinlist_out.append(
                        (
                            f"VIN{num}_PULSECOUNTER_UP",
                            data["pins"]["up"],
                            "INPUT",
                            pullup,
                        )
                    )
                if "down" in data["pins"]:
                    pinlist_out.append(
                        (
                            f"VIN{num}_PULSECOUNTER_DOWN",
                            data["pins"]["down"],
                            "INPUT",
                            pullup,
                        )
                    )
                if "reset" in data["pins"]:
                    pinlist_out.append(
                        (
                            f"VIN{num}_PULSECOUNTER_RESET",
                            data["pins"]["reset"],
                            "INPUT",
                            pullup,
                        )
                    )
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
            if data.get("type") == self.ptype:
                name = data.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                func_out.append(f"    vin_pulsecounter vin_pulsecounter{num} (")
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .counter ({nameIntern}),")
                if "up" in data["pins"]:
                    func_out.append(f"        .UP (VIN{num}_PULSECOUNTER_UP),")
                else:
                    func_out.append("        .UP (1'd0),")
                if "down" in data["pins"]:
                    func_out.append(f"        .DOWN (VIN{num}_PULSECOUNTER_DOWN),")
                else:
                    func_out.append("        .DOWN (1'd0),")
                if "reset" in data["pins"]:
                    func_out.append(f"        .RESET (VIN{num}_PULSECOUNTER_RESET)")
                else:
                    func_out.append("        .RESET (1'd0)")
                func_out.append("    );")
        return func_out

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                return ["vin_pulsecounter.v"]
        return []
