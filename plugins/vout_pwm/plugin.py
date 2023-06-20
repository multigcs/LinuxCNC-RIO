class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vout",
                "subtype": "pwm",
                "options": {
                    "frequency": {
                        "type": "int",
                        "name": "pwm frequency",
                        "comment": "pwm frequency in Hz",
                        "defaut": 10000,
                    },
                    "dir": {
                        "type": "output",
                        "name": "dir output pin",
                    },
                    "pin": {
                        "type": "output",
                        "name": "pwm output pin",
                    },
                    "invert_pwm": {
                        "type": "bool",
                        "name": "inverted pwm pin",
                        "default": False,
                        "comment": "this option inverts the pwm signal",
                    },
                },
            },
            {
                "basetype": "vout",
                "subtype": "rcservo",
                "options": {
                    "frequency": {
                        "type": "int",
                        "name": "pwm frequency",
                        "comment": "servo update-rate in Hz (max 50Hz for old analog servos)",
                        "defaut": 100,
                    },
                    "pin": {
                        "type": "output",
                        "name": "pwm output pin",
                    },
                    "invert_pwm": {
                        "type": "bool",
                        "name": "inverted pwm pin",
                        "comment": "this option inverts the pwm signal",
                    },
                },
            }
        ]

    def types(self):
        return ["pwm", "rcservo", ]

    def pinlist(self):
        pinlist_out = []
        for num, vout in enumerate(self.jdata["vout"]):
            if vout["type"] in ["pwm", "rcservo"]:
                if "dir" in vout:
                    pinlist_out.append((f"VOUT{num}_PWM_DIR", vout["dir"], "OUTPUT"))
                pinlist_out.append((f"VOUT{num}_PWM_PWM", vout["pin"], "OUTPUT"))
        return pinlist_out

    def vouts(self):
        vouts_out = 0
        for _num, vout in enumerate(self.jdata["vout"]):
            if vout["type"] in ["pwm", "rcservo"]:
                vouts_out += 1
        return vouts_out

    def defs(self):
        func_out = ["    // vout_pwm's"]
        for num, vout in enumerate(self.jdata["vout"]):
            if vout["type"] in ["pwm", "rcservo"]:
                if "dir" not in vout:
                    func_out.append(
                        f"    wire VOUT{num}_PWM_DIR; // fake direction output"
                    )
                invert_pwm = vout.get("invert_pwm", False)
                if invert_pwm:
                    func_out.append(
                        f"    wire VOUT{num}_PWM_PWM_INVERTED; // inverted pwm wire"
                    )
        return func_out


    def funcs(self):
        func_out = ["    // vout_pwm's"]
        for num, vout in enumerate(self.jdata["vout"]):
            if vout["type"] in ["pwm", "rcservo"]:
                if vout["type"] == "rcservo":
                    freq = int(vout.get("frequency", 100))
                else:
                    freq = int(vout.get("frequency", 10000))
                divider = int(self.jdata["clock"]["speed"]) // freq
                invert_pwm = vout.get("invert_pwm", False)
                if invert_pwm:
                    func_out.append(
                        f"    assign VOUT{num}_PWM_PWM = !VOUT{num}_PWM_PWM_INVERTED; // invert pwm output"
                    )
                func_out.append(f"    vout_pwm #({divider}) vout_pwm{num} (")
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .dty (setPoint{num}),")
                func_out.append(f"        .disabled (ERROR),")
                func_out.append(f"        .dir (VOUT{num}_PWM_DIR),")
                if invert_pwm:
                    func_out.append(f"        .pwm (VOUT{num}_PWM_PWM_INVERTED)")
                else:
                    func_out.append(f"        .pwm (VOUT{num}_PWM_PWM)")
                func_out.append("    );")
        return func_out

    def ips(self):
        for num, vout in enumerate(self.jdata["vout"]):
            if vout["type"] in ["pwm", "rcservo"]:
                return ["vout_pwm.v"]
        return []
