---
layout: default
title: "APS_eacMonitor (0x27D) — Driver assistance computer (secondary), Tesla Model 3 2025.20.8 CH CAN"
description: "Driver assistance computer (secondary) message: eac monitor. Tesla Model 3 CAN bus message APS_eacMonitor (0x27D) of Driver assistance computer (secondary), firmware 2025.20.8, 3 signals (APS_eacAllow, APS_eacMonitorCounter, APS_eacMonitorChecksum). Bit layout, scaling, units and value tables."
---

# APS_eacMonitor (0x27D) — Driver assistance computer (secondary), Tesla Model 3 2025.20.8 CH CAN

Driver assistance computer (secondary) message: eac monitor; frame length from the layout, not yet observed on a vehicle bus. This page documents the 3 signals of APS_eacMonitor as defined for Tesla Model 3 firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APS_eacMonitor` |
| CAN id | 0x27D (637) |
| ECU | [Driver assistance computer (secondary)](../../aps.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | APS |
| Frame length | 3 bytes |
| Cycle time | 100 ms |
| Signals | 3 |

## Signals of APS_eacMonitor

Tesla Model 3 CAN bus signals in `APS_eacMonitor`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APS_eacAllow` | Indicates whether or not the Aurix external angle control (EAC) monitor logic currently allows angle control for Autopilot functions; raw 3 = signal not available (SNA) | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `APS_EAC_INHIBIT`<br>1 = `APS_EAC_ALLOW`<br>2 = `APS_EAC_RESERVED`<br>3 = `APS_EAC_SNA` | plausible |
| `APS_eacMonitorCounter` | Driver assistance computer (secondary): eac monitor counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `APS_eacMonitorChecksum` | Driver assistance computer (secondary): eac monitor checksum | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 CH DBC file](../../../../../dbc/Model3/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/CH.json)

## See also

- [All Driver assistance computer (secondary) messages (APS)](../../aps.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
