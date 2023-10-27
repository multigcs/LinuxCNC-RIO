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
                if "flash_io2" in data["pins"] and "flash_io3" in data["pins"]:
                    pinlist_out.append(
                        (f"PICOSOC{num}_FLASH_IO2", data["pins"]["flash_io2"], "INOUT", pullup)
                    )
                    pinlist_out.append(
                        (f"PICOSOC{num}_FLASH_IO3", data["pins"]["flash_io3"], "INOUT", pullup)
                    )

                if "gpio" in data["pins"]:
                    for pn, pin in enumerate(data["pins"]["gpio"]):
                        pinlist_out.append(
                            (f"PICOSOC{num}_GPIO_{pn}", pin, "INOUT")
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

                baud = data.get("baud", 11520)

                mem = 1024  # 1kByte
                if self.jdata.get("type") == "up5k":
                    mem = 128 * 1024  # 128kByte
                mem_words = data.get("mem", mem) // 4

                prog_addr = data.get("prog_addr", "32'h00100000")
                if self.jdata.get("type") == "xc7a35ticsg324-1l":
                    prog_addr = data.get("prog_addr", "32'h00400000")
                prog_addr = prog_addr.replace("0x", "32'h")


                if "gpio" in data["pins"]:
                    """
                    gpios = []
                    gpio_len = len(data['pins']['gpio'])
                    if gpio_len < 32:
                        gpios.append(f"{32 - gpio_len}'d0")
                    for pn, pin in enumerate(data["pins"]["gpio"]):
                        gpios.append(f"PICOSOC{num}_GPIO_{pn}")
                    func_out.append(f"    reg [31:0] PICOSOC{num}_GPIO = {{{', '.join(gpios)}}};")
                    """

                    func_out.append(f"    wire [31:0] PICOSOC{num}_GPIO;")
                    for pn, pin in enumerate(data["pins"]["gpio"]):
                        func_out.append(f"    assign PICOSOC{num}_GPIO_{pn} = PICOSOC{num}_GPIO[{pn}];")

                func_out.append(f"    picosoc_plugin #({mem_words}, {prog_addr}) picosoc_plugin{num} (")
                func_out.append("        .clk (sysclk),")
                func_out.append(f"        .ser_rx (PICOSOC{num}_RX),")
                func_out.append(f"        .ser_tx (PICOSOC{num}_TX),")
                if "gpio" in data["pins"]:
                    func_out.append(f"        .gpio (PICOSOC{num}_GPIO),")
                func_out.append(f"        .flash_clk (PICOSOC{num}_FLASH_CLK),")
                func_out.append(f"        .flash_csb (PICOSOC{num}_FLASH_CSB),")
                if "flash_io2" in data["pins"] and "flash_io3" in data["pins"]:
                    func_out.append(f"        .flash_io2 (PICOSOC{num}_FLASH_IO2),")
                    func_out.append(f"        .flash_io3 (PICOSOC{num}_FLASH_IO3),")
                func_out.append(f"        .flash_io0 (PICOSOC{num}_FLASH_IO0),")
                func_out.append(f"        .flash_io1 (PICOSOC{num}_FLASH_IO1)")
                func_out.append("    );")
        return func_out

    def ips(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                ret = ["firmware.c", "sections.lds", "start.s", "picosoc_plugin.v", "spimemio.v", "simpleuart.v", "picosoc.v", "picorv32.v", "peripheral_gpio.v", "peripheral_counter.v", "peripheral_sysclock.v", "peripheral.v"]
                if self.jdata.get("type") == "up5k":
                    ret.append("ice40up5k_spram.v")
                return ret
        return []

    def ipdefs(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                ret = {}

                fpga_speed = int(self.jdata.get("clock", {}).get("speed", 12000000))
                ret.update({
                    "PICOSOC_CLOCK": str(fpga_speed),
                    "PICOSOC_CLOCK_HALF": str(fpga_speed // 2),
                })

                if "flash_io2" not in data["pins"] or "flash_io3" not in data["pins"]:
                    ret.update({
                        "PICOSOC_NO_QUADFLASH": "1",
                    })

                if self.jdata.get("type") == "xc7a35ticsg324-1l":
                    ret.update({
                        "PICOSOC_REGS_DISTRIBUTED": "1",
                        "PICOSOC_MEM_DISTRIBUTED": "1",
                    })
                elif self.jdata.get("type") == "up5k":
                    ret.update({
                        "PICOSOC_MEM": "ice40up5k_spram",
                        "PICOSOC_SB_IO": "1",
                    })
                return ret
        return {}

    def firmware_extrafiles(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                mem = 1024  # 1kByte
                if self.jdata.get("type") == "up5k":
                    mem = 128 * 1024  # 128kByte
                mem_total = data.get("mem", mem)

                baud = data.get("baud", 11520)
                fpga_speed = int(self.jdata.get("clock", {}).get("speed", 12000000))
                uart_clock_div = fpga_speed // baud

                prog_addr = data.get("prog_addr", "0x00100000")
                if self.jdata.get("type") == "xc7a35ticsg324-1l":
                    prog_addr = data.get("prog_addr", "0x00400000")
                prog_addr = prog_addr.replace("32'h", "0x")

                makefile = []
                makefile.append("")
                makefile.append(f"CFLAGS=-DMEM_TOTAL=0x{mem_total:x} -DUART_CLOCK_DIV={uart_clock_div} -DPROGADDR={prog_addr}")
                makefile.append("CROSS=riscv32-unknown-elf-")
                makefile.append("")
                makefile.append("all: firmware.bin")
                makefile.append("")
                makefile.append("clean:")
                makefile.append("	rm -rf firmware.bin firmware.elf firmware.lds")
                makefile.append("")
                makefile.append("firmware.lds: sections.lds")
                makefile.append("	$(CROSS)cpp -P $(CFLAGS) -o firmware.lds sections.lds")
                makefile.append("")
                makefile.append("firmware.elf: firmware.lds start.s firmware.c ")
                makefile.append("	$(CROSS)gcc $(CFLAGS) -mabi=ilp32 -march=rv32ic -Wl,-Bstatic,-T,firmware.lds,--strip-debug -ffreestanding -nostdlib -I. -o firmware.elf start.s firmware.c")
                makefile.append("")
                makefile.append("firmware.bin: firmware.elf")
                makefile.append("	$(CROSS)objcopy -O binary firmware.elf firmware.bin")
                makefile.append("")
                makefile.append("firmware.hex: firmware.elf")
                makefile.append("	$(CROSS)objcopy -O verilog firmware.elf firmware.hex")
                makefile.append("")
                makefile.append("load: firmware.bin")
                if self.jdata.get("type") == "xc7a35ticsg324-1l":
                    makefile.append(f"	openFPGALoader -b arty -o {int(prog_addr, 16)} -f firmware.bin")
                else:
                    makefile.append(f"	openFPGALoader -b ice40_generic -o {int(prog_addr, 16)} -f firmware.bin")
                makefile.append("	#minicom -D /dev/ttyUSB1 -b 115200")
                makefile.append("")


                peripheral = []
                peripheral.append("")
                peripheral.append("module peripheral (")
                peripheral.append("        input resetn,")
                peripheral.append("        input clk,")
                peripheral.append("        input iomem_valid,")
                peripheral.append("        input [3:0]  iomem_wstrb,")
                peripheral.append("        input [31:0] iomem_addr,")
                peripheral.append("        output [31:0] iomem_rdata,")
                peripheral.append("        output iomem_ready,")
                peripheral.append("        input [31:0] iomem_wdata,")
                peripheral.append("        output [31:0] gpio")
                peripheral.append("    );")
                peripheral.append("")

                peripherals = {"gpio": "gpio", "counter": "", "sysclock": ""}

                paddr = 3;
                for name, pins in peripherals.items():
                    peripheral.append(f"    // {name.upper()} mapped to 0x0{paddr}xx_xxxx")
                    peripheral.append(f"    wire {name}_en = (iomem_addr[31:24] == 8'h{paddr});")
                    peripheral.append(f"    wire [31:0] {name}_iomem_rdata;")
                    peripheral.append(f"    wire {name}_iomem_ready;")
                    peripheral.append(f"    peripheral_{name} {name}1 (")
                    peripheral.append("        .clk(clk),")
                    peripheral.append("        .resetn(resetn),")
                    peripheral.append(f"        .iomem_ready({name}_iomem_ready),")
                    peripheral.append(f"        .iomem_rdata({name}_iomem_rdata),")
                    peripheral.append(f"        .iomem_valid(iomem_valid && {name}_en),")
                    if pins:
                        peripheral.append(f"        .{pins}({pins}),")
                    peripheral.append("        .iomem_wstrb(iomem_wstrb),")
                    peripheral.append("        .iomem_addr(iomem_addr),")
                    peripheral.append("        .iomem_wdata(iomem_wdata)")
                    peripheral.append("    );")
                    peripheral.append("")
                    paddr += 1


                iomem_ready = "    assign iomem_ready = "
                iomem_rdata = "    assign iomem_rdata = "
                for name, pins in peripherals.items():
                    iomem_ready += f"{name}_en ? {name}_iomem_ready : "
                    iomem_rdata += f"{name}_iomem_ready ? {name}_iomem_rdata : "
                iomem_ready += "1'b0;"
                iomem_rdata += "32'h0;"
                peripheral.append(iomem_ready)
                peripheral.append(iomem_rdata)
                peripheral.append("")
                peripheral.append("endmodule")

                registers = []
                registers.append("")
                registers.append("#define reg_spictrl (*(volatile uint32_t*)0x02000000)")
                registers.append("#define reg_uart_clkdiv (*(volatile uint32_t*)0x02000004)")
                registers.append("#define reg_uart_data (*(volatile uint32_t*)0x02000008)")
                registers.append("")
                paddr = 3;
                for name, pins in peripherals.items():
                    registers.append(f"#define reg_{name} (*(volatile uint32_t*)0x{paddr}000000)")
                    paddr += 1
                registers.append("")
                registers.append("")

                return {
                    f"Makefile.{self.ptype}": "\n".join(makefile),
                    f"peripheral.v": "\n".join(peripheral),
                    f"registers.h": "\n".join(registers),
                }



        return {}

