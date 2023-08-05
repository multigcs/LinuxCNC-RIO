class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vin",
                "subtype": "frequency",
                "comment": "measures the frequency of signals on the input-pin in Hz",
                "options": {
                    "pin": {
                        "type": "input",
                        "name": "input pin",
                    },
                    "pullup": {
                        "type": "bool",
                        "name": "internal pullup",
                    },
                    "freq_min": {
                        "type": "int",
                        "name": "internal pullup",
                        "default": 10,
                        "comment": "this is the minumum frequency in Hz on the input-pin, all below is set to 0 Hz",
                    },
                },
            }
        ]

    def types(self):
        return ["frequency", ]

    def entry_info(self, joint):
        info = ""
        if joint.get("type") == "frequency":
            pin = joint["pin"]
            pullup = joint.get("pullup", False)
            info += f"Variable frequency (pin:{pin}, pullup:{pullup})"
        return info


    def pinlist(self):
        pinlist_out = []
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "frequency":
                pullup = vin.get("pullup", False)
                pinlist_out.append((f"VIN{num}_FREQUENCY", vin["pin"], "INPUT", pullup))
        return pinlist_out

    def vinnames(self):
        ret = []
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "frequency":
                name = vin.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                ret.append((nameIntern, name, vin))
        return ret

    def funcs(self):
        func_out = ["    // vin_frequency's"]
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "frequency":
                name = vin.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                freq_min = int(vin.get("freq_min", 10))
                func_out.append(
                    f"    vin_frequency #({int(self.jdata['clock']['speed']) // freq_min}) vin_frequency{num} ("
                )
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .frequency ({nameIntern}),")
                func_out.append(f"        .SIGNAL (VIN{num}_FREQUENCY)")
                func_out.append("    );")

        return func_out

    def ips(self):
        for num, vin in enumerate(self.jdata["vin"]):
            if vin["type"] in ["frequency"]:
                return ["vin_frequency.v"]
        return []
