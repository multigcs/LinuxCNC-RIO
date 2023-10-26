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

                baud = data.get("baud", 11520)

                mem = 1024  # 1kByte
                if self.jdata.get("type") == "up5k":
                    mem = 128 * 1024  # 128kByte
                mem_words = data.get("mem", mem) // 4

                func_out.append(f"    picosoc_plugin #({mem_words}) picosoc_plugin{num} (")
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
                ret = ["Makefile.picosoc_plugin", "firmware.c", "sections.lds", "start.s", "picosoc_plugin.v", "spimemio.v", "simpleuart.v", "picosoc.v", "picorv32.v"]
                if self.jdata.get("type") == "up5k":
                    ret.append("ice40up5k_spram.v")
                return ret
        return []

    def ipdefs(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:
                if self.jdata.get("type") == "up5k":
                    return {
                        "PICOSOC_MEM": "ice40up5k_spram",
                        "PICOSOC_SB_IO": "1",
                    }
        return {}

    def firmware_extrafiles(self):
        for num, data in enumerate(self.jdata["plugins"]):
            if data["type"] == self.ptype:

                mem = 1024  # 1kByte
                if self.jdata.get("type") == "up5k":
                    mem = 128 * 1024  # 128kByte
                mem_total = data.get("mem", mem)

                makefile = []
                makefile.append("")
                makefile.append(f"CFLAGS=-DMEM_TOTAL=0x{mem_total:x}")
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
                makefile.append("	$(CROSS)gcc $(CFLAGS) -mabi=ilp32 -march=rv32ic -Wl,-Bstatic,-T,firmware.lds,--strip-debug -ffreestanding -nostdlib -o firmware.elf start.s firmware.c")
                makefile.append("")
                makefile.append("firmware.bin: firmware.elf")
                makefile.append("	$(CROSS)objcopy -O binary firmware.elf firmware.bin")
                makefile.append("")
                makefile.append("firmware.hex: firmware.elf")
                makefile.append("	$(CROSS)objcopy -O verilog firmware.elf firmware.hex")
                makefile.append("")
                makefile.append("load: firmware.bin")
                makefile.append("	openFPGALoader -b ice40_generic -o 1048576 firmware.bin")
                makefile.append("	#minicom -D /dev/ttyUSB1 -b 115200")
                makefile.append("")
                return {
                    f"Makefile.{self.ptype}": "\n".join(makefile),
                }
        return {}

