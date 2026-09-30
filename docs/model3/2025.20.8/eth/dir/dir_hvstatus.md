---
layout: default
title: "DIR_hvStatus (0x279) — Rear drive inverter, Tesla Model 3 2025.20.8 ETH"
description: "Rear drive inverter message: hv status. Ethernet-side message DIR_hvStatus of Rear drive inverter for Tesla Model 3 firmware 2025.20.8, 14 signals (DIR_hvStatusChecksum, DIR_hvStatusCounter, DIR_hvilCurrent, DIR_hvilCmVoltage and 10 more). Bit layout, scaling, units and value tables."
---

# DIR_hvStatus (0x279) — Rear drive inverter, Tesla Model 3 2025.20.8 ETH

Rear drive inverter message: hv status. This page documents the 14 signals of DIR_hvStatus as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DIR_hvStatus` |
| Ethernet-side id | 0x279 (633) |
| ECU | [Rear drive inverter](../../dir.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DIR |
| Frame length | 7 bytes |
| Cycle time | 100 ms |
| Signals | 14 |

## Signals of DIR_hvStatus

Tesla Model 3 CAN bus signals in `DIR_hvStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIR_hvStatusChecksum` | Rear drive inverter: hv status checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `DIR_hvStatusCounter` | Rear drive inverter: hv status counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `DIR_hvilCurrent` | HVIL Current | 12\|8 | little-endian | unsigned | 0.1 | 0 | mA | 0 to 25.5 |  | validated |
| `DIR_hvilCmVoltage` | HVIL Common Mode Voltage | 20\|8 | little-endian | unsigned | 0.08 | 0 | V | 0 to 20.4 |  | validated |
| `DIR_hvilStatus` | Aggregated hardware and measured HVIL unit status; raw 3 = signal not available (SNA) | 28\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `DISABLED`<br>1 = `OPEN`<br>2 = `CLOSED`<br>3 = `SNA` | validated |
| `DIR_hvilSupplyState` | Rear drive inverter: hvil supply state | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_AVAILABLE`<br>1 = `INACTIVE`<br>2 = `ACTIVE` | validated |
| `DIR_activeDischargeCtrl` | Rear drive inverter: active discharge ctrl | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DIR_activeDischargeStatus` | Active discharge status from HVIL_FAULT signal. | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DIR_vBat` | Reports the battery voltage measured by the Drive Inverter's local Analog to Digital Converter (ADC). | 34\|10 | little-endian | unsigned | 1 | 0 | V | 0 to 1023 |  | validated |
| `DIR_vBatQF` | Rear drive inverter: v bat QF | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_QUALIFIED`<br>1 = `QUALIFIED` | validated |
| `DIR_powerStageSafeState` | Rear drive inverter: power stage safe state | 45\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PSTG_SAFESTATE_NONE`<br>1 = `PSTG_SAFESTATE_ALL_OFF`<br>2 = `PSTG_SAFESTATE_3PS_HIGH`<br>3 = `PSTG_SAFESTATE_3PS_LOW` | validated |
| `DIR_fluxState` | Rear drive inverter: flux state | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `DI_FLUXSTATE_START`<br>1 = `DI_FLUXSTATE_TEST`<br>2 = `DI_FLUXSTATE_STANDBY`<br>3 = `DI_FLUXSTATE_FLUX_UP`<br>4 = `DI_FLUXSTATE_FLUX_DOWN`<br>5 = `DI_FLUXSTATE_ENABLED`<br>6 = `DI_FLUXSTATE_ICONTROL`<br>7 = `DI_FLUXSTATE_VCONTROL`<br>9 = `DI_FLUXSTATE_FAULT`<br>10 = `DI_FLUXSTATE_STATIONARY_WASTE`<br>11 = `DI_FLUXSTATE_MAGNET_FLUX_DETECT`<br>12 = `DI_FLUXSTATE_DISABLED` | validated |
| `DIR_vBusDiag` | Rear drive inverter: v bus diag | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DIR_gateDriveState` | Rear drive inverter: gate drive state | 53\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `PSTG_GD_STATE_INIT`<br>1 = `PSTG_GD_STATE_SELFTEST`<br>2 = `PSTG_GD_STATE_CONFIGURING`<br>3 = `PSTG_GD_STATE_CONFIGURED`<br>4 = `PSTG_GD_STATE_NOT_CONFIGURED` | validated |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Rear drive inverter messages (DIR)](../../dir.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
