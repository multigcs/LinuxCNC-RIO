
module joint_pwmdir
    #(
         parameter pwm_freq = 100000, // clk / 1000 * 10
     )
     (
         input clk,
         input jointEnable,
         input signed [31:0] jointFreqCmd,
         output signed [31:0] jointFeedback,
         output DIR,
         output PWM
     );
    reg [31:0] jointCounter = 32'd0;
    reg [31:0] jointFreqCmdAbs = 32'd0;
    reg signed [31:0] jointFeedbackMem = 32'd0;
    reg step = 0;
    assign jointFeedback = jointFeedbackMem;

    assign DIR = (jointFreqCmd > 0);

    reg pulse = 0;
    assign PWM = pulse;
    reg [31:0] counter = 0;
    always @ (posedge clk) begin
        if (jointFreqCmd > 0) begin
            jointFreqCmdAbs = jointFreqCmd;
        end else begin
            jointFreqCmdAbs = -jointFreqCmd;
        end
        if (jointFreqCmdAbs > 0) begin
            counter = counter + 1;
            if (counter == pwm_freq) begin
                pulse = 1;
                counter = 0;
            end else if (counter == jointFreqCmdAbs) begin
                pulse = 0;
            end
        end else begin
            pulse = 0;
        end
    end
endmodule
