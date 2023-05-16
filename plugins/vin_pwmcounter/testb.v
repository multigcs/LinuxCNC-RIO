`timescale 1ns/100ps

module testb;
    reg clk = 0;
    always #1 clk = !clk;

    wire [15:0] dty;
    wire [15:0] dtyu;

    reg SIGNAL = 0;

    always #100 SIGNAL = !SIGNAL;

    initial begin
        $dumpfile("testb.vcd");
        $dumpvars(0, clk);
        $dumpvars(1, SIGNAL);
        $dumpvars(2, dty);
        $dumpvars(3, dtyu);

        # 10000 $finish;
    end

    pwm_counter pwm_counter1 (
                    .clk (clk),
                    .SIGNAL (SIGNAL),
                    .dty (dty),
                    .dtyu (dtyu)
                );

endmodule
