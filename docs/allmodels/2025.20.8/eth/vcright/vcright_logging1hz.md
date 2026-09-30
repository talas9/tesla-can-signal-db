---
layout: default
title: "VCRIGHT_logging1Hz (0x2B3) — Right body controller, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Right body controller message: logging1 hz. Ethernet-side message VCRIGHT_logging1Hz of Right body controller for Tesla Model 3 / Model Y firmware 2025.20.8, 161 signals (VCRIGHT_logging1HzIndex, VCRIGHT_tempIncarCabinProbe, VCRIGHT_tempIncarCabinDeep, VCRIGHT_cabinTempInteriorL2 and 157 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_logging1Hz (0x2B3) — Right body controller, Tesla Model 3 / Model Y 2025.20.8 ETH

Right body controller message: logging1 hz. This page documents the 161 signals of VCRIGHT_logging1Hz as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_logging1Hz` |
| Ethernet-side id | 0x2B3 (691) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 60 ms |
| Signals | 161 |

## Signals of VCRIGHT_logging1Hz

Tesla Model 3 / Model Y CAN bus signals in `VCRIGHT_logging1Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_logging1HzIndex` | selector | Right body controller: logging1 hz index | 0\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `HVAC_TEMP_SENSORS_AND_ESTIMATES_1`<br>1 = `HVAC_TEMP_SENSORS_AND_ESTIMATES_2`<br>2 = `HVAC_HUMIDITY_HEATER_TEMP`<br>3 = `HVAC_STATUS_AIRFLOW`<br>4 = `HVAC_COMFORT_SOLAR`<br>5 = `HEATER_AND_DUCT_TARGETS`<br>6 = `HVAC_ACTUATOR_VOLTAGES`<br>7 = `HVAC_TEMP_SENSORS_AND_ESTIMATES_3`<br>8 = `HVAC_MISCELLANEOUS_1`<br>9 = `HVAC_MISCELLANEOUS_2`<br>10 = `HSD_CURRENTS_1`<br>11 = `HSD_CURRENTS_2`<br>12 = `HVAC_COMFORT_SOLAR_2`<br>13 = `HVAC_COMFORT_SOLAR_3`<br>14 = `STEERING_WHEEL_HEAT`<br>15 = `HVAC_MISCELLANEOUS_3`<br>16 = `HVAC_MISCELLANEOUS_4`<br>17 = `END` | plausible |
| `VCRIGHT_tempIncarCabinProbe` | page 0 | Right body controller: temp incar cabin probe; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 85 | 255 = `SNA` | validated |
| `VCRIGHT_tempIncarCabinDeep` | page 0 | Right body controller: temp incar cabin deep; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 85 | 255 = `SNA` | plausible |
| `VCRIGHT_cabinTempInteriorL2` | page 0 | Right body controller: cabin temp interior L2; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | plausible |
| `VCRIGHT_tempIncarCabinMid` | page 0 | Right body controller: temp incar cabin mid; raw 250 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 85 | 250 = `SNA` | validated |
| `VCRIGHT_cabinTempInteriorSunnyL2` | page 0 | Right body controller: cabin temp interior sunny L2; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.6 | -40 | degC | -40 to 100 | 255 = `SNA` | plausible |
| `VCRIGHT_cabinTempInteriorL3` | page 0 | Right body controller: cabin temp interior L3; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | plausible |
| `VCRIGHT_cabinTempInteriorSunnyL3` | page 0 | Right body controller: cabin temp interior sunny L3; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.6 | -40 | degC | -40 to 100 | 255 = `SNA` | plausible |
| `VCRIGHT_cabinTempGlassRoof` | page 1 | Modeled cabin temperature near the glass roof; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_cabinTempWindshield` | page 1 | Windshield temperature estimate; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_cabinTempInterior` | page 1 | Modeled interior cabin temperature; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_cabinTempInteriorSunny` | page 1 | Modeled interior surface temperature exposed to direct sunlight; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.6 | -40 | degC | -40 to 100 | 255 = `SNA` | validated |
| `VCRIGHT_cabinTempSideGlassLeft` | page 1 | Modeled glass temperature left; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_cabinTempSideGlassRight` | page 1 | Modeled glass temperature right; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_cabinTempBreathLevel` | page 1 | Modeled cabin temperature near occupant breathing level; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_pcbaTemperature` | page 2 | Right body controller: pcba temperature | 5\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 150 |  | validated |
| `VCRIGHT_wattsHeaterLeftTotal` | page 2 | Right body controller: watts heater left total | 16\|10 | little-endian | unsigned | 5 | 0 | W | 0 to 4000 |  | validated |
| `VCRIGHT_wattsHeaterRightTotal` | page 2 | Right body controller: watts heater right total | 26\|10 | little-endian | unsigned | 5 | 0 | W | 0 to 4000 |  | validated |
| `VCRIGHT_qdotLeftFFUnsat` | page 2 | Right body controller: qdot left FF unsat | 36\|9 | little-endian | signed | 10 | 0 | W | -1500 to 1500 |  | validated |
| `VCRIGHT_qdotRightFFUnsat` | page 2 | Right body controller: qdot right FF unsat | 45\|9 | little-endian | signed | 10 | 0 | W | -1500 to 1500 |  | validated |
| `VCRIGHT_nvhLevelDb` | page 2 | Right body controller: nvh level db | 54\|9 | little-endian | unsigned | 0.1 | 30 | dB | 30 to 80 |  | validated |
| `VCRIGHT_hvacSetTempActualLeft` | page 3 | HVAC internal left temperature set point | 8\|8 | little-endian | unsigned | 0.1 | 15 | degC | 15 to 28 |  | validated |
| `VCRIGHT_hvacSetTempActualRight` | page 3 | HVAC internal right temperature set point | 16\|8 | little-endian | unsigned | 0.1 | 15 | degC | 15 to 28 |  | validated |
| `VCRIGHT_hvacAutoTransitionReason` | page 3 | Reason for airflow mode change when system is operating in auto | 24\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `NONE`<br>1 = `HUMIDITY_HIGH`<br>2 = `HUMIDITY_MODERATE`<br>3 = `HUMIDITY_LOW`<br>4 = `TEMP_TARGET_BELOW_THRESHOLD`<br>5 = `TEMP_TARGET_ABOVE_THRESHOLD`<br>6 = `EXCESS_OCCUPANT_CONVECTION`<br>7 = `OCCUPANT_CONVECTION_REQUIREMENT`<br>8 = `TEMP_TARGET_LOW`<br>9 = `DUCTS_COLD`<br>10 = `BI_LEVEL_LANDING`<br>11 = `DEFOG_OVERRIDE`<br>12 = `SET_TEMP_LO`<br>13 = `SET_TEMP_HI`<br>14 = `CABIN_PURGE`<br>15 = `EVAP_DRYING`<br>16 = `EVAP_OIL_PURGE`<br>17 = `HVAC_OFF`<br>18 = `DUCT_TARGETS_INVALID`<br>19 = `BIODEFENSE`<br>20 = `HVAC_AIR_HUMID`<br>21 = `RETURN_FROM_DEFOG_OVERRIDE`<br>22 = `VOC_PURGE`<br>23 = `END` | validated |
| `VCRIGHT_hvacMassflowTarget` | page 3 | Right body controller: hvac massflow target | 29\|8 | little-endian | unsigned | 1 | 0 | g/s | 0 to 200 |  | validated |
| `VCRIGHT_hvacQdotLimitedLeft` | page 3 | Right body controller: hvac qdot limited left | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_hvacQdotLimitedRight` | page 3 | Right body controller: hvac qdot limited right | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_LHPanelAirflowBlocked` | page 3 | Right body controller: LH panel airflow blocked | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_RHPanelAirflowBlocked` | page 3 | Right body controller: RH panel airflow blocked | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_floorAirflowBlocked` | page 3 | Right body controller: floor airflow blocked | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_defrostAirflowBlocked` | page 3 | Right body controller: defrost airflow blocked | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_hvacFilterLifeDetectActive` | page 3 | Indicates when filter life detection is active | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_hvacLHBleedOperationMode` | page 3 | Right body controller: hvac LH bleed operation mode | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `HVACACTUATOR_OPERATION_MODE_NORMAL`<br>1 = `HVACACTUATOR_OPERATION_MODE_CALIBRATION` | validated |
| `VCRIGHT_hvacRHBleedOperationMode` | page 3 | Right body controller: hvac RH bleed operation mode | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `HVACACTUATOR_OPERATION_MODE_NORMAL`<br>1 = `HVACACTUATOR_OPERATION_MODE_CALIBRATION` | validated |
| `VCRIGHT_hvacLHVaneOperationMode` | page 3 | Right body controller: hvac LH vane operation mode | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `HVACACTUATOR_OPERATION_MODE_NORMAL`<br>1 = `HVACACTUATOR_OPERATION_MODE_CALIBRATION` | validated |
| `VCRIGHT_hvacRHVaneOperationMode` | page 3 | Right body controller: hvac RH vane operation mode | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `HVACACTUATOR_OPERATION_MODE_NORMAL`<br>1 = `HVACACTUATOR_OPERATION_MODE_CALIBRATION` | validated |
| `VCRIGHT_hvacUpperModeOpMode` | page 3 | Right body controller: hvac upper mode op mode | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `HVACACTUATOR_OPERATION_MODE_NORMAL`<br>1 = `HVACACTUATOR_OPERATION_MODE_CALIBRATION` | validated |
| `VCRIGHT_hvacLowerModeOpMode` | page 3 | Right body controller: hvac lower mode op mode | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `HVACACTUATOR_OPERATION_MODE_NORMAL`<br>1 = `HVACACTUATOR_OPERATION_MODE_CALIBRATION` | validated |
| `VCRIGHT_hvacIntakeOperationMode` | page 3 | Right body controller: hvac intake operation mode | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `HVACACTUATOR_OPERATION_MODE_NORMAL`<br>1 = `HVACACTUATOR_OPERATION_MODE_CALIBRATION` | validated |
| `VCRIGHT_isProbeFeedbackApplied` | page 3 | Right body controller: is probe feedback applied | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OFF`<br>1 = `POSITIVE`<br>2 = `NEGATIVE`<br>3 = `POSITIVEHIGH`<br>4 = `NEGATIVEHIGH` | validated |
| `VCRIGHT_feedbackPullDownScalar` | page 3 | Right body controller: feedback pull down scalar | 55\|2 | little-endian | unsigned | 30 | 70 | - | 70 to 130 |  | validated |
| `VCRIGHT_feedForwardPullDownScalar` | page 3 | Right body controller: feed forward pull down scalar | 57\|6 | little-endian | unsigned | 1 | 70 | - | 70 to 130 |  | validated |
| `VCRIGHT_convectionTargetLeft` | page 4 | Right body controller: convection target left; raw 511 = signal not available (SNA) | 5\|9 | little-endian | unsigned | 4 | -1000 | W/m2 | -1000 to 1000 | 511 = `SNA` | validated |
| `VCRIGHT_convectionTargetRight` | page 4 | Right body controller: convection target right; raw 511 = signal not available (SNA) | 14\|9 | little-endian | unsigned | 4 | -1000 | W/m2 | -1000 to 1000 | 511 = `SNA` | validated |
| `VCRIGHT_convectionDeliveredLeft` | page 4 | Right body controller: convection delivered left; raw 511 = signal not available (SNA) | 23\|9 | little-endian | unsigned | 4 | -1000 | W/m2 | -1000 to 1000 | 511 = `SNA` | validated |
| `VCRIGHT_convectionDeliveredRight` | page 4 | Right body controller: convection delivered right; raw 511 = signal not available (SNA) | 32\|9 | little-endian | unsigned | 4 | -1000 | W/m2 | -1000 to 1000 | 511 = `SNA` | validated |
| `VCRIGHT_solarLoadRightOccupant` | page 4 | Right body controller: solar load right occupant; raw 127 = signal not available (SNA) | 41\|7 | little-endian | unsigned | 2 | 0 | W/m2 | 0 to 252 | 127 = `SNA` | validated |
| `VCRIGHT_solarLoadLeftOccupant` | page 4 | Right body controller: solar load left occupant; raw 127 = signal not available (SNA) | 48\|7 | little-endian | unsigned | 2 | 0 | W/m2 | 0 to 252 | 127 = `SNA` | validated |
| `VCRIGHT_ptcShutOutletMitigationActive` | page 4 | Right body controller: ptc shut outlet mitigation active | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_solarLoadFromThsTemp` | page 4 | Right body controller: solar load from ths temp; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 8 | -1020 | W/m2 | -1020 to 1012 | 255 = `SNA` | validated |
| `VCRIGHT_ptcHeaterTempDuctHigh` | page 5 | Right body controller: ptc heater temp duct high | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_ptcHeaterTempDuctFault` | page 5 | Right body controller: ptc heater temp duct fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_ptcHeaterNoAirflow` | page 5 | Right body controller: ptc heater no airflow | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_ptcHeaterHvacActNotReady` | page 5 | Right body controller: ptc heater hvac act not ready | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_ptcHeaterNoUiRequest` | page 5 | Right body controller: ptc heater no ui request | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_ptcHeaterNoHighVoltage` | page 5 | Right body controller: ptc heater no high voltage | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_ptcHeaterLAirPathBlocked` | page 5 | Right body controller: ptc heater l air path blocked | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_ptcHeaterRAirPathBlocked` | page 5 | Right body controller: ptc heater r air path blocked | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_ptcHeaterReqAirpathBlocked` | page 5 | Right body controller: ptc heater req airpath blocked | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_hvacQdotFeedforward` | page 5 | Right body controller: hvac qdot feedforward | 16\|16 | little-endian | unsigned | 1 | -32767 | W | -32767 to 32767 |  | plausible |
| `VCRIGHT_evapLoadInFresh` | page 5 | Right body controller: evap load in fresh | 32\|8 | little-endian | unsigned | 35 | 0 | W | 0 to 8000 |  | plausible |
| `VCRIGHT_evapLoadInRecirc` | page 5 | Right body controller: evap load in recirc | 40\|8 | little-endian | unsigned | 35 | 0 | W | 0 to 8000 |  | plausible |
| `VCRIGHT_cabinTempWshldDefog` | page 5 | Windshield temperature estimate used for defogging; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_cabinTempWshldDefogTop` | page 5 | Right body controller: cabin temp wshld defog top; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_hvacLHBleedVoltage` | page 6 | Right body controller: hvac LH bleed voltage | 8\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_hvacRHBleedVoltage` | page 6 | Right body controller: hvac RH bleed voltage | 16\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_hvacLHVaneVoltage` | page 6 | Right body controller: hvac LH vane voltage | 24\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_hvacRHVaneVoltage` | page 6 | Right body controller: hvac RH vane voltage | 32\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_hvacUpperModeVoltage` | page 6 | Right body controller: hvac upper mode voltage | 40\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_hvacLowerModeVoltage` | page 6 | Right body controller: hvac lower mode voltage | 48\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_hvacIntakeVoltage` | page 6 | Right body controller: hvac intake voltage | 56\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_cabinTempBreathLevelFHeating` | page 7 | Right body controller: cabin temp breath level f heating; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | plausible |
| `VCRIGHT_cabinTempBreathLevelFCooling` | page 7 | Right body controller: cabin temp breath level f cooling; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | plausible |
| `VCRIGHT_cabinTempBreathLevelF5minHeating` | page 7 | Right body controller: cabin temp breath level f5min heating; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | plausible |
| `VCRIGHT_cabinTempBreathLevelF5minCooling` | page 7 | Right body controller: cabin temp breath level f5min cooling; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | plausible |
| `VCRIGHT_cabinTempBreathLevelF10minHeating` | page 7 | Right body controller: cabin temp breath level f10min heating; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | plausible |
| `VCRIGHT_cabinTempBreathLevelF10minCooling` | page 7 | Right body controller: cabin temp breath level f10min cooling; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | plausible |
| `VCRIGHT_cabinTempInteriorFHeating` | page 7 | Right body controller: cabin temp interior f heating; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | plausible |
| `VCRIGHT_hvacCabOvrheatProtActive` | page 8 | Status of cabin overheat protection | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_hvacCabinPurgeAllowed` | page 8 | Right body controller: hvac cabin purge allowed | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_hvacCabOvrheatProtAllowed` | page 8 | Cabin overheat protection is allowed to run | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_filterLifeBlowerTorque` | page 8 | Right body controller: filter life blower torque; raw 1023 = signal not available (SNA) | 8\|10 | little-endian | unsigned | 0.006 | -1.5 | Nm | -1.5 to 4.5 | 1023 = `SNA` | plausible |
| `VCRIGHT_cabinTempFanCurrent` | page 8 | Right body controller: cabin temp fan current | 18\|6 | little-endian | unsigned | 0.001 | -0.01 | A | -0.01 to 0.05 |  | validated |
| `VCRIGHT_cabinTempFanOutput` | page 8 | Right body controller: cabin temp fan output | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_cloudinessEstimatedPct` | page 8 | Right body controller: cloudiness estimated pct | 25\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_solarLoadOnVehFiltered` | page 8 | Right body controller: solar load on veh filtered; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 4 | 0 | W/m2 | 0 to 1016 | 255 = `SNA` | validated |
| `VCRIGHT_cabinTempProbeEstimate` | page 8 | Right body controller: cabin temp probe estimate; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_cabinTempThs` | page 8 | Estimated temperature from Tesla HVAC Sensor; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_cabinTempThsBracket` | page 8 | Right body controller: cabin temp ths bracket; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_leftHeatOvertempProtect` | page 9 | Right body controller: left heat overtemp protect | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_rightHeatOvertempProtect` | page 9 | Right body controller: right heat overtemp protect | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_CO2ppm` | page 9 | Right body controller: co2ppm; raw 1023 = signal not available (SNA) | 7\|10 | little-endian | unsigned | 5 | 0 | - | 0 to 4000 | 1023 = `SNA` | validated |
| `VCRIGHT_timeLeftToCabinModelInit` | page 9 | Right body controller: time left to cabin model init | 17\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 |  | validated |
| `VCRIGHT_hvacEstimateWindshieldRH` | page 9 | Estimated windshield relative humidity | 24\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 150 |  | validated |
| `VCRIGHT_hvacFoggingRiskLevel` | page 9 | Control signal of the windshield fogging risk controller | 32\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvacCabinHumidityLevel` | page 9 | Control signal of the cabin humidity controller | 39\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvacFlashFoggingDetected` | page 9 | Windshield flash fogging risk detected | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_solarSensitivityInfr` | page 9 | Right body controller: solar sensitivity infr | 48\|7 | little-endian | unsigned | 1 | 0 | - | 0 to 100 |  | validated |
| `VCRIGHT_solarSensitivityInfrCorr` | page 9 | Right body controller: solar sensitivity infr corr | 55\|7 | little-endian | unsigned | 1 | 0 | - | 0 to 100 |  | validated |
| `VCRIGHT_lumbarCurrent` | page 10 | Electrical current of the lumbar ECU | 5\|4 | little-endian | unsigned | 0.2 | 0 | A | 0 to 3 |  | validated |
| `VCRIGHT_ocsCurrent` | page 10 | Electrical current of the OCS ECU | 9\|3 | little-endian | unsigned | 0.01 | 0 | A | 0 to 0.07 |  | validated |
| `VCRIGHT_rcmCurrent` | page 10 | Electrical current of the RCM ECU | 12\|5 | little-endian | unsigned | 0.1 | 0 | A | 0 to 3.1 |  | validated |
| `VCRIGHT_radioTunerCurrent` | page 10 | Electrical current of the Radio Tuner | 17\|4 | little-endian | unsigned | 0.1 | 0 | A | 0 to 1.5 |  | validated |
| `VCRIGHT_rearOilPumpCurrent` | page 10 | Right body controller: rear oil pump current | 21\|5 | little-endian | unsigned | 0.5 | 0 | A | 0 to 15.5 |  | validated |
| `VCRIGHT_rearDefrostCurrent` | page 10 | Right body controller: rear defrost current | 26\|5 | little-endian | unsigned | 2 | 0 | A | 0 to 62 |  | validated |
| `VCRIGHT_tailLightCurrent` | page 10 | Electrical current of the tail and license plate lights | 31\|4 | little-endian | unsigned | 0.1 | 0 | A | 0 to 1.5 |  | validated |
| `VCRIGHT_turnTailStopLightCurrent` | page 10 | Reports the electrical current of the right rear turn indicator, right rear tail light, or right rear brake light | 35\|4 | little-endian | unsigned | 0.1 | 0 | A | 0 to 1.5 |  | validated |
| `VCRIGHT_reverseFogLightsCurrent` | page 10 | Electrical current of the trunk fog light; raw 15 = signal not available (SNA) | 39\|4 | little-endian | unsigned | 0.1 | 0 | A | 0 to 1.4 | 15 = `SNA` | validated |
| `VCRIGHT_stopReverseTurnLightCurrent` | page 10 | Reports the electrical current of the right rear brake light, right rear reverse light, or right rear turn indicator | 43\|4 | little-endian | unsigned | 0.1 | 0 | A | 0 to 1.5 |  | validated |
| `VCRIGHT_sideMirrorCurrent` | page 10 | Electrical current of side mirror tilt and fold | 47\|5 | little-endian | unsigned | 0.2 | 0 | A | 0 to 6.2 |  | validated |
| `VCRIGHT_sideMirrorHeaterCurrent` | page 10 | Electrical current of the mirror heater; raw 31 = signal not available (SNA) | 52\|5 | little-endian | unsigned | 0.2 | 0 | A | 0 to 6 | 31 = `SNA` | validated |
| `VCRIGHT_frontSeatHeatCushionPwr` | page 10 | Right body controller: front seat heat cushion pwr | 57\|7 | little-endian | unsigned | 1 | 0 | W | 0 to 127 |  | validated |
| `VCRIGHT_trunkInteriorLEDCurrent` | page 11 | Electrical current of the trunk interior light; raw 15 = signal not available (SNA) | 8\|4 | little-endian | unsigned | 5 | 0 | mA | 0 to 70 | 15 = `SNA` | validated |
| `VCRIGHT_mapPocketLEDsCurrent` | page 11 | Electrical current of the map pocket lights; raw 15 = signal not available (SNA) | 12\|4 | little-endian | unsigned | 5 | 0 | mA | 0 to 70 | 15 = `SNA` | validated |
| `VCRIGHT_miscEFuseCurrent` | page 11 | Right body controller: misc e fuse current; raw 31 = signal not available (SNA) | 16\|5 | little-endian | unsigned | 0.05 | 0 | A | 0 to 1.5 | 31 = `SNA` | validated |
| `VCRIGHT_interiorHandleLEDCurrent` | page 11 | Electrical current of the interior handle LED | 21\|4 | little-endian | unsigned | 2 | 0 | mA | 0 to 30 |  | validated |
| `VCRIGHT_miscInteriorLightsCurrent` | page 11 | Electrical current of the misc interior lights; raw 7 = signal not available (SNA) | 25\|3 | little-endian | unsigned | 5 | 0 | mA | 0 to 30 | 7 = `SNA` | validated |
| `VCRIGHT_frontPuddleLEDCurrent` | page 11 | Electrical current of the front puddle LED; raw 7 = signal not available (SNA) | 28\|3 | little-endian | unsigned | 0.05 | 0 | A | 0 to 0.3 | 7 = `SNA` | validated |
| `VCRIGHT_rearPuddleLEDCurrent` | page 11 | Electrical current of the rear puddle LED; raw 7 = signal not available (SNA) | 31\|3 | little-endian | unsigned | 0.05 | 0 | A | 0 to 0.3 | 7 = `SNA` | validated |
| `VCRIGHT_liftgateShutfaceLEDCurrent` | page 11 | Electrical current of the liftgate shutface LED; raw 7 = signal not available (SNA) | 34\|3 | little-endian | unsigned | 5 | 0 | mA | 0 to 30 | 7 = `SNA` | validated |
| `VCRIGHT_3rSeatTOSCurrent` | page 11 | Electrical current of the 3R TOS; raw 15 = signal not available (SNA) | 37\|4 | little-endian | unsigned | 5 | 0 | mA | 0 to 70 | 15 = `SNA` | validated |
| `VCRIGHT_vbatFusedCurrent` | page 11 | Right body controller: vbat fused current; raw 15 = signal not available (SNA) | 41\|4 | little-endian | unsigned | 0.1 | 0 | A | 0 to 1.4 | 15 = `SNA` | validated |
| `VCRIGHT_cabinTempGlassGridHeater` | page 11 | Right body controller: cabin temp glass grid heater; raw 255 = signal not available (SNA) | 45\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | validated |
| `VCRIGHT_hvacAirflowReasonRight` | page 11 | Right body controller: hvac airflow reason right | 53\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `HVAC_OFF`<br>1 = `MANUAL_FAN_SPEED`<br>2 = `UI_SHORTCUT`<br>3 = `CABIN_TEMPERATURE_CONTROL`<br>4 = `MINIMUM_AUTO_AIRFLOW`<br>5 = `STRATIFICATION_GLASS_ROOF`<br>6 = `STRATIFICATION_INTERIOR_SURFACES`<br>7 = `OCCUPANT_CONVECTION_REQUIREMENT`<br>8 = `OUTLET_TEMP_LIMIT`<br>9 = `CABIN_PURGE`<br>10 = `CABIN_OVERHEAT_PROTECT`<br>11 = `SCREEN_PROTECTION`<br>12 = `EVAP_DRYING`<br>13 = `EVAP_OIL_PURGE`<br>14 = `BIOWEAPON_DEFENSE`<br>15 = `COLD_DUCT_LOCKOUT`<br>16 = `HOT_DUCT_LOCKOUT`<br>17 = `STRATIFICATION_TOP_PAD_AREA`<br>18 = `VOC_PURGE`<br>19 = `DRIVERLESS_SELF_TEST`<br>20 = `ODOR_ROUTINE`<br>21 = `NONE` | validated |
| `VCRIGHT_hvacAirflowReasonLeft` | page 11 | Right body controller: hvac airflow reason left | 58\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `HVAC_OFF`<br>1 = `MANUAL_FAN_SPEED`<br>2 = `UI_SHORTCUT`<br>3 = `CABIN_TEMPERATURE_CONTROL`<br>4 = `MINIMUM_AUTO_AIRFLOW`<br>5 = `STRATIFICATION_GLASS_ROOF`<br>6 = `STRATIFICATION_INTERIOR_SURFACES`<br>7 = `OCCUPANT_CONVECTION_REQUIREMENT`<br>8 = `OUTLET_TEMP_LIMIT`<br>9 = `CABIN_PURGE`<br>10 = `CABIN_OVERHEAT_PROTECT`<br>11 = `SCREEN_PROTECTION`<br>12 = `EVAP_DRYING`<br>13 = `EVAP_OIL_PURGE`<br>14 = `BIOWEAPON_DEFENSE`<br>15 = `COLD_DUCT_LOCKOUT`<br>16 = `HOT_DUCT_LOCKOUT`<br>17 = `STRATIFICATION_TOP_PAD_AREA`<br>18 = `VOC_PURGE`<br>19 = `DRIVERLESS_SELF_TEST`<br>20 = `ODOR_ROUTINE`<br>21 = `NONE` | validated |
| `VCRIGHT_hvacMassflowTargetLeft` | page 12 | Right body controller: hvac massflow target left | 5\|8 | little-endian | unsigned | 1 | 0 | g/s | 0 to 200 |  | validated |
| `VCRIGHT_hvacMassflowTargetRight` | page 12 | Right body controller: hvac massflow target right | 13\|8 | little-endian | unsigned | 1 | 0 | g/s | 0 to 200 |  | validated |
| `VCRIGHT_solarLoadLeftOccupantFilt` | page 12 | Right body controller: solar load left occupant filt; raw 127 = signal not available (SNA) | 21\|7 | little-endian | unsigned | 2 | 0 | W/m2 | 0 to 252 | 127 = `SNA` | validated |
| `VCRIGHT_solarLoadRightOccupantFilt` | page 12 | Right body controller: solar load right occupant filt; raw 127 = signal not available (SNA) | 28\|7 | little-endian | unsigned | 2 | 0 | W/m2 | 0 to 252 | 127 = `SNA` | validated |
| `VCRIGHT_windshieldRHCapped` | page 12 | Estimated windshield relative humidity | 35\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 150 |  | validated |
| `VCRIGHT_feedbackWarmUpScalar` | page 12 | Right body controller: feedback warm up scalar | 43\|2 | little-endian | unsigned | 16 | 84 | - | 84 to 116 |  | validated |
| `VCRIGHT_maxMassflowScalarWarmUp` | page 12 | Right body controller: max massflow scalar warm up | 45\|5 | little-endian | unsigned | 1 | 74 | - | 74 to 100 |  | validated |
| `VCRIGHT_feedforwardWarmUpScalar` | page 12 | Right body controller: feedforward warm up scalar | 50\|6 | little-endian | unsigned | 1 | 80 | - | 80 to 120 |  | validated |
| `VCRIGHT_frontSeatHeatBackrestPwr` | page 12 | Right body controller: front seat heat backrest pwr | 56\|7 | little-endian | unsigned | 1 | 0 | W | 0 to 127 |  | validated |
| `VCRIGHT_maxMassflowScalar` | page 13 | Right body controller: max massflow scalar | 5\|6 | little-endian | unsigned | 1 | 60 | - | 60 to 100 |  | validated |
| `VCRIGHT_massflowTargetAutoInManualMode` | page 13 | Right body controller: massflow target auto in manual mode | 11\|8 | little-endian | unsigned | 1 | 0 | g/s | 0 to 250 |  | validated |
| `VCRIGHT_airflowReasonAutoInManualMode` | page 13 | Right body controller: airflow reason auto in manual mode | 19\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `HVAC_OFF`<br>1 = `MANUAL_FAN_SPEED`<br>2 = `UI_SHORTCUT`<br>3 = `CABIN_TEMPERATURE_CONTROL`<br>4 = `MINIMUM_AUTO_AIRFLOW`<br>5 = `STRATIFICATION_GLASS_ROOF`<br>6 = `STRATIFICATION_INTERIOR_SURFACES`<br>7 = `OCCUPANT_CONVECTION_REQUIREMENT`<br>8 = `OUTLET_TEMP_LIMIT`<br>9 = `CABIN_PURGE`<br>10 = `CABIN_OVERHEAT_PROTECT`<br>11 = `SCREEN_PROTECTION`<br>12 = `EVAP_DRYING`<br>13 = `EVAP_OIL_PURGE`<br>14 = `BIOWEAPON_DEFENSE`<br>15 = `COLD_DUCT_LOCKOUT`<br>16 = `HOT_DUCT_LOCKOUT`<br>17 = `STRATIFICATION_TOP_PAD_AREA`<br>18 = `VOC_PURGE`<br>19 = `DRIVERLESS_SELF_TEST`<br>20 = `ODOR_ROUTINE`<br>21 = `NONE` | validated |
| `VCRIGHT_airflowReasonAutoInManualModeLeft` | page 13 | Right body controller: airflow reason auto in manual mode left | 24\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `HVAC_OFF`<br>1 = `MANUAL_FAN_SPEED`<br>2 = `UI_SHORTCUT`<br>3 = `CABIN_TEMPERATURE_CONTROL`<br>4 = `MINIMUM_AUTO_AIRFLOW`<br>5 = `STRATIFICATION_GLASS_ROOF`<br>6 = `STRATIFICATION_INTERIOR_SURFACES`<br>7 = `OCCUPANT_CONVECTION_REQUIREMENT`<br>8 = `OUTLET_TEMP_LIMIT`<br>9 = `CABIN_PURGE`<br>10 = `CABIN_OVERHEAT_PROTECT`<br>11 = `SCREEN_PROTECTION`<br>12 = `EVAP_DRYING`<br>13 = `EVAP_OIL_PURGE`<br>14 = `BIOWEAPON_DEFENSE`<br>15 = `COLD_DUCT_LOCKOUT`<br>16 = `HOT_DUCT_LOCKOUT`<br>17 = `STRATIFICATION_TOP_PAD_AREA`<br>18 = `VOC_PURGE`<br>19 = `DRIVERLESS_SELF_TEST`<br>20 = `ODOR_ROUTINE`<br>21 = `NONE` | validated |
| `VCRIGHT_airflowReasonAutoInManualModeRight` | page 13 | Right body controller: airflow reason auto in manual mode right | 29\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `HVAC_OFF`<br>1 = `MANUAL_FAN_SPEED`<br>2 = `UI_SHORTCUT`<br>3 = `CABIN_TEMPERATURE_CONTROL`<br>4 = `MINIMUM_AUTO_AIRFLOW`<br>5 = `STRATIFICATION_GLASS_ROOF`<br>6 = `STRATIFICATION_INTERIOR_SURFACES`<br>7 = `OCCUPANT_CONVECTION_REQUIREMENT`<br>8 = `OUTLET_TEMP_LIMIT`<br>9 = `CABIN_PURGE`<br>10 = `CABIN_OVERHEAT_PROTECT`<br>11 = `SCREEN_PROTECTION`<br>12 = `EVAP_DRYING`<br>13 = `EVAP_OIL_PURGE`<br>14 = `BIOWEAPON_DEFENSE`<br>15 = `COLD_DUCT_LOCKOUT`<br>16 = `HOT_DUCT_LOCKOUT`<br>17 = `STRATIFICATION_TOP_PAD_AREA`<br>18 = `VOC_PURGE`<br>19 = `DRIVERLESS_SELF_TEST`<br>20 = `ODOR_ROUTINE`<br>21 = `NONE` | validated |
| `VCRIGHT_cabinTempInteriorFCooling` | page 13 | Right body controller: cabin temp interior f cooling; raw 255 = signal not available (SNA) | 34\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | plausible |
| `VCRIGHT_averageDuctTempFHeating` | page 13 | Estimated average duct temp temp 15 min into the drive; raw 255 = signal not available (SNA) | 42\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | plausible |
| `VCRIGHT_averageDuctTempFCooling` | page 13 | Estimated average duct temp temp 15 min into the drive; raw 255 = signal not available (SNA) | 50\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | plausible |
| `VCRIGHT_hvacBiLevelWhsldRhEst` | page 13 | Right body controller: hvac bi level whsld rh est | 58\|6 | little-endian | unsigned | 2 | 20 | % | 20 to 120 |  | validated |
| `VCRIGHT_steeringWheelSurfaceTempEst` | page 14 | Right body controller: steering wheel surface temp est; raw 1023 = signal not available (SNA) | 5\|10 | little-endian | unsigned | 0.1 | -35 | degC | -35 to 65 | 1023 = `SNA` | validated |
| `VCRIGHT_steeringWheelSurfaceTempTgt` | page 14 | Right body controller: steering wheel surface temp tgt; raw 1023 = signal not available (SNA) | 16\|10 | little-endian | unsigned | 0.1 | -35 | degC | -35 to 65 | 1023 = `SNA` | validated |
| `VCRIGHT_timeToComfortHeating` | page 14 | Right body controller: time to comfort heating | 26\|6 | little-endian | unsigned | 15 | -15 | s | -15 to 930 | 0 = `IN_COMFORT_BAND`<br>62 = `UNATTAINABLE`<br>63 = `HVAC_OFF` | validated |
| `VCRIGHT_timeToComfortCooling` | page 14 | Right body controller: time to comfort cooling | 32\|6 | little-endian | unsigned | 15 | -15 | s | -15 to 930 | 0 = `IN_COMFORT_BAND`<br>62 = `UNATTAINABLE`<br>63 = `HVAC_OFF` | validated |
| `VCRIGHT_cabinWaterMassRaw` | page 14 | Right body controller: cabin water mass raw; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.1 | 0 | g/kg | 0 to 25 | 255 = `SNA` | plausible |
| `VCRIGHT_massflowSingleZoneSplit` | page 14 | Right body controller: massflow single zone split | 48\|7 | little-endian | unsigned | 1 | 0 | - | 0 to 100 |  | plausible |
| `VCRIGHT_VOCPurgeState` | page 14 | Right body controller: VOC purge state | 56\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INIT`<br>1 = `INACTIVE`<br>2 = `IDLE`<br>3 = `PURGING`<br>4 = `WAITING`<br>5 = `PURGING_AND_DRYING` | plausible |
| `VCRIGHT_cameraFoggingMonitorState` | page 14 | Right body controller: camera fogging monitor state | 59\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INIT`<br>1 = `MONITORING`<br>2 = `WAKEUP`<br>3 = `RUNNING`<br>4 = `INACTIVE`<br>5 = `IDLE`<br>6 = `PRE_RUN_PURGE` | plausible |
| `VCRIGHT_cabinOverheatProtectNotRunningReasonRaw` | page 15 | Reports all reasons cabin overheat protection is not running. | 5\|14 | little-endian | unsigned | 1 | 0 |  | 0 to 16383 |  | validated |
| `VCRIGHT_hvacIntakeReason` | page 15 | Reason for current intake door position | 19\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `INTAKE_REASON_NONE`<br>1 = `INTAKE_REASON_UDS`<br>2 = `INTAKE_REASON_CAR_WASH`<br>3 = `INTAKE_REASON_MANUAL_FRESH`<br>4 = `INTAKE_REASON_MANUAL_RECIRC`<br>5 = `INTAKE_REASON_TEMPERATURE_CONTROL`<br>6 = `INTAKE_REASON_BIO_WEAPON_INIT`<br>7 = `INTAKE_REASON_BIO_WEAPON_STEADY`<br>8 = `INTAKE_REASON_HUMIDITY`<br>9 = `INTAKE_REASON_PRECON_OVERRIDE`<br>10 = `INTAKE_REASON_CHARGE_PORT_THAW`<br>11 = `INTAKE_REASON_ENHANCED_FILTERATION`<br>12 = `INTAKE_REASON_COP`<br>13 = `INTAKE_REASON_CABIN_PURGE`<br>14 = `INTAKE_REASON_OIL_PURGE`<br>15 = `INTAKE_REASON_EVAP_DRYING`<br>16 = `INTAKE_REASON_PARK_POSITION`<br>17 = `INTAKE_REASON_HVAC_OFF`<br>18 = `INTAKE_REASON_CO2_PURGE`<br>19 = `INTAKE_REASON_RECIRC_NVH`<br>20 = `INTAKE_REASON_PULLDOWN_IN_FRESH`<br>21 = `INTAKE_REASON_STEAMING`<br>22 = `INTAKE_REASON_VOC_PURGE`<br>23 = `INTAKE_REASON_DRIVERLESS_SELF_TEST`<br>24 = `INTAKE_REASON_LIFTGATE_CLOSING`<br>25 = `INTAKE_REASON_HVAC_OFF_IN_MOTION`<br>26 = `INTAKE_REASON_ODOR_ROUTINE` | validated |
| `VCRIGHT_hvacCabinPurgeActive` | page 15 | Indicates if cabin purge is active | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_solarAzimuthCarRef` | page 15 | Right body controller: solar azimuth car ref; raw 1025 = signal not available (SNA) | 25\|11 | little-endian | signed | 0.5 | 0 | deg | -511 to 511.5 | -1023 = `SNA` | validated |
| `VCRIGHT_massflowPulldownBias` | page 15 | Right body controller: massflow pulldown bias | 36\|4 | little-endian | unsigned | 7 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_evapPulldownBias` | page 15 | Right body controller: evap pulldown bias | 40\|4 | little-endian | unsigned | 7 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_modeledMassflowFresh` | page 15 | Right body controller: modeled massflow fresh | 44\|8 | little-endian | unsigned | 1 | 0 | g/s | 0 to 255 |  | validated |
| `VCRIGHT_modeledMassflowRecirc` | page 15 | Right body controller: modeled massflow recirc | 52\|8 | little-endian | unsigned | 1 | 0 | g/s | 0 to 255 |  | validated |
| `VCRIGHT_hvacLimpModeStatus` | page 15 | Reports the cabin model limp mode status. | 60\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `LIMP_MODE_NOT_NEEDED`<br>1 = `LIMP_MODE_WAITING_FOR_SENSORS`<br>2 = `LIMP_MODE_READY`<br>3 = `LIMP_MODE_ACTIVE`<br>4 = `LIMP_MODE_FAULTED` | validated |
| `VCRIGHT_hvacEstimatedCameraWindshieldRH` | page 16 | Right body controller: hvac estimated camera windshield RH | 8\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 150 |  | plausible |

## Multiplexing

`VCRIGHT_logging1HzIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (7 signals), page 1 (7 signals), page 2 (6 signals), page 3 (21 signals), page 4 (8 signals), page 5 (14 signals), page 6 (7 signals), page 7 (7 signals), page 8 (11 signals), page 9 (10 signals), page 10 (13 signals), page 11 (13 signals), page 12 (9 signals), page 13 (9 signals), page 14 (8 signals), page 15 (9 signals), page 16 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
