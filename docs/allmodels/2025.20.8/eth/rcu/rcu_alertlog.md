---
layout: default
title: "RCU_alertLog (0x5BF) — RCU ECU, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "RCU ECU message: alert log. Ethernet-side message RCU_alertLog of RCU ECU for Tesla Model 3 / Model Y firmware 2025.20.8, 15 signals (RCU_alertID, RCU_alertState, RCU_a010_sensorPowerSupply, RCU_a010_sensorHardware and 11 more). Bit layout, scaling, units and value tables."
---

# RCU_alertLog (0x5BF) — RCU ECU, Tesla Model 3 / Model Y 2025.20.8 ETH

RCU ECU message: alert log. This page documents the 15 signals of RCU_alertLog as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `RCU_alertLog` |
| Ethernet-side id | 0x5BF (1471) |
| ECU | [RCU ECU](../../rcu.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | RCU |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 15 |

## Signals of RCU_alertLog

Tesla Model 3 / Model Y CAN bus signals in `RCU_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `RCU_alertID` | selector | RCU ECU: alert ID | 0\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_valveDriverFault`<br>2 = `a002_solenoidValveFault`<br>3 = `a003_pumpMotorFault`<br>4 = `a004_supplyOvervoltage`<br>5 = `a005_supplyUndervoltage`<br>6 = `a006_wakeLineOpen`<br>7 = `a007_pressureSensorFault`<br>8 = `a008_pressureNotCalibrated`<br>9 = `a009_brakeFluidLow`<br>10 = `a010_pedalSensorFault`<br>11 = `a011_idbPedalTravelMismatch`<br>12 = `a012_pedalSensorNotCal`<br>13 = `a013_mcuGenericFault`<br>14 = `a014_asicTempHigh`<br>15 = `a015_fluidLeakDetected`<br>16 = `a016_partyBusOff`<br>17 = `a017_chassisBusOff`<br>18 = `a018_DItorquePathFaulted`<br>19 = `a019_DItorquePathActive`<br>20 = `a020_BBstatusDLC`<br>21 = `a021_BBstatusChecksum`<br>22 = `a022_BBstatusCounter`<br>23 = `a023_IDBstatusDLC`<br>24 = `a024_IDBstatusChecksum`<br>25 = `a025_IDBstatusCounter`<br>26 = `a026_DIchassisControlDLC`<br>27 = `a027_DIchassisCtrlChecksum`<br>28 = `a028_DIchassisControlCounter`<br>29 = `a029_PMstate2DLC`<br>30 = `a030_PMstate2Checksum`<br>31 = `a031_PMstate2Counter`<br>32 = `a032_VCFRONTLVPowerStateDLC`<br>33 = `a033_VCFRONTLVPowerStateChecksum`<br>34 = `a034_VCFRONTLVPowerStateCounter`<br>35 = `a035_IDBpcpInvalid`<br>36 = `a036_IDBpspInvalid`<br>37 = `a037_IDBinputRodStrokeInvalid`<br>38 = `a038_DIsystemStatusDLC`<br>39 = `a039_DIaccelPosInvalid`<br>40 = `a040_DIgearInvalid`<br>41 = `a041_DIsystemStatusCounter`<br>42 = `a042_DIsystemStatusChecksum`<br>43 = `a043_VCFRONTiBoosterLvStateInvalid`<br>44 = `a044_VCFRONTsensorsMIA`<br>45 = `a045_VCFRONTtempInvalid`<br>46 = `a046_brakeFluidLevelSNA`<br>47 = `a047_ESPwheelSpeedsDLC`<br>48 = `a048_ESPFrLWSSLInvalid`<br>49 = `a049_ESPFrRWSSLInvalid`<br>50 = `a050_ESPReLWSSLInvalid`<br>51 = `a051_ESPReRWSSLInvalid`<br>52 = `a052_ESPwheelSpeedsCounter`<br>53 = `a053_ESPwheelSpeedsChecksum`<br>54 = `a054_IDBcircuitPressFaulted`<br>55 = `a055_IDBsimulatorPressFaulted`<br>56 = `a056_redundantControllerIsMaster`<br>57 = `a057_PMebrCmdStateInvalid`<br>58 = `a058_DIbrakeTorqueCommandAndFlagMismatch` | plausible |
| `RCU_alertState` |  | RCU ECU: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `RCU_a010_sensorPowerSupply` | page 10 | RCU ECU: a010 sensor power supply | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `RCU_a010_sensorHardware` | page 10 | RCU ECU: a010 sensor hardware | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `RCU_a010_sensorSignal` | page 10 | RCU ECU: a010 sensor signal | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `RCU_a023_validityOnChassisBus` | page 23 | RCU ECU: a023 validity on chassis bus | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `RCU_a023_validityOnPartyBus` | page 23 | RCU ECU: a023 validity on party bus | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `RCU_a024_validityOnChassisBus` | page 24 | RCU ECU: a024 validity on chassis bus | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `RCU_a024_validityOnPartyBus` | page 24 | RCU ECU: a024 validity on party bus | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `RCU_a025_validityOnChassisBus` | page 25 | RCU ECU: a025 validity on chassis bus | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `RCU_a025_validityOnPartyBus` | page 25 | RCU ECU: a025 validity on party bus | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `RCU_a035_validityOnChassisBus` | page 35 | RCU ECU: a035 validity on chassis bus | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `RCU_a035_validityOnPartyBus` | page 35 | RCU ECU: a035 validity on party bus | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `RCU_a036_validityOnChassisBus` | page 36 | RCU ECU: a036 validity on chassis bus | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |
| `RCU_a036_validityOnPartyBus` | page 36 | RCU ECU: a036 validity on party bus | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `NOT_OK` | plausible |

## Multiplexing

`RCU_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (3 signals), page 23 (2 signals), page 24 (2 signals), page 25 (2 signals), page 35 (2 signals), page 36 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All RCU ECU messages (RCU)](../../rcu.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
