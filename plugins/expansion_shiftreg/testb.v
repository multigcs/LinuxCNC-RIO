`timescale 1ns/100ps

module testb;
    reg clk = 0;
    always #2 clk = !clk;

    wire SHIFT_OUT;
    reg SHIFT_IN = 0;
    wire SHIFT_CLK;
    wire SHIFT_LOAD;
    wire [7:0] data_in;
    reg [7:0] data_out = 8'd3;

    initial begin
        $dumpfile("testb.vcd");
    
        $dumpvars(0, clk);
        $dumpvars(1, SHIFT_OUT);
        $dumpvars(2, SHIFT_IN);
        $dumpvars(3, SHIFT_CLK);
        $dumpvars(4, SHIFT_LOAD);
        $dumpvars(5, data_in);
        $dumpvars(6, data_out);

        # 36 SHIFT_IN = 1;
        # 24 SHIFT_IN = 0;
        # 24 SHIFT_IN = 1;
        # 24 SHIFT_IN = 0;

        # 500 $finish;
    end

    expansion_shiftreg #(8, 1) expansion_shiftreg1 (
        .clk (clk),
        .SHIFT_OUT (SHIFT_OUT),
        .SHIFT_IN (SHIFT_IN),
        .SHIFT_CLK (SHIFT_CLK),
        .SHIFT_LOAD (SHIFT_LOAD),
        .data_in (data_in),
        .data_out (data_out)
    );

endmodule
