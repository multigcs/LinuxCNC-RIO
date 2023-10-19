class Plugin:
    ptype = "picosoc"

    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "plugins",
                "subtype": self.ptype,
                "comment": "picosoc bridge",
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
                    "baud": {
                        "type": "int",
                        "name": "baud-rate",
                        "comment": "baud-rate",
                        "default": 9600,
                    },
                    "pins": {
                        "type": "dict",
                        "options": {
                            "rx": {
                                "type": "input",
                                "name": "rx pin",
                            },
                            "tx": {
                                "type": "output",
                                "name": "tx pin",
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
                    (f"PICOSOC{num}_RX", data["pins"]["rx"], "INOUT", pullup)
                )
                pinlist_out.append(
                    (f"PICOSOC{num}_TX", data["pins"]["tx"], "OUTPUT", pullup)
                )
                pinlist_out.append(
                    (f"PICOSOC{num}_FLASH_CLK", data["pins"]["flash_clk"], "OUTPUT", pullup)
                )
                pinlist_out.append(
                    (f"PICOSOC{num}_FLASH_CSB", data["pins"]["flash_csb"], "OUTPUT", pullup)
                )
                pinlist_out.append(
                    (f"PICOSOC{num}_FLASH_IO0", data["pins"]["flash_io0"], "INOUT", pullup)
                )
                pinlist_out.append(
                    (f"PICOSOC{num}_FLASH_IO1", data["pins"]["flash_io1"], "INOUT", pullup)
                )
                pinlist_out.append(
                    (f"PICOSOC{num}_FLASH_IO2", data["pins"]["flash_io2"], "INOUT", pullup)
                )
                pinlist_out.append(
                    (f"PICOSOC{num}_FLASH_IO3", data["pins"]["flash_io3"], "INOUT", pullup)
                )


        return pinlist_out

    def boutnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"PICOSOC.{num}") + "_OUT"
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["size"] = 72
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data.copy())
        return ret

    def binnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"PICOSOC.{num}") + "_IN"
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["size"] = 72
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data.copy())
        return ret

    def funcs(self):
        func_out = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name_out = data.get("name", f"PICOSOC.{num}") + "_OUT"
                nameIntern_out = name_out.replace(".", "").replace("-", "_").upper()
                name_in = data.get("name", f"PICOSOC.{num}") + "_IN"
                nameIntern_in = name_in.replace(".", "").replace("-", "_").upper()

                baud = data.get("baud", 9600)

                func_out.append(f"    picosoc_up5k picosoc{num} (")
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .ser_rx (PICOSOC{num}_RX),")
                func_out.append(f"        .ser_tx (PICOSOC{num}_TX),")
                func_out.append(f"        .flash_clk (PICOSOC{num}_FLASH_CLK),")
                func_out.append(f"        .flash_csb (PICOSOC{num}_FLASH_CSB),")
                func_out.append(f"        .flash_io0 (PICOSOC{num}_FLASH_IO0),")
                func_out.append(f"        .flash_io1 (PICOSOC{num}_FLASH_IO1),")
                func_out.append(f"        .flash_io2 (PICOSOC{num}_FLASH_IO2),")
                func_out.append(f"        .flash_io3 (PICOSOC{num}_FLASH_IO3)")

                func_out.append("    );")
        return func_out

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                return ["icebreaker.v", "ice40up5k_spram.v", "spimemio.v", "simpleuart.v", "picosoc.v", "picorv32.v"]
        return []
