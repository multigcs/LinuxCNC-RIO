module joint_stepper_nf
    (
        input clk,
        input jointEnable,
        input signed [31:0] jointFreqCmd,
        output DIR,
        output STP
    );
    assign DIR = (jointFreqCmd > 0);
    reg [31:0] jointCounter = 32'd0;
    reg [31:0] jointFreqCmdAbs = 32'd0;
    reg step = 0;
    assign STP = step;
    always @ (posedge clk) begin
        if (DIR) begin
            jointFreqCmdAbs <= jointFreqCmd;
        end else begin
            jointFreqCmdAbs <= -jointFreqCmd;
        end
        jointCounter <= jointCounter + 1;
        if (jointFreqCmd != 0 && jointEnable == 1) begin
            if (jointCounter >= jointFreqCmdAbs) begin
                step <= ~step;
                jointCounter <= 32'b0;
            end
        end
    end
endmodule

