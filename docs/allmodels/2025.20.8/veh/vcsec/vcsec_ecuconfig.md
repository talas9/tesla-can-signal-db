---
layout: default
title: "VCSEC_ecuConfig (0x720) — Vehicle security controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Vehicle security controller message: ecu config. Tesla Model 3 / Model Y CAN bus message VCSEC_ecuConfig (0x720) of Vehicle security controller, firmware 2025.20.8, 3 signals (VCSEC_ECUConfigCRC32, VCSEC_autoWriteConfig, VCSEC_requestForConfig). Bit layout, scaling, units and value tables."
---

# VCSEC_ecuConfig (0x720) — Vehicle security controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Vehicle security controller message: ecu config; frame length from the layout, not yet observed on a vehicle bus. This page documents the 3 signals of VCSEC_ecuConfig as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEC_ecuConfig` |
| CAN id | 0x720 (1824) |
| ECU | [Vehicle security controller](../../vcsec.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCSEC |
| Frame length | 5 bytes |
| Cycle time | 10000 ms |
| Signals | 3 |

## Signals of VCSEC_ecuConfig

Tesla Model 3 / Model Y CAN bus signals in `VCSEC_ecuConfig`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEC_ECUConfigCRC32` | Vehicle security controller: ECU config CRC32 | 0\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_autoWriteConfig` | Vehicle security controller: auto write config | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_requestForConfig` | Vehicle security controller: request for config | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Vehicle security controller messages (VCSEC)](../../vcsec.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
