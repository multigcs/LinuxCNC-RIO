

`default_nettype none


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


    wire [3:0] gpdi_dp;
    wire [3:0] gpdi_dn;

    assign gpdi_dp0 = gpdi_dp[0];
    assign gpdi_dn0 = gpdi_dn[0];
    assign gpdi_dp1 = gpdi_dp[1];
    assign gpdi_dn1 = gpdi_dn[1];
    assign gpdi_dp2 = gpdi_dp[2];
    assign gpdi_dn2 = gpdi_dn[2];
    assign gpdi_dp3 = gpdi_dp[3];
    assign gpdi_dn3 = gpdi_dn[3];


    ULX3S_25F xx0 (
        .clk_25mhz(clk),
        .gpdi_dp(gpdi_dp),
        .gpdi_dn(gpdi_dn)
    );

endmodule



module ULX3S_25F (
        input clk_25mhz,
        output [3:0] gpdi_dp,
        output [3:0] gpdi_dn
    );

    // Tie gpio0 high, this keeps the board from rebooting
    assign wifi_gpio0 = 1'b1;

    wire clk_25MHz, clk_250MHz;
    clock clock_instance (
        .clkin_25MHz(clk_25mhz),
        .clk_25MHz(clk_25MHz),
        .clk_250MHz(clk_250MHz)
    );

    wire [7:0] red, grn, blu;
    wire [23:0] pixel;
    assign red= pixel[23:16];
    assign grn= pixel[15:8];
    assign blu= pixel[7:0];

    wire o_red;
    wire o_grn;
    wire o_blu;
    wire o_rd, o_newline, o_newframe;

    // A reset line that goes low after 16 ticks
    reg [2:0] reset_cnt = 0;
    wire reset = ~reset_cnt[2];
    always @(posedge clk_25mhz)
    if (reset) reset_cnt <= reset_cnt + 1;


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
        .o_pixel(pixel)
    );

    OBUFDS OBUFDS_red(.I(o_red), .O(gpdi_dp[2]), .OB(gpdi_dn[2]));
    OBUFDS OBUFDS_grn(.I(o_grn), .O(gpdi_dp[1]), .OB(gpdi_dn[1]));
    OBUFDS OBUFDS_blu(.I(o_blu), .O(gpdi_dp[0]), .OB(gpdi_dn[0]));
    OBUFDS OBUFDS_clock(.I(clk_25MHz), .O(gpdi_dp[3]), .OB(gpdi_dn[3]));

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

////////////////////////////////////////////////////////////////////////
module TMDS_encoder(
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

    wire [3:0] balance_acc_inc = balance
        - {3'b0,
           ({q_m[8] ^ ~balance_sign_eq} & ~(balance==0 || balance_acc==0)) };
    wire [3:0] balance_acc_new = invert_q_m ? balance_acc-balance_acc_inc : balance_acc+balance_acc_inc;
    wire [9:0] TMDS_data = {invert_q_m, q_m[8], q_m[7:0] ^ {8{invert_q_m}}};
    wire [9:0] TMDS_code = CD[1] ? (CD[0] ? 10'b1010101011 : 10'b0101010100) : (CD[0] ? 10'b0010101011 : 10'b1101010100);

    always @(posedge clk) TMDS <= VDE ? TMDS_data : TMDS_code;
    always @(posedge clk) balance_acc <= VDE ? balance_acc_new : 4'h0;
endmodule

////////////////////////////////////////////////////////////////////////



module clock
(
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
        i_tmdsclk, i_pixclk,
        i_reset, i_red, i_grn, i_blu,
        o_rd, o_newline, o_newframe,
`ifdef VERILATOR
        o_TMDS_red, o_TMDS_grn, o_TMDS_blu,
