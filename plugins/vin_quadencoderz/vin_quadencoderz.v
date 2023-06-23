
module vin_quadencoderz
    #(parameter BITS = 32)
     (
         input clk,
         input quadA,
         input quadB,
         input quadZ,
         input reset_in,
         output reg reset_out = 0,
         output [BITS-1:0] pos
     );
    reg [2:0] quadA_delayed;
    reg [2:0] quadB_delayed;
    reg [2:0] quadZ_delayed;
    always @(posedge clk) quadA_delayed <= {quadA_delayed[1:0], quadA};
    always @(posedge clk) quadB_delayed <= {quadB_delayed[1:0], quadB};
    always @(posedge clk) quadZ_delayed <= {quadZ_delayed[1:0], quadZ};
    wire count_enable = quadA_delayed[1] ^ quadA_delayed[2] ^ quadB_delayed[1] ^ quadB_delayed[2];
    wire count_direction = quadA_delayed[1] ^ quadB_delayed[2];
    reg [BITS-1:0] count = 0;
    assign pos = count;
    always @(posedge clk) begin
        if (reset_in == 1 && reset_out == 0) begin
            if (quadZ_delayed == 1) begin
                reset_out <= 1;
                count <= 0;
            end
        end else begin
            if (count_enable) begin
                if(count_direction) begin
                    count <= count + 1;
                end else begin
                    count <= count - 1;
                end
            end
            if (reset_in == 0 && reset_out == 1) begin
                reset_out <= 0;
            end
        end

    end
endmodule
