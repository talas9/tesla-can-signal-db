---
layout: default
title: "VCRIGHT_epbmStatus (0x263) — Right body controller, Tesla Model 3 / Model Y 2026.26.6.5 PARTY CAN"
description: "Right body controller message: epbm status. Tesla Model 3 / Model Y CAN bus message VCRIGHT_epbmStatus (0x263) of Right body controller, firmware 2026.26.6.5, 7 signals (VCRIGHT_cdpRequestState, VCRIGHT_epbmSystemStatusQF, VCRIGHT_epbmUnitStatus, VCRIGHT_epbmCdpState and 3 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_epbmStatus (0x263) — Right body controller, Tesla Model 3 / Model Y 2026.26.6.5 PARTY CAN

Right body controller message: epbm status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 7 signals of VCRIGHT_epbmStatus as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_epbmStatus` |
| CAN id | 0x263 (611) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 7 |

## Signals of VCRIGHT_epbmStatus

Tesla Model 3 / Model Y CAN bus signals in `VCRIGHT_epbmStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_cdpRequestState` | If the Electronic Parking Brake makes a Controlled Deceleration for Parking Brake request, when cdpOkayToRequest is EPB_CDP_REQUEST_INVALID, cdpRequestState shall transition to EPB_CDP_REQUEST_INVALID, untill the Electronic Parking Brake Monitor enters unitStatus PARKED. Stability Control listens to this signal to qualify Controlled Deceleration for Parking Brake requests from the Electronic Parking Brake. | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `EPB_CDP_REQUEST_INVALID`<br>1 = `EPB_CDP_REQUEST_VALID` | plausible |
| `VCRIGHT_epbmSystemStatusQF` | Right body controller: epbm system status QF | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `EPBM_SYSTEM_STATUS_VALID`<br>1 = `EPBM_SYSTEM_STATUS_INVALID` | plausible |
| `VCRIGHT_epbmUnitStatus` | Electronic Parking Brake Monitors state. | 4\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `EPB_STATUS_UNKNOWN`<br>1 = `EPB_STATUS_OPEN`<br>2 = `EPB_STATUS_DYNAMIC`<br>3 = `EPB_STATUS_PARK`<br>4 = `EPB_STATUS_START`<br>5 = `EPB_STATUS_SERVICE`<br>6 = `EPB_STATUS_WINCHMODE`<br>7 = `EPB_STATUS_WINCHMODE_RELEASING`<br>8 = `EPB_STATUS_PARKING`<br>9 = `EPB_STATUS_DYNAMIC_APPLYING`<br>10 = `EPB_STATUS_RELEASING`<br>11 = `EPB_STATUS_SERVICE_RELEASING`<br>12 = `EPB_STATUS_PARK_PENDING`<br>13 = `EPB_STATUS_WINCHMODE_PENDING`<br>14 = `EPB_STATUS_SUMMON`<br>15 = `EPB_STATUS_SUMMON_RELEASING`<br>16 = `EPB_STATUS_SUMMON_PARKING`<br>17 = `EPB_STATUS_EXTERNAL_DYNAMIC`<br>18 = `EPB_STATUS_RELEASING_FOR_EXTERNAL_PARK`<br>19 = `EPB_STATUS_EXTERNAL_PARKING`<br>20 = `EPB_STATUS_DYNAMIC_PARKING`<br>21 = `EPB_STATUS_FREE_ROLL_MODE`<br>22 = `EPB_STATUS_AUTONOMY_OPEN`<br>23 = `EPB_STATUS_COUNT` | plausible |
| `VCRIGHT_epbmCdpState` | Right body controller: epbm cdp state | 9\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `EPB_CDP_STATE_UNKNOWN`<br>1 = `EPB_CDP_STATE_VALID`<br>2 = `EPB_CDP_STATE_FAULT` | plausible |
| `VCRIGHT_epbmRedundantBrakingEnabled` | Right body controller: epbm redundant braking enabled | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `VCRIGHT_epbmStatusCounter` | Right body controller: epbm status counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `VCRIGHT_epbmStatusChecksum` | Right body controller: epbm status checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 PARTY DBC file](../../../../../dbc/AllModels/2026.26.6.5/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/PARTY.json)

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