`endif
        o_red, o_grn, o_blu
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
    if (i_reset)
      CounterX <= 0;
    else
      CounterX <= (CounterX==799) ? 0 : CounterX+1;

  always @(posedge i_pixclk)
    if (i_reset)
      CounterY <= 0;
    else if (CounterX==799) begin
      CounterY <= (CounterY==524) ? 0 : CounterY+1;
    end

  // Signal end of line, end of frame
  always @(posedge i_pixclk) begin
    o_newline  <= (CounterX==639) ? 1 : 0;
    o_newframe <= (CounterX==639) && (CounterY==479) ? 1 : 0;
  end

  // Determine when we are in a drawable area
  always @(posedge i_pixclk)
    DrawArea <= (CounterX<640) && (CounterY<480);

  assign o_rd= ~i_reset & DrawArea;

  // Generate horizontal and vertical sync pulses
  always @(posedge i_pixclk)
    hSync <= (CounterX>=656) && (CounterX<752);

  always @(posedge i_pixclk)
    vSync <= (CounterY>=490) && (CounterY<492);

  // Convert the 8-bit colours into 10-bit TMDS values
  wire [9:0] TMDS_red, TMDS_grn, TMDS_blu;
  TMDS_encoder encode_R(.clk(i_pixclk), .VD(i_red), .CD(2'b00),
                                        .VDE(DrawArea), .TMDS(TMDS_red));
  TMDS_encoder encode_G(.clk(i_pixclk), .VD(i_grn), .CD(2'b00),
                                        .VDE(DrawArea), .TMDS(TMDS_grn));
  TMDS_encoder encode_B(.clk(i_pixclk), .VD(i_blu), .CD({vSync,hSync}),
                                        .VDE(DrawArea), .TMDS(TMDS_blu));

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
        o_pixel
    );

	parameter BITS_PER_COLOR = 8, HW=12, VW=12;

	localparam	BPC = BITS_PER_COLOR,
			BITS_PER_PIXEL = 3 * BPC,
			BPP = BITS_PER_PIXEL;

	input wire          i_pixclk;
	input wire          i_reset;
	input wire [HW-1:0]	i_width;
	input wire [VW-1:0]	i_height;
	input wire          i_rd;
	input wire          i_newline;
	input wire          i_newframe;


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

	output reg [(BPP-1):0] o_pixel = 0;


    localparam start_x = 220;
    localparam start_y = 100;
    localparam cn_x = 32;
    localparam cn_y = 24;

	reg [9:0] pos_x = 0;
	reg [9:0] pos_y = 0;
	reg [9:0] ch_n = 0;
	reg [7:0] ch_x = 0;
	reg [7:0] ch_y = 0;

    reg [7:0] text [(cn_x*cn_y)-1:0];

    assign text[0] = " ";
    assign text[1] = " ";
    assign text[2] = " ";
    assign text[3] = " ";
    assign text[4] = " ";
    assign text[5] = " ";
    assign text[6] = " ";
    assign text[7] = " ";
    assign text[8] = " ";
    assign text[9] = " ";
    assign text[10] = " ";
    assign text[11] = " ";
    assign text[12] = " ";
    assign text[13] = " ";
    assign text[14] = " ";
    assign text[15] = " ";
    assign text[16] = " ";
    assign text[17] = " ";
    assign text[18] = " ";
    assign text[19] = " ";
    assign text[20] = " ";
    assign text[21] = " ";
    assign text[22] = " ";
    assign text[23] = " ";
    assign text[24] = " ";
    assign text[25] = " ";
    assign text[26] = " ";
    assign text[27] = " ";
    assign text[28] = " ";
    assign text[29] = " ";
    assign text[30] = " ";
    assign text[31] = " ";
    assign text[32] = " ";
    assign text[33] = " ";
    assign text[34] = " ";
    assign text[35] = " ";
    assign text[36] = " ";
    assign text[37] = " ";
    assign text[38] = " ";
    assign text[39] = " ";
    assign text[40] = " ";
    assign text[41] = " ";
    assign text[42] = " ";
    assign text[43] = " ";
    assign text[44] = " ";
    assign text[45] = " ";
    assign text[46] = " ";
    assign text[47] = " ";
    assign text[48] = " ";
    assign text[49] = " ";
    assign text[50] = " ";
    assign text[51] = " ";
    assign text[52] = " ";
    assign text[53] = " ";
    assign text[54] = " ";
    assign text[55] = " ";
    assign text[56] = " ";
    assign text[57] = " ";
    assign text[58] = " ";
    assign text[59] = " ";
    assign text[60] = " ";
    assign text[61] = " ";
    assign text[62] = " ";
    assign text[63] = " ";
    assign text[64] = " ";
    assign text[65] = " ";
    assign text[66] = " ";
    assign text[67] = " ";
    assign text[68] = " ";
    assign text[69] = " ";
    assign text[70] = " ";
    assign text[71] = " ";
    assign text[72] = "H";
    assign text[73] = "a";
    assign text[74] = "l";
    assign text[75] = "l";
    assign text[76] = "o";
    assign text[77] = " ";
    assign text[78] = "F";
    assign text[79] = "a";
    assign text[80] = "c";
    assign text[81] = "e";
    assign text[82] = "b";
    assign text[83] = "o";
    assign text[84] = "o";
    assign text[85] = "k";
    assign text[86] = " ";
    assign text[87] = " ";
    assign text[88] = " ";
    assign text[89] = " ";
    assign text[90] = " ";
    assign text[91] = " ";
    assign text[92] = " ";
    assign text[93] = " ";
    assign text[94] = " ";
    assign text[95] = " ";
    assign text[96] = " ";
    assign text[97] = " ";
    assign text[98] = " ";
    assign text[99] = " ";
    assign text[100] = " ";
    assign text[101] = " ";
    assign text[102] = " ";
    assign text[103] = " ";
    assign text[104] = " ";
    assign text[105] = " ";
    assign text[106] = " ";
    assign text[107] = " ";
    assign text[108] = " ";
    assign text[109] = " ";
    assign text[110] = " ";
    assign text[111] = " ";
    assign text[112] = " ";
    assign text[113] = " ";
    assign text[114] = " ";
    assign text[115] = " ";
    assign text[116] = " ";
    assign text[117] = " ";
    assign text[118] = " ";
    assign text[119] = " ";
    assign text[120] = " ";
    assign text[121] = " ";
    assign text[122] = " ";
    assign text[123] = " ";
    assign text[124] = " ";
    assign text[125] = " ";
    assign text[126] = " ";
    assign text[127] = " ";
    assign text[128] = " ";
    assign text[129] = " ";
    assign text[130] = " ";
    assign text[131] = " ";
    assign text[132] = " ";
    assign text[133] = "D";
    assign text[134] = "a";
    assign text[135] = "s";
    assign text[136] = " ";
    assign text[137] = "i";
    assign text[138] = "s";
    assign text[139] = "t";
    assign text[140] = " ";
    assign text[141] = "e";
    assign text[142] = "i";
    assign text[143] = "n";
    assign text[144] = " ";
    assign text[145] = "H";
    assign text[146] = "D";
    assign text[147] = "M";
    assign text[148] = "I";
    assign text[149] = "-";
    assign text[150] = "B";
    assign text[151] = "i";
    assign text[152] = "l";
    assign text[153] = "d";
    assign text[154] = " ";
    assign text[155] = " ";
    assign text[156] = " ";
    assign text[157] = " ";
    assign text[158] = " ";
    assign text[159] = " ";
    assign text[160] = " ";
    assign text[161] = " ";
    assign text[162] = " ";
    assign text[163] = " ";
    assign text[164] = " ";
    assign text[165] = " ";
    assign text[166] = " ";
    assign text[167] = " ";
    assign text[168] = " ";
    assign text[169] = " ";
    assign text[170] = " ";
    assign text[171] = " ";
    assign text[172] = " ";
    assign text[173] = " ";
    assign text[174] = " ";
    assign text[175] = " ";
    assign text[176] = " ";
    assign text[177] = " ";
    assign text[178] = " ";
    assign text[179] = " ";
    assign text[180] = " ";
    assign text[181] = " ";
    assign text[182] = " ";
    assign text[183] = " ";
    assign text[184] = " ";
    assign text[185] = " ";
    assign text[186] = " ";
    assign text[187] = " ";
    assign text[188] = " ";
    assign text[189] = " ";
    assign text[190] = " ";
    assign text[191] = " ";
    assign text[192] = " ";
    assign text[193] = " ";
    assign text[194] = " ";
    assign text[195] = " ";
    assign text[196] = " ";
    assign text[197] = " ";
    assign text[198] = " ";
    assign text[199] = " ";
    assign text[200] = " ";
    assign text[201] = "g";
    assign text[202] = "e";
    assign text[203] = "n";
    assign text[204] = "e";
    assign text[205] = "r";
    assign text[206] = "i";
    assign text[207] = "e";
    assign text[208] = "r";
    assign text[209] = "t";
    assign text[210] = " ";
    assign text[211] = "m";
    assign text[212] = "i";
    assign text[213] = "t";
    assign text[214] = " ";
    assign text[215] = " ";
    assign text[216] = " ";
    assign text[217] = " ";
    assign text[218] = " ";
    assign text[219] = " ";
    assign text[220] = " ";
    assign text[221] = " ";
    assign text[222] = " ";
    assign text[223] = " ";
    assign text[224] = " ";
    assign text[225] = " ";
    assign text[226] = " ";
    assign text[227] = " ";
    assign text[228] = " ";
    assign text[229] = " ";
    assign text[230] = " ";
    assign text[231] = " ";
    assign text[232] = " ";
    assign text[233] = " ";
    assign text[234] = " ";
    assign text[235] = " ";
    assign text[236] = " ";
    assign text[237] = " ";
    assign text[238] = " ";
    assign text[239] = " ";
    assign text[240] = " ";
    assign text[241] = " ";
    assign text[242] = " ";
    assign text[243] = " ";
    assign text[244] = " ";
    assign text[245] = " ";
    assign text[246] = " ";
    assign text[247] = " ";
    assign text[248] = " ";
    assign text[249] = " ";
    assign text[250] = " ";
    assign text[251] = " ";
    assign text[252] = " ";
    assign text[253] = " ";
    assign text[254] = " ";
    assign text[255] = " ";
    assign text[256] = " ";
    assign text[257] = " ";
    assign text[258] = "V";
    assign text[259] = "e";
    assign text[260] = "r";
    assign text[261] = "i";
    assign text[262] = "l";
    assign text[263] = "o";
    assign text[264] = "g";
    assign text[265] = " ";
    assign text[266] = "a";
    assign text[267] = "u";
    assign text[268] = "f";
    assign text[269] = " ";
    assign text[270] = "e";
    assign text[271] = "i";
    assign text[272] = "n";
    assign text[273] = "e";
    assign text[274] = "m";
    assign text[275] = " ";
    assign text[276] = "E";
    assign text[277] = "C";
    assign text[278] = "P";
    assign text[279] = "5";
    assign text[280] = " ";
    assign text[281] = "F";
    assign text[282] = "P";
    assign text[283] = "G";
    assign text[284] = "A";
    assign text[285] = " ";
    assign text[286] = " ";
    assign text[287] = " ";
    assign text[288] = " ";
    assign text[289] = " ";
    assign text[290] = " ";
    assign text[291] = " ";
    assign text[292] = " ";
    assign text[293] = " ";
    assign text[294] = " ";
    assign text[295] = " ";
    assign text[296] = " ";
    assign text[297] = " ";
    assign text[298] = " ";
    assign text[299] = " ";
    assign text[300] = " ";
    assign text[301] = " ";
    assign text[302] = " ";
    assign text[303] = " ";
    assign text[304] = " ";
    assign text[305] = " ";
    assign text[306] = " ";
    assign text[307] = " ";
    assign text[308] = " ";
    assign text[309] = " ";
    assign text[310] = " ";
    assign text[311] = " ";
    assign text[312] = " ";
    assign text[313] = " ";
    assign text[314] = " ";
    assign text[315] = " ";
    assign text[316] = " ";
    assign text[317] = " ";
    assign text[318] = " ";
    assign text[319] = " ";
    assign text[320] = "-";
    assign text[321] = "-";
    assign text[322] = "-";
    assign text[323] = "-";
    assign text[324] = "-";
    assign text[325] = "-";
    assign text[326] = "-";
    assign text[327] = "-";
    assign text[328] = "-";
    assign text[329] = "-";
    assign text[330] = "-";
    assign text[331] = "-";
    assign text[332] = "-";
    assign text[333] = "-";
    assign text[334] = "-";
    assign text[335] = "-";
    assign text[336] = "-";
    assign text[337] = "-";
    assign text[338] = "-";
    assign text[339] = "-";
    assign text[340] = "-";
    assign text[341] = "-";
    assign text[342] = "-";
    assign text[343] = "-";
    assign text[344] = "-";
    assign text[345] = "-";
    assign text[346] = "-";
    assign text[347] = "-";
    assign text[348] = "-";
    assign text[349] = "-";
    assign text[350] = "-";
    assign text[351] = "-";
    assign text[352] = " ";
    assign text[353] = " ";
    assign text[354] = " ";
    assign text[355] = " ";
    assign text[356] = " ";
    assign text[357] = " ";
    assign text[358] = " ";
    assign text[359] = " ";
    assign text[360] = " ";
    assign text[361] = " ";
    assign text[362] = " ";
    assign text[363] = " ";
    assign text[364] = " ";
    assign text[365] = " ";
    assign text[366] = " ";
    assign text[367] = " ";
    assign text[368] = " ";
    assign text[369] = " ";
    assign text[370] = " ";
    assign text[371] = " ";
    assign text[372] = " ";
    assign text[373] = " ";
    assign text[374] = " ";
    assign text[375] = " ";
    assign text[376] = " ";
    assign text[377] = " ";
    assign text[378] = " ";
    assign text[379] = " ";
    assign text[380] = " ";
    assign text[381] = " ";
    assign text[382] = " ";
    assign text[383] = " ";
    assign text[384] = " ";
    assign text[385] = " ";
    assign text[386] = " ";
    assign text[387] = " ";
    assign text[388] = " ";
    assign text[389] = " ";
    assign text[390] = " ";
    assign text[391] = " ";
    assign text[392] = " ";
    assign text[393] = " ";
    assign text[394] = "p";
    assign text[395] = "u";
    assign text[396] = "r";
    assign text[397] = "e";
    assign text[398] = " ";
    assign text[399] = "l";
    assign text[400] = "o";
    assign text[401] = "g";
    assign text[402] = "i";
    assign text[403] = "c";
    assign text[404] = " ";
    assign text[405] = " ";
    assign text[406] = " ";
    assign text[407] = " ";
    assign text[408] = " ";
    assign text[409] = " ";
    assign text[410] = " ";
    assign text[411] = " ";
    assign text[412] = " ";
    assign text[413] = " ";
    assign text[414] = " ";
    assign text[415] = " ";
    assign text[416] = " ";
    assign text[417] = " ";
    assign text[418] = " ";
    assign text[419] = " ";
    assign text[420] = " ";
    assign text[421] = " ";
    assign text[422] = " ";
    assign text[423] = " ";
    assign text[424] = " ";
    assign text[425] = " ";
    assign text[426] = " ";
    assign text[427] = " ";
    assign text[428] = " ";
    assign text[429] = " ";
    assign text[430] = " ";
    assign text[431] = " ";
    assign text[432] = " ";
    assign text[433] = " ";
    assign text[434] = " ";
    assign text[435] = " ";
    assign text[436] = " ";
    assign text[437] = " ";
    assign text[438] = " ";
    assign text[439] = " ";
    assign text[440] = " ";
    assign text[441] = " ";
    assign text[442] = " ";
    assign text[443] = " ";
    assign text[444] = " ";
    assign text[445] = " ";
    assign text[446] = " ";
    assign text[447] = " ";
    assign text[448] = " ";
    assign text[449] = " ";
    assign text[450] = " ";
    assign text[451] = " ";
    assign text[452] = " ";
    assign text[453] = " ";
    assign text[454] = " ";
    assign text[455] = "w";
    assign text[456] = "i";
    assign text[457] = "t";
    assign text[458] = "h";
    assign text[459] = "o";
    assign text[460] = "u";
    assign text[461] = "t";
    assign text[462] = " ";
    assign text[463] = "s";
    assign text[464] = "o";
    assign text[465] = "f";
    assign text[466] = "t";
    assign text[467] = "c";
    assign text[468] = "o";
    assign text[469] = "r";
    assign text[470] = "e";
    assign text[471] = " ";
    assign text[472] = " ";
    assign text[473] = " ";
    assign text[474] = " ";
    assign text[475] = " ";
    assign text[476] = " ";
    assign text[477] = " ";
    assign text[478] = " ";
    assign text[479] = " ";
    assign text[480] = " ";
    assign text[481] = " ";
    assign text[482] = " ";
    assign text[483] = " ";
    assign text[484] = " ";
    assign text[485] = " ";
    assign text[486] = " ";
    assign text[487] = " ";
    assign text[488] = " ";
    assign text[489] = " ";
    assign text[490] = " ";
    assign text[491] = " ";
    assign text[492] = " ";
    assign text[493] = " ";
    assign text[494] = " ";
    assign text[495] = " ";
    assign text[496] = " ";
    assign text[497] = " ";
    assign text[498] = " ";
    assign text[499] = " ";
    assign text[500] = " ";
    assign text[501] = " ";
    assign text[502] = " ";
    assign text[503] = " ";
    assign text[504] = " ";
    assign text[505] = " ";
    assign text[506] = " ";
    assign text[507] = " ";
    assign text[508] = " ";
    assign text[509] = " ";
    assign text[510] = " ";
    assign text[511] = " ";
    assign text[512] = " ";
    assign text[513] = " ";
    assign text[514] = " ";
    assign text[515] = " ";
    assign text[516] = " ";
    assign text[517] = "b";
    assign text[518] = "y";
    assign text[519] = " ";
    assign text[520] = "O";
    assign text[521] = "l";
    assign text[522] = "i";
    assign text[523] = "v";
    assign text[524] = "e";
    assign text[525] = "r";
    assign text[526] = " ";
    assign text[527] = "D";
    assign text[528] = "i";
    assign text[529] = "p";
    assign text[530] = "p";
    assign text[531] = "e";
    assign text[532] = "l";
    assign text[533] = " ";
    assign text[534] = ":";
    assign text[535] = ")";
    assign text[536] = " ";
    assign text[537] = " ";
    assign text[538] = " ";
    assign text[539] = " ";
    assign text[540] = " ";
    assign text[541] = " ";
    assign text[542] = " ";
    assign text[543] = " ";
    assign text[544] = " ";
    assign text[545] = " ";
    assign text[546] = " ";
    assign text[547] = " ";
    assign text[548] = " ";
    assign text[549] = " ";
    assign text[550] = " ";
    assign text[551] = " ";
    assign text[552] = " ";
    assign text[553] = " ";
    assign text[554] = " ";
    assign text[555] = " ";
    assign text[556] = " ";
    assign text[557] = " ";
    assign text[558] = " ";
    assign text[559] = " ";
    assign text[560] = " ";
    assign text[561] = " ";
    assign text[562] = " ";
    assign text[563] = " ";
    assign text[564] = " ";
    assign text[565] = " ";
    assign text[566] = " ";
    assign text[567] = " ";
    assign text[568] = " ";
    assign text[569] = " ";
    assign text[570] = " ";
    assign text[571] = " ";
    assign text[572] = " ";
    assign text[573] = " ";
    assign text[574] = " ";
    assign text[575] = " ";



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

        if (pos_y >= start_y && pos_y < start_y + 16 * cn_y && pos_x >= start_x && pos_x < start_x + 16 * cn_x) begin
            ch_n = ((pos_x - start_x)>>4) + (((pos_y - start_y)>>4)<<5);
            ch_x = (pos_x - start_x - (ch_n<<4))>>1;
            ch_y = (pos_y - start_y)>>1;
            o_pixel = font(text[ch_n], ch_x, ch_y) ? 24'hFFFFFF : {r, g, b};
        end else begin
            o_pixel = {r, g, b};
        end
   
    end
endmodule



