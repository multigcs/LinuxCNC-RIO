class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vout",
                "subtype": "frequency",
                "options": {
                    "pin": {
                        "type": "input",
                        "name": "output pin",
                    },
                },
            }
        ]

    def pinlist(self):
        pinlist_out = []
        for num, vout in enumerate(self.jdata["vout"]):
            if vout["type"] in ["frequency"]:
                pinlist_out.append((f"VOUT{num}_FREQUENCY", vout["pin"], "OUTPUT"))
        return pinlist_out

    def vouts(self):
        vouts_out = 0
        for _num, vout in enumerate(self.jdata["vout"]):
            if vout["type"] in ["frequency"]:
                vouts_out += 1
        return vouts_out

    def funcs(self):
        func_out = ["    // vout_frequency's"]
        for num, vout in enumerate(self.jdata["vout"]):
            if vout["type"] in ["frequency"]:
                freq = int(vout.get("frequency", 10000))
                divider = int(self.jdata["clock"]["speed"]) // freq
                func_out.append(f"    vout_frequency vout_frequency{num} (")
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .frequency (setPoint{num}),")
                func_out.append(f"        .disabled (ERROR),")
                func_out.append(f"        .SIGNAL (VOUT{num}_FREQUENCY),")
                func_out.append("    );")

        return func_out

    def ips(self):
        files = ["vout_frequency.v"]
        return files
