---
layout: default
title: "CC_logData (0x32C) — Charge cable controller, Tesla Model Y 2025.20.8 VEH CAN"
description: "Charge cable controller message: log data. Tesla Model Y CAN bus message CC_logData (0x32C) of Charge cable controller, firmware 2025.20.8, 18 signals (CC_logIndex, CC_activeConnectorID, CC_temperature1, CC_temperature2 and 14 more). Bit layout, scaling, units and value tables."
---

# CC_logData (0x32C) — Charge cable controller, Tesla Model Y 2025.20.8 VEH CAN

Charge cable controller message: log data; frame length from the layout, not yet observed on a vehicle bus. This page documents the 18 signals of CC_logData as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `CC_logData` |
| CAN id | 0x32C (812) |
| ECU | [Charge cable controller](../../cc.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | CC |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 18 |

## Signals of CC_logData

Tesla Model Y CAN bus signals in `CC_logData`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `CC_logIndex` | selector | Charge cable controller: log index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `Mux0`<br>1 = `Mux1`<br>2 = `Mux2`<br>3 = `Mux3`<br>4 = `Mux4`<br>10 = `Mux10`<br>11 = `Mux11`<br>12 = `Mux12`<br>13 = `Mux13` | plausible |
| `CC_activeConnectorID` | page 0 | Site identifier of active charge connector | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 255 = `SNA` | plausible |
| `CC_temperature1` | page 0 | Charge cable vehicle connector temperature | 16\|8 | little-endian | signed | 1 | 88 | DegC | -40 to 215 | 127 = `SNA` | plausible |
| `CC_temperature2` | page 0 | Charge cable vehicle connector temperature | 24\|8 | little-endian | signed | 1 | 88 | DegC | -40 to 215 | 127 = `SNA` | plausible |
| `CC_temperature3` | page 0 | Charge cable vehicle connector temperature | 32\|8 | little-endian | signed | 1 | 88 | DegC | -40 to 215 | 127 = `SNA` | plausible |
| `CC_contactor1Closed` | page 0 | State of contactor 1 in wall connector | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CC_CONTACTOR_OPEN`<br>1 = `CC_CONTACTOR_CLOSED`<br>3 = `CC_CONTACTOR_SNA` | plausible |
| `CC_contactor2Closed` | page 0 | State of contactor 1 in wall connector | 42\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CC_CONTACTOR_OPEN`<br>1 = `CC_CONTACTOR_CLOSED`<br>3 = `CC_CONTACTOR_SNA` | plausible |
| `CC_temperature4` | page 0 | Charge cable vehicle connector temperature | 44\|8 | little-endian | signed | 1 | 88 | DegC | -40 to 215 | 127 = `SNA` | plausible |
| `CC_conn1Current` | page 1 | AC current on connector 1 in wall charger load sharing group; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.5 | 0 | A | 0 to 127 | 255 = `SNA` | plausible |
| `CC_conn2Current` | page 2 | AC current on connector 2 in wall charger load sharing group; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.5 | 0 | A | 0 to 127 | 255 = `SNA` | plausible |
| `CC_conn3Current` | page 3 | AC current on connector 3 in wall charger load sharing group; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.5 | 0 | A | 0 to 127 | 255 = `SNA` | plausible |
| `CC_conn4Current` | page 4 | AC current on connector 4 in wall charger load sharing group; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.5 | 0 | A | 0 to 127 | 255 = `SNA` | plausible |
| `CC_lifetimei2t` | page 10 | Charge cable controller: lifetimei2t | 32\|32 | little-endian | unsigned | 0.1 | 0 | A2h | 0 to 429496729.5 |  | plausible |
| `CC_lifetimeCtrCycles` | page 11 | Charge cable controller: lifetime ctr cycles | 8\|28 | little-endian | unsigned | 1 | 0 |  | 0 to 268435455 |  | layout-only |
| `CC_lifetimeCtrCyclesLoaded` | page 11 | Charge cable controller: lifetime ctr cycles loaded | 36\|28 | little-endian | unsigned | 1 | 0 |  | 0 to 268435455 |  | layout-only |
| `CC_lifetimeAlertCount` | page 12 | Charge cable controller: lifetime alert count | 8\|28 | little-endian | unsigned | 1 | 0 |  | 0 to 268435455 |  | layout-only |
| `CC_lifetimeThermalFoldbacks` | page 12 | Charge cable controller: lifetime thermal foldbacks | 36\|28 | little-endian | unsigned | 1 | 0 |  | 0 to 268435455 |  | layout-only |
| `CC_lifetimeAvgStartupTemp` | page 13 | Charge cable controller: lifetime avg startup temp | 36\|28 | little-endian | signed | 0.1 | 0 | degC | -13421772.8 to 13421772.7 |  | plausible |

## Multiplexing

`CC_logIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (7 signals), page 1 (1 signals), page 2 (1 signals), page 3 (1 signals), page 4 (1 signals), page 10 (1 signals), page 11 (2 signals), page 12 (2 signals), page 13 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All Charge cable controller messages (CC)](../../cc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
