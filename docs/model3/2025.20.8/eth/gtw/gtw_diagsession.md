---
layout: default
title: "GTW_diagSession (0x666) — Gateway, Tesla Model 3 2025.20.8 ETH"
description: "Gateway message: diag session. Ethernet-side message GTW_diagSession of Gateway for Tesla Model 3 firmware 2025.20.8, 6 signals (GTW_diagRemainingSeconds, GTW_diagSessionActive, GTW_diagLevel, GTW_diagUnlockProcedureActive and 2 more). Bit layout, scaling, units and value tables."
---

# GTW_diagSession (0x666) — Gateway, Tesla Model 3 2025.20.8 ETH

Gateway message: diag session. This page documents the 6 signals of GTW_diagSession as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `GTW_diagSession` |
| Ethernet-side id | 0x666 (1638) |
| ECU | [Gateway](../../gtw.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | GTW |
| Frame length | 4 bytes |
| Cycle time | 250 ms |
| Signals | 6 |

## Signals of GTW_diagSession

Tesla Model 3 CAN bus signals in `GTW_diagSession`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `GTW_diagRemainingSeconds` | Seconds remaining for the diagnostics session | 0\|16 | little-endian | unsigned | 1 | 0 | seconds | 0 to 65535 |  | validated |
| `GTW_diagSessionActive` | UDS Session Active | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `GTW_diagLevel` | Current diagnostics level | 17\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 | 0 = `LEVEL_FACTORY`<br>10 = `LEVEL_DIAG_LINK_ACTIVE`<br>25 = `LEVEL_SERVICE`<br>50 = `LEVEL_SERVICE_DRIVE`<br>70 = `LEVEL_PARK_ROBOTAXI`<br>80 = `LEVEL_PARK`<br>100 = `LEVEL_NORMAL_OPERATION` | validated |
| `GTW_diagUnlockProcedureActive` | GTW diag unlock procedure active | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `GTW_diagOverrideActive` | GTW diag level override active | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `GTW_diagPhysicalLinkEstablished` | Physical diag cable connected to the switch and link established | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Gateway messages (GTW)](../../gtw.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
