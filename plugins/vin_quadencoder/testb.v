`timescale 1ns/100ps

module testb;
    reg clk = 0;
    always #2 clk = !clk;

    reg quadA = 0;
    reg quadB = 0;

    wire [31:0] pos;

    initial begin
        $dumpfile("testb.vcd");
        $dumpvars(0, clk);
        $dumpvars(1, quadA);
        $dumpvars(2, quadB);
        $dumpvars(3, pos);

        # 10 quadA = 1;
        # 10 quadB = 1;
        # 10 quadA = 0;
        # 10 quadB = 0;
        # 100 $finish;
    end

    vin_quadencoder vin_quadencoder1 (
        .clk (clk),
        .quadA (quadA),
        .quadB (quadB),
        .pos (pos)
    );

endmodule
