class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "dout",
                "subtype": "",
                "options": {
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
            pinlist_out.append((f"DOUT{num}", dout["pin"], "OUTPUT"))
        return pinlist_out

    def douts(self):
        douts_out = 0
        for _num, _dout in enumerate(self.jdata["dout"]):
            douts_out += 1
        return douts_out

    def doutnames(self):
        douts_out = []
        for num, _dout in enumerate(self.jdata["dout"]):
            douts_out.append((f"DOUT{num}", f"DOUT.{num}"))
        return douts_out
