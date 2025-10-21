module tbdac(
    input wire dac_clk,
    input wire dac_rst,
    output logic [3:0] b,
    output logic [2:0] count
);

    // logic [2:0] count;

    always_ff @ (posedge dac_clk) begin
        
        if (dac_rst) begin
        
            count <= 3'b0;
            b <= 4'b0;

        end else begin

            case (count)
                // 0 : b <= 4'b0000;
                1 : b <= 4'b0001;
                2 : b <= 4'b0011;
                3 : b <= 4'b0111;
                4 : b <= 4'b1111;
                default : b <= 4'b0000; // strikethrough(If b is ever this value, somethings wrong)
            endcase

            if (count < 4) begin
                count <= count + 1;
            end else if (count < 7) begin 
                count <= count + 1;
            end else begin
                count <= 0;
            end
        
        end
    
    end

endmodule