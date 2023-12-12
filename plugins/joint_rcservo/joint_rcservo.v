module joint_rcservo
    #(
         parameter servo_freq = 480000,
         parameter servo_center = 72000,
         parameter servo_minmax = 72000
     )
     (
         input clk,
         input signed [31:0] jointFreqCmd,
         output signed [31:0] jointFeedback,
         output PWM
     );
    reg pulse = 0;
    assign PWM = pulse;
    reg [31:0] counter = 0;
    reg [31:0] jointCounter = 32'd0;
    reg [31:0] jointFreqCmdAbs = 32'd0;
    reg signed [31:0] jointFeedbackMem = 32'd0;
    reg step = 0;
    wire signed [31:0] jointFeedbackMemCalc;
    assign jointFeedbackMemCalc = {jointFeedbackMem[23:0], 8'h0};
    assign jointFeedback = jointFeedbackMem;
    always @ (posedge clk) begin

        if (jointFreqCmd > 0) begin
            jointFreqCmdAbs <= jointFreqCmd / 2;
        end else begin
            jointFreqCmdAbs <= -jointFreqCmd / 2;
        end
        jointCounter <= jointCounter + 1;
        if (jointFreqCmd != 0) begin
            if (jointCounter >= jointFreqCmdAbs) begin
                step <= ~step;
                jointCounter <= 32'b0;
                if (step) begin
                    if (jointFreqCmd > 0 && jointFeedbackMemCalc < servo_minmax) begin
                        jointFeedbackMem <= jointFeedbackMem + 1;
                    end else if (jointFeedbackMemCalc > -servo_minmax) begin
                        jointFeedbackMem <= jointFeedbackMem - 1;
                    end
                end
            end
        end

        counter <= counter + 1;
        if (counter == servo_freq) begin
            pulse <= 1;
            counter <= 0;
        end else if (counter == servo_center + jointFeedbackMemCalc) begin
            pulse <= 0;
        end

    end
endmodule
