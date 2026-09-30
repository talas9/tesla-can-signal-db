---
layout: default
title: "HVP_hvpFaults (0x682) — High-voltage processor (pack contactor and isolation controller), Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "High-voltage processor (pack contactor and isolation controller) message: hvp faults. Tesla Model 3 / Model Y CAN bus message HVP_hvpFaults (0x682) of High-voltage processor (pack contactor and isolation controller), firmware 2026.26.6.5, 3 signals (HVP_packContactorHwFault, HVP_fcContactorHwFault, HVP_hvilStatus). Bit layout, scaling, units and value tables."
---

# HVP_hvpFaults (0x682) — High-voltage processor (pack contactor and isolation controller), Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

High-voltage processor (pack contactor and isolation controller) message: hvp faults; frame length observed on a vehicle bus. This page documents the 3 signals of HVP_hvpFaults as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `HVP_hvpFaults` |
| CAN id | 0x682 (1666) |
| ECU | [High-voltage processor (pack contactor and isolation controller)](../../hvp.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | HVP |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 3 |

## Signals of HVP_hvpFaults

Tesla Model 3 / Model Y CAN bus signals in `HVP_hvpFaults`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `HVP_packContactorHwFault` | High-voltage processor (pack contactor and isolation controller): pack contactor hw fault | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `HVP_fcContactorHwFault` | High-voltage processor (pack contactor and isolation controller): fc contactor hw fault | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `HVP_hvilStatus` | High-voltage processor (pack contactor and isolation controller): hvil status | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `UNKNOWN`<br>1 = `OK`<br>2 = `FAULT` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All High-voltage processor (pack contactor and isolation controller) messages (HVP)](../../hvp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
