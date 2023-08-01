class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "din",
                "subtype": "",
                "comment": "normal binary input pin",
                "options": {
                    "name": {
                        "type": "str",
                        "name": "pin name",
                        "comment": "the name of the pin",
                        "default": '',
                    },
                    "net": {
                        "type": "dtarget",
                        "name": "net target",
                        "comment": "the target net of the pin in the hal",
                        "default": '',
                    },
                    "pin": {
                        "type": "input",
                        "name": "input pin",
                    },
                    "pullup": {
                        "type": "bool",
                        "name": "input pin",
                        "comment": "activates the internal pullup resistor for this pin",
                        "default": False,
                    },
                    "invert": {
                        "type": "bool",
                        "name": "invert pin",
                        "comment": "invert this pin",
                        "default": False,
                    },
                },
            },
        ]

    def pinlist(self):
        pinlist_out = []
        for num, din in enumerate(self.jdata["din"]):
            pullup = din.get("pullup", False)
            pinlist_out.append((f"DIN{num}", din["pin"], "INPUT", pullup))
        return pinlist_out

    def dins(self):
        dins_out = 0
        for _num, _din in enumerate(self.jdata["din"]):
            dins_out += 1
        return dins_out

    def dinnames(self):
        dins_out = []
        for num, _din in enumerate(self.jdata["din"]):
            dins_out.append((f"DIN{num}", f"DIN.{num}"))
        return dins_out
