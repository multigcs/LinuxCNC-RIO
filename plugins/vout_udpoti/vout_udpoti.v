
module vout_udpoti
    #(
         parameter RESOLUTION = 100,
         parameter SPEED = 100000
     )
     (
         input clk,
         input wire [31:0] value,
         output reg UPDOWN = 0,
         output reg INCREMENT = 0
     );

    reg ctrl_clk = 0;
    reg [31:0] counter;
    reg init = 0;
    always @(posedge clk) begin
        if (counter == 0) begin
            counter <= SPEED;
            ctrl_clk <= ~ctrl_clk;
        end else begin
            counter <= counter - 1;
        end
    end

    reg [31:0] init_counter = RESOLUTION;
    reg [31:0] pos = 0;
    always @ (posedge ctrl_clk) begin
        if (init == 1) begin
            UPDOWN <= 0;
            if (init_counter > 0) begin
                if (INCREMENT == 0) begin
                    INCREMENT <= 1;
                end else begin
                    INCREMENT <= 0;
                    init_counter <= init_counter - 1;
                end
            end else begin
                init <= 0;
                pos <= 0;
            end
        end else begin
            if (value > pos) begin
                UPDOWN <= 1;
                if (INCREMENT == 0) begin
                    INCREMENT <= 1;
                end else begin
                    INCREMENT <= 0;
                    pos <= pos + 1;
                end
            end else if (value < pos) begin
                UPDOWN <= 0;
                if (INCREMENT == 0) begin
                    INCREMENT <= 1;
                end else begin
                    INCREMENT <= 0;
                    pos <= pos - 1;
                end
            end
        end
    end
endmodule

