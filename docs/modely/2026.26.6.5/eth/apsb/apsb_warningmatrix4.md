---
layout: default
title: "APSB_warningMatrix4 (0x3EB) — APSB ECU, Tesla Model Y 2026.26.6.5 ETH"
description: "APSB ECU message: warning matrix4. Ethernet-side message APSB_warningMatrix4 of APSB ECU for Tesla Model Y firmware 2026.26.6.5, 63 signals (APSB_w257_assertFailure, APSB_w258_qspiFlashSectorChecksumMismatch, APSB_w259_qspiFailure, APSB_w260_pgoodFailure and 59 more). Bit layout, scaling, units and value tables."
---

# APSB_warningMatrix4 (0x3EB) — APSB ECU, Tesla Model Y 2026.26.6.5 ETH

APSB ECU message: warning matrix4. This page documents the 63 signals of APSB_warningMatrix4 as defined for Tesla Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `APSB_warningMatrix4` |
| Ethernet-side id | 0x3EB (1003) |
| ECU | [APSB ECU](../../apsb.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | APSB |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 63 |

## Signals of APSB_warningMatrix4

Tesla Model Y CAN bus signals in `APSB_warningMatrix4`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APSB_w257_assertFailure` | APSB ECU: w257 assert failure | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w258_qspiFlashSectorChecksumMismatch` | APSB ECU: w258 qspi flash sector checksum mismatch | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w259_qspiFailure` | APSB ECU: w259 qspi failure | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w260_pgoodFailure` | APSB ECU: w260 pgood failure | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w261_vrmFaultGrpA` | APSB ECU: w261 vrm fault grp a | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w262_vrmFaultGrpB` | APSB ECU: w262 vrm fault grp b | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w263_vrmFaultGrpC` | APSB ECU: w263 vrm fault grp c | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w264_ddrPhy0Failures` | APSB ECU: w264 ddr phy0 failures | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w265_ddrPhy1Failures` | APSB ECU: w265 ddr phy1 failures | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w266_ddrPhy2Failures` | APSB ECU: w266 ddr phy2 failures | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w267_ddrPhy3Failures` | APSB ECU: w267 ddr phy3 failures | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w268_ddrControllerFailures` | APSB ECU: w268 ddr controller failures | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w269_ethSwitchRxPageCountTooHighPort0_3` | APSB ECU: w269 eth switch rx page count too high port0 3 | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w270_ethSwitchRxPageCountTooHighPort4_7` | APSB ECU: w270 eth switch rx page count too high port4 7 | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w271_ddrScheduler0EccErrors` | APSB ECU: w271 ddr scheduler0 ecc errors | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w272_ddrScheduler1EccErrors` | APSB ECU: w272 ddr scheduler1 ecc errors | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w273_ddrScheduler2EccErrors` | APSB ECU: w273 ddr scheduler2 ecc errors | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w274_ddrScheduler3EccErrors` | APSB ECU: w274 ddr scheduler3 ecc errors | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w275_ddrScheduler4EccErrors` | APSB ECU: w275 ddr scheduler4 ecc errors | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w276_ddrScheduler5EccErrors` | APSB ECU: w276 ddr scheduler5 ecc errors | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w277_ddrScheduler6EccErrors` | APSB ECU: w277 ddr scheduler6 ecc errors | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w278_ddrScheduler7EccErrors` | APSB ECU: w278 ddr scheduler7 ecc errors | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w279_ufsPartitionError` | APSB ECU: w279 ufs partition error | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w280_pepsMia` | APSB ECU: w280 peps mia | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w281_rsaMia` | APSB ECU: w281 rsa mia | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w282_smmuError` | APSB ECU: w282 smmu error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w283_psfaMia` | APSB ECU: w283 psfa mia | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w284_cam12VBuckBoostAPwrIssue` | APSB ECU: w284 cam12 v buck boost a pwr issue | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w285_cam12VBuckBoostBPwrIssue` | APSB ECU: w285 cam12 v buck boost b pwr issue | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w286_cam12VEFuseAPrimaryIssue` | APSB ECU: w286 cam12 VE fuse a primary issue | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w287_cam12VEFuseASecondaryIssue` | APSB ECU: w287 cam12 VE fuse a secondary issue | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w288_brakeboosterMia` | APSB ECU: w288 brakebooster mia | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w289_turboTemperatureWarning` | APSB ECU: w289 turbo temperature warning | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w290_cam12VBuckBoostBPwrRinging` | APSB ECU: w290 cam12 v buck boost b pwr ringing | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w291_eplannerError` | APSB ECU: w291 eplanner error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w292_CH_busOff` | APSB ECU: w292 CH bus off | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w293_PARTY_busOff` | APSB ECU: w293 PARTY bus off | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w294_VEH_busOff` | APSB ECU: w294 VEH bus off | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w295_PT_busOff` | APSB ECU: w295 PT bus off | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w296_wdogMonTaskDeadlineMiss` | APSB ECU: w296 wdog mon task deadline miss | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w297_earlyWDogAlert` | APSB ECU: w297 early w dog alert | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w298_cpuToApCanSharedMemError` | APSB ECU: w298 cpu to ap can shared mem error | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w299_apToCpuCanSharedMemError` | APSB ECU: w299 ap to cpu can shared mem error | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w300_sharedMemoryAccessError` | APSB ECU: w300 shared memory access error | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w301_nocTimeoutDetected` | APSB ECU: w301 noc timeout detected | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w302_canAPShmFifoFull` | APSB ECU: w302 can AP shm fifo full | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w303_canAPShmFifoEmpty` | APSB ECU: w303 can AP shm fifo empty | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w304_dataAbort` | APSB ECU: w304 data abort | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w305_gpsPgoodFailure` | APSB ECU: w305 gps pgood failure | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w306_ethPgoodFailure` | APSB ECU: w306 eth pgood failure | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w307_eccEventDetected` | APSB ECU: w307 ecc event detected | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w308_pmicErrorDetected` | APSB ECU: w308 pmic error detected | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w309_ethBridgeDown` | APSB ECU: w309 eth bridge down | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w310_wakeBootMetrics` | APSB ECU: w310 wake boot metrics | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w311_apbdgDasMia` | APSB ECU: w311 apbdg das mia | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w312_apbdgApMia` | APSB ECU: w312 apbdg ap mia | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w313_BDY_busOff` | APSB ECU: w313 BDY bus off | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w315_epas3pMiaBdyBus` | APSB ECU: w315 epas3p mia bdy bus | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w316_apBootHealth` | APSB ECU: w316 ap boot health | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w317_uiMia` | APSB ECU: w317 ui mia | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w318_ethernetNetworkBufferHighWatermark` | APSB ECU: w318 ethernet network buffer high watermark | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w319_vehDasImposterDetected` | APSB ECU: w319 veh das imposter detected | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_w320_eplannerPreconditionsMet` | APSB ECU: w320 eplanner preconditions met | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/ModelY/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All APSB ECU messages (APSB)](../../apsb.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
