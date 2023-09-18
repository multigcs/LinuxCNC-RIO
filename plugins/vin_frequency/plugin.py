class Plugin:
    ptype = "vin_frequency"

    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vin",
                "subtype": self.ptype,
                "comment": "measures the frequency of signals on the input-pin in Hz",
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
                    "pullup": {
                        "type": "bool",
                        "name": "internal pullup",
                    },
                    "freq_min": {
                        "type": "int",
                        "name": "min-frequency",
                        "default": 10,
                        "comment": "this is the minumum frequency in Hz on the input-pin, all below is set to 0 Hz",
                    },
                },
            }
        ]

    def pinlist(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                pullup = data.get("pullup", False)
                ret.append((f"VIN{num}_FREQUENCY", data["pin"], "INPUT", pullup))
        return ret

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
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                freq_min = int(data.get("freq_min", 10))
                debounce = data.get("debounce", False)
                debounce_val = 16
                if debounce:
                    if debounce is not True:
                        debounce_val = debounce
                    ret.append(f"    wire VIN{num}_FREQUENCY_DEBOUNCED;")
                    ret.append(f"    debouncer #({debounce_val}) din_debouncer{num} (")
                    ret.append("        .clk (sysclk),")
                    ret.append(f"        .SIGNAL (VIN{num}_FREQUENCY),")
                    ret.append(f"        .SIGNAL_state (VIN{num}_FREQUENCY_DEBOUNCED)")
                    ret.append("    );")

                ret.append(
                    f"    vin_frequency #({int(self.jdata['clock']['speed']) // freq_min}) vin_frequency{num} ("
                )
                ret.append("        .clk (sysclk),")
                ret.append(f"        .frequency ({nameIntern}),")
                if debounce:
                    ret.append(f"        .SIGNAL (VIN{num}_FREQUENCY_DEBOUNCED)")
                else:
                    ret.append(f"        .SIGNAL (VIN{num}_FREQUENCY)")
                ret.append("    );")

        return ret

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                return ["vin_frequency.v"]
        return []
