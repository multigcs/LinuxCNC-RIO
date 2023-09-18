class Plugin:
    ptype = "vin_sonar"

    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vin",
                "subtype": self.ptype,
                "comment": "to messure distance via ultrasonic modules with trigger/echo pins",
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
                            "trigger": {
                                "type": "input",
                                "name": "echo pin",
                            },
                            "echo": {
                                "type": "output",
                                "name": "trigger pin",
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
                pinlist_out.append(
                    (
                        f"VIN{num}_SONAR_TRIGGER",
                        data["pins"]["trigger"],
                        "OUTPUT",
                        False,
                    )
                )
                pinlist_out.append(
                    (f"VIN{num}_SONAR_ECHO", data["pins"]["echo"], "INPUT", pullup)
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
                osc = int(self.jdata["clock"]["speed"])
                func_out.append(
                    f"    vin_sonar #({osc // 50000}, {osc // 13}, {osc // 5}) vin_sonar{num} ("
                )
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .trigger (VIN{num}_SONAR_TRIGGER),")
                func_out.append(f"        .echo (VIN{num}_SONAR_ECHO),")
                func_out.append(f"        .distance ({nameIntern})")
                func_out.append("    );")
        return func_out

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                return ["vin_sonar.v"]
        return []
