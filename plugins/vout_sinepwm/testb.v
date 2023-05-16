`timescale 1ns/100ps

module testb;
    reg clk = 0;
    always #2 clk = !clk;

    reg signed [31:0] freq = 16'd10000;

    wire pwm_out;

    initial begin
        $dumpfile("testb.vcd");
        $dumpvars(0, clk);
        $dumpvars(1, freq);
        $dumpvars(2, pwm_out);

        # 500000 freq = 32'd30000;
        # 500000 freq = 32'd50000;
        # 500000 $finish;
    end

    vout_sinepwm vout_sinepwm1 (
                 .clk (clk),
                 .freq (freq),
                 .pwm_out (pwm_out)
             );

endmodule
