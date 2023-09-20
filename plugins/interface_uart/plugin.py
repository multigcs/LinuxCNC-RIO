class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def setup(self):
        return [
            {
                "basetype": "interface",
                "subtype": "uart",
                "comment": "uart interface for the communication with LinuxCNC",
                "options": {
                    "pins": {
                        "type": "dict",
                        "name": "pin config",
                        "options": {
                            "RX": {
                                "type": "input",
                                "name": "rx pin",
                            },
                            "TX": {
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
        for num, interface in enumerate(self.jdata.get("interface", [])):
            if interface["type"] == "uart":
                pinlist_out.append(
                    ("INTERFACE_UART_RX", interface["pins"]["RX"], "INPUT")
                )
                pinlist_out.append(
                    (
                        "INTERFACE_UART_TX",
                        interface["pins"]["TX"],
                        "OUTPUT",
                    )
                )
        return pinlist_out

    def funcs(self):
        func_out = []
        for num, interface in enumerate(self.jdata.get("interface", [])):
            if interface["type"] == "uart":
                baud = interface.get("baud", 1000000)
                func_out.append("    assign INTERFACE_TIMEOUT = 0;")
                func_out.append(
                    f"    interface_uart #(BUFFER_SIZE, 32'h74697277, 32'd{int(self.jdata['clock']['speed']) // 4}, {self.jdata['clock']['speed']}, {baud}) uart1 ("
                )
                func_out.append("        .clk (sysclk),")
                func_out.append("        .UART_RX (INTERFACE_UART_RX),")
                func_out.append("        .UART_TX (INTERFACE_UART_TX),")
                func_out.append("        .rx_data (rx_data),")
                func_out.append("        .tx_data (tx_data)")
                # func_out.append("        .pkg_timeout (INTERFACE_TIMEOUT)")
                func_out.append("    );")
        return func_out

    def ips(self):
        for num, interface in enumerate(self.jdata.get("interface", [])):
            if interface["type"] == "uart":
                return ["uart_baud.v", "uart_rx.v", "uart_tx.v", "interface_uart.v"]
        return []
