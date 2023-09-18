class Plugin:
    ptype = "dout_bit"

    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "dout",
                "subtype": self.ptype,
                "comment": "Digital Output",
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
                name = data.get("name", f"DOUT.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                ret.append((nameIntern, data["pin"], "OUTPUT"))
        return ret

    def doutnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"DOUT.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data)
        return ret
