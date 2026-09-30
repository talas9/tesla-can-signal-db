---
layout: default
title: "PMR_state4 (0x1D8) — PMR ECU, Tesla Model 3 2025.20.8 ETH"
description: "PMR ECU message: state4. Ethernet-side message PMR_state4 of PMR ECU for Tesla Model 3 firmware 2025.20.8, 1 signals (PMR_hvilStatus). Bit layout, scaling, units and value tables."
---

# PMR_state4 (0x1D8) — PMR ECU, Tesla Model 3 2025.20.8 ETH

PMR ECU message: state4. This page documents the 1 signals of PMR_state4 as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `PMR_state4` |
| Ethernet-side id | 0x1D8 (472) |
| ECU | [PMR ECU](../../pmr.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | PMR |
| Frame length | 8 bytes |
| Cycle time | 10 ms |
| Signals | 1 |

## Signals of PMR_state4

Tesla Model 3 CAN bus signals in `PMR_state4`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PMR_hvilStatus` | PMR ECU: hvil status | 37\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DISABLED`<br>1 = `OPEN`<br>2 = `CLOSED`<br>3 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All PMR ECU messages (PMR)](../../pmr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
