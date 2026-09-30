---
layout: default
title: "VCLEFT_pitchEstimation (0x2D7) — Left body controller, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Left body controller message: pitch estimation. Tesla Model 3 CAN bus message VCLEFT_pitchEstimation (0x2D7) of Left body controller, firmware 2026.26.6.5, 6 signals (VCLEFT_pitchEstimateFusionState, VCLEFT_pitchEstimateStateTransitionID, VCLEFT_pitchEstimateArbitratedState, VCLEFT_pitchEstimateOKForAiming and 2 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_pitchEstimation (0x2D7) — Left body controller, Tesla Model 3 2026.26.6.5 VEH CAN

Left body controller message: pitch estimation; frame length observed on a vehicle bus. This page documents the 6 signals of VCLEFT_pitchEstimation as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_pitchEstimation` |
| CAN id | 0x2D7 (727) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCLEFT |
| Frame length | 4 bytes |
| Cycle time | 1000 ms |
| Signals | 6 |

## Signals of VCLEFT_pitchEstimation

Tesla Model 3 CAN bus signals in `VCLEFT_pitchEstimation`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_pitchEstimateFusionState` | Left body controller: pitch estimate fusion state | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `PITCHESTIMATION_STATE_INIT`<br>1 = `PITCHESTIMATION_STATE_WAIT_FOR_SIGNALS_AND_DOORS`<br>2 = `PITCHESTIMATION_STATE_WAIT_FOR_SPEED`<br>3 = `PITCHESTIMATION_STATE_WAIT_FOR_STARTUP`<br>4 = `PITCHESTIMATION_STATE_CALCULATE`<br>7 = `PITCHESTIMATION_STATE_UNKNOWN` | validated |
| `VCLEFT_pitchEstimateStateTransitionID` | Left body controller: pitch estimate state transition ID | 3\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `PITCHESTIMATION_INVALID_STATE_TRANSITION_DEFAULT`<br>1 = `PITCHESTIMATION_LIVE_AX_THEN_NO_LONGER_LIVE_AX`<br>2 = `PITCHESTIMATION_LIVE_AX_THEN_VALIDITIES_NOT_GOOD`<br>3 = `PITCHESTIMATION_UNAVAILABLE_THEN_TRANSPORT`<br>4 = `PITCHESTIMATION_UNAVAILABLE_THEN_NVRAM_DISALLOW`<br>5 = `PITCHESTIMATION_UNAVAILABLE_THEN_SPEED_AND_EPB_NOT_PARKED`<br>6 = `PITCHESTIMATION_UNAVAILABLE_THEN_DELTA_LIVE_READY`<br>7 = `PITCHESTIMATION_UNAVAILABLE_THEN_FUSION_READY`<br>8 = `PITCHESTIMATION_UNAVAILABLE_THEN_LIVE_AX`<br>9 = `PITCHESTIMATION_FUSION_THEN_FUSION_INIT`<br>10 = `PITCHESTIMATION_FUSION_THEN_LIVE_AX`<br>11 = `PITCHESTIMATION_FROZEN_THEN_FUSION_INIT`<br>12 = `PITCHESTIMATION_FROZEN_THEN_VALIDITIES_NOT_GOOD`<br>13 = `PITCHESTIMATION_FROZEN_THEN_FUSION_READY`<br>14 = `PITCHESTIMATION_FROZEN_THEN_LIVE_AX`<br>15 = `PITCHESTIMATION_CARRYOVER_THEN_FUSION_INIT`<br>16 = `PITCHESTIMATION_CARRYOVER_THEN_VALIDITIES_NOT_GOOD`<br>17 = `PITCHESTIMATION_CARRYOVER_THEN_FUSION_READY`<br>18 = `PITCHESTIMATION_CARRYOVER_THEN_LIVE_AX`<br>19 = `PITCHESTIMATION_DELTA_LIVE_THEN_EPB_RELEASING`<br>20 = `PITCHESTIMATION_DELTA_LIVE_THEN_DOORS_CLOSED_LONG_TIME`<br>21 = `PITCHESTIMATION_DELTA_LIVE_THEN_TRANSPORT`<br>22 = `PITCHESTIMATION_DELTA_LIVE_THEN_NVRAM_DISALLOW`<br>23 = `PITCHESTIMATION_DELTA_LIVE_THEN_SPEED_AND_EPB_NOT_PARKED`<br>24 = `PITCHESTIMATION_DELTA_LIVE_THEN_LIVE_AX`<br>25 = `PITCHESTIMATION_DELTA_LIVE_THEN_FUSION_INIT`<br>26 = `PITCHESTIMATION_DELTA_LIVE_THEN_VALIDITIES_NOT_GOOD` | validated |
| `VCLEFT_pitchEstimateArbitratedState` | Left body controller: pitch estimate arbitrated state | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `PITCHESTIMATION_ARBITRATEDSTATE_UNAVAILABLE`<br>1 = `PITCHESTIMATION_ARBITRATEDSTATE_FUSION`<br>2 = `PITCHESTIMATION_ARBITRATEDSTATE_CYCLE_DELTA_LIVE`<br>3 = `PITCHESTIMATION_ARBITRATEDSTATE_CYCLE_DELTA_CARRYOVER`<br>4 = `PITCHESTIMATION_ARBITRATEDSTATE_CYCLE_DELTA_FROZEN`<br>5 = `PITCHESTIMATION_ARBITRATEDSTATE_LIVE_AX_NO_DELTA`<br>7 = `PITCHESTIMATION_ARBITRATEDSTATE_UNKNOWN` | validated |
| `VCLEFT_pitchEstimateOKForAiming` | Left body controller: pitch estimate OK for aiming | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_pitchEstimateFusionRaw` | Left body controller: pitch estimate fusion raw | 12\|10 | little-endian | signed | 0.0002 | 0 | rad | -0.1024 to 0.1022 |  | validated |
| `VCLEFT_pitchEstimate` | Left body controller: pitch estimate; raw 512 = signal not available (SNA) | 22\|10 | little-endian | signed | 0.0002 | 0 | rad | -0.1022 to 0.1022 | -512 = `SNA` | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
