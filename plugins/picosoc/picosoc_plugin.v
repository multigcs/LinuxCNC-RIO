/*
 *  PicoSoC - A simple example SoC using PicoRV32
 *
 *  Copyright (C) 2017  Claire Xenia Wolf <claire@yosyshq.com>
 *
 *  Permission to use, copy, modify, and/or distribute this software for any
 *  purpose with or without fee is hereby granted, provided that the above
 *  copyright notice and this permission notice appear in all copies.
 *
 *  THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
 *  WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
 *  MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
 *  ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
 *  WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
 *  ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
 *  OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
 *
 */

`ifdef PICOSOC_V
`error "picosoc_plugin.v must be read before picosoc.v!"
`endif


module picosoc_plugin (
    input clk,
    output ser_tx,
    input ser_rx,

    output        resetn,
	output        iomem_valid,
	input         iomem_ready,
	output [ 3:0] iomem_wstrb,
	output [31:0] iomem_addr,
	output [31:0] iomem_wdata,
	input  [31:0] iomem_rdata,

    output [31:0] gpio,
    output flash_csb,
    output flash_clk,
`ifndef PICOSOC_NO_QUADFLASH
    inout  flash_io2,
    inout  flash_io3,
`endif
    inout  flash_io0,
    inout  flash_io1
);
    parameter integer MEM_WORDS = 256;
    parameter [31:0] PROGADDR_RESET = 32'h 0010_0000;

    reg [5:0] reset_cnt = 0;
    wire resetn = &reset_cnt;
    always @(posedge clk) begin
        reset_cnt <= reset_cnt + !resetn;
    end

    wire flash_io0_oe, flash_io0_do, flash_io0_di;
    wire flash_io1_oe, flash_io1_do, flash_io1_di;
`ifndef PICOSOC_NO_QUADFLASH
    wire flash_io2_oe, flash_io2_do, flash_io2_di;
    wire flash_io3_oe, flash_io3_do, flash_io3_di;
`endif

`ifdef PICOSOC_SB_IO
    SB_IO #(
        .PIN_TYPE(6'b 1010_01),
        .PULLUP(1'b 0)
`ifndef PICOSOC_NO_QUADFLASH
    ) flash_io_buf [3:0] (
        .PACKAGE_PIN({flash_io3, flash_io2, flash_io1, flash_io0}),
        .OUTPUT_ENABLE({flash_io3_oe, flash_io2_oe, flash_io1_oe, flash_io0_oe}),
        .D_OUT_0({flash_io3_do, flash_io2_do, flash_io1_do, flash_io0_do}),
        .D_IN_0({flash_io3_di, flash_io2_di, flash_io1_di, flash_io0_di})
    );
`else
    ) flash_io_buf [1:0] (
        .PACKAGE_PIN({flash_io1, flash_io0}),
        .OUTPUT_ENABLE({flash_io1_oe, flash_io0_oe}),
        .D_OUT_0({flash_io1_do, flash_io0_do}),
        .D_IN_0({flash_io1_di, flash_io0_di})
    );
`endif
`else
    assign flash_io0 = flash_io0_oe ? flash_io0_do : 1'bz;
    assign flash_io0_di = flash_io0;
    assign flash_io1 = flash_io1_oe ? flash_io1_do : 1'bz;
    assign flash_io1_di = flash_io1;
`ifndef PICOSOC_NO_QUADFLASH
    assign flash_io2 = flash_io2_oe ? flash_io2_do : 1'bz;
    assign flash_io2_di = flash_io2;
    assign flash_io3 = flash_io3_oe ? flash_io3_do : 1'bz;
    assign flash_io3_di = flash_io3;
`endif
`endif

    picosoc #(
        .BARREL_SHIFTER(0),
        .ENABLE_MUL(1),
        .ENABLE_DIV(1),
        .ENABLE_FAST_MUL(1),
        .ENABLE_COMPRESSED(1),
        .ENABLE_COUNTERS(1),
        .MEM_WORDS(MEM_WORDS),
        .PROGADDR_RESET(PROGADDR_RESET)
    ) soc (
        .clk          (clk         ),
        .resetn       (resetn      ),
        .ser_tx       (ser_tx      ),
        .ser_rx       (ser_rx      ),
        .flash_csb    (flash_csb   ),
        .flash_clk    (flash_clk   ),
`ifndef PICOSOC_NO_QUADFLASH
        .flash_io2_oe (flash_io2_oe),
        .flash_io3_oe (flash_io3_oe),
        .flash_io2_do (flash_io2_do),
        .flash_io3_do (flash_io3_do),
        .flash_io2_di (flash_io2_di),
        .flash_io3_di (flash_io3_di),
`endif
        .flash_io0_oe (flash_io0_oe),
        .flash_io1_oe (flash_io1_oe),
        .flash_io0_do (flash_io0_do),
        .flash_io1_do (flash_io1_do),
        .flash_io0_di (flash_io0_di),
        .flash_io1_di (flash_io1_di),
        .irq_5        (1'b0        ),
        .irq_6        (1'b0        ),
        .irq_7        (1'b0        ),
        .iomem_valid  (iomem_valid ),
        .iomem_ready  (iomem_ready ),
        .iomem_wstrb  (iomem_wstrb ),
        .iomem_addr   (iomem_addr  ),
        .iomem_wdata  (iomem_wdata ),
        .iomem_rdata  (iomem_rdata )
    );
endmodule

