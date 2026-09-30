---
layout: default
title: "Parking assist sensors (PARK) CAN messages and signals — Tesla Model 3 2026.26.6.5"
description: "Tesla Model 3 PARK CAN bus messages and signals of the Parking assist sensors (PARK) for firmware 2026.26.6.5: 16 messages, 502 signals with bit layout, scaling and value tables."
---

# Parking assist sensors (PARK) CAN messages and signals — Tesla Model 3 2026.26.6.5

All 16 messages of the Parking assist sensors (PARK) documented for Tesla Model 3 firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`PARK_alertLog`](ch/park/park_alertlog.md) | CH | 0x5CE | 8 |  | 268 |
| [`PARK_info`](ch/park/park_info.md) | CH | 0x326 | 8 | 1000 ms | 9 |
| [`PARK_pasFrontMiddle`](ch/park/park_pasfrontmiddle.md) | CH | 0x34E | 5 | 100 ms | 5 |
| [`PARK_pasRearMiddle`](ch/park/park_pasrearmiddle.md) | CH | 0x35E | 5 | 100 ms | 5 |
| [`PARK_pasSides`](ch/park/park_passides.md) | CH | 0x39E | 6 | 100 ms | 6 |
| [`PARK_pscEnvSlot`](ch/park/park_pscenvslot.md) | CH | 0x25E | 8 | 100 ms | 25 |
| [`PARK_pscStatus`](ch/park/park_pscstatus.md) | CH | 0x21E | 8 | 40 ms | 15 |
| [`PARK_pscVehSlot`](ch/park/park_pscvehslot.md) | CH | 0x24E | 8 | 100 ms | 21 |
| [`PARK_sdiFront`](ch/park/park_sdifront.md) | CH | 0x20E | 8 | 40 ms | 8 |
| [`PARK_sdiRear`](ch/park/park_sdirear.md) | CH | 0x22E | 8 | 40 ms | 8 |
| [`PARK_sensorStatusFront`](ch/park/park_sensorstatusfront.md) | CH | 0x32E | 5 | 100 ms | 10 |
| [`PARK_sensorStatusRear`](ch/park/park_sensorstatusrear.md) | CH | 0x33E | 5 | 100 ms | 10 |
| [`PARK_status`](ch/park/park_status.md) | CH | 0x31E | 6 | 500 ms | 8 |
| [`PARK_status2`](ch/park/park_status2.md) | CH | 0x30E | 8 | 250 ms | 15 |
| [`PARK_udsResponse`](ch/park/park_udsresponse.md) | CH | 0x65E | 8 |  | 1 |
| [`PARK_warningMatrix`](ch/park/park_warningmatrix.md) | CH | 0x37E | 8 | 1000 ms | 88 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

