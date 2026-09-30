---
layout: default
title: "BB_status (0x3AF) — BB ECU, Tesla Model 3 / Model Y 2026.26.6.5 PARTY CAN"
description: "BB ECU message: status. Tesla Model 3 / Model Y CAN bus message BB_status (0x3AF) of BB ECU, firmware 2026.26.6.5, 13 signals (BB_statusChecksum, BB_statusCounter, BB_sOutputRod, BB_sOutputRodQF and 9 more). Bit layout, scaling, units and value tables."
---

# BB_status (0x3AF) — BB ECU, Tesla Model 3 / Model Y 2026.26.6.5 PARTY CAN

BB ECU message: status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 13 signals of BB_status as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BB_status` |
| CAN id | 0x3AF (943) |
| ECU | [BB ECU](../../bb.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | BB |
| Frame length | 7 bytes |
| Cycle time | 10 ms |
| Signals | 13 |

## Signals of BB_status

Tesla Model 3 / Model Y CAN bus signals in `BB_status`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BB_statusChecksum` | BB ECU: status checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `BB_statusCounter` | BB ECU: status counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `BB_sOutputRod` | Reports the measured brake booster (BB) plunger piston position | 12\|12 | little-endian | unsigned | 0.015625 | -5 | mm | -5 to 47 |  | validated |
| `BB_sOutputRodQF` | Reports the BB_sOutputRod signal qualifier | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NotInit_orOff`<br>1 = `Normal`<br>2 = `Faulty` | validated |
| `BB_sInputRod` | Reports the measured brake booster (BB) input rod stroke. | 26\|12 | little-endian | unsigned | 0.015625 | -5 | mm | -5 to 47 |  | validated |
| `BB_sInputRodQF` | Reports the BB_sInputRod signal qualifier. | 38\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NotInit_orOff`<br>1 = `Normal`<br>2 = `Faulty` | validated |
| `BB_driverBrakeApply` | Indicates whether the driver operates the brake pedal. Only active when the driver brakes, not when an external brake command implemented on brake booster (BB). | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `BRAKES_NOT_APPLIED`<br>1 = `DRIVER_APPLYING_BRAKES` | validated |
| `BB_driverBrakeApplyQF` | Qualifier for BB_driverBrakeApply | 41\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NotInit_orOff`<br>1 = `Normal`<br>2 = `Faulty` | validated |
| `BB_boosterStatus` | Indication of the brake booster (BB) functional state | 43\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OFF`<br>1 = `INIT`<br>2 = `FAILURE`<br>3 = `DIAGNOSTIC`<br>4 = `ACTIVE_GOOD_CHECK`<br>5 = `READY`<br>6 = `ACTUATION` | validated |
| `BB_warningLampRequest` | Request from brake booster (BB) to enable the red brake lamp | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NO_LAMP_REQUEST`<br>1 = `YELLOW_BRAKE_LAMP_REQUEST`<br>2 = `RED_BRAKE_LAMP_REQUEST` | validated |
| `BB_brakeFluidLevel` | Indication of the brake fluid reservoir fluid level sensor status measured by the brake booster (BB). | 48\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `BRAKE_FLUID_LEVEL_UNKNOWN`<br>1 = `BRAKE_FLUID_LEVEL_LOW`<br>2 = `BRAKE_FLUID_LEVEL_NORMAL`<br>3 = `BRAKE_FLUID_LEVEL_INVALID` | validated |
| `BB_internalState` | Indication of the brake booster (BB) internal state | 50\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NO_MODE_ACTIVE`<br>1 = `PRE_DRIVE_CHECK`<br>2 = `LOCAL_BRAKE_REQUEST`<br>3 = `EXTERNAL_BRAKE_REQUEST`<br>4 = `DIAGNOSTIC`<br>5 = `TRANSITION_TO_IDLE`<br>6 = `POST_DRIVE_CHECK`<br>7 = `READY_TO_SHUTDOWN` | validated |
| `BB_unfilteredFluidLevelLow` | Indicates whether the unfiltered brake fluid level is detected as low. | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEVEL_NORMAL_OR_UNKNOWN_OR_INVALID`<br>1 = `LEVEL_LOW` | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 PARTY DBC file](../../../../../dbc/AllModels/2026.26.6.5/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/PARTY.json)

## See also

- [All BB ECU messages (BB)](../../bb.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
