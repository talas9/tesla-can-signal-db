---
layout: default
title: "Gateway (GTW) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8"
description: "Tesla Model 3 / Model Y GTW CAN bus messages and signals of the Gateway (GTW) for firmware 2025.20.8: 18 messages, 693 signals with bit layout, scaling and value tables."
---

# Gateway (GTW) CAN messages and signals — Tesla Model 3 / Model Y 2025.20.8

All 18 messages of the Gateway (GTW) documented for Tesla Model 3 / Model Y firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`GTW_adc4`](eth/gtw/gtw_adc4.md) | ETH | 0x11A | 8 | 1000 ms | 5 |
| [`GTW_alertLog`](eth/gtw/gtw_alertlog.md) | ETH | 0x568 | 8 |  | 136 |
| [`GTW_alertMatrix`](eth/gtw/gtw_alertmatrix.md) | ETH | 0x3E | 8 | 100 ms | 241 |
| [`GTW_autopilotOverride`](eth/gtw/gtw_autopilotoverride.md) | ETH | 0x346 | 8 | 1000 ms | 4 |
| [`GTW_canStatus`](eth/gtw/gtw_canstatus.md) | ETH | 0x388 | 3 | 1000 ms | 16 |
| [`GTW_carConfig`](eth/gtw/gtw_carconfig.md) | ETH | 0x7FF | 8 | 100 ms | 149 |
| [`GTW_carState`](eth/gtw/gtw_carstate.md) | ETH | 0x318 | 8 | 100 ms | 1 |
| [`GTW_diagSession`](eth/gtw/gtw_diagsession.md) | ETH | 0x666 | 4 | 250 ms | 6 |
| [`GTW_ECall`](eth/gtw/gtw_ecall.md) | ETH | 0x378 | 1 | 1000 ms | 2 |
| [`GTW_ethNm`](eth/gtw/gtw_ethnm.md) | ETH | 0x438 | 2 | 100 ms | 5 |
| [`GTW_factoryEcuPresent`](eth/gtw/gtw_factoryecupresent.md) | ETH | 0x560 | 4 | 1000 ms | 28 |
| [`GTW_gearControl`](eth/gtw/gtw_gearcontrol.md) | ETH | 0x678 | 7 | 100 ms | 16 |
| [`GTW_hrl`](eth/gtw/gtw_hrl.md) | ETH | 0x7F1 | 7 | 2000 ms | 6 |
| [`GTW_info`](eth/gtw/gtw_info.md) | ETH | 0x3C | 8 | 2000 ms | 7 |
| [`GTW_mismatchFault`](eth/gtw/gtw_mismatchfault.md) | ETH | 0x55A | 8 | 250 ms | 49 |
| [`GTW_status`](eth/gtw/gtw_status.md) | ETH | 0x348 | 8 | 1000 ms | 8 |
| [`GTW_updateStatus`](eth/gtw/gtw_updatestatus.md) | ETH | 0x3ED | 1 | 1000 ms | 3 |
| [`GTW_vehNm`](eth/gtw/gtw_vehnm.md) | ETH | 0x458 | 7 | 100 ms | 11 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

