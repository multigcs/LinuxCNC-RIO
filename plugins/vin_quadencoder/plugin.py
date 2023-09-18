class Plugin:
    ptype = "vin_quadencoder"

    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vin",
                "subtype": self.ptype,
                "comment": "quad-encoder input",
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
                pinlist_out.append((f"VIN{num}_ENCODER_A", pin_a, "INPUT", pullup))
                pinlist_out.append((f"VIN{num}_ENCODER_B", pin_b, "INPUT", pullup))
        return pinlist_out

    def vinnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data)
        return ret

    def funcs(self):
        func_out = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                debounce = data.get("debounce", False)
                quadType = data.get("quadType", 2)

                if debounce:
                    func_out.append(f"    wire VIN{num}_ENCODER_A_DEBOUNCED;")
                    func_out.append(f"    wire VIN{num}_ENCODER_B_DEBOUNCED;")
                    func_out.append(f"    debouncer #(16) vin_debouncer{num}_A (")
                    func_out.append("        .clk (sysclk),")
                    func_out.append(f"        .SIGNAL (VIN{num}_ENCODER_A),")
                    func_out.append(
                        f"        .SIGNAL_state (VIN{num}_ENCODER_A_DEBOUNCED)"
                    )
                    func_out.append("    );")
                    func_out.append(f"    debouncer #(16) vin_debouncer{num}_B (")
                    func_out.append("        .clk (sysclk),")
                    func_out.append(f"        .SIGNAL (VIN{num}_ENCODER_B),")
                    func_out.append(
                        f"        .SIGNAL_state (VIN{num}_ENCODER_B_DEBOUNCED)"
                    )
                    func_out.append("    );")

                func_out.append(
                    f"    vin_quadencoder #(32, {quadType}) vin_quadencoder{num} ("
                )
                func_out.append("        .clk (sysclk),")
                if debounce:
                    func_out.append(f"        .quadA (VIN{num}_ENCODER_A_DEBOUNCED),")
                    func_out.append(f"        .quadB (VIN{num}_ENCODER_B_DEBOUNCED),")
                else:
                    func_out.append(f"        .quadA (VIN{num}_ENCODER_A),")
                    func_out.append(f"        .quadB (VIN{num}_ENCODER_B),")
                func_out.append(f"        .pos ({nameIntern})")
                func_out.append("    );")
        return func_out

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                return ["vin_quadencoder.v"]
        return []
