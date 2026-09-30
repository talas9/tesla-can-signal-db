---
layout: default
title: "DIF_alertMatrix3 (0x35A) — Front drive inverter, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Front drive inverter message: alert matrix3. Ethernet-side message DIF_alertMatrix3 of Front drive inverter for Tesla Model 3 / Model Y firmware 2025.20.8, 23 signals (DIF_a133_capacitorOT, DIF_a134_wheelSpeedIrrational, DIF_a136_spiError, DIF_a142_highLashAngle and 19 more). Bit layout, scaling, units and value tables."
---

# DIF_alertMatrix3 (0x35A) — Front drive inverter, Tesla Model 3 / Model Y 2025.20.8 ETH

Front drive inverter message: alert matrix3. This page documents the 23 signals of DIF_alertMatrix3 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DIF_alertMatrix3` |
| Ethernet-side id | 0x35A (858) |
| ECU | [Front drive inverter](../../dif.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DIF |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 23 |

## Signals of DIF_alertMatrix3

Tesla Model 3 / Model Y CAN bus signals in `DIF_alertMatrix3`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIF_a133_capacitorOT` | Front drive inverter: a133 capacitor OT | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a134_wheelSpeedIrrational` | Front drive inverter: a134 wheel speed irrational | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a136_spiError` | Front drive inverter: a136 spi error | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a142_highLashAngle` | Front drive inverter: a142 high lash angle | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a144_configMismatch` | Front drive inverter: a144 config mismatch | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a147_highTorqueWearLimit` | Front drive inverter: a147 high torque wear limit | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a148_burnInCycleEnded` | Front drive inverter: a148 burn in cycle ended | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a149_oilPumpFailure` | Front drive inverter: a149 oil pump failure | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a150_busVD` | Front drive inverter: a150 bus VD | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a151_shockTorqueLimiter` | Front drive inverter: a151 shock torque limiter | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a152_linError` | Front drive inverter: a152 lin error | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a153_oilPumpDiagnostics` | Front drive inverter: a153 oil pump diagnostics | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a154_resolver` | Front drive inverter: a154 resolver | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a155_vcfrontMIA` | Front drive inverter: a155 vcfront MIA | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a156_currentObserver` | Front drive inverter: a156 current observer | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a157_rcmMIA` | Front drive inverter: a157 rcm MIA | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a158_ibstMIA` | Front drive inverter: a158 ibst MIA | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a160_busVoltageAnomaly` | Front drive inverter: a160 bus voltage anomaly | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a161_epas3pMIA` | Front drive inverter: a161 epas3p MIA | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a162_endOfLifetimeBurnIn` | Front drive inverter: a162 end of lifetime burn in | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a174_unitMayNotRestart` | Front drive inverter: a174 unit may not restart | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a176_safetyICFault` | Front drive inverter: a176 safety IC fault | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a177_fluxReferenceCorrected` | Front drive inverter: a177 flux reference corrected | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Front drive inverter messages (DIF)](../../dif.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
