
module din_toggle
     (
         input clk,
         input din,
         output reg toggled = 0
     );

    reg[2:0] dinr;  always @(posedge clk) dinr <= {dinr[1:0], din};
    wire din_risingedge = (dinr[2:1]==2'b01);  // now we can detect SCK rising edges
    // wire din_fallingedge = (dinr[2:1]==2'b10);  // and falling edges

    always @(posedge clk) begin
        if (din_risingedge) begin
            toggled <= ~toggled;
        end
    end
endmodule
