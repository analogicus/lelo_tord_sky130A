module tbdigctrl(
    input wire clk,
    input wire cmp,
    input wire reset,
    output logic [4:0] b
    );

    logic rst = 0;

    always_ff @(posedge clk) begin
        if(reset) begin
            rst <= 1;
        end else begin
            rst <= 0;
        end
    end

    always_ff @(posedge cmp) begin
        if(rst)
            b <= 0;
        else
            b <= b + 1;
    end // tbdigctrl
endmodule