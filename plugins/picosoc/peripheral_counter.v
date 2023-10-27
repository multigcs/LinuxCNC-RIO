
module peripheral_counter (
        input resetn,
        input clk,
        input iomem_valid,
        input [3:0]  iomem_wstrb,
        input [31:0] iomem_addr,
        output reg [31:0] iomem_rdata,
        output reg iomem_ready,
        input [31:0] iomem_wdata
    );

    reg [31:0] counter = 0;

    always @(posedge clk) begin
        if (!resetn) begin
            counter <= 0;
        end else begin
            iomem_ready <= 0;
            if (iomem_valid && !iomem_ready) begin
                iomem_ready <= 1;
                counter <= counter + 1;
                iomem_rdata <= counter;

                if (iomem_wstrb[0]) counter[ 7: 0] <= iomem_wdata[ 7: 0];
                if (iomem_wstrb[1]) counter[15: 8] <= iomem_wdata[15: 8];
                if (iomem_wstrb[2]) counter[23:16] <= iomem_wdata[23:16];
                if (iomem_wstrb[3]) counter[31:24] <= iomem_wdata[31:24];

            end
        end
    end
endmodule

