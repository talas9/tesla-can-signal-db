---
layout: default
title: "ICR_intrusionDebug (0x2F8) — ICR ECU, Tesla Model 3 2025.20.8 ETH"
description: "ICR ECU message: intrusion debug. Ethernet-side message ICR_intrusionDebug of ICR ECU for Tesla Model 3 firmware 2025.20.8, 5 signals (ICR_loggingPeaksDBG, ICR_loggingCorrelationDBG, ICR_loggingTriggerRangeDBG, ICR_loggingTriggerXPosDBG and 1 more). Bit layout, scaling, units and value tables."
---

# ICR_intrusionDebug (0x2F8) — ICR ECU, Tesla Model 3 2025.20.8 ETH

ICR ECU message: intrusion debug. This page documents the 5 signals of ICR_intrusionDebug as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `ICR_intrusionDebug` |
| Ethernet-side id | 0x2F8 (760) |
| ECU | [ICR ECU](../../icr.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | ICR |
| Frame length | 7 bytes |
| Cycle time | 100 ms |
| Signals | 5 |

## Signals of ICR_intrusionDebug

Tesla Model 3 CAN bus signals in `ICR_intrusionDebug`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `ICR_loggingPeaksDBG` | ICR ECU: logging peaks DBG | 0\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `ICR_loggingCorrelationDBG` | ICR ECU: logging correlation DBG | 16\|16 | little-endian | signed | 0.390625 | 0 | % | -12800 to 12799.609375 |  | plausible |
| `ICR_loggingTriggerRangeDBG` | ICR ECU: logging trigger range DBG | 32\|8 | little-endian | signed | 0.04 | 0 | m | -5.12 to 5.08 |  | plausible |
| `ICR_loggingTriggerXPosDBG` | ICR ECU: logging trigger x pos DBG | 40\|8 | little-endian | signed | 0.04 | 0 | m | -5.12 to 5.08 |  | plausible |
| `ICR_loggingTriggerYPosDBG` | ICR ECU: logging trigger y pos DBG | 48\|8 | little-endian | signed | 0.04 | 0 | m | -5.12 to 5.08 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All ICR ECU messages (ICR)](../../icr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
