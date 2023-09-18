class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "joints",
                "subtype": "joint_pwmdir",
                "comment": "using pwm/dir signals for joints / axis movements (DC-Motors)",
                "options": {
                    "enable": {
                        "type": "output",
                        "name": "enable pin",
                        "comment": "optional",
                    },
                    "pwm": {
                        "type": "output",
                        "name": "pwm pin",
                    },
                    "dir": {
                        "type": "output",
                        "name": "dir pin",
                    },
                },
            }
        ]

    def pinlist(self):
        pinlist_out = []
        for num, joint in enumerate(self.jdata["plugins"]):
            if joint["type"] == "joint_pwmdir":
                if "enable" in joint["pins"]:
                    pinlist_out.append(
                        (f"JOINT{num}_EN", joint["pins"]["enable"], "OUTPUT")
                    )
                pinlist_out.append(
                    (f"JOINT{num}_PWMDIR_PWM", joint["pins"]["pwm"], "OUTPUT")
                )
                pinlist_out.append(
                    (f"JOINT{num}_PWMDIR_DIR", joint["pins"]["dir"], "OUTPUT")
                )
                if joint.get("cl"):
                    pullup = joint["pins"].get("pullup", False)
                    pinlist_out.append(
                        (
                            f"JOINT{num}_PWMDIR_ENCA",
                            joint["pins"]["enc_a"],
                            "INPUT",
                            pullup,
                        )
                    )
                    pinlist_out.append(
                        (
                            f"JOINT{num}_PWMDIR_ENCB",
                            joint["pins"]["enc_b"],
                            "INPUT",
                            pullup,
                        )
                    )
        return pinlist_out

    def jointnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == "joint_pwmdir":
                name = data.get("name", f"JOINT.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data)
        return ret

    def funcs(self):
        func_out = []
        sysclk = int(self.jdata["clock"]["speed"])
        for num, joint in enumerate(self.jdata["plugins"]):
            if joint["type"] == "joint_pwmdir":
                name = joint.get("name", f"JOINT.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                pwm_freq = joint.get("frequency", 100000)
                if "enable" in joint["pins"]:
                    func_out.append(
                        f"    assign JOINT{num}_EN = jointEnable{num} && ~ERROR;"
                    )
                if joint.get("cl"):
                    func_out.append(f"    quad_encoder_pwm quad_encoder_pwm{num} (")
                    func_out.append("        .clk (sysclk),")
                    func_out.append(f"        .quadA (JOINT{num}_PWMDIR_ENCA),")
                    func_out.append(f"        .quadB (JOINT{num}_PWMDIR_ENCB),")
                    func_out.append(f"        .pos ({nameIntern}Feedback)")
                    func_out.append("    );")
                    func_out.append("    wire signed [31:0] jointFeedbackFake;")
                    func_out.append(
                        f"    joint_pwmdir #({int(sysclk / pwm_freq)}) joint_pwmdir{num} ("
                    )
                    func_out.append("        .clk (sysclk),")
                    func_out.append(
                        f"        .jointEnable (jointEnable{num} && !ERROR),"
                    )
                    func_out.append(f"        .jointFreqCmd ({nameIntern}FreqCmd),")
                    func_out.append("        .jointFeedback (jointFeedbackFake),")
                    func_out.append(f"        .DIR (JOINT{num}_PWMDIR_DIR),")
                    func_out.append(f"        .PWM (JOINT{num}_PWMDIR_PWM)")
                    func_out.append("    );")
                else:
                    func_out.append(
                        f"    joint_pwmdir #({int(sysclk / pwm_freq)}) joint_pwmdir{num} ("
                    )
                    func_out.append("        .clk (sysclk),")
                    func_out.append(
                        f"        .jointEnable (jointEnable{num} && !ERROR),"
                    )
                    func_out.append(f"        .jointFreqCmd ({nameIntern}FreqCmd),")
                    func_out.append(f"        .jointFeedback ({nameIntern}Feedback),")
                    func_out.append(f"        .DIR (JOINT{num}_PWMDIR_DIR),")
                    func_out.append(f"        .PWM (JOINT{num}_PWMDIR_PWM)")
                    func_out.append("    );")

        return func_out

    def ips(self):
        for num, joint in enumerate(self.jdata["plugins"]):
            if joint["type"] == "joint_pwmdir":
                return ["joint_pwmdir.v"]
        return []
