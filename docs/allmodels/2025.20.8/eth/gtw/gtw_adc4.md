---
layout: default
title: "GTW_adc4 (0x11A) — Gateway, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Gateway message: adc4. Ethernet-side message GTW_adc4 of Gateway for Tesla Model 3 / Model Y firmware 2025.20.8, 5 signals (GTW_BKP_BATT_MON, GTW_BKP_BATT_NTC_P, GTW_ECALL_GPS_ANT_BIAS, GTW_ECALL_MIC_DIAG and 1 more). Bit layout, scaling, units and value tables."
---

# GTW_adc4 (0x11A) — Gateway, Tesla Model 3 / Model Y 2025.20.8 ETH

Gateway message: adc4. This page documents the 5 signals of GTW_adc4 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `GTW_adc4` |
| Ethernet-side id | 0x11A (282) |
| ECU | [Gateway](../../gtw.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 5 |

## Signals of GTW_adc4

Tesla Model 3 / Model Y CAN bus signals in `GTW_adc4`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `GTW_BKP_BATT_MON` | Gateway: BKP BATT MON; raw 4095 = signal not available (SNA) | 7\|12 | big-endian | unsigned | 1 | 0 | mV | 0 to 4094 | 4095 = `SNA` | plausible |
| `GTW_BKP_BATT_NTC_P` | BKP_BATT_NTC_P pni voltage; raw 4095 = signal not available (SNA) | 11\|12 | big-endian | unsigned | 1 | 0 | mV | 0 to 4094 | 4095 = `SNA` | plausible |
| `GTW_ECALL_GPS_ANT_BIAS` | Gateway: ECALL GPS ANT BIAS; raw 4095 = signal not available (SNA) | 31\|12 | big-endian | unsigned | 1 | 0 | mV | 0 to 4094 | 4095 = `SNA` | plausible |
| `GTW_ECALL_MIC_DIAG` | ECALL_MIC_DIAG voltage; raw 4095 = signal not available (SNA) | 35\|12 | big-endian | unsigned | 1 | 0 | mV | 0 to 4094 | 4095 = `SNA` | plausible |
| `GTW_SOS_ECALL_nRQST_BUF` | SOS_ECALL_nRQST_BUF voltage; raw 4095 = signal not available (SNA) | 55\|12 | big-endian | unsigned | 1 | 0 | mV | 0 to 4094 | 4095 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Gateway messages (GTW)](../../gtw.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
