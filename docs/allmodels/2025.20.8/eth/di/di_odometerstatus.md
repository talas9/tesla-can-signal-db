---
layout: default
title: "DI_odometerStatus (0x3B6) — Drive inverter, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Drive inverter message: odometer status. Ethernet-side message DI_odometerStatus of Drive inverter for Tesla Model 3 / Model Y firmware 2025.20.8, 3 signals (DI_odometer, DI_odometerStatusCounter, DI_odometerStatusChecksum). Bit layout, scaling, units and value tables."
---

# DI_odometerStatus (0x3B6) — Drive inverter, Tesla Model 3 / Model Y 2025.20.8 ETH

Drive inverter message: odometer status. This page documents the 3 signals of DI_odometerStatus as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DI_odometerStatus` |
| Ethernet-side id | 0x3B6 (950) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DI |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 3 |

## Signals of DI_odometerStatus

Tesla Model 3 / Model Y CAN bus signals in `DI_odometerStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_odometer` | Total traveled distance; raw 4294967295 = signal not available (SNA) | 0\|32 | little-endian | unsigned | 0.001 | 0 | km | 0 to 4294967.294 | 4294967295 = `SNA` | validated |
| `DI_odometerStatusCounter` | Drive inverter: odometer status counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `DI_odometerStatusChecksum` | Drive inverter: odometer status checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
