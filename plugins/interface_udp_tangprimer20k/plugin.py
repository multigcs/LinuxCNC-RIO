class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "interface",
                "subtype": "udp_tangprimer20k",
                "comment": "udp_tangprimer20k interface for the communication with LinuxCNC",
                "options": {
                    "pins": {
                        "type": "dict",
                        "name": "pin config",
                        "options": {
                            "XXXX": {
                                "type": "input",
                                "name": "rx pin",
                            },
                        },
                    },
                },
            }
        ]


    def pinlist(self):
        pinlist_out = []
        for num, interface in enumerate(self.jdata.get("interface", [])):
            if interface["type"] == "udp_tangprimer20k":
                pins = interface["pins"]
                pinlist_out.append(("phyrst", pins["phyrst"], "OUTPUT"))
                pinlist_out.append(("netrmii_txd_1", pins["netrmii_txd_1"], "OUTPUT"))
                pinlist_out.append(("netrmii_txd_0", pins["netrmii_txd_0"], "OUTPUT"))
                pinlist_out.append(("netrmii_txen", pins["netrmii_txen"], "OUTPUT"))
                pinlist_out.append(("netrmii_mdc", pins["netrmii_mdc"], "OUTPUT"))
                pinlist_out.append(("netrmii_rxd_1", pins["netrmii_rxd_1"], "INPUT"))
                pinlist_out.append(("netrmii_rxd_0", pins["netrmii_rxd_0"], "INPUT"))
                pinlist_out.append(("netrmii_rx_crs", pins["netrmii_rx_crs"], "INPUT"))
                pinlist_out.append(("netrmii_clk50m", pins["netrmii_clk50m"], "INPUT"))
                pinlist_out.append(("netrmii_mdio", pins["netrmii_mdio"], "INOUT"))
        return pinlist_out

    def funcs(self):
        func_out = []
        for num, interface in enumerate(self.jdata.get("interface", [])):
            if interface["type"] == "udp_tangprimer20k":
                MAC_STR = interface.get("mac", "06:00:AA:BB:0C:DD")
                MAC = ",".join([f"8'h{part}" for part in MAC_STR.split(":")])
                IP_STR = interface.get("ip", "192.168.10.14")
                IP = ",".join([f"8'd{part}" for part in IP_STR.split(".")])

                func_out.append("    assign INTERFACE_TIMEOUT = 0;")
                func_out.append(
                    f"    interface_udp_tangprimer20k #(BUFFER_SIZE, 32'h74697277, {{{MAC}}}, {{{IP}}}) udp1 ("
                )
                func_out.append("        .sysclk (sysclk),")
                func_out.append("        .rx_data (rx_data),")
                func_out.append("        .tx_data (tx_data),")
                func_out.append("        .phyrst (phyrst),")
                func_out.append("        .netrmii_clk50m (netrmii_clk50m),")
                func_out.append("        .netrmii_rx_crs (netrmii_rx_crs),")
                func_out.append("        .netrmii_mdc (netrmii_mdc),")
                func_out.append("        .netrmii_txen (netrmii_txen),")
                func_out.append("        .netrmii_mdio (netrmii_mdio),")
                func_out.append("        .netrmii_txd_0 (netrmii_txd_0),")
                func_out.append("        .netrmii_txd_1 (netrmii_txd_1),")
                func_out.append("        .netrmii_rxd_0 (netrmii_rxd_0),")
                func_out.append("        .netrmii_rxd_1 (netrmii_rxd_1)")
                func_out.append("    );")
        return func_out

    def ips(self):
        for num, interface in enumerate(self.jdata.get("interface", [])):
            if interface["type"] == "udp_tangprimer20k":
                return ["PLL_6M.v", "udp.v", "interface_udp_tangprimer20k.v", "interface_udp_tangprimer20k.sdc"]
        return []
