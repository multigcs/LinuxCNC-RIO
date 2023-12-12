`timescale 1ns/100ps

module testb;
    reg clk = 0;
    always #1 clk = !clk;

    reg [7:0] value = 3;

    wire MOSI;
    wire SCLK;
    wire CS;

    //always #10 value = value + 1;

    initial begin
        $dumpfile("testb.vcd");
        //$dumpvars(0, clk);
        $dumpvars(1, MOSI);
        $dumpvars(2, SCLK);
        $dumpvars(3, CS);
        $dumpvars(4, value);
        # 300 $finish;
    end

    vout_spipoti #(8, 0) vout_spipoti1 (
                     .clk (clk),
                     .MOSI (MOSI),
                     .SCLK (SCLK),
                     .CS (CS),
                     .value (value)
                 );

endmodule
