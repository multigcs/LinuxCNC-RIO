
module peripheral (
        input resetn,
        input clk,
        input iomem_valid,
        input [3:0]  iomem_wstrb,
        input [31:0] iomem_addr,
        output [31:0] iomem_rdata,
        output iomem_ready,
        input [31:0] iomem_wdata,
        output [31:0] gpio
    );

    // GPIO mapped to 0x03xx_xxxx
    wire gpio_en = (iomem_addr[31:24] == 8'h03);
    wire [31:0] gpio_iomem_rdata;
    wire gpio_iomem_ready;
    peripheral_gpio gpio1 (
        .clk(clk),
        .resetn(resetn),
        .iomem_ready(gpio_iomem_ready),
        .iomem_rdata(gpio_iomem_rdata),
        .iomem_valid(iomem_valid && gpio_en),
        .iomem_wstrb(iomem_wstrb),
        .iomem_addr(iomem_addr),
        .iomem_wdata(iomem_wdata),
        .gpio(gpio)
    );


    // COUNTER mapped to 0x04xx_xxxx
    wire counter_en = (iomem_addr[31:24] == 8'h04);
    wire [31:0] counter_iomem_rdata;
    wire counter_iomem_ready;
    peripheral_counter counter1 (
        .clk(clk),
        .resetn(resetn),
        .iomem_ready(counter_iomem_ready),
        .iomem_rdata(counter_iomem_rdata),
        .iomem_valid(iomem_valid && counter_en),
        .iomem_wstrb(iomem_wstrb),
        .iomem_addr(iomem_addr),
        .iomem_wdata(iomem_wdata)
    );

    assign iomem_ready = gpio_en ? gpio_iomem_ready : counter_en ? counter_iomem_ready : 1'b0;
    assign iomem_rdata = gpio_iomem_ready ? gpio_iomem_rdata : counter_iomem_ready ? counter_iomem_rdata : 32'h0;

endmodule

