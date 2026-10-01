---
layout: default
title: "ICR_occupancy2 (0x29E) — ICR ECU, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "ICR ECU message: occupancy2. Ethernet-side message ICR_occupancy2 of ICR ECU for Tesla Model 3 / Model Y firmware 2025.20.8, 9 signals (ICR_userPresenceMLOutput, ICR_childPresenceMLOutput, ICR_classification1RFilt, ICR_classification1LRaw and 5 more). Bit layout, scaling, units and value tables."
---

# ICR_occupancy2 (0x29E) — ICR ECU, Tesla Model 3 / Model Y 2025.20.8 ETH

ICR ECU message: occupancy2. This page documents the 9 signals of ICR_occupancy2 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `ICR_occupancy2` |
| Ethernet-side id | 0x29E (670) |
| ECU | [ICR ECU](../../icr.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | ICR |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 9 |

## Signals of ICR_occupancy2

Tesla Model 3 / Model Y CAN bus signals in `ICR_occupancy2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `ICR_userPresenceMLOutput` | ICR ECU: user presence ML output; raw 255 = signal not available (SNA) | 0\|8 | little-endian | unsigned | 0.004 | 0 | points | 0 to 1.016 | 255 = `SNA` | plausible |
| `ICR_childPresenceMLOutput` | ICR ECU: child presence ML output; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.004 | 0 | points | 0 to 1.016 | 255 = `SNA` | plausible |
| `ICR_classification1RFilt` | Occupant classification status of First Row Right seat; raw 0 = signal not available (SNA) | 16\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `OCCUPANT_CLASSIFICATION_SNA`<br>1 = `OCCUPANT_CLASSIFICATION_INIT`<br>2 = `OCCUPANT_CLASSIFICATION_EMPTY`<br>3 = `OCCUPANT_CLASSIFICATION_OCCUPIED_INHIBIT`<br>4 = `OCCUPANT_CLASSIFICATION_OCCUPIED_ALLOW` | plausible |
| `ICR_classification1LRaw` | ICR ECU: classification1 l raw; raw 0 = signal not available (SNA) | 19\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `OCCUPANT_CLASSIFICATION_SNA`<br>1 = `OCCUPANT_CLASSIFICATION_INIT`<br>2 = `OCCUPANT_CLASSIFICATION_EMPTY`<br>3 = `OCCUPANT_CLASSIFICATION_OCCUPIED_INHIBIT`<br>4 = `OCCUPANT_CLASSIFICATION_OCCUPIED_ALLOW` | plausible |
| `ICR_classification1RRaw` | ICR ECU: classification1 r raw; raw 0 = signal not available (SNA) | 22\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `OCCUPANT_CLASSIFICATION_SNA`<br>1 = `OCCUPANT_CLASSIFICATION_INIT`<br>2 = `OCCUPANT_CLASSIFICATION_EMPTY`<br>3 = `OCCUPANT_CLASSIFICATION_OCCUPIED_INHIBIT`<br>4 = `OCCUPANT_CLASSIFICATION_OCCUPIED_ALLOW` | plausible |
| `ICR_classification1LMLOutput` | ICR ECU: classification1 LML output; raw 255 = signal not available (SNA) | 25\|8 | little-endian | unsigned | 0.004 | 0 | points | 0 to 1.016 | 255 = `SNA` | plausible |
| `ICR_classification1RMLOutput` | ICR ECU: classification1 RML output; raw 255 = signal not available (SNA) | 33\|8 | little-endian | unsigned | 0.004 | 0 | points | 0 to 1.016 | 255 = `SNA` | plausible |
| `ICR_occupancy2Counter` | ICR ECU: occupancy2 counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `ICR_occupancy2Checksum` | ICR ECU: occupancy2 checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All ICR ECU messages (ICR)](../../icr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
