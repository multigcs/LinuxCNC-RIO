
module vin_ps2
    #(parameter SPEED = 24)
    (
        input  clk,
        input  ps2_clk,
        input  ps2_data,
        output reg [15:0]code
    );

    reg [7:0] data_curr;
    reg [7:0] data_pre;
    reg [3:0] b;
    reg flag;

    initial begin
        b <= 4'h1;
        flag <= 1'b0;
        data_curr <= 8'hf0;
        data_pre <= 8'hf0;
    end

    always @(negedge ps2_clk) begin
        case(b)
            1: ; //first bit
            2: data_curr[0] <= ps2_data;
            3: data_curr[1] <= ps2_data;
            4: data_curr[2] <= ps2_data;
            5: data_curr[3] <= ps2_data;
            6: data_curr[4] <= ps2_data;
            7: data_curr[5] <= ps2_data;
            8: data_curr[6] <= ps2_data;
            9: data_curr[7] <= ps2_data;
            10: flag <= 1'b1; //Parity bit
            11: flag <= 1'b0; //Ending bit
        endcase
        if (b <= 10) begin
            b <= b + 1;
        end else if (b == 11) begin
            code <= code<<8;
            code[7:0] <= data_curr;
            b <= 1;
        end
    end

    always @(posedge flag) begin
        if (data_curr == 8'hf0) begin
            //code <= data_pre;
        end else begin
            data_pre <= data_curr;
        end
    end


endmodule
