---
layout: default
title: "TPMS_StatusC (0x36F) — Tire pressure monitoring, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Tire pressure monitoring message: status c. Tesla Model 3 / Model Y CAN bus message TPMS_StatusC (0x36F) of Tire pressure monitoring, firmware 2026.26.6.5, 46 signals (TPMS_c_globalHardWarning, TPMS_c_globalSoftWarning, TPMS_systemMalfunction, TPMS_WA_version and 42 more). Bit layout, scaling, units and value tables."
---

# TPMS_StatusC (0x36F) — Tire pressure monitoring, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Tire pressure monitoring message: status c; frame length from the layout, not yet observed on a vehicle bus. This page documents the 46 signals of TPMS_StatusC as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `TPMS_StatusC` |
| CAN id | 0x36F (879) |
| ECU | [Tire pressure monitoring](../../tpms.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | TPMS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 46 |

## Signals of TPMS_StatusC

Tesla Model 3 / Model Y CAN bus signals in `TPMS_StatusC`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `TPMS_c_globalHardWarning` | Tire pressure monitoring: c global hard warning | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_c_globalSoftWarning` | Tire pressure monitoring: c global soft warning | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_systemMalfunction` | Tire pressure monitoring: system malfunction | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_WA_version` | Tire pressure monitoring: WA version | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_globalDeltaPressure` | Tire pressure monitoring: global delta pressure | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_newSensorLearnt` | Tire pressure monitoring: new sensor learnt | 5\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | validated |
| `TPMS_softWarningRR` | Tire pressure monitoring: soft warning RR | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_hardWarningRR` | Tire pressure monitoring: hard warning RR | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_softWarningRL` | Tire pressure monitoring: soft warning RL | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_hardWarningRL` | Tire pressure monitoring: hard warning RL | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_softWarningFR` | Tire pressure monitoring: soft warning FR | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_hardWarningFR` | Tire pressure monitoring: hard warning FR | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_softWarningFL` | Tire pressure monitoring: soft warning FL | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_hardWarningFL` | Tire pressure monitoring: hard warning FL | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_learningStatus` | Monitors Tire Pressure Monitoring System (TPMS) Learn Status and evaluates issues. | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `FAILED`<br>1 = `ONGOING`<br>2 = `STOPPED`<br>3 = `PASSED` | validated |
| `TPMS_localisationStatus` | Monitors Tire Pressure Monitoring System (TPMS) Localization Status and evaluates issues. | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `FAILED`<br>1 = `ONGOING`<br>2 = `STOPPED`<br>3 = `PASSED` | validated |
| `TPMS_deltaPressWarningFL` | Tire pressure monitoring: delta press warning FL | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_deltaPressWarningFR` | Tire pressure monitoring: delta press warning FR | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_deltaPressWarningRL` | Tire pressure monitoring: delta press warning RL | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_deltaPressWarningRR` | Tire pressure monitoring: delta press warning RR | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_sensorNoResponseFL` | Count of times Front Left sensor did not respond to message | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_sensorNoResponseFR` | Count of times Front Right sensor did not respond to message | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_sensorNoResponseRL` | Count of times Rear Left sensor did not respond to message | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_sensorNoResponseRR` | Count of times Rear Right sensor did not respond to message | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_sensorThermShutdownFL` | Tire pressure monitoring: sensor therm shutdown FL | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_sensorThermShutdownFR` | Tire pressure monitoring: sensor therm shutdown FR | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_sensorThermShutdownRL` | Tire pressure monitoring: sensor therm shutdown RL | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_sensorThermShutdownRR` | Tire pressure monitoring: sensor therm shutdown RR | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_sensorBatteryLowFL` | Tracks near end of life sensor batteries in the fleet. | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_sensorBatteryLowFR` | Tracks near end of life sensor batteries in the fleet. | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_sensorBatteryLowRL` | Tracks near end of life sensor batteries in the fleet. | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_sensorBatteryLowRR` | Tracks near end of life sensor batteries in the fleet. | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_sensorDefectiveFL` | Tracks malfunctioning sensors in the fleet. | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_sensorDefectiveFR` | Tracks malfunctioning sensors in the fleet. | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_sensorDefectiveRL` | Tracks malfunctioning sensors in the fleet. | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_sensorDefectiveRR` | Tracks malfunctioning sensors in the fleet. | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_ecuUnderVoltage` | Tire pressure monitoring: ecu under voltage | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_ecuOverVoltage` | Tire pressure monitoring: ecu over voltage | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_ecuRamRomNvMFail` | Tire pressure monitoring: ecu ram rom nv m fail | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_rfReceiverFail` | Tire pressure monitoring: rf receiver fail | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_wheelPulseMissing` | Tire pressure monitoring: wheel pulse missing | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_vehicleSpeedFail` | Tire pressure monitoring: vehicle speed fail | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_externalTemperatureFail` | Tire pressure monitoring: external temperature fail | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_eolNotCompleted` | Monitors sensor completion of End of Line (EOL) routine. | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `TPMS_rcpFront` | Front tire recommended cold pressure | 48\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.375 |  | validated |
| `TPMS_rcpRear` | Rear tire recommended cold pressure | 56\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.375 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Tire pressure monitoring messages (TPMS)](../../tpms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
