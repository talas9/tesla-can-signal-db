---
layout: default
title: "VCSEC_TPMSData (0x219) — Vehicle security controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Vehicle security controller message: TPMS data. Tesla Model 3 / Model Y CAN bus message VCSEC_TPMSData (0x219) of Vehicle security controller, firmware 2026.26.6.5, 45 signals (VCSEC_TPMSDataIndex, VCSEC_TPMSCapabilityPressureInAdv0, VCSEC_TPMSCapabilityConfigurablePressure0, VCSEC_TPMSPressureRateOfChange0 and 41 more). Bit layout, scaling, units and value tables."
---

# VCSEC_TPMSData (0x219) — Vehicle security controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Vehicle security controller message: TPMS data; frame length from the layout, not yet observed on a vehicle bus. This page documents the 45 signals of VCSEC_TPMSData as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEC_TPMSData` |
| CAN id | 0x219 (537) |
| ECU | [Vehicle security controller](../../vcsec.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCSEC |
| Frame length | 7 bytes |
| Cycle time | 100 ms |
| Signals | 45 |

## Signals of VCSEC_TPMSData

Tesla Model 3 / Model Y CAN bus signals in `VCSEC_TPMSData`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEC_TPMSDataIndex` | selector | Vehicle security controller: TPMS data index | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `Sensor0`<br>1 = `Sensor1`<br>2 = `Sensor2`<br>3 = `Sensor3`<br>4 = `RCP`<br>5 = `AutonomyHealth` | validated |
| `VCSEC_TPMSCapabilityPressureInAdv0` | page 0 | Vehicle security controller: TPMS capability pressure in adv0 | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_TPMSCapabilityConfigurablePressure0` | page 0 | Vehicle security controller: TPMS capability configurable pressure0 | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_TPMSPressureRateOfChange0` | page 0 | Reports the raw pressure value of TPMS sensor 0. | 5\|10 | little-endian | signed | 0.02 | 0 | kPa/S | -10.24 to 10.22 |  | validated |
| `VCSEC_TPMSPressure0` | page 0 | Indicates Absolute pressure measured by wheel unit; raw 511 = signal not available (SNA) | 15\|9 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 12.75 | 510 = `OVER_RANGE`<br>511 = `SNA` | validated |
| `VCSEC_TPMSTemperature0` | page 0 | Indicates temperature in tire; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 214 | 255 = `SNA` | validated |
| `VCSEC_TPMSBatVoltage0` | page 0 | Sensor battery voltage; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.01 | 1.5 | V | 1.5 to 4.04 | 255 = `SNA` | validated |
| `VCSEC_TPMSLocation0` | page 0 | Indicates the localization result | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `LOCATION_FL`<br>1 = `LOCATION_FR`<br>2 = `LOCATION_RL`<br>3 = `LOCATION_RR`<br>4 = `LOCATION_UNKNOWN` | validated |
| `VCSEC_TPMSTemperatureCompensatedPressure0` | page 0 | Indicates Absolute pressure measured by wheel unit; raw 511 = signal not available (SNA) | 43\|9 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 12.75 | 510 = `OVER_RANGE`<br>511 = `SNA` | validated |
| `VCSEC_TPMSCapabilityPressureInAdv1` | page 1 | Vehicle security controller: TPMS capability pressure in adv1 | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_TPMSCapabilityConfigurablePressure1` | page 1 | Vehicle security controller: TPMS capability configurable pressure1 | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_TPMSPressureRateOfChange1` | page 1 | Reports the raw pressure value of TPMS sensor 1. | 5\|10 | little-endian | signed | 0.02 | 0 | kPa/S | -10.24 to 10.22 |  | validated |
| `VCSEC_TPMSPressure1` | page 1 | Indicates Absolute pressure measured by wheel unit; raw 511 = signal not available (SNA) | 15\|9 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 12.75 | 510 = `OVER_RANGE`<br>511 = `SNA` | validated |
| `VCSEC_TPMSTemperature1` | page 1 | Indicates temperature in tire; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 214 | 255 = `SNA` | validated |
| `VCSEC_TPMSBatVoltage1` | page 1 | Sensor battery voltage; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.01 | 1.5 | V | 1.5 to 4.04 | 255 = `SNA` | validated |
| `VCSEC_TPMSLocation1` | page 1 | Indicates the localization result | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `LOCATION_FL`<br>1 = `LOCATION_FR`<br>2 = `LOCATION_RL`<br>3 = `LOCATION_RR`<br>4 = `LOCATION_UNKNOWN` | validated |
| `VCSEC_TPMSTemperatureCompensatedPressure1` | page 1 | Indicates Absolute pressure measured by wheel unit; raw 511 = signal not available (SNA) | 43\|9 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 12.75 | 510 = `OVER_RANGE`<br>511 = `SNA` | validated |
| `VCSEC_TPMSCapabilityPressureInAdv2` | page 2 | Vehicle security controller: TPMS capability pressure in adv2 | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_TPMSCapabilityConfigurablePressure2` | page 2 | Vehicle security controller: TPMS capability configurable pressure2 | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_TPMSPressureRateOfChange2` | page 2 | Reports the raw pressure value of TPMS sensor 2. | 5\|10 | little-endian | signed | 0.02 | 0 | kPa/S | -10.24 to 10.22 |  | validated |
| `VCSEC_TPMSPressure2` | page 2 | Indicates Absolute pressure measured by wheel unit; raw 511 = signal not available (SNA) | 15\|9 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 12.75 | 510 = `OVER_RANGE`<br>511 = `SNA` | validated |
| `VCSEC_TPMSTemperature2` | page 2 | Indicates temperature in tire; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 214 | 255 = `SNA` | validated |
| `VCSEC_TPMSBatVoltage2` | page 2 | Sensor battery voltage; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.01 | 1.5 | V | 1.5 to 4.04 | 255 = `SNA` | validated |
| `VCSEC_TPMSLocation2` | page 2 | Indicates the localization result | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `LOCATION_FL`<br>1 = `LOCATION_FR`<br>2 = `LOCATION_RL`<br>3 = `LOCATION_RR`<br>4 = `LOCATION_UNKNOWN` | validated |
| `VCSEC_TPMSTemperatureCompensatedPressure2` | page 2 | Indicates Absolute pressure measured by wheel unit; raw 511 = signal not available (SNA) | 43\|9 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 12.75 | 510 = `OVER_RANGE`<br>511 = `SNA` | validated |
| `VCSEC_TPMSCapabilityPressureInAdv3` | page 3 | Vehicle security controller: TPMS capability pressure in adv3 | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_TPMSCapabilityConfigurablePressure3` | page 3 | Vehicle security controller: TPMS capability configurable pressure3 | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_TPMSPressureRateOfChange3` | page 3 | Reports the raw pressure value of TPMS sensor 3. | 5\|10 | little-endian | signed | 0.02 | 0 | kPa/S | -10.24 to 10.22 |  | validated |
| `VCSEC_TPMSPressure3` | page 3 | Indicates Absolute pressure measured by wheel unit; raw 511 = signal not available (SNA) | 15\|9 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 12.75 | 510 = `OVER_RANGE`<br>511 = `SNA` | validated |
| `VCSEC_TPMSTemperature3` | page 3 | Indicates temperature in tire; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 214 | 255 = `SNA` | validated |
| `VCSEC_TPMSBatVoltage3` | page 3 | Sensor battery voltage; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.01 | 1.5 | V | 1.5 to 4.04 | 255 = `SNA` | validated |
| `VCSEC_TPMSLocation3` | page 3 | Indicates the localization result | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `LOCATION_FL`<br>1 = `LOCATION_FR`<br>2 = `LOCATION_RL`<br>3 = `LOCATION_RR`<br>4 = `LOCATION_UNKNOWN` | validated |
| `VCSEC_TPMSTemperatureCompensatedPressure3` | page 3 | Indicates Absolute pressure measured by wheel unit; raw 511 = signal not available (SNA) | 43\|9 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 12.75 | 510 = `OVER_RANGE`<br>511 = `SNA` | validated |
| `VCSEC_TPMSRecommendedColdPressureFront` | page 4 | Indicates Absolute pressure measured by wheel unit; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.35 | 254 = `OVER_RANGE`<br>255 = `SNA` | validated |
| `VCSEC_TPMSRecommendedColdPressureRear` | page 4 | Indicates Absolute pressure measured by wheel unit; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.35 | 254 = `OVER_RANGE`<br>255 = `SNA` | validated |
| `VCSEC_TPMSFeature0` | page 4 | Vehicle security controller: TPMS feature0 | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `FEATURE_0_NOT_SUPPORTED`<br>1 = `FEATURE_0_UNAVAILABLE_1`<br>2 = `FEATURE_0_UNAVAILABLE_2`<br>3 = `FEATURE_0_WAIT_FOR_STATIONARY`<br>4 = `FEATURE_0_READY`<br>5 = `FEATURE_0_ACTIVE`<br>6 = `FEATURE_0_BLOCKED` | validated |
| `VCSEC_TPMSFeature1` | page 4 | Vehicle security controller: TPMS feature1 | 27\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `FEATURE_1_NONE`<br>1 = `FEATURE_1_REACHED`<br>2 = `FEATURE_1_INCORRECT`<br>3 = `FEATURE_1_FAR_AWAY`<br>4 = `FEATURE_1_MEDIUM`<br>5 = `FEATURE_1_CLOSE` | validated |
| `VCSEC_TPMSFeature0Count` | page 4 | Vehicle security controller: TPMS feature0 count | 32\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `VCSEC_TPMSFeature0TimeS` | page 4 | Vehicle security controller: TPMS feature0 time s | 36\|11 | little-endian | unsigned | 1 | 0 |  | 0 to 2047 |  | validated |
| `VCSEC_TPMSAutonomyStatus` | page 5 | Vehicle security controller: TPMS autonomy status | 3\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TPMS_AUTONOMY_STATUS_NORMAL`<br>1 = `TPMS_AUTONOMY_STATUS_MIA`<br>2 = `TPMS_AUTONOMY_STATUS_RESET` | validated |
| `VCSEC_TPMSAutonomyStatusMIATimeS` | page 5 | Vehicle security controller: TPMS autonomy status MIA time s | 5\|9 | little-endian | unsigned | 1 | 0 |  | 0 to 511 |  | validated |
| `VCSEC_TPMSLastKnownPressureFL` | page 5 | Vehicle security controller: TPMS last known pressure FL; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.35 | 254 = `OVER_RANGE`<br>255 = `SNA` | validated |
| `VCSEC_TPMSLastKnownPressureFR` | page 5 | Vehicle security controller: TPMS last known pressure FR; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.35 | 254 = `OVER_RANGE`<br>255 = `SNA` | validated |
| `VCSEC_TPMSLastKnownPressureRL` | page 5 | Vehicle security controller: TPMS last known pressure RL; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.35 | 254 = `OVER_RANGE`<br>255 = `SNA` | validated |
| `VCSEC_TPMSLastKnownPressureRR` | page 5 | Vehicle security controller: TPMS last known pressure RR; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.35 | 254 = `OVER_RANGE`<br>255 = `SNA` | validated |

## Multiplexing

`VCSEC_TPMSDataIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (8 signals), page 1 (8 signals), page 2 (8 signals), page 3 (8 signals), page 4 (6 signals), page 5 (6 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Vehicle security controller messages (VCSEC)](../../vcsec.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
