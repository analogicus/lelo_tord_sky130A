// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vlng.h for the primary calling header

#include "Vlng__pch.h"
#include "Vlng__Syms.h"
#include "Vlng___024root.h"

#ifdef VL_DEBUG
VL_ATTR_COLD void Vlng___024root___dump_triggers__stl(Vlng___024root* vlSelf);
#endif  // VL_DEBUG

VL_ATTR_COLD void Vlng___024root___eval_triggers__stl(Vlng___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vlng___024root___eval_triggers__stl\n"); );
    Vlng__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelfRef.__VstlTriggered.set(0U, (IData)(vlSelfRef.__VstlFirstIteration));
#ifdef VL_DEBUG
    if (VL_UNLIKELY(vlSymsp->_vm_contextp__->debug())) {
        Vlng___024root___dump_triggers__stl(vlSelf);
    }
#endif
}
