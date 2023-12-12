`timescale 1 ns/10 ps


module testb;
    reg clk = 0;
    always #2 clk = !clk;

    wire SPI_MISO;
    reg SPI_MOSI = 0;
    reg SPI_SCK = 0;
    reg SPI_SSEL = 1;
    reg DIN0 = 0;
    wire DOUT0;
    wire pkg_timeout;

    //wire [15:0] counter;
    always #10 SPI_SCK = !SPI_SCK;
    always #40 SPI_MOSI = !SPI_MOSI;
    always #60 SPI_MOSI = !SPI_MOSI;

    initial begin
        $dumpfile("testb.vcd");
        $dumpvars(0, clk);
        $dumpvars(1, SPI_MISO);
        $dumpvars(2, SPI_MOSI);
        $dumpvars(3, SPI_SCK);
        $dumpvars(4, SPI_SSEL);
        $dumpvars(5, jointFreqCmd0);
        $dumpvars(6, setPoint0);
        $dumpvars(7, rx_data);
        $dumpvars(8, tx_data);
        $dumpvars(9, pkg_timeout);
        //$dumpvars(10, counter);

        #100
         SPI_MOSI = 0;
        #5
         SPI_SSEL = 0;
        #1920
         //$display("counter = %d", counter);
         SPI_SSEL = 1;
        #100
         $display("-------");
        $display("(%d) rx_data = %h", (rx_data == 96'h17a17a17a17a17a17a17a17a), rx_data);
        $display("(%d) jointFreqCmd0 = %h", (jointFreqCmd0 == 32'ha1177aa1), jointFreqCmd0);
        $display("(%d) setPoint0 = %h", (setPoint0 == 32'h177a), setPoint0);
        $display("pkg_timeout = %h", pkg_timeout);
        $display("-------");

        #1000 $finish;
    end

    parameter BUFFER_SIZE = 96;

    wire[95:0] rx_data;
    wire[95:0] tx_data;
    reg signed [31:0] header_tx = 32'h64617461;

    wire jointEnable0;

    // fake din's to fit byte
    reg DIN1 = 1;
    reg DIN2 = 0;
    reg DIN3 = 1;
    reg DIN4 = 0;
    reg DIN5 = 1;
    reg DIN6 = 0;
    reg DIN7 = 1;

    // vouts 1
    wire [15:0] setPoint0;

    // vins 0

    // joints 1
    wire signed [31:0] jointFreqCmd0;
    reg signed [31:0] jointFeedback0 = 35000;

    // rx_data 96
    wire [31:0] header_rx;
    assign header_rx = {rx_data[71:64], rx_data[79:72], rx_data[87:80], rx_data[95:88]};
    assign jointFreqCmd0 = {rx_data[39:32], rx_data[47:40], rx_data[55:48], rx_data[63:56]};
    assign setPoint0 = {rx_data[23:16], rx_data[31:24]};
    assign jointEnable0 = rx_data[15];
    assign DOUT0 = rx_data[0];

    // tx_data 72
    assign tx_data = {
               header_tx[7:0], header_tx[15:8], header_tx[23:16], header_tx[31:24],
               jointFeedback0[7:0], jointFeedback0[15:8], jointFeedback0[23:16], jointFeedback0[31:24],
               DIN7,
               DIN6,
               DIN5,
               DIN4,
               DIN3,
               DIN2,
               DIN1,
               DIN0,
               24'd0
           };

    interface_spislave #(BUFFER_SIZE, 32'h17a17a17) interface_spislave1 (
                           .clk (clk),
                           .SPI_SCK (SPI_SCK),
                           .SPI_SSEL (SPI_SSEL),
                           .SPI_MOSI (SPI_MOSI),
                           .SPI_MISO (SPI_MISO),
                           .rx_data (rx_data),
                           .tx_data (tx_data),
                           .pkg_timeout (pkg_timeout)
                           //.counter (counter)
                       );
endmodule
