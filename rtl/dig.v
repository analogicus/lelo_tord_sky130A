

module dig(
          input wire cmp,
          input wire rst,
          output logic rst_out,
          output logic sel_cap1,
          output logic sel_cap2,
          output logic [7:0] b
          );

     initial begin
          sel_cap1 = 1'b1;
          sel_cap2 = 1'b0;
          b = 8'b0;
          rst_out = 1'b0;
     end

     always_latch @(posedge cmp or posedge rst) begin
          if (rst) begin
              b <= 8'b0;
          end
          else begin
               b <= b + 1;
               sel_cap1 <= ~sel_cap1;
               sel_cap2 <= ~sel_cap2;
          end

          // if (b > 6) begin
               // b <= 8'b0;
               // rst_out <= 1'b1;
          // end
     end

endmodule // 