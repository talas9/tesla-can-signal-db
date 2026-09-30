---
layout: default
title: "PARK_udsResponse (0x65E) — Parking assist sensors, Tesla Model 3 2025.20.8 ETH"
description: "Parking assist sensors message: uds response. Ethernet-side message PARK_udsResponse of Parking assist sensors for Tesla Model 3 firmware 2025.20.8, 1 signals (PARK_udsResponseData). Bit layout, scaling, units and value tables."
---

# PARK_udsResponse (0x65E) — Parking assist sensors, Tesla Model 3 2025.20.8 ETH

Parking assist sensors message: uds response. This page documents the 1 signals of PARK_udsResponse as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `PARK_udsResponse` |
| Ethernet-side id | 0x65E (1630) |
| ECU | [Parking assist sensors](../../park.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | PARK |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of PARK_udsResponse

Tesla Model 3 CAN bus signals in `PARK_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PARK_udsResponseData` | Parking assist sensors: uds response data | 0\|64 | little-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Parking assist sensors messages (PARK)](../../park.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
