---
layout: default
title: "FC_alertMatrix3 (0x37F) — FC ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "FC ECU message: alert matrix3. Tesla Model 3 / Model Y CAN bus message FC_alertMatrix3 (0x37F) of FC ECU, firmware 2026.26.6.5, 59 signals (FC_a129_CA_flyback_HW_OC, FC_a130_CA_flyback_SW_OV, FC_a131_CA_flyback_HW_OV, FC_a132_CA_bmsMia and 55 more). Bit layout, scaling, units and value tables."
---

# FC_alertMatrix3 (0x37F) — FC ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

FC ECU message: alert matrix3; frame length from the layout, not yet observed on a vehicle bus. This page documents the 59 signals of FC_alertMatrix3 as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `FC_alertMatrix3` |
| CAN id | 0x37F (895) |
| ECU | [FC ECU](../../fc.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | FC |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 59 |

## Signals of FC_alertMatrix3

Tesla Model 3 / Model Y CAN bus signals in `FC_alertMatrix3`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `FC_a129_CA_flyback_HW_OC` | FC ECU: a129 CA flyback HW OC | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a130_CA_flyback_SW_OV` | FC ECU: a130 CA flyback SW OV | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a131_CA_flyback_HW_OV` | FC ECU: a131 CA flyback HW OV | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a132_CA_bmsMia` | FC ECU: a132 CA bms mia | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a133_CA_evseMia` | FC ECU: a133 CA evse mia | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a134_CA_vehTxBufOvf` | FC ECU: a134 CA veh tx buf ovf | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a135_CA_vehRxBufOvf` | FC ECU: a135 CA veh rx buf ovf | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a136_CA_evseTxBufOvf` | FC ECU: a136 CA evse tx buf ovf | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a137_CA_evseRxBufOvf` | FC ECU: a137 CA evse rx buf ovf | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a138_CA_hwProxTrip` | FC ECU: a138 CA hw prox trip | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a139_CA_ss2NotLow` | FC ECU: a139 CA ss2 not low | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a140_CA_bmsIncompatible` | FC ECU: a140 CA bms incompatible | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a141_CA_vehConn_OT` | FC ECU: a141 CA veh conn OT | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a142_CA_evseConn_OT` | FC ECU: a142 CA evse conn OT | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a143_CA_pcb_OT` | FC ECU: a143 CA pcb OT | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a144_CA_flybackUnstable` | FC ECU: a144 CA flyback unstable | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a145_CA_flybackDataStale` | FC ECU: a145 CA flyback data stale | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a146_CA_flybackBusLoadHi` | FC ECU: a146 CA flyback bus load hi | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a147_CA_vehConn_UT` | FC ECU: a147 CA veh conn UT | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a148_CA_evseConn_UT` | FC ECU: a148 CA evse conn UT | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a149_CA_pcb_UT` | FC ECU: a149 CA pcb UT | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a150_CA_vehToEvseDeltaHi` | FC ECU: a150 CA veh to evse delta hi | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a151_CA_vehToEvseDeltaLo` | FC ECU: a151 CA veh to evse delta lo | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a152_CA_vehToPcbDeltaHi` | FC ECU: a152 CA veh to pcb delta hi | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a153_CA_evseToPcbDeltaHi` | FC ECU: a153 CA evse to pcb delta hi | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a154_CA_vehToPcbDeltaLo` | FC ECU: a154 CA veh to pcb delta lo | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a155_CA_evseToPcbDeltaLo` | FC ECU: a155 CA evse to pcb delta lo | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a156_CA_flybackRunTimeout` | FC ECU: a156 CA flyback run timeout | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a157_CA_unused` | FC ECU: a157 CA unused | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a158_CA_evseOverCurrent` | FC ECU: a158 CA evse over current | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a159_CA_wdtExpired` | FC ECU: a159 CA wdt expired | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a160_CA_ss2Deasserted` | FC ECU: a160 CA ss2 deasserted | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a161_CA_vehTempHiFoldBk` | FC ECU: a161 CA veh temp hi fold bk | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a162_CA_evseTempHiFoldBk` | FC ECU: a162 CA evse temp hi fold bk | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a163_CA_pcbTempHiFoldBk` | FC ECU: a163 CA pcb temp hi fold bk | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a164_CA_proxDisconnected` | FC ECU: a164 CA prox disconnected | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a165_CA_evseConnUnlocked` | FC ECU: a165 CA evse conn unlocked | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a166_CA_vehConnUnlocked` | FC ECU: a166 CA veh conn unlocked | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a167_CA_isoVoltageLow` | FC ECU: a167 CA iso voltage low | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a168_CA_proxTimeout` | FC ECU: a168 CA prox timeout | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a169_CA_pilotAcceptTimeout` | FC ECU: a169 CA pilot accept timeout | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a170_CA_vehDataTimeout` | FC ECU: a170 CA veh data timeout | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a171_CA_vehConLockTimeout` | FC ECU: a171 CA veh con lock timeout | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a172_CA_ss2LowTimeout` | FC ECU: a172 CA ss2 low timeout | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a173_CA_evseDataTimeout` | FC ECU: a173 CA evse data timeout | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a174_CA_vehReadyTimeout` | FC ECU: a174 CA veh ready timeout | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a175_CA_evseIsoTestTimeout` | FC ECU: a175 CA evse iso test timeout | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a176_CA_chargingBusTimeout` | FC ECU: a176 CA charging bus timeout | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a177_CA_bmsCtrCloseTimeout` | FC ECU: a177 CA bms ctr close timeout | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a178_CA_evseStartTimeout` | FC ECU: a178 CA evse start timeout | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a179_CA_startupProblem` | FC ECU: a179 CA startup problem | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a180_CA_chargingProblem` | FC ECU: a180 CA charging problem | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a181_CA_vRegBrownout` | FC ECU: a181 CA v reg brownout | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a182_CA_evseChrMalfunc` | FC ECU: a182 CA evse chr malfunc | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a183_CA_evseBatIncompat` | FC ECU: a183 CA evse bat incompat | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a184_CA_evseBatMalfunc` | FC ECU: a184 CA evse bat malfunc | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a185_CA_vehReadyDeasserted` | FC ECU: a185 CA veh ready deasserted | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a186_CA_fcContOpenTimeout` | FC ECU: a186 CA fc cont open timeout | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a187_CA_evseConLockTimeout` | FC ECU: a187 CA evse con lock timeout | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All FC ECU messages (FC)](../../fc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
