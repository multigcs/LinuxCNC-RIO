
module vin_tlc549c
    #(parameter SPEED = 24)
    (
        input		clk,
        input		adc_data_in,
        output 		adc_clk,
        output reg	adc_cs_n,
        output reg	[7:0]adc_data
    );
	
	reg	[7:0] adc_data_buf;
	reg	[3:0] cnt;
	reg adc_clk_valid;
	reg adc_cs_n_valid;

    reg clk_1m;
    reg [31:0]counter_1m;
    always @(posedge clk) begin
        if (counter_1m == 0) begin
            counter_1m <= SPEED;
            clk_1m <= ~clk_1m;
        end else begin
            counter_1m <= counter_1m - 1;
        end
    end

    reg clk_40k;
    reg [31:0]counter_40k;
    always @(posedge clk_1m) begin
        if (counter_40k == 0) begin
            counter_40k <= 12;
            clk_40k <= ~clk_40k;
        end else begin
            counter_40k <= counter_40k - 1;
        end
    end

	always @(posedge clk_1m) begin
		if(clk_40k == 0) begin
			cnt <= 0;
		end else if(cnt == 10) begin
			cnt <= 10;
		end else begin
			cnt <= cnt + 1'b1;
        end
		adc_clk_valid <= !((cnt == 0) | (cnt == 1) | (cnt == 10));
		adc_cs_n <= (cnt == 0) | (cnt == 10);
    end
	
	assign adc_clk = adc_clk_valid ? clk_1m : 1'b0;

	always @(posedge adc_clk) begin
		if(adc_cs_n == 0) begin
			adc_data_buf <= {adc_data_in, adc_data_buf[7:1]};
        end
    end

	always @(posedge clk_40k) begin
		adc_data <= adc_data_buf;
    end
		
endmodule
