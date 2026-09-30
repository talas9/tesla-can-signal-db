---
layout: default
title: "FC_status (0x214) — FC ECU, Tesla Model 3 2025.20.8 VEH CAN"
description: "FC ECU message: status. Tesla Model 3 CAN bus message FC_status (0x214) of FC ECU, firmware 2025.20.8, 13 signals (FC_protocolVersion, FC_statusCode, FC_deprecated1, FC_deprecated2 and 9 more). Bit layout, scaling, units and value tables."
---

# FC_status (0x214) — FC ECU, Tesla Model 3 2025.20.8 VEH CAN

FC ECU message: status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 13 signals of FC_status as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `FC_status` |
| CAN id | 0x214 (532) |
| ECU | [FC ECU](../../fc.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | FC |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 13 |

## Signals of FC_status

Tesla Model 3 CAN bus signals in `FC_status`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `FC_protocolVersion` | FC ECU: protocol version | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `FC_statusCode` | Fast charger status code; raw 0 = signal not available (SNA) | 8\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `FC_STATUS_NOTREADY_SNA`<br>1 = `FC_STATUS_READY`<br>2 = `FC_STATUS_UPDATE_IN_PROGRESS`<br>3 = `FC_STATUS_DEPRECATED_3`<br>4 = `FC_STATUS_DEPRECATED_4`<br>5 = `FC_STATUS_INT_ISOACTIVE`<br>6 = `FC_STATUS_EXT_ISOACTIVE`<br>7 = `FC_STATUS_POST_OUT_OF_SERVICE`<br>13 = `FC_STATUS_NOTCOMPATIBLE`<br>14 = `FC_STATUS_MALFUNCTION`<br>15 = `FC_STATUS_NODATA` | validated |
| `FC_deprecated1` | FC ECU: deprecated1 | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `FC_deprecated2` | FC ECU: deprecated2 | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `FC_deprecated3` | FC ECU: deprecated3 | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `FC_adapterLocked` | Indicates if the DC adapter is secure or not | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `FC_minCurrentLimit` | Fast charger min current limit | 16\|13 | little-endian | unsigned | 0.1 | 0 | A | 0 to 600 |  | validated |
| `FC_type` | Type of EVSE connected that supports digital communication; raw 7 = signal not available (SNA) | 29\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `FC_TYPE_SUPERCHARGER`<br>1 = `FC_TYPE_CHADEMO`<br>2 = `FC_TYPE_GB`<br>3 = `FC_TYPE_CC_EVSE`<br>4 = `FC_TYPE_COMBO`<br>5 = `FC_TYPE_MC_EVSE`<br>6 = `FC_TYPE_OTHER`<br>7 = `FC_TYPE_SNA` | validated |
| `FC_dcCurrent` | Fast charger DC output current | 32\|14 | little-endian | signed | 0.07324219 | 0 | A | -600 to 599.92675781 |  | validated |
| `FC_postID` | Fast charger charging post ID; raw 3 = signal not available (SNA) | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `FC_POST_MASTER`<br>1 = `FC_POST_SLAVE`<br>2 = `FC_POST_ID_2`<br>3 = `FC_POST_ID_SNA` | validated |
| `FC_dcVoltage` | Fast charger DC voltage | 48\|13 | little-endian | unsigned | 0.07324219 | 0 | V | 0 to 599.92675822 |  | validated |
| `FC_leakageTestNotSupported` | Indicates if the S/X leakage test can be run on this supercharger | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `FC_dischargeSupported` | FC ECU: discharge supported | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All FC ECU messages (FC)](../../fc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
