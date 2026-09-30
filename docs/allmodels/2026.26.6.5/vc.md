---
layout: default
title: "VC ECU (VC) CAN messages and signals — Tesla Model 3 / Model Y 2026.26.6.5"
description: "Tesla Model 3 / Model Y VC CAN bus messages and signals of the VC ECU (VC) for firmware 2026.26.6.5: 5 messages, 101 signals with bit layout, scaling and value tables."
---

# VC ECU (VC) CAN messages and signals — Tesla Model 3 / Model Y 2026.26.6.5

All 5 messages of the VC ECU (VC) documented for Tesla Model 3 / Model Y firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`VC_LVBMS_brickMeasurements`](veh/vc/vc_lvbms_brickmeasurements.md) | VEH | 0x73A | 8 | 1000 ms | 13 |
| [`VC_LVBMS_statusHigh`](veh/vc/vc_lvbms_statushigh.md) | VEH | 0x677 | 8 | 40 ms | 30 |
| [`VC_LVBMS_statusLow`](veh/vc/vc_lvbms_statuslow.md) | VEH | 0x718 | 8 | 200 ms | 39 |
| [`VC_pcsInterface`](veh/vc/vc_pcsinterface.md) | VEH | 0x441 | 8 | 50 ms | 13 |
| [`VC_pcsManagement`](veh/vc/vc_pcsmanagement.md) | VEH | 0x443 | 6 | 500 ms | 6 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

