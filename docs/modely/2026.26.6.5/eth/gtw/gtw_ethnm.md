---
layout: default
title: "GTW_ethNm (0x438) — Gateway, Tesla Model Y 2026.26.6.5 ETH"
description: "Gateway message: eth nm. Ethernet-side message GTW_ethNm of Gateway for Tesla Model Y firmware 2026.26.6.5, 5 signals (GTW_ethGotoSleep, GTW_ethWakeUpBus, GTW_vehBusAsleep, GTW_ethHeartBeatCounter and 1 more). Bit layout, scaling, units and value tables."
---

# GTW_ethNm (0x438) — Gateway, Tesla Model Y 2026.26.6.5 ETH

Gateway message: eth nm. This page documents the 5 signals of GTW_ethNm as defined for Tesla Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `GTW_ethNm` |
| Ethernet-side id | 0x438 (1080) |
| ECU | [Gateway](../../gtw.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | GTW |
| Frame length | 2 bytes |
| Cycle time | 100 ms |
| Signals | 5 |

## Signals of GTW_ethNm

Tesla Model Y CAN bus signals in `GTW_ethNm`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `GTW_ethGotoSleep` | ETH bus sleep commanded | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `GTW_ethWakeUpBus` | Gateway: eth wake up bus | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `GTW_vehBusAsleep` | VEH bus sleep state | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `GTW_ethHeartBeatCounter` | Gateway: eth heart beat counter | 4\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `GTW_ethWakeUpReason` | Tracks the cause of why the gateway wakes up the ethernet bus | 8\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `GTW_WAKEUP_REASON_NONE`<br>1 = `GTW_WAKEUP_REASON_RESET`<br>2 = `GTW_WAKEUP_REASON_GSM_RI`<br>3 = `GTW_WAKEUP_REASON_CH_CAN`<br>4 = `GTW_WAKEUP_REASON_ETH_CAN`<br>5 = `GTW_WAKEUP_REASON_VEH_CAN`<br>6 = `GTW_WAKEUP_REASON_VCFRONT`<br>7 = `GTW_WAKEUP_REASON_RTC_ALARM`<br>8 = `GTW_WAKEUP_REASON_UI_SCHEDULED`<br>9 = `GTW_WAKEUP_REASON_PT_CAN`<br>10 = `GTW_WAKEUP_REASON_BDY_CAN`<br>11 = `GTW_WAKEUP_REASON_URGENT_TRANSMIT_ALERT`<br>12 = `GTW_WAKEUP_REASON_DISPLAY_TAP`<br>13 = `GTW_WAKEUP_REASON_LOOP`<br>14 = `GTW_WAKEUP_REASON_VCLEFT`<br>15 = `GTW_WAKEUP_REASON_RCMPRIVATE_CAN`<br>16 = `GTW_WAKEUP_REASON_EGGLEFT_LINK_DOWN`<br>17 = `GTW_WAKEUP_REASON_TCU_TC10_VERSION_CHECK` | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/ModelY/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Gateway messages (GTW)](../../gtw.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
