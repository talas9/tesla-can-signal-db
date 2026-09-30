---
layout: default
title: "PCS_thermalStatus (0x2A4) — Power conversion system (on-board charger and DC-DC converter), Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Power conversion system (on-board charger and DC-DC converter) message: thermal status. Tesla Model 3 CAN bus message PCS_thermalStatus (0x2A4) of Power conversion system (on-board charger and DC-DC converter), firmware 2026.26.6.5, 6 signals (PCS_chgPhATemp, PCS_chgPhBTemp, PCS_chgPhCTemp, PCS_dcdcTemp and 2 more). Bit layout, scaling, units and value tables."
---

# PCS_thermalStatus (0x2A4) — Power conversion system (on-board charger and DC-DC converter), Tesla Model 3 2026.26.6.5 VEH CAN

Power conversion system (on-board charger and DC-DC converter) message: thermal status; frame length observed on a vehicle bus. This page documents the 6 signals of PCS_thermalStatus as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PCS_thermalStatus` |
| CAN id | 0x2A4 (676) |
| ECU | [Power conversion system (on-board charger and DC-DC converter)](../../pcs.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | PCS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 6 |

## Signals of PCS_thermalStatus

Tesla Model 3 CAN bus signals in `PCS_thermalStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PCS_chgPhATemp` | Sensed temperature of AC charger phase A; raw 1025 = signal not available (SNA) | 0\|11 | little-endian | signed | 0.1 | 40 | C | -62.4 to 142.3 | -1023 = `SNA` | validated |
| `PCS_chgPhBTemp` | Sensed temperature of AC charger phase B; raw 1025 = signal not available (SNA) | 11\|11 | little-endian | signed | 0.1 | 40 | C | -62.4 to 142.3 | -1023 = `SNA` | validated |
| `PCS_chgPhCTemp` | Sensed temperature of AC charger phase C; raw 1025 = signal not available (SNA) | 22\|11 | little-endian | signed | 0.1 | 40 | C | -62.4 to 142.3 | -1023 = `SNA` | validated |
| `PCS_dcdcTemp` | Sensed temperature of DCDC; raw 1025 = signal not available (SNA) | 33\|11 | little-endian | signed | 0.1 | 40 | C | -62.4 to 142.3 | -1023 = `SNA` | validated |
| `PCS_ambientTemp` | Ambient temperature sensed by the PCS; raw 1025 = signal not available (SNA) | 44\|11 | little-endian | signed | 0.1 | 40 | C | -62.4 to 142.3 | -1023 = `SNA` | validated |
| `PCS_dcdcBusbarTemp` | Sensed temperature of DCDC busbar; raw 511 = signal not available (SNA) | 55\|9 | little-endian | unsigned | 0.2935421 | 0 | C | 0 to 149.706471 | 511 = `SNA` | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Power conversion system (on-board charger and DC-DC converter) messages (PCS)](../../pcs.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
