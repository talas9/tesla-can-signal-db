---
layout: default
title: "VC ECU (VC) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8"
description: "Tesla Model 3 / Model Y VC CAN bus messages and signals of the VC ECU (VC) for firmware 2025.20.8: 4 messages, 93 signals with bit layout, scaling and value tables."
---

# VC ECU (VC) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8

All 4 messages of the VC ECU (VC) documented for Tesla Model 3 / Model Y firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`VC_LVBMS_brickMeasurements`](veh/vc/vc_lvbms_brickmeasurements.md) | VEH | 0x73A | 8 | 1000 ms | 13 |
| [`VC_LVBMS_statusHigh`](eth/vc/vc_lvbms_statushigh.md) | ETH | 0x677 | 8 | 33 ms | 30 |
| [`VC_LVBMS_statusLow`](eth/vc/vc_lvbms_statuslow.md) | ETH | 0x718 | 7 | 100 ms | 38 |
| [`VC_pcsInterface`](eth/vc/vc_pcsinterface.md) | ETH | 0x441 | 8 | 50 ms | 12 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

