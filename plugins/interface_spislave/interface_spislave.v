
module interface_spislave
    #(parameter BUFFER_SIZE=64, parameter MSGID=32'h74697277, parameter TIMEOUT=32'd4800000)
     (
         input clk,
         input SPI_SCK,
         input SPI_SSEL,
         input SPI_MOSI,
         input [BUFFER_SIZE-1:0] tx_data,
         output [BUFFER_SIZE-1:0] rx_data,
         output SPI_MISO,
         output pkg_timeout
         //output [15:0] counter
     );
    reg [31:0] timeout_counter = 0;
    //assign counter = bitcnt;
    reg[2:0] SCKr;  always @(posedge clk) SCKr <= {SCKr[1:0], SPI_SCK};
    wire SCK_risingedge = (SCKr[2:1]==2'b01);  // now we can detect SCK rising edges
    wire SCK_fallingedge = (SCKr[2:1]==2'b10);  // and falling edges
    reg[2:0] SSELr;  always @(posedge clk) SSELr <= {SSELr[1:0], SPI_SSEL};
    wire SSEL_active = ~SSELr[1];  // SSEL is active low
    wire SSEL_startmessage = (SSELr[2:1]==2'b10);  // message starts at falling edge
    wire SSEL_endmessage = (SSELr[2:1]==2'b01);  // message stops at rising edge
    reg[15:0] bitcnt;
    reg[BUFFER_SIZE-1:0] byte_data_received;
    reg[BUFFER_SIZE-1:0] byte_data_receive;
    reg[BUFFER_SIZE-1:0] byte_data_sent;
    reg timeout = 1;
    assign pkg_timeout = timeout;
    assign rx_data = byte_data_received;
    always @(posedge clk) begin
        if(~SSEL_active) begin
            bitcnt <= 16'd0;
        end else begin
            if(SCK_risingedge) begin
                bitcnt <= bitcnt + 16'd1;
                byte_data_receive <= {byte_data_receive[BUFFER_SIZE-2:0], SPI_MOSI};
            end
        end
    end
    always @(posedge clk) begin
        if (SSEL_endmessage) begin
            if (byte_data_receive[BUFFER_SIZE-1:BUFFER_SIZE-32] == MSGID) begin
                byte_data_received <= byte_data_receive;
                timeout_counter <= 0;
            end
        end else if (timeout_counter < TIMEOUT) begin
            timeout_counter <= timeout_counter + 1;
            timeout <= 0;
        end else begin
            timeout <= 1;
        end
    end
    always @(posedge clk) begin
        if(SSEL_active) begin
            if(SSEL_startmessage) begin
                byte_data_sent <= tx_data;
            end else begin
                if(SCK_fallingedge) begin
                    if(bitcnt==16'd0)
                        byte_data_sent <= 0;  // after that, we send 0s
                    else
                        byte_data_sent <= {byte_data_sent[BUFFER_SIZE-2:0], 1'b0};
                end
            end
        end
    end
    assign SPI_MISO = byte_data_sent[BUFFER_SIZE-1];  // send MSB first
endmodule
