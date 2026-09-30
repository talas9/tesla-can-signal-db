---
layout: default
title: "SCM_alertMatrix1 (0x32F) — SCM ECU, Tesla Model Y 2025.20.8 VEH CAN"
description: "SCM ECU message: alert matrix1. Tesla Model Y CAN bus message SCM_alertMatrix1 (0x32F) of SCM ECU, firmware 2025.20.8, 2 signals (SCM_a027_externalIsolationLow, SCM_a044_proximityRationality). Bit layout, scaling, units and value tables."
---

# SCM_alertMatrix1 (0x32F) — SCM ECU, Tesla Model Y 2025.20.8 VEH CAN

SCM ECU message: alert matrix1; frame length from the layout, not yet observed on a vehicle bus. This page documents the 2 signals of SCM_alertMatrix1 as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `SCM_alertMatrix1` |
| CAN id | 0x32F (815) |
| ECU | [SCM ECU](../../scm.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | SCM |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 2 |

## Signals of SCM_alertMatrix1

Tesla Model Y CAN bus signals in `SCM_alertMatrix1`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `SCM_a027_externalIsolationLow` | SCM ECU: a027 external isolation low | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCM_a044_proximityRationality` | SCM ECU: a044 proximity rationality | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All SCM ECU messages (SCM)](../../scm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
