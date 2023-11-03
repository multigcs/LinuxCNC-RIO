
`default_nettype none
`define CN_X 32
`define CN_Y 24
`define START_X 216
`define START_Y 81
//`define CN_X16 32*16+`START_X
//`define CN_Y16 24*16+`START_Y
`define CN_X16 728
`define CN_Y16 465

module peripheral_hdmi (
        input resetn,
        input clk,
        input iomem_valid,
        input [3:0]  iomem_wstrb,
        input [31:0] iomem_addr,
        output reg [31:0] iomem_rdata,
        output reg iomem_ready,
        input [31:0] iomem_wdata,
        output wire gpdi_dp0,
        output wire gpdi_dn0,
        output wire gpdi_dp1,
        output wire gpdi_dn1,
        output wire gpdi_dp2,
        output wire gpdi_dn2,
        output wire gpdi_dp3,
        output wire gpdi_dn3
    );


    //reg [(`CN_X*`CN_Y*8)-1:0] textbuffer = "1                                       Hallo Facebook                                               Das ist ein HDMI-Bild                                               generiert mit                                            Verilog auf einem ECP5 FPGA                                   --------------------------------                                          pure logic                                                   without softcore                                              by Oliver Dippel :)                                                                                                        21                              22                              23                              24                                                             X";
    reg [(`CN_X*`CN_Y*8)-1:0] textbuffer = 0;

    reg [15:1] pos = 0;

    always @(posedge clk) begin
        if (!resetn) begin
            //
        end else begin
            iomem_ready <= 0;
            if (iomem_valid && !iomem_ready) begin
                iomem_ready <= 1;
                iomem_rdata <= 0;

                if (iomem_wstrb[0]) begin

                    textbuffer <= textbuffer<<8;

                    textbuffer[7:0] <= iomem_wdata[7:0];

                end

            end
        end
    end


    wire clk_25MHz;
    wire clk_250MHz;
    clock clock_instance (
        .clkin_25MHz(clk),
        .clk_25MHz(clk_25MHz),
        .clk_250MHz(clk_250MHz)
    );

    wire [7:0] red;
    wire [7:0] grn;
    wire [7:0] blu;
    wire [23:0] pixel;
    assign red = pixel[23:16];
    assign grn = pixel[15:8];
    assign blu = pixel[7:0];

    wire o_red;
    wire o_grn;
    wire o_blu;
    wire o_rd;
    wire o_newline;
    wire o_newframe;

    reg [2:0] reset_cnt = 0;
    wire reset = ~reset_cnt[2];
    always @(posedge clk) begin
        if (reset) begin
            reset_cnt <= reset_cnt + 1;
        end
    end

    llhdmi llhdmi_instance (
        .i_tmdsclk(clk_250MHz),
        .i_pixclk(clk_25MHz),
        .i_reset(reset),
        .i_red(red),
        .i_grn(grn),
        .i_blu(blu),
        .o_rd(o_rd),
        .o_newline(o_newline),
        .o_newframe(o_newframe),
        .o_red(o_red),
        .o_grn(o_grn),
        .o_blu(o_blu)
    );

    drawtext #(.BITS_PER_COLOR(8)) drawtext_instance (
        .i_pixclk(clk_25MHz),
        .i_reset(reset),
        .i_width(640),
        .i_height(480),
        .i_rd(o_rd),
        .i_newline(o_newline),
        .i_newframe(o_newframe),
        .o_pixel(pixel),
        .textbuffer(textbuffer)
    );

    OBUFDS OBUFDS_red(.I(o_red), .O(gpdi_dp2), .OB(gpdi_dn2));
    OBUFDS OBUFDS_grn(.I(o_grn), .O(gpdi_dp1), .OB(gpdi_dn1));
    OBUFDS OBUFDS_blu(.I(o_blu), .O(gpdi_dp0), .OB(gpdi_dn0));
    OBUFDS OBUFDS_clock(.I(clk_25MHz), .O(gpdi_dp3), .OB(gpdi_dn3));
endmodule


module OBUFDS (
        input I, // input
        output O, // positive output
        output OB // negative output
    );
    assign O = I;
    assign OB = ~I;
endmodule


// (c) fpga4fun.com & KNJN LLC 2013
module TMDS_encoder (
        input clk, // 250 MHz
        input [7:0] VD,  // video data (red, green or blue)
        input [1:0] CD,  // control data
        input VDE,  // video data enable, to choose between CD (when VDE=0) and VD (when VDE=1)
        output reg [9:0] TMDS = 0
    );

    wire [3:0] Nb1s = {3'b0, VD[0]} + {3'b0, VD[1]} + {3'b0, VD[2]}
        + {3'b0, VD[3]} + {3'b0, VD[4]} + {3'b0, VD[5]}
        + {3'b0, VD[6]} + {3'b0, VD[7]};
    wire XNOR = (Nb1s>4'd4) || (Nb1s==4'd4 && VD[0]==1'b0);

    // To keep Verilator happy, we create individual wires, determine
    // their values and then merge them into q_m[]
    wire QM0, QM1, QM2, QM3, QM4, QM5, QM6, QM7, QM8;
    assign QM0= VD[0];
    assign QM1= QM0 ^ VD[1] ^ XNOR;
    assign QM2= QM1 ^ VD[2] ^ XNOR;
    assign QM3= QM2 ^ VD[3] ^ XNOR;
    assign QM4= QM3 ^ VD[4] ^ XNOR;
    assign QM5= QM4 ^ VD[5] ^ XNOR;
    assign QM6= QM5 ^ VD[6] ^ XNOR;
    assign QM7= QM6 ^ VD[7] ^ XNOR;
    assign QM8= ~XNOR;
    wire [8:0] q_m = { QM8, QM7, QM6, QM5, QM4, QM3, QM2, QM1, QM0 };

    reg [3:0] balance_acc = 0;
    wire [3:0] balance = {3'b0, q_m[0]} + {3'b0, q_m[1]} + {3'b0, q_m[2]}
        + {3'b0, q_m[3]} + {3'b0, q_m[4]} + {3'b0, q_m[5]}
        + {3'b0, q_m[6]} + {3'b0, q_m[7]} - 4'd4;
    wire balance_sign_eq = (balance[3] == balance_acc[3]);
    wire invert_q_m = (balance==0 || balance_acc==0) ? ~q_m[8] : balance_sign_eq;

    wire [3:0] balance_acc_inc = balance - {3'b0, ({q_m[8] ^ ~balance_sign_eq} & ~(balance==0 || balance_acc==0))};
    wire [3:0] balance_acc_new = invert_q_m ? balance_acc-balance_acc_inc : balance_acc+balance_acc_inc;
    wire [9:0] TMDS_data = {invert_q_m, q_m[8], q_m[7:0] ^ {8{invert_q_m}}};
    wire [9:0] TMDS_code = CD[1] ? (CD[0] ? 10'b1010101011 : 10'b0101010100) : (CD[0] ? 10'b0010101011 : 10'b1101010100);

    always @(posedge clk) TMDS <= VDE ? TMDS_data : TMDS_code;
    always @(posedge clk) balance_acc <= VDE ? balance_acc_new : 4'h0;
endmodule



module clock (
        input clkin_25MHz,
        output clk_125MHz,
        output clk_250MHz,
        output clk_25MHz,
        output clk_83M333Hz,
        output locked
    );
    wire int_locked;

    (* ICP_CURRENT="9" *) (* LPF_RESISTOR="8" *) (* MFG_ENABLE_FILTEROPAMP="1" *) (* MFG_GMCREF_SEL="2" *)
    EHXPLLL
    #(
        .PLLRST_ENA("DISABLED"),
        .INTFB_WAKE("DISABLED"),
        .STDBY_ENABLE("DISABLED"),
        .DPHASE_SOURCE("DISABLED"),
        .CLKOS_FPHASE(0),
        .CLKOP_FPHASE(0),
        .CLKOS3_CPHASE(5),
        .CLKOS2_CPHASE(0),
        .CLKOS_CPHASE(1),
        .CLKOP_CPHASE(3),
        .OUTDIVIDER_MUXD("DIVD"),
        .OUTDIVIDER_MUXC("DIVC"),
        .OUTDIVIDER_MUXB("DIVB"),
        .OUTDIVIDER_MUXA("DIVA"),
        .CLKOS3_ENABLE("ENABLED"),
        .CLKOS2_ENABLE("ENABLED"),
        .CLKOS_ENABLE("ENABLED"),
        .CLKOP_ENABLE("ENABLED"),
        .CLKOS3_DIV(0),
        .CLKOS2_DIV(20),
        .CLKOS_DIV(2),
        .CLKOP_DIV(4),
        .CLKFB_DIV(5),
        .CLKI_DIV(1),
        .FEEDBK_PATH("CLKOP")
    )
    pll_i
    (
        .CLKI(clkin_25MHz),
        .CLKFB(clk_125MHz),
        .CLKOP(clk_125MHz),
        .CLKOS(clk_250MHz),
        .CLKOS2(clk_25MHz), 
        .CLKOS3(clk_83M333Hz),
        .RST(1'b0),
        .STDBY(1'b0),
        .PHASESEL0(1'b0),
        .PHASESEL1(1'b0),
        .PHASEDIR(1'b0),
        .PHASESTEP(1'b0),
        .PLLWAKESYNC(1'b0),
        .ENCLKOP(1'b0),
        .ENCLKOS(1'b0),
        .ENCLKOS2(1'b0),
        .ENCLKOS3(1'b0),
        .LOCK(locked),
        .INTLOCK(int_locked)
    );
endmodule


module llhdmi (
        i_tmdsclk,
        i_pixclk,
        i_reset,
        i_red,
        i_grn,
        i_blu,
        o_rd,
        o_newline,
        o_newframe,
`ifdef VERILATOR
        o_TMDS_red,
        o_TMDS_grn,
        o_TMDS_blu,
