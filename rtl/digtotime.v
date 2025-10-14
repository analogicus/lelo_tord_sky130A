module digtotime(
    input wire clk,
    input wire rst,
    output logic [3:0] d,
    output logic [2:0] count
);

    // logic [2:0] count;

    always_ff @ (posedge clk) begin
        
        if (rst) begin

            count <= 3'b0;
            d <= 4'b0;

        end else begin

            case (count)
                0 : d <= 4'b0000;
                1 : d <= 4'b0001;
                2 : d <= 4'b0010;
                3 : d <= 4'b0100;
                4 : d <= 4'b1000;
                default : d <= 4'b0110; // If b is ever this value, somethings wrong
            endcase

            if (count < 4) begin
                count <= count + 1;
            end else begin
                count <= 0;
            end
        
        end
    
    end

endmodule