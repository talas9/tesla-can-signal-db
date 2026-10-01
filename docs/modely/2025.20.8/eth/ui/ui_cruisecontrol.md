---
layout: default
title: "UI_cruiseControl (0x213) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 ETH"
description: "Touchscreen user interface computer message: cruise control. Ethernet-side message UI_cruiseControl of Touchscreen user interface computer for Tesla Model Y firmware 2025.20.8, 4 signals (UI_cruiseSpeedCommand, UI_smartSummonRequest, UI_cruiseControlCounter, UI_cruiseControlChecksum). Bit layout, scaling, units and value tables."
---

# UI_cruiseControl (0x213) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 ETH

Touchscreen user interface computer message: cruise control. This page documents the 4 signals of UI_cruiseControl as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_cruiseControl` |
| Ethernet-side id | 0x213 (531) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 2 bytes |
| Cycle time | 500 ms |
| Signals | 4 |

## Signals of UI_cruiseControl

Tesla Model Y CAN bus signals in `UI_cruiseControl`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_cruiseSpeedCommand` | User command to change the cruise set speed. | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CRUISE_SPEED_IDLE`<br>1 = `CRUISE_SPEED_INC_SHORT`<br>2 = `CRUISE_SPEED_INC_LONG`<br>3 = `CRUISE_SPEED_DEC_SHORT`<br>4 = `CRUISE_SPEED_DEC_LONG`<br>5 = `CRUISE_SPEED_SNAP`<br>6 = `CRUISE_SPEED_SNAP_SPEEDO` | plausible |
| `UI_smartSummonRequest` | Touchscreen user interface computer: smart summon request | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_cruiseControlCounter` | Touchscreen user interface computer: cruise control counter | 4\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | plausible |
| `UI_cruiseControlChecksum` | Touchscreen user interface computer: cruise control checksum | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
