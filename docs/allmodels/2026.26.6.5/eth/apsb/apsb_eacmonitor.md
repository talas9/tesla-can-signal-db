---
layout: default
title: "APSB_eacMonitor (0x2DB) — APSB ECU, Tesla Model 3 / Model Y 2026.26.6.5 ETH"
description: "APSB ECU message: eac monitor. Ethernet-side message APSB_eacMonitor of APSB ECU for Tesla Model 3 / Model Y firmware 2026.26.6.5, 3 signals (APSB_eacAllow, APSB_eacMonitorCounter, APSB_eacMonitorChecksum). Bit layout, scaling, units and value tables."
---

# APSB_eacMonitor (0x2DB) — APSB ECU, Tesla Model 3 / Model Y 2026.26.6.5 ETH

APSB ECU message: eac monitor. This page documents the 3 signals of APSB_eacMonitor as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `APSB_eacMonitor` |
| Ethernet-side id | 0x2DB (731) |
| ECU | [APSB ECU](../../apsb.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | APSB |
| Frame length | 3 bytes |
| Cycle time | 100 ms |
| Signals | 3 |

## Signals of APSB_eacMonitor

Tesla Model 3 / Model Y CAN bus signals in `APSB_eacMonitor`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APSB_eacAllow` | Indicates whether or not the Aurix external angle control (EAC) monitor logic currently allows angle control for Autopilot functions; raw 3 = signal not available (SNA) | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `APS_EAC_INHIBIT`<br>1 = `APS_EAC_ALLOW`<br>2 = `APS_EAC_RESERVED`<br>3 = `APS_EAC_SNA` | validated |
| `APSB_eacMonitorCounter` | APSB ECU: eac monitor counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `APSB_eacMonitorChecksum` | APSB ECU: eac monitor checksum | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/AllModels/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All APSB ECU messages (APSB)](../../apsb.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
