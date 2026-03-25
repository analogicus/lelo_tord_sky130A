// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// The code below does not work as intended for some reason.
// It does not stop stepping through the coarse DAC levels,
// even when the flag is raised. The flag is also raised when
// the clock counter resets the first time, and I lack the 
// functionality to reset it.

module tbdigctrl(
    input wire clk,
    input wire cmp,
    input wire reset,
    output logic [4:0] cmp_count,
    output logic [5:0] clk_count,
    output logic [3:0] step_count,
    output logic [14:0] coarse_step,
    output logic flag
    );

    logic rst = 0;

    always_ff @(posedge clk) begin
        clk_count <= clk_count + 1;

        if (reset) begin
            rst <= 1;
        end else begin
            rst <= 0;
        end

        if ((clk_count == 25) && (flag == 0)) begin
            step_count <= step_count + 1;
            clk_count <= 0;
        end

        case (step_count)
            4'd1: coarse_step = 15'b000_0000_0000_0001;
            4'd2: coarse_step = 15'b000_0000_0000_0011;
            4'd3: coarse_step = 15'b000_0000_0000_0111;
            4'd4: coarse_step = 15'b000_0000_0000_1111;
            4'd5: coarse_step = 15'b000_0000_0001_1111;
            4'd6: coarse_step = 15'b000_0000_0011_1111;
            4'd7: coarse_step = 15'b000_0000_0111_1111;
            4'd8: coarse_step = 15'b000_0000_1111_1111;
            4'd9: coarse_step = 15'b000_0001_1111_1111;
            4'd10: coarse_step = 15'b000_0011_1111_1111;
            4'd11: coarse_step = 15'b000_0111_1111_1111;
            4'd12: coarse_step = 15'b000_1111_1111_1111;
            4'd13: coarse_step = 15'b001_1111_1111_1111;
            4'd14: coarse_step = 15'b011_1111_1111_1111;
            4'd15: coarse_step = 15'b111_1111_1111_1111;
            default: coarse_step = 15'b000_0000_0000_0000;
        endcase
 
        if ((cmp_count == 6) && (flag == 0)) begin
            flag <= 1;
        end else begin
            flag <= 0;
        end
    end

    always_ff @(posedge cmp) begin
        if (rst)
            cmp_count <= 0;
        else
            cmp_count <= cmp_count + 1;
    end // tbdigctrl
endmodule

// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// This module works like the one above should have

module tbdigctrl(
    input wire clk,
    input wire cmp,
    input wire reset,
    output logic [4:0] cmp_count,
    output logic [5:0] clk_count,
    output logic [3:0] step_count,
    output logic [5:0] coarse_step,
    output logic flag
    );

    logic rst = 0;

    always_ff @(posedge clk) begin
        clk_count <= clk_count + 1;

        if (reset) begin
            rst <= 1;
        end else begin
            rst <= 0;
        end

        if ((clk_count == 33) && (flag == 0)) begin
            step_count <= step_count + 1;
            clk_count <= 0;
        end

        case (step_count)
            4'd1: coarse_step = 6'b001111;
            4'd2: coarse_step = 6'b011111;
            4'd3: coarse_step = 6'b111111;
            default: coarse_step = 6'b000111;
        endcase
 
        if (cmp_count == 6) begin
            flag <= 1;
        end
    end

    always_ff @(posedge cmp) begin
        if (rst)
            cmp_count <= 0;
        else
            cmp_count <= cmp_count + 1;
    end // tbdigctrl
endmodule

// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// This module does not work. only updates on clock  counter reset 

