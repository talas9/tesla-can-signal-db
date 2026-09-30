---
layout: default
title: "GTW_updateStatus (0x3ED) — Gateway, Tesla Model 3 2025.20.8 ETH"
description: "Gateway message: update status. Ethernet-side message GTW_updateStatus of Gateway for Tesla Model 3 firmware 2025.20.8, 3 signals (GTW_i2cUpdateActive, GTW_ecuUpdateStarted, GTW_updateStarted). Bit layout, scaling, units and value tables."
---

# GTW_updateStatus (0x3ED) — Gateway, Tesla Model 3 2025.20.8 ETH

Gateway message: update status. This page documents the 3 signals of GTW_updateStatus as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `GTW_updateStatus` |
| Ethernet-side id | 0x3ED (1005) |
| ECU | [Gateway](../../gtw.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | GTW |
| Frame length | 1 bytes |
| Cycle time | 1000 ms |
| Signals | 3 |

## Signals of GTW_updateStatus

Tesla Model 3 CAN bus signals in `GTW_updateStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `GTW_i2cUpdateActive` | Gateway: i2c update active | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_ecuUpdateStarted` | Reports whether Electronic Control Unit (ECU) update phase is active. | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `GTW_updateStarted` | Main update in progress bit | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Gateway messages (GTW)](../../gtw.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
