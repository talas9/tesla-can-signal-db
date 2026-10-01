---
layout: default
title: "VCRIGHT_status (0x343) — Right body controller, Tesla Model Y 2025.20.8 ETH"
description: "Right body controller message: status. Ethernet-side message VCRIGHT_status of Right body controller for Tesla Model Y firmware 2025.20.8, 10 signals (VCRIGHT_LVBatteryTypeDBG, VCRIGHT_rearDefrostState, VCRIGHT_mirrorHeatState, VCRIGHT_OTAState and 6 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_status (0x343) — Right body controller, Tesla Model Y 2025.20.8 ETH

Right body controller message: status. This page documents the 10 signals of VCRIGHT_status as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_status` |
| Ethernet-side id | 0x343 (835) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 10 |

## Signals of VCRIGHT_status

Tesla Model Y CAN bus signals in `VCRIGHT_status`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_LVBatteryTypeDBG` | Right body controller: LV battery type DBG | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `LV_BATTERY_TYPE_UNKNOWN`<br>1 = `LV_BATTERY_TYPE_ATLASBX_B24_FLOODED`<br>2 = `LV_BATTERY_TYPE_CLARIOS_B24_FLOODED`<br>3 = `LV_BATTERY_TYPE_CATL_LI_ION`<br>4 = `LV_BATTERY_TYPE_TESLA_16V_LI_ION`<br>5 = `LV_BATTERY_TYPE_TESLA_48V_LI_ION` | plausible |
| `VCRIGHT_rearDefrostState` | Right body controller: rear defrost state; raw 0 = signal not available (SNA) | 11\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `HEATER_STATE_SNA`<br>1 = `HEATER_STATE_ON`<br>2 = `HEATER_STATE_OFF`<br>3 = `HEATER_STATE_OFF_UNAVAILABLE`<br>4 = `HEATER_STATE_FAULT` | plausible |
| `VCRIGHT_mirrorHeatState` | Right body controller: mirror heat state; raw 0 = signal not available (SNA) | 14\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `HEATER_STATE_SNA`<br>1 = `HEATER_STATE_ON`<br>2 = `HEATER_STATE_OFF`<br>3 = `HEATER_STATE_OFF_UNAVAILABLE`<br>4 = `HEATER_STATE_FAULT` | plausible |
| `VCRIGHT_OTAState` | Right body controller: OTA state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_5AVoltage` | Right body controller: 5 a voltage | 18\|10 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 5.568880548 |  | plausible |
| `VCRIGHT_vbatProt` | Input voltage monitor to controller | 28\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `VCRIGHT_rationalityAggregateCurrent` | Right body controller: rationality aggregate current | 40\|8 | little-endian | unsigned | 0.5 | 0 | A | 0 to 127.5 |  | plausible |
| `VCRIGHT_eFuseMgmtVoltageMonitor` | Right body controller: e fuse mgmt voltage monitor | 48\|7 | little-endian | unsigned | 0.125 | 0 | V | 0 to 15.875 |  | plausible |
| `VCRIGHT_isSteeringWheelHeaterReq` | Right body controller: is steering wheel heater req | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_steeringWheelHeaterDCTgt` | Right body controller: steering wheel heater DC tgt; raw 127 = signal not available (SNA) | 56\|7 | little-endian | unsigned | 0.01 | 0 | - | 0 to 1 | 127 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
