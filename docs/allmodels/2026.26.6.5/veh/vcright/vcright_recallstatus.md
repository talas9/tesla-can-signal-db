---
layout: default
title: "VCRIGHT_recallStatus (0x743) — Right body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Right body controller message: recall status. Tesla Model 3 / Model Y CAN bus message VCRIGHT_recallStatus (0x743) of Right body controller, firmware 2026.26.6.5, 3 signals (VCRIGHT_systemRecallStatus, VCRIGHT_seatRecallStatus, VCRIGHT_mirrorRecallStatus). Bit layout, scaling, units and value tables."
---

# VCRIGHT_recallStatus (0x743) — Right body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Right body controller message: recall status; frame length observed on a vehicle bus. This page documents the 3 signals of VCRIGHT_recallStatus as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_recallStatus` |
| CAN id | 0x743 (1859) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCRIGHT |
| Frame length | 1 bytes |
| Cycle time | 1000 ms |
| Signals | 3 |

## Signals of VCRIGHT_recallStatus

Tesla Model 3 / Model Y CAN bus signals in `VCRIGHT_recallStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_systemRecallStatus` | Recall state of superset of body controls ECUs; raw 0 = signal not available (SNA) | 0\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `RECALL_SNA`<br>1 = `RECALL_IN_PROGRESS`<br>2 = `RECALL_COMPLETE`<br>3 = `RECALL_INTERRUPTED` | validated |
| `VCRIGHT_seatRecallStatus` | Right body controller: seat recall status; raw 0 = signal not available (SNA) | 2\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `RECALL_SNA`<br>1 = `RECALL_IN_PROGRESS`<br>2 = `RECALL_COMPLETE`<br>3 = `RECALL_INTERRUPTED` | validated |
| `VCRIGHT_mirrorRecallStatus` | Recall status for the right side view mirror; raw 0 = signal not available (SNA) | 4\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `RECALL_SNA`<br>1 = `RECALL_IN_PROGRESS`<br>2 = `RECALL_COMPLETE`<br>3 = `RECALL_INTERRUPTED` | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
