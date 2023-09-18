class Plugin:
    ptype = "vin_pwm"

    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vin",
                "subtype": self.ptype,
                "comment": "measures the puls-lenght of pwm-signals on the input-pin",
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
            if data.get("type") == self.ptype:
                pullup = data.get("pullup", False)
                pinlist_out.append((f"VIN{num}_PWM", data["pin"], "INPUT", pullup))
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
            if data["type"] == self.ptype:
                return ["vin_pwmcounter.v"]
        return []
