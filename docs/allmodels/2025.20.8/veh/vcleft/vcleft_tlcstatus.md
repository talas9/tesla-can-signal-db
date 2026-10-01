---
layout: default
title: "VCLEFT_TLCStatus (0x1FB) — Left body controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Left body controller message: TLC status. Tesla Model 3 / Model Y CAN bus message VCLEFT_TLCStatus (0x1FB) of Left body controller, firmware 2025.20.8, 10 signals (VCLEFT_TLCStatusIndex, VCLEFT_TLCTemperature, VCLEFT_TLCLeftTurnVoltage, VCLEFT_TLCRightTurnVoltage and 6 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_TLCStatus (0x1FB) — Left body controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Left body controller message: TLC status; frame length observed on a vehicle bus. This page documents the 10 signals of VCLEFT_TLCStatus as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_TLCStatus` |
| CAN id | 0x1FB (507) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | 50 ms |
| Signals | 10 |

## Signals of VCLEFT_TLCStatus

Tesla Model 3 / Model Y CAN bus signals in `VCLEFT_TLCStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_TLCStatusIndex` | selector | Left body controller: TLC status index | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `0`<br>1 = `1`<br>2 = `INVALID` | plausible |
| `VCLEFT_TLCTemperature` | page 1 | Monitors board temperatures for electrical validation; raw 128 = signal not available (SNA) | 2\|8 | little-endian | signed | 1 | 68 | degC | -59 to 195 | -128 = `SNA` | plausible |
| `VCLEFT_TLCLeftTurnVoltage` | page 1 | Reports voltage for analysis of in field issues; raw 255 = signal not available (SNA) | 10\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.4 | 255 = `SNA` | plausible |
| `VCLEFT_TLCRightTurnVoltage` | page 1 | Reports voltage for analysis of in field issues; raw 255 = signal not available (SNA) | 18\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.4 | 255 = `SNA` | plausible |
| `VCLEFT_TLCState_LeftTurn` | page 1 | Reports trailer light status; raw 5 = signal not available (SNA) | 26\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VCLEFT_TLC_LIGHT_STATE_OFF_WITHOUT_LOAD`<br>1 = `VCLEFT_TLC_LIGHT_STATE_OFF_WITH_LOAD`<br>2 = `VCLEFT_TLC_LIGHT_STATE_ON_WITHOUT_LOAD`<br>3 = `VCLEFT_TLC_LIGHT_STATE_ON_WITH_LOAD`<br>4 = `VCLEFT_TLC_LIGHT_STATE_FAULT`<br>5 = `VCLEFT_TLC_LIGHT_STATE_SNA` | plausible |
| `VCLEFT_TLCState_RightTurn` | page 1 | Reports trailer light status; raw 5 = signal not available (SNA) | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VCLEFT_TLC_LIGHT_STATE_OFF_WITHOUT_LOAD`<br>1 = `VCLEFT_TLC_LIGHT_STATE_OFF_WITH_LOAD`<br>2 = `VCLEFT_TLC_LIGHT_STATE_ON_WITHOUT_LOAD`<br>3 = `VCLEFT_TLC_LIGHT_STATE_ON_WITH_LOAD`<br>4 = `VCLEFT_TLC_LIGHT_STATE_FAULT`<br>5 = `VCLEFT_TLC_LIGHT_STATE_SNA` | plausible |
| `VCLEFT_TLCState_Tail` | page 1 | Reports trailer light status; raw 5 = signal not available (SNA) | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VCLEFT_TLC_LIGHT_STATE_OFF_WITHOUT_LOAD`<br>1 = `VCLEFT_TLC_LIGHT_STATE_OFF_WITH_LOAD`<br>2 = `VCLEFT_TLC_LIGHT_STATE_ON_WITHOUT_LOAD`<br>3 = `VCLEFT_TLC_LIGHT_STATE_ON_WITH_LOAD`<br>4 = `VCLEFT_TLC_LIGHT_STATE_FAULT`<br>5 = `VCLEFT_TLC_LIGHT_STATE_SNA` | plausible |
| `VCLEFT_TLCState_Stop` | page 1 | Reports trailer light status; raw 5 = signal not available (SNA) | 35\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VCLEFT_TLC_LIGHT_STATE_OFF_WITHOUT_LOAD`<br>1 = `VCLEFT_TLC_LIGHT_STATE_OFF_WITH_LOAD`<br>2 = `VCLEFT_TLC_LIGHT_STATE_ON_WITHOUT_LOAD`<br>3 = `VCLEFT_TLC_LIGHT_STATE_ON_WITH_LOAD`<br>4 = `VCLEFT_TLC_LIGHT_STATE_FAULT`<br>5 = `VCLEFT_TLC_LIGHT_STATE_SNA` | plausible |
| `VCLEFT_TLCState_Fog` | page 1 | Reports trailer light status; raw 5 = signal not available (SNA) | 38\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VCLEFT_TLC_LIGHT_STATE_OFF_WITHOUT_LOAD`<br>1 = `VCLEFT_TLC_LIGHT_STATE_OFF_WITH_LOAD`<br>2 = `VCLEFT_TLC_LIGHT_STATE_ON_WITHOUT_LOAD`<br>3 = `VCLEFT_TLC_LIGHT_STATE_ON_WITH_LOAD`<br>4 = `VCLEFT_TLC_LIGHT_STATE_FAULT`<br>5 = `VCLEFT_TLC_LIGHT_STATE_SNA` | plausible |
| `VCLEFT_TLCState_Reverse` | page 1 | Reports trailer light status; raw 5 = signal not available (SNA) | 41\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VCLEFT_TLC_LIGHT_STATE_OFF_WITHOUT_LOAD`<br>1 = `VCLEFT_TLC_LIGHT_STATE_OFF_WITH_LOAD`<br>2 = `VCLEFT_TLC_LIGHT_STATE_ON_WITHOUT_LOAD`<br>3 = `VCLEFT_TLC_LIGHT_STATE_ON_WITH_LOAD`<br>4 = `VCLEFT_TLC_LIGHT_STATE_FAULT`<br>5 = `VCLEFT_TLC_LIGHT_STATE_SNA` | plausible |

## Multiplexing

`VCLEFT_TLCStatusIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (9 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
