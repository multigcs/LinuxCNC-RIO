class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vout",
                "subtype": "frequency",
                "comment": "generates a variable frequency on the output pin",
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

    def voutnames(self):
        ret = []
        for num, vout in enumerate(self.jdata.get("vout", [])):
            if vout.get("type") == "frequency":
                name = vout.get("name", f"SP.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                ret.append((nameIntern, name, vout))
        return ret

    def funcs(self):
        func_out = ["    // vout_frequency's"]
        for num, vout in enumerate(self.jdata["vout"]):
            if vout["type"] in ["frequency"]:
                name = vout.get("name", f"SP.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                func_out.append(f"    vout_frequency vout_frequency{num} (")
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .frequency ({nameIntern}),")
                func_out.append(f"        .disabled (ERROR),")
                func_out.append(f"        .SIGNAL (VOUT{num}_FREQUENCY)")
                func_out.append("    );")

        return func_out

    def ips(self):
        for num, vout in enumerate(self.jdata["vout"]):
            if vout["type"] in ["frequency"]:
                return ["vout_frequency.v"]
        return []
