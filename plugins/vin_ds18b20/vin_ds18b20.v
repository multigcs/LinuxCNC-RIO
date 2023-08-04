
module vin_ds18b20(
        input         clk,
        inout         one_wire,
        output [31:0] temperature
    );

    reg [5:0] cnt = 0;

    wire one_wireIn;
    reg one_wireOut;
    reg isSending;
    assign one_wire = (isSending & ~one_wireOut) ? 1'b0 : 1'bz;
    assign one_wireIn = one_wire ? 1'b1 : 1'b0;


    always @ (posedge clk)
      if (cnt == 49)
        cnt <= 0;
      else
        cnt <= cnt + 1'b1;

    reg clk_1us = 0;

    always @ (posedge clk)
      if (cnt <= 24)                     
        clk_1us <= 0;
      else
        clk_1us <= 1;      


    reg [19:0] cnt_1us;                      
    reg cnt_1us_clear;                      

    always @ (posedge clk_1us)
      if (cnt_1us_clear)
        cnt_1us <= 0;
      else
        cnt_1us <= cnt_1us + 1'b1;

    parameter S00     = 5'h00;
    parameter S0      = 5'h01;
    parameter S1      = 5'h03;
    parameter S2      = 5'h02;
    parameter S3      = 5'h06;
    parameter S4      = 5'h07;
    parameter S5      = 5'h05;
    parameter S6      = 5'h04;
    parameter S7      = 5'h0C;
    parameter WRITE0  = 5'h0D;
    parameter WRITE1  = 5'h0F;
    parameter WRITE00 = 5'h0E;
    parameter WRITE01 = 5'h0A;
    parameter READ0   = 5'h0B;
    parameter READ1   = 5'h09;
    parameter READ2   = 5'h08;
    parameter READ3   = 5'h18;

    reg [4:0] state = S00;
    reg [15:0] temperature_buf;
    reg [5:0] step = 0;
    reg [3:0] bit_valid;                  
      
    always @(posedge clk_1us) begin
        case (state)
          S00 : begin              //0000 0000 0001 1111 16 bit for
                  temperature_buf <= 16'h001F; 
                  state           <= S0;
                end
          S0 :  begin                       
                  cnt_1us_clear <= 1;
                  isSending <= 1;
                  one_wireOut  <= 0;              
                  state         <= S1;
                end
          S1 :  begin
                  cnt_1us_clear <= 0;
                  if (cnt_1us == 500)        
                  begin
                    cnt_1us_clear <= 1;
                    isSending <= 0;
                    state         <= S2;
                  end 
                end
          S2 :  begin
                  cnt_1us_clear <= 0;
                  if (cnt_1us == 100)        
                  begin
                    cnt_1us_clear <= 1;
                    state         <= S3;
                  end 
                end
          S3 :  if (~one_wire)             
                  state <= S4;
                else if (one_wire)       
                  state <= S0;
          S4 :  begin
                  cnt_1us_clear <= 0;
                  if (cnt_1us == 400)         
                  begin
                    cnt_1us_clear <= 1;
                    state         <= S5;
                  end 
                end        
          S5 :  begin                   
                  if      (step == 0)      
                  begin
                    step  <= step + 1'b1;
                    state <= WRITE0;
                  end
                  else if (step == 1)
                  begin
                    step  <= step + 1'b1;
                    state <= WRITE0;
                  end
                  else if (step == 2)
                  begin                
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= WRITE01; 
                  end
                  else if (step == 3)
                  begin
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= WRITE01;                
                  end
                  else if (step == 4)
                  begin
                    step  <= step + 1'b1;
                    state <= WRITE0;
                  end
                  else if (step == 5)
                  begin
                    step  <= step + 1'b1;
                    state <= WRITE0;
                  end
                  else if (step == 6)
                  begin
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= WRITE01;
                  end
                  else if (step == 7)
                  begin
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= WRITE01;
                  end
                  
                  else if (step == 8)      
                  begin
                    step  <= step + 1'b1;
                    state <= WRITE0;
                  end
                  else if (step == 9)
                  begin
                    step  <= step + 1'b1;
                    state <= WRITE0;
                  end
                  else if (step == 10)
                  begin
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= WRITE01;
                  end
                  else if (step == 11)
                  begin
                    step  <= step + 1'b1;
                    state <= WRITE0;
                  end
                  else if (step == 12)
                  begin
                    step  <= step + 1'b1;
                    state <= WRITE0;
                  end
                  else if (step == 13)
                  begin
                    step  <= step + 1'b1;
                    state <= WRITE0;
                  end
                  else if (step == 14)
                  begin
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= WRITE01;
                     
                  end
                  else if (step == 15)
                  begin
                    step  <= step + 1'b1;
                    state <= WRITE0;
                  end
                  
                  else if (step == 16)
                  begin
                    isSending <= 0;
                    step         <= step + 1'b1;
                    state        <= S6;                
                  end
                  

                  else if (step == 17)
                  begin
                    step  <= step + 1'b1;
                    state <= WRITE0;
                  end
                  else if (step == 18)
                  begin
                    step  <= step + 1'b1;
                    state <= WRITE0;
                  end
                  else if (step == 19)
                  begin
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= WRITE01;                
                  end
                  else if (step == 20)
                  begin
                    step  <= step + 1'b1;
                    state <= WRITE01;
                    isSending <= 1;
                    one_wireOut <= 0;
                  end
                  else if (step == 21)
                  begin
                    step  <= step + 1'b1;
                    state <= WRITE0;
                  end
                  else if (step == 22)
                  begin
                    step  <= step + 1'b1;
                    state <= WRITE0;
                  end
                  else if (step == 23)
                  begin
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= WRITE01;
                  end
                  else if (step == 24)
                  begin
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= WRITE01;               
                  end
                  
                  else if (step == 25)     
                  begin
                    step  <= step + 1'b1;
                    state <= WRITE0;
                  end
                  else if (step == 26)
                  begin
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= WRITE01;                
                  end
                  else if (step == 27)
                  begin
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= WRITE01;                
                  end
                  else if (step == 28)
                  begin
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= WRITE01;                
                  end
                  else if (step == 29)
                  begin
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= WRITE01;
                  end
                  else if (step == 30)
                  begin
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= WRITE01;
                  end
                  else if (step == 31)
                  begin
                    step  <= step + 1'b1;
                    state <= WRITE0;
                  end
                  else if (step == 32)
                  begin
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= WRITE01;
                  end
                  
                  else if (step == 33)
                  begin
                    step  <= step + 1'b1;
                    state <= S7;
                  end 
                end
          S6 :  begin
                  cnt_1us_clear <= 0;
                  if (cnt_1us == 750000 | one_wire)    
                  begin
                    cnt_1us_clear <= 1;
                    state         <= S0;   
                  end 
                end
                
          S7 :  begin                     
                  if      (step == 34)
                  begin
                    bit_valid    <= 0;
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= READ0;
                  end
                  else if (step == 35)
                  begin
                    bit_valid    <= bit_valid + 1'b1;
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= READ0;
                  end
                  else if (step == 36)
                  begin
                    bit_valid    <= bit_valid + 1'b1;
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= READ0;
                  end
                  else if (step == 37)
                  begin
                    bit_valid    <= bit_valid + 1'b1;
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= READ0;               
                  end
                  else if (step == 38)
                  begin
                    bit_valid    <= bit_valid + 1'b1;
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= READ0;                
                  end
                  else if (step == 39)
                  begin
                    bit_valid    <= bit_valid + 1'b1;
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= READ0;               
                  end
                  else if (step == 40)
                  begin
                    bit_valid    <= bit_valid + 1'b1;
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= READ0;                
                  end
                  else if (step == 41)
                  begin
                    bit_valid    <= bit_valid + 1'b1;
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= READ0;
                  end
                  else if (step == 42)
                  begin
                    bit_valid    <= bit_valid + 1'b1;
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= READ0;                
                  end
                  else if (step == 43)
                  begin
                    bit_valid    <= bit_valid + 1'b1;
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= READ0;
                  end
                  else if (step == 44)
                  begin
                    bit_valid    <= bit_valid + 1'b1;
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= READ0;                
                  end
                  else if (step == 45)
                  begin
                    bit_valid    <= bit_valid + 1'b1;
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= READ0;                
                  end
                  else if (step == 46)
                  begin
                    bit_valid    <= bit_valid + 1'b1;
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= READ0;                
                  end
                  else if (step == 47)
                  begin
                    bit_valid    <= bit_valid + 1'b1;
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= READ0;                
                  end
                  else if (step == 48)
                  begin
                    bit_valid    <= bit_valid + 1'b1;
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= READ0;                
                  end
                  else if (step == 49)
                  begin
                    bit_valid    <= bit_valid + 1'b1;
                    isSending <= 1;
                    one_wireOut <= 0;
                    step         <= step + 1'b1;
                    state        <= READ0;                
                  end
                  else if (step == 50)
                  begin
                    step  <= 0;
                    state <= S0;
                  end 
                end            
                
                
         
          WRITE0 :
                begin
                  cnt_1us_clear <= 0;
                  isSending <= 1;
                  one_wireOut  <= 0;                 
                  if (cnt_1us == 80)        
                  begin
                    cnt_1us_clear <= 1;
                    isSending <= 0;
                    state         <= WRITE00;
                  end 
                end
          WRITE00 :                       
                  state <= S5;
          WRITE01 :                       
                  state <= WRITE1;
          WRITE1 :
                begin
                  cnt_1us_clear <= 0;
                  isSending <= 0;
                  if (cnt_1us == 80)        
                  begin
                    cnt_1us_clear <= 1;
                    state         <= S5;
                  end 
                end
         
          READ0 : state <= READ1;          
          READ1 :
                begin
                  cnt_1us_clear <= 0;
                  isSending <= 0;
                  if (cnt_1us == 10)       
                  begin
                    cnt_1us_clear <= 1;
                    state         <= READ2;
                  end 
                end
          READ2 :                          
                begin
                  temperature_buf[bit_valid] <= one_wireIn;
                  state                      <= READ3;
                end
          READ3 :
                begin
                  cnt_1us_clear <= 0;
                  if (cnt_1us == 55)       
                  begin
                    cnt_1us_clear <= 1;
                    state         <= S7;
                  end 
                end
        
          
          default : state <= S00;
        endcase 
    end 

    wire [15:0] t_buf = temperature_buf & 16'h07FF;
    assign temperature[3:0]   = (t_buf[3:0] * 10) >> 4;
    assign temperature[7:4]   = (((t_buf[7:4] * 10) >> 4) >= 4'd10) ? (((t_buf[7:4] * 10) >> 4) - 'd10) : ((t_buf[7:4] * 10) >> 4);
    assign temperature[11:8]  = (((t_buf[7:4] * 10) >> 4) >= 4'd10) ? (((t_buf[11:8] * 10) >> 4) + 'd1) + 'd2 : ((t_buf[11:8] * 10) >> 4) + 'd2;
    assign temperature[15:12] = temperature_buf[12] ? 1 : 0;
    assign temperature[31:16] = 0;

endmodule
