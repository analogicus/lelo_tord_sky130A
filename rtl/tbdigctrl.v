module tbdigctrl  #(
     parameter DAC_WIDTH                     = 15, // DAC control resolution
     parameter TIMEOUT_LIMIT                 = 100,
     parameter INITIAL_COARSE_STEP_COUNT     = 4,   // initial coarse DAC step
     parameter INITIAL_FINETUNING_DUTY_CYCLE = 2,   // finetunig pulse length in tens if percent (5=50%)
     parameter INITIAL_FINETUNING_PERIODE    = 10   // finetuning periode lenght,
)(
     input  logic       clk, // 10 MHz clock
     input  logic       rst, // active high reset
     input  logic       cmp, // comparator output

     output logic       swbrn1,
     output logic       swbrn2,
     output logic       swbrn3,

     // output logic       swbgr1,
     // output logic       swbgr2,

     output logic       swcap1,
     output logic       swcap2,
     output logic       swcap3,

     // output logic       swdrn1,
     // output logic       swdrn2,
     // output logic       swdrn3,

     output logic       cmp_sync1,       
     output logic       cmp_sync2,       
     output logic       cmp_rising,   
     output logic [7:0] cmp_rising_counter,

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

     typedef enum logic [1:0] {
          BRANCH_1 = 2'd0,
          BRANCH_2 = 2'd1,
          BRANCH_3 = 2'd2
     } branch_sel_t;

     branch_sel_t branch_sel;

     initial begin
          coarse_step_counter_saved   = INITIAL_COARSE_STEP_COUNT;
          finetuning_duty_cycle_saved = INITIAL_FINETUNING_DUTY_CYCLE;
          finetuning_periode_saved    = INITIAL_FINETUNING_PERIODE;
          branch_sel                  = BRANCH_1;
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
               branch_sel            <= BRANCH_1;

               coarse_step_counter   <= coarse_step_counter_saved;
               finetuning_duty_cycle <= finetuning_duty_cycle_saved;
               finetuning_periode    <= finetuning_periode_saved;
          end 
          else if ((cmp_rising) && (branch_sel == BRANCH_2)) begin
               timeout_counter <= 0;

               cmp_rising_counter <= cmp_rising_counter + 1;

               if (cmp_rising_counter > 3) begin
                    cmp_rising_counter <= 0;
                    branch_sel      <= BRANCH_3;
                    coarse_step_counter_saved   <= coarse_step_counter;
                    finetuning_duty_cycle_saved <= finetuning_duty_cycle;
                    finetuning_periode_saved    <= finetuning_periode;
               end
          end 
          else if (timeout_counter >= TIMEOUT_LIMIT - 1) begin  
               timeout_counter <= 0;
               cmp_rising_counter <= 0;

               case (branch_sel)
                    BRANCH_1: begin
                         branch_sel <= BRANCH_2;
                    end
                    BRANCH_2: begin
                         branch_sel <= BRANCH_1;

                         if (finetuning_duty_cycle >= finetuning_periode - 1) begin
                              finetuning_duty_cycle <= 1;
                         end 
                         else if (finetuning_duty_cycle != finetuning_duty_cycle_saved - 1) begin
                              finetuning_duty_cycle <= finetuning_duty_cycle + 1;
                         end 
                         else begin
                              finetuning_duty_cycle <= finetuning_duty_cycle_saved;
                              coarse_step_counter   <= coarse_step_counter + 1;
                         end 
                    end
                    BRANCH_3: begin
                         branch_sel <= BRANCH_1;
                    end
                    default: ;
               endcase
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

     always_comb begin
          swcap1 = 0; swbrn1 = 0;
          swcap2 = 0; swbrn2 = 0;
          swcap3 = 0; swbrn3 = 0;

          case (branch_sel)
               BRANCH_1: begin
                    swbrn1 = 1'b1;
                    swcap1 = 1'b1;
               end
               BRANCH_2: begin
                    swbrn2 = 1'b1;
                    swcap2 = 1'b1;
               end
               BRANCH_3: begin
                    swbrn3 = 1'b1;
                    swcap3 = 1'b1;
               end
               default: ;
          endcase
     end

endmodule