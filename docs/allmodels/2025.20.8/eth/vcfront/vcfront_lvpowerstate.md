---
layout: default
title: "VCFRONT_LVPowerState (0x221) — Front body controller, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Front body controller message: LV power state. Ethernet-side message VCFRONT_LVPowerState of Front body controller for Tesla Model 3 / Model Y firmware 2025.20.8, 23 signals (VCFRONT_LVPowerStateIndex, VCFRONT_vehiclePowerState, VCFRONT_inAccessoryPlus, VCFRONT_LVShuttingDown and 19 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_LVPowerState (0x221) — Front body controller, Tesla Model 3 / Model Y 2025.20.8 ETH

Front body controller message: LV power state. This page documents the 23 signals of VCFRONT_LVPowerState as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_LVPowerState` |
| Ethernet-side id | 0x221 (545) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCFRONT |
| Frame length | 8 bytes |
| Cycle time | 50 ms |
| Signals | 23 |

## Signals of VCFRONT_LVPowerState

Tesla Model 3 / Model Y CAN bus signals in `VCFRONT_LVPowerState`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_LVPowerStateIndex` | selector | Front body controller: LV power state index | 0\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `Mux0`<br>1 = `Mux1` | plausible |
| `VCFRONT_vehiclePowerState` |  | Front body controller: vehicle power state | 5\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VEHICLE_POWER_STATE_OFF`<br>1 = `VEHICLE_POWER_STATE_CONDITIONING`<br>2 = `VEHICLE_POWER_STATE_ACCESSORY`<br>3 = `VEHICLE_POWER_STATE_DRIVE` | plausible |
| `VCFRONT_inAccessoryPlus` |  | Front body controller: in accessory plus | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_LVShuttingDown` |  | Front body controller: LV shutting down | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_LVPowerStateCounter` |  | Front body controller: LV power state counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | plausible |
| `VCFRONT_LVPowerStateChecksum` |  | Front body controller: LV power state checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCFRONT_dirLVRequest` | page 0 | Front body controller: dir LV request | 34\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_OFF`<br>1 = `LV_ON`<br>2 = `LV_GOING_DOWN`<br>3 = `LV_FAULT` | plausible |
| `VCFRONT_cpLVRequest` | page 1 | Front body controller: cp LV request | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_OFF`<br>1 = `LV_ON`<br>2 = `LV_GOING_DOWN`<br>3 = `LV_FAULT` | plausible |
| `VCFRONT_epasLVState` | page 1 | Front body controller: epas LV state | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_OFF`<br>1 = `LV_ON`<br>2 = `LV_GOING_DOWN`<br>3 = `LV_FAULT` | plausible |
| `VCFRONT_hvcLVRequest` | page 1 | Front body controller: hvc LV request | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_OFF`<br>1 = `LV_ON`<br>2 = `LV_GOING_DOWN`<br>3 = `LV_FAULT` | plausible |
| `VCFRONT_tasLVState` | page 1 | Front body controller: tas LV state | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_OFF`<br>1 = `LV_ON`<br>2 = `LV_GOING_DOWN`<br>3 = `LV_FAULT` | plausible |
| `VCFRONT_pcsLVState` | page 1 | Front body controller: pcs LV state | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_OFF`<br>1 = `LV_ON`<br>2 = `LV_GOING_DOWN`<br>3 = `LV_FAULT` | plausible |
| `VCFRONT_CMPDLVState` | page 1 | Front body controller: CMPDLV state | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_OFF`<br>1 = `LV_ON`<br>2 = `LV_GOING_DOWN`<br>3 = `LV_FAULT` | plausible |
| `VCFRONT_hcmlLVState` | page 1 | Front body controller: hcml LV state | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_OFF`<br>1 = `LV_ON`<br>2 = `LV_GOING_DOWN`<br>3 = `LV_FAULT` | plausible |
| `VCFRONT_hcmrLVState` | page 1 | Front body controller: hcmr LV state | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_OFF`<br>1 = `LV_ON`<br>2 = `LV_GOING_DOWN`<br>3 = `LV_FAULT` | plausible |
| `VCFRONT_MCUAudioLVState` | page 1 | Front body controller: MCU audio LV state | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_OFF`<br>1 = `LV_ON`<br>2 = `LV_GOING_DOWN`<br>3 = `LV_FAULT` | plausible |
| `VCFRONT_espValveLVState` | page 1 | Front body controller: esp valve LV state | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_OFF`<br>1 = `LV_ON`<br>2 = `LV_GOING_DOWN`<br>3 = `LV_FAULT` | plausible |
| `VCFRONT_MCUGraphicsLVState` | page 1 | Front body controller: MCU graphics LV state | 28\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LV_OFF`<br>1 = `LV_ON`<br>2 = `LV_GOING_DOWN`<br>3 = `LV_FAULT` | plausible |
| `VC_dcdcSupportRequest` | page 1 | Front body controller: dcdc support request | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VC_hvStateRequest` | page 1 | Reports the request for the High Voltage (HV) system state. | 31\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VC_HV_REQUEST_STATE_NONE`<br>1 = `VC_HV_REQUEST_STATE_LV_SUPPORT_ONLY`<br>2 = `VC_HV_REQUEST_STATE_HV_UP`<br>7 = `VC_HV_REQUEST_STATE_RESERVED` | plausible |
| `VC_persistAccPowerRequestOverridden` | page 1 | Front body controller: persist acc power request overridden | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VC_accPortPowerRequest` | page 1 | Front body controller: acc port power request | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VC_persistAccPortPowerState` | page 1 | Front body controller: persist acc port power state | 41\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STATE_KEEP_AWAKE_DISARMED`<br>1 = `STATE_KEEP_AWAKE_ARMED`<br>2 = `STATE_KEEP_AWAKE_ACTIVE`<br>3 = `STATE_KEEP_AWAKE_ALLOW_SLEEP`<br>4 = `STATE_KEEP_AWAKE_OVERRIDDEN_NOTIFY_USER` | plausible |

## Multiplexing

`VCFRONT_LVPowerStateIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (1 signals), page 1 (16 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
