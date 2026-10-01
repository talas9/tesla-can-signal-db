---
layout: default
title: "GTW_hrl (0x7F1) — Gateway, Tesla Model Y 2025.20.8 ETH"
description: "Gateway message: hrl. Ethernet-side message GTW_hrl of Gateway for Tesla Model Y firmware 2025.20.8, 6 signals (GTW_hrlIndex, GTW_hrlState, GTW_hrlTriggerDuration, GTW_hrlTriggerType and 2 more). Bit layout, scaling, units and value tables."
---

# GTW_hrl (0x7F1) — Gateway, Tesla Model Y 2025.20.8 ETH

Gateway message: hrl. This page documents the 6 signals of GTW_hrl as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `GTW_hrl` |
| Ethernet-side id | 0x7F1 (2033) |
| ECU | [Gateway](../../gtw.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | GTW |
| Frame length | 7 bytes |
| Cycle time | 2000 ms |
| Signals | 6 |

## Signals of GTW_hrl

Tesla Model Y CAN bus signals in `GTW_hrl`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `GTW_hrlIndex` | selector | Gateway: hrl index | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 1 = `Mux1`<br>2 = `Mux2` | plausible |
| `GTW_hrlState` | page 2 | GTW hrl state | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | plausible |
| `GTW_hrlTriggerDuration` | page 2 | HRL duration | 15\|16 | big-endian | unsigned | 1 | 0 | seconds | 0 to 65535 |  | plausible |
| `GTW_hrlTriggerType` | page 2 | HRL trigger type | 24\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `HRL_TRIGGER_UDPAPI`<br>1 = `HRL_TRIGGER_EVENT`<br>2 = `HRL_TRIGGER_GAME_MODE`<br>3 = `HRL_TRIGGER_CONTINUOUS`<br>4 = `HRL_TRIGGER_PSEUDONYMOUS`<br>5 = `HRL_TRIGGER_EVENT_EXTERNAL`<br>15 = `HRL_TRIGGER_NONE` | plausible |
| `GTW_hrlTriggerId` | page 2 | HRL trigger ID. A unique ID representing the signal conditions causing the HRL event to occur. | 39\|16 | big-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | plausible |
| `GTW_hrlTriggerBus` | page 2 | Gateway: hrl trigger bus | 53\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |

## Multiplexing

`GTW_hrlIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 2 (5 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Gateway messages (GTW)](../../gtw.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
