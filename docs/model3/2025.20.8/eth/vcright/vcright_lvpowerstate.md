---
layout: default
title: "VCRIGHT_LVPowerState (0x225) — Right body controller, Tesla Model 3 2025.20.8 ETH"
description: "Right body controller message: LV power state. Ethernet-side message VCRIGHT_LVPowerState of Right body controller for Tesla Model 3 firmware 2025.20.8, 16 signals (VCRIGHT_ptcLVState, VCRIGHT_ocsLVState, VCRIGHT_premAudioLVState, VCRIGHT_rearOilPumpLVState and 12 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_LVPowerState (0x225) — Right body controller, Tesla Model 3 2025.20.8 ETH

Right body controller message: LV power state. This page documents the 16 signals of VCRIGHT_LVPowerState as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_LVPowerState` |
| Ethernet-side id | 0x225 (549) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCRIGHT |
| Frame length | 4 bytes |
| Cycle time | 100 ms |
| Signals | 16 |

## Signals of VCRIGHT_LVPowerState

Tesla Model 3 CAN bus signals in `VCRIGHT_LVPowerState`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_ptcLVState` | Right body controller: ptc LV state | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_OFF`<br>1 = `LV_ON`<br>2 = `LV_GOING_DOWN`<br>3 = `LV_FAULT` | plausible |
| `VCRIGHT_ocsLVState` | Right body controller: ocs LV state | 2\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_OFF`<br>1 = `LV_ON`<br>2 = `LV_GOING_DOWN`<br>3 = `LV_FAULT` | plausible |
| `VCRIGHT_premAudioLVState` | Right body controller: prem audio LV state | 4\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_OFF`<br>1 = `LV_ON`<br>2 = `LV_GOING_DOWN`<br>3 = `LV_FAULT` | plausible |
| `VCRIGHT_rearOilPumpLVState` | Right body controller: rear oil pump LV state | 6\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_OFF`<br>1 = `LV_ON`<br>2 = `LV_GOING_DOWN`<br>3 = `LV_FAULT` | plausible |
| `VCRIGHT_tunerLVState` | Right body controller: tuner LV state | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_OFF`<br>1 = `LV_ON`<br>2 = `LV_GOING_DOWN`<br>3 = `LV_FAULT` | plausible |
| `VCRIGHT_hvcLVState` | Right body controller: hvc LV state | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_OFF`<br>1 = `LV_ON`<br>2 = `LV_GOING_DOWN`<br>3 = `LV_FAULT` | plausible |
| `VCRIGHT_rcmLVState` | Right body controller: rcm LV state | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_OFF`<br>1 = `LV_ON`<br>2 = `LV_GOING_DOWN`<br>3 = `LV_FAULT` | plausible |
| `VCRIGHT_lumbarLVState` | Right body controller: lumbar LV state | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_OFF`<br>1 = `LV_ON`<br>2 = `LV_GOING_DOWN`<br>3 = `LV_FAULT` | plausible |
| `VCRIGHT_cntctrPwrState` | Right body controller: cntctr pwr state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_eFuseLockoutStatus` | Right body controller: e fuse lockout status | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `EFUSE_LOCKOUT_STATUS_IDLE`<br>1 = `EFUSE_LOCKOUT_STATUS_PENDING`<br>2 = `EFUSE_LOCKOUT_STATUS_ACTIVE` | plausible |
| `VCRIGHT_swEnStatus` | Status of the internal switched power rail on the board | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_vehiclePowerStateDBG` | Right body controller: vehicle power state DBG | 21\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VEHICLE_POWER_STATE_OFF`<br>1 = `VEHICLE_POWER_STATE_CONDITIONING`<br>2 = `VEHICLE_POWER_STATE_ACCESSORY`<br>3 = `VEHICLE_POWER_STATE_DRIVE` | plausible |
| `VCRIGHT_parkLVState` | Right body controller: park LV state | 23\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_OFF`<br>1 = `LV_ON`<br>2 = `LV_GOING_DOWN`<br>3 = `LV_FAULT` | plausible |
| `VCRIGHT_icrLVState` | Right body controller: icr LV state | 25\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_OFF`<br>1 = `LV_ON`<br>2 = `LV_GOING_DOWN`<br>3 = `LV_FAULT` | plausible |
| `VCRIGHT_interiorCameraLedLVState` | Right body controller: interior camera led LV state | 27\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_OFF`<br>1 = `LV_ON`<br>2 = `LV_GOING_DOWN`<br>3 = `LV_FAULT` | plausible |
| `VCRIGHT_diLVState` | Right body controller: di LV state | 29\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_OFF`<br>1 = `LV_ON`<br>2 = `LV_GOING_DOWN`<br>3 = `LV_FAULT` | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
