---
layout: default
title: "APS_status2 (0x41C) — Driver assistance computer (secondary), Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Driver assistance computer (secondary) message: status2. Tesla Model 3 / Model Y CAN bus message APS_status2 (0x41C) of Driver assistance computer (secondary), firmware 2026.26.6.5, 6 signals (APS_autonomyBehavior, APS_status2Counter, APS_cameraMitigationRequired, APS_autonomyControlActive and 2 more). Bit layout, scaling, units and value tables."
---

# APS_status2 (0x41C) — Driver assistance computer (secondary), Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Driver assistance computer (secondary) message: status2; frame length from the layout, not yet observed on a vehicle bus. This page documents the 6 signals of APS_status2 as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APS_status2` |
| CAN id | 0x41C (1052) |
| ECU | [Driver assistance computer (secondary)](../../aps.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | APS |
| Frame length | 2 bytes |
| Cycle time | 100 ms |
| Signals | 6 |

## Signals of APS_status2

Tesla Model 3 / Model Y CAN bus signals in `APS_status2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APS_autonomyBehavior` | Reports the current autonomy mode indicated by Autopilot Secondary (APS); raw 3 = signal not available (SNA) | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `DRIVER`<br>1 = `DRIVERLESS_TAKEOVER`<br>2 = `DRIVERLESS_NO_TAKEOVER`<br>3 = `SNA` | validated |
| `APS_status2Counter` | Driver assistance computer (secondary): status2 counter | 2\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `APS_cameraMitigationRequired` | Driver assistance computer (secondary): camera mitigation required | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APS_autonomyControlActive` | Driver assistance computer (secondary): autonomy control active | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APS_A_manualMotionControlState` | Driver assistance computer (secondary): a manual motion control state | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `MANUAL_MOTION_CONTROL_STATE_INIT`<br>1 = `MANUAL_MOTION_CONTROL_STATE_FAULTED`<br>2 = `MANUAL_MOTION_CONTROL_STATE_ACTUATE`<br>3 = `MANUAL_MOTION_CONTROL_STATE_ABORTED`<br>4 = `MANUAL_MOTION_CONTROL_STATE_MIA`<br>5 = `MANUAL_MOTION_CONTROL_STATE_COUNT` | validated |
| `APS_B_manualMotionControlState` | Driver assistance computer (secondary): b manual motion control state | 11\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `MANUAL_MOTION_CONTROL_STATE_INIT`<br>1 = `MANUAL_MOTION_CONTROL_STATE_FAULTED`<br>2 = `MANUAL_MOTION_CONTROL_STATE_ACTUATE`<br>3 = `MANUAL_MOTION_CONTROL_STATE_ABORTED`<br>4 = `MANUAL_MOTION_CONTROL_STATE_MIA`<br>5 = `MANUAL_MOTION_CONTROL_STATE_COUNT` | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer (secondary) messages (APS)](../../aps.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
