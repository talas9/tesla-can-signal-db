---
layout: default
title: "APSB_warningMatrix2 (0x3AE) — APSB ECU, Tesla Model Y 2026.26.6.5 ETH"
description: "APSB ECU message: warning matrix2. Ethernet-side message APSB_warningMatrix2 of APSB ECU for Tesla Model Y firmware 2026.26.6.5, 58 signals (APSB_w129_ECU_Power_Issue, APSB_w130_ECU_Thermal_Issue, APSB_w131_trap_exception, APSB_w132_appVersionMismatch and 54 more). Bit layout, scaling, units and value tables."
---

# APSB_warningMatrix2 (0x3AE) — APSB ECU, Tesla Model Y 2026.26.6.5 ETH

APSB ECU message: warning matrix2. This page documents the 58 signals of APSB_warningMatrix2 as defined for Tesla Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `APSB_warningMatrix2` |
| Ethernet-side id | 0x3AE (942) |
| ECU | [APSB ECU](../../apsb.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | APSB |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 58 |

## Signals of APSB_warningMatrix2

Tesla Model Y CAN bus signals in `APSB_warningMatrix2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APSB_w129_ECU_Power_Issue` | APSB ECU: w129 ECU power issue | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w130_ECU_Thermal_Issue` | APSB ECU: w130 ECU thermal issue | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w131_trap_exception` | APSB ECU: w131 trap exception | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w132_appVersionMismatch` | APSB ECU: w132 app version mismatch | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w133_ETHSwitchError` | APSB ECU: w133 ETH switch error | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w134_appMia` | APSB ECU: w134 app mia | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w135_appCritical` | APSB ECU: w135 app critical | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w136_gpsDisabled` | APSB ECU: w136 gps disabled | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w137_gpsFaultReset` | APSB ECU: w137 gps fault reset | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w138_gpsComIssue` | APSB ECU: w138 gps com issue | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w139_udpBufferOverflow` | APSB ECU: w139 udp buffer overflow | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w140_vcfrontMiaVehicleBus` | APSB ECU: w140 vcfront mia vehicle bus | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w141_rcmMiaPartyBus` | APSB ECU: w141 rcm mia party bus | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w142_diMiaPartyBus` | APSB ECU: w142 di mia party bus | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w143_espMiaPartyBus` | APSB ECU: w143 esp mia party bus | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w144_vcleftMiaPartyBus` | APSB ECU: w144 vcleft mia party bus | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w145_vcrightMiaPartyBus` | APSB ECU: w145 vcright mia party bus | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w146_epas3pMiaPartyBus` | APSB ECU: w146 epas3p mia party bus | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w147_vcleftMiaVehBus` | APSB ECU: w147 vcleft mia veh bus | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w148_vcrightMiaVehBus` | APSB ECU: w148 vcright mia veh bus | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w149_epblMiaVehBus` | APSB ECU: w149 epbl mia veh bus | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w150_sccmMiaVehBus` | APSB ECU: w150 sccm mia veh bus | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w151_apRecovered` | APSB ECU: w151 ap recovered | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w152_gpsFusionStatus` | APSB ECU: w152 gps fusion status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w153_eacInhibit` | APSB ECU: w153 eac inhibit | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w155_ethLwipError` | APSB ECU: w155 eth lwip error | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w156_lwipAssert` | APSB ECU: w156 lwip assert | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w157_autopilotReboot` | APSB ECU: w157 autopilot reboot | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w158_apbMia` | APSB ECU: w158 apb mia | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w159_apbCritical` | APSB ECU: w159 apb critical | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w160_apbVersionMismatch` | APSB ECU: w160 apb version mismatch | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w161_gpsAntennaDisconnected` | APSB ECU: w161 gps antenna disconnected | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w162_TurboA_DisRegPgoodErr` | APSB ECU: w162 turbo a dis reg pgood err | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w163_TurboA_DisRegNFault` | APSB ECU: w163 turbo a dis reg n fault | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w164_TurboA_12VFuseFault` | APSB ECU: w164 turbo a 12 v fuse fault | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w165_TurboA_Temp_NOS` | APSB ECU: w165 turbo a temp NOS | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w166_TurboA_SMSLockStepErr` | APSB ECU: w166 turbo a SMS lock step err | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w167_TurboA_TMU_Throttle` | APSB ECU: w167 turbo a TMU throttle | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w168_TurboA_SMS_WDOG` | APSB ECU: w168 turbo a SMS WDOG | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w169_TurboA_SCS_LKUP` | APSB ECU: w169 turbo a SCS LKUP | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w170_TurboA_A72_watchdog` | APSB ECU: w170 turbo a A72 watchdog | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w171_TurboA_SMS_taskUtilErr` | APSB ECU: w171 turbo a SMS task util err | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w172_apFeaturesUnavailable` | APSB ECU: w172 ap features unavailable | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w178_TurboB_DisRegPgoodErr` | APSB ECU: w178 turbo b dis reg pgood err | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w179_TurboB_DisRegNFault` | APSB ECU: w179 turbo b dis reg n fault | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w180_TurboB_12VFuseFault` | APSB ECU: w180 turbo b 12 v fuse fault | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w181_TurboB_Temp_NOS` | APSB ECU: w181 turbo b temp NOS | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w182_TurboB_SMSLockStepErr` | APSB ECU: w182 turbo b SMS lock step err | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w183_TurboB_TMU_Throttle` | APSB ECU: w183 turbo b TMU throttle | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w184_TurboB_SMS_WDOG` | APSB ECU: w184 turbo b SMS WDOG | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w185_TurboB_SCS_LKUP` | APSB ECU: w185 turbo b SCS LKUP | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w186_TurboB_A72_watchdog` | APSB ECU: w186 turbo b A72 watchdog | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w187_TurboB_SMS_taskUtilErr` | APSB ECU: w187 turbo b SMS task util err | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w188_otherTurboUartMIA` | APSB ECU: w188 other turbo uart MIA | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w189_vcfrontMiaPartyBus` | APSB ECU: w189 vcfront mia party bus | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w190_iboosterMia` | APSB ECU: w190 ibooster mia | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w191_timesyncError` | APSB ECU: w191 timesync error | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w192_CANFault` | APSB ECU: w192 CAN fault | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/ModelY/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All APSB ECU messages (APSB)](../../apsb.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
