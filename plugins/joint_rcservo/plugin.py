class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "joints",
                "subtype": "joint_rcservo",
                "comment": "using rcservo's for joints / axis movements",
                "options": {
                    "pins": {
                        "type": "dict",
                        "name": "pin config",
                        "options": {
                            "pwm": {
                                "type": "output",
                                "name": "pwm pin",
                            },
                        },
                    },
                },
            }
        ]

    def pinlist(self):
        pinlist_out = []
        for num, joint in enumerate(self.jdata["plugins"]):
            if joint["type"] == "joint_rcservo":
                if "enable" in joint["pins"]:
                    pinlist_out.append(
                        (f"JOINT{num}_EN", joint["pins"]["enable"], "OUTPUT")
                    )
                pinlist_out.append(
                    (f"JOINT{num}_RCSERVO", joint["pins"]["pwm"], "OUTPUT")
                )
        return pinlist_out

    def jointnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == "joint_rcservo":
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
            if joint["type"] == "joint_rcservo":
                name = joint.get("name", f"JOINT.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                rate = joint.get("rate", 50)
                center = joint.get("center", 1.5)
                diff = joint.get("range", 0.5)

                rate_divider = int(sysclk / rate)
                center_divider = int(sysclk * center / 1000)
                diff_divider = int(sysclk * diff / 1000)

                if joint.get("invert", False):
                    func_out.append(f"    wire JOINT{num}_RCSERVO_INV;")
                    func_out.append(
                        f"    assign JOINT{num}_RCSERVO = ~JOINT{num}_RCSERVO_INV;"
                    )

                if "enable" in joint["pins"]:
                    func_out.append(
                        f"    assign JOINT{num}_EN = jointEnable{num} && ~ERROR;"
                    )
                func_out.append(
                    f"    // output at {rate}Hz, center: {center}ms, range: +-{diff}ms"
                )

                func_out.append(
                    f"    joint_rcservo #({rate_divider}, {center_divider}, {diff_divider}) joint_rcservo{num} ("
                )
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .jointFreqCmd ({nameIntern}FreqCmd),")
                func_out.append(f"        .jointFeedback ({nameIntern}Feedback),")
                if joint.get("invert", False):
                    func_out.append(f"        .PWM (JOINT{num}_RCSERVO_INV)")
                else:
                    func_out.append(f"        .PWM (JOINT{num}_RCSERVO)")
                func_out.append("    );")

        return func_out

    def ips(self):
        for num, joint in enumerate(self.jdata["plugins"]):
            if joint["type"] in ["joint_rcservo"]:
                return ["joint_rcservo.v"]
        return []
