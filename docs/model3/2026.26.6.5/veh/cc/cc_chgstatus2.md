---
layout: default
title: "CC_chgStatus2 (0x31D) — Charge cable controller, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Charge cable controller message: chg status2. Tesla Model 3 CAN bus message CC_chgStatus2 (0x31D) of Charge cable controller, firmware 2026.26.6.5, 5 signals (CC_chgStatus2Index, CC_buttonState, EVSE_v2xSupport, EVSE_v2xHandshakeStart and 1 more). Bit layout, scaling, units and value tables."
---

# CC_chgStatus2 (0x31D) — Charge cable controller, Tesla Model 3 2026.26.6.5 VEH CAN

Charge cable controller message: chg status2; frame length from the layout, not yet observed on a vehicle bus. This page documents the 5 signals of CC_chgStatus2 as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `CC_chgStatus2` |
| CAN id | 0x31D (797) |
| ECU | [Charge cable controller](../../cc.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | CC |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 5 |

## Signals of CC_chgStatus2

Tesla Model 3 CAN bus signals in `CC_chgStatus2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `CC_chgStatus2Index` | selector | Charge cable controller: chg status2 index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `Mux0` | plausible |
| `CC_buttonState` | page 0 | Charge cable controller: button state | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CC_BUTTON_RELEASED`<br>1 = `CC_BUTTON_PRESSED` | validated |
| `EVSE_v2xSupport` | page 0 | Charge cable controller: v2x support | 9\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `V2X_NOT_SUPPORTED`<br>1 = `V2X_OVER_PLC`<br>2 = `V2X_OVER_SWCAN` | validated |
| `EVSE_v2xHandshakeStart` | page 0 | Charge cable controller: v2x handshake start | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EVSE_v2xSessionType` | page 0 | Charge cable controller: v2x session type; raw 0 = signal not available (SNA) | 13\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SESSION_TYPE_SNA` | validated |

## Multiplexing

`CC_chgStatus2Index` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (4 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Charge cable controller messages (CC)](../../cc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
