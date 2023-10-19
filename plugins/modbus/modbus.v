
module modbus
    #(parameter ClkFrequency=12000000, parameter Baud=9600)
    (
        input clk,
        input rx,
        output reg tx,
        output wire tx_en,
        output reg [71:0] data_in,
        input wire [71:0] data_out
    );

    wire RxD_data_ready;
    wire RxD_idle;
    wire RxD_endofpacket;
    reg [7:0] RxD_package [7:0];
    reg [7:0] RxD_data;
    reg [3:0] RxD_counter = 0;

    uart_rx #(ClkFrequency, Baud) rx1 (
        .clk (clk),
        .RxD (rx),
        .RxD_data_ready (RxD_data_ready),
        .RxD_data (RxD_data),
        .RxD_idle (RxD_idle),
        .RxD_endofpacket (RxD_endofpacket)
    );


    always @(posedge clk) begin
        if (RxD_endofpacket == 1) begin
            data_in[7:0] <= {4'd0, RxD_counter};
            data_in[15:8] <= RxD_package[0];
            data_in[23:16] <= RxD_package[1];
            data_in[31:24] <= RxD_package[2];
            data_in[39:32] <= RxD_package[3];
            data_in[47:40] <= RxD_package[4];
            data_in[55:48] <= RxD_package[5];
            data_in[63:56] <= RxD_package[6];
            data_in[71:64] <= RxD_package[7];
            RxD_counter <= 0;

        end else if (RxD_data_ready == 1) begin
            if (RxD_counter < 8) begin
                RxD_package[RxD_counter] <= RxD_data;
                RxD_counter <= RxD_counter + 1;
            end

        end

    end

    reg [71:0] data_out_tmp;

    reg TxD_start = 0;
    wire TxD_busy;
    reg [7:0] TxD_data = 0;
    reg [3:0] TxD_counter = 0;
    wire [3:0] TxD_len;
    wire [7:0] TxD_package [7:0];
    assign tx_en = TxD_busy;
    assign TxD_len = data_out_tmp[3:0];
    assign TxD_package[0] = data_out_tmp[15:8];
    assign TxD_package[1] = data_out_tmp[23:16];
    assign TxD_package[2] = data_out_tmp[31:24];
    assign TxD_package[3] = data_out_tmp[39:32];
    assign TxD_package[4] = data_out_tmp[47:40];
    assign TxD_package[5] = data_out_tmp[55:48];
    assign TxD_package[6] = data_out_tmp[63:56];
    assign TxD_package[7] = data_out_tmp[71:64];

    uart_tx #(ClkFrequency, Baud) tx1 (
        .clk (clk),
        .TxD_start (TxD_start),
        .TxD_data (TxD_data),
        .TxD (tx),
        .TxD_busy (TxD_busy)
    );

    always @(posedge clk) begin
        if ( data_out[3:0] > 0) begin
            data_out_tmp <= data_out;
        end
        if (TxD_busy == 0) begin
            if (TxD_start == 0) begin
                if (TxD_counter < TxD_len) begin
                    TxD_start <= 1;
                    TxD_data <= TxD_package[TxD_counter];
                    TxD_counter <= TxD_counter + 1;
                end else if (TxD_len != 0) begin
                    // wait
                    data_out_tmp[3:0] <= 0;
                end else begin
                    // next package
                    TxD_counter <= 0;
                end
            end
        end else begin
            TxD_start <= 0;
        end
    end

endmodule

