`timescale 1ns/100ps

module testb;
    reg clk = 0;
    always #2 clk = !clk;

    reg signed [31:0] dty = 16'd10000;

    wire PWM;

    initial begin
        $dumpfile("testb.vcd");
        $dumpvars(0, clk);
        $dumpvars(1, dty);
        $dumpvars(2, PWM);
        
        # 500000 dty = 32'd30000;
        # 500000 dty = 32'd50000;
        # 500000 $finish;
    end

    sine_pwm sine_pwm1 (
        .clk (clk),
        .dty (dty),
        .pwm (PWM)
    );

endmodule
