
module vout_pwm
    #(parameter divider = 255)
     (
         input clk,
         input signed [31:0] dty,
         output dir,
         output pwm
     );
    reg [31:0] jointCounter = 32'd0;
    reg [31:0] dtyAbs = 32'd0;

    reg pulse = 0;
    assign pwm = pulse;
    reg direction = 0;
    assign dir = direction;
    reg [31:0] counter = 0;
    always @ (posedge clk) begin
        if (dty > 0) begin
            dtyAbs = dty;
            direction = 1;
        end else begin
            dtyAbs = -dty;
            direction = 0;
        end
        if (dtyAbs != 0) begin
            counter = counter + 1;
            if (counter == divider) begin
                pulse = 1;
                counter = 0;
            end else if (counter == dtyAbs) begin
                pulse = 0;
            end
        end else begin
            pulse = 0;
        end
    end
endmodule
