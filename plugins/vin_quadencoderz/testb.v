`timescale 1ns/100ps

module testb;
    reg clk = 0;
    always #2 clk = !clk;

    reg quadA = 0;
    reg quadB = 0;
    reg quadZ = 0;
    reg reset_in = 0;
    wire reset_out;

    wire [31:0] pos;

    initial begin
        $dumpfile("testb.vcd");
        $dumpvars(0, clk);
        $dumpvars(1, quadA);
        $dumpvars(2, quadB);
        $dumpvars(3, quadZ);
        $dumpvars(4, pos);
        $dumpvars(5, reset_in);
        $dumpvars(6, reset_out);

        # 5 quadA = 1;
        # 5 quadB = 1;
        # 5 quadA = 0;
        # 5 quadB = 0;
        # 5 quadZ = 1;
        # 5 quadZ = 0;
        # 5 quadA = 1;
        # 5 quadB = 1;
        # 1 reset_in = 1;
        # 5 quadA = 0;
        # 5 quadB = 0;
        # 5 quadZ = 1;
        # 5 quadZ = 0;
        # 5 quadA = 1;
        # 5 quadB = 1;
        # 5 quadA = 0;
        # 5 quadB = 0;
        # 5 quadZ = 1;
        # 5 quadZ = 0;
        # 8 reset_in = 0;
        # 5 quadA = 1;
        # 5 quadB = 1;
        # 5 quadA = 0;
        # 5 quadB = 0;
        # 5 quadZ = 1;
        # 5 quadZ = 0;
        # 100 $finish;
    end

    vin_quadencoderz vin_quadencoderz1 (
                         .clk (clk),
                         .quadA (quadA),
                         .quadB (quadB),
                         .quadZ (quadZ),
                         .reset_in (reset_in),
                         .reset_out (reset_out),
                         .pos (pos)
                     );

endmodule
