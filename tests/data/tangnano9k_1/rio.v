/*
    ######### TangNano9K #########
*/

module rio (
        output BLINK_LED,
        input DIN0,
        input DIN1,
        input DIN2,
        input DIN3,
        input DIN4,
        input DIN5,
        input DIN6,
        input DIN7,
        input DIN8,
        input DIN9,
        input DIN10,
        input DIN11,
        input DIN12,
        output DOUT0,
        output DOUT1,
        output DOUT2,
        output DOUT3,
        output ENA,
        output ERROR_OUT,
        output EXPANSION0_SHIFTREG_CLOCK,
        output EXPANSION0_SHIFTREG_LOAD,
        output EXPANSION0_SHIFTREG_OUT,
        input EXPANSION0_SHIFTREG_IN,
        input INTERFACE_SPI_MOSI,
        output INTERFACE_SPI_MISO,
        input INTERFACE_SPI_SCK,
        input INTERFACE_SPI_SSEL,
        output JOINT35_STEPPER_STP,
        output JOINT35_STEPPER_DIR,
        output JOINT36_STEPPER_STP,
        output JOINT36_STEPPER_DIR,
        output JOINT37_STEPPER_STP,
        output JOINT37_STEPPER_DIR,
        output JOINT38_STEPPER_STP,
        output JOINT38_STEPPER_DIR,
        output JOINT39_STEPPER_STP,
        output JOINT39_STEPPER_DIR,
        input sysclk,
        input VIN33_PULSECOUNTER_UP,
        input VIN33_PULSECOUNTER_DOWN,
        output VOUT34_PWM_PWM
    );


    reg ESTOP = 0;
    wire ERROR;
    wire INTERFACE_TIMEOUT;
    assign ERROR = (INTERFACE_TIMEOUT | ESTOP);
    blink #(13500000) blink1 (
        .clk (sysclk),
        .led (BLINK_LED)
    );

    assign ERROR_OUT = ~ERROR;

    parameter BUFFER_SIZE = 248;

    wire[247:0] rx_data;
    wire[247:0] tx_data;

    reg signed [31:0] header_tx;
    always @(posedge sysclk) begin
        if (ESTOP) begin
            header_tx <= 32'h65737470;
        end else begin
            header_tx <= 32'h64617461;
        end
    end



    // expansion_shiftreg
    wire [7:0] EXPANSION0_INPUT;
    wire [7:0] EXPANSION0_OUTPUT;
    wire EXPANSION0_SHIFTREG_OUT_INV;
    assign EXPANSION0_SHIFTREG_OUT = ~EXPANSION0_SHIFTREG_OUT_INV;
    wire EXPANSION0_SHIFTREG_IN_INV;
    assign EXPANSION0_SHIFTREG_IN_INV = ~EXPANSION0_SHIFTREG_IN;
    wire EXPANSION0_SHIFTREG_CLOCK_INV;
    assign EXPANSION0_SHIFTREG_CLOCK = ~EXPANSION0_SHIFTREG_CLOCK_INV;
    wire EXPANSION0_SHIFTREG_LOAD_INV;
    assign EXPANSION0_SHIFTREG_LOAD = ~EXPANSION0_SHIFTREG_LOAD_INV;


    // vout_pwm
    wire VOUT34_PWM_DIR; // fake direction output
    wire DOUT4;
    wire DOUT5;
    wire DOUT6;
    wire DOUT7;
    wire DOUT8;
    wire DOUT9;
    wire DOUT10;
    wire DOUT11;
    wire DIN13;
    wire DIN14;
    wire DIN15;
    wire DIN16;
    wire DIN17;
    wire DIN18;
    wire DIN19;
    wire DIN20;
    wire JOINT0Enable;
    wire JOINT1Enable;
    wire JOINT2Enable;
    wire JOINT3Enable;
    wire JOINT4Enable;
    assign ENA = (JOINT0Enable || JOINT1Enable || JOINT2Enable || JOINT3Enable || JOINT4Enable) && ~ERROR;

    // vouts 1
    wire signed [31:0] VOUT0;

    // vins 1
    wire signed [31:0] VIN0;

    // joints 5
    wire signed [31:0] JOINT0FreqCmd;
    wire signed [31:0] JOINT1FreqCmd;
    wire signed [31:0] JOINT2FreqCmd;
    wire signed [31:0] JOINT3FreqCmd;
    wire signed [31:0] JOINT4FreqCmd;
    wire signed [31:0] JOINT0Feedback;
    wire signed [31:0] JOINT1Feedback;
    wire signed [31:0] JOINT2Feedback;
    wire signed [31:0] JOINT3Feedback;
    wire signed [31:0] JOINT4Feedback;

    // rx_data 248
    wire [31:0] header_rx;
    assign header_rx = {rx_data[223:216], rx_data[231:224], rx_data[239:232], rx_data[247:240]};
    assign JOINT0FreqCmd = {rx_data[191:184], rx_data[199:192], rx_data[207:200], rx_data[215:208]};
    assign JOINT1FreqCmd = {rx_data[159:152], rx_data[167:160], rx_data[175:168], rx_data[183:176]};
    assign JOINT2FreqCmd = {rx_data[127:120], rx_data[135:128], rx_data[143:136], rx_data[151:144]};
    assign JOINT3FreqCmd = {rx_data[95:88], rx_data[103:96], rx_data[111:104], rx_data[119:112]};
    assign JOINT4FreqCmd = {rx_data[63:56], rx_data[71:64], rx_data[79:72], rx_data[87:80]};
    assign VOUT0 = {rx_data[31:24], rx_data[39:32], rx_data[47:40], rx_data[55:48]};
    assign JOINT4Enable = rx_data[20];
    assign JOINT3Enable = rx_data[19];
    assign JOINT2Enable = rx_data[18];
    assign JOINT1Enable = rx_data[17];
    assign JOINT0Enable = rx_data[16];
    assign DOUT0 = ~rx_data[15];
    assign DOUT1 = ~rx_data[14];
    assign DOUT2 = ~rx_data[13];
    assign DOUT3 = ~rx_data[12];
    assign DOUT4 = ~rx_data[11];
    assign DOUT5 = ~rx_data[10];
    assign DOUT6 = ~rx_data[9];
    assign DOUT7 = ~rx_data[8];
    assign DOUT8 = ~rx_data[7];
    assign DOUT9 = ~rx_data[6];
    assign DOUT10 = ~rx_data[5];
    assign DOUT11 = ~rx_data[4];
    // assign DOUTx = rx_data[3];
    // assign DOUTx = rx_data[2];
    // assign DOUTx = rx_data[1];
    // assign DOUTx = rx_data[0];
    // tx_data 248
    assign tx_data = {
        header_tx[7:0], header_tx[15:8], header_tx[23:16], header_tx[31:24],
        JOINT0Feedback[7:0], JOINT0Feedback[15:8], JOINT0Feedback[23:16], JOINT0Feedback[31:24],
        JOINT1Feedback[7:0], JOINT1Feedback[15:8], JOINT1Feedback[23:16], JOINT1Feedback[31:24],
        JOINT2Feedback[7:0], JOINT2Feedback[15:8], JOINT2Feedback[23:16], JOINT2Feedback[31:24],
        JOINT3Feedback[7:0], JOINT3Feedback[15:8], JOINT3Feedback[23:16], JOINT3Feedback[31:24],
        JOINT4Feedback[7:0], JOINT4Feedback[15:8], JOINT4Feedback[23:16], JOINT4Feedback[31:24],
        VIN0[7:0], VIN0[15:8], VIN0[23:16], VIN0[31:24],
        DIN0, DIN1, DIN2, DIN3, DIN4, DIN5, DIN6, DIN7, DIN8, DIN9, DIN10, DIN11, DIN12, DIN13, DIN14, DIN15, DIN16, DIN17, DIN18, DIN19, DIN20, 1'd0, 1'd0, 1'd0
    };
    assign DIN13 = EXPANSION0_INPUT[0];
    assign DIN14 = EXPANSION0_INPUT[1];
    assign DIN15 = EXPANSION0_INPUT[2];
    assign DIN16 = EXPANSION0_INPUT[3];
    assign DIN17 = EXPANSION0_INPUT[4];
    assign DIN18 = EXPANSION0_INPUT[5];
    assign DIN19 = EXPANSION0_INPUT[6];
    assign DIN20 = EXPANSION0_INPUT[7];
    assign EXPANSION0_OUTPUT = {DOUT11, DOUT10, DOUT9, DOUT8, DOUT7, DOUT6, DOUT5, DOUT4};

    // interface_spislave
    interface_spislave #(BUFFER_SIZE, 32'h74697277, 32'd6750000) spi1 (
        .clk (sysclk),
        .SPI_SCK (INTERFACE_SPI_SCK),
        .SPI_SSEL (INTERFACE_SPI_SSEL),
        .SPI_MOSI (INTERFACE_SPI_MOSI),
        .SPI_MISO (INTERFACE_SPI_MISO),
        .rx_data (rx_data),
        .tx_data (tx_data),
        .pkg_timeout (INTERFACE_TIMEOUT)
    );

    // expansion_shiftreg
    wire [7:0] EXPANSION0_INPUT_RAW;
    assign EXPANSION0_INPUT = EXPANSION0_INPUT_RAW;
    wire [7:0] EXPANSION0_OUTPUT_RAW;
    assign EXPANSION0_OUTPUT_RAW = EXPANSION0_OUTPUT;
    expansion_shiftreg #(8, 135) expansion_shiftreg0 (
       .clk (sysclk),
       .SHIFT_OUT (EXPANSION0_SHIFTREG_OUT_INV),
       .SHIFT_IN (EXPANSION0_SHIFTREG_IN_INV),
       .SHIFT_CLK (EXPANSION0_SHIFTREG_CLOCK_INV),
       .SHIFT_LOAD (EXPANSION0_SHIFTREG_LOAD_INV),
       .data_in (EXPANSION0_INPUT_RAW),
       .data_out (EXPANSION0_OUTPUT_RAW)
    );

    // vout_pwm
    vout_pwm #(2700) vout_pwm34 (
        .clk (sysclk),
        .dty (VOUT0),
        .disabled (ERROR),
        .dir (VOUT34_PWM_DIR),
        .pwm (VOUT34_PWM_PWM)
    );

    // vin_pulsecounter
    vin_pulsecounter vin_pulsecounter33 (
        .clk (sysclk),
        .counter (VIN0),
        .UP (VIN33_PULSECOUNTER_UP),
        .DOWN (VIN33_PULSECOUNTER_DOWN),
        .RESET (1'd0)
    );

    // joint_stepper
    joint_stepper joint_stepper35 (
        .clk (sysclk),
        .jointEnable (JOINT0Enable && !ERROR),
        .jointFreqCmd (JOINT0FreqCmd),
        .jointFeedback (JOINT0Feedback),
        .DIR (JOINT35_STEPPER_DIR),
        .STP (JOINT35_STEPPER_STP)
    );
    joint_stepper joint_stepper36 (
        .clk (sysclk),
        .jointEnable (JOINT1Enable && !ERROR),
        .jointFreqCmd (JOINT1FreqCmd),
        .jointFeedback (JOINT1Feedback),
        .DIR (JOINT36_STEPPER_DIR),
        .STP (JOINT36_STEPPER_STP)
    );
    joint_stepper joint_stepper37 (
        .clk (sysclk),
        .jointEnable (JOINT2Enable && !ERROR),
        .jointFreqCmd (JOINT2FreqCmd),
        .jointFeedback (JOINT2Feedback),
        .DIR (JOINT37_STEPPER_DIR),
        .STP (JOINT37_STEPPER_STP)
    );
    joint_stepper joint_stepper38 (
        .clk (sysclk),
        .jointEnable (JOINT3Enable && !ERROR),
        .jointFreqCmd (JOINT3FreqCmd),
        .jointFeedback (JOINT3Feedback),
        .DIR (JOINT38_STEPPER_DIR),
        .STP (JOINT38_STEPPER_STP)
    );
    joint_stepper joint_stepper39 (
        .clk (sysclk),
        .jointEnable (JOINT4Enable && !ERROR),
        .jointFreqCmd (JOINT4FreqCmd),
        .jointFeedback (JOINT4Feedback),
        .DIR (JOINT39_STEPPER_DIR),
        .STP (JOINT39_STEPPER_STP)
    );
endmodule
