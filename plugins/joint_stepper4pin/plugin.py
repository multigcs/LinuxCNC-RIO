class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "joints",
                "subtype": "joint_stepper4pin",
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
                            "a1": {
                                "type": "output",
                                "name": "stepper a1 pin",
                                "comment": "stepper a1 pin",
                            },
                            "a2": {
                                "type": "output",
                                "name": "stepper a2 pin",
                                "comment": "stepper a2 pin",
                            },
                            "b1": {
                                "type": "output",
                                "name": "stepper b1 pin",
                                "comment": "stepper b1 pin",
                            },
                            "b2": {
                                "type": "output",
                                "name": "stepper b2 pin",
                                "comment": "stepper b2 pin",
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
        if joint.get("type") == "joint_stepper4pin":
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
            if joint["type"] == "joint_stepper4pin":
                pinlist_out.append(
                    (f"JOINT{num}_STEPPER_A1", joint["pins"]["1a"], "OUTPUT")
                )
                pinlist_out.append(
                    (f"JOINT{num}_STEPPER_A2", joint["pins"]["2a"], "OUTPUT")
                )
                pinlist_out.append(
                    (f"JOINT{num}_STEPPER_B1", joint["pins"]["1b"], "OUTPUT")
                )
                pinlist_out.append(
                    (f"JOINT{num}_STEPPER_B2", joint["pins"]["2b"], "OUTPUT")
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
            if data.get("type") == "joint_stepper4pin":
                name = data.get("name", f"JOINT.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data)
        return ret

    def funcs(self):
        func_out = []
        for num, joint in enumerate(self.jdata["plugins"]):
            if joint["type"] == "joint_stepper4pin":
                name = joint.get("name", f"JOINT.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                steptype = joint.get("steptype", 1)

                if joint.get("cl") and "enc_a" in joint["pins"]:
                    func_out.append(f"    quad_encoder quad{num} (")
                    func_out.append("        .clk (sysclk),")
                    func_out.append(f"        .quadA (JOINT{num}_STEPPER_ENCA),")
                    func_out.append(f"        .quadB (JOINT{num}_STEPPER_ENCB),")
                    func_out.append(f"        .pos ({nameIntern}Feedback)")
                    func_out.append("    );")
                    func_out.append(f"    joint_stepper4pin_nf #(.STEPTYPE({steptype})) joint_stepper4pin{num} (")
                    func_out.append("        .clk (sysclk),")
                    func_out.append(
                        f"        .jointEnable ({nameIntern}Enable && !ERROR),"
                    )
                    func_out.append(f"        .jointFreqCmd ({nameIntern}FreqCmd),")

                else:
                    func_out.append(f"    joint_stepper4pin #(.STEPTYPE({steptype})) joint_stepper4pin{num} (")
                    func_out.append("        .clk (sysclk),")
                    func_out.append(
                        f"        .jointEnable ({nameIntern}Enable && !ERROR),"
                    )
                    func_out.append(f"        .jointFreqCmd ({nameIntern}FreqCmd),")
                    func_out.append(f"        .jointFeedback ({nameIntern}Feedback),")

                func_out.append(f"        .a1 (JOINT{num}_STEPPER_A1),")
                func_out.append(f"        .a2 (JOINT{num}_STEPPER_A2),")
                func_out.append(f"        .b1 (JOINT{num}_STEPPER_B1),")
                func_out.append(f"        .b2 (JOINT{num}_STEPPER_B2)")
                func_out.append("    );")

        return func_out

    def ips(self):
        for num, joint in enumerate(self.jdata["plugins"]):
            if joint["type"] in ["joint_stepper4pin"]:
                return ["quad_encoder.v", "joint_stepper4pin.v", "joint_stepper4pin_nf.v"]
        return []
