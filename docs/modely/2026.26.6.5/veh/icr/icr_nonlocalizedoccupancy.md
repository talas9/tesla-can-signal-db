---
layout: default
title: "ICR_nonLocalizedOccupancy (0x29B) — ICR ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "ICR ECU message: non localized occupancy. Tesla Model Y CAN bus message ICR_nonLocalizedOccupancy (0x29B) of ICR ECU, firmware 2026.26.6.5, 11 signals (ICR_lifePresenceMLOutput, ICR_largeOccupantPresenceMLOutput, ICR_lifePresenceRaw, ICR_lifePresenceFilt and 7 more). Bit layout, scaling, units and value tables."
---

# ICR_nonLocalizedOccupancy (0x29B) — ICR ECU, Tesla Model Y 2026.26.6.5 VEH CAN

ICR ECU message: non localized occupancy; frame length from the layout, not yet observed on a vehicle bus. This page documents the 11 signals of ICR_nonLocalizedOccupancy as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `ICR_nonLocalizedOccupancy` |
| CAN id | 0x29B (667) |
| ECU | [ICR ECU](../../icr.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | ICR |
| Frame length | 5 bytes |
| Cycle time | 100 ms |
| Signals | 11 |

## Signals of ICR_nonLocalizedOccupancy

Tesla Model Y CAN bus signals in `ICR_nonLocalizedOccupancy`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `ICR_lifePresenceMLOutput` | ICR ECU: life presence ML output; raw 255 = signal not available (SNA) | 0\|8 | little-endian | unsigned | 0.004 | 0 | points | 0 to 1.016 | 255 = `SNA` | validated |
| `ICR_largeOccupantPresenceMLOutput` | ICR ECU: large occupant presence ML output; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.004 | 0 | points | 0 to 1.016 | 255 = `SNA` | validated |
| `ICR_lifePresenceRaw` | ICR ECU: life presence raw; raw 0 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `LIFE_DETECTED_SNA`<br>1 = `LIFE_NOT_DETECTED`<br>2 = `LIFE_DETECTED` | validated |
| `ICR_lifePresenceFilt` | ICR ECU: life presence filt; raw 0 = signal not available (SNA) | 18\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `LIFE_DETECTED_SNA`<br>1 = `LIFE_NOT_DETECTED`<br>2 = `LIFE_DETECTED` | validated |
| `ICR_largeOccupantPresenceRaw` | ICR ECU: large occupant presence raw; raw 3 = signal not available (SNA) | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SBRStatus_SEAT_UNOCCUPIED`<br>1 = `SBRStatus_SEAT_OCCUPIED`<br>2 = `SBRStatus_SEAT_FAULTED`<br>3 = `SBRStatus_SEAT_SNA` | validated |
| `ICR_largeOccupantPresenceFilt` | Indicates the filtered detection status of the Large Occupant Presence Detection feature; raw 3 = signal not available (SNA) | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SBRStatus_SEAT_UNOCCUPIED`<br>1 = `SBRStatus_SEAT_OCCUPIED`<br>2 = `SBRStatus_SEAT_FAULTED`<br>3 = `SBRStatus_SEAT_SNA` | validated |
| `ICR_childPresenceFunctionality` | The functionality of the child presence detection app on ICR; raw 2 = signal not available (SNA) | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CHILD_PRESENCE_DISABLED`<br>1 = `CHILD_PRESENCE_ENABLED`<br>2 = `CHILD_PRESENCE_SNA` | validated |
| `ICR_userPresenceFunctionality` | ICR ECU: user presence functionality; raw 2 = signal not available (SNA) | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CHILD_PRESENCE_DISABLED`<br>1 = `CHILD_PRESENCE_ENABLED`<br>2 = `CHILD_PRESENCE_SNA` | validated |
| `ICR_userPresenceMLOutput` | ICR ECU: user presence ML output; raw 255 = signal not available (SNA) | 28\|8 | little-endian | unsigned | 0.004 | 0 | points | 0 to 1.016 | 255 = `SNA` | validated |
| `ICR_userPresenceRaw` | ICR ECU: user presence raw; raw 3 = signal not available (SNA) | 36\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SBRStatus_SEAT_UNOCCUPIED`<br>1 = `SBRStatus_SEAT_OCCUPIED`<br>2 = `SBRStatus_SEAT_FAULTED`<br>3 = `SBRStatus_SEAT_SNA` | validated |
| `ICR_userPresenceFilt` | Detection status of User Presence Detection feature; raw 3 = signal not available (SNA) | 38\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `SBRStatus_SEAT_UNOCCUPIED`<br>1 = `SBRStatus_SEAT_OCCUPIED`<br>2 = `SBRStatus_SEAT_FAULTED`<br>3 = `SBRStatus_SEAT_SNA` | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All ICR ECU messages (ICR)](../../icr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
