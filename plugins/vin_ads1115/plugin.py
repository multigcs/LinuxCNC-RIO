class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vin",
                "subtype": "ads1115",
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
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "ads1115":
                pullup = vin.get("pullup", True)
                pinlist_out.append(
                    (f"VIN{num}_SDA", vin["pins"]["sda"], "INOUT", pullup)
                )
                pinlist_out.append(
                    (f"VIN{num}_SCL", vin["pins"]["scl"], "OUTPUT", pullup)
                )
        return pinlist_out


    def vinnames(self):
        ret = []
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "ads1115":
                name = vin.get("name", f"PV.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                function = vin.get("function")
                if isinstance(function, list):
                    vin["function"] = function[0]
                ret.append((f"{nameIntern}_0", f"{name}.0", vin.copy()))

                if isinstance(function, list):
                    vin["function"] = function[1]
                ret.append((f"{nameIntern}_1", f"{name}.1", vin.copy()))

                if isinstance(function, list):
                    vin["function"] = function[2]
                ret.append((f"{nameIntern}_2", f"{name}.2", vin.copy()))

                if isinstance(function, list):
                    vin["function"] = function[3]
                ret.append((f"{nameIntern}_3", f"{name}.3", vin.copy()))
        return ret

    def funcs(self):
        func_out = ["    // vin_ads1115's"]
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "ads1115":
                name = vin.get("name", f"PV.{num}")
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
        for num, vin in enumerate(self.jdata["vin"]):
            if vin["type"] in ["ads1115"]:
                return ["vin_ads1115.v"]
        return []
