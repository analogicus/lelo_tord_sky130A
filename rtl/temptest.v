module tbdigctrl  #(
     parameter DAC_WIDTH                     = 15,
     parameter TIMEOUT_LIMIT                 = 100,
     parameter INITIAL_COARSE_STEP_COUNT     = 2,
     parameter INITIAL_FINETUNING_DUTY_CYCLE = 2,
     parameter INITIAL_FINETUNING_PERIODE    = 10
)(
     input  logic       clk,
     input  logic       rst,
     input  logic       cmp,

     output logic       swbrn1,
     output logic       swbrn2,
     output logic       swbrn3,

     output logic       swcap1,
     output logic       swcap2,
     output logic       swcap3,

     output logic       cmp_sync1,       
     output logic       cmp_sync2,       
     output logic       cmp_rising,   
     output logic [7:0] cmp_rising_counter,

     output logic       cmp_level,        // NEW: latched comparator level

     output logic [7:0] timeout_counter, 
     output logic [3:0] coarse_step_counter,
     output logic [7:0] coarse_step1,
     output logic [6:0] coarse_step2,

     output logic [7:0] finetuning_duty_cycle,
     output logic [7:0] finetuning_periode,
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

     // NEW: direction flag. 0 = stepping up (cmp was low), 1 = stepping down (cmp went high)
     logic stepping_down;

     initial begin
          coarse_step_counter_saved   = INITIAL_COARSE_STEP_COUNT;
          finetuning_duty_cycle_saved = INITIAL_FINETUNING_DUTY_CYCLE;
          finetuning_periode_saved    = INITIAL_FINETUNING_PERIODE;
          branch_sel                  = BRANCH_1;
          stepping_down               = 1'b0;
     end

     // --- Comparator sync chain ---
     always_ff @(posedge clk) begin
          cmp_sync1   <= cmp;
          cmp_sync2   <= cmp_sync1;
          cmp_rising  <= cmp_sync1 & ~cmp_sync2;
     end

     // NEW: latch comparator level (debounced via sync2) so we know
     // whether cmp is currently high or low when a timeout fires
     always_ff @(posedge clk or posedge rst) begin
          if (rst)
               cmp_level <= 1'b0;
          else
               cmp_level <= cmp_sync2;
     end

     // --- Finetuning counter ---
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

     // --- Main state machine ---
     always_ff @(posedge clk or posedge rst) begin
          if (rst) begin
               timeout_counter       <= 0;
               branch_sel            <= BRANCH_1;
               stepping_down         <= 1'b0;

               coarse_step_counter   <= coarse_step_counter_saved;
               finetuning_duty_cycle <= finetuning_duty_cycle_saved;
               finetuning_periode    <= finetuning_periode_saved;
          end 

          // --- BRANCH_2: watching for a comparator rising edge ---
          else if ((cmp_rising) && (branch_sel == BRANCH_2)) begin
               timeout_counter    <= 0;
               cmp_rising_counter <= cmp_rising_counter + 1;

               if (cmp_rising_counter > 3) begin
                    cmp_rising_counter <= 0;
                    branch_sel         <= BRANCH_3;

                    // Save the converged operating point
                    coarse_step_counter_saved   <= coarse_step_counter;
                    finetuning_duty_cycle_saved <= finetuning_duty_cycle;
                    finetuning_periode_saved    <= finetuning_periode;

                    // cmp just went high → switch to stepping-down mode
                    stepping_down <= 1'b1;
               end
          end 

          // --- Timeout handler ---
          else if (timeout_counter >= TIMEOUT_LIMIT - 1) begin  
               timeout_counter    <= 0;
               cmp_rising_counter <= 0;

               case (branch_sel)

                    // BRANCH_1: idle / settling branch — just advance to BRANCH_2
                    BRANCH_1: begin
                         branch_sel <= BRANCH_2;
                    end

                    // BRANCH_2: no comparator edge seen within timeout
                    BRANCH_2: begin
                         branch_sel <= BRANCH_1;

                         // ---- STEP-UP path (cmp low, need more current) ----
                         if (!stepping_down) begin
                              if (finetuning_duty_cycle >= finetuning_periode - 1) begin
                                   // Duty cycle wrapped all the way — step coarse up
                                   finetuning_duty_cycle <= 1;
                                   coarse_step_counter   <= coarse_step_counter + 1;
                              end else begin
                                   finetuning_duty_cycle <= finetuning_duty_cycle + 1;
                              end
                         end

                         // ---- STEP-DOWN path (cmp high, too much current) ----
                         else begin
                              if (finetuning_duty_cycle <= 1) begin
                                   // Duty cycle wrapped all the way down — step coarse down
                                   finetuning_duty_cycle <= finetuning_periode - 1;
                                   if (coarse_step_counter > 0)
                                        coarse_step_counter <= coarse_step_counter - 1;
                                   // else already at minimum, hold
                              end else begin
                                   finetuning_duty_cycle <= finetuning_duty_cycle - 1;
                              end
                         end
                    end

                    // BRANCH_3: locked — stay here until reset
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

     // --- Coarse DAC thermometer decode (unchanged) ---
     always_comb begin
          case (coarse_step_counter)
               1:  begin coarse_step1 = 8'b0000_0001; coarse_step2 = 7'b000_0000; end
               2:  begin coarse_step1 = 8'b0000_0011; coarse_step2 = 7'b000_0000; end
               3:  begin coarse_step1 = 8'b0000_0111; coarse_step2 = 7'b000_0000; end
               4:  begin coarse_step1 = 8'b0000_1111; coarse_step2 = 7'b000_0000; end
               5:  begin coarse_step1 = 8'b0001_1111; coarse_step2 = 7'b000_0000; end
               6:  begin coarse_step1 = 8'b0011_1111; coarse_step2 = 7'b000_0000; end
               7:  begin coarse_step1 = 8'b0111_1111; coarse_step2 = 7'b000_0000; end
               8:  begin coarse_step1 = 8'b1111_1111; coarse_step2 = 7'b000_0000; end
               9:  begin coarse_step1 = 8'b1111_1111; coarse_step2 = 7'b000_0001; end
               10: begin coarse_step1 = 8'b1111_1111; coarse_step2 = 7'b000_0011; end
               11: begin coarse_step1 = 8'b1111_1111; coarse_step2 = 7'b000_0111; end
               12: begin coarse_step1 = 8'b1111_1111; coarse_step2 = 7'b000_1111; end
               13: begin coarse_step1 = 8'b1111_1111; coarse_step2 = 7'b001_1111; end
               14: begin coarse_step1 = 8'b1111_1111; coarse_step2 = 7'b011_1111; end
               15: begin coarse_step1 = 8'b1111_1111; coarse_step2 = 7'b111_1111; end
               default: begin coarse_step1 = '0; coarse_step2 = '0; end
          endcase
     end

     // --- Switch mux (unchanged) ---
     always_comb begin
          swcap1 = 0; swbrn1 = 0;
          swcap2 = 0; swbrn2 = 0;
          swcap3 = 0; swbrn3 = 0;

          case (branch_sel)
               BRANCH_1: begin swbrn1 = 1'b1; swcap1 = 1'b1; end
               BRANCH_2: begin swbrn2 = 1'b1; swcap2 = 1'b1; end
               BRANCH_3: begin swbrn3 = 1'b1; swcap3 = 1'b1; end
               default: ;
          endcase
     end

endmodule