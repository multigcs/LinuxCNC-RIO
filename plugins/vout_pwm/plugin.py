class Plugin:
    ptype = "vout_pwm"

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
                    "frequency": {
                        "type": "int",
                        "name": "pwm frequency",
                        "comment": "pwm frequency in Hz",
                        "default": "10000",
                    },
                    "invert_pwm": {
                        "type": "bool",
                        "name": "inverted pwm pin",
                        "default": False,
                        "comment": "this option inverts the pwm signal",
                    },
                    "pins": {
                        "type": "dict",
                        "options": {
                            "dir": {
                                "type": "output",
                                "name": "dir output pin",
                            },
                            "pwm": {
                                "type": "output",
                                "name": "pwm output pin",
                            },
                        },
                    },
                },
            }
        ]

    def pinlist(self):
        pinlist_out = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                if "pins" not in data:
                    data["pins"] = {
                        "pwm": data["pin"],
                    }
                    if "dir" in data:
                        data["pins"]["dir"] = data["dir"]
                    print(
                        f"WARNING: {data['type']}: please use new format for pins: '\"pins\": {data['pins']}'"
                    )
                pins = data["pins"]
                if "dir" in pins:
                    pinlist_out.append((f"VOUT{num}_PWM_DIR", pins["dir"], "OUTPUT"))
                pinlist_out.append((f"VOUT{num}_PWM_PWM", pins["pwm"], "OUTPUT"))
        return pinlist_out

    def voutnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                name = data.get("name", f"SP.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data)
        return ret

    def defs(self):
        func_out = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                pins = data["pins"]
                if "dir" not in pins:
                    func_out.append(
                        f"    wire VOUT{num}_PWM_DIR; // fake direction output"
                    )
                invert_pwm = data.get("invert_pwm", False)
                if invert_pwm:
                    func_out.append(
                        f"    wire VOUT{num}_PWM_PWM_INVERTED; // inverted pwm wire"
                    )
        return func_out

    def funcs(self):
        func_out = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                name = data.get("name", f"SP.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                if data["type"] == "rcservo":
                    freq = int(data.get("frequency", 100))
                else:
                    freq = int(data.get("frequency", 10000))
                divider = int(self.jdata["clock"]["speed"]) // freq
                invert_pwm = data.get("invert_pwm", False)
                if invert_pwm:
                    func_out.append(
                        f"    assign VOUT{num}_PWM_PWM = ~VOUT{num}_PWM_PWM_INVERTED; // invert pwm output"
                    )
                func_out.append(f"    vout_pwm #({divider}) vout_pwm{num} (")
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .dty ({nameIntern}),")
                func_out.append("        .disabled (ERROR),")
                func_out.append(f"        .dir (VOUT{num}_PWM_DIR),")
                if invert_pwm:
                    func_out.append(f"        .pwm (VOUT{num}_PWM_PWM_INVERTED)")
                else:
                    func_out.append(f"        .pwm (VOUT{num}_PWM_PWM)")
                func_out.append("    );")
        return func_out

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                return ["vout_pwm.v"]
        return []
