`timescale 1ns/100ps

module testb;
    reg clk = 0;
    always #1 clk = !clk;

    wire [15:0] counter;

    reg UP = 0;
    reg DOWN = 0;
    reg RESET = 0;

    always #10 UP = !UP;

    initial begin
        $dumpfile("testb.vcd");
        $dumpvars(0, clk);
        $dumpvars(1, UP);
        $dumpvars(2, DOWN);
        $dumpvars(3, RESET);
        $dumpvars(4, counter);

        # 50 RESET = 1;
        # 51 RESET = 0;
        # 100 $finish;
    end

    vin_pulsecounter vin_pulsecounter1 (
                         .clk (clk),
                         .UP (UP),
                         .DOWN (DOWN),
                         .RESET (RESET),
                         .counter (counter)
                     );

endmodule
