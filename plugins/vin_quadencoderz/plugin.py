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
                    "name": {
                        "type": "str",
                        "name": "pin name",
                        "comment": "the name of the pin",
                        "default": '',
                    },
                    "net": {
                        "type": "vtarget",
                        "name": "net target",
                        "comment": "the target net of the pin in the hal",
                        "default": '',
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
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "quadencoderz":
                pullup = vin.get("pullup", False)
                pins = vin.get("pins", {})
                pin_a = pins.get("a", vin.get("pin_a"))
                pin_b = pins.get("b", vin.get("pin_b"))
                pin_z = pins.get("z", vin.get("pin_z"))
                pinlist_out.append(
                    (f"VIN{num}_ENCODER_A", pin_a, "INPUT", pullup)
                )
                pinlist_out.append(
                    (f"VIN{num}_ENCODER_B", pin_b, "INPUT", pullup)
                )
                pinlist_out.append(
                    (f"VIN{num}_ENCODER_Z", pin_z, "INPUT", pullup)
                )
        return pinlist_out

    def vins(self):
        vins_out = 0
        for _num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "quadencoderz":
                vins_out += 1
        return vins_out

    def vdata(self):
        vdata = []
        for _num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "quadencoderz":
                vdata.append(vin)
        return vdata

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
        vin_num = 0
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "quadencoderz":
                dins_out.append((f"VIN{num}_ENCODER_INDEX_OUT", f"PV.{vin_num}-index-enable-out"))
            vin_num += vin.get("vars", 1)
        return dins_out

    def doutnames(self):
        douts_out = []
        vin_num = 0
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "quadencoderz":
                douts_out.append((f"VIN{num}_ENCODER_INDEX_ENABLE", f"PV.{vin_num}-index-enable"))
            vin_num += vin.get("vars", 1)
        return douts_out

    def defs(self):
        defs_out = ["    // vin_quadencoderz's"]
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "quadencoderz":
                defs_out.append(f"    wire VIN{num}_ENCODER_INDEX_OUT;")
                defs_out.append(f"    wire VIN{num}_ENCODER_INDEX_ENABLE;")
        return defs_out


    def funcs(self):
        func_out = ["    // vin_quadencoderz's"]
        vin_num = 0
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "quadencoderz":
                debounce = vin.get("debounce", False)
                quadType = vin.get("quadType", 2)
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

                func_out.append(f"    vin_quadencoderz #(32, {quadType}) vin_quadencoderz{num} (")
                func_out.append("        .clk (sysclk),")
                if debounce:
                    func_out.append(f"        .quadA (VIN{num}_ENCODER_A_DEBOUNCED),")
                    func_out.append(f"        .quadB (VIN{num}_ENCODER_B_DEBOUNCED),")
                    func_out.append(f"        .quadZ (VIN{num}_ENCODER_Z_DEBOUNCED),")
                else:
                    func_out.append(f"        .quadA (VIN{num}_ENCODER_A),")
                    func_out.append(f"        .quadB (VIN{num}_ENCODER_B),")
                    func_out.append(f"        .quadZ (VIN{num}_ENCODER_Z),")
                func_out.append(f"        .index_enable (VIN{num}_ENCODER_INDEX_ENABLE),")
                func_out.append(f"        .index_out (VIN{num}_ENCODER_INDEX_OUT),")
                func_out.append(f"        .pos (processVariable{vin_num})")
                func_out.append("    );")
            vin_num += vin.get("vars", 1)
        return func_out

    def ips(self):
        for num, vin in enumerate(self.jdata["vin"]):
            if vin["type"] in ["quadencoderz"]:
                return ["vin_quadencoderz.v"]
        return []
