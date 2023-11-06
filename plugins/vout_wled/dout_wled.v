
module dout_wled
    #(parameter CLK_MHZ = 27)
    (
        input clk,
        input green,
        input blue,
        input red,
        output wled
    );

    // Green, Red, Blue
    reg [23:0] rgb_data;

    always @(posedge clk) begin
        if (green) begin
            rgb_data[23:16] <= 255;
        end else begin
            rgb_data[23:16] <= 0;
        end
        if (red) begin
            rgb_data[15:8] <= 255;
        end else begin
            rgb_data[15:8] <= 0;
        end
        if (blue) begin
            rgb_data[7:0] <= 255;
        end else begin
            rgb_data[7:0] <= 0;
        end
    end

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

