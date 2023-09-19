class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "interface",
                "subtype": "spi",
                "comment": "spi slave interface for the communication with LinuxCNC",
                "options": {
                    "pins": {
                        "type": "dict",
                        "name": "pin config",
                        "options": {
                            "MOSI": {
                                "type": "input",
                                "name": "mosi pin",
                            },
                            "MISO": {
                                "type": "output",
                                "name": "miso pin",
                            },
                            "SCK": {
                                "type": "input",
                                "name": "clock pin",
                            },
                            "SEL": {
                                "type": "input",
                                "name": "selectionpin",
                                "comment": "do not use the spi-flash pin !!!",
                            },
                        },
                    },
                },
            }
        ]

    def pinlist(self):
        pinlist_out = []
        for num, interface in enumerate(self.jdata.get("interface", [])):
            if interface["type"] == "spi":
                pinlist_out.append(
                    ("INTERFACE_SPI_MOSI", interface["pins"]["MOSI"], "INPUT")
                )
                pinlist_out.append(
                    (
                        "INTERFACE_SPI_MISO",
                        interface["pins"]["MISO"],
                        "OUTPUT",
                    )
                )
                pinlist_out.append(
                    ("INTERFACE_SPI_SCK", interface["pins"]["SCK"], "INPUT")
                )
                pinlist_out.append(
                    ("INTERFACE_SPI_SSEL", interface["pins"]["SEL"], "INPUT")
                )
        return pinlist_out

    def funcs(self):
        func_out = []
        for num, interface in enumerate(self.jdata.get("interface", [])):
            if interface["type"] == "spi":
                func_out.append(
                    f"    interface_spislave #(BUFFER_SIZE, 32'h74697277, 32'd{int(self.jdata['clock']['speed']) // 4}) spi1 ("
                )
                func_out.append("        .clk (sysclk),")
                func_out.append("        .SPI_SCK (INTERFACE_SPI_SCK),")
                func_out.append("        .SPI_SSEL (INTERFACE_SPI_SSEL),")
                func_out.append("        .SPI_MOSI (INTERFACE_SPI_MOSI),")
                func_out.append("        .SPI_MISO (INTERFACE_SPI_MISO),")
                func_out.append("        .rx_data (rx_data),")
                func_out.append("        .tx_data (tx_data),")
                func_out.append("        .pkg_timeout (INTERFACE_TIMEOUT)")
                func_out.append("    );")
        return func_out

    def ips(self):
        for num, interface in enumerate(self.jdata.get("interface", [])):
            if interface["type"] == "spi":
                return ["interface_spislave.v"]
        return []
