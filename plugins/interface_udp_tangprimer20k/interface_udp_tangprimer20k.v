

module interface_udp_tangprimer20k
    #(parameter BUFFER_SIZE=80, parameter MSGID=32'h74697277, parameter MAC={8'h06,8'h00,8'hAA,8'hBB,8'h0C,8'hDD}, parameter IP={8'd192,8'd168,8'd10,8'd14})
    (
        input sysclk,
        output reg [BUFFER_SIZE-1:0] rx_data,
        input [BUFFER_SIZE-1:0] tx_data,
        output phyrst,
        input netrmii_clk50m,
        input netrmii_rx_crs,
        output netrmii_mdc,
        output netrmii_txen,
        inout netrmii_mdio,
        output netrmii_txd_0,
        output netrmii_txd_1,
        input netrmii_rxd_0,
        input netrmii_rxd_1
    );

    reg soft_rst = 0;
    reg [31:0] rst_counter = 0;
    always @(posedge sysclk) begin
        if (rst_counter < 27000000) begin
            rst_counter <= rst_counter + 1;
        end else begin
            soft_rst <= 1;
        end
    end

    reg [BUFFER_SIZE-1:0] tx_data_buffer;
    reg [BUFFER_SIZE-1:0] rx_data_buffer;

    logic clk1m;
    logic clk6m;
    PLL_6M PLL6m(
        .clkout(clk6m),
        .clkoutd(clk1m),
        .clkin(sysclk)
    );

    logic clk50m;
    logic ready;

    logic eth_rx_head_av;
    logic[31:0] eth_rx_head;
    logic eth_rx_data_av;
    logic[7:0] eth_rx_data;
    logic eth_rx_head_rdy;

    logic [31:0] eth_tx_ip;
    logic [15:0] eth_tx_dst_port;
    logic eth_tx_req;
    logic [7:0] eth_tx_data;
    logic eth_tx_data_av;
    logic eth_tx_req_rdy;
    logic eth_tx_data_rdy;

    udp #(
        .ip_adr(IP),
        .mac_adr(MAC),

        .arp_refresh_interval(50000000*15), // 15 seconds    
        .arp_max_life_time(50000000*30) // 30 seconds
    )udp_inst(
        .clk1m(clk1m),
        .rst(soft_rst),
        .clk50m(clk50m),
        .ready(ready),
        .netrmii_clk50m(netrmii_clk50m),
        .netrmii_rx_crs(netrmii_rx_crs),
        .netrmii_mdc(netrmii_mdc),
        .netrmii_txen(netrmii_txen),
        .netrmii_mdio(netrmii_mdio),
        .netrmii_txd({netrmii_txd_1, netrmii_txd_0}),
        .netrmii_rxd({netrmii_rxd_1, netrmii_rxd_0}),
        .phyrst(phyrst),

        .rx_head_rdy_i(eth_rx_head_rdy),
        .rx_head_av_o(eth_rx_head_av),
        .rx_head_o(eth_rx_head),
        .rx_data_rdy_i(1'b1),
        .rx_data_av_o(eth_rx_data_av),
        .rx_data_o(eth_rx_data),

        .tx_ip_i(eth_tx_ip),
        .tx_src_port_i(16'd11451),
        .tx_dst_port_i(eth_tx_dst_port),
        .tx_req_i(eth_tx_req),
        .tx_data_i(eth_tx_data),
        .tx_data_av_i(eth_tx_data_av),
        .tx_req_rdy_o(eth_tx_req_rdy),
        .tx_data_rdy_o(eth_tx_data_rdy)
    );

    reg [7:0] eth_rx_state = 0;
    reg [7:0] eth_tx_state = 0;
    reg [7:0] eth_rx_counter = 0;
    reg [7:0] eth_tx_counter = 0;

    always_ff@(posedge clk50m or negedge ready)begin
        if (ready == 0) begin
            eth_tx_state <= 0;
            eth_rx_state <= 0;
            eth_tx_req <= 0;
        end else begin

            // receive
            case(eth_rx_state)
                0:begin
                    // wait for header
                    if (eth_rx_head_av) begin
                        eth_rx_head_rdy <= 1'b1;
                        eth_rx_counter <= 0;
                        eth_rx_state <= eth_rx_state + 1;
                    end else begin
                        eth_rx_head_rdy <= 1'b0;
                    end
                end
                1:begin
                    // read ip from header
                    eth_tx_ip <= eth_rx_head;
                    eth_rx_state <= eth_rx_state + 1;
                end
                2:begin
                    // read ??? from header
                    eth_rx_state <= eth_rx_state + 1;
                end
                3:begin
                    // read port from header
                    if (eth_rx_head[15:0] == 16'd2390) begin
                        eth_tx_dst_port <= eth_rx_head[31:16];
                        eth_rx_state <= eth_rx_state + 1;
                    end else begin
                        eth_rx_state <= 0;
                    end
                end
                4:begin
                    if (eth_rx_data_av) begin
                        // receive data
                        rx_data_buffer <= {rx_data_buffer[BUFFER_SIZE-1-8:0], eth_rx_data};
                        eth_rx_counter <= eth_rx_counter + 1;
                    end else begin
                        // check and save data
                        // if (eth_rx_counter == BUFFER_SIZE && header) begin
                        
                        // if (rx_data_buffer[BUFFER_SIZE-1:BUFFER_SIZE-32] == MSGID) begin
                        //     rx_data <= rx_data_buffer;
                        //     eth_rx_state <= eth_rx_state + 1;
                        // end

                        rx_data <= rx_data_buffer;
                        eth_rx_state <= eth_rx_state + 1;
 
                    end
                end
                5:begin
                    // receive done
                    eth_rx_state <= 0;
                end
            endcase


            // transmit
            case(eth_tx_state)
                0:begin
                    // wait for tx ready
                    if (eth_tx_req_rdy) begin
                        // wait for rx received
                        if (eth_rx_state == 5) begin
                            // set data to transmit
                            eth_tx_counter <= 0;
                            tx_data_buffer <= tx_data;
                            eth_tx_state <= eth_tx_state + 1;
                        end
                    end
                end
                1:begin
                    // send data
                    if (eth_tx_counter <= BUFFER_SIZE-1) begin
                        eth_tx_data_av <= 1;
                        eth_tx_data <= tx_data_buffer[BUFFER_SIZE-1:BUFFER_SIZE-1-7];
                        tx_data_buffer <= {tx_data_buffer[BUFFER_SIZE-1-8:0], 8'd0};
                        eth_tx_counter = eth_tx_counter + 1;
                    end else begin
                        eth_tx_data_av <= 0;
                        eth_tx_state <= eth_tx_state + 1;
                    end
                end
                2:begin
                    // start transmit
                    if (eth_tx_req_rdy) begin
                        eth_tx_req <= 1'b1;
                        eth_tx_state <= eth_tx_state + 1;
                    end
                end
                3:begin
                    // transmit done
                    eth_tx_req <= 1'b0;
                    eth_tx_state <= 0;
                end
                default:begin
                    eth_tx_state <= eth_tx_state + 1;
                end
            endcase
        end
    end

endmodule
