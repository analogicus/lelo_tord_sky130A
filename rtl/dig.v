module dig(
           input wire cmp,
           output logic [7:0] b
           );

     always_ff @(posedge cmp) begin
          b <= b + 1;
     end

endmodule // 