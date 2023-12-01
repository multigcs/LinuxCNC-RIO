class Plugin:
    ptype = "vout_7seg"

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
                        "comment": "the target net of the signal in the hal",
                        "default": "",
                    },
                    "pins": {
                        "type": "dict",
                        "options": {
                            "en1": {
                                "type": "output",
                                "name": "digit 1 enable output pin",
                            },
                            "en2": {
                                "type": "output",
                                "name": "digit 2 enable output pin",
                            },
                            "en3": {
                                "type": "output",
                                "name": "digit 3 enable output pin",
                            },
                            "en4": {
                                "type": "output",
                                "name": "digit 4 enable output pin",
                            },
                            "seg_a": {
                                "type": "output",
                                "name": "segment A output pin",
                            },
                            "seg_b": {
                                "type": "output",
                                "name": "segment B output pin",
                            },
                            "seg_c": {
                                "type": "output",
                                "name": "segment C output pin",
                            },
                            "seg_d": {
                                "type": "output",
                                "name": "segment D output pin",
                            },
                            "seg_e": {
                                "type": "output",
                                "name": "segment E output pin",
                            },
                            "seg_f": {
                                "type": "output",
                                "name": "segment F output pin",
                            },
                            "seg_g": {
                                "type": "output",
                                "name": "segment G output pin",
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
                pins = data["pins"]
                pinlist_out.append((f"VOUT{num}_7SEG_EN1", pins["en1"], "OUTPUT"))
                pinlist_out.append((f"VOUT{num}_7SEG_EN2", pins["en2"], "OUTPUT"))
                pinlist_out.append((f"VOUT{num}_7SEG_EN3", pins["en3"], "OUTPUT"))
                pinlist_out.append((f"VOUT{num}_7SEG_EN4", pins["en4"], "OUTPUT"))
                pinlist_out.append((f"VOUT{num}_7SEG_SEG_A", pins["seg_a"], "OUTPUT"))
                pinlist_out.append((f"VOUT{num}_7SEG_SEG_B", pins["seg_b"], "OUTPUT"))
                pinlist_out.append((f"VOUT{num}_7SEG_SEG_C", pins["seg_c"], "OUTPUT"))
                pinlist_out.append((f"VOUT{num}_7SEG_SEG_D", pins["seg_d"], "OUTPUT"))
                pinlist_out.append((f"VOUT{num}_7SEG_SEG_E", pins["seg_e"], "OUTPUT"))
                pinlist_out.append((f"VOUT{num}_7SEG_SEG_F", pins["seg_f"], "OUTPUT"))
                pinlist_out.append((f"VOUT{num}_7SEG_SEG_G", pins["seg_g"], "OUTPUT"))
        return pinlist_out

    def voutnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                name = data.get("name", f"SP.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["_name"] = name
                data["_prefix"] = nameIntern
                ret.append(data)
        return ret

    def funcs(self):
        func_out = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                name = data.get("name", f"SP.{num}")
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                func_out.append(f"    vout_7seg vout_7seg{num} (")
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .value ({nameIntern}),")
                func_out.append(f"        .en1 (VOUT{num}_7SEG_EN1),")
                func_out.append(f"        .en2 (VOUT{num}_7SEG_EN2),")
                func_out.append(f"        .en3 (VOUT{num}_7SEG_EN3),")
                func_out.append(f"        .en4 (VOUT{num}_7SEG_EN4),")
                func_out.append(f"        .displayA (VOUT{num}_7SEG_SEG_A),")
                func_out.append(f"        .displayB (VOUT{num}_7SEG_SEG_B),")
                func_out.append(f"        .displayC (VOUT{num}_7SEG_SEG_C),")
                func_out.append(f"        .displayD (VOUT{num}_7SEG_SEG_D),")
                func_out.append(f"        .displayE (VOUT{num}_7SEG_SEG_E),")
                func_out.append(f"        .displayF (VOUT{num}_7SEG_SEG_F),")
                func_out.append(f"        .displayG (VOUT{num}_7SEG_SEG_G)")
                func_out.append("    );")
        return func_out

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                return ["vout_7seg.v"]
        return []
