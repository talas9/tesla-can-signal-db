---
layout: default
title: "EPBL_udsResponse (0x625) — Left electric parking brake, Tesla Model Y 2025.20.8 ETH"
description: "Left electric parking brake message: uds response. Ethernet-side message EPBL_udsResponse of Left electric parking brake for Tesla Model Y firmware 2025.20.8, 2 signals (EPBL_udsResponseData_H, EPBL_udsResponseData_L). Bit layout, scaling, units and value tables."
---

# EPBL_udsResponse (0x625) — Left electric parking brake, Tesla Model Y 2025.20.8 ETH

Left electric parking brake message: uds response. This page documents the 2 signals of EPBL_udsResponse as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `EPBL_udsResponse` |
| Ethernet-side id | 0x625 (1573) |
| ECU | [Left electric parking brake](../../epbl.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | EPBL |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 2 |

## Signals of EPBL_udsResponse

Tesla Model Y CAN bus signals in `EPBL_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `EPBL_udsResponseData_H` | Left electric parking brake: uds response data h | 7\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `EPBL_udsResponseData_L` | Left electric parking brake: uds response data l | 39\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Left electric parking brake messages (EPBL)](../../epbl.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
