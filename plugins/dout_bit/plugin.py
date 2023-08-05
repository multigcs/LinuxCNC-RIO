class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "dout",
                "subtype": "",
                "comment": "Digital Output",
                "options": {
                    "name": {
                        "type": "str",
                        "name": "pin name",
                        "comment": "the name of the pin",
                        "default": '',
                    },
                    "net": {
                        "type": "dsource",
                        "name": "net source",
                        "comment": "the source net of the pin in the hal",
                        "default": '',
                    },
                    "pin": {
                        "type": "output",
                        "name": "output pin",
                    },
                },
            }
        ]

    def pinlist(self):
        pinlist_out = []
        for num, dout in enumerate(self.jdata["dout"]):
            name = dout.get("name", f"DOUT.{num}")
            nameIntern = name.replace(".", "").replace("-", "_").upper()
            pinlist_out.append((nameIntern, dout["pin"], "OUTPUT"))
        return pinlist_out

    def doutnames(self):
        douts_out = []
        for num, dout in enumerate(self.jdata["dout"]):
            name = dout.get("name", f"DOUT.{num}")
            nameIntern = name.replace(".", "").replace("-", "_").upper()
            douts_out.append((nameIntern, name, dout))
        return douts_out
