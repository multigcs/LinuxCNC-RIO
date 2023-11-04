
module vout_7seg (
        input clk,
        input signed [31:0] value,
        output reg en1,
        output reg en2,
        output reg en3,
        output reg en4,
        output wire displayA,
        output wire displayB,
        output wire displayC,
        output wire displayD,
        output wire displayE,
        output wire displayF,
        output wire displayG,
        output wire displayP
    );


    wire [6:0] display;
    assign displayA = display[0];
    assign displayB = display[1];
    assign displayC = display[2];
    assign displayD = display[3];
    assign displayE = display[4];
    assign displayF = display[5];
    assign displayG = display[6];

    wire [19:0] bcd;

    bin2bcd bin2bcd1 (
        .bin (value[15:0]),
        .bcd (bcd)
    );
    wire [7:0] int1;
    wire [7:0] int10;
    wire [7:0] int100;
    wire [7:0] int1000;
    wire [7:0] int10000;
    assign int1 = 8'd48 + {4'd0, bcd[3:0]};
    assign int10 = 8'd48 + {4'd0, bcd[7:4]};
    assign int100 = 8'd48 + {4'd0, bcd[11:8]};
    assign int1000 = 8'd48 + {4'd0, bcd[15:12]};
    assign int10000 = 8'd48 + {4'd0, bcd[19:16]};

    reg [3:0] digit;

    reg [7:0] digit_delay = 0;
    reg [1:0] digit_n = 0;
    always @(posedge clk) begin
    
        digit_delay <= digit_delay + 1;

        if (digit_delay == 0) begin
            digit_n <= digit_n + 1;
        end
 
		case (digit_n)
			2'h0: begin
                digit <= int1;
                en1 <= 0;
                en2 <= 1;
                en3 <= 1;
                en4 <= 1;
            end
			2'h1: begin
                digit <= int10;
                en1 <= 1;
                en2 <= 0;
                en3 <= 1;
                en4 <= 1;
            end
			2'h2: begin
                digit <= int100;
                en1 <= 1;
                en2 <= 1;
                en3 <= 0;
                en4 <= 1;
            end
			2'h3: begin
                digit <= int1000;
                en1 <= 1;
                en2 <= 1;
                en3 <= 1;
                en4 <= 0;
            end
		endcase

    end


    seven_segments ss1 (
        .clk(clk),
        .binary(digit),
        .display(display)
    );

endmodule

module bin2bcd(
       input [15:0] bin,
       output reg [19:0] bcd
    );
    integer i;
    always @(bin) begin
        bcd=0;		 	
        for (i = 0; i < 16; i = i + 1) begin
            if (bcd[3:0] >= 5) bcd[3:0] = bcd[3:0] + 3;
            if (bcd[7:4] >= 5) bcd[7:4] = bcd[7:4] + 3;
            if (bcd[11:8] >= 5) bcd[11:8] = bcd[11:8] + 3;
            if (bcd[15:12] >= 5) bcd[15:12] = bcd[15:12] + 3;
            if (bcd[19:16] >= 5) bcd[19:16] = bcd[19:16] + 3;

            bcd = {bcd[18:0], bin[15 - i]};
        end
    end
endmodule



module seven_segments (
        input wire clk,
        input wire [3:0] binary,
        output reg [6:0] display
    );

	always @(binary) begin
		case (binary)
			4'h0: display = 7'b0111111;
			4'h1: display = 7'b0000110;
			4'h2: display = 7'b1011011;
			4'h3: display = 7'b1001111;
			4'h4: display = 7'b1100110;
			4'h5: display = 7'b1101101;
			4'h6: display = 7'b1111101;
			4'h7: display = 7'b0000111;
			4'h8: display = 7'b1111111;
			4'h9: display = 7'b1101111;

			4'ha: display = 7'b1110111;
			4'hb: display = 7'b1111100;
			4'hc: display = 7'b0111001;
			4'hd: display = 7'b1011110;
			4'he: display = 7'b1111001;
			4'hf: display = 7'b1110001;
			default: display = 7'b1111001;
		endcase
	end

endmodule


