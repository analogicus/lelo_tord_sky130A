module tbdigctrl  #(
    parameter TIMEOUT_LIMIT                 = 100, 
    parameter INITIAL_COARSE_STEP_COUNT     = 2,   // initial coarse DAC step
    parameter INITIAL_FINETUNING_DUTY_CYCLE = 2,   // initial finetunig pulse length in number of clock cycles
    parameter INITIAL_FINETUNING_PERIODE    = 10,  // initial finetuning periode in number of clock cycles
    parameter SW_TIMEOUT                    = 3    // how many clock periods to wait in each switch state before moving on to the next.
)(
    input  logic       clk,  // the (10 MHz) clock signal
    input  logic       rst,  // external active high reset signal resetting circuit operation to initial values as defined in parameters
    input  logic       slp,  // external active high sleep signal enabling a power saving sleep mode
    input  logic       mode, // external operational mode signal (1 = reference generation, 0 = tempearture sensing)
    input  logic       cmp_async, // asynchrounous input from the comparator
    
    // Debug outputs - expose internal synchronizer stages for testbench visibility
    output logic       rst_meta,
    output logic       reset,
    output logic       slp_meta,
    output logic       sleep,

    output logic       mode_meta,
    output logic       operation,

    output logic       cmp_meta,       
    output logic       cmp_sync, 

    output logic       cmp_rising, 
    output logic       cmp_falling,  

    output logic [7:0] cmp_rising_counter,
    output logic [7:0] cmp_switching_counter,

    output logic       swbrn1,
    output logic       swbrn2,
    output logic       swbrn3,

    output logic       swbgr1,
    output logic       swbgr2,

    output logic       swcap1,
    output logic       swcap2,
    output logic       swcap3,

    // output logic       swdrn1,
    // output logic       swdrn2,
    // output logic       swdrn3,

    output logic [4:0] switch_counter,    

    output logic [7:0] timeout_counter, 
    output logic [3:0] coarse_step_counter,
    output logic [7:0] coarse_step1, // 8 bit first half of coarse current steering DAC input control
    output logic [6:0] coarse_step2, // 7 bit second half of coarse current steering DAC input control

    output logic [7:0] finetuning_duty_cycle, // sets duty cycle of finetuning signal in number of clock cycles
    output logic [7:0] finetuning_periode,    // sets periode (and thus frequency) of finetuning signal in number of clock cycles
    output logic [7:0] finetuning_counter, 
    output logic       finetuning_signal,

    output logic [3:0] saved_coarse_step_counter,
    output logic [7:0] saved_finetuning_duty_cycle,
    output logic [7:0] saved_finetuning_periode,

    output logic       stepping_up

    // output logic       output_found
);

    // ----- DEFINITIONS -----

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
    selected_branch_t active_branch; // what branch the switch_state machine is currently on


    // ----- SIGNAL SYNCHRONIZATION -----

    always_ff @(posedge clk or posedge rst) begin
        if (rst) begin
            rst_meta <= 1'b1;
            reset    <= 1'b1;
        end else begin
            rst_meta <= 1'b0;
            reset    <= rst_meta;
        end
    end

    always_ff @(posedge clk) begin
        slp_meta <= slp;
        sleep    <= slp_meta;
    end

    always_ff @(posedge clk) begin
        mode_meta <= mode;
        operation <= mode_meta; // 1 = reference generating mode, 0 = Temperatture sensing mode
    end

    always_ff @(posedge clk) begin
        cmp_meta <= cmp_async;
        cmp_sync <= cmp_meta;

        cmp_rising  <=  cmp_meta & ~cmp_sync;
        cmp_falling <= ~cmp_meta &  cmp_sync;
    end


    // ----- FINETUNING SIGNAL GENERATION -----

    always_ff @(posedge clk) begin
        if (reset || sleep) begin
            finetuning_counter <= 0;
            finetuning_signal  <= 0;
        end else if (finetuning_counter >= finetuning_periode - 1) begin
            finetuning_counter <= 0;
            finetuning_signal  <= (0 < finetuning_duty_cycle); // counter resets to 0 next cycle
        end else begin
            finetuning_counter <= finetuning_counter + 1;
            finetuning_signal  <= ((finetuning_counter + 1) < finetuning_duty_cycle);
        end
    end


    // ----- TEMPORARY SLEEP SIGNAL GENERATION -----

    // always_ff @(posedge clk) begin
    //     if (output_found) begin
    //         slp <= 1;
    //     end else begin
    //         slp <= 0;
    //     end
    // end


    // ----- MAIN FSM -----

    always_ff @(posedge clk) begin

        if (reset) begin
            timeout_counter <= 0;
            selected_branch <= BRANCH_1;
            stepping_up <= 1;

            // output_found <= 0;
            
            swbgr1 <= 0;
            swbgr2 <= 0;

            cmp_rising_counter <= 0;
            cmp_switching_counter <= 0;

            saved_coarse_step_counter   <= INITIAL_COARSE_STEP_COUNT;
            saved_finetuning_duty_cycle <= INITIAL_FINETUNING_DUTY_CYCLE;
            saved_finetuning_periode    <= INITIAL_FINETUNING_PERIODE;

            coarse_step_counter   <= INITIAL_COARSE_STEP_COUNT;
            finetuning_duty_cycle <= INITIAL_FINETUNING_DUTY_CYCLE;
            finetuning_periode    <= INITIAL_FINETUNING_PERIODE;
        end 

        else if (sleep) begin
            timeout_counter <= 0;
            selected_branch <= BRANCH_1;
            stepping_up <= 1;
            
            swbgr1 <= 0;
            swbgr2 <= 0;

            cmp_rising_counter <= 0;
            cmp_switching_counter <= 0;

            coarse_step_counter   <= saved_coarse_step_counter;
            finetuning_duty_cycle <= saved_finetuning_duty_cycle;
            finetuning_periode    <= saved_finetuning_periode; // Could set saved finetuning anc coarse states here and wait for slp to go low again
        end

        else begin

            swbgr1 <= operation;
            swbgr2 <= operation;

            if ((cmp_rising) && (selected_branch == BRANCH_2)) begin
                timeout_counter <= 0;
                cmp_rising_counter <= cmp_rising_counter + 1;

                if (cmp_rising_counter > 3) begin
                    cmp_rising_counter    <= 0;
                    cmp_switching_counter <= 0;
                    selected_branch       <= BRANCH_3;

                    saved_coarse_step_counter   <= coarse_step_counter;
                    saved_finetuning_duty_cycle <= finetuning_duty_cycle;
                    saved_finetuning_periode    <= finetuning_periode;
                end
            end

            else if ((cmp_switching_counter > 4) && (selected_branch == BRANCH_2)) begin
                timeout_counter <= 0;
                cmp_switching_counter <= 0;

                selected_branch <= BRANCH_3;

                saved_coarse_step_counter   <= coarse_step_counter;
                saved_finetuning_duty_cycle <= finetuning_duty_cycle;
                saved_finetuning_periode    <= finetuning_periode;
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
                        if (!cmp_sync) begin
                            if (!stepping_up) begin
                                cmp_switching_counter <= cmp_switching_counter + 1;
                            end
                            stepping_up <= 1;

                            if (finetuning_duty_cycle >= finetuning_periode - 1) begin
                                finetuning_duty_cycle <= 1;
                            end 
                            else if (finetuning_duty_cycle != saved_finetuning_duty_cycle - 1) begin
                                finetuning_duty_cycle <= finetuning_duty_cycle + 1;
                            end 
                            else begin
                                finetuning_duty_cycle <= saved_finetuning_duty_cycle;
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
                            else if (finetuning_duty_cycle != saved_finetuning_duty_cycle + 1) begin
                                finetuning_duty_cycle <= finetuning_duty_cycle - 1;
                            end 
                            else begin
                                finetuning_duty_cycle <= saved_finetuning_duty_cycle;
                                coarse_step_counter   <= coarse_step_counter - 1;
                            end
                        end
                    end

                    BRANCH_3: begin
                            selected_branch <= BRANCH_1;
                            // output_found <= 1;
                    end

                    default: ;
                endcase
            end

            else begin
                timeout_counter <= timeout_counter + 1;
            end  
        end
    end


    // ----- COARSE DAC STEP -----

    always_ff @(posedge clk) begin
        if (reset || sleep) begin
            coarse_step1 <= 8'b0000_0000;
            coarse_step2 <= 7'b000_0000;
        end else begin
            case (coarse_step_counter)
                1:  begin 
                        coarse_step1 <= 8'b0000_0001; 
                        coarse_step2 <= 7'b000_0000; 
                    end
                2:  begin 
                        coarse_step1 <= 8'b0000_0011; 
                        coarse_step2 <= 7'b000_0000; 
                    end
                3:  begin 
                        coarse_step1 <= 8'b0000_0111; 
                        coarse_step2 <= 7'b000_0000; 
                    end
                4:  begin 
                        coarse_step1 <= 8'b0000_1111; 
                        coarse_step2 <= 7'b000_0000; 
                    end
                5:  begin 
                        coarse_step1 <= 8'b0001_1111; 
                        coarse_step2 <= 7'b000_0000; 
                    end
                6:  begin 
                        coarse_step1 <= 8'b0011_1111; 
                        coarse_step2 <= 7'b000_0000; 
                    end
                7:  begin 
                        coarse_step1 <= 8'b0111_1111; 
                        coarse_step2 <= 7'b000_0000; 
                    end
                8:  begin 
                        coarse_step1 <= 8'b1111_1111; 
                        coarse_step2 <= 7'b000_0000; 
                    end
                9:  begin 
                        coarse_step1 <= 8'b1111_1111; 
                        coarse_step2 <= 7'b000_0001; 
                    end
                10: begin 
                        coarse_step1 <= 8'b1111_1111; 
                        coarse_step2 <= 7'b000_0011; 
                    end
                11: begin 
                        coarse_step1 <= 8'b1111_1111; 
                        coarse_step2 <= 7'b000_0111; 
                    end
                12: begin 
                        coarse_step1 <= 8'b1111_1111; 
                        coarse_step2 <= 7'b000_1111; 
                    end
                13: begin 
                        coarse_step1 <= 8'b1111_1111; 
                        coarse_step2 <= 7'b001_1111; 
                    end
                14: begin 
                        coarse_step1 <= 8'b1111_1111; 
                        coarse_step2 <= 7'b011_1111; 
                    end
                15: begin 
                        coarse_step1 <= 8'b1111_1111; 
                        coarse_step2 <= 7'b111_1111; 
                    end
                default: begin 
                        coarse_step1 <= '0; 
                        coarse_step2 <= '0; 
                    end
            endcase
        end
    end


    // ----- SWITCHING BETWEEN BRANCHES -----

    always_ff @(posedge clk) begin

        if (reset) begin
            switch_state   <= SW_IDLE;
            active_branch  <= BRANCH_1;
            target_branch  <= BRANCH_1;
            switch_counter <= 0;

            // branch 1 active at reset
            swbrn1 <= 1'b1;
            swcap1 <= 1'b1;

            swbrn2 <= 1'b0;
            swcap2 <= 1'b0; 

            swbrn3 <= 1'b0;
            swcap3 <= 1'b0;

            // swdrn1 <= 1;
            // swdrn2 <= 1;
            // swdrn3 <= 1;
        end 

        else if (sleep) begin
            switch_state   <= SW_IDLE;
            active_branch  <= BRANCH_1;
            target_branch  <= BRANCH_1;
            switch_counter <= 0;

            // no branch active when asleep
            swbrn1 <= 1'b0;
            swcap1 <= 1'b0;

            swbrn2 <= 1'b0;
            swcap2 <= 1'b0;

            swbrn3 <= 1'b0;
            swcap3 <= 1'b0;

            // swdrn1 <= 1;
            // swdrn2 <= 1;
            // swdrn3 <= 1;
        end
        
        else begin

            // swdrn1 <= 0;
            // swdrn2 <= 0;
            // swdrn3 <= 0;

            if (selected_branch != target_branch) begin
                target_branch <= selected_branch;
            end

            case (switch_state)

                SW_IDLE: begin
                        if (target_branch != active_branch) begin
                            switch_state   <= SW_CAP_OFF;
                            switch_counter <= 0;
                        end
                end

                SW_CAP_OFF: begin
                        case (active_branch)
                            BRANCH_1: swcap1 <= 1'b0;
                            BRANCH_2: swcap2 <= 1'b0;
                            BRANCH_3: swcap3 <= 1'b0;
                            default: ;
                        endcase

                        if (switch_counter >= SW_TIMEOUT - 1) begin
                            switch_state   <= SW_BR_OFF;
                            switch_counter <= 0;
                        end else begin
                            switch_counter <= switch_counter + 1;
                        end
                end

                SW_BR_OFF: begin
                        case (active_branch)
                            BRANCH_1: swbrn1 <= 1'b0;
                            BRANCH_2: swbrn2 <= 1'b0;
                            BRANCH_3: swbrn3 <= 1'b0;
                            default: ;
                        endcase

                        if (switch_counter >= SW_TIMEOUT - 1) begin
                            switch_state   <= SW_BR_ON;
                            switch_counter <= 0;
                        end else begin
                            switch_counter <= switch_counter + 1;
                        end
                end

                SW_BR_ON: begin
                        case (target_branch)
                            BRANCH_1: swbrn1 <= 1'b1;
                            BRANCH_2: swbrn2 <= 1'b1;
                            BRANCH_3: swbrn3 <= 1'b1;
                            default: ;
                        endcase

                        if (switch_counter >= SW_TIMEOUT - 1) begin
                            switch_state   <= SW_CAP_ON;
                            switch_counter <= 0;
                        end else begin
                            switch_counter <= switch_counter + 1;
                        end
                end

                SW_CAP_ON: begin
                        case (target_branch)
                            BRANCH_1: swcap1 <= 1'b1;
                            BRANCH_2: swcap2 <= 1'b1;
                            BRANCH_3: swcap3 <= 1'b1;
                            default: ;
                        endcase

                        if (switch_counter >= SW_TIMEOUT - 1) begin
                            active_branch  <= target_branch;  // commit the switch
                            switch_state   <= SW_IDLE;
                            switch_counter <= 0;
                        end else begin
                            switch_counter <= switch_counter + 1;
                        end
                end

                default: switch_state <= SW_IDLE;
            endcase
        end
    end




endmodule