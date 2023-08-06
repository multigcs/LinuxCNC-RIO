class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vin",
                "subtype": "vin_pwm",
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
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == "vin_pwm":
                pullup = data.get("pullup", False)
                pinlist_out.append((f"VIN{num}_PWM", data["pin"], "INPUT", pullup))
        return pinlist_out

    def vinnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == "vin_pwm":
                name = data.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data)
        return ret

    def funcs(self):
        func_out = ["    // vin_pwmcounter's"]
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == "vin_pwm":
                name = data.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                freq_min = int(data.get("freq_min", 10))
                func_out.append(
                    f"    vin_pwmcounter #({int(self.jdata['clock']['speed']) // freq_min}) vin_pwmcounter{num} ("
                )
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .frequency ({nameIntern}),")
                func_out.append(f"        .SIGNAL (VIN{num}_PWM)")
                func_out.append("    );")
        return func_out

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] in ["vin_pwm"]:
                return ["vin_pwmcounter.v"]
        return []
