module blink
    (
        input clk,
        input [31:0] speed,
        output led
    );
    reg rled;
    reg [31:0] counter;
    assign led = rled;
    always @(posedge clk) begin
        if (counter == 0) begin
            counter <= speed;
            rled <= ~rled;
        end else begin
            counter <= counter - 1;
        end
    end
endmodule
