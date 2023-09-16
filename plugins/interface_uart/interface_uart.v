
module interface_uart
    #(parameter BUFFER_SIZE=80, parameter MSGID=32'h74697277, parameter TIMEOUT=32'd4800000, parameter ClkFrequency=12000000, parameter Baud=2000000)
    (
        input clk,
        output reg [BUFFER_SIZE-1:0] rx_data,
        input [BUFFER_SIZE-1:0] tx_data,
        output UART_TX,
        input UART_RX
    );

    reg [BUFFER_SIZE-1:0] tx_data_buffer;
    reg [BUFFER_SIZE-1:0] rx_data_buffer;

    reg TxD_start = 0;
    wire TxD_busy;

    reg [7:0] TxD_data;
    wire [7:0] RxD_data;
    wire RxD_data_ready;
    wire RxD_idle;
    wire RxD_endofpacket;

    async_receiver #(ClkFrequency, Baud) uart_rx1 (
        .clk (clk),
        .RxD (UART_RX),
        .RxD_data_ready (RxD_data_ready),
        .RxD_data (RxD_data),
        .RxD_idle (RxD_idle),
        .RxD_endofpacket (RxD_endofpacket)
    );

    async_transmitter #(ClkFrequency, Baud) uart_tx1 (
        .clk (clk),
        .TxD_start (TxD_start),
        .TxD_data (TxD_data),
        .TxD (UART_TX),
        .TxD_busy (TxD_busy)
    );

    reg tx_state = 0;
    reg [7:0] rx_counter = 0;
    reg [7:0] tx_counter = 0;

    always @(posedge clk) begin
        if (RxD_endofpacket == 1) begin
            rx_counter <= 0;
        end else if (tx_state == 1) begin
            if (TxD_busy == 0) begin
                TxD_data <= tx_data_buffer[BUFFER_SIZE-1:BUFFER_SIZE-1-7];
                TxD_start <= 1;
            end else if (TxD_start == 1) begin
                TxD_start <= 0;
                if (tx_counter < BUFFER_SIZE/8-1) begin
                    tx_counter <= tx_counter+1;
                    tx_data_buffer <= {tx_data_buffer[BUFFER_SIZE-1-8:0], 8'd0};
                end else begin
                    tx_state <= 0;
                end
            end
        end else if (RxD_data_ready == 1) begin
            if (rx_counter < BUFFER_SIZE/8-1) begin
                rx_data_buffer <= {rx_data_buffer[BUFFER_SIZE-1-8:0], RxD_data};
                rx_counter <= rx_counter + 1;
            end else begin
                // TODO: check MSGID
                rx_data <= {rx_data_buffer[BUFFER_SIZE-1-8:0], RxD_data};
                rx_counter <= 0;
                tx_counter <= 0;
                tx_data_buffer <= tx_data;
                tx_state <= 1;
            end
        end
    end
endmodule

module async_transmitter(
	input clk,
	input TxD_start,
	input [7:0] TxD_data,
	output TxD,
	output TxD_busy
);

    // Assert TxD_start for (at least) one clock cycle to start transmission of TxD_data
    // TxD_data is latched so that it doesn't have to stay valid while it is being sent

    parameter ClkFrequency = 12000000;
    parameter Baud = 2000000;

    wire BitTick;
    BaudTickGen #(ClkFrequency, Baud) tickgen(.clk(clk), .enable(TxD_busy), .tick(BitTick));

    reg [3:0] TxD_state = 0;
    wire TxD_ready = (TxD_state==0);
    assign TxD_busy = ~TxD_ready;

    reg [7:0] TxD_shift = 0;
    always @(posedge clk)
    begin
        if(TxD_ready & TxD_start)
            TxD_shift <= TxD_data;
        else
        if(TxD_state[3] & BitTick)
            TxD_shift <= (TxD_shift >> 1);

        case(TxD_state)
            4'b0000: if(TxD_start) TxD_state <= 4'b0100;
            4'b0100: if(BitTick) TxD_state <= 4'b1000;  // start bit
            4'b1000: if(BitTick) TxD_state <= 4'b1001;  // bit 0
            4'b1001: if(BitTick) TxD_state <= 4'b1010;  // bit 1
            4'b1010: if(BitTick) TxD_state <= 4'b1011;  // bit 2
            4'b1011: if(BitTick) TxD_state <= 4'b1100;  // bit 3
            4'b1100: if(BitTick) TxD_state <= 4'b1101;  // bit 4
            4'b1101: if(BitTick) TxD_state <= 4'b1110;  // bit 5
            4'b1110: if(BitTick) TxD_state <= 4'b1111;  // bit 6
            4'b1111: if(BitTick) TxD_state <= 4'b0010;  // bit 7
            4'b0010: if(BitTick) TxD_state <= 4'b0011;  // stop1
            4'b0011: if(BitTick) TxD_state <= 4'b0000;  // stop2
            default: if(BitTick) TxD_state <= 4'b0000;
        endcase
    end

    assign TxD = (TxD_state<4) | (TxD_state[3] & TxD_shift[0]);  // put together the start, data and stop bits
endmodule


module async_receiver(
	input clk,
	input RxD,
	output reg RxD_data_ready = 0,
	output reg [7:0] RxD_data = 0,  // data received, valid only (for one clock cycle) when RxD_data_ready is asserted
	// We also detect if a gap occurs in the received stream of characters
	// That can be useful if multiple characters are sent in burst
	//  so that multiple characters can be treated as a "packet"
	output RxD_idle,  // asserted when no data has been received for a while
	output reg RxD_endofpacket = 0  // asserted for one clock cycle when a packet has been detected (i.e. RxD_idle is going high)
);

    parameter ClkFrequency = 12000000;
    parameter Baud = 2000000;

    parameter Oversampling = 8;  // needs to be a power of 2
    // we oversample the RxD line at a fixed rate to capture each RxD data bit at the "right" time
    // 8 times oversampling by default, use 16 for higher quality reception

    reg [3:0] RxD_state = 0;

    wire OversamplingTick;
    BaudTickGen #(ClkFrequency, Baud, Oversampling) tickgen(.clk(clk), .enable(1'b1), .tick(OversamplingTick));

    // synchronize RxD to our clk domain
    reg [1:0] RxD_sync = 2'b11;
    always @(posedge clk) if(OversamplingTick) RxD_sync <= {RxD_sync[0], RxD};

    // and filter it
    reg [1:0] Filter_cnt = 2'b11;
    reg RxD_bit = 1'b1;

    always @(posedge clk)
    if(OversamplingTick)
    begin
        if(RxD_sync[1]==1'b1 && Filter_cnt!=2'b11) Filter_cnt <= Filter_cnt + 1'd1;
        else 
        if(RxD_sync[1]==1'b0 && Filter_cnt!=2'b00) Filter_cnt <= Filter_cnt - 1'd1;

        if(Filter_cnt==2'b11) RxD_bit <= 1'b1;
        else
        if(Filter_cnt==2'b00) RxD_bit <= 1'b0;
    end

    // and decide when is the good time to sample the RxD line
    function integer log2(input integer v); begin log2=0; while(v>>log2) log2=log2+1; end endfunction
    localparam l2o = log2(Oversampling);
    reg [l2o-2:0] OversamplingCnt = 0;
    always @(posedge clk) if(OversamplingTick) OversamplingCnt <= (RxD_state==0) ? 1'd0 : OversamplingCnt + 1'd1;
    wire sampleNow = OversamplingTick && (OversamplingCnt==Oversampling/2-1);

    // now we can accumulate the RxD bits in a shift-register
    always @(posedge clk)
    case(RxD_state)
        4'b0000: if(~RxD_bit) RxD_state <= 4'b0001;  // start bit found?
        4'b0001: if(sampleNow) RxD_state <= 4'b1000;  // sync start bit to sampleNow
        4'b1000: if(sampleNow) RxD_state <= 4'b1001;  // bit 0
        4'b1001: if(sampleNow) RxD_state <= 4'b1010;  // bit 1
        4'b1010: if(sampleNow) RxD_state <= 4'b1011;  // bit 2
        4'b1011: if(sampleNow) RxD_state <= 4'b1100;  // bit 3
        4'b1100: if(sampleNow) RxD_state <= 4'b1101;  // bit 4
        4'b1101: if(sampleNow) RxD_state <= 4'b1110;  // bit 5
        4'b1110: if(sampleNow) RxD_state <= 4'b1111;  // bit 6
        4'b1111: if(sampleNow) RxD_state <= 4'b0010;  // bit 7
        4'b0010: if(sampleNow) RxD_state <= 4'b0000;  // stop bit
        default: RxD_state <= 4'b0000;
    endcase

    always @(posedge clk)
    if(sampleNow && RxD_state[3]) RxD_data <= {RxD_bit, RxD_data[7:1]};

    //reg RxD_data_error = 0;
    always @(posedge clk)
    begin
        RxD_data_ready <= (sampleNow && RxD_state==4'b0010 && RxD_bit);  // make sure a stop bit is received
        //RxD_data_error <= (sampleNow && RxD_state==4'b0010 && ~RxD_bit);  // error if a stop bit is not received
    end

    reg [l2o+1:0] GapCnt = 0;
    always @(posedge clk) if (RxD_state!=0) GapCnt<=0; else if(OversamplingTick & ~GapCnt[log2(Oversampling)+1]) GapCnt <= GapCnt + 1'h1;
    assign RxD_idle = GapCnt[l2o+1];
    always @(posedge clk) RxD_endofpacket <= OversamplingTick & ~GapCnt[l2o+1] & &GapCnt[l2o:0];

endmodule

module BaudTickGen(
	input clk, enable,
	output tick  // generate a tick at the specified baud rate * oversampling
);
    parameter ClkFrequency = 12000000;
    parameter Baud = 2000000;
    parameter Oversampling = 1;

    function integer log2(input integer v); begin log2=0; while(v>>log2) log2=log2+1; end endfunction
    localparam AccWidth = log2(ClkFrequency/Baud)+8;  // +/- 2% max timing error over a byte
    reg [AccWidth:0] Acc = 0;
    localparam ShiftLimiter = log2(Baud*Oversampling >> (31-AccWidth));  // this makes sure Inc calculation doesn't overflow
    localparam Inc = ((Baud*Oversampling << (AccWidth-ShiftLimiter))+(ClkFrequency>>(ShiftLimiter+1)))/(ClkFrequency>>ShiftLimiter);
    always @(posedge clk) if(enable) Acc <= Acc[AccWidth-1:0] + Inc[AccWidth:0]; else Acc <= Inc[AccWidth:0];
    assign tick = Acc[AccWidth];
endmodule
