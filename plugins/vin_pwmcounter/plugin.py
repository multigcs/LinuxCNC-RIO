class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vin",
                "subtype": "pwm",
                "comment": "measures the puls-lenght of pwm-signals on the input-pin",
                "options": {
                    "pin": {
                        "type": "input",
                        "name": "input pin",
                    },
                    "freq_min": {
                        "type": "int",
                        "name": "minimum frequency",
                        "default": 10,
                        "comment": "this is the minumum frequency in Hz on the input-pin, all below is set to zero",
                    },
                },
            }
        ]

    def pinlist(self):
        pinlist_out = []
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "pwm":
                pullup = vin.get("pullup", False)
                pinlist_out.append((f"VIN{num}_PWM", vin["pin"], "INPUT", pullup))
        return pinlist_out

    def vinnames(self):
        ret = []
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "pwm":
                name = vin.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                ret.append((nameIntern, name, vin))
        return ret

    def funcs(self):
        func_out = ["    // vin_pwmcounter's"]
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "pwm":
                name = vin.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                freq_min = int(vin.get("freq_min", 10))
                func_out.append(
                    f"    vin_pwmcounter #({int(self.jdata['clock']['speed']) // freq_min}) vin_pwmcounter{num} ("
                )
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .frequency ({nameIntern}),")
                func_out.append(f"        .SIGNAL (VIN{num}_PWM)")
                func_out.append("    );")
        return func_out

    def ips(self):
        for num, vin in enumerate(self.jdata["vin"]):
            if vin["type"] in ["pwm"]:
                return ["vin_pwmcounter.v"]
        return []
