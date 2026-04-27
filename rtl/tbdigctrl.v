module tbdigctrl  #(
     parameter DAC_WIDTH                     = 15,  // DAC control resolution
     parameter TIMEOUT_LIMIT                 = 100,
     parameter INITIAL_COARSE_STEP_COUNT     = 3,   // initial coarse DAC step
     parameter INITIAL_FINETUNING_DUTY_CYCLE = 2,   // finetunig pulse length in tens if percent (5=50%) (bug: cannot start on zero i think or the script won't work)
     parameter INITIAL_FINETUNING_PERIODE    = 10,  // finetuning periode lenght
     parameter SW_TIMEOUT                    = 3   // How many clock periods to hold on each switch state before moving on.
)(
     input  logic       clk, // a 10 MHz clock signal
     input  logic       rst, // active high reset to initial
     input  logic       cmp, // input from comparator
     
     output logic       slp, // active high signal enabling a power saving sleep mode

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

     output logic [4:0] sw_counter,

     output logic       cmp_sync1,       
     output logic       cmp_sync2,       
     output logic       cmp_rising, 
     output logic       cmp_falling,  

     output logic [7:0] cmp_rising_counter,
     output logic [7:0] cmp_switching_counter,

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
     output logic [7:0] finetuning_periode_saved,

     output logic       stepping_up
);

     typedef enum logic [1:0] {
          BRANCH_1 = 2'd0,
          BRANCH_2 = 2'd1,
          BRANCH_3 = 2'd2
     } selected_branch_t;

     selected_branch_t selected_branch;

     typedef enum logic [2:0] {
          SW_IDLE,
          SW_CAP_OFF,
          SW_BR_OFF,
          SW_BR_ON,
          SW_CAP_ON
     } switch_state_t;

     switch_state_t    switch_state;  // the state of the switches to the current brnaches and the capacitors on their outputs
     selected_branch_t target_branch; // the target we're switching toward
     selected_branch_t active_branch; // what switch_state machine is currently driving

     initial begin
          coarse_step_counter_saved   = INITIAL_COARSE_STEP_COUNT;
          finetuning_duty_cycle_saved = INITIAL_FINETUNING_DUTY_CYCLE;
          finetuning_periode_saved    = INITIAL_FINETUNING_PERIODE;
          selected_branch             = BRANCH_1;
          slp = 0;
     end

     always_ff @(posedge clk) begin
          cmp_sync1  <= cmp;
          cmp_sync2  <= cmp_sync1;
          cmp_rising <= cmp_sync1 & ~cmp_sync2;
          cmp_falling <= ~cmp_sync1 & cmp_sync2;
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
               selected_branch       <= BRANCH_1;
               slp <= 0;

               coarse_step_counter   <= coarse_step_counter_saved;
               finetuning_duty_cycle <= finetuning_duty_cycle_saved;
               finetuning_periode    <= finetuning_periode_saved;
          end 

          else if ((cmp_rising) && (selected_branch == BRANCH_2)) begin
               timeout_counter <= 0;
               cmp_rising_counter <= cmp_rising_counter + 1;

               if (cmp_rising_counter > 3) begin
                    cmp_rising_counter    <= 0;
                    cmp_switching_counter <= 0;
                    selected_branch       <= BRANCH_3;

                    coarse_step_counter_saved   <= coarse_step_counter;
                    finetuning_duty_cycle_saved <= finetuning_duty_cycle;
                    finetuning_periode_saved    <= finetuning_periode;
               end
          end

          else if ((cmp_switching_counter > 4) && (selected_branch == BRANCH_2)) begin
               timeout_counter <= 0;
               cmp_switching_counter <= 0;

               selected_branch <= BRANCH_3;

               coarse_step_counter_saved   <= coarse_step_counter;
               finetuning_duty_cycle_saved <= finetuning_duty_cycle;
               finetuning_periode_saved    <= finetuning_periode;
          end 

          else if (timeout_counter >= TIMEOUT_LIMIT - 1) begin  
               timeout_counter <= 0;
               cmp_rising_counter <= 0;

               case (selected_branch)

                    BRANCH_1: begin
                         selected_branch <= BRANCH_2;
                    end

                    BRANCH_2: begin
                         selected_branch <= BRANCH_1;

                         // STEP-UP (cmp is low => need more current):
                         if (!cmp_sync1) begin
                              if (!stepping_up) begin
                                   cmp_switching_counter <= cmp_switching_counter + 1;
                              end
                              stepping_up <= 1;

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

                         // STEP-DOWN (cmp is high => too much current):
                         else begin
                              if (stepping_up) begin
                                   cmp_switching_counter <= cmp_switching_counter + 1;
                              end
                              stepping_up <= 0;

                              if (finetuning_duty_cycle <= 1) begin
                                   finetuning_duty_cycle <= finetuning_periode - 1;
                              end 
                              else if (finetuning_duty_cycle != finetuning_duty_cycle_saved + 1) begin
                                   finetuning_duty_cycle <= finetuning_duty_cycle - 1;
                              end 
                              else begin
                                   finetuning_duty_cycle <= finetuning_duty_cycle_saved;
                                   coarse_step_counter   <= coarse_step_counter - 1;
                              end
                         end

                    end

                    BRANCH_3: begin
                         slp <= 1;
                         // selected_branch <= BRANCH_1;
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

     always_ff @(posedge clk or posedge rst) begin

          if (rst) begin
               switch_state  <= SW_IDLE;
               active_branch <= BRANCH_1;
               target_branch <= BRANCH_1;
               sw_counter    <= 0;

               // branch 1 active at reset
               swbrn1 <= 1'b1;
               swcap1 <= 1'b1;
               swbrn2 <= 1'b0;
               swcap2 <= 1'b0;
               swbrn3 <= 1'b0;
               swcap3 <= 1'b0;
          end 
          
          else begin

               if (selected_branch != target_branch) begin
                    target_branch <= selected_branch;
               end

               case (switch_state)

                    SW_IDLE: begin
                         if (target_branch != active_branch) begin
                              switch_state <= SW_CAP_OFF;
                              sw_counter   <= 0;
                         end
                    end

                    SW_CAP_OFF: begin
                         case (active_branch)
                              BRANCH_1: swcap1 <= 1'b0;
                              BRANCH_2: swcap2 <= 1'b0;
                              BRANCH_3: swcap3 <= 1'b0;
                              default: ;
                         endcase

                         if (sw_counter >= SW_TIMEOUT - 1) begin
                              switch_state <= SW_BR_OFF;
                              sw_counter   <= 0;
                         end else begin
                              sw_counter <= sw_counter + 1;
                         end
                    end

                    SW_BR_OFF: begin
                         case (active_branch)
                              BRANCH_1: swbrn1 <= 1'b0;
                              BRANCH_2: swbrn2 <= 1'b0;
                              BRANCH_3: swbrn3 <= 1'b0;
                              default: ;
                         endcase

                         if (sw_counter >= SW_TIMEOUT - 1) begin
                              switch_state <= SW_BR_ON;
                              sw_counter   <= 0;
                         end else begin
                              sw_counter <= sw_counter + 1;
                         end
                    end

                    SW_BR_ON: begin
                         case (target_branch)
                              BRANCH_1: swbrn1 <= 1'b1;
                              BRANCH_2: swbrn2 <= 1'b1;
                              BRANCH_3: swbrn3 <= 1'b1;
                              default: ;
                         endcase

                         if (sw_counter >= SW_TIMEOUT - 1) begin
                              switch_state <= SW_CAP_ON;
                              sw_counter   <= 0;
                         end else begin
                              sw_counter <= sw_counter + 1;
                         end
                    end

                    SW_CAP_ON: begin
                         case (target_branch)
                              BRANCH_1: swcap1 <= 1'b1;
                              BRANCH_2: swcap2 <= 1'b1;
                              BRANCH_3: swcap3 <= 1'b1;
                              default: ;
                         endcase

                         if (sw_counter >= SW_TIMEOUT - 1) begin
                              active_branch <= target_branch;  // commit the switch
                              switch_state  <= SW_IDLE;
                              sw_counter    <= 0;
                         end else begin
                              sw_counter <= sw_counter + 1;
                         end
                    end

                    default: switch_state <= SW_IDLE;
               endcase
          end
     end




endmodule