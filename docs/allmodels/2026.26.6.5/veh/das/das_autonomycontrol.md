---
layout: default
title: "DAS_autonomyControl (0x20E) — Driver assistance computer, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Driver assistance computer message: autonomy control. Tesla Model 3 / Model Y CAN bus message DAS_autonomyControl (0x20E) of Driver assistance computer, firmware 2026.26.6.5, 12 signals (DAS_autonomyControlChecksum, DAS_autonomyControlCounter, DAS_manualDrivingProhibited, DAS_autonomyControlActive and 8 more). Bit layout, scaling, units and value tables."
---

# DAS_autonomyControl (0x20E) — Driver assistance computer, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Driver assistance computer message: autonomy control; frame length observed on a vehicle bus. This page documents the 12 signals of DAS_autonomyControl as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DAS_autonomyControl` |
| CAN id | 0x20E (526) |
| ECU | [Driver assistance computer](../../das.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | DAS |
| Frame length | 3 bytes |
| Cycle time | 100 ms |
| Signals | 12 |

## Signals of DAS_autonomyControl

Tesla Model 3 / Model Y CAN bus signals in `DAS_autonomyControl`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DAS_autonomyControlChecksum` | Driver assistance computer: autonomy control checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `DAS_autonomyControlCounter` | Driver assistance computer: autonomy control counter | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `DAS_manualDrivingProhibited` | Reports whether the driver is allowed to override autonomy control. | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `DAS_autonomyControlActive` | Denotes if autonomy is active or inactive. | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `DAS_autonomyBehavior` | Current autonomy mode and expected vehicle behaviors; raw 3 = signal not available (SNA) | 13\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `DRIVER`<br>1 = `DRIVERLESS_TAKEOVER`<br>2 = `DRIVERLESS_NO_TAKEOVER`<br>3 = `SNA` | plausible |
| `DAS_epbFallbackRequest` | Driver assistance computer: epb fallback request | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DAS_EPBREQUEST_NO_REQUEST`<br>1 = `DAS_EPBREQUEST_PARK` | plausible |
| `DAS_suppressAPedalOverride` | DAS requesting for A-pedal suppression | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `DAS_useEpbRedundantBraking` | Driver assistance computer: use epb redundant braking | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_epbOnlyStoppingTarget` | Driver assistance computer: epb only stopping target | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DAS_EPB_TARGET_DYNAMIC`<br>1 = `DAS_EPB_TARGET_STATIC` | plausible |
| `DAS_requireFirmBPedalCancel` | Requests firmer brake press requirement to disengage autopilot | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `DAS_authRequestType` | Driver assistance computer: auth request type; raw 3 = signal not available (SNA) | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NONE`<br>1 = `MANUAL_RECOVERY`<br>2 = `AUTONOMOUS_DRIVING`<br>3 = `SNA` | plausible |
| `DAS_brakePedalMuted` | Driver assistance computer: brake pedal muted | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Driver assistance computer messages (DAS)](../../das.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
