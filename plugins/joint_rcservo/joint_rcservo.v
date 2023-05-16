module joint_rcservo
    #(
         parameter servo_freq = 480000, // clk / 1000 * 10
         parameter servo_center = 72000, // clk / 1000 * 1.5
         parameter servo_scale = 64
     )
     (
         input clk,
         input signed [31:0] jointFreqCmd,
         output signed [31:0] jointFeedback,
         output PWM
     );
    reg [31:0] jointCounter = 32'd0;
    reg [31:0] jointFreqCmdAbs = 32'd0;
    reg signed [31:0] jointFeedbackMem = 32'd0;
    reg step = 0;
    assign jointFeedback = jointFeedbackMem;
    always @ (posedge clk) begin
        if (jointFreqCmd > 0) begin
            jointFreqCmdAbs = jointFreqCmd / 2;
        end else begin
            jointFreqCmdAbs = -jointFreqCmd / 2;
        end
        jointCounter <= jointCounter + 1;
        if (jointFreqCmd != 0) begin
            if (jointCounter >= jointFreqCmdAbs) begin
                step <= ~step;
                jointCounter <= 32'b0;
                if (step) begin
                    if (jointFreqCmd > 0) begin
                        jointFeedbackMem = jointFeedbackMem + 1;
                    end else begin
                        jointFeedbackMem = jointFeedbackMem - 1;
                    end
                end
            end
        end
    end
    reg pulse = 0;
    assign PWM = pulse;
    reg [31:0] counter = 0;
    always @ (posedge clk) begin
        counter = counter + 1;
        if (counter == servo_freq) begin
            pulse = 1;
            counter = 0;
        end else if (counter == servo_center + jointFeedbackMem / servo_scale) begin
            pulse = 0;
        end
    end
endmodule
