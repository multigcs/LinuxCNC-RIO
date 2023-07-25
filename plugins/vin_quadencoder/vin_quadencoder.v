module vin_quadencoder
    #(
      parameter BITS = 32,
      parameter QUAD_TYPE = 0
     )
     (
         input clk,
         input quadA,
         input quadB,
         output signed [BITS-1:0] pos
     );
    reg [2:0] quadA_delayed = 0;
    reg [2:0] quadB_delayed = 0;
    always @(posedge clk) quadA_delayed <= {quadA_delayed[1:0], quadA};
    always @(posedge clk) quadB_delayed <= {quadB_delayed[1:0], quadB};
    wire count_enable = quadA_delayed[1] ^ quadA_delayed[2] ^ quadB_delayed[1] ^ quadB_delayed[2];
    wire count_direction = quadA_delayed[1] ^ quadB_delayed[2];
    reg signed [BITS-1:0] count = 0;
    assign pos = $signed(count>>>QUAD_TYPE);
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
