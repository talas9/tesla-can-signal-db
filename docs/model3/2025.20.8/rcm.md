---
layout: default
title: "Restraint control module (RCM) CAN messages and signals — Tesla Model 3 2025.20.8"
description: "Tesla Model 3 RCM CAN bus messages and signals of the Restraint control module (RCM) for firmware 2025.20.8: 9 messages, 1766 signals with bit layout, scaling and value tables."
---

# Restraint control module (RCM) CAN messages and signals — Tesla Model 3 2025.20.8

All 9 messages of the Restraint control module (RCM) documented for Tesla Model 3 firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`RCM_inertial1`](ch/rcm/rcm_inertial1.md) | CH | 0x101 | 8 | 20 ms | 8 |
| [`RCM_inertial2`](ch/rcm/rcm_inertial2.md) | CH | 0x111 | 8 | 20 ms | 9 |
| [`RCM_info`](ch/rcm/rcm_info.md) | CH | 0x351 | 8 | 2000 ms | 11 |
| [`RCM_status`](ch/rcm/rcm_status.md) | CH | 0x211 | 6 | 100 ms | 19 |
| [`RCM_collision`](party/rcm/rcm_collision.md) | PARTY | 0x11 | 4 | 10 ms | 9 |
| [`RCM_nearDeploy`](party/rcm/rcm_neardeploy.md) | PARTY | 0x121 | 4 | 10 ms | 8 |
| [`RCM_alertLog`](eth/rcm/rcm_alertlog.md) | ETH | 0x511 | 8 |  | 1581 |
| [`RCM_alertMatrix`](eth/rcm/rcm_alertmatrix.md) | ETH | 0x371 | 8 | 1000 ms | 120 |
| [`RCM_udsResponse`](eth/rcm/rcm_udsresponse.md) | ETH | 0x651 | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

