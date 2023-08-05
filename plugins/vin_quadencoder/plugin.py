class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vin",
                "subtype": "quadencoder",
                "comment": "quad-encoder input",
                "options": {
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
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "quadencoder":
                pullup = vin.get("pullup", False)
                pins = vin.get("pins", {})
                pin_a = pins.get("a", vin.get("pin_a"))
                pin_b = pins.get("b", vin.get("pin_b"))
                pinlist_out.append(
                    (f"VIN{num}_ENCODER_A", pin_a, "INPUT", pullup)
                )
                pinlist_out.append(
                    (f"VIN{num}_ENCODER_B", pin_b, "INPUT", pullup)
                )
        return pinlist_out

    def vinnames(self):
        ret = []
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "quadencoder":
                name = vin.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                ret.append((nameIntern, name, vin))
        return ret

    def funcs(self):
        func_out = ["    // vin_quadencoder's"]
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "quadencoder" or vin.get("type") == "mpgencoder":
                name = vin.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                debounce = vin.get("debounce", False)
                quadType = vin.get("quadType", 2)

                if debounce:
                    func_out.append(f"    wire VIN{num}_ENCODER_A_DEBOUNCED;")
                    func_out.append(f"    wire VIN{num}_ENCODER_B_DEBOUNCED;")
                    func_out.append(f"    debouncer #(16) vin_debouncer{num}_A (")
                    func_out.append("        .clk (sysclk),")
                    func_out.append(f"        .SIGNAL (VIN{num}_ENCODER_A),")
                    func_out.append(f"        .SIGNAL_state (VIN{num}_ENCODER_A_DEBOUNCED)")
                    func_out.append("    );")
                    func_out.append(f"    debouncer #(16) vin_debouncer{num}_B (")
                    func_out.append("        .clk (sysclk),")
                    func_out.append(f"        .SIGNAL (VIN{num}_ENCODER_B),")
                    func_out.append(f"        .SIGNAL_state (VIN{num}_ENCODER_B_DEBOUNCED)")
                    func_out.append("    );")

                func_out.append(f"    vin_quadencoder #(32, {quadType}) vin_quadencoder{num} (")
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
        for num, vin in enumerate(self.jdata["vin"]):
            if vin["type"] in ["quadencoder"]:
                return ["vin_quadencoder.v"]
        return []
