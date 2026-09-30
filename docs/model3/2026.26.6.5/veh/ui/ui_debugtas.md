---
layout: default
title: "UI_debugTas (0x7FB) — Touchscreen user interface computer, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Touchscreen user interface computer message: debug tas. Tesla Model 3 CAN bus message UI_debugTas (0x7FB) of Touchscreen user interface computer, firmware 2026.26.6.5, 8 signals (UI_debugDampingRequestFLC, UI_debugDampingRequestFLR, UI_debugDampingRequestFRC, UI_debugDampingRequestFRR and 4 more). Bit layout, scaling, units and value tables."
---

# UI_debugTas (0x7FB) — Touchscreen user interface computer, Tesla Model 3 2026.26.6.5 VEH CAN

Touchscreen user interface computer message: debug tas; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 8 signals of UI_debugTas as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_debugTas` |
| CAN id | 0x7FB (2043) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 2000 ms |
| Signals | 8 |

## Signals of UI_debugTas

Tesla Model 3 CAN bus signals in `UI_debugTas`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_debugDampingRequestFLC` | Touchscreen user interface computer: debug damping request FLC; raw 255 = signal not available (SNA) | 0\|8 | little-endian | unsigned | 0.01 | 0 | A | 0 to 2.54 | 255 = `SNA` | plausible |
| `UI_debugDampingRequestFLR` | Touchscreen user interface computer: debug damping request FLR; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.01 | 0 | A | 0 to 2.54 | 255 = `SNA` | plausible |
| `UI_debugDampingRequestFRC` | Touchscreen user interface computer: debug damping request FRC; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.01 | 0 | A | 0 to 2.54 | 255 = `SNA` | plausible |
| `UI_debugDampingRequestFRR` | Touchscreen user interface computer: debug damping request FRR; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.01 | 0 | A | 0 to 2.54 | 255 = `SNA` | plausible |
| `UI_debugDampingRequestRLC` | Touchscreen user interface computer: debug damping request RLC; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.01 | 0 | A | 0 to 2.54 | 255 = `SNA` | plausible |
| `UI_debugDampingRequestRLR` | Touchscreen user interface computer: debug damping request RLR; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.01 | 0 | A | 0 to 2.54 | 255 = `SNA` | plausible |
| `UI_debugDampingRequestRRC` | Touchscreen user interface computer: debug damping request RRC; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 0.01 | 0 | A | 0 to 2.54 | 255 = `SNA` | plausible |
| `UI_debugDampingRequestRRR` | Touchscreen user interface computer: debug damping request RRR; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 0.01 | 0 | A | 0 to 2.54 | 255 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