`endif
        o_red,
        o_grn,
        o_blu
    );

    input wire i_tmdsclk;		// TMDS clock
    input wire i_pixclk;		// Pixel clock, 10 times slower than i_tmdsclk
    input wire i_reset;		// Reset this module when strobed high
    input wire [7:0] i_red;	// Red green and blue colour values
    input wire [7:0] i_grn;	// for each pixel
    input wire [7:0] i_blu;
    output wire o_rd;		// True when we can accept pixel data
    output reg o_newline;		// True on last pixel of each line
    output reg o_newframe;	// True on last pixel of each frame
    output wire o_red;		// Red TMDS pixel stream
    output wire o_grn;		// Green TMDS pixel stream
    output wire o_blu;		// Blue TMDS pixel stream
`ifdef VERILATOR
    output wire [9:0] o_TMDS_red, o_TMDS_grn, o_TMDS_blu;
    assign o_TMDS_red= TMDS_red;
    assign o_TMDS_grn= TMDS_grn;
    assign o_TMDS_blu= TMDS_blu;
`endif

    reg [9:0] CounterX, CounterY;
    reg hSync, vSync, DrawArea;

    // Keep track of the current X/Y pixel position
    always @(posedge i_pixclk)
    if (i_reset) begin
        CounterX <= 0;
    end else begin
        CounterX <= (CounterX==799) ? 0 : CounterX+1;
    end

    always @(posedge i_pixclk)
    if (i_reset) begin
        CounterY <= 0;
    end else if (CounterX==799) begin
        CounterY <= (CounterY==524) ? 0 : CounterY+1;
    end

    // Signal end of line, end of frame
    always @(posedge i_pixclk) begin
        o_newline  <= (CounterX==639) ? 1 : 0;
        o_newframe <= (CounterX==639) && (CounterY==479) ? 1 : 0;
    end

    // Determine when we are in a drawable area
    always @(posedge i_pixclk) begin
        DrawArea <= (CounterX<640) && (CounterY<480);
    end

    assign o_rd= ~i_reset & DrawArea;

    // Generate horizontal and vertical sync pulses
    always @(posedge i_pixclk) begin
        hSync <= (CounterX>=656) && (CounterX<752);
    end

    always @(posedge i_pixclk) begin
        vSync <= (CounterY>=490) && (CounterY<492);
    end

    // Convert the 8-bit colours into 10-bit TMDS values
    wire [9:0] TMDS_red, TMDS_grn, TMDS_blu;
    TMDS_encoder encode_R (
        .clk(i_pixclk),
        .VD(i_red),
        .CD(2'b00),
        .VDE(DrawArea),
        .TMDS(TMDS_red)
    );
    TMDS_encoder encode_G (
        .clk(i_pixclk),
        .VD(i_grn),
        .CD(2'b00),
        .VDE(DrawArea),
        .TMDS(TMDS_grn)
    );
    TMDS_encoder encode_B (
        .clk(i_pixclk),
        .VD(i_blu),
        .CD({vSync,hSync}),
        .VDE(DrawArea),
        .TMDS(TMDS_blu)
    );

    // Strobe the TMDS_shift_load once every 10 i_tmdsclks
    // i.e. at the start of new pixel data
    reg [3:0] TMDS_mod10=0;
    reg TMDS_shift_load=0;
    always @(posedge i_tmdsclk) begin
        if (i_reset) begin
          TMDS_mod10 <= 0;
          TMDS_shift_load <= 0;
        end else begin
          TMDS_mod10 <= (TMDS_mod10==4'd9) ? 4'd0 : TMDS_mod10+4'd1;
          TMDS_shift_load <= (TMDS_mod10==4'd9);
        end
    end

    // Latch the TMDS colour values into three shift registers
    // at the start of the pixel, then shift them one bit each i_tmdsclk.
    // We will then output the LSB on each i_tmdsclk.
    reg [9:0] TMDS_shift_red=0, TMDS_shift_grn=0, TMDS_shift_blu=0;
    always @(posedge i_tmdsclk) begin
        if (i_reset) begin
          TMDS_shift_red <= 0;
          TMDS_shift_grn <= 0;
          TMDS_shift_blu <= 0;
        end else begin
          TMDS_shift_red <= TMDS_shift_load ? TMDS_red: {1'b0, TMDS_shift_red[9:1]};
          TMDS_shift_grn <= TMDS_shift_load ? TMDS_grn: {1'b0, TMDS_shift_grn[9:1]};
          TMDS_shift_blu <= TMDS_shift_load ? TMDS_blu: {1'b0, TMDS_shift_blu[9:1]};
        end
    end

    // Finally output the LSB of each color bitstream
    assign o_red= TMDS_shift_red[0];
    assign o_grn= TMDS_shift_grn[0];
    assign o_blu= TMDS_shift_blu[0];

endmodule


module	drawtext(
        i_pixclk,
        i_reset,
        i_width,
        i_height,
        i_rd,
        i_newline,
        i_newframe,
        o_pixel,
        textbuffer
    );

	parameter BITS_PER_COLOR = 8;
	parameter HW=12;
	parameter VW=12;

    localparam BPC = BITS_PER_COLOR;
    localparam BITS_PER_PIXEL = 3 * BPC;
    localparam BPP = BITS_PER_PIXEL;

	input wire          i_pixclk;
	input wire          i_reset;
	input wire [HW-1:0]	i_width;
	input wire [VW-1:0]	i_height;
	input wire          i_rd;
	input wire          i_newline;
	input wire          i_newframe;
	output reg [(BPP-1):0] o_pixel = 0;
    input wire [(`CN_X*`CN_Y*8)-1:0] textbuffer;

	localparam [8191:0] fontmem = {
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b01100000, 8'b10010010, 8'b00001100, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00001100, 8'b00010000, 8'b00010000, 8'b00100000, 8'b00010000, 8'b00010000, 8'b00001100,
		8'b00000000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00010000,
		8'b00000000, 8'b00110000, 8'b00001000, 8'b00001000, 8'b00000100, 8'b00001000, 8'b00001000, 8'b00110000,
		8'b00000000, 8'b00111100, 8'b00001000, 8'b00010000, 8'b00100000, 8'b00111100, 8'b00000000, 8'b00000000,
		8'b00111000, 8'b01000000, 8'b01110000, 8'b01001000, 8'b01001000, 8'b01001000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b01000100, 8'b00101000, 8'b00010000, 8'b00101000, 8'b01000100, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b01000100, 8'b10101010, 8'b10010010, 8'b10000010, 8'b10000010, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00010000, 8'b00101000, 8'b01000100, 8'b01000100, 8'b01000100, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b01011000, 8'b00100100, 8'b00100100, 8'b00100100, 8'b00100100, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00111000, 8'b00010000, 8'b00000000,
		8'b00000000, 8'b00011100, 8'b00100000, 8'b00011000, 8'b00000100, 8'b00111000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000100, 8'b00000100, 8'b00000100, 8'b00001100, 8'b00110100, 8'b00000000, 8'b00000000,
		8'b00100000, 8'b00100000, 8'b00111000, 8'b00100100, 8'b00100100, 8'b01011000, 8'b00000000, 8'b00000000,
		8'b00001000, 8'b00001000, 8'b00111000, 8'b01001000, 8'b01001000, 8'b00110100, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00111000, 8'b01000100, 8'b01000100, 8'b01000100, 8'b00111000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b01001000, 8'b01001000, 8'b01001000, 8'b01001000, 8'b00110100, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b10000010, 8'b10000010, 8'b10010010, 8'b10010010, 8'b01101101, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00011000,
		8'b00000000, 8'b00100100, 8'b00010100, 8'b00001100, 8'b00010100, 8'b00100100, 8'b00000100, 8'b00000100,
		8'b00001100, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00000000, 8'b00010000, 8'b00000000,
		8'b00000000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00000000, 8'b00010000, 8'b00000000,
		8'b00000000, 8'b01000100, 8'b01000100, 8'b01000100, 8'b01001100, 8'b00110100, 8'b00000100, 8'b00000100,
		8'b00111000, 8'b01000000, 8'b01111000, 8'b01000100, 8'b01000100, 8'b10111000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00001000, 8'b00001000, 8'b00001000, 8'b00011100, 8'b00001000, 8'b01001000, 8'b00110000,
		8'b00000000, 8'b00111000, 8'b00000100, 8'b01111100, 8'b01000100, 8'b00111000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b10110000, 8'b01001000, 8'b01001000, 8'b01001000, 8'b01110000, 8'b01000000, 8'b01000000,
		8'b00000000, 8'b00111000, 8'b00000100, 8'b00000100, 8'b00000100, 8'b00111000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00110100, 8'b01001000, 8'b01001000, 8'b01001000, 8'b00111000, 8'b00001000, 8'b00001000,
		8'b00000000, 8'b10111000, 8'b01000100, 8'b01000100, 8'b01111000, 8'b01000000, 8'b00111000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00010000, 8'b00001000,
		8'b11111110, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b01000100, 8'b00101000, 8'b00010000,
		8'b00000000, 8'b00111000, 8'b00100000, 8'b00100000, 8'b00100000, 8'b00100000, 8'b00100000, 8'b00111000,
		8'b00000000, 8'b10000000, 8'b01000000, 8'b00100000, 8'b00010000, 8'b00001000, 8'b00000100, 8'b00000010,
		8'b00000000, 8'b00111000, 8'b00001000, 8'b00001000, 8'b00001000, 8'b00001000, 8'b00001000, 8'b00111000,
		8'b00000000, 8'b01111100, 8'b00000100, 8'b00001000, 8'b00010000, 8'b00100000, 8'b01000000, 8'b01111100,
		8'b00000000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00101000, 8'b01000100, 8'b01000100,
		8'b00000000, 8'b01000100, 8'b01000100, 8'b00101000, 8'b00010000, 8'b00101000, 8'b01000100, 8'b01000100,
		8'b00000000, 8'b00101000, 8'b00101000, 8'b01010100, 8'b01010100, 8'b10000010, 8'b10000010, 8'b10000010,
		8'b00000000, 8'b00010000, 8'b00010000, 8'b00101000, 8'b00101000, 8'b01000100, 8'b01000100, 8'b01000100,
		8'b00000000, 8'b00111000, 8'b01000100, 8'b01000100, 8'b01000100, 8'b01000100, 8'b01000100, 8'b01000100,
		8'b00000000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b01111100,
		8'b00000000, 8'b00111000, 8'b01000100, 8'b01000000, 8'b00111000, 8'b00000100, 8'b01000100, 8'b00111000,
		8'b00000000, 8'b01000100, 8'b00100100, 8'b00010100, 8'b00111100, 8'b01000100, 8'b01000100, 8'b00111100,
		8'b01100000, 8'b00111000, 8'b01000100, 8'b01000100, 8'b01000100, 8'b01000100, 8'b01000100, 8'b00111000,
		8'b00000000, 8'b00001000, 8'b00001000, 8'b00001000, 8'b00111000, 8'b01001000, 8'b01001000, 8'b00111000,
		8'b00000000, 8'b00111000, 8'b01000100, 8'b01000100, 8'b01000100, 8'b01000100, 8'b01000100, 8'b00111000,
		8'b00000000, 8'b01000100, 8'b01000100, 8'b01100100, 8'b01010100, 8'b01010100, 8'b01001100, 8'b01000100,
		8'b00000000, 8'b10000010, 8'b10000010, 8'b10000010, 8'b10010010, 8'b10101010, 8'b11000110, 8'b10000010,
		8'b00000000, 8'b01111000, 8'b00001000, 8'b00001000, 8'b00001000, 8'b00001000, 8'b00001000, 8'b00001000,
		8'b00000000, 8'b01000100, 8'b01000100, 8'b00100100, 8'b00011100, 8'b00100100, 8'b01000100, 8'b01000100,
		8'b00000000, 8'b00011000, 8'b00100100, 8'b00100100, 8'b00100000, 8'b00100000, 8'b00100000, 8'b01110000,
		8'b00000000, 8'b00111000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00111000,
		8'b00000000, 8'b01000100, 8'b01000100, 8'b01000100, 8'b01111100, 8'b01000100, 8'b01000100, 8'b01000100,
		8'b00000000, 8'b00111000, 8'b01000100, 8'b01000100, 8'b01110100, 8'b00000100, 8'b01000100, 8'b00111000,
		8'b00000000, 8'b00000100, 8'b00000100, 8'b00000100, 8'b01111100, 8'b00000100, 8'b00000100, 8'b01111100,
		8'b00000000, 8'b01111100, 8'b00000100, 8'b00000100, 8'b00111100, 8'b00000100, 8'b00000100, 8'b01111100,
		8'b00000000, 8'b00111100, 8'b01000100, 8'b01000100, 8'b01000100, 8'b01000100, 8'b01000100, 8'b00111100,
		8'b00000000, 8'b00111000, 8'b01000100, 8'b00000100, 8'b00000100, 8'b00000100, 8'b01000100, 8'b00111000,
		8'b00000000, 8'b00111100, 8'b01000100, 8'b01000100, 8'b00111100, 8'b01000100, 8'b01000100, 8'b00111100,
		8'b00000000, 8'b01000100, 8'b01000100, 8'b01000100, 8'b01111100, 8'b01000100, 8'b01000100, 8'b00111000,
		8'b00000000, 8'b00111000, 8'b00000100, 8'b01110100, 8'b01010100, 8'b01110100, 8'b01000100, 8'b00111000,
		8'b00000000, 8'b00010000, 8'b00000000, 8'b00010000, 8'b00100000, 8'b01000000, 8'b01000100, 8'b00111000,
		8'b00000000, 8'b00000100, 8'b00001000, 8'b00010000, 8'b00100000, 8'b00010000, 8'b00001000, 8'b00000100,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b11111110, 8'b00000000, 8'b11111110, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00100000, 8'b00010000, 8'b00001000, 8'b00000100, 8'b00001000, 8'b00010000, 8'b00100000,
		8'b00010000, 8'b00100000, 8'b00110000, 8'b00110000, 8'b00000000, 8'b00110000, 8'b00110000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00110000, 8'b00110000, 8'b00000000, 8'b00110000, 8'b00110000, 8'b00000000,
		8'b00000000, 8'b00111000, 8'b01000100, 8'b01000000, 8'b01111000, 8'b01000100, 8'b01000100, 8'b00111000,
		8'b00000000, 8'b00111000, 8'b01000100, 8'b01000100, 8'b00111000, 8'b01000100, 8'b01000100, 8'b00111000,
		8'b00000000, 8'b00001000, 8'b00001000, 8'b00001000, 8'b00010000, 8'b00100000, 8'b01000000, 8'b01111100,
		8'b00000000, 8'b00111000, 8'b01000100, 8'b01000100, 8'b00111100, 8'b00000100, 8'b01000100, 8'b00111000,
		8'b00000000, 8'b00111000, 8'b01000100, 8'b01000000, 8'b00111100, 8'b00000100, 8'b00000100, 8'b01111100,
		8'b00000000, 8'b01110000, 8'b00100000, 8'b00100000, 8'b01111100, 8'b00100100, 8'b00101000, 8'b00110000,
		8'b00000000, 8'b00111000, 8'b01000100, 8'b01000000, 8'b00110000, 8'b01000000, 8'b01000100, 8'b00111000,
		8'b00000000, 8'b01111100, 8'b00001000, 8'b00010000, 8'b00100000, 8'b01000000, 8'b01000100, 8'b00111000,
		8'b00000000, 8'b00111000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00011000, 8'b00010000,
		8'b00000000, 8'b00111000, 8'b01000100, 8'b01000100, 8'b01010100, 8'b01000100, 8'b01000100, 8'b00111000,
		8'b00000000, 8'b00000010, 8'b00000100, 8'b00001000, 8'b00010000, 8'b00100000, 8'b01000000, 8'b10000000,
		8'b00000000, 8'b00110000, 8'b00110000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b11111110, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00010000, 8'b00100000, 8'b00110000, 8'b00110000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b11111110, 8'b00010000, 8'b00010000, 8'b00010000,
		8'b00000000, 8'b00010000, 8'b10010010, 8'b01010100, 8'b00111000, 8'b01010100, 8'b10010010, 8'b00010000,
		8'b00000000, 8'b00001000, 8'b00010000, 8'b00100000, 8'b00100000, 8'b00100000, 8'b00010000, 8'b00001000,
		8'b00000000, 8'b00100000, 8'b00010000, 8'b00001000, 8'b00001000, 8'b00001000, 8'b00010000, 8'b00100000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00010000, 8'b00010000,
		8'b00000000, 8'b01011100, 8'b00100010, 8'b01100010, 8'b00010100, 8'b00001000, 8'b00010100, 8'b00011000,
		8'b00000000, 8'b00000000, 8'b01100100, 8'b01101000, 8'b00010000, 8'b00101100, 8'b01001100, 8'b00000000,
		8'b00000000, 8'b00010000, 8'b00111100, 8'b01010000, 8'b00111000, 8'b00010100, 8'b01111000, 8'b00010000,
		8'b00000000, 8'b00101000, 8'b00101000, 8'b11111110, 8'b00101000, 8'b11111110, 8'b00101000, 8'b00101000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00101000, 8'b00101000,
		8'b00000000, 8'b00010000, 8'b00000000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00010000, 8'b00010000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000,
		8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000, 8'b00000000
	};

	function font(input [7:0] c, input [2:0] x, input [2:0] y);
		font = fontmem[{c, y, x}];
	endfunction

	reg [9:0] pos_x = 0;
	reg [9:0] pos_y = 0;
	reg [12:0] ch_n = 0;
	reg [7:0] ch_x = 0;
	reg [7:0] ch_y = 0;
	reg [7:0] ch = " ";

    reg [7:0] r = 0;
    reg [7:0] g = 0;
    reg [7:0] b = 0;

	always @(posedge i_pixclk) begin

        r <= pos_x>>2;
        g <= pos_y>>2;
        b <= (pos_x+pos_y)>>5;

        if (i_newframe == 1) begin
            pos_x <= 0;
            pos_y <= 0;
        end else if (i_newline == 1) begin
            pos_x <= 0;
            pos_y <= pos_y + 1;
        end else begin
            pos_x <= pos_x + 1;
        end

        if (pos_y >= `START_Y && pos_y < `CN_Y16 && pos_x >= `START_X && pos_x < `CN_X16) begin
            ch_n <= (((pos_x - `START_X)>>4) + (((pos_y - `START_Y)>>4)<<5))<<3;
            ch_x <= (pos_x - `START_X - (ch_n<<4))>>1;
            ch_y <= (pos_y - `START_Y)>>1;
            //ch = textbuffer[(`CN_X*`CN_Y*8-(ch_n))-1:(`CN_X*`CN_Y*8-(ch_n))-8];
            o_pixel <= font(textbuffer[(ch_n)+7:(ch_n)], ch_x, ch_y) ? 24'hFFFFFF : {r, g, b};
        end else begin
            o_pixel = {r, g, b};
        end
   
    end
endmodule

