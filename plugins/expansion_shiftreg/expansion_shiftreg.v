/* verilator lint_off WIDTHTRUNC */
module expansion_shiftreg
    #(
        parameter WIDTH = 8, 
        parameter SPEED = 100000
    )
    (
       input clk,
       output reg SHIFT_OUT = 0,
       input SHIFT_IN,
       output reg SHIFT_CLK = 0,
       output reg SHIFT_LOAD = 1,
       output reg [WIDTH-1:0] data_in = 0,
       input [WIDTH-1:0] data_out
    );
    reg [7:0] data_pos = 0;
    reg [31:0] counter = 0;
    reg [8:0] state = 0;
    reg delay = 0;

    always @(posedge clk) begin
        if (counter == 0) begin
            counter <= SPEED;

            if (state == 0) begin
                if (delay == 1) begin
                    delay <= 0;
                    SHIFT_CLK <= 1;
                end else if (SHIFT_CLK == 1) begin
                    SHIFT_CLK <= 0;
                    data_pos <= data_pos + 1;
                end else if (data_pos < WIDTH) begin
                    data_in[data_pos] = SHIFT_IN;
                    SHIFT_OUT = data_out[WIDTH - 1 - data_pos];
                    delay <= 1;
                end else begin
                    SHIFT_LOAD <= 1'd0;
                    state <= 1;
                end
            end else if (state == 1) begin
                // output
                SHIFT_LOAD <= 1'd1;
                SHIFT_CLK <= 1'd0;
                data_pos <= 8'd0;
                state <= 0;
            end

        end else begin
            counter <= counter - 1;
        end
    end
endmodule
