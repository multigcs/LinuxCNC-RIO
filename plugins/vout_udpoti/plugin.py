class Plugin:
    ptype = "vout_udpoti"

    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vout",
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
                        "comment": "the target net of the pin in the hal",
                        "default": "",
                    },
                    "resolution": {
                        "type": "int",
                        "name": "resolution",
                        "default": "100",
                        "comment": "number of steps / resolution of the poti",
                    },
                    "speed": {
                        "type": "int",
                        "name": "speed",
                        "default": "100000",
                        "comment": "the clock speed in Hz",
                    },
                    "pins": {
                        "type": "dict",
                        "name": "pin config",
                        "options": {
                            "updown": {
                                "type": "output",
                                "name": "updown pin",
                                "comment": "this pin set the direction for increment (UP/Down)",
                            },
                            "incr": {
                                "type": "output",
                                "name": "increment pin",
                            },
                        },
                    },
                },
            }
        ]

    def pinlist(self):
        pinlist_out = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                pinlist_out.append(
                    (f"VOUT{num}_UDPOTI_UPDOWN", data["pins"]["updown"], "OUTPUT")
                )
                pinlist_out.append(
                    (f"VOUT{num}_UDPOTI_INCR", data["pins"]["incr"], "OUTPUT")
                )
        return pinlist_out

    def voutnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"SP.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data)
        return ret

    def funcs(self):
        func_out = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] in self.ptype:
                name = data.get("name", f"SP.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                resolution = int(data.get("resolution", 100))
                speed = int(data.get("speed", 100000))
                divider = int(self.jdata["clock"]["speed"]) // speed
                func_out.append(
                    f"    vout_udpoti #({resolution}, {divider}) vout_udpoti{num} ("
                )
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .value ({nameIntern}),")
                func_out.append(f"        .UPDOWN (VOUT{num}_UDPOTI_UPDOWN),")
                func_out.append(f"        .INCREMENT (VOUT{num}_UDPOTI_INCR)")
                func_out.append("    );")

        return func_out

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] in self.ptype:
                return ["vout_udpoti.v"]
        return []
