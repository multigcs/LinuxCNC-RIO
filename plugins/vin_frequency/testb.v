`timescale 1ns/100ps

module testb;
    reg clk = 0;
    always #1 clk = !clk;

    wire [15:0] frequency;

    reg SIGNAL = 0;

    always #100 SIGNAL = !SIGNAL;

    initial begin
        $dumpfile("testb.vcd");
        $dumpvars(0, clk);
        $dumpvars(1, SIGNAL);
        $dumpvars(2, frequency);

        # 10000 $finish;
    end

    freq_counter freq_counter1 (
                     .clk (clk),
                     .SIGNAL (SIGNAL),
                     .frequency (frequency)
                 );

endmodule
