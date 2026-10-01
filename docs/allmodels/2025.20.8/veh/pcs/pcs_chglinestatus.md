---
layout: default
title: "PCS_chgLineStatus (0x264) — Power conversion system (on-board charger and DC-DC converter), Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Power conversion system (on-board charger and DC-DC converter) message: chg line status. Tesla Model 3 / Model Y CAN bus message PCS_chgLineStatus (0x264) of Power conversion system (on-board charger and DC-DC converter), firmware 2025.20.8, 5 signals (PCS_chgInputVoltage, PCS_chgLineCurrent, PCS_chgAcVoltagePresent, PCS_chgInputPower and 1 more). Bit layout, scaling, units and value tables."
---

# PCS_chgLineStatus (0x264) — Power conversion system (on-board charger and DC-DC converter), Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Power conversion system (on-board charger and DC-DC converter) message: chg line status; frame length observed on a vehicle bus. This page documents the 5 signals of PCS_chgLineStatus as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PCS_chgLineStatus` |
| CAN id | 0x264 (612) |
| ECU | [Power conversion system (on-board charger and DC-DC converter)](../../pcs.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | PCS |
| Frame length | 6 bytes |
| Cycle time | 100 ms |
| Signals | 5 |

## Signals of PCS_chgLineStatus

Tesla Model 3 / Model Y CAN bus signals in `PCS_chgLineStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PCS_chgInputVoltage` | RMS value of AC charger's sensed input voltage | 0\|14 | little-endian | unsigned | 0.033 | 0 | V | 0 to 540.639 |  | plausible |
| `PCS_chgLineCurrent` | AC charger's sensed input line current | 14\|9 | little-endian | unsigned | 0.1 | 0 | A | 0 to 50 |  | plausible |
| `PCS_chgAcVoltagePresent` | Indicates whether AC voltage is present on the PCS input | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `PCS_chgInputPower` | Total AC charger input power | 24\|8 | little-endian | unsigned | 0.1 | 0 | kW | 0 to 20 |  | plausible |
| `PCS_chgAcCurrentLimit` | Maximum AC current that can be pulled from a single conductor | 32\|10 | little-endian | unsigned | 0.1 | 0 | A | 0 to 102.3 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Power conversion system (on-board charger and DC-DC converter) messages (PCS)](../../pcs.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
