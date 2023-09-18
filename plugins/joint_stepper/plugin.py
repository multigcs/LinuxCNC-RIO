class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "joints",
                "subtype": "joint_stepper",
                "options": {
                    "cl": {
                        "type": "bool",
                        "name": "closed loop",
                        "comment": "using encoder for the feedback, this needs 2 extra pins (enc_a / enc_b)",
                    },
                    "invert_dir": {
                        "type": "bool",
                        "name": "invert dir pin",
                        "comment": "inverts the dir pin",
                    },
                    "scale": {
                        "type": "int",
                        "name": "axis scale",
                        "default": "800",
                    },
                    "pins": {
                        "type": "dict",
                        "name": "pin config",
                        "options": {
                            "step": {
                                "type": "output",
                                "name": "stepper pin",
                                "comment": "do not use expansion-pins here, we need very fast pulses",
                            },
                            "dir": {
                                "type": "output",
                                "name": "dir pin",
                            },
                            "en": {
                                "type": "output",
                                "name": "enable pin",
                                "comment": "this pin is optional",
                            },
                            "enc_a": {
                                "type": "input",
                                "name": "encoder A pin",
                                "comment": "this pin is optional / needed for closed-loop systems",
                            },
                            "enc_b": {
                                "type": "input",
                                "name": "encoder B pin",
                                "comment": "this pin is optional / needed for closed-loop systems",
                            },
                        },
                    },
                },
            }
        ]

    def types(self):
        return [
            "stepper",
        ]

    def entry_info(self, joint):
        info = ""
        if joint.get("type") == "joint_stepper":
            if joint.get("cl"):
                info += "CL-Stepper ("
            else:
                info += "Stepper ("
            for ptype, pname in joint["pins"].items():
                if pname:
                    info += f" {ptype}:{pname}"
            info += ")"
        return info

    def pinlist(self):
        pinlist_out = []
        for num, joint in enumerate(self.jdata["plugins"]):
            if joint["type"] == "joint_stepper":
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
                if joint.get("cl") and "enc_a" in joint["pins"]:
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

    def jointnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == "joint_stepper":
                name = data.get("name", f"JOINT.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data)
        return ret

    def funcs(self):
        func_out = []
        for num, joint in enumerate(self.jdata["plugins"]):
            if joint["type"] == "joint_stepper":
                name = joint.get("name", f"JOINT.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                invert_dir = joint.get("invert_dir", False)

                if "enable" in joint["pins"]:
                    func_out.append(
                        f"    assign JOINT{num}_EN = {nameIntern}Enable && ~ERROR;"
                    )
                if invert_dir:
                    func_out.append(
                        f"    wire JOINT{num}_STEPPER_DIR_INVERTED; // inverted dir wire"
                    )
                    func_out.append(
                        f"    assign JOINT{num}_STEPPER_DIR = !JOINT{num}_STEPPER_DIR_INVERTED; // invert dir output"
                    )

                if joint.get("cl") and "enc_a" in joint["pins"]:
                    func_out.append(f"    quad_encoder quad{num} (")
                    func_out.append("        .clk (sysclk),")
                    func_out.append(f"        .quadA (JOINT{num}_STEPPER_ENCA),")
                    func_out.append(f"        .quadB (JOINT{num}_STEPPER_ENCB),")
                    func_out.append(f"        .pos ({nameIntern}Feedback)")
                    func_out.append("    );")
                    func_out.append(f"    joint_stepper_nf joint_stepper{num} (")
                    func_out.append("        .clk (sysclk),")
                    func_out.append(
                        f"        .jointEnable ({nameIntern}Enable && !ERROR),"
                    )
                    func_out.append(f"        .jointFreqCmd ({nameIntern}FreqCmd),")

                else:
                    func_out.append(f"    joint_stepper joint_stepper{num} (")
                    func_out.append("        .clk (sysclk),")
                    func_out.append(
                        f"        .jointEnable ({nameIntern}Enable && !ERROR),"
                    )
                    func_out.append(f"        .jointFreqCmd ({nameIntern}FreqCmd),")
                    func_out.append(f"        .jointFeedback ({nameIntern}Feedback),")

                if invert_dir:
                    func_out.append(f"        .DIR (JOINT{num}_STEPPER_DIR_INVERTED),")
                else:
                    func_out.append(f"        .DIR (JOINT{num}_STEPPER_DIR),")
                func_out.append(f"        .STP (JOINT{num}_STEPPER_STP)")
                func_out.append("    );")

        return func_out

    def ips(self):
        for num, joint in enumerate(self.jdata["plugins"]):
            if joint["type"] in ["joint_stepper"]:
                return ["quad_encoder.v", "joint_stepper.v", "joint_stepper_nf.v"]
        return []
