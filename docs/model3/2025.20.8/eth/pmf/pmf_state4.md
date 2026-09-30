---
layout: default
title: "PMF_state4 (0x1D5) — PMF ECU, Tesla Model 3 2025.20.8 ETH"
description: "PMF ECU message: state4. Ethernet-side message PMF_state4 of PMF ECU for Tesla Model 3 firmware 2025.20.8, 1 signals (PMF_hvilStatus). Bit layout, scaling, units and value tables."
---

# PMF_state4 (0x1D5) — PMF ECU, Tesla Model 3 2025.20.8 ETH

PMF ECU message: state4. This page documents the 1 signals of PMF_state4 as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `PMF_state4` |
| Ethernet-side id | 0x1D5 (469) |
| ECU | [PMF ECU](../../pmf.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | PMF |
| Frame length | 8 bytes |
| Cycle time | 10 ms |
| Signals | 1 |

## Signals of PMF_state4

Tesla Model 3 CAN bus signals in `PMF_state4`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PMF_hvilStatus` | PMF ECU: hvil status | 37\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DISABLED`<br>1 = `OPEN`<br>2 = `CLOSED`<br>3 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All PMF ECU messages (PMF)](../../pmf.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
