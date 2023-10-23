class Plugin:
    ptype = "modbus"

    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "plugins",
                "subtype": self.ptype,
                "comment": "modbus bridge",
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
                            "tx_enable": {
                                "type": "output",
                                "name": "tx enable pin",
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
                    (f"MODBUS{num}_RX", data["pins"]["rx"], "INOUT", pullup)
                )
                pinlist_out.append(
                    (f"MODBUS{num}_TX", data["pins"]["tx"], "OUTPUT", pullup)
                )
                pinlist_out.append(
                    (f"MODBUS{num}_TXEN", data["pins"]["tx_enable"], "OUTPUT", pullup)
                )
        return pinlist_out

    def boutnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"MODBUS.{num}") + "_OUT"
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["size"] = 72
                data["_name"] = name
                data["_prefix"] = nameIntern
                data["inits"] = []
                data["callbacks"] = []
                for pnum, protocol in enumerate(data.get("protocols")):
                    ptype = protocol["type"]
                    addr = protocol["addr"]
                    spindle = protocol["spindle"]
                    init = f"{self.ptype}_{ptype}_init(comp_id, prefix);"
                    callback = f"{self.ptype}_{ptype}_send_msg(txData.{data['_prefix']});"
                    if init not in data["inits"]:
                        data["inits"].append(init)
                    if callback not in data["callbacks"]:
                        data["callbacks"].append(callback)
                ret.append(data.copy())
        return ret

    def binnames(self):
        ret = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name = data.get("name", f"MODBUS.{num}") + "_IN"
                nameIntern = name.replace(".", "").replace("-", "_").upper()
                data["size"] = 72
                data["_name"] = name
                data["_prefix"] = nameIntern
                data["callbacks"] = []

                for pnum, protocol in enumerate(data.get("protocols")):
                    ptype = protocol["type"]
                    addr = protocol["addr"]
                    spindle = protocol["spindle"]
                    callback = f"{self.ptype}_{ptype}_rec_msg(rxData.{data['_prefix']});"
                    if callback not in data["callbacks"]:
                        data["callbacks"].append(callback)

                ret.append(data.copy())

        return ret

    def funcs(self):
        func_out = []
        for num, data in enumerate(self.jdata["plugins"]):
            if data.get("type") == self.ptype:
                name_out = data.get("name", f"MODBUS.{num}") + "_OUT"
                nameIntern_out = name_out.replace(".", "").replace("-", "_").upper()
                name_in = data.get("name", f"MODBUS.{num}") + "_IN"
                nameIntern_in = name_in.replace(".", "").replace("-", "_").upper()

                baud = data.get("baud", 9600)

                func_out.append(f"    modbus #({self.jdata['clock']['speed']}, {baud}) modbus{num} (")
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .rx (MODBUS{num}_RX),")
                func_out.append(f"        .tx (MODBUS{num}_TX),")
                func_out.append(f"        .tx_en (MODBUS{num}_TXEN),")
                func_out.append(f"        .data_in ({nameIntern_in}),")
                func_out.append(f"        .data_out ({nameIntern_out})")
                func_out.append("    );")
        return func_out

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                return ["uart_baud.v", "uart_rx.v", "uart_tx.v", "modbus.v"]
        return []

    def components(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                cfiles = []
                for pnum, protocol in enumerate(data.get("protocols")):
                    source = f"{protocol['type']}.h"
                    header = f"{protocol['type']}.c"
                    if source not in cfiles:
                        cfiles.append(source)
                    if header not in cfiles:
                        cfiles.append(header)
                return cfiles
        return []
