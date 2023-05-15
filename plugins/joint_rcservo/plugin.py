class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def pinlist(self):
        pinlist_out = []
        for num, joint in enumerate(self.jdata["joints"]):
            if joint["type"] == "rcservo":
                if "enable" in joint["pins"]:
                    pinlist_out.append(
                        (f"JOINT{num}_EN", joint["pins"]["enable"], "OUTPUT")
                    )
                pinlist_out.append(
                    (f"JOINT{num}_RCSERVO", joint["pins"]["pwm"], "OUTPUT")
                )
        return pinlist_out

    def joints(self):
        joints_out = 0
        for _num, joint in enumerate(self.jdata["joints"]):
            if joint["type"] == "rcservo":
                joints_out += 1
        return joints_out

    def jointcalcs(self):
        jointcalcs_out = {}
        sysclk = int(self.jdata["clock"]["speed"])
        for num, joint in enumerate(self.jdata["joints"]):
            if joint["type"] == "rcservo":
                jointcalcs_out[num] = ("none", int(sysclk / 1000 * 0.5))  # max +-0.5ms
        return jointcalcs_out

    def funcs(self):
        func_out = ["    // joint_rcservo's"]
        sysclk = int(self.jdata["clock"]["speed"])
        for num, joint in enumerate(self.jdata["joints"]):
            if joint["type"] == "rcservo":
                scale = joint.get("scale", 64)
                if "enable" in joint["pins"]:
                    func_out.append(
                        f"    assign JOINT{num}_EN = jointEnable{num} && ~ERROR;"
                    )
                func_out.append(
                    f"    joint_rcservo #({int(sysclk / 1000 * 12)}, {int(sysclk / 1000 * 1.5)}, {scale}) joint_rcservo{num} ("
                )
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .jointFreqCmd (jointFreqCmd{num}),")
                func_out.append(f"        .jointFeedback (jointFeedback{num}),")
                func_out.append(f"        .PWM (JOINT{num}_RCSERVO)")
                func_out.append("    );")

        return func_out

    def ips(self):
        return ["joint_rcservo.v"]
