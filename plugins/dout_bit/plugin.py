class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def pinlist(self):
        pinlist_out = []
        for num, dout in enumerate(self.jdata["dout"]):
            pinlist_out.append((f"DOUT{num}", dout["pin"], "OUTPUT"))
        return pinlist_out

    def douts(self):
        douts_out = 0
        for _num, _pwmout in enumerate(self.jdata["dout"]):
            douts_out += 1
        return douts_out
