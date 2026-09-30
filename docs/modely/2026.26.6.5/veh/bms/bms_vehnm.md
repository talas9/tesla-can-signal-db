---
layout: default
title: "BMS_vehNm (0x2F2) — High-voltage battery management system, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "High-voltage battery management system message: veh nm. Tesla Model Y CAN bus message BMS_vehNm (0x2F2) of High-voltage battery management system, firmware 2026.26.6.5, 5 signals (BMS_nmGoingToSleep, BMS_nmWakeUpBus, BMS_hvsBusAsleep, BMS_nmKeepAwakeReason and 1 more). Bit layout, scaling, units and value tables."
---

# BMS_vehNm (0x2F2) — High-voltage battery management system, Tesla Model Y 2026.26.6.5 VEH CAN

High-voltage battery management system message: veh nm; frame length from the layout, not yet observed on a vehicle bus. This page documents the 5 signals of BMS_vehNm as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_vehNm` |
| CAN id | 0x2F2 (754) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | BMS |
| Frame length | 2 bytes |
| Cycle time | 100 ms |
| Signals | 5 |

## Signals of BMS_vehNm

Tesla Model Y CAN bus signals in `BMS_vehNm`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_nmGoingToSleep` | High-voltage battery management system: nm going to sleep | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_nmWakeUpBus` | High-voltage battery management system: nm wake up bus | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_hvsBusAsleep` | HVS bus reported as off | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_nmKeepAwakeReason` | BMS' determined reason to keep CAN awake; raw 0 = signal not available (SNA) | 4\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `BMS_KEEPAWAKE_REASON_NONE_SNA`<br>1 = `BMS_KEEPAWAKE_REASON_CTRS_CLOSED`<br>2 = `BMS_KEEPAWAKE_REASON_CRITICAL_ALERT`<br>3 = `BMS_KEEPAWAKE_REASON_FC_CTR_CLEANING`<br>4 = `BMS_KEEPAWAKE_REASON_HVP_ACTIVE`<br>5 = `BMS_KEEPAWAKE_REASON_BMS_ACTIVE`<br>6 = `BMS_KEEPAWAKE_REASON_CP_ACTIVE`<br>7 = `BMS_KEEPAWAKE_REASON_PRECONDITIONING`<br>8 = `BMS_KEEPAWAKE_REASON_OTA` | validated |
| `BMS_nmWakeUpReason` | BMS' determined reason to wake up CAN | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `BMS_WAKEUP_REASON_NONE`<br>1 = `BMS_WAKEUP_REASON_CAN_VEH`<br>2 = `BMS_WAKEUP_REASON_CAN_HVS`<br>3 = `BMS_WAKEUP_REASON_WANTTOCHARGE`<br>4 = `BMS_WAKEUP_REASON_CRITICALALERT` | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
