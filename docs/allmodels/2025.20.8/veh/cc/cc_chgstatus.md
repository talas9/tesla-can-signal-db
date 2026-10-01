---
layout: default
title: "CC_chgStatus (0x31C) — Charge cable controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Charge cable controller message: chg status. Tesla Model 3 / Model Y CAN bus message CC_chgStatus (0x31C) of Charge cable controller, firmware 2025.20.8, 10 signals (CC_currentLimit, CC_pilotState, CC_numPhases, CC_line1Voltage and 6 more). Bit layout, scaling, units and value tables."
---

# CC_chgStatus (0x31C) — Charge cable controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Charge cable controller message: chg status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 10 signals of CC_chgStatus as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `CC_chgStatus` |
| CAN id | 0x31C (796) |
| ECU | [Charge cable controller](../../cc.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | CC |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 10 |

## Signals of CC_chgStatus

Tesla Model 3 / Model Y CAN bus signals in `CC_chgStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `CC_currentLimit` | Maximum allowable AC current the wall connector is willing to provide; raw 255 = signal not available (SNA) | 0\|8 | little-endian | unsigned | 0.5 | 0 | A | 0 to 127 | 255 = `SNA` | plausible |
| `CC_pilotState` | State of pilot signal reported by the wall connector; raw 3 = signal not available (SNA) | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `CC_PILOT_STATE_READY`<br>1 = `CC_PILOT_STATE_IDLE`<br>2 = `CC_PILOT_STATE_FAULTED`<br>3 = `CC_PILOT_STATE_SNA` | plausible |
| `CC_numPhases` | Number of AC phases expected by wall connector; raw 0 = signal not available (SNA) | 10\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA` | plausible |
| `CC_line1Voltage` | RMS voltage on L1 terminal of wall connector; raw 511 = signal not available (SNA) | 16\|9 | little-endian | unsigned | 1 | 0 | V | 0 to 510 | 511 = `SNA` | plausible |
| `CC_gridGrounding` | Grouding scheme expected by the wall connector; raw 2 = signal not available (SNA) | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CC_GRID_GROUNDING_TN_TT`<br>1 = `CC_GRID_GROUNDING_IT_SplitPhase`<br>2 = `CC_GRID_GROUNDING_SNA` | plausible |
| `CC_deltaTransformer` | Grid configuration expected by the wall connector | 28\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | plausible |
| `CC_numVehCharging` | Number of vehicles charging in wall connector load sharing group | 30\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | plausible |
| `CC_line2Voltage` | RMS voltage on L2 terminal of wall connector; raw 511 = signal not available (SNA) | 33\|9 | little-endian | unsigned | 1 | 0 | V | 0 to 510 | 511 = `SNA` | plausible |
| `CC_line3Voltage` | RMS voltage on L3 terminal of wall connector; raw 511 = signal not available (SNA) | 42\|9 | little-endian | unsigned | 1 | 0 | V | 0 to 510 | 511 = `SNA` | plausible |
| `CC_groundResistance` | Charge cable controller: ground resistance; raw 4095 = signal not available (SNA) | 51\|12 | little-endian | unsigned | 1 | 0 | kOhm | 0 to 4094 | 4094 = `NO_GROUND`<br>4095 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Charge cable controller messages (CC)](../../cc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
