---
layout: default
title: "APS_warningMatrix4 (0x310) — Driver assistance computer (secondary), Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Driver assistance computer (secondary) message: warning matrix4. Tesla Model 3 / Model Y CAN bus message APS_warningMatrix4 (0x310) of Driver assistance computer (secondary), firmware 2026.26.6.5, 63 signals (APS_w257_assertFailure, APS_w258_qspiFlashSectorChecksumMismatch, APS_w259_qspiFailure, APS_w260_pgoodFailure and 59 more). Bit layout, scaling, units and value tables."
---

# APS_warningMatrix4 (0x310) — Driver assistance computer (secondary), Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Driver assistance computer (secondary) message: warning matrix4; frame length from the layout, not yet observed on a vehicle bus. This page documents the 63 signals of APS_warningMatrix4 as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APS_warningMatrix4` |
| CAN id | 0x310 (784) |
| ECU | [Driver assistance computer (secondary)](../../aps.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | APS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 63 |

## Signals of APS_warningMatrix4

Tesla Model 3 / Model Y CAN bus signals in `APS_warningMatrix4`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APS_w257_assertFailure` | Driver assistance computer (secondary): w257 assert failure | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w258_qspiFlashSectorChecksumMismatch` | Driver assistance computer (secondary): w258 qspi flash sector checksum mismatch | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w259_qspiFailure` | Driver assistance computer (secondary): w259 qspi failure | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w260_pgoodFailure` | Driver assistance computer (secondary): w260 pgood failure | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w261_vrmFaultGrpA` | Driver assistance computer (secondary): w261 vrm fault grp a | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w262_vrmFaultGrpB` | Driver assistance computer (secondary): w262 vrm fault grp b | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w263_vrmFaultGrpC` | Driver assistance computer (secondary): w263 vrm fault grp c | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w264_ddrPhy0Failures` | Driver assistance computer (secondary): w264 ddr phy0 failures | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w265_ddrPhy1Failures` | Driver assistance computer (secondary): w265 ddr phy1 failures | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w266_ddrPhy2Failures` | Driver assistance computer (secondary): w266 ddr phy2 failures | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w267_ddrPhy3Failures` | Driver assistance computer (secondary): w267 ddr phy3 failures | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w268_ddrControllerFailures` | Driver assistance computer (secondary): w268 ddr controller failures | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w269_ethSwitchRxPageCountTooHighPort0_3` | Driver assistance computer (secondary): w269 eth switch rx page count too high port0 3 | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w270_ethSwitchRxPageCountTooHighPort4_7` | Driver assistance computer (secondary): w270 eth switch rx page count too high port4 7 | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w271_ddrScheduler0EccErrors` | Driver assistance computer (secondary): w271 ddr scheduler0 ecc errors | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w272_ddrScheduler1EccErrors` | Driver assistance computer (secondary): w272 ddr scheduler1 ecc errors | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w273_ddrScheduler2EccErrors` | Driver assistance computer (secondary): w273 ddr scheduler2 ecc errors | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w274_ddrScheduler3EccErrors` | Driver assistance computer (secondary): w274 ddr scheduler3 ecc errors | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w275_ddrScheduler4EccErrors` | Driver assistance computer (secondary): w275 ddr scheduler4 ecc errors | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w276_ddrScheduler5EccErrors` | Driver assistance computer (secondary): w276 ddr scheduler5 ecc errors | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w277_ddrScheduler6EccErrors` | Driver assistance computer (secondary): w277 ddr scheduler6 ecc errors | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w278_ddrScheduler7EccErrors` | Driver assistance computer (secondary): w278 ddr scheduler7 ecc errors | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w279_ufsPartitionError` | Driver assistance computer (secondary): w279 ufs partition error | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w280_pepsMia` | Driver assistance computer (secondary): w280 peps mia | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w281_rsaMia` | Driver assistance computer (secondary): w281 rsa mia | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w282_smmuError` | Driver assistance computer (secondary): w282 smmu error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w283_psfaMia` | Driver assistance computer (secondary): w283 psfa mia | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w284_cam12VBuckBoostAPwrIssue` | Driver assistance computer (secondary): w284 cam12 v buck boost a pwr issue | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w285_cam12VBuckBoostBPwrIssue` | Driver assistance computer (secondary): w285 cam12 v buck boost b pwr issue | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w286_cam12VEFuseAPrimaryIssue` | Driver assistance computer (secondary): w286 cam12 VE fuse a primary issue | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w287_cam12VEFuseASecondaryIssue` | Driver assistance computer (secondary): w287 cam12 VE fuse a secondary issue | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w288_brakeboosterMia` | Driver assistance computer (secondary): w288 brakebooster mia | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w289_turboTemperatureWarning` | Driver assistance computer (secondary): w289 turbo temperature warning | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w290_cam12VBuckBoostBPwrRinging` | Driver assistance computer (secondary): w290 cam12 v buck boost b pwr ringing | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w291_eplannerError` | Driver assistance computer (secondary): w291 eplanner error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w292_CH_busOff` | Driver assistance computer (secondary): w292 CH bus off | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w293_PARTY_busOff` | Driver assistance computer (secondary): w293 PARTY bus off | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w294_VEH_busOff` | Driver assistance computer (secondary): w294 VEH bus off | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w295_PT_busOff` | Driver assistance computer (secondary): w295 PT bus off | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w296_wdogMonTaskDeadlineMiss` | Driver assistance computer (secondary): w296 wdog mon task deadline miss | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w297_earlyWDogAlert` | Driver assistance computer (secondary): w297 early w dog alert | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w298_cpuToApCanSharedMemError` | Driver assistance computer (secondary): w298 cpu to ap can shared mem error | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w299_apToCpuCanSharedMemError` | Driver assistance computer (secondary): w299 ap to cpu can shared mem error | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w300_sharedMemoryAccessError` | Driver assistance computer (secondary): w300 shared memory access error | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w301_nocTimeoutDetected` | Driver assistance computer (secondary): w301 noc timeout detected | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w302_canAPShmFifoFull` | Driver assistance computer (secondary): w302 can AP shm fifo full | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w303_canAPShmFifoEmpty` | Driver assistance computer (secondary): w303 can AP shm fifo empty | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w304_dataAbort` | Driver assistance computer (secondary): w304 data abort | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w305_gpsPgoodFailure` | Driver assistance computer (secondary): w305 gps pgood failure | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w306_ethPgoodFailure` | Driver assistance computer (secondary): w306 eth pgood failure | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w307_eccEventDetected` | Driver assistance computer (secondary): w307 ecc event detected | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w308_pmicErrorDetected` | Driver assistance computer (secondary): w308 pmic error detected | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w309_ethBridgeDown` | Driver assistance computer (secondary): w309 eth bridge down | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w310_wakeBootMetrics` | Driver assistance computer (secondary): w310 wake boot metrics | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w311_apbdgDasMia` | Driver assistance computer (secondary): w311 apbdg das mia | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w312_apbdgApMia` | Driver assistance computer (secondary): w312 apbdg ap mia | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w313_BDY_busOff` | Driver assistance computer (secondary): w313 BDY bus off | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w315_epas3pMiaBdyBus` | Driver assistance computer (secondary): w315 epas3p mia bdy bus | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w316_apBootHealth` | Driver assistance computer (secondary): w316 ap boot health | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w317_uiMia` | Driver assistance computer (secondary): w317 ui mia | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w318_ethernetNetworkBufferHighWatermark` | Driver assistance computer (secondary): w318 ethernet network buffer high watermark | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w319_vehDasImposterDetected` | Driver assistance computer (secondary): w319 veh das imposter detected | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w320_eplannerPreconditionsMet` | Driver assistance computer (secondary): w320 eplanner preconditions met | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer (secondary) messages (APS)](../../aps.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
