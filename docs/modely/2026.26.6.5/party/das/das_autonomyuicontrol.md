---
layout: default
title: "DAS_autonomyUiControl (0x248) — Driver assistance computer, Tesla Model Y 2026.26.6.5 PARTY CAN"
description: "Driver assistance computer message: autonomy ui control. Tesla Model Y CAN bus message DAS_autonomyUiControl (0x248) of Driver assistance computer, firmware 2026.26.6.5, 8 signals (DAS_autonomyUiControlChecksum, DAS_autonomyUiControlCounter, DAS_rideState, DAS_infotainmentResetRequested and 4 more). Bit layout, scaling, units and value tables."
---

# DAS_autonomyUiControl (0x248) — Driver assistance computer, Tesla Model Y 2026.26.6.5 PARTY CAN

Driver assistance computer message: autonomy ui control; frame length from the layout, not yet observed on a vehicle bus. This page documents the 8 signals of DAS_autonomyUiControl as defined for Tesla Model Y firmware 2026.26.6.5 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DAS_autonomyUiControl` |
| CAN id | 0x248 (584) |
| ECU | [Driver assistance computer](../../das.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | DAS |
| Frame length | 3 bytes |
| Cycle time | 100 ms |
| Signals | 8 |

## Signals of DAS_autonomyUiControl

Tesla Model Y CAN bus signals in `DAS_autonomyUiControl`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DAS_autonomyUiControlChecksum` | Driver assistance computer: autonomy ui control checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `DAS_autonomyUiControlCounter` | Driver assistance computer: autonomy ui control counter | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `DAS_rideState` | Driver assistance computer: ride state; raw 0 = signal not available (SNA) | 11\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `SNA`<br>1 = `INACTIVE`<br>2 = `SUMMON`<br>3 = `WAITING`<br>4 = `ENROUTE`<br>5 = `IDLE`<br>6 = `PULLOVER` | plausible |
| `DAS_infotainmentResetRequested` | Driver assistance computer: infotainment reset requested | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_rideHailingActive` | Driver assistance computer: ride hailing active | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_autonomyCriticalMode` | Driver assistance computer: autonomy critical mode | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_micFocusRequest` | Driver assistance computer: mic focus request | 17\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `FRONT_DRIVER`<br>2 = `FRONT_PASSENGER`<br>3 = `FRONT_ROW`<br>4 = `ENTIRE_CABIN` | plausible |
| `DAS_autonomyUiBehavior` | Driver assistance computer: autonomy ui behavior; raw 0 = signal not available (SNA) | 20\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `NONE`<br>2 = `RIDEHAILING_ROAMING`<br>3 = `AUTONOMY_SUMMON` | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 PARTY DBC file](../../../../../dbc/ModelY/2026.26.6.5/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/PARTY.json)

## See also

- [All Driver assistance computer messages (DAS)](../../das.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
