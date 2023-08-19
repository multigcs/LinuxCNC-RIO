
module vfdbridge 
    #(parameter divider = 5)
    (
        input clk,
        inout i2cSda,
        output i2cScl,
        output wire [31:0] speed_feedback,
        input wire [31:0] speed_set,
        output reg speed_at = 0
    );

    localparam STATE_TRIGGER_CONV = 0;
    localparam STATE_WAIT_FOR_START = 1;
    localparam STATE_SAVE_VALUE_WHEN_READY = 2;

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
    wire [15:0] comOutputData;
    wire comDataReady;
    reg comEnable = 0;

    reg [2:0] ctrl = 0;
    reg iclk = 0;
    reg [255:0] iclk_cnt = 0;

    always @(posedge clk) begin
    
        if (iclk_cnt == divider) begin
            iclk <= ~iclk;
            iclk_cnt <= 0;
        end else begin
            iclk_cnt <= iclk_cnt + 1;
        end
    
    end

    vfdbridge_i2c i2c(
        iclk,
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

    vfdbridge_com com(
        iclk,
        speed_feedback,
        speed_set,
        comDataReady,
        comEnable,
        i2cInstruction,
        i2cEnable,
        i2cByteToSend,
        i2cByteReceived,
        i2cComplete
    );


    always @(posedge iclk) begin

        if ((speed_set>>4) == (speed_feedback>>4)) begin
            speed_at <= 1;
        end else if ((speed_set>>4) == (-speed_feedback>>4)) begin
            speed_at <= 1;
        end else begin
            speed_at <= 0;
        end

        case (drawState)
            STATE_TRIGGER_CONV: begin
                comEnable <= 1;
                drawState <= STATE_WAIT_FOR_START;
            end
            STATE_WAIT_FOR_START: begin
                if (~comDataReady) begin
                    drawState <= STATE_SAVE_VALUE_WHEN_READY;
                end
            end
            STATE_SAVE_VALUE_WHEN_READY: begin
                if (comDataReady) begin
                    drawState <= STATE_TRIGGER_CONV;
                    comEnable <= 0;
                end
            end
        endcase
    end
endmodule



module vfdbridge_com
    (
        input clk,
        output reg [31:0] speed_feedback,
        input wire [31:0] speed_set,
        output reg dataReady = 1,
        input enable,
        output reg [1:0] instructionI2C = 0,
        output reg enableI2C = 0,
        output reg [7:0] byteToSendI2C = 0,
        input [7:0] byteReceivedI2C,
        input completeI2C
    );

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

    reg [4:0] taskIndex = 0;
    reg [4:0] state = STATE_IDLE;
    reg [7:0] counter = 0;
    reg processStarted = 0;

    always @(posedge clk) begin
        case (state)
            STATE_IDLE: begin
                if (enable) begin
                    state <= STATE_RUN_TASK;
                    taskIndex <= 5'd0;
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
                    1: begin
                        instructionI2C <= INST_WRITE_BYTE;
                        byteToSendI2C <= {7'd64, 1'd0};
                        enableI2C <= 1;
                        state <= STATE_WAIT_FOR_I2C;
                    end
                    2: begin
                        instructionI2C <= INST_WRITE_BYTE;
                        byteToSendI2C <= speed_set[31:24];
                        enableI2C <= 1;
                        state <= STATE_WAIT_FOR_I2C;
                    end
                    3: begin
                        instructionI2C <= INST_WRITE_BYTE;
                        byteToSendI2C <= speed_set[23:16];
                        enableI2C <= 1;
                        state <= STATE_WAIT_FOR_I2C;
                    end
                    4: begin
                        instructionI2C <= INST_WRITE_BYTE;
                        byteToSendI2C <= speed_set[15:8];
                        enableI2C <= 1;
                        state <= STATE_WAIT_FOR_I2C;
                    end
                    5: begin
                        instructionI2C <= INST_WRITE_BYTE;
                        byteToSendI2C <= speed_set[7:0];
                        enableI2C <= 1;
                        state <= STATE_WAIT_FOR_I2C;
                    end
                    6: begin
                        instructionI2C <= INST_STOP_TX;
                        enableI2C <= 1;
                        state <= STATE_WAIT_FOR_I2C;
                    end


                    10: begin
                        instructionI2C <= INST_START_TX;
                        enableI2C <= 1;
                        state <= STATE_WAIT_FOR_I2C;
                    end
                    11: begin
                        instructionI2C <= INST_WRITE_BYTE;
                        byteToSendI2C <= {7'd64, 1'd1};
                        enableI2C <= 1;
                        state <= STATE_WAIT_FOR_I2C;
                    end
                    12: begin
                        instructionI2C <= INST_READ_BYTE;
                        enableI2C <= 1;
                        state <= STATE_WAIT_FOR_I2C;
                    end
                    13: begin
                        instructionI2C <= INST_READ_BYTE;
                        speed_feedback[7:0] <= byteReceivedI2C;
                        enableI2C <= 1;
                        state <= STATE_WAIT_FOR_I2C;
                    end
                    14: begin
                        instructionI2C <= INST_READ_BYTE;
                        speed_feedback[15:8] <= byteReceivedI2C;
                        enableI2C <= 1;
                        state <= STATE_WAIT_FOR_I2C;
                    end
                    15: begin
                        instructionI2C <= INST_READ_BYTE;
                        speed_feedback[23:16] <= byteReceivedI2C;
                        enableI2C <= 1;
                        state <= STATE_WAIT_FOR_I2C;
                    end

                    16: begin
                        instructionI2C <= INST_STOP_TX;
                        speed_feedback[31:24] <= byteReceivedI2C;
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
                    state <= STATE_INC_TASK;
                    processStarted <= 0;
                    enableI2C <= 0;
                end
            end
            STATE_INC_TASK: begin
                state <= STATE_RUN_TASK;
                if (taskIndex == 5'd20) begin
                    state <= STATE_DONE;
                end else begin
                    taskIndex <= taskIndex + 4'd1;
                end
            end
            STATE_DELAY: begin
                counter <= counter + 8'd1;
                if (counter == 8'b11111111) begin
                    state <= STATE_INC_TASK;
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





module vfdbridge_i2c (
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
