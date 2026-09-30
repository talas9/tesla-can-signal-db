---
layout: default
title: "BMS_contactorRequest (0x232) — High-voltage battery management system, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "High-voltage battery management system message: contactor request. Ethernet-side message BMS_contactorRequest of High-voltage battery management system for Tesla Model 3 / Model Y firmware 2025.20.8, 2 signals (BMS_internalHvilSenseV, BMS_hvilCoverVSense). Bit layout, scaling, units and value tables."
---

# BMS_contactorRequest (0x232) — High-voltage battery management system, Tesla Model 3 / Model Y 2025.20.8 ETH

High-voltage battery management system message: contactor request. This page documents the 2 signals of BMS_contactorRequest as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_contactorRequest` |
| Ethernet-side id | 0x232 (562) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 2 |

## Signals of BMS_contactorRequest

Tesla Model 3 / Model Y CAN bus signals in `BMS_contactorRequest`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_internalHvilSenseV` | High-voltage battery management system: internal hvil sense v | 16\|16 | little-endian | unsigned | 0.001 | 0 | V | 0 to 65.534 | 65535 = `SNA` | plausible |
| `BMS_hvilCoverVSense` | High-voltage battery management system: hvil cover v sense | 32\|16 | little-endian | unsigned | 0.001 | 0 | V | 0 to 65.534 | 65535 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
