class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "joints",
                "subtype": "stepper",
                "options": {
                    "cl": {
                        "type": "bool",
                        "name": "closed loop",
                    },
                    "pins": {
                        "type": "dict",
                        "name": "pin config",
                        "options": {
                            "step": {
                                "type": "output",
                                "name": "stepper pin",
                            },
                            "dir": {
                                "type": "output",
                                "name": "dir pin",
                            },
                            "en": {
                                "type": "output",
                                "name": "enable pin",
                            },
                            "enc_a": {
                                "type": "input",
                                "name": "encoder A pin",
                            },
                            "enc_b": {
                                "type": "input",
                                "name": "encoder B pin",
                            },
                        },
                    },
                },
            }
        ]
    def types(self):
        return ["stepper", ]

    def entry_info(self, joint):
        info = ""
        if joint.get("type") == "stepper":
            if joint.get("cl"):
                info += "CL-Stepper ("
            else:
                info += "Stepper ("
            for ptype, pname in joint["pins"].items():
                info += f" {ptype}:{pname}"
            info += ")"
        return info


    def pinlist(self):
        pinlist_out = []
        for num, joint in enumerate(self.jdata["joints"]):
            if joint["type"] == "stepper":
                if "enable" in joint["pins"]:
                    pinlist_out.append(
                        (f"JOINT{num}_EN", joint["pins"]["enable"], "OUTPUT")
                    )
                pinlist_out.append(
                    (f"JOINT{num}_STEPPER_STP", joint["pins"]["step"], "OUTPUT")
                )
                pinlist_out.append(
                    (f"JOINT{num}_STEPPER_DIR", joint["pins"]["dir"], "OUTPUT")
                )
                if joint.get("cl"):
                    pullup = joint["pins"].get("pullup", False)
                    pinlist_out.append(
                        (
                            f"JOINT{num}_STEPPER_ENCA",
                            joint["pins"]["enc_a"],
                            "INPUT",
                            pullup,
                        )
                    )
                    pinlist_out.append(
                        (
                            f"JOINT{num}_STEPPER_ENCB",
                            joint["pins"]["enc_b"],
                            "INPUT",
                            pullup,
                        )
                    )
        return pinlist_out

    def joints(self):
        joints_out = 0
        for _num, joint in enumerate(self.jdata["joints"]):
            if joint["type"] == "stepper":
                joints_out += 1
        return joints_out

    def jointcalcs(self):
        jointcalcs_out = {}
        # sysclk = int(self.jdata["clock"]["speed"])
        for num, joint in enumerate(self.jdata["joints"]):
            if joint["type"] == "stepper":
                jointcalcs_out[num] = ("oscdiv", int(10000))  # max 100khz
        return jointcalcs_out

    def funcs(self):
        func_out = ["    // joint_stepper's"]
        for num, joint in enumerate(self.jdata["joints"]):
            if joint["type"] == "stepper":
                invert_dir = joint.get("invert_dir", False)

                if "enable" in joint["pins"]:
                    func_out.append(
                        f"    assign JOINT{num}_EN = jointEnable{num} && ~ERROR;"
                    )
                if invert_dir:
                    func_out.append(f"    wire JOINT{num}_STEPPER_DIR_INVERTED; // inverted dir wire")
                    func_out.append(f"    assign JOINT{num}_STEPPER_DIR = !JOINT{num}_STEPPER_DIR_INVERTED; // invert dir output")

                if joint.get("cl"):
                    func_out.append(f"    quad_encoder quad{num} (")
                    func_out.append("        .clk (sysclk),")
                    func_out.append(f"        .quadA (JOINT{num}_STEPPER_ENCA),")
                    func_out.append(f"        .quadB (JOINT{num}_STEPPER_ENCB),")
                    func_out.append(f"        .pos (jointFeedback{num})")
                    func_out.append("    );")
                    func_out.append(f"    joint_stepper_nf joint_stepper{num} (")
                    func_out.append("        .clk (sysclk),")
                    func_out.append(
                        f"        .jointEnable (jointEnable{num} && !ERROR),"
                    )
                    func_out.append(f"        .jointFreqCmd (jointFreqCmd{num}),")

                else:
                    func_out.append(f"    joint_stepper joint_stepper{num} (")
                    func_out.append("        .clk (sysclk),")
                    func_out.append(
                        f"        .jointEnable (jointEnable{num} && !ERROR),"
                    )
                    func_out.append(f"        .jointFreqCmd (jointFreqCmd{num}),")
                    func_out.append(f"        .jointFeedback (jointFeedback{num}),")

                if invert_dir:
                    func_out.append(f"        .DIR (JOINT{num}_STEPPER_DIR_INVERTED),")
                else:
                    func_out.append(f"        .DIR (JOINT{num}_STEPPER_DIR),")
                func_out.append(f"        .STP (JOINT{num}_STEPPER_STP)")
                func_out.append("    );")


        return func_out

    def ips(self):
        for num, joint in enumerate(self.jdata["joints"]):
            if joint["type"] in ["stepper"]:
                return ["quad_encoder.v", "joint_stepper.v", "joint_stepper_nf.v"]
        return []
