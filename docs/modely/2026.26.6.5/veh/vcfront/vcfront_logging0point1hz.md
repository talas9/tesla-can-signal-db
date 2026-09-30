---
layout: default
title: "VCFRONT_logging0point1Hz (0x709) — Front body controller, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Front body controller message: logging0point1 hz. Tesla Model Y CAN bus message VCFRONT_logging0point1Hz (0x709) of Front body controller, firmware 2026.26.6.5, 33 signals (VCFRONT_logging0point1HzIndex, VC_leftHeadlampCurrentVerticalPosition, VC_leftHeadlampCurrentHorizontalPosition, VC_rightHeadlampCurrentVerticalPosition and 29 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_logging0point1Hz (0x709) — Front body controller, Tesla Model Y 2026.26.6.5 VEH CAN

Front body controller message: logging0point1 hz; frame length observed on a vehicle bus. This page documents the 33 signals of VCFRONT_logging0point1Hz as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_logging0point1Hz` |
| CAN id | 0x709 (1801) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT |
| Frame length | 8 bytes |
| Cycle time | 294 ms |
| Signals | 33 |

## Signals of VCFRONT_logging0point1Hz

Tesla Model Y CAN bus signals in `VCFRONT_logging0point1Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_logging0point1HzIndex` | selector | Front body controller: logging0point1 hz index | 0\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `LIGHT_CURRENTS`<br>1 = `HCML_LED_TEMPS`<br>2 = `HCMR_LED_TEMPS`<br>3 = `HEADLAMP_CURRENT_POSITION`<br>4 = `HEADLAMP_AIMED_POSITION`<br>5 = `EXV_CHILLER_COUNTERS_1`<br>6 = `EXV_CHILLER_COUNTERS_2`<br>7 = `EXV_EVAPORATOR_COUNTERS_1`<br>8 = `EXV_EVAPORATOR_COUNTERS_2`<br>9 = `EXV_RECIRC_COUNTERS_1`<br>10 = `EXV_RECIRC_COUNTERS_2`<br>11 = `EXV_LCC_COUNTERS_1`<br>12 = `EXV_LCC_COUNTERS_2`<br>13 = `EXV_CCL_COUNTERS_1`<br>14 = `EXV_CCL_COUNTERS_2`<br>15 = `EXV_CCR_COUNTERS_1`<br>16 = `EXV_CCR_COUNTERS_2`<br>17 = `EXV_TOTAL_DISTANCE_COUNTERS_1`<br>18 = `EXV_TOTAL_DISTANCE_COUNTERS_2`<br>19 = `EXV_TOTAL_DISTANCE_COUNTERS_3`<br>20 = `HEADLAMP_MIGRATION`<br>21 = `HEADLAMP_COMM_FAULT_COUNTERS`<br>22 = `LIGHT_DEBUG`<br>23 = `PART_FAILURE_CONFIDENCE`<br>24 = `PART_FAILURE_CONFIDENCE_CONTINUED`<br>25 = `EXV_VALVE_TYPES`<br>26 = `HEADLAMP_LEFT_EEPROM_INFO`<br>27 = `HEADLAMP_RIGHT_EEPROM_INFO`<br>28 = `COMPRESSOR_WEAR_COUNTERS`<br>29 = `HEADLAMP_RIGHT_ECULESS_IO_DIAGNOSTIC`<br>30 = `HEADLAMP_LEFT_ECULESS_IO_DIAGNOSTIC`<br>31 = `HEADLAMP_RIGHT_ECULESS_IO_DIAGNOSTIC_2`<br>32 = `HEADLAMP_LEFT_ECULESS_IO_DIAGNOSTIC_2`<br>33 = `HEADLAMP_OFFSETS_AND_STATUS`<br>34 = `DYNAMIC_LEVELING_CONTRIBUTORS`<br>35 = `END` | plausible |
| `VC_leftHeadlampCurrentVerticalPosition` | page 3 | Front body controller: left headlamp current vertical position | 6\|10 | little-endian | unsigned | 1 | 0 | Steps | 0 to 1022 | 1022 = `INVALID_POSITION`<br>1023 = `SNA` | plausible |
| `VC_leftHeadlampCurrentHorizontalPosition` | page 3 | Front body controller: left headlamp current horizontal position | 16\|10 | little-endian | unsigned | 1 | 0 | Steps | 0 to 1022 | 1022 = `INVALID_POSITION`<br>1023 = `SNA` | plausible |
| `VC_rightHeadlampCurrentVerticalPosition` | page 3 | Front body controller: right headlamp current vertical position | 26\|10 | little-endian | unsigned | 1 | 0 | Steps | 0 to 1022 | 1022 = `INVALID_POSITION`<br>1023 = `SNA` | plausible |
| `VC_rightHeadlampCurrentHorizontalPosition` | page 3 | Front body controller: right headlamp current horizontal position | 36\|10 | little-endian | unsigned | 1 | 0 | Steps | 0 to 1022 | 1022 = `INVALID_POSITION`<br>1023 = `SNA` | plausible |
| `VC_leftHeadlampAimingState` | page 3 | Front body controller: left headlamp aiming state | 51\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HEADLAMP_AIMING_STATE_IDLE`<br>1 = `HEADLAMP_AIMING_STATE_CALIBRATING`<br>2 = `HEADLAMP_AIMING_STATE_AIMING`<br>3 = `HEADLAMP_AIMING_STATE_POST_AIMING_CALIBRATION`<br>7 = `HEADLAMP_AIMING_STATE_RESERVED` | plausible |
| `VC_rightHeadlampAimingState` | page 3 | Front body controller: right headlamp aiming state | 56\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `HEADLAMP_AIMING_STATE_IDLE`<br>1 = `HEADLAMP_AIMING_STATE_CALIBRATING`<br>2 = `HEADLAMP_AIMING_STATE_AIMING`<br>3 = `HEADLAMP_AIMING_STATE_POST_AIMING_CALIBRATION`<br>7 = `HEADLAMP_AIMING_STATE_RESERVED` | plausible |
| `VC_leftHeadlampAimedVerticalPosition` | page 4 | Front body controller: left headlamp aimed vertical position | 6\|10 | little-endian | unsigned | 1 | 0 | Steps | 0 to 1022 | 1022 = `INVALID_POSITION`<br>1023 = `SNA` | plausible |
| `VC_rightHeadlampAimedVerticalPosition` | page 4 | Front body controller: right headlamp aimed vertical position | 16\|10 | little-endian | unsigned | 1 | 0 | Steps | 0 to 1022 | 1022 = `INVALID_POSITION`<br>1023 = `SNA` | plausible |
| `VC_leftHeadlampAimedHorizontalPosition` | page 4 | Front body controller: left headlamp aimed horizontal position | 26\|10 | little-endian | unsigned | 1 | 0 | Steps | 0 to 1022 | 1022 = `INVALID_POSITION`<br>1023 = `SNA` | plausible |
| `VC_rightHeadlampAimedHorizontalPosition` | page 4 | Front body controller: right headlamp aimed horizontal position | 36\|10 | little-endian | unsigned | 1 | 0 | Steps | 0 to 1022 | 1022 = `INVALID_POSITION`<br>1023 = `SNA` | plausible |
| `VC_hcmlFactoryOfOrigin` | page 26 | Tier 1 supplier (Hella) factory of origin of the left headlamp | 6\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `HELLA_CHINA`<br>2 = `HELLA_SLOVAKIA`<br>3 = `HELLA_MEXICO` | validated |
| `VC_hcmlHellaPartNumberStatus` | page 26 | Front body controller: hcml hella part number status | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | validated |
| `VC_hcmlHellaPartNumber` | page 26 | Value of the Hella Part Number written into EEPROM in the left headlamp | 9\|32 | little-endian | unsigned | 1 | 0 | - | 0 to 4294967295 |  | validated |
| `VC_hcmlCurrentBinMappingType` | page 26 | Front body controller: hcml current bin mapping type | 41\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `BIN_MAP_TYPE_UNKNOWN`<br>1 = `BIN_MAP_TYPE_1`<br>2 = `BIN_MAP_TYPE_2` | validated |
| `VC_hcmlCurrentBin0Value` | page 26 | Front body controller: hcml current bin0 value; raw 0 = signal not available (SNA) | 43\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `LIGHTCLASS_SNA`<br>1 = `LIGHTCLASS_1`<br>2 = `LIGHTCLASS_2`<br>3 = `LIGHTCLASS_3`<br>4 = `LIGHTCLASS_4`<br>7 = `INVALID_LIGHTCLASS` | validated |
| `VC_hcmlCurrentBin1Value` | page 26 | Front body controller: hcml current bin1 value; raw 0 = signal not available (SNA) | 46\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `LIGHTCLASS_SNA`<br>1 = `LIGHTCLASS_1`<br>2 = `LIGHTCLASS_2`<br>3 = `LIGHTCLASS_3`<br>4 = `LIGHTCLASS_4`<br>7 = `INVALID_LIGHTCLASS` | validated |
| `VC_hcmlCurrentBin2Value` | page 26 | Front body controller: hcml current bin2 value; raw 0 = signal not available (SNA) | 49\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `LIGHTCLASS_SNA`<br>1 = `LIGHTCLASS_1`<br>2 = `LIGHTCLASS_2`<br>3 = `LIGHTCLASS_3`<br>4 = `LIGHTCLASS_4`<br>7 = `INVALID_LIGHTCLASS` | validated |
| `VC_hcmlCurrentBin3Value` | page 26 | Front body controller: hcml current bin3 value; raw 0 = signal not available (SNA) | 52\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `LIGHTCLASS_SNA`<br>1 = `LIGHTCLASS_1`<br>2 = `LIGHTCLASS_2`<br>3 = `LIGHTCLASS_3`<br>4 = `LIGHTCLASS_4`<br>7 = `INVALID_LIGHTCLASS` | validated |
| `VC_hcmlCurrentBin4Value` | page 26 | Front body controller: hcml current bin4 value; raw 0 = signal not available (SNA) | 55\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `LIGHTCLASS_SNA`<br>1 = `LIGHTCLASS_1`<br>2 = `LIGHTCLASS_2`<br>3 = `LIGHTCLASS_3`<br>4 = `LIGHTCLASS_4`<br>7 = `INVALID_LIGHTCLASS` | validated |
| `VC_hcmlCurrentBin5Value` | page 26 | Front body controller: hcml current bin5 value; raw 0 = signal not available (SNA) | 58\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `LIGHTCLASS_SNA`<br>1 = `LIGHTCLASS_1`<br>2 = `LIGHTCLASS_2`<br>3 = `LIGHTCLASS_3`<br>4 = `LIGHTCLASS_4`<br>7 = `INVALID_LIGHTCLASS` | validated |
| `VC_hcmlRegionAndSide` | page 26 | Left headlamp EEPROM region and side; raw 0 = signal not available (SNA) | 61\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `HEADLAMP_REGION_AND_SIDE_SNA`<br>1 = `HEADLAMP_REGION_AND_SIDE_SAE_LEFT`<br>2 = `HEADLAMP_REGION_AND_SIDE_SAE_RIGHT`<br>3 = `HEADLAMP_REGION_AND_SIDE_ECE_LHD_LEFT`<br>4 = `HEADLAMP_REGION_AND_SIDE_ECE_LHD_RIGHT`<br>5 = `HEADLAMP_REGION_AND_SIDE_ECE_RHD_LEFT`<br>6 = `HEADLAMP_REGION_AND_SIDE_ECE_RHD_RIGHT` | validated |
| `VC_hcmrFactoryOfOrigin` | page 27 | Tier 1 supplier (Hella) factory of origin of the right headlamp | 6\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `HELLA_CHINA`<br>2 = `HELLA_SLOVAKIA`<br>3 = `HELLA_MEXICO` | validated |
| `VC_hcmrHellaPartNumberStatus` | page 27 | Front body controller: hcmr hella part number status | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | validated |
| `VC_hcmrHellaPartNumber` | page 27 | Value of the Hella Part Number written into EEPROM in the right headlamp | 9\|32 | little-endian | unsigned | 1 | 0 | - | 0 to 4294967295 |  | validated |
| `VC_hcmrCurrentBinMappingType` | page 27 | Front body controller: hcmr current bin mapping type | 41\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `BIN_MAP_TYPE_UNKNOWN`<br>1 = `BIN_MAP_TYPE_1`<br>2 = `BIN_MAP_TYPE_2` | validated |
| `VC_hcmrCurrentBin0Value` | page 27 | Front body controller: hcmr current bin0 value; raw 0 = signal not available (SNA) | 43\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `LIGHTCLASS_SNA`<br>1 = `LIGHTCLASS_1`<br>2 = `LIGHTCLASS_2`<br>3 = `LIGHTCLASS_3`<br>4 = `LIGHTCLASS_4`<br>7 = `INVALID_LIGHTCLASS` | validated |
| `VC_hcmrCurrentBin1Value` | page 27 | Front body controller: hcmr current bin1 value; raw 0 = signal not available (SNA) | 46\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `LIGHTCLASS_SNA`<br>1 = `LIGHTCLASS_1`<br>2 = `LIGHTCLASS_2`<br>3 = `LIGHTCLASS_3`<br>4 = `LIGHTCLASS_4`<br>7 = `INVALID_LIGHTCLASS` | validated |
| `VC_hcmrCurrentBin2Value` | page 27 | Front body controller: hcmr current bin2 value; raw 0 = signal not available (SNA) | 49\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `LIGHTCLASS_SNA`<br>1 = `LIGHTCLASS_1`<br>2 = `LIGHTCLASS_2`<br>3 = `LIGHTCLASS_3`<br>4 = `LIGHTCLASS_4`<br>7 = `INVALID_LIGHTCLASS` | validated |
| `VC_hcmrCurrentBin3Value` | page 27 | Front body controller: hcmr current bin3 value; raw 0 = signal not available (SNA) | 52\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `LIGHTCLASS_SNA`<br>1 = `LIGHTCLASS_1`<br>2 = `LIGHTCLASS_2`<br>3 = `LIGHTCLASS_3`<br>4 = `LIGHTCLASS_4`<br>7 = `INVALID_LIGHTCLASS` | validated |
| `VC_hcmrCurrentBin4Value` | page 27 | Front body controller: hcmr current bin4 value; raw 0 = signal not available (SNA) | 55\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `LIGHTCLASS_SNA`<br>1 = `LIGHTCLASS_1`<br>2 = `LIGHTCLASS_2`<br>3 = `LIGHTCLASS_3`<br>4 = `LIGHTCLASS_4`<br>7 = `INVALID_LIGHTCLASS` | validated |
| `VC_hcmrCurrentBin5Value` | page 27 | Front body controller: hcmr current bin5 value; raw 0 = signal not available (SNA) | 58\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `LIGHTCLASS_SNA`<br>1 = `LIGHTCLASS_1`<br>2 = `LIGHTCLASS_2`<br>3 = `LIGHTCLASS_3`<br>4 = `LIGHTCLASS_4`<br>7 = `INVALID_LIGHTCLASS` | validated |
| `VC_hcmrRegionAndSide` | page 27 | Right headlamp EEPROM region and side; raw 0 = signal not available (SNA) | 61\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `HEADLAMP_REGION_AND_SIDE_SNA`<br>1 = `HEADLAMP_REGION_AND_SIDE_SAE_LEFT`<br>2 = `HEADLAMP_REGION_AND_SIDE_SAE_RIGHT`<br>3 = `HEADLAMP_REGION_AND_SIDE_ECE_LHD_LEFT`<br>4 = `HEADLAMP_REGION_AND_SIDE_ECE_LHD_RIGHT`<br>5 = `HEADLAMP_REGION_AND_SIDE_ECE_RHD_LEFT`<br>6 = `HEADLAMP_REGION_AND_SIDE_ECE_RHD_RIGHT` | validated |

## Multiplexing

`VCFRONT_logging0point1HzIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 3 (6 signals), page 4 (4 signals), page 26 (11 signals), page 27 (11 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
