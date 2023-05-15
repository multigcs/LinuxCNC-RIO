
module vin_pulsecounter
    (
        input clk,
        input UP,
        input DOWN,
        input RESET,
        output [31:0] counter
    );
    reg [31:0] cnt = 0;
    assign counter = cnt;

    reg[2:0] UPr;  always @(posedge clk) UPr <= {UPr[1:0], UP};
    reg[2:0] DOWNr;  always @(posedge clk) DOWNr <= {DOWNr[1:0], DOWN};
    wire UP_risingedge = (UPr[2:1]==2'b01);
    wire DOWN_risingedge = (DOWNr[2:1]==2'b01);

    always @(posedge clk)
    begin
        if (RESET) begin
            cnt <= 0;
        end
        if (UP_risingedge) begin
            cnt <= cnt + 1;
        end
        if (DOWN_risingedge) begin
            cnt <= cnt - 1;
        end
    end
endmodule
