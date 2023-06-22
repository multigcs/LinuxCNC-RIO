/* verilator lint_off WIDTH */
module vout_spipoti
    #(parameter WIDTH = 8, SPEED = 100000)
    (
       input clk,
       output reg MOSI = 0,
       output reg SCLK = 0,
       output reg CS = 1,
       input wire [7:0] value
    );
    parameter cmd = 8'd0;
    reg [7:0] state = 0;
    reg [7:0] data_pos = 0;
    reg [31:0] counter = 0;
    reg mclk = 0;
    reg next_clk = 0;
    wire [15:0] cmddata = {cmd, value};
    always @(posedge clk) begin
        if (counter == 0) begin
            counter <= SPEED;
            mclk <= ~mclk;
        end else begin
            counter <= counter - 1;
        end
    end
    always @(posedge mclk) begin
        if (state == 0) begin
            SCLK = 0;
            CS = 0;
            data_pos = 0;
            state = 1;
            next_clk = 0;
        end else if (state == 1) begin
            if (next_clk == 1) begin
                next_clk = 0;
                SCLK = 1;
            end else if (data_pos < 16) begin
                SCLK = 0;
                MOSI = cmddata[15 - data_pos];
                next_clk = 1;
                data_pos = data_pos + 1;
            end else begin
                state = 2;
                MOSI = 0;
                SCLK = 0;
            end
        end else if (state == 2) begin
            CS = 1;
            state = state + 1;
        end else if (state == 3) begin
            state = 0;
        end
    end
endmodule












