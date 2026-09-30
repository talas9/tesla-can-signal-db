---
layout: default
title: "DI_locStatus2 (0x4F6) — Drive inverter, Tesla Model 3 2025.20.8 ETH"
description: "Drive inverter message: loc status2. Ethernet-side message DI_locStatus2 of Drive inverter for Tesla Model 3 firmware 2025.20.8, 14 signals (DI_locStatus2Checksum, DI_locStatus2Counter, DI_doublePedalState, DI_autopilotRequest and 10 more). Bit layout, scaling, units and value tables."
---

# DI_locStatus2 (0x4F6) — Drive inverter, Tesla Model 3 2025.20.8 ETH

Drive inverter message: loc status2. This page documents the 14 signals of DI_locStatus2 as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DI_locStatus2` |
| Ethernet-side id | 0x4F6 (1270) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DI |
| Frame length | 7 bytes |
| Cycle time | 100 ms |
| Signals | 14 |

## Signals of DI_locStatus2

Tesla Model 3 CAN bus signals in `DI_locStatus2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_locStatus2Checksum` | Drive inverter: loc status2 checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `DI_locStatus2Counter` | Drive inverter: loc status2 counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `DI_doublePedalState` | Drive inverter: double pedal state | 12\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `DBL_IDLE`<br>1 = `DBL_DRIVING`<br>2 = `DBL_BRKPRESS_RAMPDOWN`<br>3 = `DBL_BRKPRESS_RAMPUP`<br>4 = `DBL_BRKPRESS_PREOVR`<br>5 = `DBL_BRKOVR_RAMPDOWN`<br>6 = `DBL_BRKOVR_RAMPUP`<br>7 = `DBL_BRKSTAND_ARMED1`<br>8 = `DBL_BRKSTAND_ARMED2`<br>9 = `DBL_BRKSTAND_INIT_TRQ_RAMPUP`<br>10 = `DBL_BRKSTAND_TRQ_HOLD`<br>11 = `DBL_BRKSTAND_LAUNCH`<br>12 = `DBL_BRKSTAND_TRQ_RAMPUP_DONE` | validated |
| `DI_autopilotRequest` | Drive inverter: autopilot request | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DI_AP_RQST_IDLE`<br>1 = `DI_AP_RQST_ACTIVATE` | validated |
| `DI_rollPreventionState` | Drive inverter: roll prevention state | 17\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DI_RP_STATE_UNAVAILABLE`<br>1 = `DI_RP_STATE_STANDBY`<br>2 = `DI_RP_STATE_READY`<br>3 = `DI_RP_STATE_BUILD`<br>4 = `DI_RP_STATE_HOLD`<br>5 = `DI_RP_STATE_MAX_BRAKE_TORQUE`<br>6 = `DI_RP_STATE_FAULT`<br>7 = `DI_RP_STATE_INIT` | validated |
| `DI_locIntegratorSaturated` | Drive inverter: loc integrator saturated | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_temporaryOpdActiveAfterLoncCancel` | Drive inverter: temporary opd active after lonc cancel | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_reapplyOnParkRequest` | Drive inverter: reapply on park request | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_regenBlendingState` | Drive inverter: regen blending state | 23\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `BLEND_UNAVAILABLE`<br>1 = `BLEND_STANDBY`<br>2 = `BLEND_ACTIVE`<br>3 = `BLEND_FRICTION_ONLY` | plausible |
| `DI_brakeCpScale` | Drive inverter: brake cp scale | 25\|11 | little-endian | unsigned | 0.005 | 0 | N/N | 0 to 10 |  | validated |
| `DI_rollbackDistance` | Maximum vehicle rollback distance in current stopping event when OPD/Cruise is active | 36\|8 | little-endian | unsigned | 0.005 | 0 | m | 0 to 1.275 |  | validated |
| `DI_lowMuProbabilityConfidence` | Drive inverter: low mu probability confidence | 44\|4 | little-endian | unsigned | 0.06666667 | 0 | - | 0 to 1 |  | validated |
| `DI_pedalAssistCurveSelectForSX` | Drive inverter: pedal assist curve select for SX | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `PEDAL_ASSIST_CURVE_0`<br>3 = `PEDAL_ASSIST_CURVE_3`<br>6 = `PEDAL_ASSIST_CURVE_6`<br>8 = `PEDAL_ASSIST_CURVE_8`<br>11 = `PEDAL_ASSIST_CURVE_11`<br>12 = `PEDAL_ASSIST_CURVE_12`<br>15 = `PEDAL_ASSIST_CURVE_15` | validated |
| `DI_longitudinalControlStack` | Drive inverter: longitudinal control stack; raw 0 = signal not available (SNA) | 52\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `REQUEST_SNA`<br>1 = `LEGACY_CRUISE`<br>2 = `LONC_TORQUE_PROFILER`<br>3 = `VELOCITY_PROFILE_CONTROL`<br>4 = `AEB_CONTROL`<br>5 = `DIRECT_PEDAL_CONTROL`<br>6 = `DIRECT_TORQUE_CONTROL`<br>7 = `VELOCITY_PROFILE_CONTROL_SUPPRESS_CANCEL` | validated |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
