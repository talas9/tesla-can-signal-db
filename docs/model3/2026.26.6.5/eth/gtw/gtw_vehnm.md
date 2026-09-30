---
layout: default
title: "GTW_vehNm (0x458) — Gateway, Tesla Model 3 2026.26.6.5 ETH"
description: "Gateway message: veh nm. Ethernet-side message GTW_vehNm of Gateway for Tesla Model 3 firmware 2026.26.6.5, 11 signals (GTW_nmGoingToSleep, GTW_nmWakeUpBus, GTW_chBusAsleep, GTW_ethBusAsleep and 7 more). Bit layout, scaling, units and value tables."
---

# GTW_vehNm (0x458) — Gateway, Tesla Model 3 2026.26.6.5 ETH

Gateway message: veh nm. This page documents the 11 signals of GTW_vehNm as defined for Tesla Model 3 firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `GTW_vehNm` |
| Ethernet-side id | 0x458 (1112) |
| ECU | [Gateway](../../gtw.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | GTW |
| Frame length | 7 bytes |
| Cycle time | 100 ms |
| Signals | 11 |

## Signals of GTW_vehNm

Tesla Model 3 CAN bus signals in `GTW_vehNm`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `GTW_nmGoingToSleep` | Network management - Going to sleep state | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `GTW_nmWakeUpBus` | Gateway: nm wake up bus | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `GTW_chBusAsleep` | Chassis bus sleep state | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `GTW_ethBusAsleep` | ETH bus sleep state | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `GTW_nmKeepAwakeReason` | Network management - Keep awake reason; raw 0 = signal not available (SNA) | 4\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `GTW_KEEPAWAKE_REASON_NONE_SNA`<br>1 = `GTW_KEEPAWAKE_REASON_UI_SCHEDULED`<br>2 = `GTW_KEEPAWAKE_REASON_GSM_RI`<br>3 = `GTW_KEEPAWAKE_REASON_FCSM_ACTIVE`<br>4 = `GTW_KEEPAWAKE_REASON_URGENT_TRANSMIT_ALERT`<br>5 = `GTW_KEEPAWAKE_REASON_EGGLEFT_LINK_DOWN`<br>6 = `GTW_KEEPAWAKE_REASON_TCU_TC10_VERSION_CHECK`<br>7 = `GTW_KEEPAWAKE_REASON_TCU_TC10_VERSION_UNSUPPORTED`<br>15 = `GTW_KEEPAWAKE_REASON_TBD` | validated |
| `GTW_nmWakeUpReason` | Network management - Wakeup reason | 8\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `GTW_WAKEUP_REASON_NONE`<br>1 = `GTW_WAKEUP_REASON_RESET`<br>2 = `GTW_WAKEUP_REASON_GSM_RI`<br>3 = `GTW_WAKEUP_REASON_CH_CAN`<br>4 = `GTW_WAKEUP_REASON_ETH_CAN`<br>5 = `GTW_WAKEUP_REASON_VEH_CAN`<br>6 = `GTW_WAKEUP_REASON_VCFRONT`<br>7 = `GTW_WAKEUP_REASON_RTC_ALARM`<br>8 = `GTW_WAKEUP_REASON_UI_SCHEDULED`<br>9 = `GTW_WAKEUP_REASON_PT_CAN`<br>10 = `GTW_WAKEUP_REASON_BDY_CAN`<br>11 = `GTW_WAKEUP_REASON_URGENT_TRANSMIT_ALERT`<br>12 = `GTW_WAKEUP_REASON_DISPLAY_TAP`<br>13 = `GTW_WAKEUP_REASON_LOOP`<br>14 = `GTW_WAKEUP_REASON_VCLEFT`<br>15 = `GTW_WAKEUP_REASON_RCMPRIVATE_CAN`<br>16 = `GTW_WAKEUP_REASON_EGGLEFT_LINK_DOWN`<br>17 = `GTW_WAKEUP_REASON_TCU_TC10_VERSION_CHECK` | validated |
| `GTW_ethKeepAwakeReason` | Reason GTW is keeping ETH bus awake; raw 0 = signal not available (SNA) | 13\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `NONE_SNA`<br>1 = `URGENT_TRANSMIT_ALERT`<br>2 = `TCU_TC10_VERSION_CHECK`<br>3 = `TCU_TC10_VERSION_UNSUPPORTED` | validated |
| `GTW_nmDebugWakeUp` | Gateway: nm debug wake up | 17\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 | 0 = `WKPU_NONE`<br>1 = `WKPU_0`<br>2 = `WKPU_1`<br>4 = `WKPU_2`<br>8 = `WKPU_3`<br>16 = `WKPU_4`<br>32 = `WKPU_5`<br>64 = `WKPU_6`<br>128 = `WKPU_7`<br>256 = `WKPU_8`<br>512 = `WKPU_9`<br>1024 = `WKPU_10`<br>2048 = `WKPU_11`<br>4096 = `WKPU_12`<br>8192 = `WKPU_13`<br>16384 = `WKPU_14`<br>32768 = `WKPU_15`<br>65536 = `WKPU_16`<br>131072 = `WKPU_17`<br>262144 = `WKPU_18`<br>524288 = `WKPU_19`<br>1048576 = `WKPU_20`<br>2097152 = `WKPU_21`<br>4194304 = `WKPU_22`<br>8388608 = `WKPU_23`<br>16777216 = `WKPU_24`<br>33554432 = `WKPU_25`<br>67108864 = `WKPU_26`<br>134217728 = `WKPU_27`<br>268435456 = `WKPU_28`<br>536870912 = `WKPU_29`<br>1073741824 = `WKPU_30`<br>2147483648 = `WKPU_31` | validated |
| `GTW_OTAKeepAwake` | Signals that the vehicle buses should remain awake for an ongoing OTA update | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `GTW_smsPokeReceived` | The modem indicated it received an SMS poke | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `GTW_bdyBusAsleep` | BDY bus sleep state | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 ETH DBC file](../../../../../dbc/Model3/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Gateway messages (GTW)](../../gtw.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
