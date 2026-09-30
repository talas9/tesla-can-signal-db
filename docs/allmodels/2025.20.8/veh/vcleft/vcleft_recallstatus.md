---
layout: default
title: "VCLEFT_recallStatus (0x744) — Left body controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Left body controller message: recall status. Tesla Model 3 / Model Y CAN bus message VCLEFT_recallStatus (0x744) of Left body controller, firmware 2025.20.8, 4 signals (VCLEFT_systemRecallStatus, VCLEFT_seatRecallStatus, VCLEFT_columnRecallStatus, VCLEFT_mirrorRecallStatus). Bit layout, scaling, units and value tables."
---

# VCLEFT_recallStatus (0x744) — Left body controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Left body controller message: recall status; frame length observed on a vehicle bus. This page documents the 4 signals of VCLEFT_recallStatus as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_recallStatus` |
| CAN id | 0x744 (1860) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCLEFT |
| Frame length | 1 bytes |
| Cycle time | 1000 ms |
| Signals | 4 |

## Signals of VCLEFT_recallStatus

Tesla Model 3 / Model Y CAN bus signals in `VCLEFT_recallStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_systemRecallStatus` | Left body controller: system recall status; raw 0 = signal not available (SNA) | 0\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `RECALL_SNA`<br>1 = `RECALL_IN_PROGRESS`<br>2 = `RECALL_COMPLETE`<br>3 = `RECALL_INTERRUPTED` | validated |
| `VCLEFT_seatRecallStatus` | Left body controller: seat recall status; raw 0 = signal not available (SNA) | 2\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `RECALL_SNA`<br>1 = `RECALL_IN_PROGRESS`<br>2 = `RECALL_COMPLETE`<br>3 = `RECALL_INTERRUPTED` | validated |
| `VCLEFT_columnRecallStatus` | Left body controller: column recall status; raw 0 = signal not available (SNA) | 4\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `RECALL_SNA`<br>1 = `RECALL_IN_PROGRESS`<br>2 = `RECALL_COMPLETE`<br>3 = `RECALL_INTERRUPTED` | validated |
| `VCLEFT_mirrorRecallStatus` | Recall status for the left side view mirror; raw 0 = signal not available (SNA) | 6\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `RECALL_SNA`<br>1 = `RECALL_IN_PROGRESS`<br>2 = `RECALL_COMPLETE`<br>3 = `RECALL_INTERRUPTED` | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
