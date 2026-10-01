---
layout: default
title: "UI_vehicleControlThermal (0x355) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Touchscreen user interface computer message: vehicle control thermal. Ethernet-side message UI_vehicleControlThermal of Touchscreen user interface computer for Tesla Model 3 / Model Y firmware 2025.20.8, 15 signals (UI_coolantFlowRequest, UI_inletActiveCoolTarget, UI_disableHVPTThermalLoads, UI_enableCompLiquidPumpOut and 11 more). Bit layout, scaling, units and value tables."
---

# UI_vehicleControlThermal (0x355) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 ETH

Touchscreen user interface computer message: vehicle control thermal. This page documents the 15 signals of UI_vehicleControlThermal as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_vehicleControlThermal` |
| Ethernet-side id | 0x355 (853) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 6 bytes |
| Cycle time | 1000 ms |
| Signals | 15 |

## Signals of UI_vehicleControlThermal

Tesla Model 3 / Model Y CAN bus signals in `UI_vehicleControlThermal`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_coolantFlowRequest` | request for coolant flow to MCU in LPM | 0\|5 | little-endian | unsigned | 1 | 0 | LPM | 0 to 25 |  | validated |
| `UI_inletActiveCoolTarget` | request for coolant temperature at Car Computer inlet | 5\|7 | little-endian | unsigned | 1 | 0 | degC | 0 to 127 |  | plausible |
| `UI_disableHVPTThermalLoads` | Request thermal system to disable active battery heating | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableCompLiquidPumpOut` | Touchscreen user interface computer: enable comp liquid pump out | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableCOP1HighSHOperation` | Touchscreen user interface computer: enable COP1 high SH operation | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableIncreasedEvapRampRate` | Touchscreen user interface computer: enable increased evap ramp rate | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableCOP1BatteryHeating` | Touchscreen user interface computer: enable COP1 battery heating | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableCOP1CabinHeatingBatteryHeating` | Touchscreen user interface computer: enable COP1 cabin heating battery heating | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableLouverAutoDetection` | Touchscreen user interface computer: enable louver auto detection | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableUserFacingLowFlowDeliveryAlert` | Touchscreen user interface computer: enable user facing low flow delivery alert | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_disableHvacCameraOnlyDefog` | Touchscreen user interface computer: disable hvac camera only defog | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableEXVFastCalibration` | Touchscreen user interface computer: enable EXV fast calibration | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_geofencedLiftgateHeight` | Touchscreen user interface computer: geofenced liftgate height; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | 0 | cm | 0 to 254 | 0 = `PENDING_SAVE`<br>1 = `USE_DEFAULT`<br>255 = `INVALID_SNA` | plausible |
| `UI_enableConservativeBatteryHeating` | Touchscreen user interface computer: enable conservative battery heating | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableDefaultApTempTarget` | Touchscreen user interface computer: enable default ap temp target | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
