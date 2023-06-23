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
                },
            },
            {
                "basetype": "din",
                "subtype": "home",
                "comment": "input pin used for home-switches",
                "options": {
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
                },
            },
            {
                "basetype": "din",
                "subtype": "probe",
                "comment": "input pin used for the probe-switche",
                "options": {
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
            dins_out.append(f"DIN{num}")
        return dins_out
