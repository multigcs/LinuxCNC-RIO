class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vin",
                "subtype": "mpgencoder",
                "comment": "mpg-encoder input",
                "options": {
                    "debounce": {
                        "type": "bool",
                        "name": "debounce",
                        "default": False,
                        "comment": "this option adds an debouncer to the input-pins",
                    },
                    "pin_a": {
                        "type": "input",
                        "name": "input pin A",
                    },
                    "pin_b": {
                        "type": "input",
                        "name": "input pin B",
                    },
                },
            }
        ]

    def pinlist(self):
        pinlist_out = []
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "mpgencoder":
                pullup = vin.get("pullup", False)
                pinlist_out.append(
                    (f"VIN{num}_ENCODER_A", vin["pin_a"], "INPUT", pullup)
                )
                pinlist_out.append(
                    (f"VIN{num}_ENCODER_B", vin["pin_b"], "INPUT", pullup)
                )
        return pinlist_out

    def vins(self):
        vins_out = 0
        for _num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "mpgencoder":
                vins_out += 1
        return vins_out

    def funcs(self):
        func_out = ["    // vin_mpgencoder's"]
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "mpgencoder":
                debounce = vin.get("debounce", False)
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

                func_out.append(f"    vin_mpgencoder #(32) vin_mpgencoder{num} (")
                func_out.append("        .clk (sysclk),")
                if debounce:
                    func_out.append(f"        .quadA (VIN{num}_ENCODER_A_DEBOUNCED),")
                    func_out.append(f"        .quadB (VIN{num}_ENCODER_B_DEBOUNCED),")
                else:
                    func_out.append(f"        .quadA (VIN{num}_ENCODER_A),")
                    func_out.append(f"        .quadB (VIN{num}_ENCODER_B),")
                func_out.append(f"        .pos (processVariable{num})")
                func_out.append("    );")

        return func_out

    def ips(self):
        for num, vin in enumerate(self.jdata["vin"]):
            if vin["type"] in ["mpgencoder"]:
                return ["vin_mpgencoder.v"]
        return []
