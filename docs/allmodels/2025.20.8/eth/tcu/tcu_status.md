---
layout: default
title: "TCU_status (0x580) — TCU ECU, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "TCU ECU message: status. Ethernet-side message TCU_status of TCU ECU for Tesla Model 3 / Model Y firmware 2025.20.8, 4 signals (TCU_statusMux, TCU_wakeUpReason, TCU_tcuCmdId, TCU_goingToSleep). Bit layout, scaling, units and value tables."
---

# TCU_status (0x580) — TCU ECU, Tesla Model 3 / Model Y 2025.20.8 ETH

TCU ECU message: status. This page documents the 4 signals of TCU_status as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `TCU_status` |
| Ethernet-side id | 0x580 (1408) |
| ECU | [TCU ECU](../../tcu.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | TCU |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 4 |

## Signals of TCU_status

Tesla Model 3 / Model Y CAN bus signals in `TCU_status`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `TCU_statusMux` | selector | TCU ECU: status mux | 0\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 | 0 = `wakeUpReason`<br>1 = `tcuCmdId`<br>2 = `goingToSleep` | plausible |
| `TCU_wakeUpReason` | page 0 | TCU ECU: wake up reason; raw 4294967295 = signal not available (SNA) | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967294 | 4294967295 = `SNA` | plausible |
| `TCU_tcuCmdId` | page 1 | TCU ECU: tcu cmd id | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU_goingToSleep` | page 2 | TCU ECU: going to sleep; raw 4294967295 = signal not available (SNA) | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967294 | 4294967295 = `SNA` | plausible |

## Multiplexing

`TCU_statusMux` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (1 signals), page 1 (1 signals), page 2 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All TCU ECU messages (TCU)](../../tcu.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
