---
layout: default
title: "CC_chgStatus2 (0x31D) — Charge cable controller, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Charge cable controller message: chg status2. Ethernet-side message CC_chgStatus2 of Charge cable controller for Tesla Model 3 / Model Y firmware 2025.20.8, 2 signals (CC_chgStatus2Index, CC_buttonState). Bit layout, scaling, units and value tables."
---

# CC_chgStatus2 (0x31D) — Charge cable controller, Tesla Model 3 / Model Y 2025.20.8 ETH

Charge cable controller message: chg status2. This page documents the 2 signals of CC_chgStatus2 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `CC_chgStatus2` |
| Ethernet-side id | 0x31D (797) |
| ECU | [Charge cable controller](../../cc.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | CC |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 2 |

## Signals of CC_chgStatus2

Tesla Model 3 / Model Y CAN bus signals in `CC_chgStatus2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `CC_chgStatus2Index` | selector | Charge cable controller: chg status2 index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `Mux0` | plausible |
| `CC_buttonState` | page 0 | Charge cable controller: button state | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CC_BUTTON_RELEASED`<br>1 = `CC_BUTTON_PRESSED` | plausible |

## Multiplexing

`CC_chgStatus2Index` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Charge cable controller messages (CC)](../../cc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
