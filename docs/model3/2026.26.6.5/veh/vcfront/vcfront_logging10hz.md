---
layout: default
title: "VCFRONT_logging10Hz (0x2C1) — Front body controller, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Front body controller message: logging10 hz. Tesla Model 3 CAN bus message VCFRONT_logging10Hz (0x2C1) of Front body controller, firmware 2026.26.6.5, 23 signals (VCFRONT_logging10HzIndex, VCFRONT_pumpBatteryOutVoltage, VCFRONT_pumpPowertrainOutVoltage, VCFRONT_pumpBatteryInitd and 19 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_logging10Hz (0x2C1) — Front body controller, Tesla Model 3 2026.26.6.5 VEH CAN

Front body controller message: logging10 hz; frame length observed on a vehicle bus. This page documents the 23 signals of VCFRONT_logging10Hz as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_logging10Hz` |
| CAN id | 0x2C1 (705) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT |
| Frame length | 8 bytes |
| Cycle time | 20 ms |
| Signals | 23 |

## Signals of VCFRONT_logging10Hz

Tesla Model 3 CAN bus signals in `VCFRONT_logging10Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_logging10HzIndex` | selector | Front body controller: logging10 hz index | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `COOLANT_PUMPS_FAN`<br>1 = `THERMAL_FAN_COOLANT_COMP`<br>2 = `COMPRESSOR_REFRIGERANT_LOUVER`<br>3 = `ACTIVE_LOUVER_RADAR`<br>4 = `EXV_TORQUE_COUNT`<br>5 = `END` | plausible |
| `VCFRONT_pumpBatteryOutVoltage` | page 0 | Front body controller: pump battery out voltage | 3\|7 | little-endian | unsigned | 0.2 | 0 | V | 0 to 20 |  | validated |
| `VCFRONT_pumpPowertrainOutVoltage` | page 0 | Front body controller: pump powertrain out voltage | 10\|7 | little-endian | unsigned | 0.2 | 0 | V | 0 to 20 |  | validated |
| `VCFRONT_pumpBatteryInitd` | page 0 | Front body controller: pump battery initd | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_pumpPowertrainInitd` | page 0 | Front body controller: pump powertrain initd | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_pumpBatteryEnabled` | page 0 | Front body controller: pump battery enabled | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_pumpPowertrainEnabled` | page 0 | Front body controller: pump powertrain enabled | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_pumpBatteryPowerOn` | page 0 | Front body controller: pump battery power on | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_pumpPowertrainPowerOn` | page 0 | Front body controller: pump powertrain power on | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_pumpsWake` | page 0 | Front body controller: pumps wake | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_pumpBatSpiError` | page 0 | Front body controller: pump bat spi error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_pumpPtSpiError` | page 0 | Front body controller: pump pt spi error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_coolantFlowChillerActual` | page 0 | Front body controller: coolant flow chiller actual | 26\|8 | little-endian | unsigned | 0.1 | 0 | LPM | 0 to 25 |  | validated |
| `VCFRONT_radiatorFanOutVoltage` | page 0 | Front body controller: radiator fan out voltage | 34\|7 | little-endian | unsigned | 0.2 | 0 | V | 0 to 20 |  | validated |
| `VCFRONT_radiatorFanInitd` | page 0 | Front body controller: radiator fan initd | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_radiatorFanEnabled` | page 0 | Indication that the cooling fan is enabled | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_radiatorFanPowerOn` | page 0 | Indication that the cooling fan is powered on | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_radiatorFanPhaseCurrent` | page 0 | Front body controller: radiator fan phase current | 44\|8 | little-endian | unsigned | 0.25 | -10 | A | -10 to 50 |  | validated |
| `VCFRONT_radiatorFanPhaseIMax` | page 0 | Front body controller: radiator fan phase i max | 52\|7 | little-endian | unsigned | 0.25 | 5 | A | 5 to 35 |  | validated |
| `VCFRONT_thmlFanSpiError` | page 0 | Front body controller: thml fan spi error | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_chargeTrapNominalCOP1BattHeat` | page 0 | Front body controller: charge trap nominal COP1 batt heat | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_chargeTrapNominalCOP1ChillerBattHeat` | page 0 | Front body controller: charge trap nominal COP1 chiller batt heat | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_COP1OilWarmingNeeded` | page 0 | Reports if refrigerant compressor oil warming is needed. | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Multiplexing

`VCFRONT_logging10HzIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (22 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
