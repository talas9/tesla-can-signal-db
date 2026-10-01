---
layout: default
title: "DI_vdcRight (0x11A) — Drive inverter, Tesla Model 3 / Model Y 2025.20.8 PARTY CAN"
description: "Drive inverter message: vdc right. Tesla Model 3 / Model Y CAN bus message DI_vdcRight (0x11A) of Drive inverter, firmware 2025.20.8, 11 signals (DI_vdcRightChecksum, DI_vdcRightCounter, DI_vdcCommandTypeFrR, DI_vdcCommandTypeReR and 7 more). Bit layout, scaling, units and value tables."
---

# DI_vdcRight (0x11A) — Drive inverter, Tesla Model 3 / Model Y 2025.20.8 PARTY CAN

Drive inverter message: vdc right; frame length from the layout, not yet observed on a vehicle bus. This page documents the 11 signals of DI_vdcRight as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DI_vdcRight` |
| CAN id | 0x11A (282) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | DI |
| Frame length | 8 bytes |
| Cycle time | 20 ms |
| Signals | 11 |

## Signals of DI_vdcRight

Tesla Model 3 / Model Y CAN bus signals in `DI_vdcRight`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_vdcRightChecksum` | Drive inverter: vdc right checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `DI_vdcRightCounter` | Drive inverter: vdc right counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `DI_vdcCommandTypeFrR` | Drive inverter: vdc command type fr r | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NO_TORQUE_COMMAND`<br>1 = `BTC_TORQUE_COMMAND`<br>2 = `VDC_TORQUE_COMMAND`<br>3 = `VDC_SLIP_COMMAND` | plausible |
| `DI_vdcCommandTypeReR` | Drive inverter: vdc command type re r | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NO_TORQUE_COMMAND`<br>1 = `BTC_TORQUE_COMMAND`<br>2 = `VDC_TORQUE_COMMAND`<br>3 = `VDC_SLIP_COMMAND` | plausible |
| `DI_vdcCommandABSFrR` | Drive inverter: vdc command ABS fr r | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NO_COMMAND`<br>1 = `FEED_THROUGH`<br>2 = `MODIFY_BY_ABS_ALL`<br>3 = `MODIFY_BY_ABS_NO_GMA`<br>4 = `MODIFY_BY_ABS_NO_GMA_NO_EBD` | plausible |
| `DI_vdcCommandABSReR` | Drive inverter: vdc command ABS re r | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NO_COMMAND`<br>1 = `FEED_THROUGH`<br>2 = `MODIFY_BY_ABS_ALL`<br>3 = `MODIFY_BY_ABS_NO_GMA`<br>4 = `MODIFY_BY_ABS_NO_GMA_NO_EBD` | plausible |
| `DI_brakeTorqueTarFrR` | Drive inverter: brake torque tar fr r | 22\|12 | little-endian | unsigned | 3 | -3 | Nm | -3 to 12282 | 0 = `NO_COMMAND` | plausible |
| `DI_brakeTorqueTarReR` | Drive inverter: brake torque tar re r | 34\|12 | little-endian | unsigned | 3 | -3 | Nm | -3 to 12282 | 0 = `NO_COMMAND` | plausible |
| `DI_wheelSlipLimitFrR` | Drive inverter: wheel slip limit fr r | 46\|8 | little-endian | unsigned | 0.004 | -0.004 | 1 | -0.004 to 1 | 0 = `NO_COMMAND` | plausible |
| `DI_wheelSlipLimitReR` | Drive inverter: wheel slip limit re r | 54\|6 | little-endian | unsigned | 0.004 | -0.004 | 1 | -0.004 to 0.248 | 0 = `NO_COMMAND` | plausible |
| `DI_rawLowMuProbability` | Drive inverter: raw low mu probability | 60\|4 | little-endian | unsigned | 0.06666667 | 0 | - | 0 to 1 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 PARTY DBC file](../../../../../dbc/AllModels/2025.20.8/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/PARTY.json)

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
