---
layout: default
title: "VCSEC_udsResponse (0x60B) — Vehicle security controller, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Vehicle security controller message: uds response. Tesla Model Y CAN bus message VCSEC_udsResponse (0x60B) of Vehicle security controller, firmware 2026.26.6.5, 1 signals (VCSEC_udsResponseData). Bit layout, scaling, units and value tables."
---

# VCSEC_udsResponse (0x60B) — Vehicle security controller, Tesla Model Y 2026.26.6.5 VEH CAN

Vehicle security controller message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of VCSEC_udsResponse as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEC_udsResponse` |
| CAN id | 0x60B (1547) |
| ECU | [Vehicle security controller](../../vcsec.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCSEC |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 1 |

## Signals of VCSEC_udsResponse

Tesla Model Y CAN bus signals in `VCSEC_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEC_udsResponseData` | Vehicle security controller: uds response data | 7\|64 | big-endian | unsigned | 1 | 0 |  | 0 to 1.84467440737e+19 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Vehicle security controller messages (VCSEC)](../../vcsec.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
