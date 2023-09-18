class Plugin:
    ptype = "vfdbridge"

    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "plugins",
                "subtype": self.ptype,
                "comment": "Huanyang VFD Spindel Control",
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
                        "default": "spindle.0.speed-out",
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

    def defs(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"VFD.{num}") + "-at-speed"
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                ret.append(f"    wire {nameIntern};")
        return ret

    def dinnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"VFD.{num}") + "-at-speed"
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data)
        return ret

    def vinnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"VFD.{num}") + "-get-speed"
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data.copy())
        return ret

    def voutnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"VFD.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data.copy())
        return ret

    def funcs(self):
        func_out = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name_out = data.get("name", f"VFD.{num}")
                nameIntern_out = name_out.replace(".", "").replace("-", "_").upper()
                name_in = data.get("name", f"VFD.{num}") + "-get-speed"
                nameIntern_in = name_in.replace(".", "").replace("-", "_").upper()
                name_on = data.get("name", f"VFD.{num}") + "-at-speed"
                nameIntern_on = name_on.replace(".", "").replace("-", "_").upper()

                i2c_clock = 50000
                divider = int(self.jdata["clock"]["speed"]) // i2c_clock // 256 - 1

                func_out.append(f"    vfdbridge #({divider}) vfdbridge{num} (")
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .i2cSda (VIN{num}_SDA),")
                func_out.append(f"        .i2cScl (VIN{num}_SCL),")
                func_out.append(f"        .speed_feedback ({nameIntern_in}),")
                func_out.append(f"        .speed_set ({nameIntern_out}),")
                func_out.append(f"        .speed_at ({nameIntern_on})")
                func_out.append("    );")
        return func_out

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                return ["vfdbridge.v"]
        return []