module tbdigctrl #(
    parameter COARSE_DAC_LEVELS = 15, // Width of DAC control word
    parameter TIMEOUT_CYCLES    = 60, // Number of clk cycles without pulse before stepping DAC
    parameter PULSE_LIMIT       = 6
)(
    input wire clk,
    input wire cmp,
    input wire rst,

    output logic [4:0] cmp_count,
    output logic [5:0] clk_count,
    output logic [3:0] step_count,
    output logic [14:0] coarse_step,
    output logic flag,
);

    always_ff @(posedge clk) begin
        cmp_curr <= cmp;
        cmp_prev <= cmp_curr;
    end

    assign cmp_rise = cmp_curr & ~cmp_prev;

    always_ff @(posedge clk) begin
        if (rst) begin
            clk_count  <= 0;
            step_count <= 0;
            flag       <= 0;
        end else begin
            if (clk_count >= 60) begin
                if (!flag) begin
                    clk_count <= 0;
                    step_count <= step_count + 1;
                end
            end else begin
                clk_count <= clk_count + 1;

                if (cmp_rise && !flag) begin
                    cmp_count <= cmp_count + 1;

                    if (cmp_count > 5) begin
                        flag <= 1;
                    end
                end

                unique case (step_count)
                    4'b0001: coarse_step <= 15'b000_0000_0000_0001;
                    4'b0010: coarse_step <= 15'b000_0000_0000_0011;
                    4'b0011: coarse_step <= 15'b000_0000_0000_0111;
                    4'b0100: coarse_step <= 15'b000_0000_0000_1111;
                    4'b0101: coarse_step <= 15'b000_0000_0001_1111;
                    4'b0110: coarse_step <= 15'b000_0000_0011_1111;
                    default: coarse_step <= 15'b000_0000_0000_0000;
                endcase
            end
        end
    end
endmodule



// %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

module tbdigctrl #(
    parameter DAC_WIDTH                     = 15,   // DAC control resolution
    parameter COARSE_TIMEOUT_LIMIT          = 11,   // 10 * 0.1 us @10MHz (detect missing 1MHz pulses)
    parameter INITIAL_FINETUNING_DUTY_CYCLE = 5,    // finetunig pulse length
    parameter INITIAL_FINETUNING_PERIODE    = 10,   // finetuning periode lenght
    parameter INITIAL_COARSE_STEP_COUNT     = 4     // initial coarse DAC step
)(
    input  logic       clk, // 10 MHz clock
    input  logic       rst, // active high reset
    input  logic       cmp, // comparator output
   
    output logic       cmp_sync1,       
    output logic       cmp_sync2,       
    output logic       cmp_rising,   

    output logic [7:0] coarse_step_timeout_counter, 
    output logic [3:0] coarse_step_counter,
    output logic [7:0] coarse_step1, // 8 bit first half of coarse current steering DAC input control
    output logic [6:0] coarse_step2, // 7 bit second half of coarse current steering DAC input control

    output logic [7:0] finetuning_duty_cycle, // sets duty cycle of finetuning signal in number of clock cycles
    output logic [7:0] finetuning_periode,  // sets periode (and thus freqeuncy) of finetuning signal in number of clock cycles
    output logic [7:0] finetuning_counter, 
    output logic       finetuning_signal
);
    always_ff @(posedge clk) begin
        cmp_sync1  <= cmp;
        cmp_sync2  <= cmp_sync1;
        cmp_rising <= cmp_sync1 & ~cmp_sync2;
    end

    always_ff @(posedge clk or posedge rst) begin
        if (rst) begin
            finetuning_duty_cycle <= INITIAL_FINETUNING_DUTY_CYCLE;
            finetuning_periode    <= INITIAL_FINETUNING_PERIODE;
        end
    end

    always_ff @(posedge clk or posedge rst) begin
        if (rst) begin
            finetuning_counter <= 0;
        end else if (finetuning_counter >= finetuning_periode - 1) begin
            finetuning_counter <= 0;
        end else begin
            finetuning_counter <= finetuning_counter + 1;
        end
    end

    always_comb begin
        finetuning_signal = (finetuning_counter < finetuning_duty_cycle);
    end

    always_ff @(posedge clk or posedge rst) begin
        if (rst) begin
            coarse_step_timeout_counter <= 0;
            coarse_step_counter <= INITIAL_COARSE_STEP_COUNT;
        end else if (cmp_rising) begin
            coarse_step_timeout_counter <= 0;
        end else if (coarse_step_timeout_counter == COARSE_TIMEOUT_LIMIT-1) begin
            coarse_step_timeout_counter <= 0;
            coarse_step_counter <= coarse_step_counter + 1;
        end else begin
            coarse_step_timeout_counter <= coarse_step_timeout_counter + 1;
        end
    end

    always_comb begin
        case (coarse_step_counter)
            1: begin
                coarse_step1 = 8'b0000_0001;
                coarse_step2 = 7'b_000_0000;
            end 
            2: begin
                coarse_step1 = 8'b0000_0011;
                coarse_step2 = 7'b_000_0000;
            end 
            3: begin
                coarse_step1 = 8'b0000_0111;
                coarse_step2 = 7'b_000_0000;
            end 
            4: begin
                coarse_step1 = 8'b0000_1111;
                coarse_step2 = 7'b_000_0000;
            end 
            5: begin
                coarse_step1 = 8'b0001_1111;
                coarse_step2 = 7'b_000_0000;
            end 
            6: begin
                coarse_step1 = 8'b0011_1111;
                coarse_step2 = 7'b_000_0000;
            end 
            7: begin
                coarse_step1 = 8'b0111_1111;
                coarse_step2 = 7'b_000_0000;
            end 
            8: begin
                coarse_step1 = 8'b1111_1111;
                coarse_step2 = 7'b_000_0000;
            end 
            9: begin
                coarse_step1 = 8'b1111_1111;
                coarse_step2 = 7'b_000_0001;
            end 
            10: begin
                coarse_step1 = 8'b1111_1111;
                coarse_step2 = 7'b_000_0011;
            end 
            11: begin
                coarse_step1 = 8'b1111_1111;
                coarse_step2 = 7'b_000_0111;
            end 
            12: begin
                coarse_step1 = 8'b1111_1111;
                coarse_step2 = 7'b_000_1111;
            end 
            13: begin
                coarse_step1 = 8'b1111_1111;
                coarse_step2 = 7'b_001_1111;
            end 
            14: begin
                coarse_step1 = 8'b1111_1111;
                coarse_step2 = 7'b_011_1111;
            end 
            15: begin
                coarse_step1 = 8'b1111_1111;
                coarse_step2 = 7'b_111_1111;
            end 
            default: begin
                coarse_step1 = '0;
                coarse_step2 = '0;
            end
        endcase
    end
