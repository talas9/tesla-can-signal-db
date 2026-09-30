---
layout: default
title: "DIF_hvStatus (0x27A) — Front drive inverter, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Front drive inverter message: hv status. Tesla Model 3 / Model Y CAN bus message DIF_hvStatus (0x27A) of Front drive inverter, firmware 2026.26.6.5, 15 signals (DIF_hvStatusChecksum, DIF_hvStatusCounter, DIF_hvilCurrent, DIF_hvilCmVoltage and 11 more). Bit layout, scaling, units and value tables."
---

# DIF_hvStatus (0x27A) — Front drive inverter, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Front drive inverter message: hv status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 15 signals of DIF_hvStatus as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DIF_hvStatus` |
| CAN id | 0x27A (634) |
| ECU | [Front drive inverter](../../dif.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | DIF |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 15 |

## Signals of DIF_hvStatus

Tesla Model 3 / Model Y CAN bus signals in `DIF_hvStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIF_hvStatusChecksum` | Front drive inverter: hv status checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `DIF_hvStatusCounter` | Front drive inverter: hv status counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `DIF_hvilCurrent` | HVIL Current | 12\|8 | little-endian | unsigned | 0.1 | 0 | mA | 0 to 25.5 |  | validated |
| `DIF_hvilCmVoltage` | HVIL Common Mode Voltage | 20\|8 | little-endian | unsigned | 0.08 | 0 | V | 0 to 20.4 |  | validated |
| `DIF_hvilStatus` | Aggregated hardware and measured HVIL unit status; raw 3 = signal not available (SNA) | 28\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `DISABLED`<br>1 = `OPEN`<br>2 = `CLOSED`<br>3 = `SNA` | validated |
| `DIF_hvilSupplyState` | Front drive inverter: hvil supply state | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_AVAILABLE`<br>1 = `INACTIVE`<br>2 = `ACTIVE` | validated |
| `DIF_activeDischargeCtrl` | Front drive inverter: active discharge ctrl | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DIF_activeDischargeStatus` | Active discharge status from HVIL_FAULT signal. | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DIF_vBat` | Reports the battery voltage measured by the Drive Inverter's local Analog to Digital Converter (ADC). | 34\|10 | little-endian | unsigned | 1 | 0 | V | 0 to 1023 |  | validated |
| `DIF_vBatQF` | Front drive inverter: v bat QF | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_QUALIFIED`<br>1 = `QUALIFIED` | validated |
| `DIF_powerStageSafeState` | Front drive inverter: power stage safe state | 45\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PSTG_SAFESTATE_NONE`<br>1 = `PSTG_SAFESTATE_ALL_OFF`<br>2 = `PSTG_SAFESTATE_3PS_HIGH`<br>3 = `PSTG_SAFESTATE_3PS_LOW` | validated |
| `DIF_fluxState` | Front drive inverter: flux state | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `DI_FLUXSTATE_START`<br>1 = `DI_FLUXSTATE_TEST`<br>2 = `DI_FLUXSTATE_STANDBY`<br>3 = `DI_FLUXSTATE_FLUX_UP`<br>4 = `DI_FLUXSTATE_FLUX_DOWN`<br>5 = `DI_FLUXSTATE_ENABLED`<br>6 = `DI_FLUXSTATE_ICONTROL`<br>7 = `DI_FLUXSTATE_VCONTROL`<br>9 = `DI_FLUXSTATE_FAULT`<br>10 = `DI_FLUXSTATE_STATIONARY_WASTE`<br>11 = `DI_FLUXSTATE_MAGNET_FLUX_DETECT`<br>12 = `DI_FLUXSTATE_DISABLED` | validated |
| `DIF_vBusDiag` | Front drive inverter: v bus diag | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DIF_gateDriveState` | Front drive inverter: gate drive state | 53\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `PSTG_GD_STATE_INIT`<br>1 = `PSTG_GD_STATE_SELFTEST`<br>2 = `PSTG_GD_STATE_CONFIGURING`<br>3 = `PSTG_GD_STATE_CONFIGURED`<br>4 = `PSTG_GD_STATE_NOT_CONFIGURED` | validated |
| `DIF_gateDriveSupplyState` | Front drive inverter: gate drive supply state | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PSTG_GD_SUPPLY_DOWN`<br>1 = `PSTG_GD_SUPPLY_RISING`<br>2 = `PSTG_GD_SUPPLY_UP`<br>3 = `PSTG_GD_SUPPLY_FALLING` | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Front drive inverter messages (DIF)](../../dif.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
