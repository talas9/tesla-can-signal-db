---
layout: default
title: "HVP_hvpFaults (0x682) — High-voltage processor (pack contactor and isolation controller), Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "High-voltage processor (pack contactor and isolation controller) message: hvp faults. Ethernet-side message HVP_hvpFaults of High-voltage processor (pack contactor and isolation controller) for Tesla Model 3 / Model Y firmware 2025.20.8, 3 signals (HVP_packContactorHwFault, HVP_fcContactorHwFault, HVP_hvilStatus). Bit layout, scaling, units and value tables."
---

# HVP_hvpFaults (0x682) — High-voltage processor (pack contactor and isolation controller), Tesla Model 3 / Model Y 2025.20.8 ETH

High-voltage processor (pack contactor and isolation controller) message: hvp faults. This page documents the 3 signals of HVP_hvpFaults as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `HVP_hvpFaults` |
| Ethernet-side id | 0x682 (1666) |
| ECU | [High-voltage processor (pack contactor and isolation controller)](../../hvp.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | HVP |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 3 |

## Signals of HVP_hvpFaults

Tesla Model 3 / Model Y CAN bus signals in `HVP_hvpFaults`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `HVP_packContactorHwFault` | High-voltage processor (pack contactor and isolation controller): pack contactor hw fault | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_fcContactorHwFault` | High-voltage processor (pack contactor and isolation controller): fc contactor hw fault | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_hvilStatus` | High-voltage processor (pack contactor and isolation controller): hvil status | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `UNKNOWN`<br>1 = `OK`<br>2 = `FAULT` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All High-voltage processor (pack contactor and isolation controller) messages (HVP)](../../hvp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
