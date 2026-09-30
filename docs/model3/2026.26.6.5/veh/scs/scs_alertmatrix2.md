---
layout: default
title: "SCS_alertMatrix2 (0x370) — SCS ECU, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "SCS ECU message: alert matrix2. Tesla Model 3 CAN bus message SCS_alertMatrix2 (0x370) of SCS ECU, firmware 2026.26.6.5, 64 signals (SCS_a065_vBatRationalityStage1, SCS_a066_vBatRationalityStage2, SCS_a067_vBatRationalityStage3, SCS_a068_vBatRationalityStage4 and 60 more). Bit layout, scaling, units and value tables."
---

# SCS_alertMatrix2 (0x370) — SCS ECU, Tesla Model 3 2026.26.6.5 VEH CAN

SCS ECU message: alert matrix2; frame length from the layout, not yet observed on a vehicle bus. This page documents the 64 signals of SCS_alertMatrix2 as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `SCS_alertMatrix2` |
| CAN id | 0x370 (880) |
| ECU | [SCS ECU](../../scs.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | SCS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 64 |

## Signals of SCS_alertMatrix2

Tesla Model 3 CAN bus signals in `SCS_alertMatrix2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `SCS_a065_vBatRationalityStage1` | SCS ECU: a065 v bat rationality stage1 | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a066_vBatRationalityStage2` | SCS ECU: a066 v bat rationality stage2 | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a067_vBatRationalityStage3` | SCS ECU: a067 v bat rationality stage3 | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a068_vBatRationalityStage4` | SCS ECU: a068 v bat rationality stage4 | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a069_vStageRationalityV1` | SCS ECU: a069 v stage rationality V1 | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a070_vStageRationalityV2` | SCS ECU: a070 v stage rationality V2 | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a071_chargerMIA` | SCS ECU: a071 charger MIA | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a072_gtwMIA` | SCS ECU: a072 gtw MIA | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a073_lccMIA` | SCS ECU: a073 lcc MIA | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a074_isoVDiffHi` | SCS ECU: a074 iso v diff hi | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a075_unused75` | SCS ECU: a075 unused75 | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a076_bmsMIA` | SCS ECU: a076 bms MIA | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a077_unexpectedVbatBehavior` | SCS ECU: a077 unexpected vbat behavior | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a078_voltageMatchTimeout` | SCS ECU: a078 voltage match timeout | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a079_unexpectedVbat` | SCS ECU: a079 unexpected vbat | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a080_lccFaulted` | SCS ECU: a080 lcc faulted | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a081_rmsInputVoltageHigh` | SCS ECU: a081 rms input voltage high | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a082_VbatUV` | SCS ECU: a082 vbat UV | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a083_chargeCurrentLimited` | SCS ECU: a083 charge current limited | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a084_unused84` | SCS ECU: a084 unused84 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a085_unused85` | SCS ECU: a085 unused85 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a086_lccResetDetected` | SCS ECU: a086 lcc reset detected | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a087_posCordTempRationality` | SCS ECU: a087 pos cord temp rationality | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a088_negCordTempRationality` | SCS ECU: a088 neg cord temp rationality | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a089_posCordOT` | SCS ECU: a089 pos cord OT | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a090_negCordOT` | SCS ECU: a090 neg cord OT | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a091_voltageRiseDetection` | SCS ECU: a091 voltage rise detection | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a092_cabEnableDeasserted` | SCS ECU: a092 cab enable deasserted | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a093_unused93` | SCS ECU: a093 unused93 | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a094_unused94` | SCS ECU: a094 unused94 | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a095_unused95` | SCS ECU: a095 unused95 | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a096_unused96` | SCS ECU: a096 unused96 | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a097_unused97` | SCS ECU: a097 unused97 | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a098_unused98` | SCS ECU: a098 unused98 | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a099_unused99` | SCS ECU: a099 unused99 | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a100_unused100` | SCS ECU: a100 unused100 | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a101_unused101` | SCS ECU: a101 unused101 | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a102_unused102` | SCS ECU: a102 unused102 | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a103_unused103` | SCS ECU: a103 unused103 | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a104_unused104` | SCS ECU: a104 unused104 | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a105_unused105` | SCS ECU: a105 unused105 | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a106_unused106` | SCS ECU: a106 unused106 | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a107_unused107` | SCS ECU: a107 unused107 | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a108_unused108` | SCS ECU: a108 unused108 | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a109_unused109` | SCS ECU: a109 unused109 | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a110_unused110` | SCS ECU: a110 unused110 | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a111_unused111` | SCS ECU: a111 unused111 | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a112_unused112` | SCS ECU: a112 unused112 | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a113_unused113` | SCS ECU: a113 unused113 | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a114_unused114` | SCS ECU: a114 unused114 | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a115_unused115` | SCS ECU: a115 unused115 | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a116_unused116` | SCS ECU: a116 unused116 | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a117_unused117` | SCS ECU: a117 unused117 | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a118_unused118` | SCS ECU: a118 unused118 | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a119_unused119` | SCS ECU: a119 unused119 | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a120_unused120` | SCS ECU: a120 unused120 | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a121_unused121` | SCS ECU: a121 unused121 | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a122_unused122` | SCS ECU: a122 unused122 | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a123_unused123` | SCS ECU: a123 unused123 | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a124_unused124` | SCS ECU: a124 unused124 | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a125_unused125` | SCS ECU: a125 unused125 | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a126_unused126` | SCS ECU: a126 unused126 | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a127_unused127` | SCS ECU: a127 unused127 | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `SCS_a128_unused128` | SCS ECU: a128 unused128 | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All SCS ECU messages (SCS)](../../scs.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
