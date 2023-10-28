
module peripheral_sysclock (
        input resetn,
        input clk,
        input iomem_valid,
        input [3:0]  iomem_wstrb,
        input [31:0] iomem_addr,
        output reg [31:0] iomem_rdata,
        output reg iomem_ready,
        input [31:0] iomem_wdata
    );

    reg [31:0] sysclock = 0;
    reg [31:0] counter = 0;

    always @(posedge clk) begin
        if (!resetn) begin
            sysclock <= 0;
        end else begin
            if (counter == 0) begin
                counter <= `PICOSOC_CLOCK;
                sysclock <= sysclock + 1;
            end else begin
                counter <= counter - 1;
            end

            iomem_ready <= 0;
            if (iomem_valid && !iomem_ready) begin
                iomem_ready <= 1;
                iomem_rdata <= sysclock;
                if (iomem_wstrb[0]) sysclock[ 7: 0] <= iomem_wdata[ 7: 0];
                if (iomem_wstrb[1]) sysclock[15: 8] <= iomem_wdata[15: 8];
                if (iomem_wstrb[2]) sysclock[23:16] <= iomem_wdata[23:16];
                if (iomem_wstrb[3]) sysclock[31:24] <= iomem_wdata[31:24];
            end
        end
    end
endmodule

