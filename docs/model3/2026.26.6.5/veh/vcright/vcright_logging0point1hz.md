---
layout: default
title: "VCRIGHT_logging0point1Hz (0x70B) — Right body controller, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Right body controller message: logging0point1 hz. Tesla Model 3 CAN bus message VCRIGHT_logging0point1Hz (0x70B) of Right body controller, firmware 2026.26.6.5, 58 signals (VCRIGHT_logging0point1HzIndex, VCRIGHT_glareShieldEstimatedResistance, VCRIGHT_cabinAirFilterLifeRemaining, VCRIGHT_HEPAAirFilterLifeRemaining and 54 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_logging0point1Hz (0x70B) — Right body controller, Tesla Model 3 2026.26.6.5 VEH CAN

Right body controller message: logging0point1 hz; frame length observed on a vehicle bus. This page documents the 58 signals of VCRIGHT_logging0point1Hz as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_logging0point1Hz` |
| CAN id | 0x70B (1803) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 58 |

## Signals of VCRIGHT_logging0point1Hz

Tesla Model 3 CAN bus signals in `VCRIGHT_logging0point1Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_logging0point1HzIndex` | selector | Right body controller: logging0point1 hz index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `LIGHT_CURRENTS_0`<br>1 = `LIGHT_CURRENTS_1`<br>2 = `HVAC`<br>3 = `HVAC_ACTUATOR_ENDSTOP`<br>4 = `HVAC_ACTUATOR_ZEROSTOP`<br>5 = `LIGHT_CURRENTS_2`<br>6 = `HVAC_2`<br>7 = `HVAC_3`<br>8 = `HVAC_4`<br>9 = `HVAC_5`<br>10 = `END` | plausible |
| `VCRIGHT_glareShieldEstimatedResistance` | page 2 | Reports estimated resistance of the glare shield heater. | 4\|6 | little-endian | unsigned | 0.5 | 10 | Ohm | 10 to 40 |  | validated |
| `VCRIGHT_cabinAirFilterLifeRemaining` | page 2 | Life remaining on the cabin air filter | 10\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | validated |
| `VCRIGHT_HEPAAirFilterLifeRemaining` | page 2 | Life remaining on the cabin air filter | 17\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | validated |
| `VCRIGHT_leftPTCCompromisedRod` | page 2 | Right body controller: left PTC compromised rod | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `ALL`<br>2 = `INNER`<br>3 = `CENTER`<br>4 = `OUTER`<br>5 = `OUTER_INNER`<br>6 = `OUTER_CENTER`<br>7 = `CENTER_INNER` | validated |
| `VCRIGHT_rightPTCCompromisedRod` | page 2 | Right body controller: right PTC compromised rod | 27\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `ALL`<br>2 = `INNER`<br>3 = `CENTER`<br>4 = `OUTER`<br>5 = `OUTER_INNER`<br>6 = `OUTER_CENTER`<br>7 = `CENTER_INNER` | validated |
| `VCRIGHT_hepaFilterHealthScore` | page 2 | Right body controller: hepa filter health score | 32\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | validated |
| `VCRIGHT_cabinFilterHealthScore` | page 2 | Right body controller: cabin filter health score | 40\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | validated |
| `VCRIGHT_cabinTempBreathLevelFOff` | page 2 | Right body controller: cabin temp breath level f off; raw 255 = signal not available (SNA) | 47\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_airDistributionModeAdjustmentFactor` | page 2 | Right body controller: air distribution mode adjustment factor | 55\|9 | little-endian | unsigned | 0.001 | 1 | - | 1 to 1.5 |  | validated |
| `VCRIGHT_hvacLHBleedEndStop` | page 3 | Right body controller: hvac LH bleed end stop | 8\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_hvacRHBleedEndStop` | page 3 | Right body controller: hvac RH bleed end stop | 16\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_hvacLHVaneEndStop` | page 3 | Right body controller: hvac LH vane end stop | 24\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_hvacRHVaneEndStop` | page 3 | Right body controller: hvac RH vane end stop | 32\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_hvacUpperModeEndStop` | page 3 | Right body controller: hvac upper mode end stop | 40\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_hvacLowerModeEndStop` | page 3 | Right body controller: hvac lower mode end stop | 48\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_hvacIntakeEndStop` | page 3 | Right body controller: hvac intake end stop | 56\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_hvacLHBleedZeroStop` | page 4 | Right body controller: hvac LH bleed zero stop | 8\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_hvacRHBleedZeroStop` | page 4 | Right body controller: hvac RH bleed zero stop | 16\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_hvacLHVaneZeroStop` | page 4 | Right body controller: hvac LH vane zero stop | 24\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_hvacRHVaneZeroStop` | page 4 | Right body controller: hvac RH vane zero stop | 32\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_hvacUpperModeZeroStop` | page 4 | Right body controller: hvac upper mode zero stop | 40\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_hvacLowerModeZeroStop` | page 4 | Right body controller: hvac lower mode zero stop | 48\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_hvacIntakeZeroStop` | page 4 | Right body controller: hvac intake zero stop | 56\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_averageDuctTempFCooling` | page 5 | Estimated average duct temp temp 15 min into the drive; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_fasciaTailLeftLightCurrent` | page 5 | Current sensed by the left fascia tail light HSD (high side driver); raw 511 = signal not available (SNA) | 16\|9 | little-endian | unsigned | 0.002 | 0 | A | 0 to 1.02 | 511 = `SNA` | validated |
| `VCRIGHT_fasciaTailLeftLightCurrentSenseState` | page 5 | State representing validity of the left fascia tail light HSD (high side driver) current sense; raw 0 = signal not available (SNA) | 25\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `SNA`<br>1 = `STEADY_STATE_OFF`<br>2 = `RISING_EDGE_TRANSIENT`<br>3 = `STEADY_STATE_ON`<br>4 = `FALLING_EDGE_TRANSIENT` | contradicted |
| `VCRIGHT_fasciaTailRightLightCurrent` | page 5 | Current sensed by the right fascia tail light HSD (high side driver); raw 511 = signal not available (SNA) | 28\|9 | little-endian | unsigned | 0.002 | 0 | A | 0 to 1.02 | 511 = `SNA` | validated |
| `VCRIGHT_fasciaTailRightLightCurrentSenseState` | page 5 | State representing validity of the right fascia tail light HSD (high side driver) current sense; raw 0 = signal not available (SNA) | 37\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `SNA`<br>1 = `STEADY_STATE_OFF`<br>2 = `RISING_EDGE_TRANSIENT`<br>3 = `STEADY_STATE_ON`<br>4 = `FALLING_EDGE_TRANSIENT` | contradicted |
| `VCRIGHT_liftgateTailLeftLightCurrent` | page 5 | Current sensed by the left liftgate tail light HSD (high side driver); raw 511 = signal not available (SNA) | 40\|9 | little-endian | unsigned | 0.002 | 0 | A | 0 to 1.02 | 511 = `SNA` | validated |
| `VCRIGHT_liftgateTailLeftLightCurrentSenseState` | page 5 | State representing validity of the left liftgate tail light HSD (high side driver) current sense; raw 0 = signal not available (SNA) | 49\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `SNA`<br>1 = `STEADY_STATE_OFF`<br>2 = `RISING_EDGE_TRANSIENT`<br>3 = `STEADY_STATE_ON`<br>4 = `FALLING_EDGE_TRANSIENT` | contradicted |
| `VCRIGHT_liftgateTailRightLightCurrentSenseState` | page 5 | State representing validity of the right liftgate tail light HSD (high side driver) current sense; raw 0 = signal not available (SNA) | 52\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `SNA`<br>1 = `STEADY_STATE_OFF`<br>2 = `RISING_EDGE_TRANSIENT`<br>3 = `STEADY_STATE_ON`<br>4 = `FALLING_EDGE_TRANSIENT` | contradicted |
| `VCRIGHT_ambientTempLimp` | page 6 | Reports the estimated ambient temperature in limp mode; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_cabinProbeTempLimp` | page 6 | Reports the estimated cabin probe temperature in limp mode; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_thsTempLimp` | page 6 | Reports the estimated Tesla HVAC Sensor (THS) temperature in limp mode; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | contradicted |
| `VCRIGHT_thsCabinWaterMassLimp` | page 6 | Reports the estimated Tesla HVAC Sensor (THS) humidity cabin water mass backup in limp mode. | 32\|8 | little-endian | unsigned | 0.5 | 0 | g/kg | 0 to 124 |  | validated |
| `VCRIGHT_thsSolarIrradianceLimp` | page 6 | Reports the estimated Tesla HVAC Sensor (THS) solar irradiance backup in limp mode; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 5 | 0 | W/m2 | 0 to 1270 | 255 = `SNA` | validated |
| `VCRIGHT_silentWakeRecordCount` | page 6 | Reports the number of records recorded during silent wake events. | 48\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | validated |
| `VCRIGHT_interiorCameraLedCurrent` | page 6 | Right body controller: interior camera led current; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 8 | 0 | mA | 0 to 2032 | 255 = `SNA` | validated |
| `VCRIGHT_evapCondensateMass` | page 7 | Right body controller: evap condensate mass | 8\|8 | little-endian | unsigned | 2 | 0 | g | 0 to 500 |  | validated |
| `VCRIGHT_airwaveRightLateralTotalTravel` | page 7 | Right body controller: airwave right lateral total travel | 16\|16 | little-endian | unsigned | 6100 | 0 | deg | 0 to 399763500 |  | validated |
| `VCRIGHT_airwaveLeftLateralTotalTravel` | page 7 | Right body controller: airwave left lateral total travel | 32\|16 | little-endian | unsigned | 6100 | 0 | deg | 0 to 399763500 |  | validated |
| `VCRIGHT_hvacRearEndStop` | page 7 | Right body controller: hvac rear end stop | 48\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_hvacRearZeroStop` | page 7 | Right body controller: hvac rear zero stop | 56\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_evapLoadInFresh` | page 8 | Right body controller: evap load in fresh | 8\|8 | little-endian | unsigned | 35 | 0 | W | 0 to 8000 |  | validated |
| `VCRIGHT_evapLoadInRecirc` | page 8 | Right body controller: evap load in recirc | 16\|8 | little-endian | unsigned | 35 | 0 | W | 0 to 8000 |  | validated |
| `VCRIGHT_tempIncarCabinDeep` | page 8 | Right body controller: temp incar cabin deep; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 85 | 255 = `SNA` | validated |
| `VCRIGHT_cabinTempBreathLevelF10minHeating` | page 8 | Right body controller: cabin temp breath level f10min heating; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_cabinTempBreathLevelF10minCooling` | page 8 | Right body controller: cabin temp breath level f10min cooling; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_cabinTempBreathLevelF5minHeating` | page 8 | Right body controller: cabin temp breath level f5min heating; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_cabinTempBreathLevelF5minCooling` | page 8 | Right body controller: cabin temp breath level f5min cooling; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_foggingMonitorRuntime` | page 9 | Total runtime of the overnight camera fogging monitor | 4\|12 | little-endian | unsigned | 10 | 0 | Hours | 0 to 40950 |  | validated |
| `VCRIGHT_cabinTempInteriorFHeating` | page 9 | Right body controller: cabin temp interior f heating; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_cabinTempInteriorFCooling` | page 9 | Right body controller: cabin temp interior f cooling; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_filterLifeBlowerTorque` | page 9 | Right body controller: filter life blower torque; raw 1023 = signal not available (SNA) | 32\|10 | little-endian | unsigned | 0.006 | -1.5 | Nm | -1.5 to 4.5 | 1023 = `SNA` | validated |
| `VCRIGHT_averageDuctTempFHeating` | page 9 | Estimated average duct temp temp 15 min into the drive; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_thsSolarSensorType` | page 9 | Indicates the solar sensor type for THS | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `ISL76683`<br>2 = `OPT4003` | validated |
| `VCRIGHT_thsTempSensorType` | page 9 | Indicates the temperature sensor type for THS | 58\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `SHT31`<br>2 = `SHT41` | validated |

## Multiplexing

`VCRIGHT_logging0point1HzIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 2 (9 signals), page 3 (7 signals), page 4 (7 signals), page 5 (8 signals), page 6 (7 signals), page 7 (5 signals), page 8 (7 signals), page 9 (7 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
