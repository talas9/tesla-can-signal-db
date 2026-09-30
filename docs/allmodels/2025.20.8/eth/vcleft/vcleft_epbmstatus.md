---
layout: default
title: "VCLEFT_epbmStatus (0x474) — Left body controller, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Left body controller message: epbm status. Ethernet-side message VCLEFT_epbmStatus of Left body controller for Tesla Model 3 / Model Y firmware 2025.20.8, 6 signals (VCLEFT_cdpRequestState, VCLEFT_epbmSystemStatusQF, VCLEFT_epbmUnitStatus, VCLEFT_epbmCdpState and 2 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_epbmStatus (0x474) — Left body controller, Tesla Model 3 / Model Y 2025.20.8 ETH

Left body controller message: epbm status. This page documents the 6 signals of VCLEFT_epbmStatus as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_epbmStatus` |
| Ethernet-side id | 0x474 (1140) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 6 |

## Signals of VCLEFT_epbmStatus

Tesla Model 3 / Model Y CAN bus signals in `VCLEFT_epbmStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_cdpRequestState` | If the Electronic Parking Brake makes a Controlled Deceleration for Parking Brake request, when cdpOkayToRequest is EPB_CDP_REQUEST_INVALID, cdpRequestState shall transition to EPB_CDP_REQUEST_INVALID, untill the Electronic Parking Brake Monitor enters unitStatus PARKED. Stability Control listens to this signal to qualify Controlled Deceleration for Parking Brake requests from the Electronic Parking Brake. | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `EPB_CDP_REQUEST_INVALID`<br>1 = `EPB_CDP_REQUEST_VALID` | validated |
| `VCLEFT_epbmSystemStatusQF` | Left body controller: epbm system status QF | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `EPBM_SYSTEM_STATUS_VALID`<br>1 = `EPBM_SYSTEM_STATUS_INVALID` | validated |
| `VCLEFT_epbmUnitStatus` | Electronic Parking Brake Monitors state. | 4\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `EPB_STATUS_UNKNOWN`<br>1 = `EPB_STATUS_OPEN`<br>2 = `EPB_STATUS_DYNAMIC`<br>3 = `EPB_STATUS_PARK`<br>4 = `EPB_STATUS_START`<br>5 = `EPB_STATUS_SERVICE`<br>6 = `EPB_STATUS_WINCHMODE`<br>7 = `EPB_STATUS_WINCHMODE_RELEASING`<br>8 = `EPB_STATUS_PARKING`<br>9 = `EPB_STATUS_DYNAMIC_APPLYING`<br>10 = `EPB_STATUS_RELEASING`<br>11 = `EPB_STATUS_SERVICE_RELEASING`<br>12 = `EPB_STATUS_PARK_PENDING`<br>13 = `EPB_STATUS_WINCHMODE_PENDING`<br>14 = `EPB_STATUS_SUMMON`<br>15 = `EPB_STATUS_SUMMON_RELEASING`<br>16 = `EPB_STATUS_SUMMON_PARKING`<br>17 = `EPB_STATUS_EXTERNAL_DYNAMIC`<br>18 = `EPB_STATUS_RELEASING_FOR_EXTERNAL_PARK`<br>19 = `EPB_STATUS_EXTERNAL_PARKING`<br>20 = `EPB_STATUS_DYNAMIC_PARKING`<br>21 = `EPB_STATUS_FREE_ROLL_MODE`<br>22 = `EPB_STATUS_AUTONOMY_OPEN`<br>23 = `EPB_STATUS_COUNT` | validated |
| `VCLEFT_epbmCdpState` | Left body controller: epbm cdp state | 9\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `EPB_CDP_STATE_UNKNOWN`<br>1 = `EPB_CDP_STATE_VALID`<br>2 = `EPB_CDP_STATE_FAULT` | validated |
| `VCLEFT_epbmStatusCounter` | Left body controller: epbm status counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `VCLEFT_epbmStatusChecksum` | Left body controller: epbm status checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
