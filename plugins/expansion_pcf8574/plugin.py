class Plugin:
    ptype = "pcf8574"

    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "expansion",
                "subtype": self.ptype,
                "comment": "to expand the number of IO's using pcf8574 via I2C",
                "options": {
                    "pins": {
                        "type": "dict",
                        "name": "pin config",
                        "options": {
                            "address": {
                                "type": "number",
                                "name": "address of the first device",
                                "default": "8'h40",
                            },
                            "devices": {
                                "type": "number",
                                "name": "number of devices",
                                "default": 1,
                            },
                            "sda": {
                                "type": "inout",
                                "name": "inout pin SDA",
                            },
                            "scl": {
                                "type": "output",
                                "name": "output pin SCL",
                            },
                        },
                    },
                },
            }
        ]

    def pinlist(self):
        pinlist_out = []
        for num, expansion in enumerate(self.jdata.get("expansion", [])):
            if expansion["type"] == self.ptype:
                pullup = expansion.get("pullup", True)
                pinlist_out.append(
                    (
                        f"EXPANSION{num}_PCF8574_SDA",
                        expansion["pins"]["sda"],
                        "INOUT",
                        pullup,
                    )
                )
                pinlist_out.append(
                    (
                        f"EXPANSION{num}_PCF8574_SCL",
                        expansion["pins"]["scl"],
                        "OUTPUT",
                        pullup,
                    )
                )
        return pinlist_out

    def expansions(self):
        expansions = {}
        for num, expansion in enumerate(self.jdata.get("expansion", [])):
            if expansion["type"] == self.ptype:
                devices = expansion.get("devices", 1)
                bits = devices * 8
                expansions[f"EXPANSION{num}_OUTPUT"] = bits
                expansions[f"EXPANSION{num}_INPUT"] = bits
        return expansions

    def defs(self):
        func_out = []
        for num, expansion in enumerate(self.jdata.get("expansion", [])):
            if expansion["type"] == self.ptype:
                devices = expansion.get("devices", 1)
                bits = devices * 8
                func_out.append(f"    wire [{bits - 1}:0] EXPANSION{num}_INPUT;")
                func_out.append(f"    wire [{bits - 1}:0] EXPANSION{num}_OUTPUT;")
        return func_out

    def funcs(self):
        func_out = []
        for num, expansion in enumerate(self.jdata.get("expansion", [])):
            if expansion["type"] == self.ptype:
                address = expansion.get("address", "8'h40")
                devices = expansion.get("devices", 1)
                func_out.append(
                    f"    expansion_pcf8574 #({address}, {devices}) expansion_pcf8574{num} ("
                )
                func_out.append("       .clk (sysclk),")
                func_out.append(f"       .i2cSda (EXPANSION{num}_PCF8574_SDA),")
                func_out.append(f"       .i2cScl (EXPANSION{num}_PCF8574_SCL),")
                func_out.append(f"       .data_in (EXPANSION{num}_INPUT),")
                func_out.append(f"       .data_out (EXPANSION{num}_OUTPUT)")
                func_out.append("    );")
        return func_out

    def ips(self):
        for num, expansion in enumerate(self.jdata.get("expansion", [])):
            if expansion["type"] in [self.ptype]:
                return ["expansion_pcf8574.v"]
        return []
