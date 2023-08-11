class Plugin:
    ptype = "vin_ads1115"

    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vin",
                "subtype": self.ptype,
                "comment": "4Channel ADC",
                "options": {
                    "name": {
                        "type": "str",
                        "name": "pin name",
                        "comment": "the name of the pin",
                        "default": '',
                    },
                    "net": {
                        "type": "vtarget",
                        "name": "net target",
                        "comment": "the target net of the pin in the hal",
                        "default": '',
                    },
                    "pins": {
                        "type": "dict",
                        "options": {
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
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                pullup = data.get("pullup", True)
                pinlist_out.append(
                    (f"VIN{num}_SDA", data["pins"]["sda"], "INOUT", pullup)
                )
                pinlist_out.append(
                    (f"VIN{num}_SCL", data["pins"]["scl"], "OUTPUT", pullup)
                )
        return pinlist_out


    def vinnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()

                names = data.get("names")
                sensors = data.get("sensors")
                function = data.get("function")
                displays = data.get("displays")

                for vnum in range(4):
                    data["_name"] = f"{name}.{vnum}"
                    data["_prefix"] = f"{nameIntern}_{vnum}"
                    if isinstance(function, list):
                        data["function"] = function[vnum]
                    if isinstance(sensors, list):
                        data["sensor"] = sensors[vnum]
                    if isinstance(displays, list):
                        data["display"] = displays[vnum]
                    if isinstance(names, list):
                        data["name"] = names[vnum] or f"PV.{num}.{vnum}"
                        data["_prefix"] = data["name"].replace(".", "").replace("-", "_").upper()
                    ret.append(data.copy())

        return ret

    def funcs(self):
        func_out = ["    // vin_ads1115's"]
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                func_out.append(f"    vin_ads1115 vin_ads1115{num} (")
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .i2cSda (VIN{num}_SDA),")
                func_out.append(f"        .i2cScl (VIN{num}_SCL),")
                func_out.append(f"        .adc0 ({nameIntern}_0),")
                func_out.append(f"        .adc1 ({nameIntern}_1),")
                func_out.append(f"        .adc2 ({nameIntern}_2),")
                func_out.append(f"        .adc3 ({nameIntern}_3)")
                func_out.append("    );")
        return func_out

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                return ["vin_ads1115.v"]
        return []



