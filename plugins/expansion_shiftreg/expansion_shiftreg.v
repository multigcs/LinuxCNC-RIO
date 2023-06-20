
module expansion_shiftreg
    #(parameter WIDTH = 8, SPEED = 100000)
    (
       input clk,
       output reg SHIFT_OUT,
       input SHIFT_IN,
       output reg SHIFT_CLK,
       output reg SHIFT_LOAD,
       output reg [WIDTH-1:0] data_in,
       input [WIDTH-1:0] data_out
    );
    reg [7:0] data_pos = 0;
    reg rclock;
    reg [31:0] counter;

    always @(posedge clk) begin
        if (counter == 0) begin
            counter <= SPEED;
            SHIFT_CLK <= ~SHIFT_CLK;
        end else begin
            counter <= counter - 1;
        end
    end

    always @(posedge SHIFT_CLK) begin
        if (data_pos < 8) begin
            data_in[WIDTH - 1 - data_pos] = SHIFT_IN;
            SHIFT_OUT = data_out[WIDTH - 1 - data_pos];
            data_pos = data_pos + 8'd1;
        end else if (data_pos == 8) begin
            SHIFT_LOAD = 1'd0;
            data_pos = data_pos + 8'd1;
        end else begin
            SHIFT_LOAD = 1'd1;
            data_pos = 8'd0;
        end
    end
endmodule
