module quad_encoder
    #(parameter BITS = 32)
     (
         input clk,
         input quadA,
         input quadB,
         output [BITS-1:0] pos
     );
    reg [2:0] quadA_delayed, quadB_delayed;
    always @(posedge clk) quadA_delayed <= {quadA_delayed[1:0], quadA};
    always @(posedge clk) quadB_delayed <= {quadB_delayed[1:0], quadB};
    wire count_enable = quadA_delayed[1] ^ quadA_delayed[2] ^ quadB_delayed[1] ^ quadB_delayed[2];
    wire count_direction = quadA_delayed[1] ^ quadB_delayed[2];
    reg [BITS-1:0] count = 0;
    assign pos = count;
    always @(posedge clk) begin
        if (count_enable) begin
            if(count_direction) begin
                count <= count + 1;
            end else begin
                count <= count - 1;
            end
        end
    end
endmodule
