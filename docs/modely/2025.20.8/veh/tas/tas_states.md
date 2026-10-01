---
layout: default
title: "TAS_states (0x20D) — Air suspension controller, Tesla Model Y 2025.20.8 VEH CAN"
description: "Air suspension controller message: states. Tesla Model Y CAN bus message TAS_states (0x20D) of Air suspension controller, firmware 2025.20.8, 16 signals (TAS_levelingState, TAS_levelingItem, TAS_pressureGallery, TAS_pressureReservoir and 12 more). Bit layout, scaling, units and value tables."
---

# TAS_states (0x20D) — Air suspension controller, Tesla Model Y 2025.20.8 VEH CAN

Air suspension controller message: states; frame length from the layout, not yet observed on a vehicle bus. This page documents the 16 signals of TAS_states as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `TAS_states` |
| CAN id | 0x20D (525) |
| ECU | [Air suspension controller](../../tas.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | TAS |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 16 |

## Signals of TAS_states

Tesla Model Y CAN bus signals in `TAS_states`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `TAS_levelingState` | Indicates air suspension leveling state. | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `LEVELING_STATE_IDLE`<br>1 = `LEVELING_STATE_READ_P_RESERVOIR`<br>2 = `LEVELING_STATE_MEASURE_SPRING_PRESSURE`<br>3 = `LEVELING_STATE_EXHAUST_GALLERY`<br>4 = `LEVELING_STATE_COMPRESSOR_RAMPUP`<br>5 = `LEVELING_STATE_COMPRESSOR_PREFILL_GALLERY`<br>6 = `LEVELING_STATE_FILL_RESERVOIR_FROM_COMPRESSOR`<br>7 = `LEVELING_STATE_FILL_SPRING_FROM_COMPRESSOR`<br>8 = `LEVELING_STATE_FILL_SPRING_FROM_BOOST`<br>9 = `LEVELING_STATE_FILL_SPRING_FROM_RESERVOIR`<br>10 = `LEVELING_STATE_FILL_SPRING_RESERVOIR_FROM_COMPRESSOR`<br>11 = `LEVELING_STATE_LOWER_SPRING`<br>12 = `LEVELING_STATE_LOWER_SPRING_WITH_COMPRESSOR`<br>13 = `LEVELING_STATE_EXHAUST_RESERVOIR`<br>14 = `LEVELING_STATE_QUIET_EXHAUST`<br>15 = `LEVELING_STATE_CROSSLINK` | plausible |
| `TAS_levelingItem` | Indicates the currently active air suspension components. | 4\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `TAS_LEVELING_ITEM_NONE`<br>1 = `TAS_LEVELING_ITEM_FL`<br>2 = `TAS_LEVELING_ITEM_FR`<br>3 = `TAS_LEVELING_ITEM_RL`<br>4 = `TAS_LEVELING_ITEM_RR`<br>5 = `TAS_LEVELING_ITEM_FRONT_AXLE`<br>6 = `TAS_LEVELING_ITEM_REAR_AXLE`<br>7 = `TAS_LEVELING_ITEM_ALL` | plausible |
| `TAS_pressureGallery` | Current air suspension valve block gallery pressure; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.1 | 0 | bara | 0 to 25.4 | 255 = `SNA` | plausible |
| `TAS_pressureReservoir` | Indicates the latest valid reservoir pressure; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.1 | 0 | bara | 0 to 25.4 | 255 = `SNA` | plausible |
| `TAS_runMode` | Indicates the status of run mode. | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `RUN_MODE_INIT`<br>1 = `RUN_MODE_SYSTEM_CHECK`<br>2 = `RUN_MODE_SERVICE`<br>3 = `RUN_MODE_ASSEMBLY`<br>4 = `RUN_MODE_DAN`<br>5 = `RUN_MODE_NORMAL`<br>6 = `RUN_MODE_LOW_POWER`<br>7 = `RUN_MODE_DYNO` | plausible |
| `TAS_filterMode` | Indicates the status of filter mode. | 27\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `MODE_NONE`<br>1 = `MODE_INIT`<br>2 = `MODE_CALIBRATE`<br>3 = `MODE_TEST`<br>4 = `MODE_READY`<br>5 = `MODE_LOADING`<br>6 = `MODE_DRIVE`<br>7 = `MODE_STOPPING` | plausible |
| `TAS_compressorRun` | Either an indication that the compressor is running or a request to run the air compressor | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `TAS_twistDetected` | TAS has detected large amount of twist. | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `TAS_leanDetected` | TAS has detected vehicle to be leaning left or right. | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `TAS_limpHomeMode` | Indicates which limp home mode is active. | 33\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `LIMP_HOME_MODE_0`<br>1 = `LIMP_HOME_MODE_10`<br>2 = `LIMP_HOME_MODE_20`<br>3 = `LIMP_HOME_MODE_30`<br>4 = `LIMP_HOME_MODE_40` | plausible |
| `TAS_targetLevel` | Indicates target ride height. | 36\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `TAS_VERY_HIGH`<br>1 = `TAS_HIGH`<br>2 = `TAS_STANDARD`<br>3 = `TAS_LOW`<br>4 = `TAS_VERY_LOW` | plausible |
| `TAS_currentLevel` | Indicates current ride height. | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `TAS_VERY_HIGH`<br>1 = `TAS_HIGH`<br>2 = `TAS_STANDARD`<br>3 = `TAS_LOW`<br>4 = `TAS_VERY_LOW` | plausible |
| `TAS_jackMode` | Indicates the status of Jack mode. | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `TAS_reduceVehicleSpeedRequest` | Air suspension controller: reduce vehicle speed request | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_statesCounter` | Air suspension controller: states counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `TAS_statesChecksum` | Air suspension controller: states checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All Air suspension controller messages (TAS)](../../tas.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
