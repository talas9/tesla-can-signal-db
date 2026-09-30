---
layout: default
title: "High-voltage processor (pack contactor and isolation controller) (HVP) CAN messages and signals — Tesla Model Y 2026.26.6.5"
description: "Tesla Model Y HVP CAN bus messages and signals of the High-voltage processor (pack contactor and isolation controller) (HVP) for firmware 2026.26.6.5: 9 messages, 356 signals with bit layout, scaling and value tables."
---

# High-voltage processor (pack contactor and isolation controller) (HVP) CAN messages and signals — Tesla Model Y 2026.26.6.5

All 9 messages of the High-voltage processor (pack contactor and isolation controller) (HVP) documented for Tesla Model Y firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`HVP_alertLog`](veh/hvp/hvp_alertlog.md) | VEH | 0x50A | 8 |  | 200 |
| [`HVP_alertMatrix`](veh/hvp/hvp_alertmatrix.md) | VEH | 0x3AA | 8 | 1000 ms | 71 |
| [`HVP_contactorState`](veh/hvp/hvp_contactorstate.md) | VEH | 0x20A | 6 | 1000 ms | 23 |
| [`HVP_debugMessage`](veh/hvp/hvp_debugmessage.md) | VEH | 0x7AA | 8 | 1000 ms | 24 |
| [`HVP_hvpFaults`](veh/hvp/hvp_hvpfaults.md) | VEH | 0x682 | 8 | 100 ms | 3 |
| [`HVP_hvsControl`](veh/hvp/hvp_hvscontrol.md) | VEH | 0x22A | 4 | 100 ms | 5 |
| [`HVP_info`](veh/hvp/hvp_info.md) | VEH | 0x310 | 8 | 10000 ms | 15 |
| [`HVP_log1hz`](veh/hvp/hvp_log1hz.md) | VEH | 0x77A | 8 | 1000 ms | 14 |
| [`HVP_udsResponse`](veh/hvp/hvp_udsresponse.md) | VEH | 0x611 | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

