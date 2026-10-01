---
layout: default
title: "UI_systemMonitor (0x295) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 ETH"
description: "Touchscreen user interface computer message: system monitor. Ethernet-side message UI_systemMonitor of Touchscreen user interface computer for Tesla Model Y firmware 2025.20.8, 12 signals (UI_systemMonitorIndex, UI_SystemMemUsage, UI_QtCarMemUsage, UI_QtCarCPUUsage and 8 more). Bit layout, scaling, units and value tables."
---

# UI_systemMonitor (0x295) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 ETH

Touchscreen user interface computer message: system monitor. This page documents the 12 signals of UI_systemMonitor as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_systemMonitor` |
| Ethernet-side id | 0x295 (661) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 8 bytes |
| Cycle time | 15000 ms |
| Signals | 12 |

## Signals of UI_systemMonitor

Tesla Model Y CAN bus signals in `UI_systemMonitor`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `UI_systemMonitorIndex` | selector | Touchscreen user interface computer: system monitor index | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `0`<br>1 = `1` | plausible |
| `UI_SystemMemUsage` | page 0 | Monitors system memory usage | 8\|16 | little-endian | unsigned | 1 | 0 | MB | 0 to 65535 |  | plausible |
| `UI_QtCarMemUsage` | page 0 | Monitors memory usage of the primary User Interface application | 24\|16 | little-endian | unsigned | 1 | 0 | MB | 0 to 65535 |  | plausible |
| `UI_QtCarCPUUsage` | page 0 | Monitors CPU usage of the primary User Interface application | 40\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `UI_emmcStatus` | page 0 | Touchscreen user interface computer: emmc status | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_SystemCPUUsage` | page 0 | Monitors system CPU usage | 48\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `UI_HomeHealth` | page 0 | Touchscreen user interface computer: home health | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_VarHealth` | page 0 | Touchscreen user interface computer: var health | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_LogHealth` | page 0 | Touchscreen user interface computer: log health | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_TmpfsHealth` | page 0 | Touchscreen user interface computer: tmpfs health | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_emmcDataWritten` | page 1 | Touchscreen user interface computer: emmc data written | 8\|24 | little-endian | unsigned | 1 | 0 |  | 0 to 16777215 |  | layout-only |
| `UI_emmcTotalErases` | page 1 | Touchscreen user interface computer: emmc total erases | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |

## Multiplexing

`UI_systemMonitorIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (9 signals), page 1 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
