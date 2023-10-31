// https://github.com/wuxx/Colorlight-FPGA-Projects/blob/master/src/i5/hdmi_test_pattern/vgatestsrc.v

/*
LOCATE COMP "gpdi_dp[0]" SITE "G19"; # Blue +
LOCATE COMP "gpdi_dn[0]" SITE "H20"; # Blue -
LOCATE COMP "gpdi_dp[1]" SITE "E20"; # Green +
LOCATE COMP "gpdi_dn[1]" SITE "F19"; # Green -
LOCATE COMP "gpdi_dp[2]" SITE "C20"; # Red +
LOCATE COMP "gpdi_dn[2]" SITE "D19"; # Red -
LOCATE COMP "gpdi_dp[3]" SITE "J19"; # Clock +
LOCATE COMP "gpdi_dn[3]" SITE "K19"; # Clock -

IOBUF PORT "gpdi_dp[0]" IO_TYPE=LVCMOS33 DRIVE=4;
IOBUF PORT "gpdi_dn[0]" IO_TYPE=LVCMOS33 DRIVE=4;
IOBUF PORT "gpdi_dp[1]" IO_TYPE=LVCMOS33 DRIVE=4;
IOBUF PORT "gpdi_dn[1]" IO_TYPE=LVCMOS33 DRIVE=4;
IOBUF PORT "gpdi_dp[2]" IO_TYPE=LVCMOS33 DRIVE=4;
IOBUF PORT "gpdi_dn[2]" IO_TYPE=LVCMOS33 DRIVE=4;
IOBUF PORT "gpdi_dp[3]" IO_TYPE=LVCMOS33 DRIVE=4;
IOBUF PORT "gpdi_dn[3]" IO_TYPE=LVCMOS33 DRIVE=4;



module rio (
        output BLINK_LED,
        input sysclk,

        output [3:0] gpdi_dp, gpdi_dn,

        inout PICOSOC0_RX,
        output PICOSOC0_TX,
        output PICOSOC0_FLASH_CSB,
        inout PICOSOC0_FLASH_IO0,
        inout PICOSOC0_FLASH_IO1,
        output PICOSOC_P3_GPIO0,
        output PICOSOC_P3_GPIO1
    );


wire wifi_gpio0;

ULX3S_25F xx0 (
	.clk_25mhz(sysclk),
    .gpdi_dp(gpdi_dp),
    .gpdi_dn(gpdi_dn),
	.wifi_gpio0(wifi_gpio0)
);


*/

`default_nettype none

module ULX3S_25F (
	input clk_25mhz,
        output [3:0] gpdi_dp, gpdi_dn,
	output wifi_gpio0);

  // Tie gpio0 high, this keeps the board from rebooting
  assign wifi_gpio0 = 1'b1;

  wire clk_25MHz, clk_250MHz;
  clock clock_instance(
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


  llhdmi llhdmi_instance(
    .i_tmdsclk(clk_250MHz), .i_pixclk(clk_25MHz),
    .i_reset(reset), .i_red(red), .i_grn(grn), .i_blu(blu),
    .o_rd(o_rd), .o_newline(o_newline), .o_newframe(o_newframe),
    .o_red(o_red), .o_grn(o_grn), .o_blu(o_blu));

  vgatestsrc #(.BITS_PER_COLOR(8))
    vgatestsrc_instance(
      .i_pixclk(clk_25MHz), .i_reset(reset),
      .i_width(640), .i_height(480),
      .i_rd(o_rd), .i_newline(o_newline), .i_newframe(o_newframe),
      .o_pixel(pixel));

  OBUFDS OBUFDS_red(.I(o_red), .O(gpdi_dp[2]), .OB(gpdi_dn[2]));
  OBUFDS OBUFDS_grn(.I(o_grn), .O(gpdi_dp[1]), .OB(gpdi_dn[1]));
  OBUFDS OBUFDS_blu(.I(o_blu), .O(gpdi_dp[0]), .OB(gpdi_dn[0]));
  OBUFDS OBUFDS_clock(.I(clk_25MHz), .O(gpdi_dp[3]), .OB(gpdi_dn[3]));

endmodule




module OBUFDS(
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


`default_nettype none
//
module llhdmi(
  i_tmdsclk, i_pixclk,
  i_reset, i_red, i_grn, i_blu,
  o_rd, o_newline, o_newframe,
`ifdef VERILATOR
  o_TMDS_red, o_TMDS_grn, o_TMDS_blu,
`endif
  o_red, o_grn, o_blu);

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



