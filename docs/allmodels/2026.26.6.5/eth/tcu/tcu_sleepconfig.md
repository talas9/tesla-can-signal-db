---
layout: default
title: "TCU_SleepConfig (0x487) — TCU ECU, Tesla Model 3 / Model Y 2026.26.6.5 ETH"
description: "TCU ECU message: sleep config. Ethernet-side message TCU_SleepConfig of TCU ECU for Tesla Model 3 / Model Y firmware 2026.26.6.5, 1 signals (TCU_tc10Version). Bit layout, scaling, units and value tables."
---

# TCU_SleepConfig (0x487) — TCU ECU, Tesla Model 3 / Model Y 2026.26.6.5 ETH

TCU ECU message: sleep config. This page documents the 1 signals of TCU_SleepConfig as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `TCU_SleepConfig` |
| Ethernet-side id | 0x487 (1159) |
| ECU | [TCU ECU](../../tcu.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | TCU |
| Frame length | 1 bytes |
| Cycle time | 1000 ms |
| Signals | 1 |

## Signals of TCU_SleepConfig

Tesla Model 3 / Model Y CAN bus signals in `TCU_SleepConfig`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `TCU_tc10Version` | Indicates which version of Open Alliance's TC10 protocol is supported by the modem; raw 0 = signal not available (SNA) | 0\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `TCU_tc10Version_DRAFT`<br>2 = `TCU_tc10Version_FINAL_1_0` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/AllModels/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All TCU ECU messages (TCU)](../../tcu.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
