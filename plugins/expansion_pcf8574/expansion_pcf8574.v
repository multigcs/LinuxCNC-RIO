
module expansion_pcf8574
    #(
        parameter ADDR = 8'h40,
        parameter DEVICES = 1
    )
    (
       input clk,
       inout i2cSda,
       output i2cScl,
       output reg [(DEVICES*8)-1:0] data_in = 0,
       input wire [(DEVICES*8)-1:0] data_out
    );

    localparam STATE_TRIGGER_TRX = 0;
    localparam STATE_WAIT_FOR_START = 1;
    localparam STATE_SAVE_VALUE_WHEN_READY = 2;

    localparam DEV1 = (DEVICES > 1) ? 15 : 7;
    localparam DEV2 = (DEVICES > 2) ? 23 : 7;
    localparam DEV3 = (DEVICES > 3) ? 31 : 7;

    wire [1:0] i2cInstruction;
    wire [7:0] i2cByteToSend;
    wire [7:0] i2cByteReceived;
    wire i2cComplete;
    wire i2cEnable;
    wire sdaIn;
    wire sdaOut;
    wire isSending;
    assign i2cSda = (isSending & ~sdaOut) ? 1'b0 : 1'bz;
    assign sdaIn = i2cSda ? 1'b1 : 1'b0;
    reg [2:0] drawState = 0;
    wire [7:0] ioeInputData;
    reg [7:0] ioeOutputData = 0;
    wire ioeDataReady;
    reg ioeEnable = 0;

    // TODO: clock setup via param
    reg [2:0] clk_cnt = 0;
    wire clk_slow;
    assign clk_slow = clk_cnt[2];

    reg [3:0] device = 0;
    reg [7:0] address = 0;

    pcf8574_i2c i2c(
        clk_slow,
        sdaIn,
        sdaOut,
        isSending,
        i2cScl,
        i2cInstruction,
        i2cEnable,
        i2cByteToSend,
        i2cByteReceived,
        i2cComplete
    );

    pcf8574_ioe ioe
    (
        clk_slow,
        address,
        ioeInputData,
        ioeOutputData,
        ioeDataReady,
        ioeEnable,
        i2cInstruction,
        i2cEnable,
        i2cByteToSend,
        i2cByteReceived,
        i2cComplete
    );

    always @(posedge clk) begin
        clk_cnt = clk_cnt + 1;
    end

    always @(posedge clk_slow) begin
        case (drawState)
            STATE_TRIGGER_TRX: begin
                ioeEnable <= 1;
                drawState <= STATE_WAIT_FOR_START;
                case (device)
                    0: ioeOutputData <= data_out[7:0];
                    1: ioeOutputData <= data_out[DEV1:DEV1-7];
                    2: ioeOutputData <= data_out[DEV2:DEV2-7];
                    3: ioeOutputData <= data_out[DEV3:DEV3-7];
                endcase
                address <= ADDR + {device, 1'd0};
            end
            STATE_WAIT_FOR_START: begin
                if (~ioeDataReady) begin
                    drawState <= STATE_SAVE_VALUE_WHEN_READY;
                end
            end
            STATE_SAVE_VALUE_WHEN_READY: begin
                if (ioeDataReady) begin
                    drawState <= STATE_TRIGGER_TRX;
                    case (device)
                        0: data_in[7:0] <= ioeInputData;
                        1: data_in[DEV1:DEV1-7] <= ioeInputData;
                        2: data_in[DEV2:DEV2-7] <= ioeInputData;
                        3: data_in[DEV3:DEV3-7] <= ioeInputData;
                    endcase
                    if (device < DEVICES - 1) begin
                        device <= device + 1;
                    end else begin
                        device <= 0;
                    end
                    ioeEnable <= 0;
                end
            end
        endcase
    end
endmodule

module pcf8574_ioe
    (
        input clk,
        input wire [7:0] address,
        output reg [7:0] inputData,
        input wire [7:0] outputData,
        output reg dataReady = 1,
        input enable,
        output reg [1:0] instructionI2C = 0,
        output reg enableI2C = 0,
        output reg [7:0] byteToSendI2C = 0,
        input [7:0] byteReceivedI2C,
        input completeI2C
    );

    localparam PAUSE = 8'd5;
    localparam INST_START_TX = 0;
    localparam INST_STOP_TX = 1;
    localparam INST_READ_BYTE = 2;
    localparam INST_WRITE_BYTE = 3;

    localparam STATE_IDLE = 0;
    localparam STATE_RUN_TASK = 1;
    localparam STATE_WAIT_FOR_I2C = 2;
    localparam STATE_INC_TASK = 3;
    localparam STATE_DONE = 4;
    localparam STATE_DELAY = 5;

    reg [7:0] taskIndex = 0;
    reg [4:0] state = STATE_IDLE;
    reg [7:0] counter = 0;
    reg processStarted = 0;

    always @(posedge clk) begin
        case (state)
            STATE_IDLE: begin
                if (enable) begin
                    state <= STATE_RUN_TASK;
                    taskIndex <= 0;
                    dataReady <= 0;
                    counter <= 0;
                end
            end
            STATE_RUN_TASK: begin
                case (taskIndex)

                    // set outputs
                    0: begin
                        instructionI2C <= INST_START_TX;
                        enableI2C <= 1;
                        state <= STATE_WAIT_FOR_I2C;
                    end
                    2: begin
                        instructionI2C <= INST_WRITE_BYTE;
                        byteToSendI2C <= address;
                        enableI2C <= 1;
                        state <= STATE_WAIT_FOR_I2C;
                    end
                    4: begin
                        instructionI2C <= INST_WRITE_BYTE;
                        byteToSendI2C <= outputData;
                        enableI2C <= 1;
                        state <= STATE_WAIT_FOR_I2C;
                    end
                    6: begin
                        instructionI2C <= INST_STOP_TX;
                        enableI2C <= 1;
                        state <= STATE_WAIT_FOR_I2C;
                    end

                    // get inputs
                    10: begin
                        instructionI2C <= INST_START_TX;
                        enableI2C <= 1;
                        state <= STATE_WAIT_FOR_I2C;
                    end
                    12: begin
                        instructionI2C <= INST_WRITE_BYTE;
                        byteToSendI2C <= address + 1;
                        enableI2C <= 1;
                        state <= STATE_WAIT_FOR_I2C;
                    end
                    14: begin
                        instructionI2C <= INST_READ_BYTE;
                        enableI2C <= 1;
                        state <= STATE_WAIT_FOR_I2C;
                    end
                    16: begin
                        instructionI2C <= INST_STOP_TX;
                        inputData <= byteReceivedI2C;
                        enableI2C <= 1;
                        state <= STATE_WAIT_FOR_I2C;
                    end

                    18: begin
                        instructionI2C <= INST_STOP_TX;
                        enableI2C <= 1;
                        state <= STATE_WAIT_FOR_I2C;
                    end

                    default:
                        state <= STATE_DELAY;
                endcase
            end
            STATE_WAIT_FOR_I2C: begin
                if (~processStarted && ~completeI2C) begin
                    processStarted <= 1;
                end else if (completeI2C && processStarted) begin
                    //state <= STATE_INC_TASK;
                    state <= STATE_DELAY;
                    processStarted <= 0;
                    enableI2C <= 0;
                end
            end
            STATE_INC_TASK: begin
                state <= STATE_RUN_TASK;
                if (taskIndex == 200) begin
                    state <= STATE_DONE;
                end else begin
                    taskIndex <= taskIndex + 1;
                end
            end
            STATE_DELAY: begin
                if (counter == PAUSE) begin
                    state <= STATE_INC_TASK;
                    counter <= 8'd0;
                end else begin
                    counter <= counter + 8'd1;
                end
            end
            STATE_DONE: begin
                dataReady <= 1;
                if (~enable) begin
                    state <= STATE_IDLE;
                end
            end
        endcase
    end

endmodule



module pcf8574_i2c (
        input clk,
        input sdaIn,
        output reg sdaOutReg = 1,
        output reg isSending = 0,
        output reg scl = 1,
        input [1:0] instruction,
        input enable,
        input [7:0] byteToSend,
        output reg [7:0] byteReceived = 0,
        output reg complete
    );
    localparam INST_START_TX = 0;
    localparam INST_STOP_TX = 1;
    localparam INST_READ_BYTE = 2;
    localparam INST_WRITE_BYTE = 3;
    localparam STATE_IDLE = 4;
    localparam STATE_DONE = 5;
    localparam STATE_SEND_ACK = 6;
    localparam STATE_RCV_ACK = 7;

    reg [6:0] clockDivider = 0;
    reg [2:0] state = STATE_IDLE;
    reg [2:0] bitToSend = 0;


    always @(posedge clk) begin
        case (state)
            STATE_IDLE: begin
                if (enable) begin
                    complete <= 0;
                    clockDivider <= 0;
                    bitToSend <= 0;
                    state <= {1'b0,instruction};
                end
            end
            INST_START_TX: begin
                isSending <= 1;
                clockDivider <= clockDivider + 7'd1;
                if (clockDivider[6:5] == 2'b00) begin
                    scl <= 1;
                    sdaOutReg <= 1;
                end else if (clockDivider[6:5] == 2'b01) begin
                    sdaOutReg <= 0;
                end else if (clockDivider[6:5] == 2'b10) begin
                    scl <= 0;
                end else if (clockDivider[6:5] == 2'b11) begin
                    state <= STATE_DONE;
                end
            end
            INST_STOP_TX: begin
                isSending <= 1;
                clockDivider <= clockDivider + 7'd1;
                if (clockDivider[6:5] == 2'b00) begin
                    scl <= 0;
                    sdaOutReg <= 0;
                end else if (clockDivider[6:5] == 2'b01) begin
                    scl <= 1;
                end else if (clockDivider[6:5] == 2'b10) begin
                    sdaOutReg <= 1;
                end else if (clockDivider[6:5] == 2'b11) begin
                    state <= STATE_DONE;
                end
            end
            INST_READ_BYTE: begin
                isSending <= 0;
                clockDivider <= clockDivider + 7'd1;
                if (clockDivider[6:5] == 2'b00) begin
                    scl <= 0;
                end else if (clockDivider[6:5] == 2'b01) begin
                    scl <= 1;
                end else if (clockDivider == 7'b1000000) begin
                    byteReceived <= {byteReceived[6:0], sdaIn ? 1'b1 : 1'b0};
                end else if (clockDivider == 7'b1111111) begin
                    bitToSend <= bitToSend + 3'd1;
                    if (bitToSend == 3'b111) begin
                        state <= STATE_SEND_ACK;
                    end
                end else if (clockDivider[6:5] == 2'b11) begin
                    scl <= 0;
                end
            end
            STATE_SEND_ACK: begin
                isSending <= 1;
                sdaOutReg <= 0;
                clockDivider <= clockDivider + 7'd1;
                if (clockDivider[6:5] == 2'b01) begin
                    scl <= 1;
                end else if (clockDivider == 7'b1111111) begin
                    state <= STATE_DONE;
                end else if (clockDivider[6:5] == 2'b11) begin
                    scl <= 0;
                end
            end
            INST_WRITE_BYTE: begin
                isSending <= 1;
                clockDivider <= clockDivider + 7'd1;
                sdaOutReg <= byteToSend[3'd7-bitToSend] ? 1'b1 : 1'b0;

                if (clockDivider[6:5] == 2'b00) begin
                    scl <= 0;
                end else if (clockDivider[6:5] == 2'b01) begin
                    scl <= 1;
                end else if (clockDivider == 7'b1111111) begin
                    bitToSend <= bitToSend + 3'd1;
                    if (bitToSend == 3'b111) begin
                        state <= STATE_RCV_ACK;
                    end
                end else if (clockDivider[6:5] == 2'b11) begin
                    scl <= 0;
                end
            end
            STATE_RCV_ACK: begin
                isSending <= 0;
                clockDivider <= clockDivider + 7'd1;

                if (clockDivider[6:5] == 2'b01) begin
                    scl <= 1;
                end else if (clockDivider == 7'b1111111) begin
                    state <= STATE_DONE;
                end else if (clockDivider[6:5] == 2'b11) begin
                    scl <= 0;
                end
                // else if (clockDivider == 7'b1000000) begin
                //     sdaIn should be 0
                // end
            end
            STATE_DONE: begin
                complete <= 1;
                if (~enable)
                    state <= STATE_IDLE;
            end
        endcase
    end
endmodule
