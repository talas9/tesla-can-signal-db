---
layout: default
title: "ADSP_audioVisualizer (0x79F) — Audio amplifier, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Audio amplifier message: audio visualizer. Tesla Model 3 / Model Y CAN bus message ADSP_audioVisualizer (0x79F) of Audio amplifier, firmware 2026.26.6.5, 1 signals (ADSP_audioVisualizerBrightness). Bit layout, scaling, units and value tables."
---

# ADSP_audioVisualizer (0x79F) — Audio amplifier, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Audio amplifier message: audio visualizer; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of ADSP_audioVisualizer as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `ADSP_audioVisualizer` |
| CAN id | 0x79F (1951) |
| ECU | [Audio amplifier](../../adsp.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 1 bytes |
| Cycle time | 20 ms |
| Signals | 1 |

## Signals of ADSP_audioVisualizer

Tesla Model 3 / Model Y CAN bus signals in `ADSP_audioVisualizer`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `ADSP_audioVisualizerBrightness` | Audio amplifier: audio visualizer brightness | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Audio amplifier messages (ADSP)](../../adsp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
