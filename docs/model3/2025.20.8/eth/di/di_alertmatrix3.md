---
layout: default
title: "DI_alertMatrix3 (0x36B) — Drive inverter, Tesla Model 3 2025.20.8 ETH"
description: "Drive inverter message: alert matrix3. Ethernet-side message DI_alertMatrix3 of Drive inverter for Tesla Model 3 firmware 2025.20.8, 53 signals (DI_a129_epbNotApplied, DI_a130_aebFault, DI_a131_highSpeedWearLimit, DI_a133_vehicleHoldTimedOut and 49 more). Bit layout, scaling, units and value tables."
---

# DI_alertMatrix3 (0x36B) — Drive inverter, Tesla Model 3 2025.20.8 ETH

Drive inverter message: alert matrix3. This page documents the 53 signals of DI_alertMatrix3 as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DI_alertMatrix3` |
| Ethernet-side id | 0x36B (875) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DI |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 53 |

## Signals of DI_alertMatrix3

Tesla Model 3 CAN bus signals in `DI_alertMatrix3`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_a129_epbNotApplied` | Drive inverter: a129 epb not applied | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a130_aebFault` | Drive inverter: a130 aeb fault | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a131_highSpeedWearLimit` | Drive inverter: a131 high speed wear limit | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a133_vehicleHoldTimedOut` | Drive inverter: a133 vehicle hold timed out | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a134_wheelSpeedIrrational` | Drive inverter: a134 wheel speed irrational | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a135_vehicleHoldFault` | Drive inverter: a135 vehicle hold fault | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a137_noCapableDriveUnits` | Drive inverter: a137 no capable drive units | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a138_frontUnitDisabled` | Drive inverter: a138 front unit disabled | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a139_rearUnitDisabled` | Drive inverter: a139 rear unit disabled | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a140_ptcMIA` | Drive inverter: a140 ptc MIA | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a141_dasMIA` | Drive inverter: a141 das MIA | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a142_potholeDetected` | Drive inverter: a142 pothole detected | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a143_mcuLimitActive` | Drive inverter: a143 mcu limit active | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a144_configMismatch` | Drive inverter: a144 config mismatch | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a146_pbrkPanicEpbFault` | Drive inverter: a146 pbrk panic epb fault | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a154_vdcRearSteering` | Drive inverter: a154 vdc rear steering | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a155_vcfrontMIA` | Drive inverter: a155 vcfront MIA | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a157_rcmMIA` | Drive inverter: a157 rcm MIA | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a158_ibstMIA` | Drive inverter: a158 ibst MIA | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a159_cruiseSelfCheck` | Drive inverter: a159 cruise self check | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a160_fastLearnComplete` | Drive inverter: a160 fast learn complete | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a161_epas3pMIA` | Drive inverter: a161 epas3p MIA | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a162_shiftDenied` | Drive inverter: a162 shift denied | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a163_shiftMotorSpeed` | Drive inverter: a163 shift motor speed | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a164_brakeOverride` | Drive inverter: a164 brake override | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a165_cruiseCancelled` | Drive inverter: a165 cruise cancelled | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a166_driverLeft` | Drive inverter: a166 driver left | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a167_keyNotAuthenticated` | Drive inverter: a167 key not authenticated | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a168_proximityDriveDenial` | Drive inverter: a168 proximity drive denial | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a169_regenOffOverride` | Drive inverter: a169 regen off override | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a170_tireConfigUpdated` | Drive inverter: a170 tire config updated | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a171_driveRailNotRequested` | Drive inverter: a171 drive rail not requested | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a172_accelPressedInNP` | Drive inverter: a172 accel pressed in NP | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a173_bothPedalsPressed` | Drive inverter: a173 both pedals pressed | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a174_notOkToStartDrive` | Drive inverter: a174 not ok to start drive | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a175_crsNotAvailable` | Drive inverter: a175 crs not available | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a176_EBRreleased` | Drive inverter: a176 EB rreleased | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a177_tireFitmentChanged` | Drive inverter: a177 tire fitment changed | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a178_steeringAngleOffsetFault` | Drive inverter: a178 steering angle offset fault | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a179_steeringAngleOffsetWarning` | Drive inverter: a179 steering angle offset warning | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a180_crsSeatbeltUnbuckled` | Drive inverter: a180 crs seatbelt unbuckled | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a181_rearMotorMode` | Drive inverter: a181 rear motor mode | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a182_frontMotorMode` | Drive inverter: a182 front motor mode | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a183_holdReleaseRqrd` | Drive inverter: a183 hold release rqrd | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a184_autoparkCanceled` | Drive inverter: a184 autopark canceled | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a185_autoparkAborted` | Drive inverter: a185 autopark aborted | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a186_brakeStand` | Drive inverter: a186 brake stand | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a187_pedalMisapplication` | Drive inverter: a187 pedal misapplication | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a188_tireRotationRecommendedGhosted` | Drive inverter: a188 tire rotation recommended ghosted | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a189_garageShiftWithPedal` | Drive inverter: a189 garage shift with pedal | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a190_tireRotationRecommended` | Drive inverter: a190 tire rotation recommended | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a191_brakeShiftReq` | Drive inverter: a191 brake shift req | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a192_invalidOdometer` | Drive inverter: a192 invalid odometer | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
