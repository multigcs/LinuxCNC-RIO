class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vin",
                "subtype": "ds18b20",
                "comment": "to messure temperature via one wire interface",
                "options": {
                    "pins": {
                        "type": "dict",
                        "options": {
                            "onewire": {
                                "type": "inout",
                                "name": "one wire pin",
                            },
                        },
                    },
                },
            }
        ]


    def pinlist(self):
        pinlist_out = []
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "ds18b20":
                pullup = vin.get("pullup", False)
                pinlist_out.append((f"VIN{num}_DS18B20_ONEWIRE", vin["pins"]["onewire"], "INOUT", False))
        return pinlist_out

    def vins(self):
        vins_out = 0
        for _num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "ds18b20":
                vins_out += 1
        return vins_out

    def vdata(self):
        vdata = []
        for _num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "ds18b20":
                vdata.append(vin)
        return vdata

    def funcs(self):
        func_out = ["    // vin_ds18b20's"]
        vin_num = 0
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "ds18b20":
                osc = int(self.jdata['clock']['speed'])
                func_out.append(
                    f"    vin_ds18b20 #({osc // 50000}, {osc // 13}, {osc // 5}) vin_ds18b20{num} ("
                )
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .one_wire (VIN{num}_DS18B20_ONEWIRE),")
                func_out.append(f"        .temperature (processVariable{vin_num})")
                func_out.append("    );")
            vin_num += vin.get("vars", 1)
        return func_out

    def ips(self):
        for num, vin in enumerate(self.jdata["vin"]):
            if vin["type"] in ["ds18b20"]:
                return ["vin_ds18b20.v"]
        return []
