---
layout: default
title: "A/C compressor (CMP) CAN messages and signals — Tesla Model 3 2025.20.8"
description: "Tesla Model 3 CMP CAN bus messages and signals of the A/C compressor (CMP) for firmware 2025.20.8: 3 messages, 18 signals with bit layout, scaling and value tables."
---

# A/C compressor (CMP) CAN messages and signals — Tesla Model 3 2025.20.8

All 3 messages of the A/C compressor (CMP) documented for Tesla Model 3 firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`CMP_info`](veh/cmp/cmp_info.md) | VEH | 0x363 | 8 | 1000 ms | 13 |
| [`CMP_HVStatus`](eth/cmp/cmp_hvstatus.md) | ETH | 0x227 | 8 | 100 ms | 4 |
| [`CMP_udsResponse`](eth/cmp/cmp_udsresponse.md) | ETH | 0x613 | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

