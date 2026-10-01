---
layout: default
title: "UI_stalklessHealthStatus (0x2BB) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 ETH"
description: "Touchscreen user interface computer message: stalkless health status. Ethernet-side message UI_stalklessHealthStatus of Touchscreen user interface computer for Tesla Model 3 firmware 2025.20.8, 7 signals (UI_centerDisplayRunning, UI_centerDisplaySM, UI_centerDisplayPowerOn, UI_centerDisplayCrtcOk and 3 more). Bit layout, scaling, units and value tables."
---

# UI_stalklessHealthStatus (0x2BB) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 ETH

Touchscreen user interface computer message: stalkless health status. This page documents the 7 signals of UI_stalklessHealthStatus as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_stalklessHealthStatus` |
| Ethernet-side id | 0x2BB (699) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 2 bytes |
| Cycle time | 500 ms |
| Signals | 7 |

## Signals of UI_stalklessHealthStatus

Tesla Model 3 CAN bus signals in `UI_stalklessHealthStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_centerDisplayRunning` | is center display running | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_centerDisplaySM` | Touchscreen user interface computer: center display SM | 1\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `START`<br>1 = `UP`<br>2 = `STALLING`<br>3 = `TIMING_OUT`<br>4 = `DOWN` | plausible |
| `UI_centerDisplayPowerOn` | center display power on | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_centerDisplayCrtcOk` | Touchscreen user interface computer: center display crtc ok | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_centerDisplayHardwareOk` | Touchscreen user interface computer: center display hardware ok | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_centerDisplayWindowManagerOk` | Touchscreen user interface computer: center display window manager ok | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_centerDisplayCompositorOk` | Touchscreen user interface computer: center display compositor ok | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
