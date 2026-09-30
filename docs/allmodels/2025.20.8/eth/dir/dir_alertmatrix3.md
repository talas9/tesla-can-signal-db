---
layout: default
title: "DIR_alertMatrix3 (0x3C5) — Rear drive inverter, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Rear drive inverter message: alert matrix3. Ethernet-side message DIR_alertMatrix3 of Rear drive inverter for Tesla Model 3 / Model Y firmware 2025.20.8, 24 signals (DIR_a133_capacitorOT, DIR_a134_wheelSpeedIrrational, DIR_a136_spiError, DIR_a142_highLashAngle and 20 more). Bit layout, scaling, units and value tables."
---

# DIR_alertMatrix3 (0x3C5) — Rear drive inverter, Tesla Model 3 / Model Y 2025.20.8 ETH

Rear drive inverter message: alert matrix3. This page documents the 24 signals of DIR_alertMatrix3 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DIR_alertMatrix3` |
| Ethernet-side id | 0x3C5 (965) |
| ECU | [Rear drive inverter](../../dir.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DIR |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 24 |

## Signals of DIR_alertMatrix3

Tesla Model 3 / Model Y CAN bus signals in `DIR_alertMatrix3`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIR_a133_capacitorOT` | Rear drive inverter: a133 capacitor OT | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a134_wheelSpeedIrrational` | Rear drive inverter: a134 wheel speed irrational | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a136_spiError` | Rear drive inverter: a136 spi error | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a142_highLashAngle` | Rear drive inverter: a142 high lash angle | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a144_configMismatch` | Rear drive inverter: a144 config mismatch | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a147_highTorqueWearLimit` | Rear drive inverter: a147 high torque wear limit | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a148_burnInCycleEnded` | Rear drive inverter: a148 burn in cycle ended | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a149_oilPumpFailure` | Rear drive inverter: a149 oil pump failure | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a150_busVD` | Rear drive inverter: a150 bus VD | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a151_shockTorqueLimiter` | Rear drive inverter: a151 shock torque limiter | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a152_linError` | Rear drive inverter: a152 lin error | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a153_oilPumpDiagnostics` | Rear drive inverter: a153 oil pump diagnostics | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a154_resolver` | Rear drive inverter: a154 resolver | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a155_vcfrontMIA` | Rear drive inverter: a155 vcfront MIA | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a156_currentObserver` | Rear drive inverter: a156 current observer | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a157_rcmMIA` | Rear drive inverter: a157 rcm MIA | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a158_ibstMIA` | Rear drive inverter: a158 ibst MIA | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a160_busVoltageAnomaly` | Rear drive inverter: a160 bus voltage anomaly | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a161_epas3pMIA` | Rear drive inverter: a161 epas3p MIA | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a162_endOfLifetimeBurnIn` | Rear drive inverter: a162 end of lifetime burn in | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a174_unitMayNotRestart` | Rear drive inverter: a174 unit may not restart | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a176_safetyICFault` | Rear drive inverter: a176 safety IC fault | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a177_fluxReferenceCorrected` | Rear drive inverter: a177 flux reference corrected | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a178_spindownLearningBrakeAllowed` | Rear drive inverter: a178 spindown learning brake allowed | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Rear drive inverter messages (DIR)](../../dir.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
