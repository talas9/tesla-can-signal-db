---
layout: default
title: "ESP_status (0x145) — Electronic stability control, Tesla Model Y 2025.20.8 PARTY CAN"
description: "Electronic stability control message: status. Tesla Model Y CAN bus message ESP_status (0x145) of Electronic stability control, firmware 2025.20.8, 26 signals (ESP_statusChecksum, ESP_statusCounter, ESP_espModeActive, ESP_stabilityControlSts2 and 22 more). Bit layout, scaling, units and value tables."
---

# ESP_status (0x145) — Electronic stability control, Tesla Model Y 2025.20.8 PARTY CAN

Electronic stability control message: status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 26 signals of ESP_status as defined for Tesla Model Y firmware 2025.20.8 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `ESP_status` |
| CAN id | 0x145 (325) |
| ECU | [Electronic stability control](../../esp.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | ESP |
| Frame length | 8 bytes |
| Cycle time | 20 ms |
| Signals | 26 |

## Signals of ESP_status

Tesla Model Y CAN bus signals in `ESP_status`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `ESP_statusChecksum` | Electronic stability control: status checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `ESP_statusCounter` | Electronic stability control: status counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `ESP_espModeActive` | Electronic stability control: esp mode active | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `ESP_MODE_00_NORMAL`<br>1 = `ESP_MODE_01`<br>2 = `ESP_MODE_02`<br>3 = `ESP_MODE_03` | plausible |
| `ESP_stabilityControlSts2` | Electronic stability control: stability control sts2 | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INIT`<br>1 = `ON`<br>2 = `ENGAGED`<br>3 = `FAULTED` | plausible |
| `ESP_ebdFaultLamp` | Electronic stability control: ebd fault lamp | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `EBD_FAULT_LAMP_OFF`<br>1 = `EBD_FAULT_LAMP_ON` | plausible |
| `ESP_absFaultLamp` | ESP request to display ABS Fault Lamp. | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `ABS_FAULT_LAMP_OFF`<br>1 = `ABS_FAULT_LAMP_ON` | plausible |
| `ESP_espFaultLamp` | ESP request to display ESP Fault lamp in instrument cluster. | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `ESP_FAULT_LAMP_OFF`<br>1 = `ESP_FAULT_LAMP_ON` | plausible |
| `ESP_hydraulicBoostEnabled` | Electronic stability control: hydraulic boost enabled | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ESP_espLampFlash` | Electronic stability control: esp lamp flash | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `ESP_LAMP_OFF`<br>1 = `ESP_LAMP_FLASH` | plausible |
| `ESP_brakeLamp` | Electronic stability control: brake lamp | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LAMP_OFF`<br>1 = `LAMP_ON` | plausible |
| `ESP_absBrakeEvent2` | Indicates if ABS is active and on which axle. | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `ABS_EVENT_NOT_ACTIVE`<br>1 = `ABS_EVENT_ACTIVE_FRONT_REAR`<br>2 = `ABS_EVENT_ACTIVE_FRONT`<br>3 = `ABS_EVENT_ACTIVE_REAR` | plausible |
| `ESP_longitudinalAccelQF` | Longitudinal accel sensor quialifier from ESP | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNDEFINABLE_ACCURACY`<br>1 = `IN_SPEC` | plausible |
| `ESP_lateralAccelQF` | Lateral accel sensor quialifier from ESP | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNDEFINABLE_ACCURACY`<br>1 = `IN_SPEC` | plausible |
| `ESP_yawRateQF` | Electronic stability control: yaw rate QF | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNDEFINABLE_ACCURACY`<br>1 = `IN_SPEC` | plausible |
| `ESP_steeringAngleQF` | Electronic stability control: steering angle QF | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `UNDEFINABLE_ACCURACY`<br>1 = `IN_SPEC` | plausible |
| `ESP_brakeDiscWipingActive` | Indicates when brake disc wiping is active. | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `BDW_INACTIVE`<br>1 = `BDW_ACTIVE` | plausible |
| `ESP_driverBrakeApply` | Indicates when the driver applies the brake pedal; raw 3 = signal not available (SNA) | 29\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NotInit_orOff`<br>1 = `Not_Applied`<br>2 = `Driver_applying_brakes`<br>3 = `Faulty_SNA` | plausible |
| `ESP_brakeApply` | Electronic stability control: brake apply | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `BLS_INACTIVE`<br>1 = `BLS_ACTIVE` | plausible |
| `ESP_aesPrimaryActuatorStatus` | Electronic stability control: aes primary actuator status | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `AES_NOT_SUPPORTED_OR_NOT_INIT`<br>1 = `AES_AVAILABLE`<br>2 = `AES_ACTIVE`<br>3 = `AES_FAILURE` | plausible |
| `ESP_cdpStatus` | Indicates the state of the ESP to perform pressure builds through ESP for dynamic apply | 34\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CDP_IS_NOT_AVAILABLE`<br>1 = `CDP_IS_AVAILABLE`<br>2 = `ACTUATING_EPB_CDP`<br>3 = `CDP_COMMAND_INVALID` | plausible |
| `ESP_ptcTargetState` | Electronic stability control: ptc target state; raw 3 = signal not available (SNA) | 36\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `FAULT`<br>1 = `BACKUP`<br>2 = `ON`<br>3 = `SNA` | plausible |
| `ESP_btcTargetState` | Electronic stability control: btc target state; raw 3 = signal not available (SNA) | 38\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `OFF`<br>1 = `BACKUP`<br>2 = `ON`<br>3 = `SNA` | plausible |
| `ESP_decoupledBrakePressEst` | Reports the master cylinder pressure estimated by the Electronic Stability Program (ESP) which includes four wheel ESP active pressure builds; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 1 | -30 | bar | -30 to 224 | 255 = `SNA` | plausible |
| `ESP_ebrStandstillSkid` | Electronic stability control: ebr standstill skid | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NO_STANDSTILL_SKID`<br>1 = `STANDSTILL_SKID_DETECTED` | plausible |
| `ESP_ebrStatus` | Electronic stability control: ebr status | 49\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `EBR_IS_NOT_AVAILABLE`<br>1 = `EBR_IS_AVAILABLE`<br>2 = `ACTUATING_DI_EBR`<br>3 = `EBR_COMMAND_INVALID` | plausible |
| `ESP_brakeTorqueTarget` | Electronic stability control: brake torque target | 51\|13 | little-endian | unsigned | 3 | 0 | Nm | 0 to 24573 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2025.20.8 PARTY DBC file](../../../../../dbc/ModelY/2025.20.8/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/PARTY.json)

## See also

- [All Electronic stability control messages (ESP)](../../esp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
