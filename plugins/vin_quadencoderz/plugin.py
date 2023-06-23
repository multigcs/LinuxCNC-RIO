class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vin",
                "subtype": "quadencoderz",
                "comment": "quad-encoder input with z-pin",
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
                    "pin_z": {
                        "type": "input",
                        "name": "input pin Z",
                    },
                },
            }
        ]

    def pinlist(self):
        pinlist_out = []
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "quadencoderz":
                pullup = vin.get("pullup", False)
                pinlist_out.append(
                    (f"VIN{num}_ENCODER_A", vin["pin_a"], "INPUT", pullup)
                )
                pinlist_out.append(
                    (f"VIN{num}_ENCODER_B", vin["pin_b"], "INPUT", pullup)
                )
                pinlist_out.append(
                    (f"VIN{num}_ENCODER_Z", vin["pin_z"], "INPUT", pullup)
                )
        return pinlist_out

    def vins(self):
        vins_out = 0
        for _num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "quadencoderz":
                vins_out += 1
        return vins_out

    def dins(self):
        dins_out = 0
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "quadencoderz":
                dins_out += 1
        return dins_out

    def douts(self):
        douts_out = 0
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "quadencoderz":
                douts_out += 1
        return douts_out

    def dinnames(self):
        dins_out = []
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "quadencoderz":
                dins_out.append(f"VIN{num}_ENCODER_RESET_OUT")
        return dins_out

    def doutnames(self):
        douts_out = []
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "quadencoderz":
                douts_out.append(f"VIN{num}_ENCODER_RESET_IN")
        return douts_out

    def defs(self):
        defs_out = ["    // vin_quadencoderz's"]
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "quadencoderz":
                defs_out.append(f"    wire VIN{num}_ENCODER_RESET_OUT;")
                defs_out.append(f"    wire VIN{num}_ENCODER_RESET_IN;")
        return defs_out


    def funcs(self):
        func_out = ["    // vin_quadencoderz's"]
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "quadencoderz":
                debounce = vin.get("debounce", False)

                if debounce:
                    func_out.append(f"    wire VIN{num}_ENCODER_A_DEBOUNCED;")
                    func_out.append(f"    wire VIN{num}_ENCODER_B_DEBOUNCED;")
                    func_out.append(f"    wire VIN{num}_ENCODER_Z_DEBOUNCED;")
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
                    func_out.append(f"    debouncer #(16) vin_debouncer{num}_Z (")
                    func_out.append("        .clk (sysclk),")
                    func_out.append(f"        .SIGNAL (VIN{num}_ENCODER_Z),")
                    func_out.append(f"        .SIGNAL_state (VIN{num}_ENCODER_Z_DEBOUNCED)")
                    func_out.append("    );")

                func_out.append(f"    vin_quadencoderz #(32) vin_quadencoderz{num} (")
                func_out.append("        .clk (sysclk),")
                if debounce:
                    func_out.append(f"        .quadA (VIN{num}_ENCODER_A_DEBOUNCED),")
                    func_out.append(f"        .quadB (VIN{num}_ENCODER_B_DEBOUNCED),")
                    func_out.append(f"        .quadZ (VIN{num}_ENCODER_Z_DEBOUNCED),")
                else:
                    func_out.append(f"        .quadA (VIN{num}_ENCODER_A),")
                    func_out.append(f"        .quadB (VIN{num}_ENCODER_B),")
                    func_out.append(f"        .quadZ (VIN{num}_ENCODER_Z),")
                func_out.append(f"        .reset_in (VIN{num}_ENCODER_RESET_IN),")
                func_out.append(f"        .reset_out (VIN{num}_ENCODER_RESET_OUT),")
                func_out.append(f"        .pos (processVariable{num})")
                func_out.append("    );")

        return func_out

    def ips(self):
        for num, vin in enumerate(self.jdata["vin"]):
            if vin["type"] in ["quadencoderz"]:
                return ["vin_quadencoderz.v"]
        return []
