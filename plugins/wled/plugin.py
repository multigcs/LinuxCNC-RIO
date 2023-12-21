class Plugin:
    ptype = "vout_wled"
    ptype2 = "dout_wled"

    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "vout",
                "subtype": self.ptype,
                "comment": "Digital Output to ws2812b",
                "options": {
                    "name": {
                        "type": "str",
                        "name": "pin name",
                        "comment": "the name of the pin",
                        "default": "",
                    },
                    "net": {
                        "type": "dsource",
                        "name": "net source",
                        "comment": "the source net of the pin in the hal",
                        "default": "",
                    },
                    "pin": {
                        "type": "output",
                        "name": "output pin",
                    },
                },
            },
            {
                "basetype": "dout",
                "subtype": self.ptype2,
                "comment": "Digital Output to ws2812b",
                "options": {
                    "name": {
                        "type": "str",
                        "name": "pin name",
                        "comment": "the name of the pin",
                        "default": "",
                    },
                    "net": {
                        "type": "dsource",
                        "name": "net source",
                        "comment": "the source net of the pin in the hal",
                        "default": "",
                    },
                    "pin": {
                        "type": "output",
                        "name": "output pin",
                    },
                },
            },
        ]

    def pinlist(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                ret.append((f"VOUT{num}", data["pin"], "OUTPUT"))
            elif data.get("type") == self.ptype2:
                ret.append((f"WLED{num}", data["pin"], "OUTPUT"))
        return ret

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

    def doutnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype2:
                num_leds = int(data.get("leds", 1))
                net = data.get('net')
                if not isinstance(net, list):
                    net = [net]
                for led in range(num_leds):
                    netn = led * 3
                    name = data.get("name", f"WLED.{num}") + f".{led:02d}.G"
                    nameIntern = name.replace(".", "").replace("-", "_").upper()
                    if len(net) > netn:
                        data["net"] = net[netn]
                    else:
                        data["net"] = ""
                    data["_name"] = name
                    data["_prefix"] = nameIntern
                    ret.append(data.copy())
                    name = data.get("name", f"WLED.{num}") + f".{led:02d}.B"
                    nameIntern = name.replace(".", "").replace("-", "_").upper()
                    if len(net) > netn+1:
                        data["net"] = net[netn+1]
                    else:
                        data["net"] = ""
                    data["_name"] = name
                    data["_prefix"] = nameIntern
                    ret.append(data.copy())
                    name = data.get("name", f"WLED.{num}") + f".{led:02d}.R"
                    nameIntern = name.replace(".", "").replace("-", "_").upper()
                    if len(net) > netn+2:
                        data["net"] = net[netn+2]
                    else:
                        data["net"] = ""
                    data["_name"] = name
                    data["_prefix"] = nameIntern
                    ret.append(data.copy())
        return ret

    def defs(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype2:
                name = data.get("name", f"WLED.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                num_leds = int(data.get("leds", 1))
                for led in range(num_leds):
                    ret.append(f"    wire {nameIntern}{led:02d}G;")
                    ret.append(f"    wire {nameIntern}{led:02d}B;")
                    ret.append(f"    wire {nameIntern}{led:02d}R;")
        return ret

    def funcs(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"WLED.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                ret.append(
                    f"    vout_wled #({int(self.jdata['clock']['speed']) // 1000000}) vout_wled{num} ("
                )
                ret.append("        .clk (sysclk),")
                ret.append(f"        .value ({nameIntern}),")
                ret.append(f"        .wled (VOUT{num})")
                ret.append("    );")
            elif data.get("type") == self.ptype2:
                name = data.get("name", f"WLED.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                num_leds = int(data.get("leds", 1))

                ret.append(f"    wire [{num_leds-1}:0] {nameIntern}G;")
                ret.append(f"    wire [{num_leds-1}:0] {nameIntern}B;")
                ret.append(f"    wire [{num_leds-1}:0] {nameIntern}R;")
                for led in range(num_leds):
                    ret.append(f"    assign WLED{num}G[{led:d}] = {nameIntern}{led:02d}G;")
                    ret.append(f"    assign WLED{num}B[{led:d}] = {nameIntern}{led:02d}B;")
                    ret.append(f"    assign WLED{num}R[{led:d}] = {nameIntern}{led:02d}R;")

                ret.append(
                    f"    dout_wled #(.CLK_MHZ({int(self.jdata['clock']['speed']) // 1000000}), .NUM_LEDS({num_leds})) dout_wled{num} ("
                )
                ret.append("        .clk (sysclk),")
                ret.append(f"        .green ({nameIntern}G),")
                ret.append(f"        .blue ({nameIntern}B),")
                ret.append(f"        .red ({nameIntern}R),")
                ret.append(f"        .wled (WLED{num})")
                ret.append("    );")
        return ret

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                return ["ws2812.v", "vout_wled.v"]
            if data.get("type") == self.ptype2:
                return ["ws2812.v", "dout_wled.v"]
        return []
