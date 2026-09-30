---
layout: default
title: "SCCM_udsResponse (0x690) — Steering column control module, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Steering column control module message: uds response. Tesla Model 3 CAN bus message SCCM_udsResponse (0x690) of Steering column control module, firmware 2026.26.6.5, 8 signals (SCCM_functionalResponseData_0, SCCM_functionalResponseData_1, SCCM_functionalResponseData_2, SCCM_functionalResponseData_3 and 4 more). Bit layout, scaling, units and value tables."
---

# SCCM_udsResponse (0x690) — Steering column control module, Tesla Model 3 2026.26.6.5 VEH CAN

Steering column control module message: uds response; frame length from the layout, not yet observed on a vehicle bus. This page documents the 8 signals of SCCM_udsResponse as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `SCCM_udsResponse` |
| CAN id | 0x690 (1680) |
| ECU | [Steering column control module](../../sccm.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | SCCM |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 8 |

## Signals of SCCM_udsResponse

Tesla Model 3 CAN bus signals in `SCCM_udsResponse`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `SCCM_functionalResponseData_0` | Steering column control module: functional response data 0 | 7\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `SCCM_functionalResponseData_1` | Steering column control module: functional response data 1 | 15\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `SCCM_functionalResponseData_2` | Steering column control module: functional response data 2 | 23\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `SCCM_functionalResponseData_3` | Steering column control module: functional response data 3 | 31\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `SCCM_functionalResponseData_4` | Steering column control module: functional response data 4 | 39\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `SCCM_functionalResponseData_5` | Steering column control module: functional response data 5 | 47\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `SCCM_functionalResponseData_6` | Steering column control module: functional response data 6 | 55\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `SCCM_functionalResponseData_7` | Steering column control module: functional response data 7 | 63\|8 | big-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Steering column control module messages (SCCM)](../../sccm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
