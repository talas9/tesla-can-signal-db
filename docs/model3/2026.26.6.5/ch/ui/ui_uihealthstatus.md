---
layout: default
title: "UI_uiHealthStatus (0x354) — Touchscreen user interface computer, Tesla Model 3 2026.26.6.5 CH CAN"
description: "Touchscreen user interface computer message: ui health status. Tesla Model 3 CAN bus message UI_uiHealthStatus (0x354) of Touchscreen user interface computer, firmware 2026.26.6.5, 22 signals (UI_centerDisplayRunning, UI_centerDisplaySM, UI_centerDisplayPowerOn, UI_centerDisplayCrtcOk and 18 more). Bit layout, scaling, units and value tables."
---

# UI_uiHealthStatus (0x354) — Touchscreen user interface computer, Tesla Model 3 2026.26.6.5 CH CAN

Touchscreen user interface computer message: ui health status; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 22 signals of UI_uiHealthStatus as defined for Tesla Model 3 firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_uiHealthStatus` |
| CAN id | 0x354 (852) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | GTW |
| Frame length | 6 bytes |
| Cycle time | 500 ms |
| Signals | 22 |

## Signals of UI_uiHealthStatus

Tesla Model 3 CAN bus signals in `UI_uiHealthStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_centerDisplayRunning` | is center display running | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_centerDisplaySM` | Touchscreen user interface computer: center display SM | 1\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `START`<br>1 = `UP`<br>2 = `STALLING`<br>3 = `TIMING_OUT`<br>4 = `DOWN` | plausible |
| `UI_centerDisplayPowerOn` | center display power on | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_centerDisplayCrtcOk` | Touchscreen user interface computer: center display crtc ok | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_centerDisplayHardwareOk` | Touchscreen user interface computer: center display hardware ok | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_centerDisplayWindowManagerOk` | Touchscreen user interface computer: center display window manager ok | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_centerDisplayCompositorOk` | Touchscreen user interface computer: center display compositor ok | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_apVisualizationOk` | Touchscreen user interface computer: ap visualization ok | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_autonomyCenterDispStatus` | Touchscreen user interface computer: autonomy center disp status; raw 0 = signal not available (SNA) | 10\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `AVAILABLE`<br>2 = `UNAVAILABLE` | plausible |
| `UI_autonomyRearDispStatus` | Touchscreen user interface computer: autonomy rear disp status; raw 0 = signal not available (SNA) | 12\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `AVAILABLE`<br>2 = `UNAVAILABLE` | plausible |
| `UI_autonomyConnectivityStatus` | Touchscreen user interface computer: autonomy connectivity status; raw 0 = signal not available (SNA) | 14\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `ONLINE`<br>2 = `OFFLINE` | plausible |
| `UI_autonomyConnectivtyHWOk` | Touchscreen user interface computer: autonomy connectivty HW ok | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_autonomyQtCarStatus` | Signal reported by Touchscreen user interface computer; raw 0 = signal not available (SNA) | 17\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `AVAILABLE`<br>2 = `UNAVAILABLE` | plausible |
| `UI_autonomyQtCarRearStatus` | Signal reported by Touchscreen user interface computer; raw 0 = signal not available (SNA) | 19\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `AVAILABLE`<br>2 = `UNAVAILABLE` | plausible |
| `UI_autonomyDASServerStatus` | Touchscreen user interface computer: autonomy DAS server status; raw 0 = signal not available (SNA) | 21\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `AVAILABLE`<br>2 = `UNAVAILABLE` | plausible |
| `UI_rearDisplayRunning` | is rear display running | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_rearDisplayPowerOn` | rear display power on | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_rearDisplaySM` | Touchscreen user interface computer: rear display SM | 25\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `START`<br>1 = `UP`<br>2 = `STALLING`<br>3 = `TIMING_OUT`<br>4 = `DOWN` | plausible |
| `UI_rearDisplayCrtcOk` | Touchscreen user interface computer: rear display crtc ok | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_rearDisplayHardwareOk` | Touchscreen user interface computer: rear display hardware ok | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_rearDisplayWindowManagerOk` | Touchscreen user interface computer: rear display window manager ok | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_rearDisplayCompositorOk` | Touchscreen user interface computer: rear display compositor ok | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 CH DBC file](../../../../../dbc/Model3/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/CH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
