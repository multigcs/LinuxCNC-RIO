class Plugin:
    def __init__(self, jdata):
        self.jdata = jdata

    def pinlist(self):
        pinlist_out = []
        if self.jdata["interface"]["type"] == "spi":
            pinlist_out.append(
                ("INTERFACE_SPI_MOSI", self.jdata["interface"]["pins"]["MOSI"], "INPUT")
            )
            pinlist_out.append(
                (
                    "INTERFACE_SPI_MISO",
                    self.jdata["interface"]["pins"]["MISO"],
                    "OUTPUT",
                )
            )
            pinlist_out.append(
                ("INTERFACE_SPI_SCK", self.jdata["interface"]["pins"]["SCK"], "INPUT")
            )
            pinlist_out.append(
                ("INTERFACE_SPI_SSEL", self.jdata["interface"]["pins"]["SEL"], "INPUT")
            )
        return pinlist_out

    def funcs(self):
        func_out = ["    // interface_spislave"]
        func_out.append("    wire pkg_ok;")
        func_out.append(
            f"    interface_spislave #(BUFFER_SIZE, 32'h74697277, {self.jdata['clock']['speed']}) spi1 ("
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
        files = ["interface_spislave.v"]
        return files
