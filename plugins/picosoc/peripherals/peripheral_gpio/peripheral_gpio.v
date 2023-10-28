
module peripheral_gpio (
        input resetn,
        input clk,
        input iomem_valid,
        input [3:0]  iomem_wstrb,
        input [31:0] iomem_addr,
        output reg [31:0] iomem_rdata,
        output reg iomem_ready,
        input [31:0] iomem_wdata,
        output gpio0,
        output gpio1
    );
    reg [31:0] gpio;
    assign gpio0 = gpio[0];
    assign gpio1 = gpio[1];

    always @(posedge clk) begin
        if (!resetn) begin
            gpio <= 0;
        end else begin
            iomem_ready <= 0;
            if (iomem_valid && !iomem_ready) begin
                iomem_ready <= 1;
                iomem_rdata <= gpio;
                if (iomem_wstrb[0]) gpio[ 7: 0] <= iomem_wdata[ 7: 0];
                if (iomem_wstrb[1]) gpio[15: 8] <= iomem_wdata[15: 8];
                if (iomem_wstrb[2]) gpio[23:16] <= iomem_wdata[23:16];
                if (iomem_wstrb[3]) gpio[31:24] <= iomem_wdata[31:24];
            end
        end
    end
endmodule

