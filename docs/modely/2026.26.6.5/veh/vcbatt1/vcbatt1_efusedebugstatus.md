---
layout: default
title: "VCBATT1_eFuseDebugStatus (0x406) — VCBATT1 ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "VCBATT1 ECU message: e fuse debug status. Tesla Model Y CAN bus message VCBATT1_eFuseDebugStatus (0x406) of VCBATT1 ECU, firmware 2026.26.6.5, 37 signals (VCBATT1_eFuseDebugStatusIndex, VCBATT1_leftControllerEFuseState, VCBATT1_leftControllerEFuseCurrent, VCBATT1_leftControllerEFuseOutput and 33 more). Bit layout, scaling, units and value tables."
---

# VCBATT1_eFuseDebugStatus (0x406) — VCBATT1 ECU, Tesla Model Y 2026.26.6.5 VEH CAN

VCBATT1 ECU message: e fuse debug status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 37 signals of VCBATT1_eFuseDebugStatus as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCBATT1_eFuseDebugStatus` |
| CAN id | 0x406 (1030) |
| ECU | [VCBATT1 ECU](../../vcbatt1.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCBATT1 |
| Frame length | 7 bytes |
| Cycle time | 200 ms |
| Signals | 37 |

## Signals of VCBATT1_eFuseDebugStatus

Tesla Model Y CAN bus signals in `VCBATT1_eFuseDebugStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCBATT1_eFuseDebugStatusIndex` | selector | VCBATT1 ECU: e fuse debug status index | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VCLEFT`<br>1 = `EPAS1`<br>2 = `BAT_BRIDGE`<br>3 = `AUTOPILOT_1`<br>4 = `LOADSHED`<br>5 = `BRAKE_MOTOR_ECU_1`<br>6 = `MCU_LOGIC`<br>7 = `SLEEP_BYPASS` | plausible |
| `VCBATT1_leftControllerEFuseState` | page 0 | VCBATT1 ECU: left controller e fuse state | 3\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STANDBY`<br>1 = `WAKEUP`<br>2 = `CONFIGURATION`<br>3 = `UNLOCKED`<br>4 = `LOCKED`<br>5 = `FAILSAFE`<br>6 = `SELF_TEST_PREP`<br>7 = `SELF_TEST` | validated |
| `VCBATT1_leftControllerEFuseCurrent` | page 0 | VCBATT1 ECU: left controller e fuse current | 8\|12 | little-endian | unsigned | 0.05 | 0 | A | 0 to 204.75 |  | validated |
| `VCBATT1_leftControllerEFuseOutput` | page 0 | VCBATT1 ECU: left controller e fuse output | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_leftControllerEFuseOutputDesired` | page 0 | VCBATT1 ECU: left controller e fuse output desired | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_leftControllerEFuseBypass` | page 0 | VCBATT1 ECU: left controller e fuse bypass | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_leftControllerEFuseBypassDesired` | page 0 | VCBATT1 ECU: left controller e fuse bypass desired | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_leftControllerEFuseVoltage` | page 0 | VCBATT1 ECU: left controller e fuse voltage | 24\|8 | little-endian | unsigned | 0.07 | 0 | V | 0 to 17.85 |  | validated |
| `VCBATT1_leftControllerEFuseTemperature` | page 0 | VCBATT1 ECU: left controller e fuse temperature | 32\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 150 |  | validated |
| `VCBATT1_leftControllerEFuseManagerState` | page 0 | VCBATT1 ECU: left controller e fuse manager state | 40\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `RESETTING`<br>1 = `OFF`<br>2 = `WAKEUP`<br>3 = `STANDBY`<br>4 = `LOCKING`<br>5 = `LOCKED_ON_BOOT`<br>6 = `UNLOCKING`<br>7 = `IDLE`<br>8 = `LOCKOUT` | validated |
| `VCBATT1_leftControllerEFuseHardShortThreshold` | page 0 | VCBATT1 ECU: left controller e fuse hard short threshold | 44\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `20_MV`<br>1 = `23_MV`<br>2 = `26_4_MV`<br>3 = `30_3_MV`<br>4 = `34_8_MV`<br>5 = `40_MV`<br>6 = `45_9_MV`<br>7 = `52_8_MV`<br>8 = `60_6_MV`<br>9 = `69_6_MV`<br>10 = `80_MV`<br>11 = `91_9_MV`<br>12 = `105_6_MV`<br>13 = `121_3_MV`<br>14 = `139_3_MV`<br>15 = `160_MV` | validated |
| `VCBATT1_leftControllerEFuseOCThreshold` | page 0 | VCBATT1 ECU: left controller e fuse OC threshold | 48\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `6_MV`<br>1 = `7_2_MV`<br>2 = `8_7_MV`<br>3 = `10_4_MV`<br>4 = `11_8_MV`<br>5 = `13_MV`<br>6 = `13_8_MV`<br>7 = `14_8_MV`<br>8 = `15_8_MV`<br>9 = `16_8_MV`<br>10 = `17_9_MV`<br>11 = `19_1_MV`<br>12 = `20_4_MV`<br>13 = `21_8_MV`<br>14 = `23_3_MV`<br>15 = `24_8_MV`<br>16 = `26_5_MV`<br>17 = `28_2_MV`<br>18 = `30_1_MV`<br>19 = `32_2_MV`<br>20 = `34_3_MV`<br>21 = `36_6_MV`<br>22 = `39_1_MV`<br>23 = `41_7_MV`<br>24 = `44_5_MV`<br>25 = `47_5_MV`<br>26 = `50_6_MV`<br>27 = `54_MV`<br>28 = `61_3_MV`<br>29 = `69_5_MV`<br>30 = `78_8_MV`<br>31 = `89_3_MV` | validated |
| `VCBATT1_leftControllerEFuseType` | page 0 | Reports the type of the left controller eFuse. | 53\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `VNF1048`<br>2 = `VNF1248` | validated |
| `VCBATT1_EPAS1EFuseState` | page 1 | VCBATT1 ECU: EPAS1 e fuse state | 3\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STANDBY`<br>1 = `WAKEUP`<br>2 = `CONFIGURATION`<br>3 = `UNLOCKED`<br>4 = `LOCKED`<br>5 = `FAILSAFE`<br>6 = `SELF_TEST_PREP`<br>7 = `SELF_TEST` | validated |
| `VCBATT1_EPAS1EFuseCurrent` | page 1 | VCBATT1 ECU: EPAS1 e fuse current | 8\|12 | little-endian | unsigned | 0.05 | 0 | A | 0 to 204.75 |  | validated |
| `VCBATT1_EPAS1EFuseOutput` | page 1 | VCBATT1 ECU: EPAS1 e fuse output | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_EPAS1EFuseOutputDesired` | page 1 | VCBATT1 ECU: EPAS1 e fuse output desired | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_EPAS1EFuseBypass` | page 1 | VCBATT1 ECU: EPAS1 e fuse bypass | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_EPAS1EFuseBypassDesired` | page 1 | VCBATT1 ECU: EPAS1 e fuse bypass desired | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_EPAS1EFuseVoltage` | page 1 | VCBATT1 ECU: EPAS1 e fuse voltage | 24\|8 | little-endian | unsigned | 0.07 | 0 | V | 0 to 17.85 |  | validated |
| `VCBATT1_EPAS1EFuseTemperature` | page 1 | VCBATT1 ECU: EPAS1 e fuse temperature | 32\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 150 |  | validated |
| `VCBATT1_EPAS1EFuseManagerState` | page 1 | VCBATT1 ECU: EPAS1 e fuse manager state | 40\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `RESETTING`<br>1 = `OFF`<br>2 = `WAKEUP`<br>3 = `STANDBY`<br>4 = `LOCKING`<br>5 = `LOCKED_ON_BOOT`<br>6 = `UNLOCKING`<br>7 = `IDLE`<br>8 = `LOCKOUT` | validated |
| `VCBATT1_EPAS1EFuseHardShortThreshold` | page 1 | VCBATT1 ECU: EPAS1 e fuse hard short threshold | 44\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `20_MV`<br>1 = `23_MV`<br>2 = `26_4_MV`<br>3 = `30_3_MV`<br>4 = `34_8_MV`<br>5 = `40_MV`<br>6 = `45_9_MV`<br>7 = `52_8_MV`<br>8 = `60_6_MV`<br>9 = `69_6_MV`<br>10 = `80_MV`<br>11 = `91_9_MV`<br>12 = `105_6_MV`<br>13 = `121_3_MV`<br>14 = `139_3_MV`<br>15 = `160_MV` | validated |
| `VCBATT1_EPAS1EFuseOCThreshold` | page 1 | VCBATT1 ECU: EPAS1 e fuse OC threshold | 48\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `6_MV`<br>1 = `7_2_MV`<br>2 = `8_7_MV`<br>3 = `10_4_MV`<br>4 = `11_8_MV`<br>5 = `13_MV`<br>6 = `13_8_MV`<br>7 = `14_8_MV`<br>8 = `15_8_MV`<br>9 = `16_8_MV`<br>10 = `17_9_MV`<br>11 = `19_1_MV`<br>12 = `20_4_MV`<br>13 = `21_8_MV`<br>14 = `23_3_MV`<br>15 = `24_8_MV`<br>16 = `26_5_MV`<br>17 = `28_2_MV`<br>18 = `30_1_MV`<br>19 = `32_2_MV`<br>20 = `34_3_MV`<br>21 = `36_6_MV`<br>22 = `39_1_MV`<br>23 = `41_7_MV`<br>24 = `44_5_MV`<br>25 = `47_5_MV`<br>26 = `50_6_MV`<br>27 = `54_MV`<br>28 = `61_3_MV`<br>29 = `69_5_MV`<br>30 = `78_8_MV`<br>31 = `89_3_MV` | validated |
| `VCBATT1_EPAS1EFuseType` | page 1 | Reports the type of the EPAS1 eFuse. | 53\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `VNF1048`<br>2 = `VNF1248` | validated |
| `VCBATT1_autopilot1EFuseState` | page 3 | VCBATT1 ECU: autopilot1 e fuse state | 3\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STANDBY`<br>1 = `WAKEUP`<br>2 = `CONFIGURATION`<br>3 = `UNLOCKED`<br>4 = `LOCKED`<br>5 = `FAILSAFE`<br>6 = `SELF_TEST_PREP`<br>7 = `SELF_TEST` | validated |
| `VCBATT1_autopilot1EFuseCurrent` | page 3 | VCBATT1 ECU: autopilot1 e fuse current | 8\|12 | little-endian | unsigned | 0.05 | 0 | A | 0 to 204.75 |  | validated |
| `VCBATT1_autopilot1EFuseOutput` | page 3 | VCBATT1 ECU: autopilot1 e fuse output | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_autopilot1EFuseOutputDesired` | page 3 | VCBATT1 ECU: autopilot1 e fuse output desired | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_autopilot1EFuseBypass` | page 3 | VCBATT1 ECU: autopilot1 e fuse bypass | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_autopilot1EFuseBypassDesired` | page 3 | VCBATT1 ECU: autopilot1 e fuse bypass desired | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_autopilot1EFuseVoltage` | page 3 | VCBATT1 ECU: autopilot1 e fuse voltage | 24\|8 | little-endian | unsigned | 0.07 | 0 | V | 0 to 17.85 |  | validated |
| `VCBATT1_autopilot1EFuseTemperature` | page 3 | VCBATT1 ECU: autopilot1 e fuse temperature | 32\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 150 |  | validated |
| `VCBATT1_autopilot1EFuseManagerState` | page 3 | VCBATT1 ECU: autopilot1 e fuse manager state | 40\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `RESETTING`<br>1 = `OFF`<br>2 = `WAKEUP`<br>3 = `STANDBY`<br>4 = `LOCKING`<br>5 = `LOCKED_ON_BOOT`<br>6 = `UNLOCKING`<br>7 = `IDLE`<br>8 = `LOCKOUT` | validated |
| `VCBATT1_autopilot1EFuseHardShortThreshold` | page 3 | VCBATT1 ECU: autopilot1 e fuse hard short threshold | 44\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `20_MV`<br>1 = `23_MV`<br>2 = `26_4_MV`<br>3 = `30_3_MV`<br>4 = `34_8_MV`<br>5 = `40_MV`<br>6 = `45_9_MV`<br>7 = `52_8_MV`<br>8 = `60_6_MV`<br>9 = `69_6_MV`<br>10 = `80_MV`<br>11 = `91_9_MV`<br>12 = `105_6_MV`<br>13 = `121_3_MV`<br>14 = `139_3_MV`<br>15 = `160_MV` | validated |
| `VCBATT1_autopilot1EFuseOCThreshold` | page 3 | VCBATT1 ECU: autopilot1 e fuse OC threshold | 48\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `6_MV`<br>1 = `7_2_MV`<br>2 = `8_7_MV`<br>3 = `10_4_MV`<br>4 = `11_8_MV`<br>5 = `13_MV`<br>6 = `13_8_MV`<br>7 = `14_8_MV`<br>8 = `15_8_MV`<br>9 = `16_8_MV`<br>10 = `17_9_MV`<br>11 = `19_1_MV`<br>12 = `20_4_MV`<br>13 = `21_8_MV`<br>14 = `23_3_MV`<br>15 = `24_8_MV`<br>16 = `26_5_MV`<br>17 = `28_2_MV`<br>18 = `30_1_MV`<br>19 = `32_2_MV`<br>20 = `34_3_MV`<br>21 = `36_6_MV`<br>22 = `39_1_MV`<br>23 = `41_7_MV`<br>24 = `44_5_MV`<br>25 = `47_5_MV`<br>26 = `50_6_MV`<br>27 = `54_MV`<br>28 = `61_3_MV`<br>29 = `69_5_MV`<br>30 = `78_8_MV`<br>31 = `89_3_MV` | validated |
| `VCBATT1_autopilot1EFuseType` | page 3 | Reports the type of the autopilot1 eFuse. | 53\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `VNF1048`<br>2 = `VNF1248` | validated |

## Multiplexing

`VCBATT1_eFuseDebugStatusIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (12 signals), page 1 (12 signals), page 3 (12 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All VCBATT1 ECU messages (VCBATT1)](../../vcbatt1.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
