class Plugin:
    ptype = "vin_quadencoderz"

    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vin",
                "subtype": self.ptype,
                "comment": "quad-encoder input with z-pin",
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
                    "debounce": {
                        "type": "bool",
                        "name": "debounce",
                        "default": False,
                        "comment": "this option adds an debouncer to the input-pins",
                    },
                    "quadType": {
                        "type": "int",
                        "name": "type of encoder (0, 2)",
                        "default": "2",
                    },
                    "pins": {
                        "type": "dict",
                        "options": {
                            "a": {
                                "type": "input",
                                "name": "input pin A",
                            },
                            "b": {
                                "type": "input",
                                "name": "input pin B",
                            },
                            "z": {
                                "type": "input",
                                "name": "input pin Z",
                            },
                        },
                    },
                },
            }
        ]

    def pinlist(self):
        pinlist_out = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                pullup = data.get("pullup", False)
                pins = data.get("pins", {})
                pin_a = pins.get("a", data.get("pin_a"))
                pin_b = pins.get("b", data.get("pin_b"))
                pin_z = pins.get("z", data.get("pin_z"))
                pinlist_out.append((f"VIN{num}_ENCODER_A", pin_a, "INPUT", pullup))
                pinlist_out.append((f"VIN{num}_ENCODER_B", pin_b, "INPUT", pullup))
                pinlist_out.append((f"VIN{num}_ENCODER_Z", pin_z, "INPUT", pullup))
        return pinlist_out

    def vinnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data.copy())
        return ret

    def dinnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"PV.{num}") + "-index-enable-out"
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data.copy())
        return ret

    def doutnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"PV.{num}") + "-index-enable"
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data.copy())
        return ret

    def defs(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                ret.append(f"    wire {nameIntern}_INDEX_ENABLE_OUT;")
                ret.append(f"    wire {nameIntern}_INDEX_ENABLE;")
        return ret

    def funcs(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                debounce = data.get("debounce", False)
                quadType = data.get("quadType", 2)
                if debounce:
                    ret.append(f"    wire VIN{num}_ENCODER_A_DEBOUNCED;")
                    ret.append(f"    wire VIN{num}_ENCODER_B_DEBOUNCED;")
                    ret.append(f"    wire VIN{num}_ENCODER_Z_DEBOUNCED;")
                    ret.append(f"    debouncer #(16) vin_debouncer{num}_A (")
                    ret.append("        .clk (sysclk),")
                    ret.append(f"        .SIGNAL (VIN{num}_ENCODER_A),")
                    ret.append(f"        .SIGNAL_state (VIN{num}_ENCODER_A_DEBOUNCED)")
                    ret.append("    );")
                    ret.append(f"    debouncer #(16) vin_debouncer{num}_B (")
                    ret.append("        .clk (sysclk),")
                    ret.append(f"        .SIGNAL (VIN{num}_ENCODER_B),")
                    ret.append(f"        .SIGNAL_state (VIN{num}_ENCODER_B_DEBOUNCED)")
                    ret.append("    );")
                    ret.append(f"    debouncer #(16) vin_debouncer{num}_Z (")
                    ret.append("        .clk (sysclk),")
                    ret.append(f"        .SIGNAL (VIN{num}_ENCODER_Z),")
                    ret.append(f"        .SIGNAL_state (VIN{num}_ENCODER_Z_DEBOUNCED)")
                    ret.append("    );")

                ret.append(
                    f"    vin_quadencoderz #(32, {quadType}) vin_quadencoderz{num} ("
                )
                ret.append("        .clk (sysclk),")
                if debounce:
                    ret.append(f"        .quadA (VIN{num}_ENCODER_A_DEBOUNCED),")
                    ret.append(f"        .quadB (VIN{num}_ENCODER_B_DEBOUNCED),")
                    ret.append(f"        .quadZ (VIN{num}_ENCODER_Z_DEBOUNCED),")
                else:
                    ret.append(f"        .quadA (VIN{num}_ENCODER_A),")
                    ret.append(f"        .quadB (VIN{num}_ENCODER_B),")
                    ret.append(f"        .quadZ (VIN{num}_ENCODER_Z),")
                ret.append(f"        .index_enable ({nameIntern}_INDEX_ENABLE),")
                ret.append(f"        .index_out ({nameIntern}_INDEX_ENABLE_OUT),")
                ret.append(f"        .pos ({nameIntern})")
                ret.append("    );")
        return ret

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                return ["vin_quadencoderz.v"]
        return []
