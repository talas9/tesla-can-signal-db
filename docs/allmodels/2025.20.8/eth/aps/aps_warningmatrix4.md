---
layout: default
title: "APS_warningMatrix4 (0x310) — Driver assistance computer (secondary), Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Driver assistance computer (secondary) message: warning matrix4. Ethernet-side message APS_warningMatrix4 of Driver assistance computer (secondary) for Tesla Model 3 / Model Y firmware 2025.20.8, 33 signals (APS_w257_assertFailure, APS_w258_qspiFlashSectorChecksumMismatch, APS_w259_qspiFailure, APS_w260_pgoodFailure and 29 more). Bit layout, scaling, units and value tables."
---

# APS_warningMatrix4 (0x310) — Driver assistance computer (secondary), Tesla Model 3 / Model Y 2025.20.8 ETH

Driver assistance computer (secondary) message: warning matrix4. This page documents the 33 signals of APS_warningMatrix4 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `APS_warningMatrix4` |
| Ethernet-side id | 0x310 (784) |
| ECU | [Driver assistance computer (secondary)](../../aps.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | APS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 33 |

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
| `APS_w284_cam12VBuckBoostAPwrIssue` | Driver assistance computer (secondary): w284 cam12 v buck boost a pwr issue | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w285_cam12VBuckBoostBPwrIssue` | Driver assistance computer (secondary): w285 cam12 v buck boost b pwr issue | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w286_cam12VEFuseAPrimaryIssue` | Driver assistance computer (secondary): w286 cam12 VE fuse a primary issue | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w287_cam12VEFuseASecondaryIssue` | Driver assistance computer (secondary): w287 cam12 VE fuse a secondary issue | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w288_brakeboosterMia` | Driver assistance computer (secondary): w288 brakebooster mia | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w289_turboTemperatureWarning` | Driver assistance computer (secondary): w289 turbo temperature warning | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APS_w290_cam12VBuckBoostBPwrRinging` | Driver assistance computer (secondary): w290 cam12 v buck boost b pwr ringing | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Driver assistance computer (secondary) messages (APS)](../../aps.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
