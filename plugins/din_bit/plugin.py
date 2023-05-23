class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "din",
                "subtype": "",
                "options": {
                    "pin": {
                        "type": "input",
                        "name": "input pin",
                    },
                },
            },
            {
                "basetype": "din",
                "subtype": "home",
                "options": {
                    "pin": {
                        "type": "input",
                        "name": "input pin",
                    },
                },
            },
            {
                "basetype": "din",
                "subtype": "probe",
                "options": {
                    "pin": {
                        "type": "input",
                        "name": "input pin",
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
