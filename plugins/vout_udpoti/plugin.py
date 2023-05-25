class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vout",
                "subtype": "udpoti",
                "options": {
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
        for num, vout in enumerate(self.jdata["vout"]):
            if vout["type"] in ["udpoti"]:
                pinlist_out.append((f"VOUT{num}_UDPOTI_UPDOWN", vout["pins"]["updown"], "OUTPUT"))
                pinlist_out.append((f"VOUT{num}_UDPOTI_INCR", vout["pins"]["incr"], "OUTPUT"))
        return pinlist_out

    def vouts(self):
        vouts_out = 0
        for _num, vout in enumerate(self.jdata["vout"]):
            if vout["type"] in ["udpoti"]:
                vouts_out += 1
        return vouts_out

    def funcs(self):
        func_out = ["    // vout_udpoti's"]
        for num, vout in enumerate(self.jdata["vout"]):
            if vout["type"] in ["udpoti"]:
                resolution = int(vout.get("resolution", 100))
                speed = int(vout.get("speed", 100000))
                divider = int(self.jdata["clock"]["speed"]) // speed
                func_out.append(f"    vout_udpoti #({resolution}, {divider}) vout_udpoti{num} (")
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .value (setPoint{num}),")
                func_out.append(f"        .UPDOWN (VOUT{num}_UDPOTI_UPDOWN),")
                func_out.append(f"        .INCREMENT (VOUT{num}_UDPOTI_INCR),")
                func_out.append("    );")

        return func_out

    def ips(self):
        for num, vout in enumerate(self.jdata["vout"]):
            if vout["type"] in ["udpoti"]:
                return ["vout_udpoti.v"]
        return []


