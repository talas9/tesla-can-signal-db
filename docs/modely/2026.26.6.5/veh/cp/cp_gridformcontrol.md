---
layout: default
title: "CP_gridFormControl (0x2DD) — Charge port controller, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Charge port controller message: grid form control. Tesla Model Y CAN bus message CP_gridFormControl (0x2DD) of Charge port controller, firmware 2026.26.6.5, 7 signals (CP_gridFormFrequencyRequest, CP_gridFormL1NVoltageRequest, CP_gridFormGroundType, CP_gridFormGridType and 3 more). Bit layout, scaling, units and value tables."
---

# CP_gridFormControl (0x2DD) — Charge port controller, Tesla Model Y 2026.26.6.5 VEH CAN

Charge port controller message: grid form control; frame length from the layout, not yet observed on a vehicle bus. This page documents the 7 signals of CP_gridFormControl as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `CP_gridFormControl` |
| CAN id | 0x2DD (733) |
| ECU | [Charge port controller](../../cp.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | CP |
| Frame length | 6 bytes |
| Cycle time | 1000 ms |
| Signals | 7 |

## Signals of CP_gridFormControl

Tesla Model Y CAN bus signals in `CP_gridFormControl`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `CP_gridFormFrequencyRequest` | Charge port controller: grid form frequency request; raw 4095 = signal not available (SNA) | 0\|12 | little-endian | unsigned | 0.01 | 40 | Hz | 40 to 80.94 | 4095 = `SNA` | validated |
| `CP_gridFormL1NVoltageRequest` | Charge port controller: grid form L1 n voltage request; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | 40 | V | 40 to 294 | 255 = `SNA` | validated |
| `CP_gridFormGroundType` | Charge port controller: grid form ground type; raw 0 = signal not available (SNA) | 24\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `GROUND_TYPE_SNA`<br>1 = `CP_NO_GROUNDING_EVSE_SIDE`<br>2 = `CP_N_L1_MIDPOINT_GROUNDED_EVSE_SIDE`<br>3 = `CP_N_GROUNDED_EVSE_SIDE`<br>4 = `CP_L1_L2_L3_MIDPOINT_GROUNDED_VEH_SIDE` | validated |
| `CP_gridFormGridType` | Charge port controller: grid form grid type; raw 0 = signal not available (SNA) | 27\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `GRID_TYPE_SNA`<br>1 = `CP_N_L1_SINGLE_PHASE`<br>2 = `CP_N_L1_SPLIT_PHASE`<br>3 = `CP_L1_L2_L3_THREE_PHASE`<br>4 = `CP_P_L1L2_N_L3N_DC` | validated |
| `CP_powershareType` | Charge port controller: powershare type | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `POWERSHARE_TYPE_NONE`<br>1 = `POWERSHARE_TYPE_LOAD`<br>2 = `POWERSHARE_TYPE_HOME`<br>3 = `POWERSHARE_TYPE_GRID`<br>4 = `POWERSHARE_TYPE_EPTO` | validated |
| `CP_userPowershareStatus` | Charge port controller: user powershare status | 35\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `POWERSHARE_INACTIVE`<br>1 = `POWERSHARE_HANDSHAKING`<br>2 = `POWERSHARE_INITIALIZING`<br>3 = `POWERSHARE_ENABLED`<br>4 = `POWERSHARE_ENABLED_RECONNECTING_SOON`<br>5 = `POWERSHARE_STOPPED` | validated |
| `CP_powershareStoppedReason` | Charge port controller: powershare stopped reason | 40\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `POWERSHARE_STOP_REASON_NONE`<br>1 = `POWERSHARE_STOP_REASON_FAULT`<br>2 = `POWERSHARE_STOP_REASON_RETRY`<br>3 = `POWERSHARE_STOP_REASON_SOC_TOO_LOW`<br>4 = `POWERSHARE_STOP_REASON_USER`<br>5 = `POWERSHARE_STOP_REASON_GRID_RECONNECTING`<br>6 = `POWERSHARE_STOP_REASON_NOT_AUTHORIZED`<br>7 = `POWERSHARE_STOP_REASON_OFFBOARD_UPDATE`<br>8 = `POWERSHARE_STOP_REASON_AUTHENTICATION_FAILED` | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Charge port controller messages (CP)](../../cp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
