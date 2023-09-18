class Plugin:
    ptype = "din_toggle"

    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "din",
                "subtype": self.ptype,
                "comment": "toggle binary input pin",
                "options": {
                    "name": {
                        "type": "str",
                        "name": "pin name",
                        "comment": "the name of the pin",
                        "default": "",
                    },
                    "net": {
                        "type": "dtarget",
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
                        "name": "input pin",
                        "comment": "activates the internal pullup resistor for this pin",
                        "default": False,
                    },
                    "invert": {
                        "type": "bool",
                        "name": "invert pin",
                        "comment": "invert this pin",
                        "default": False,
                    },
                },
            },
        ]

    def pinlist(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                pullup = data.get("pullup", False)
                ret.append((f"TOGGLE{num}", data["pin"], "INPUT", pullup))
        return ret

    def dinnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"DIN.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data)
        return ret

    def defs(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"DIN.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                ret.append(f"    wire {nameIntern};")
        return ret

    def funcs(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"DIN.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                invert = data.get("invert", False)
                debounce = data.get("debounce", False)
                debounce_val = 16
                if debounce:
                    if debounce is not True:
                        debounce_val = debounce

                if invert:
                    ret.append(f"    wire TOGGLE{num}_INVERTED;")
                    ret.append(f"    assign TOGGLE{num}_INVERTED = ~TOGGLE{num};")

                if debounce:
                    ret.append(f"    wire TOGGLE{num}_DEBOUNCED;")
                    ret.append(f"    debouncer #({debounce_val}) din_debouncer{num} (")
                    ret.append("        .clk (sysclk),")
                    if invert:
                        ret.append(f"        .SIGNAL (TOGGLE{num}_INVERTED),")
                    else:
                        ret.append(f"        .SIGNAL (TOGGLE{num}),")
                    ret.append(f"        .SIGNAL_state (TOGGLE{num}_DEBOUNCED)")
                    ret.append("    );")

                ret.append(f"    din_toggle din_toggle{num} (")
                ret.append("        .clk (sysclk),")
                if debounce:
                    ret.append(f"        .din (TOGGLE{num}_DEBOUNCED),")
                elif invert:
                    ret.append(f"        .din (TOGGLE{num}_INVERTED),")
                else:
                    ret.append(f"        .din (TOGGLE{num}),")
                ret.append(f"        .toggled ({nameIntern})")
                ret.append("    );")
        return ret

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                return ["din_toggle.v"]
        return []