endmodule



// %%%%%

module tbdigctrl #(
    parameter DAC_WIDTH                     = 15, // DAC control resolution
    parameter TIMEOUT_LIMIT                 = 50,
    parameter INITIAL_COARSE_STEP_COUNT     = 1,   // initial coarse DAC step
    parameter INITIAL_FINETUNING_DUTY_CYCLE = 3,  // finetunig pulse length in tens if percent (5=50%)
    parameter INITIAL_FINETUNING_PERIODE    = 10  // finetuning periode lenght
)(
    input  logic       clk, // 10 MHz clock
    input  logic       rst, // active high reset
    input  logic       cmp, // comparator output
   
    output logic       cmp_sync1,       
    output logic       cmp_sync2,       
    output logic       cmp_rising,   

    output logic [7:0] timeout_counter, 
    output logic [3:0] coarse_step_counter,
    output logic [7:0] coarse_step1, // 8 bit first half of coarse current steering DAC input control
    output logic [6:0] coarse_step2, // 7 bit second half of coarse current steering DAC input control

    output logic [7:0] finetuning_duty_cycle, // sets duty cycle of finetuning signal in number of clock cycles
    output logic [7:0] finetuning_periode,    // sets periode (and thus frequency) of finetuning signal in number of clock cycles
    output logic [7:0] finetuning_counter, 
    output logic       finetuning_signal,

    output logic [3:0] coarse_step_counter_saved,
    output logic [7:0] finetuning_duty_cycle_saved,
    output logic [7:0] finetuning_periode_saved
);

    initial begin
        coarse_step_counter_saved   = INITIAL_COARSE_STEP_COUNT;
        finetuning_duty_cycle_saved = INITIAL_FINETUNING_DUTY_CYCLE;
        finetuning_periode_saved    = INITIAL_FINETUNING_PERIODE;
    end

    always_ff @(posedge clk) begin
        cmp_sync1  <= cmp;
        cmp_sync2  <= cmp_sync1;
        cmp_rising <= cmp_sync1 & ~cmp_sync2;
    end

    always_ff @(posedge clk or posedge rst) begin
        if (rst) begin
            finetuning_counter <= 0;
        end else if (finetuning_counter >= finetuning_periode - 1) begin
            finetuning_counter <= 0;
        end else begin
            finetuning_counter <= finetuning_counter + 1;
        end
    end

    always_comb begin
        finetuning_signal = (finetuning_counter < finetuning_duty_cycle);
    end

    always_ff @(posedge clk or posedge rst) begin
        if (rst) begin
            timeout_counter       <= 0;
            coarse_step_counter   <= coarse_step_counter_saved;
            finetuning_duty_cycle <= finetuning_duty_cycle_saved;
            finetuning_periode    <= finetuning_periode_saved;
        end 
        else if (cmp_rising) begin
            timeout_counter <= 0;
            coarse_step_counter_saved <= coarse_step_counter;
            finetuning_duty_cycle_saved <= finetuning_duty_cycle;
        end 
        else if (timeout_counter == TIMEOUT_LIMIT - 1) begin  
            timeout_counter <= 0;
            if (finetuning_duty_cycle >= finetuning_periode - 1) begin
                finetuning_duty_cycle <= 1;
            end 
            else if (finetuning_duty_cycle != INITIAL_FINETUNING_DUTY_CYCLE - 1) begin
                finetuning_duty_cycle <= finetuning_duty_cycle + 1;
            end 
            else begin
                finetuning_duty_cycle <= INITIAL_FINETUNING_DUTY_CYCLE;
                coarse_step_counter   <= coarse_step_counter + 1;
            end 
        end
        else begin
            timeout_counter <= timeout_counter + 1;
        end    
    end

    always_comb begin
        case (coarse_step_counter)
            1: begin
                coarse_step1 = 8'b0000_0001;
                coarse_step2 = 7'b_000_0000;
            end 
            2: begin
                coarse_step1 = 8'b0000_0011;
                coarse_step2 = 7'b_000_0000;
            end 
            3: begin
                coarse_step1 = 8'b0000_0111;
                coarse_step2 = 7'b_000_0000;
            end 
            4: begin
                coarse_step1 = 8'b0000_1111;
                coarse_step2 = 7'b_000_0000;
            end 
            5: begin
                coarse_step1 = 8'b0001_1111;
                coarse_step2 = 7'b_000_0000;
            end 
            6: begin
                coarse_step1 = 8'b0011_1111;
                coarse_step2 = 7'b_000_0000;
            end 
            7: begin
                coarse_step1 = 8'b0111_1111;
                coarse_step2 = 7'b_000_0000;
            end 
            8: begin
                coarse_step1 = 8'b1111_1111;
                coarse_step2 = 7'b_000_0000;
            end 
            9: begin
                coarse_step1 = 8'b1111_1111;
                coarse_step2 = 7'b_000_0001;
            end 
            10: begin
                coarse_step1 = 8'b1111_1111;
                coarse_step2 = 7'b_000_0011;
            end 
            11: begin
                coarse_step1 = 8'b1111_1111;
                coarse_step2 = 7'b_000_0111;
            end 
            12: begin
                coarse_step1 = 8'b1111_1111;
                coarse_step2 = 7'b_000_1111;
            end 
            13: begin
                coarse_step1 = 8'b1111_1111;
                coarse_step2 = 7'b_001_1111;
            end 
            14: begin
                coarse_step1 = 8'b1111_1111;
                coarse_step2 = 7'b_011_1111;
            end 
            15: begin
                coarse_step1 = 8'b1111_1111;
                coarse_step2 = 7'b_111_1111;
            end 
            default: begin
                coarse_step1 = '0;
                coarse_step2 = '0;
            end
        endcase
    end
endmodule