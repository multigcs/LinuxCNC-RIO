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
            if din.get("type", "bit") == "bit":
                name = din.get("name", f"DIN.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                pullup = din.get("pullup", False)
                pinlist_out.append((nameIntern, din["pin"], "INPUT", pullup))
        return pinlist_out

    def dins_data(self):
        ddata = []
        for num, din in enumerate(self.jdata["din"]):
            if din.get("type", "bit") == "bit":
                ddata.append(din)
        return ddata

    def dinnames(self):
        dins_out = []
        for num, din in enumerate(self.jdata["din"]):
            if din.get("type", "bit") == "bit":
                name = din.get("name", f"DIN.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                dins_out.append((nameIntern, name, din))
        return dins_out
