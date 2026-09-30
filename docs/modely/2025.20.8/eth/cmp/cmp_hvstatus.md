---
layout: default
title: "CMP_HVStatus (0x227) — A/C compressor, Tesla Model Y 2025.20.8 ETH"
description: "A/C compressor message: HV status. Ethernet-side message CMP_HVStatus of A/C compressor for Tesla Model Y firmware 2025.20.8, 4 signals (CMP_inputHVVoltage, CMP_inputLVVoltage, CMP_inputHVCurrent, CMP_inputHVPower). Bit layout, scaling, units and value tables."
---

# CMP_HVStatus (0x227) — A/C compressor, Tesla Model Y 2025.20.8 ETH

A/C compressor message: HV status. This page documents the 4 signals of CMP_HVStatus as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `CMP_HVStatus` |
| Ethernet-side id | 0x227 (551) |
| ECU | [A/C compressor](../../cmp.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | CMP |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 4 |

## Signals of CMP_HVStatus

Tesla Model Y CAN bus signals in `CMP_HVStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `CMP_inputHVVoltage` | Compressor high voltage input voltage | 0\|16 | little-endian | unsigned | 0.1 | 0 | V | 0 to 6553.4 |  | validated |
| `CMP_inputLVVoltage` | A/C compressor: input LV voltage | 16\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | validated |
| `CMP_inputHVCurrent` | A/C compressor: input HV current | 24\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.4 |  | validated |
| `CMP_inputHVPower` | Compressor high voltage input power | 40\|16 | little-endian | unsigned | 1 | 0 | W | 0 to 65534 |  | validated |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All A/C compressor messages (CMP)](../../cmp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
