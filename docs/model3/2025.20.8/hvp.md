---
layout: default
title: "High-voltage processor (pack contactor and isolation controller) (HVP) CAN messages and signals — Tesla Model 3 2025.20.8"
description: "Tesla Model 3 HVP CAN bus messages and signals of the High-voltage processor (pack contactor and isolation controller) (HVP) for firmware 2025.20.8: 9 messages, 379 signals with bit layout, scaling and value tables."
---

# High-voltage processor (pack contactor and isolation controller) (HVP) CAN messages and signals — Tesla Model 3 2025.20.8

All 9 messages of the High-voltage processor (pack contactor and isolation controller) (HVP) documented for Tesla Model 3 firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`HVP_hvsControl`](veh/hvp/hvp_hvscontrol.md) | VEH | 0x22A | 4 | 100 ms | 5 |
| [`HVP_info`](veh/hvp/hvp_info.md) | VEH | 0x310 | 8 | 10000 ms | 15 |
| [`HVP_log1hz`](veh/hvp/hvp_log1hz.md) | VEH | 0x77A | 8 | 1000 ms | 14 |
| [`HVP_alertLog`](eth/hvp/hvp_alertlog.md) | ETH | 0x50A | 8 |  | 202 |
| [`HVP_alertMatrix`](eth/hvp/hvp_alertmatrix.md) | ETH | 0x3AA | 8 | 1000 ms | 68 |
| [`HVP_contactorState`](eth/hvp/hvp_contactorstate.md) | ETH | 0x20A | 6 | 1000 ms | 22 |
| [`HVP_debugMessage`](eth/hvp/hvp_debugmessage.md) | ETH | 0x7AA | 8 | 1000 ms | 49 |
| [`HVP_hvpFaults`](eth/hvp/hvp_hvpfaults.md) | ETH | 0x682 | 8 | 100 ms | 3 |
| [`HVP_udsResponse`](eth/hvp/hvp_udsresponse.md) | ETH | 0x611 | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

