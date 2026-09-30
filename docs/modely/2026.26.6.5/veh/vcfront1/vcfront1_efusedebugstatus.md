---
layout: default
title: "VCFRONT1_eFuseDebugStatus (0x403) — VCFRONT1 ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "VCFRONT1 ECU message: e fuse debug status. Tesla Model Y CAN bus message VCFRONT1_eFuseDebugStatus (0x403) of VCFRONT1 ECU, firmware 2026.26.6.5, 37 signals (VCFRONT1_eFuseDebugStatusIndex, VCFRONT1_EPAS2EFuseState, VCFRONT1_EPAS2EFuseCurrent, VCFRONT1_EPAS2EFuseOutput and 33 more). Bit layout, scaling, units and value tables."
---

# VCFRONT1_eFuseDebugStatus (0x403) — VCFRONT1 ECU, Tesla Model Y 2026.26.6.5 VEH CAN

VCFRONT1 ECU message: e fuse debug status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 37 signals of VCFRONT1_eFuseDebugStatus as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT1_eFuseDebugStatus` |
| CAN id | 0x403 (1027) |
| ECU | [VCFRONT1 ECU](../../vcfront1.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT1 |
| Frame length | 7 bytes |
| Cycle time | 200 ms |
| Signals | 37 |

## Signals of VCFRONT1_eFuseDebugStatus

Tesla Model Y CAN bus signals in `VCFRONT1_eFuseDebugStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT1_eFuseDebugStatusIndex` | selector | VCFRONT1 ECU: e fuse debug status index | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `EPAS2`<br>1 = `RIGHT_CONTROLLER`<br>2 = `PCS`<br>3 = `AUTOPILOT_2`<br>4 = `BRAKE_MOTOR_ECU_2`<br>5 = `BRIDGE` | plausible |
| `VCFRONT1_EPAS2EFuseState` | page 0 | VCFRONT1 ECU: EPAS2 e fuse state | 3\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STANDBY`<br>1 = `WAKEUP`<br>2 = `CONFIGURATION`<br>3 = `UNLOCKED`<br>4 = `LOCKED`<br>5 = `FAILSAFE`<br>6 = `SELF_TEST_PREP`<br>7 = `SELF_TEST` | validated |
| `VCFRONT1_EPAS2EFuseCurrent` | page 0 | VCFRONT1 ECU: EPAS2 e fuse current | 8\|12 | little-endian | unsigned | 0.05 | 0 | A | 0 to 204.75 |  | validated |
| `VCFRONT1_EPAS2EFuseOutput` | page 0 | VCFRONT1 ECU: EPAS2 e fuse output | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT1_EPAS2EFuseOutputDesired` | page 0 | VCFRONT1 ECU: EPAS2 e fuse output desired | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT1_EPAS2EFuseBypass` | page 0 | VCFRONT1 ECU: EPAS2 e fuse bypass | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT1_EPAS2EFuseBypassDesired` | page 0 | VCFRONT1 ECU: EPAS2 e fuse bypass desired | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT1_EPAS2EFuseVoltage` | page 0 | VCFRONT1 ECU: EPAS2 e fuse voltage | 24\|8 | little-endian | unsigned | 0.07 | 0 | V | 0 to 17.85 |  | validated |
| `VCFRONT1_EPAS2EFuseTemperature` | page 0 | VCFRONT1 ECU: EPAS2 e fuse temperature | 32\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 150 |  | validated |
| `VCFRONT1_EPAS2EFuseManagerState` | page 0 | VCFRONT1 ECU: EPAS2 e fuse manager state | 40\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `RESETTING`<br>1 = `OFF`<br>2 = `WAKEUP`<br>3 = `STANDBY`<br>4 = `LOCKING`<br>5 = `LOCKED_ON_BOOT`<br>6 = `UNLOCKING`<br>7 = `IDLE`<br>8 = `LOCKOUT` | validated |
| `VCFRONT1_EPAS2EFuseHardShortThreshold` | page 0 | VCFRONT1 ECU: EPAS2 e fuse hard short threshold | 44\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `20_MV`<br>1 = `23_MV`<br>2 = `26_4_MV`<br>3 = `30_3_MV`<br>4 = `34_8_MV`<br>5 = `40_MV`<br>6 = `45_9_MV`<br>7 = `52_8_MV`<br>8 = `60_6_MV`<br>9 = `69_6_MV`<br>10 = `80_MV`<br>11 = `91_9_MV`<br>12 = `105_6_MV`<br>13 = `121_3_MV`<br>14 = `139_3_MV`<br>15 = `160_MV` | validated |
| `VCFRONT1_EPAS2EFuseOCThreshold` | page 0 | VCFRONT1 ECU: EPAS2 e fuse OC threshold | 48\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `6_MV`<br>1 = `7_2_MV`<br>2 = `8_7_MV`<br>3 = `10_4_MV`<br>4 = `11_8_MV`<br>5 = `13_MV`<br>6 = `13_8_MV`<br>7 = `14_8_MV`<br>8 = `15_8_MV`<br>9 = `16_8_MV`<br>10 = `17_9_MV`<br>11 = `19_1_MV`<br>12 = `20_4_MV`<br>13 = `21_8_MV`<br>14 = `23_3_MV`<br>15 = `24_8_MV`<br>16 = `26_5_MV`<br>17 = `28_2_MV`<br>18 = `30_1_MV`<br>19 = `32_2_MV`<br>20 = `34_3_MV`<br>21 = `36_6_MV`<br>22 = `39_1_MV`<br>23 = `41_7_MV`<br>24 = `44_5_MV`<br>25 = `47_5_MV`<br>26 = `50_6_MV`<br>27 = `54_MV`<br>28 = `61_3_MV`<br>29 = `69_5_MV`<br>30 = `78_8_MV`<br>31 = `89_3_MV` | validated |
| `VCFRONT1_EPAS2EFuseType` | page 0 | Reports the type of the EPAS2 eFuse. | 53\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `VNF1048`<br>2 = `VNF1248` | validated |
| `VCFRONT1_rightControllerEFuseState` | page 1 | VCFRONT1 ECU: right controller e fuse state | 3\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STANDBY`<br>1 = `WAKEUP`<br>2 = `CONFIGURATION`<br>3 = `UNLOCKED`<br>4 = `LOCKED`<br>5 = `FAILSAFE`<br>6 = `SELF_TEST_PREP`<br>7 = `SELF_TEST` | validated |
| `VCFRONT1_rightControllerEFuseCurrent` | page 1 | VCFRONT1 ECU: right controller e fuse current | 8\|12 | little-endian | unsigned | 0.05 | 0 | A | 0 to 204.75 |  | validated |
| `VCFRONT1_rightControllerEFuseOutput` | page 1 | VCFRONT1 ECU: right controller e fuse output | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT1_rightControllerEFuseOutputDesired` | page 1 | VCFRONT1 ECU: right controller e fuse output desired | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT1_rightControllerEFuseBypass` | page 1 | VCFRONT1 ECU: right controller e fuse bypass | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT1_rightControllerEFuseBypassDesired` | page 1 | VCFRONT1 ECU: right controller e fuse bypass desired | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT1_rightControllerEFuseVoltage` | page 1 | VCFRONT1 ECU: right controller e fuse voltage | 24\|8 | little-endian | unsigned | 0.07 | 0 | V | 0 to 17.85 |  | validated |
| `VCFRONT1_rightControllerEFuseTemperature` | page 1 | VCFRONT1 ECU: right controller e fuse temperature | 32\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 150 |  | validated |
| `VCFRONT1_rightControllerEFuseManagerState` | page 1 | VCFRONT1 ECU: right controller e fuse manager state | 40\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `RESETTING`<br>1 = `OFF`<br>2 = `WAKEUP`<br>3 = `STANDBY`<br>4 = `LOCKING`<br>5 = `LOCKED_ON_BOOT`<br>6 = `UNLOCKING`<br>7 = `IDLE`<br>8 = `LOCKOUT` | validated |
| `VCFRONT1_rightControllerEFuseHardShortThreshold` | page 1 | VCFRONT1 ECU: right controller e fuse hard short threshold | 44\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `20_MV`<br>1 = `23_MV`<br>2 = `26_4_MV`<br>3 = `30_3_MV`<br>4 = `34_8_MV`<br>5 = `40_MV`<br>6 = `45_9_MV`<br>7 = `52_8_MV`<br>8 = `60_6_MV`<br>9 = `69_6_MV`<br>10 = `80_MV`<br>11 = `91_9_MV`<br>12 = `105_6_MV`<br>13 = `121_3_MV`<br>14 = `139_3_MV`<br>15 = `160_MV` | validated |
| `VCFRONT1_rightControllerEFuseOCThreshold` | page 1 | VCFRONT1 ECU: right controller e fuse OC threshold | 48\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `6_MV`<br>1 = `7_2_MV`<br>2 = `8_7_MV`<br>3 = `10_4_MV`<br>4 = `11_8_MV`<br>5 = `13_MV`<br>6 = `13_8_MV`<br>7 = `14_8_MV`<br>8 = `15_8_MV`<br>9 = `16_8_MV`<br>10 = `17_9_MV`<br>11 = `19_1_MV`<br>12 = `20_4_MV`<br>13 = `21_8_MV`<br>14 = `23_3_MV`<br>15 = `24_8_MV`<br>16 = `26_5_MV`<br>17 = `28_2_MV`<br>18 = `30_1_MV`<br>19 = `32_2_MV`<br>20 = `34_3_MV`<br>21 = `36_6_MV`<br>22 = `39_1_MV`<br>23 = `41_7_MV`<br>24 = `44_5_MV`<br>25 = `47_5_MV`<br>26 = `50_6_MV`<br>27 = `54_MV`<br>28 = `61_3_MV`<br>29 = `69_5_MV`<br>30 = `78_8_MV`<br>31 = `89_3_MV` | validated |
| `VCFRONT1_rightControllerEFuseType` | page 1 | Reports the type of the right controller eFuse. | 53\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `VNF1048`<br>2 = `VNF1248` | validated |
| `VCFRONT1_autopilot2EFuseState` | page 3 | VCFRONT1 ECU: autopilot2 e fuse state | 3\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STANDBY`<br>1 = `WAKEUP`<br>2 = `CONFIGURATION`<br>3 = `UNLOCKED`<br>4 = `LOCKED`<br>5 = `FAILSAFE`<br>6 = `SELF_TEST_PREP`<br>7 = `SELF_TEST` | validated |
| `VCFRONT1_autopilot2EFuseCurrent` | page 3 | VCFRONT1 ECU: autopilot2 e fuse current | 8\|12 | little-endian | unsigned | 0.05 | 0 | A | 0 to 204.75 |  | validated |
| `VCFRONT1_autopilot2EFuseOutput` | page 3 | VCFRONT1 ECU: autopilot2 e fuse output | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT1_autopilot2EFuseOutputDesired` | page 3 | VCFRONT1 ECU: autopilot2 e fuse output desired | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT1_autopilot2EFuseBypass` | page 3 | VCFRONT1 ECU: autopilot2 e fuse bypass | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT1_autopilot2EFuseBypassDesired` | page 3 | VCFRONT1 ECU: autopilot2 e fuse bypass desired | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT1_autopilot2EFuseVoltage` | page 3 | VCFRONT1 ECU: autopilot2 e fuse voltage | 24\|8 | little-endian | unsigned | 0.07 | 0 | V | 0 to 17.85 |  | validated |
| `VCFRONT1_autopilot2EFuseTemperature` | page 3 | VCFRONT1 ECU: autopilot2 e fuse temperature | 32\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 150 |  | validated |
| `VCFRONT1_autopilot2EFuseManagerState` | page 3 | VCFRONT1 ECU: autopilot2 e fuse manager state | 40\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `RESETTING`<br>1 = `OFF`<br>2 = `WAKEUP`<br>3 = `STANDBY`<br>4 = `LOCKING`<br>5 = `LOCKED_ON_BOOT`<br>6 = `UNLOCKING`<br>7 = `IDLE`<br>8 = `LOCKOUT` | validated |
| `VCFRONT1_autopilot2EFuseHardShortThreshold` | page 3 | VCFRONT1 ECU: autopilot2 e fuse hard short threshold | 44\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `20_MV`<br>1 = `23_MV`<br>2 = `26_4_MV`<br>3 = `30_3_MV`<br>4 = `34_8_MV`<br>5 = `40_MV`<br>6 = `45_9_MV`<br>7 = `52_8_MV`<br>8 = `60_6_MV`<br>9 = `69_6_MV`<br>10 = `80_MV`<br>11 = `91_9_MV`<br>12 = `105_6_MV`<br>13 = `121_3_MV`<br>14 = `139_3_MV`<br>15 = `160_MV` | validated |
| `VCFRONT1_autopilot2EFuseOCThreshold` | page 3 | VCFRONT1 ECU: autopilot2 e fuse OC threshold | 48\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `6_MV`<br>1 = `7_2_MV`<br>2 = `8_7_MV`<br>3 = `10_4_MV`<br>4 = `11_8_MV`<br>5 = `13_MV`<br>6 = `13_8_MV`<br>7 = `14_8_MV`<br>8 = `15_8_MV`<br>9 = `16_8_MV`<br>10 = `17_9_MV`<br>11 = `19_1_MV`<br>12 = `20_4_MV`<br>13 = `21_8_MV`<br>14 = `23_3_MV`<br>15 = `24_8_MV`<br>16 = `26_5_MV`<br>17 = `28_2_MV`<br>18 = `30_1_MV`<br>19 = `32_2_MV`<br>20 = `34_3_MV`<br>21 = `36_6_MV`<br>22 = `39_1_MV`<br>23 = `41_7_MV`<br>24 = `44_5_MV`<br>25 = `47_5_MV`<br>26 = `50_6_MV`<br>27 = `54_MV`<br>28 = `61_3_MV`<br>29 = `69_5_MV`<br>30 = `78_8_MV`<br>31 = `89_3_MV` | validated |
| `VCFRONT1_autopilot2EFuseType` | page 3 | Reports the type of the autopilot2 eFuse. | 53\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `VNF1048`<br>2 = `VNF1248` | validated |

## Multiplexing

`VCFRONT1_eFuseDebugStatusIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (12 signals), page 1 (12 signals), page 3 (12 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All VCFRONT1 ECU messages (VCFRONT1)](../../vcfront1.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
