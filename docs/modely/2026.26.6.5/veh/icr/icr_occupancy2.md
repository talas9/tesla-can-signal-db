---
layout: default
title: "ICR_occupancy2 (0x29E) — ICR ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "ICR ECU message: occupancy2. Tesla Model Y CAN bus message ICR_occupancy2 (0x29E) of ICR ECU, firmware 2026.26.6.5, 16 signals (ICR_classification1RFilt, ICR_classification1LRaw, ICR_classification1RRaw, ICR_classification1LMLOutput and 12 more). Bit layout, scaling, units and value tables."
---

# ICR_occupancy2 (0x29E) — ICR ECU, Tesla Model Y 2026.26.6.5 VEH CAN

ICR ECU message: occupancy2; frame length from the layout, not yet observed on a vehicle bus. This page documents the 16 signals of ICR_occupancy2 as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `ICR_occupancy2` |
| CAN id | 0x29E (670) |
| ECU | [ICR ECU](../../icr.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | ICR |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 16 |

## Signals of ICR_occupancy2

Tesla Model Y CAN bus signals in `ICR_occupancy2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `ICR_classification1RFilt` | Occupant classification status of First Row Right seat; raw 0 = signal not available (SNA) | 0\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `OCCUPANT_CLASSIFICATION_SNA`<br>1 = `OCCUPANT_CLASSIFICATION_INIT`<br>2 = `OCCUPANT_CLASSIFICATION_EMPTY`<br>3 = `OCCUPANT_CLASSIFICATION_OCCUPIED_INHIBIT`<br>4 = `OCCUPANT_CLASSIFICATION_OCCUPIED_ALLOW` | validated |
| `ICR_classification1LRaw` | ICR ECU: classification1 l raw; raw 0 = signal not available (SNA) | 3\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `OCCUPANT_CLASSIFICATION_SNA`<br>1 = `OCCUPANT_CLASSIFICATION_INIT`<br>2 = `OCCUPANT_CLASSIFICATION_EMPTY`<br>3 = `OCCUPANT_CLASSIFICATION_OCCUPIED_INHIBIT`<br>4 = `OCCUPANT_CLASSIFICATION_OCCUPIED_ALLOW` | validated |
| `ICR_classification1RRaw` | ICR ECU: classification1 r raw; raw 0 = signal not available (SNA) | 6\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `OCCUPANT_CLASSIFICATION_SNA`<br>1 = `OCCUPANT_CLASSIFICATION_INIT`<br>2 = `OCCUPANT_CLASSIFICATION_EMPTY`<br>3 = `OCCUPANT_CLASSIFICATION_OCCUPIED_INHIBIT`<br>4 = `OCCUPANT_CLASSIFICATION_OCCUPIED_ALLOW` | validated |
| `ICR_classification1LMLOutput` | ICR ECU: classification1 LML output; raw 255 = signal not available (SNA) | 9\|8 | little-endian | unsigned | 0.004 | 0 | points | 0 to 1.016 | 255 = `SNA` | validated |
| `ICR_classification1RMLOutput` | ICR ECU: classification1 RML output; raw 255 = signal not available (SNA) | 17\|8 | little-endian | unsigned | 0.004 | 0 | points | 0 to 1.016 | 255 = `SNA` | validated |
| `ICR_classification1LqF` | ICR ECU: classification1 lq f | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OCCUPANT_CLASSIFICATION_FAULTED`<br>1 = `OCCUPANT_CLASSIFICATION_NOT_FAULTED` | validated |
| `ICR_blockageClutterFar` | The far clutter output of the blockage algorithm; raw 16 = signal not available (SNA) | 26\|5 | little-endian | signed | 0.5 | -1.5 | dB | -9 to 6 | -16 = `SNA` | validated |
| `ICR_blockageClutterNear` | The near clutter output of the blockage algorithm; raw 16 = signal not available (SNA) | 31\|5 | little-endian | signed | 0.5 | -1.5 | dB | -9 to 6 | -16 = `SNA` | validated |
| `ICR_classification1LFilt` | ICR ECU: classification1 l filt; raw 0 = signal not available (SNA) | 36\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `OCCUPANT_CLASSIFICATION_SNA`<br>1 = `OCCUPANT_CLASSIFICATION_INIT`<br>2 = `OCCUPANT_CLASSIFICATION_EMPTY`<br>3 = `OCCUPANT_CLASSIFICATION_OCCUPIED_INHIBIT`<br>4 = `OCCUPANT_CLASSIFICATION_OCCUPIED_ALLOW` | validated |
| `ICR_classification1RqF` | ICR ECU: classification1 rq f | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OCCUPANT_CLASSIFICATION_FAULTED`<br>1 = `OCCUPANT_CLASSIFICATION_NOT_FAULTED` | validated |
| `ICR_classification1LLatched` | ICR ECU: classification1 l latched; raw 0 = signal not available (SNA) | 40\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `OCCUPANT_CLASSIFICATION_SNA`<br>1 = `OCCUPANT_CLASSIFICATION_INIT`<br>2 = `OCCUPANT_CLASSIFICATION_EMPTY`<br>3 = `OCCUPANT_CLASSIFICATION_OCCUPIED_INHIBIT`<br>4 = `OCCUPANT_CLASSIFICATION_OCCUPIED_ALLOW` | validated |
| `ICR_classification1RLatched` | ICR ECU: classification1 r latched; raw 0 = signal not available (SNA) | 43\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `OCCUPANT_CLASSIFICATION_SNA`<br>1 = `OCCUPANT_CLASSIFICATION_INIT`<br>2 = `OCCUPANT_CLASSIFICATION_EMPTY`<br>3 = `OCCUPANT_CLASSIFICATION_OCCUPIED_INHIBIT`<br>4 = `OCCUPANT_CLASSIFICATION_OCCUPIED_ALLOW` | validated |
| `ICR_classification1LIsLatched` | ICR ECU: classification1 l is latched | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `ICR_classification1RIsLatched` | ICR ECU: classification1 r is latched | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `ICR_occupancy2Counter` | ICR ECU: occupancy2 counter | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `ICR_occupancy2Checksum` | ICR ECU: occupancy2 checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All ICR ECU messages (ICR)](../../icr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
