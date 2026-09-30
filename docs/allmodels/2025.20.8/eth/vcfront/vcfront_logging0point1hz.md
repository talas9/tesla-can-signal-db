---
layout: default
title: "VCFRONT_logging0point1Hz (0x709) — Front body controller, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Front body controller message: logging0point1 hz. Ethernet-side message VCFRONT_logging0point1Hz of Front body controller for Tesla Model 3 / Model Y firmware 2025.20.8, 23 signals (VCFRONT_logging0point1HzIndex, VC_hcmlFactoryOfOrigin, VC_hcmlHellaPartNumberStatus, VC_hcmlHellaPartNumber and 19 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_logging0point1Hz (0x709) — Front body controller, Tesla Model 3 / Model Y 2025.20.8 ETH

Front body controller message: logging0point1 hz. This page documents the 23 signals of VCFRONT_logging0point1Hz as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_logging0point1Hz` |
| Ethernet-side id | 0x709 (1801) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCFRONT |
| Frame length | 8 bytes |
| Cycle time | 322 ms |
| Signals | 23 |

## Signals of VCFRONT_logging0point1Hz

Tesla Model 3 / Model Y CAN bus signals in `VCFRONT_logging0point1Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_logging0point1HzIndex` | selector | Front body controller: logging0point1 hz index | 0\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `LIGHT_CURRENTS`<br>1 = `HCML_LED_TEMPS`<br>2 = `HCMR_LED_TEMPS`<br>3 = `HEADLAMP_CURRENT_POSITION`<br>4 = `HEADLAMP_AIMED_POSITION`<br>5 = `EXV_CHILLER_COUNTERS_1`<br>6 = `EXV_CHILLER_COUNTERS_2`<br>7 = `EXV_EVAPORATOR_COUNTERS_1`<br>8 = `EXV_EVAPORATOR_COUNTERS_2`<br>9 = `EXV_RECIRC_COUNTERS_1`<br>10 = `EXV_RECIRC_COUNTERS_2`<br>11 = `EXV_LCC_COUNTERS_1`<br>12 = `EXV_LCC_COUNTERS_2`<br>13 = `EXV_CCL_COUNTERS_1`<br>14 = `EXV_CCL_COUNTERS_2`<br>15 = `EXV_CCR_COUNTERS_1`<br>16 = `EXV_CCR_COUNTERS_2`<br>17 = `EXV_TOTAL_DISTANCE_COUNTERS_1`<br>18 = `EXV_TOTAL_DISTANCE_COUNTERS_2`<br>19 = `EXV_TOTAL_DISTANCE_COUNTERS_3`<br>20 = `HEADLAMP_MIGRATION`<br>21 = `HEADLAMP_COMM_FAULT_COUNTERS`<br>22 = `LIGHT_DEBUG`<br>23 = `PART_FAILURE_CONFIDENCE`<br>24 = `PART_FAILURE_CONFIDENCE_CONTINUED`<br>25 = `EXV_VALVE_TYPES`<br>26 = `HEADLAMP_LEFT_EEPROM_INFO`<br>27 = `HEADLAMP_RIGHT_EEPROM_INFO`<br>28 = `COMPRESSOR_WEAR_COUNTERS`<br>29 = `HEADLAMP_RIGHT_ECULESS_IO_DIAGNOSTIC`<br>30 = `HEADLAMP_LEFT_ECULESS_IO_DIAGNOSTIC`<br>31 = `END` | plausible |
| `VC_hcmlFactoryOfOrigin` | page 26 | Tier 1 supplier (Hella) factory of origin of the left headlamp | 5\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `HELLA_CHINA`<br>2 = `HELLA_SLOVAKIA`<br>3 = `HELLA_MEXICO` | plausible |
| `VC_hcmlHellaPartNumberStatus` | page 26 | Front body controller: hcml hella part number status | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VC_hcmlHellaPartNumber` | page 26 | Value of the Hella Part Number written into EEPROM in the left headlamp | 8\|32 | little-endian | unsigned | 1 | 0 | - | 0 to 4294967295 |  | plausible |
| `VC_hcmlCurrentBinMappingType` | page 26 | Front body controller: hcml current bin mapping type | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `BIN_MAP_TYPE_UNKNOWN`<br>1 = `BIN_MAP_TYPE_1`<br>2 = `BIN_MAP_TYPE_2` | plausible |
| `VC_hcmlCurrentBin0Value` | page 26 | Front body controller: hcml current bin0 value; raw 0 = signal not available (SNA) | 42\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `LIGHTCLASS_SNA`<br>1 = `LIGHTCLASS_1`<br>2 = `LIGHTCLASS_2`<br>3 = `LIGHTCLASS_3`<br>4 = `LIGHTCLASS_4`<br>7 = `INVALID_LIGHTCLASS` | plausible |
| `VC_hcmlCurrentBin1Value` | page 26 | Front body controller: hcml current bin1 value; raw 0 = signal not available (SNA) | 45\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `LIGHTCLASS_SNA`<br>1 = `LIGHTCLASS_1`<br>2 = `LIGHTCLASS_2`<br>3 = `LIGHTCLASS_3`<br>4 = `LIGHTCLASS_4`<br>7 = `INVALID_LIGHTCLASS` | plausible |
| `VC_hcmlCurrentBin2Value` | page 26 | Front body controller: hcml current bin2 value; raw 0 = signal not available (SNA) | 48\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `LIGHTCLASS_SNA`<br>1 = `LIGHTCLASS_1`<br>2 = `LIGHTCLASS_2`<br>3 = `LIGHTCLASS_3`<br>4 = `LIGHTCLASS_4`<br>7 = `INVALID_LIGHTCLASS` | plausible |
| `VC_hcmlCurrentBin3Value` | page 26 | Front body controller: hcml current bin3 value; raw 0 = signal not available (SNA) | 51\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `LIGHTCLASS_SNA`<br>1 = `LIGHTCLASS_1`<br>2 = `LIGHTCLASS_2`<br>3 = `LIGHTCLASS_3`<br>4 = `LIGHTCLASS_4`<br>7 = `INVALID_LIGHTCLASS` | plausible |
| `VC_hcmlCurrentBin4Value` | page 26 | Front body controller: hcml current bin4 value; raw 0 = signal not available (SNA) | 54\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `LIGHTCLASS_SNA`<br>1 = `LIGHTCLASS_1`<br>2 = `LIGHTCLASS_2`<br>3 = `LIGHTCLASS_3`<br>4 = `LIGHTCLASS_4`<br>7 = `INVALID_LIGHTCLASS` | plausible |
| `VC_hcmlCurrentBin5Value` | page 26 | Front body controller: hcml current bin5 value; raw 0 = signal not available (SNA) | 57\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `LIGHTCLASS_SNA`<br>1 = `LIGHTCLASS_1`<br>2 = `LIGHTCLASS_2`<br>3 = `LIGHTCLASS_3`<br>4 = `LIGHTCLASS_4`<br>7 = `INVALID_LIGHTCLASS` | plausible |
| `VC_hcmlRegionAndSide` | page 26 | Left headlamp EEPROM region and side; raw 0 = signal not available (SNA) | 60\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `HEADLAMP_REGION_AND_SIDE_SNA`<br>1 = `HEADLAMP_REGION_AND_SIDE_SAE_LEFT`<br>2 = `HEADLAMP_REGION_AND_SIDE_SAE_RIGHT`<br>3 = `HEADLAMP_REGION_AND_SIDE_ECE_LHD_LEFT`<br>4 = `HEADLAMP_REGION_AND_SIDE_ECE_LHD_RIGHT`<br>5 = `HEADLAMP_REGION_AND_SIDE_ECE_RHD_LEFT`<br>6 = `HEADLAMP_REGION_AND_SIDE_ECE_RHD_RIGHT` | plausible |
| `VC_hcmrFactoryOfOrigin` | page 27 | Tier 1 supplier (Hella) factory of origin of the right headlamp | 5\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `HELLA_CHINA`<br>2 = `HELLA_SLOVAKIA`<br>3 = `HELLA_MEXICO` | plausible |
| `VC_hcmrHellaPartNumberStatus` | page 27 | Front body controller: hcmr hella part number status | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OK`<br>1 = `FAULT` | plausible |
| `VC_hcmrHellaPartNumber` | page 27 | Value of the Hella Part Number written into EEPROM in the right headlamp | 8\|32 | little-endian | unsigned | 1 | 0 | - | 0 to 4294967295 |  | plausible |
| `VC_hcmrCurrentBinMappingType` | page 27 | Front body controller: hcmr current bin mapping type | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `BIN_MAP_TYPE_UNKNOWN`<br>1 = `BIN_MAP_TYPE_1`<br>2 = `BIN_MAP_TYPE_2` | plausible |
| `VC_hcmrCurrentBin0Value` | page 27 | Front body controller: hcmr current bin0 value; raw 0 = signal not available (SNA) | 42\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `LIGHTCLASS_SNA`<br>1 = `LIGHTCLASS_1`<br>2 = `LIGHTCLASS_2`<br>3 = `LIGHTCLASS_3`<br>4 = `LIGHTCLASS_4`<br>7 = `INVALID_LIGHTCLASS` | plausible |
| `VC_hcmrCurrentBin1Value` | page 27 | Front body controller: hcmr current bin1 value; raw 0 = signal not available (SNA) | 45\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `LIGHTCLASS_SNA`<br>1 = `LIGHTCLASS_1`<br>2 = `LIGHTCLASS_2`<br>3 = `LIGHTCLASS_3`<br>4 = `LIGHTCLASS_4`<br>7 = `INVALID_LIGHTCLASS` | plausible |
| `VC_hcmrCurrentBin2Value` | page 27 | Front body controller: hcmr current bin2 value; raw 0 = signal not available (SNA) | 48\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `LIGHTCLASS_SNA`<br>1 = `LIGHTCLASS_1`<br>2 = `LIGHTCLASS_2`<br>3 = `LIGHTCLASS_3`<br>4 = `LIGHTCLASS_4`<br>7 = `INVALID_LIGHTCLASS` | plausible |
| `VC_hcmrCurrentBin3Value` | page 27 | Front body controller: hcmr current bin3 value; raw 0 = signal not available (SNA) | 51\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `LIGHTCLASS_SNA`<br>1 = `LIGHTCLASS_1`<br>2 = `LIGHTCLASS_2`<br>3 = `LIGHTCLASS_3`<br>4 = `LIGHTCLASS_4`<br>7 = `INVALID_LIGHTCLASS` | plausible |
| `VC_hcmrCurrentBin4Value` | page 27 | Front body controller: hcmr current bin4 value; raw 0 = signal not available (SNA) | 54\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `LIGHTCLASS_SNA`<br>1 = `LIGHTCLASS_1`<br>2 = `LIGHTCLASS_2`<br>3 = `LIGHTCLASS_3`<br>4 = `LIGHTCLASS_4`<br>7 = `INVALID_LIGHTCLASS` | plausible |
| `VC_hcmrCurrentBin5Value` | page 27 | Front body controller: hcmr current bin5 value; raw 0 = signal not available (SNA) | 57\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `LIGHTCLASS_SNA`<br>1 = `LIGHTCLASS_1`<br>2 = `LIGHTCLASS_2`<br>3 = `LIGHTCLASS_3`<br>4 = `LIGHTCLASS_4`<br>7 = `INVALID_LIGHTCLASS` | plausible |
| `VC_hcmrRegionAndSide` | page 27 | Right headlamp EEPROM region and side; raw 0 = signal not available (SNA) | 60\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `HEADLAMP_REGION_AND_SIDE_SNA`<br>1 = `HEADLAMP_REGION_AND_SIDE_SAE_LEFT`<br>2 = `HEADLAMP_REGION_AND_SIDE_SAE_RIGHT`<br>3 = `HEADLAMP_REGION_AND_SIDE_ECE_LHD_LEFT`<br>4 = `HEADLAMP_REGION_AND_SIDE_ECE_LHD_RIGHT`<br>5 = `HEADLAMP_REGION_AND_SIDE_ECE_RHD_LEFT`<br>6 = `HEADLAMP_REGION_AND_SIDE_ECE_RHD_RIGHT` | plausible |

## Multiplexing

`VCFRONT_logging0point1HzIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 26 (11 signals), page 27 (11 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
