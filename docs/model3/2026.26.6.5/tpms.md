---
layout: default
title: "Tire pressure monitoring (TPMS) CAN messages and signals — Tesla Model 3 2026.26.6.5"
description: "Tesla Model 3 TPMS CAN bus messages and signals of the Tire pressure monitoring (TPMS) for firmware 2026.26.6.5: 4 messages, 63 signals with bit layout, scaling and value tables."
---

# Tire pressure monitoring (TPMS) CAN messages and signals — Tesla Model 3 2026.26.6.5

All 4 messages of the Tire pressure monitoring (TPMS) documented for Tesla Model 3 firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`TPMS_data`](ch/tpms/tpms_data.md) | CH | 0x31F | 8 | 1000 ms | 8 |
| [`TPMS_info`](ch/tpms/tpms_info.md) | CH | 0x5EF | 8 | 1000 ms | 8 |
| [`TPMS_StatusC`](ch/tpms/tpms_statusc.md) | CH | 0x36F | 8 | 1000 ms | 46 |
| [`TPMS_udsResponse`](ch/tpms/tpms_udsresponse.md) | CH | 0x65F | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

