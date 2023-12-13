module joint_unistepper_nf
    (
        input clk,
        input jointEnable,
        input signed [31:0] jointFreqCmd,
        output a1,
        output a2,
        output b1,
        output b2
    );

    reg step = 0;
    wire DIR;
    assign DIR = (jointFreqCmd > 0);
    reg [31:0] jointCounter = 32'd0;
    reg [31:0] jointFreqCmdAbs = 32'd0;

    reg [1:0] unipos = 2'd0;

    assign a1 = jointEnable & (unipos == 0);
    assign a2 = jointEnable & (unipos == 1);
    assign b1 = jointEnable & (unipos == 2);
    assign b2 = jointEnable & (unipos == 3);

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
                if (step) begin
                    if (DIR) begin
                        unipos <= unipos + 1;
                    end else begin
                        unipos <= unipos - 1;
                    end
                end
            end
        end
    end
endmodule

