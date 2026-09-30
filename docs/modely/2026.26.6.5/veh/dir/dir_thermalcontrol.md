---
layout: default
title: "DIR_thermalControl (0x5D7) — Rear drive inverter, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Rear drive inverter message: thermal control. Tesla Model Y CAN bus message DIR_thermalControl (0x5D7) of Rear drive inverter, firmware 2026.26.6.5, 6 signals (DIR_passiveInletTempReq, DIR_activeInletTempReq, DIR_coolantFlowReq, DIR_oilFlowReq and 2 more). Bit layout, scaling, units and value tables."
---

# DIR_thermalControl (0x5D7) — Rear drive inverter, Tesla Model Y 2026.26.6.5 VEH CAN

Rear drive inverter message: thermal control; frame length from the layout, not yet observed on a vehicle bus. This page documents the 6 signals of DIR_thermalControl as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DIR_thermalControl` |
| CAN id | 0x5D7 (1495) |
| ECU | [Rear drive inverter](../../dir.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | DIR |
| Frame length | 5 bytes |
| Cycle time | 1000 ms |
| Signals | 6 |

## Signals of DIR_thermalControl

Tesla Model Y CAN bus signals in `DIR_thermalControl`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIR_passiveInletTempReq` | Rear drive inverter: passive inlet temp req | 0\|8 | little-endian | unsigned | 1 | -40 | DegC | -40 to 215 |  | validated |
| `DIR_activeInletTempReq` | Rear drive inverter: active inlet temp req | 8\|8 | little-endian | unsigned | 1 | -40 | DegC | -40 to 215 |  | validated |
| `DIR_coolantFlowReq` | Coolant flow requested | 16\|8 | little-endian | unsigned | 0.2 | 0 | LPM | 0 to 50 |  | validated |
| `DIR_oilFlowReq` | Rear drive inverter: oil flow req; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.1 | 0 | LPM | 0 to 25.4 | 255 = `SNA` | validated |
| `DIR_criticalFlowReq` | Rear drive inverter: critical flow req | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | validated |
| `DIR_burnInStatus` | Rear drive inverter: burn in status | 33\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INIT`<br>1 = `NOT_REQUIRED`<br>2 = `UNAVAILABLE`<br>3 = `INCOMPLETE`<br>4 = `ACTIVE`<br>5 = `COMPLETE` | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Rear drive inverter messages (DIR)](../../dir.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
