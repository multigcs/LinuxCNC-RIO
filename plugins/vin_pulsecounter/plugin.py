class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vin",
                "subtype": "counter",
                "comment": "counting signals on the input pins (up/down), can be reset by the reset-pin",
                "options": {
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
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") in ("counter",):
                pullup = vin.get("pullup", False)
                if "up" in vin["pins"]:
                    pinlist_out.append(
                        (f"VIN{num}_PULSECOUNTER_UP", vin["pins"]["up"], "INPUT", pullup)
                    )
                if "down" in vin["pins"]:
                    pinlist_out.append(
                        (
                            f"VIN{num}_PULSECOUNTER_DOWN",
                            vin["pins"]["down"],
                            "INPUT",
                            pullup,
                        )
                    )
                if "reset" in vin["pins"]:
                    pinlist_out.append(
                        (
                            f"VIN{num}_PULSECOUNTER_RESET",
                            vin["pins"]["reset"],
                            "INPUT",
                            pullup,
                        )
                    )
        return pinlist_out

    def vins(self):
        vins_out = 0
        for _num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") in ("counter",):
                vins_out += 1
        return vins_out

    def vdata(self):
        vdata = []
        for _num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "counter":
                vdata.append(vin)
        return vdata

    def funcs(self):
        func_out = ["    // vin_pulsecounter's"]
        vin_num = 0
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") in ("counter",):
                func_out.append(f"    vin_pulsecounter vin_pulsecounter{num} (")
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .counter (processVariable{vin_num}),")
                if "up" in vin["pins"]:
                    func_out.append(f"        .UP (VIN{num}_PULSECOUNTER_UP),")
                else:
                    func_out.append("        .UP (1'd0),")
                if "down" in vin["pins"]:
                    func_out.append(f"        .DOWN (VIN{num}_PULSECOUNTER_DOWN),")
                else:
                    func_out.append("        .DOWN (1'd0),")
                if "reset" in vin["pins"]:
                    func_out.append(f"        .RESET (VIN{num}_PULSECOUNTER_RESET)")
                else:
                    func_out.append("        .RESET (1'd0)")
                func_out.append("    );")
            vin_num += vin.get("vars", 1)
        return func_out

    def ips(self):
        for num, vin in enumerate(self.jdata["vin"]):
            if vin["type"] in ["counter"]:
                return ["vin_pulsecounter.v"]
        return []
