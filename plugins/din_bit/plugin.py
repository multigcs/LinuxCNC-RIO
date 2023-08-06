class Plugin:
    ptype = "din_bit"

    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "din",
                "subtype": self.ptype,
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
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name") or f"DIN.{num}"
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                pullup = data.get("pullup", False)
                ret.append((nameIntern, data["pin"], "INPUT", pullup))
        return ret

    def dinnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name") or f"DIN.{num}"
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data)
        return ret