`default_nettype none

module pattern(input i_tmdsclk, i_pixclk, output red, grn, blu, o_rd,
	o_TMDS_red, o_TMDS_grn, o_TMDS_blu);

  wire [7:0] red, grn, blu;
  wire [23:0] pixel;
  assign red= pixel[23:16];
  assign grn= pixel[15:8];
  assign blu= pixel[7:0];

/* verilator lint_off UNUSED */
  wire o_red;
  wire o_grn;
  wire o_blu;
  wire [9:0] o_TMDS_red, o_TMDS_grn, o_TMDS_blu;
/* verilator lint_on UNUSED */
  wire o_rd, o_newline, o_newframe;

  // A reset line that goes low after 16 ticks
  reg [2:0] reset_cnt = 0;
  wire reset = ~reset_cnt[2];
  always @(posedge i_pixclk)
    if (reset) reset_cnt <= reset_cnt + 1;


  llhdmi llhdmi_instance(
    .i_tmdsclk(i_tmdsclk), .i_pixclk(i_pixclk),
    .i_reset(reset), .i_red(red), .i_grn(grn), .i_blu(blu),
    .o_rd(o_rd), .o_newline(o_newline), .o_newframe(o_newframe),
    .o_TMDS_red(o_TMDS_red), .o_TMDS_grn(o_TMDS_grn), .o_TMDS_blu(o_TMDS_blu),
    .o_red(o_red), .o_grn(o_grn), .o_blu(o_blu));

  vgatestsrc #(.BITS_PER_COLOR(8))
    vgatestsrc_instance(
      .i_pixclk(i_pixclk), .i_reset(reset),
      .i_width(640), .i_height(480),
      .i_rd(o_rd), .i_newline(o_newline), .i_newframe(o_newframe),
      .o_pixel(pixel));

endmodule



////////////////////////////////////////////////////////////////////////////////
//
// Filename: 	vgatestsrc.v
//
// Project:	vgasim, a Verilator based VGA simulator demonstration
//
// Purpose:	To create a series of colorbars, as a testing pattern.
//
// Creator:	Dan Gisselquist, Ph.D.
//		Gisselquist Technology, LLC
//
////////////////////////////////////////////////////////////////////////////////
//
// Copyright (C) 2017-2018, Gisselquist Technology, LLC
//
// This program is free software (firmware): you can redistribute it and/or
// modify it under the terms of  the GNU General Public License as published
// by the Free Software Foundation, either version 3 of the License, or (at
// your option) any later version.
//
// This program is distributed in the hope that it will be useful, but WITHOUT
// ANY WARRANTY; without even the implied warranty of MERCHANTIBILITY or
// FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
// for more details.
//
// You should have received a copy of the GNU General Public License along
// with this program.  (It's in the $(ROOT)/doc directory.  Run make with no
// target there if the PDF file isn't present.)  If not, see
// <http://www.gnu.org/licenses/> for a copy.
//
// License:	GPL, v3, as defined and found on www.gnu.org,
//		http://www.gnu.org/licenses/gpl.html
//
//
////////////////////////////////////////////////////////////////////////////////
//
//
`default_nettype	none
//
module	vgatestsrc(i_pixclk, i_reset,
		// External connections
		i_width, i_height,
		i_rd, i_newline, i_newframe,
		// VGA connections
		o_pixel);
	parameter	BITS_PER_COLOR = 4,
			HW=12, VW=12;
		//HW=13,VW=11;
	localparam	BPC = BITS_PER_COLOR,
			BITS_PER_PIXEL = 3 * BPC,
			BPP = BITS_PER_PIXEL;
	//
	input	wire			i_pixclk, i_reset;
	input	wire	[HW-1:0]	i_width;
	input	wire	[VW-1:0]	i_height;
	//
	input	wire		i_rd, i_newline, i_newframe;
	//
	output	reg	[(BPP-1):0]	o_pixel;



	wire	[BPP-1:0]	white, black, purplish_blue, purple, dark_gray,
				darkest_gray, mid_white, mid_cyan, mid_magenta,
				mid_red, mid_green, mid_blue, mid_yellow;
	wire	[BPC-1:0]	midv, mid_off;

	assign	midv    = { 2'b11, {(BPC-2){1'b0}} };
	assign	mid_off = { (BPC){1'b0} };

	assign	white = {(BPP){1'b1}};
	assign	black = {(BPP){1'b0}};
	assign	purplish_blue = {
				{(BPC){1'b0}},
				3'b001,  {(BPC-3){1'b0}},
				2'b01, {(BPC-2){1'b0}} };
	assign	purple = { {2'b00, {(BPC-2){1'b1}} }, {(BPC){1'b0}},
			{ 1'b0, {(BPC-1){1'b1}} } };

	assign	dark_gray    = {(3){  { 4'b0010, {(BPC-4){1'b0}} } }};
	assign	darkest_gray = {(3){  { 4'b0001, {(BPC-4){1'b0}} } }};

	assign	mid_white   = { midv,    midv,    midv    };
	assign	mid_yellow  = { midv,    midv,    mid_off };
	assign	mid_red     = { midv,    mid_off, mid_off };
	assign	mid_green   = { mid_off, midv,    mid_off };
	assign	mid_blue    = { mid_off, mid_off, midv    };
	assign	mid_cyan    = { mid_off, midv,    midv    };
	assign	mid_magenta = { midv,    mid_off, midv    };

	reg	[HW-1:0]	hpos, hedge;
	reg	[VW-1:0]	ypos, yedge;
	reg	[3:0]		yline, hbar;
	//
	//
	// 1 Border
	// 8 BARS
	// 1 short bar
	// 3 fat bars
	// 1 border
	// 1 gradient bar
	// 1 border
	//
	reg	dline;
	always @(posedge i_pixclk)
	if ((i_reset)||(i_newframe)||(i_newline))
		dline <= 1'b0;
	else if (i_rd)
		dline <= 1'b1;
	
	always @(posedge i_pixclk)
	if ((i_reset)||(i_newframe))
	begin
		ypos  <= 0;
		yline <= 0;
		yedge <= { 4'h0, i_height[(VW-1):4] };
	end else if (i_newline)
	begin
		ypos <= ypos + { {(VW-1){1'h0}}, dline };
		if (ypos >= yedge)
		begin
			yline <= yline + 1'b1;
			yedge <= yedge + { 4'h0, i_height[(VW-1):4] };
		end
	end

	initial	hpos  = 0;
	initial	hbar  = 0;
	initial	hedge = 0; // { 4'h0, i_width[(HW-1):4] };
	always @(posedge i_pixclk)
	if ((i_reset)||(i_newline))
	begin
		hpos <= 0;
		hbar <= 0;
		hedge <= { 4'h0, i_width[(HW-1):4] };
	end else if (i_rd)
	begin
		hpos <= hpos + 1'b1;
		if (hpos >= hedge)
		begin
			hbar <= hbar + 1'b1;
			hedge <= hedge + { 4'h0, i_width[(HW-1):4] };
		end
	end

	reg	[BPP-1:0]	topbar, midbar, fatbar, gradient, pattern;
	always @(posedge i_pixclk)
	case(hbar[3:0])
	4'h0: topbar <= black;
	4'h1: topbar <= mid_white;
	4'h2: topbar <= mid_white;
	4'h3: topbar <= mid_yellow;
	4'h4: topbar <= mid_yellow;
	4'h5: topbar <= mid_cyan;
	4'h6: topbar <= mid_cyan;
	4'h7: topbar <= mid_green;
	4'h8: topbar <= mid_green;
	4'h9: topbar <= mid_magenta;
	4'ha: topbar <= mid_magenta;
	4'hb: topbar <= mid_red;
	4'hc: topbar <= mid_red;
	4'hd: topbar <= mid_blue;
	4'he: topbar <= mid_blue;
	4'hf: topbar <= black;
	endcase

	always @(posedge i_pixclk)
	case(hbar[3:0])
	4'h0: midbar <= black;
	4'h1: midbar <= mid_blue;
	4'h2: midbar <= mid_blue;
	4'h3: midbar <= black;
	4'h4: midbar <= black;
	4'h5: midbar <= mid_magenta;
	4'h6: midbar <= mid_magenta;
	4'h7: midbar <= black;
	4'h8: midbar <= black;
	4'h9: midbar <= mid_cyan;
	4'ha: midbar <= mid_cyan;
	4'hb: midbar <= black;
	4'hc: midbar <= black;
	4'hd: midbar <= mid_white;
	4'he: midbar <= mid_white;
	4'hf: midbar <= black;
	endcase

	always @(posedge i_pixclk)
	case(hbar[3:0])
	4'h0: fatbar <= black;
	4'h1: fatbar <= purplish_blue;
	4'h2: fatbar <= purplish_blue;
	4'h3: fatbar <= purplish_blue;
	4'h4: fatbar <=	white;
	4'h5: fatbar <= white;
	4'h6: fatbar <= white;
	4'h7: fatbar <= purple;
	4'h8: fatbar <= purple;
	4'h9: fatbar <= purple;
	4'ha: fatbar <= darkest_gray;
	4'hb: fatbar <= black;
	4'hc: fatbar <= dark_gray;
	4'hd: fatbar <= darkest_gray;
	4'he: fatbar <= black;
	4'hf: fatbar <= black;
	endcase

	reg	[(HW-1):0]	last_width;
	always @(posedge i_pixclk)
		last_width <= i_width;

	// Attempt to discover 1/i_width in h_step
	localparam	FRACB=16;
	//
	reg	[(FRACB-1):0]	hfrac, h_step;
	always @(posedge i_pixclk)
	if ((i_reset)||(i_newline))
		hfrac <= 0;
	else if (i_rd)
		hfrac <= hfrac + h_step;

	always @(posedge i_pixclk)
	if ((i_reset)||(i_width != last_width))
		h_step <= 1;
	else if ((i_newline)&&(hfrac > 0))
	begin
		if (hfrac < {(FRACB){1'b1}} - { {(FRACB-HW){1'b0}}, i_width })
			h_step <= h_step + 1'b1;
		else if (hfrac < { {(FRACB-HW){1'b0}}, i_width })
			h_step <= h_step - 1'b1;
	end

	always @(posedge i_pixclk)
	case(hfrac[FRACB-1:FRACB-4])
	4'h0: gradient <= black;
	// Red
	4'h1: gradient <= { 1'b0, hfrac[(FRACB-5):(FRACB-3-BPC)], {(2){mid_off}} };
	4'h2: gradient <= { 1'b1, hfrac[(FRACB-5):(FRACB-3-BPC)], {(2){mid_off}} };
	4'h3: gradient <= black;
	// Green
	4'h4: gradient <= { mid_off, 1'b0, hfrac[(FRACB-5):(FRACB-3-BPC)], mid_off };
	4'h5: gradient <= { mid_off, 1'b1, hfrac[(FRACB-5):(FRACB-3-BPC)], mid_off };
	4'h6: gradient <= black;
	// Blue
	4'h7: gradient <= { {(2){mid_off}}, 1'b0, hfrac[(FRACB-5):(FRACB-3-BPC)] };
	4'h8: gradient <= { {(2){mid_off}}, 1'b1, hfrac[(FRACB-5):(FRACB-3-BPC)] };
	4'h9: gradient <= black;
	// Gray
	4'ha: gradient <= {(3){ 2'b00, hfrac[(FRACB-5):(FRACB-2-BPC)] }};
	4'hb: gradient <= {(3){ 2'b01, hfrac[(FRACB-5):(FRACB-2-BPC)] }};
	4'hc: gradient <= {(3){ 2'b10, hfrac[(FRACB-5):(FRACB-2-BPC)] }};
	4'hd: gradient <= {(3){ 2'b11, hfrac[(FRACB-5):(FRACB-2-BPC)] }};
	4'he: gradient <= black;
	//
	4'hf: gradient <= black;
	endcase

	always @(posedge i_pixclk)
	case(yline)
	4'h0: pattern <= black;
	4'h1: pattern <= topbar; //
	4'h2: pattern <= topbar;
	4'h3: pattern <= topbar;
	4'h4: pattern <= topbar;
	4'h5: pattern <= topbar;
	4'h6: pattern <= topbar;
	4'h7: pattern <= topbar;
	4'h8: pattern <= topbar;
	4'h9: pattern <= midbar; //
	4'ha: pattern <= fatbar; //
	4'hb: pattern <= fatbar;
	4'hc: pattern <= fatbar;
	4'hd: pattern <= black;
	4'he: pattern <= gradient;
	4'hf: pattern <= black;
	endcase

	always @(posedge i_pixclk)
	if (i_newline)
		o_pixel <= white;
	else if (i_rd)
	begin
		if (hpos == i_width-12'd3)
			o_pixel <= white;
		else if ((ypos == 0)||(ypos == i_height-1))
			o_pixel <= white;
		else
			o_pixel <= pattern;
	end

endmodule




