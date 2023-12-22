class Plugin:
    ptype = "vin_max10adc"

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
                        "default": "",
                    },
                    "net": {
                        "type": "vtarget",
                        "name": "net target",
                        "comment": "the target net of the pin in the hal",
                        "default": "",
                    },
                    "pins": {
                        "type": "dict",
                        "options": {
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
        return pinlist_out

    def vinnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"ADC.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()

                names = data.get("names", data.get("name"))
                sensors = data.get("sensors", data.get("sensor"))
                functions = data.get("functions", data.get("function"))
                displays = data.get("displays", data.get("display"))
                scales = data.get("scales", data.get("scale"))
                offsets = data.get("offsets", data.get("offset"))

                for vnum in range(8):
                    data_copy = data.copy()
                    data_copy["_name"] = f"{name}.{vnum}"
                    data_copy["_prefix"] = f"{nameIntern}_{vnum}"
                    data_copy["_bits"] = 16
                    if isinstance(functions, list):
                        data_copy["function"] = functions[vnum]
                    if isinstance(sensors, list):
                        data_copy["sensor"] = sensors[vnum]
                    if isinstance(displays, list):
                        data_copy["display"] = displays[vnum]
                    if isinstance(scales, list):
                        data_copy["scale"] = scales[vnum]
                    if isinstance(offsets, list):
                        data_copy["offset"] = offsets[vnum]
                    if isinstance(names, list):
                        data_copy["name"] = names[vnum] or f"ADC.{num}.{vnum}"
                        data_copy["_prefix"] = (
                            data_copy["name"].replace(".", "").replace("-", "_").upper()
                        )
                    ret.append(data_copy)

        return ret

    def funcs(self):
        func_out = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"ADC.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                func_out.append(f"    vin_max10adc vin_max10adc{num} (")
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .adc0 ({nameIntern}_0),")
                func_out.append(f"        .adc1 ({nameIntern}_1),")
                func_out.append(f"        .adc2 ({nameIntern}_2),")
                func_out.append(f"        .adc3 ({nameIntern}_3),")
                func_out.append(f"        .adc4 ({nameIntern}_4),")
                func_out.append(f"        .adc5 ({nameIntern}_5),")
                func_out.append(f"        .adc6 ({nameIntern}_6),")
                func_out.append(f"        .adc7 ({nameIntern}_7)")
                func_out.append("    );")
        return func_out

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                return ["vin_max10adc.v", "max10adc.v"]
        return []
