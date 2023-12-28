class Plugin:
    ptype = "vin_ds18b20"

    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vin",
                "subtype": self.ptype,
                "options": {
                    "name": {
                        "type": "str",
                        "name": "pin name",
                        "comment": "the name of the pin",
                        "default": "",
                    },
                    "net": {
                        "type": "vtarget",
                        "name": "net target",
                        "comment": "the target net of the signal in the hal",
                        "default": "",
                    },
                    "pins": {
                        "type": "dict",
                        "options": {
                            "data": {
                                "type": "inout",
                                "name": "1Wire data pin",
                            },
                        },
                    },
                },
            }
        ]

    def calculation_vin(self, setup, value):
        unit = "°C"
        if (value << 8) & 0x80:
            value = ((value ^ 0xFFFF) + 1) * -1
        value = value / 16
        return (value, unit)

    def pinlist(self):
        pinlist_out = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                pins = data["pins"]
                pinlist_out.append((f"VIN{num}_DATA", pins["data"], "INOUT"))
        return pinlist_out

    def vinnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_bits"] = 16
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data)
        return ret

    def funcs(self):
        func_out = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                name = data.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()

                speed = int(self.jdata["clock"]["speed"]) // 1000000 // 2

                func_out.append(f"    vin_ds18b20 #({speed}) vin_ds18b20{num} (")
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .one_wire (VIN{num}_DATA),")
                func_out.append(f"        .temperature ({nameIntern})")
                func_out.append("    );")
        return func_out

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                return ["vin_ds18b20.v"]
        return []
