class Plugin:
    ptype = "vout_wled"
    ptype2 = "dout_wled"

    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vout",
                "subtype": self.ptype,
                "comment": "Digital Output to ws2812b",
                "options": {
                    "name": {
                        "type": "str",
                        "name": "pin name",
                        "comment": "the name of the pin",
                        "default": "",
                    },
                    "net": {
                        "type": "dsource",
                        "name": "net source",
                        "comment": "the source net of the pin in the hal",
                        "default": "",
                    },
                    "pin": {
                        "type": "output",
                        "name": "output pin",
                    },
                },
            },
            {
                "basetype": "dout",
                "subtype": self.ptype2,
                "comment": "Digital Output to ws2812b",
                "options": {
                    "name": {
                        "type": "str",
                        "name": "pin name",
                        "comment": "the name of the pin",
                        "default": "",
                    },
                    "net": {
                        "type": "dsource",
                        "name": "net source",
                        "comment": "the source net of the pin in the hal",
                        "default": "",
                    },
                    "pin": {
                        "type": "output",
                        "name": "output pin",
                    },
                },
            }
        ]

    def pinlist(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"SP.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                ret.append(
                    (f"VOUT{num}", data["pin"], "OUTPUT")
                )
            elif data.get("type") == self.ptype2:
                name = data.get("name", f"DOUT.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                ret.append(
                    (f"DOUT{num}", data["pin"], "OUTPUT")
                )
        return ret

    def voutnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"SP.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data)
        return ret

    def doutnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype2:
                name = data.get("name", f"DOUT.{num}") + "_G"
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data.copy())
                name = data.get("name", f"DOUT.{num}") + "_B"
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data.copy())
                name = data.get("name", f"DOUT.{num}") + "_R"
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data.copy())
        return ret

    def funcs(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"SP.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                ret.append(f"    vout_wled #({int(self.jdata['clock']['speed']) // 1000000}) vout_wled{num} (")
                ret.append("        .clk (sysclk),")
                ret.append(f"        .value ({nameIntern}),")
                ret.append(f"        .wled (VOUT{num})")
                ret.append("    );")
            elif data.get("type") == self.ptype2:
                name = data.get("name", f"DOUT.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                ret.append(f"    dout_wled #({int(self.jdata['clock']['speed']) // 1000000}) dout_wled{num} (")
                ret.append("        .clk (sysclk),")
                ret.append(f"        .green ({nameIntern}_G),")
                ret.append(f"        .blue ({nameIntern}_B),")
                ret.append(f"        .red ({nameIntern}_R),")
                ret.append(f"        .wled (DOUT{num})")
                ret.append("    );")
        return ret

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                return ["ws2812.v", "vout_wled.v"]
            if data.get("type") == self.ptype2:
                return ["ws2812.v", "dout_wled.v"]
        return []

