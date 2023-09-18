class Plugin:
    ptype = "vout_sine"

    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vout",
                "subtype": self.ptype,
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
                        "type": "output",
                        "name": "output pin",
                    },
                },
            }
        ]

    def pinlist(self):
        pinlist_out = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                if "pins" in data:
                    for pn, pin in enumerate(data["pins"]):
                        pinlist_out.append((f"VOUT{num}_SINEPWM_{pn}", pin, "OUTPUT"))
                else:
                    pinlist_out.append((f"VOUT{num}_SINEPWM", data["pin"], "OUTPUT"))
        return pinlist_out

    def voutnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"SP.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data)
        return ret

    def funcs(self):
        func_out = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                name = data.get("name", f"SP.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                # frequency = int(data.get("frequency", 100000))
                # divider = int(self.jdata["clock"]["speed"]) // frequency // 2
                divider = 255
                if "pins" in data:
                    pstep = 30 // len(data["pins"])
                    start = 0
                    for pn, _pin in enumerate(data["pins"]):
                        func_out.append(
                            f"    vout_sinepwm #({start}, {divider}) vout_sinepwm{num}_{pn} ("
                        )
                        func_out.append("        .clk (sysclk),")
                        func_out.append(f"        .freq ({nameIntern}),")
                        func_out.append(f"        .pwm_out (VOUT{num}_SINEPWM_{pn})")
                        func_out.append("    );")
                        start = start + pstep

                else:
                    start = data.get("start", 0)
                    func_out.append(
                        f"    vout_sinepwm #({start}, {divider}) vout_sinepwm{num} ("
                    )
                    func_out.append("        .clk (sysclk),")
                    func_out.append(f"        .freq ({nameIntern}),")
                    func_out.append(f"        .pwm_out (VOUT{num}_SINEPWM)")
                    func_out.append("    );")
        return func_out

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                return ["vout_sinepwm.v"]
        return []
