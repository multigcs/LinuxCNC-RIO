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
                    "pins": {
                        "type": "dict",
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

    def vins(self):
        vins_out = 0
        for _num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "ads1115":
                vins_out += 4
                vin['vars'] = 4
        return vins_out

    def vdata(self):
        vdata = []
        for _num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "ads1115":
                function = vin.get("function")
                if isinstance(function, list):
                    vin["function"] = function[0]
                vdata.append(vin.copy())
                if isinstance(function, list):
                    vin["function"] = function[1]
                vdata.append(vin.copy())
                if isinstance(function, list):
                    vin["function"] = function[2]
                vdata.append(vin.copy())
                if isinstance(function, list):
                    vin["function"] = function[3]
                vdata.append(vin.copy())
        return vdata

    def funcs(self):
        func_out = ["    // vin_ads1115's"]
        vin_num = 0
        for num, vin in enumerate(self.jdata.get("vin", [])):
            if vin.get("type") == "ads1115":
                func_out.append(f"    vin_ads1115 vin_ads1115{num} (")
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .i2cSda (VIN{num}_SDA),")
                func_out.append(f"        .i2cScl (VIN{num}_SCL),")
                func_out.append(f"        .adc0 (processVariable{vin_num}),")
                func_out.append(f"        .adc1 (processVariable{vin_num + 1}),")
                func_out.append(f"        .adc2 (processVariable{vin_num + 2}),")
                func_out.append(f"        .adc3 (processVariable{vin_num + 3})")
                func_out.append("    );")

            vin_num += vin.get("vars", 1)


        return func_out

    def ips(self):
        for num, vin in enumerate(self.jdata["vin"]):
            if vin["type"] in ["ads1115"]:
                return ["vin_ads1115.v"]
        return []
