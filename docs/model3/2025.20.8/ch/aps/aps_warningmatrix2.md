---
layout: default
title: "APS_warningMatrix2 (0x459) — Driver assistance computer (secondary), Tesla Model 3 2025.20.8 CH CAN"
description: "Driver assistance computer (secondary) message: warning matrix2. Tesla Model 3 CAN bus message APS_warningMatrix2 (0x459) of Driver assistance computer (secondary), firmware 2025.20.8, 58 signals (APS_w129_ECU_Power_Issue, APS_w130_ECU_Thermal_Issue, APS_w131_trap_exception, APS_w132_appVersionMismatch and 54 more). Bit layout, scaling, units and value tables."
---

# APS_warningMatrix2 (0x459) — Driver assistance computer (secondary), Tesla Model 3 2025.20.8 CH CAN

Driver assistance computer (secondary) message: warning matrix2; frame length from the layout, not yet observed on a vehicle bus. This page documents the 58 signals of APS_warningMatrix2 as defined for Tesla Model 3 firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APS_warningMatrix2` |
| CAN id | 0x459 (1113) |
| ECU | [Driver assistance computer (secondary)](../../aps.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | APS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 58 |

## Signals of APS_warningMatrix2

Tesla Model 3 CAN bus signals in `APS_warningMatrix2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APS_w129_ECU_Power_Issue` | Driver assistance computer (secondary): w129 ECU power issue | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w130_ECU_Thermal_Issue` | Driver assistance computer (secondary): w130 ECU thermal issue | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w131_trap_exception` | Driver assistance computer (secondary): w131 trap exception | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w132_appVersionMismatch` | Driver assistance computer (secondary): w132 app version mismatch | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w133_ETHSwitchError` | Driver assistance computer (secondary): w133 ETH switch error | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w134_appMia` | Driver assistance computer (secondary): w134 app mia | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w135_appCritical` | Driver assistance computer (secondary): w135 app critical | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w136_gpsDisabled` | Driver assistance computer (secondary): w136 gps disabled | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w137_gpsFaultReset` | Driver assistance computer (secondary): w137 gps fault reset | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w138_gpsComIssue` | Driver assistance computer (secondary): w138 gps com issue | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w139_udpBufferOverflow` | Driver assistance computer (secondary): w139 udp buffer overflow | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w140_vcfrontMiaVehicleBus` | Driver assistance computer (secondary): w140 vcfront mia vehicle bus | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w141_rcmMiaPartyBus` | Driver assistance computer (secondary): w141 rcm mia party bus | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w142_diMiaPartyBus` | Driver assistance computer (secondary): w142 di mia party bus | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w143_espMiaPartyBus` | Driver assistance computer (secondary): w143 esp mia party bus | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w144_vcleftMiaPartyBus` | Driver assistance computer (secondary): w144 vcleft mia party bus | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w145_vcrightMiaPartyBus` | Driver assistance computer (secondary): w145 vcright mia party bus | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w146_epas3pMiaPartyBus` | Driver assistance computer (secondary): w146 epas3p mia party bus | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w147_vcleftMiaVehBus` | Driver assistance computer (secondary): w147 vcleft mia veh bus | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w148_vcrightMiaVehBus` | Driver assistance computer (secondary): w148 vcright mia veh bus | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w149_epblMiaVehBus` | Driver assistance computer (secondary): w149 epbl mia veh bus | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w150_sccmMiaVehBus` | Driver assistance computer (secondary): w150 sccm mia veh bus | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w151_apRecovered` | Driver assistance computer (secondary): w151 ap recovered | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w152_gpsFusionStatus` | Driver assistance computer (secondary): w152 gps fusion status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w153_eacInhibit` | Driver assistance computer (secondary): w153 eac inhibit | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w155_ethLwipError` | Driver assistance computer (secondary): w155 eth lwip error | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w156_lwipAssert` | Driver assistance computer (secondary): w156 lwip assert | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w157_autopilotReboot` | Driver assistance computer (secondary): w157 autopilot reboot | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w158_apbMia` | Driver assistance computer (secondary): w158 apb mia | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w159_apbCritical` | Driver assistance computer (secondary): w159 apb critical | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w160_apbVersionMismatch` | Driver assistance computer (secondary): w160 apb version mismatch | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w161_gpsAntennaDisconnected` | Driver assistance computer (secondary): w161 gps antenna disconnected | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w162_TurboA_DisRegPgoodErr` | Driver assistance computer (secondary): w162 turbo a dis reg pgood err | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w163_TurboA_DisRegNFault` | Driver assistance computer (secondary): w163 turbo a dis reg n fault | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w164_TurboA_12VFuseFault` | Driver assistance computer (secondary): w164 turbo a 12 v fuse fault | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w165_TurboA_Temp_NOS` | Driver assistance computer (secondary): w165 turbo a temp NOS | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w166_TurboA_SMSLockStepErr` | Driver assistance computer (secondary): w166 turbo a SMS lock step err | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w167_TurboA_TMU_Throttle` | Driver assistance computer (secondary): w167 turbo a TMU throttle | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w168_TurboA_SMS_WDOG` | Driver assistance computer (secondary): w168 turbo a SMS WDOG | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w169_TurboA_SCS_LKUP` | Driver assistance computer (secondary): w169 turbo a SCS LKUP | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w170_TurboA_A72_watchdog` | Driver assistance computer (secondary): w170 turbo a A72 watchdog | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w171_TurboA_SMS_taskUtilErr` | Driver assistance computer (secondary): w171 turbo a SMS task util err | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w172_apFeaturesUnavailable` | Driver assistance computer (secondary): w172 ap features unavailable | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w178_TurboB_DisRegPgoodErr` | Driver assistance computer (secondary): w178 turbo b dis reg pgood err | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w179_TurboB_DisRegNFault` | Driver assistance computer (secondary): w179 turbo b dis reg n fault | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w180_TurboB_12VFuseFault` | Driver assistance computer (secondary): w180 turbo b 12 v fuse fault | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w181_TurboB_Temp_NOS` | Driver assistance computer (secondary): w181 turbo b temp NOS | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w182_TurboB_SMSLockStepErr` | Driver assistance computer (secondary): w182 turbo b SMS lock step err | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w183_TurboB_TMU_Throttle` | Driver assistance computer (secondary): w183 turbo b TMU throttle | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w184_TurboB_SMS_WDOG` | Driver assistance computer (secondary): w184 turbo b SMS WDOG | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w185_TurboB_SCS_LKUP` | Driver assistance computer (secondary): w185 turbo b SCS LKUP | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w186_TurboB_A72_watchdog` | Driver assistance computer (secondary): w186 turbo b A72 watchdog | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w187_TurboB_SMS_taskUtilErr` | Driver assistance computer (secondary): w187 turbo b SMS task util err | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w188_otherTurboUartMIA` | Driver assistance computer (secondary): w188 other turbo uart MIA | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w189_vcfrontMiaPartyBus` | Driver assistance computer (secondary): w189 vcfront mia party bus | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w190_iboosterMia` | Driver assistance computer (secondary): w190 ibooster mia | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w191_timesyncError` | Driver assistance computer (secondary): w191 timesync error | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w192_CANFault` | Driver assistance computer (secondary): w192 CAN fault | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 CH DBC file](../../../../../dbc/Model3/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/CH.json)

## See also

- [All Driver assistance computer (secondary) messages (APS)](../../aps.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
