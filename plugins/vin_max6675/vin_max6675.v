
module vin_max6675
    #(DIVIDER = 1000)
    (
        input clk,
        input spi_miso,
        output reg spi_sclk = 0,
        output reg spi_cs = 1,
        output reg [15:0] temperature
    );

    reg [15:0] state = 0;
    reg [7:0] data_pos = 0;
    reg [31:0] counter = 0;
    reg [15:0] tmp_data = 0;
    reg mclk = 0;
    always @(posedge clk) begin
        if (counter == 0) begin
            counter <= DIVIDER;
            mclk <= ~mclk;
        end else begin
            counter <= counter - 1;
        end
    end

    always @(posedge mclk) begin
        if (state == 0) begin
            spi_sclk <= 0;
            spi_cs <= 0;
            data_pos <= 0;
            state <= 1;
        end else if (state == 1) begin
            if (spi_sclk == 0) begin
                spi_sclk <= 1;
                tmp_data <= {tmp_data[14:0], spi_miso};
            end else if (data_pos < 15) begin
                spi_sclk <= 0;
                data_pos <= data_pos + 1;
            end else begin
                spi_sclk <= 0;
                temperature <= tmp_data[15:3];
                state <= state + 1;
            end
        end else if (state == 2) begin
            spi_cs <= 1;
            state <= state + 1;
        end else if (state <= 100000) begin
            state <= state + 1;
        end else begin
            state <= 0;
        end
    end



endmodule

