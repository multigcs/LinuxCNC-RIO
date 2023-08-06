class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vout",
                "subtype": "vout_frequency",
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
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] in ["vout_frequency"]:
                pinlist_out.append((f"VOUT{num}_FREQUENCY", data["pin"], "OUTPUT"))
        return pinlist_out

    def voutnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == "vout_frequency":
                name = data.get("name", f"SP.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data)
        return ret

    def funcs(self):
        func_out = ["    // vout_frequency's"]
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] in ["vout_frequency"]:
                name = data.get("name", f"SP.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                func_out.append(f"    vout_frequency vout_frequency{num} (")
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .frequency ({nameIntern}),")
                func_out.append(f"        .disabled (ERROR),")
                func_out.append(f"        .SIGNAL (VOUT{num}_FREQUENCY)")
                func_out.append("    );")

        return func_out

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] in ["vout_frequency"]:
                return ["vout_frequency.v"]
        return []
