

module vout_wled
    #(parameter CLK_MHZ = 27)
    (
        input clk,
        input [31:0] value,
        output wled
    );

    // Green, Red, Blue
    wire [23:0] rgb_data;
    assign rgb_data = value[23:0];
    reg [7:0] led_num = 0;
    reg write = 1;

    ws2812 #(CLK_MHZ) ws2812a (
        .rgb_data (rgb_data),
        .led_num (led_num),
        .write(write),
        .clk(clk),
        .data(wled)
    );

endmodule

