class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def pinlist(self):
        pinlist_out = []
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "quadencoder":
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
            if vin.get("type") == "quadencoder":
                vins_out += 1
        return vins_out

    def funcs(self):
        func_out = ["    // vin_quadencoder's"]
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "quadencoder":
                func_out.append(f"    vin_quadencoder #(32) vin_quadencoder{num} (")
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .quadA (VIN{num}_ENCODER_A),")
                func_out.append(f"        .quadB (VIN{num}_ENCODER_B),")
                func_out.append(f"        .pos (processVariable{num})")
                func_out.append("    );")

        return func_out

    def ips(self):
        files = ["vin_quadencoder.v"]
        return files
