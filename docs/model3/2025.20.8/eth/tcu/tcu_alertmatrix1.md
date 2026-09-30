---
layout: default
title: "TCU_alertMatrix1 (0x5C0) — TCU ECU, Tesla Model 3 2025.20.8 ETH"
description: "TCU ECU message: alert matrix1. Ethernet-side message TCU_alertMatrix1 of TCU ECU for Tesla Model 3 firmware 2025.20.8, 6 signals (TCU_w001_IMSRegistrationFailed, TCU_w002_CellRegRejected, TCU_w003_ECallFailed, TCU_w004_MSDTransmissionFailed and 2 more). Bit layout, scaling, units and value tables."
---

# TCU_alertMatrix1 (0x5C0) — TCU ECU, Tesla Model 3 2025.20.8 ETH

TCU ECU message: alert matrix1. This page documents the 6 signals of TCU_alertMatrix1 as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `TCU_alertMatrix1` |
| Ethernet-side id | 0x5C0 (1472) |
| ECU | [TCU ECU](../../tcu.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | TCU |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 6 |

## Signals of TCU_alertMatrix1

Tesla Model 3 CAN bus signals in `TCU_alertMatrix1`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `TCU_w001_IMSRegistrationFailed` | TCU ECU: w001 IMS registration failed | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU_w002_CellRegRejected` | TCU ECU: w002 cell reg rejected | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU_w003_ECallFailed` | TCU ECU: w003 e call failed | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU_w004_MSDTransmissionFailed` | TCU ECU: w004 MSD transmission failed | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU_w005_SIMSlotError` | TCU ECU: w005 SIM slot error | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU_w006_MpssUnavailable` | TCU ECU: w006 mpss unavailable | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All TCU ECU messages (TCU)](../../tcu.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
