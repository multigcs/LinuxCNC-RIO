/* verilator lint_off MULTITOP */

module joint_pwmdir
    #(parameter pwm_freq = 100000)
     (
         input clk,
         input jointEnable,
         input signed [31:0] jointFreqCmd,
         output signed [31:0] jointFeedback,
         output DIR,
         output PWM
     );
    reg [31:0] jointFreqCmdAbs = 32'd0;
    reg signed [31:0] jointFeedbackMem = 32'd0;
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
            if (counter >= pwm_freq && jointEnable == 1) begin
                pulse = 1;
                counter = 0;
            end else if (counter >= jointFreqCmdAbs) begin
                pulse = 0;
            end
        end else begin
            pulse = 0;
        end
    end
endmodule

module quad_encoder_pwm
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
