class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def pinlist(self):
        pinlist_out = []
        for num, din in enumerate(self.jdata["din"]):
            pullup = din.get("pullup", False)
            pinlist_out.append((f"DIN{num}", din["pin"], "INPUT", pullup))
        return pinlist_out

    def dins(self):
        dins_out = 0
        for _num, _pwmout in enumerate(self.jdata["din"]):
            dins_out += 1
        return dins_out
