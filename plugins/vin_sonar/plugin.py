class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vin",
                "subtype": "sonar",
                "comment": "to messure distance via ultrasonic modules with trigger/echo pins",
                "options": {
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
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "sonar":
                pullup = vin.get("pullup", False)
                pinlist_out.append((f"VIN{num}_SONAR_TRIGGER", vin["pins"]["trigger"], "OUTPUT", False))
                pinlist_out.append((f"VIN{num}_SONAR_ECHO", vin["pins"]["echo"], "INPUT", pullup))
        return pinlist_out

    def vinnames(self):
        ret = []
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "sonar":
                name = vin.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                ret.append((nameIntern, name, vin))
        return ret

    def funcs(self):
        func_out = ["    // vin_sonar's"]
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "sonar":
                name = vin.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                osc = int(self.jdata['clock']['speed'])
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
        for num, vin in enumerate(self.jdata["vin"]):
            if vin["type"] in ["sonar"]:
                return ["vin_sonar.v"]
        return []
