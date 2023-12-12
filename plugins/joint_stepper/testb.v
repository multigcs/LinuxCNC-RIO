`timescale 1ns/100ps

module testb;
    reg clk = 0;
    always #2 clk = !clk;

    reg signed [31:0] jointFreqCmd = 32'd128;
    wire signed [31:0] jointFeedback;

    wire DIR;
    wire STP;

    initial begin
        $dumpfile("testb.vcd");
        $dumpvars(0, clk);
        $dumpvars(1, jointFreqCmd);
        $dumpvars(2, jointFeedback);
        $dumpvars(3, DIR);
        $dumpvars(4, STP);

        # 1000 jointFreqCmd = 10;
        # 2000 $finish;
    end

    joint_stepper joint_stepper1 (
                      .clk (clk),
                      .jointFreqCmd (jointFreqCmd),
                      .jointFeedback (jointFeedback),
                      .DIR (DIR),
                      .STP (STP)
                  );

endmodule
