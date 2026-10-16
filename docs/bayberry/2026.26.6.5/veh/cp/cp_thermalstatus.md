---
layout: default
title: "CP_thermalStatus (0x37D) — Charge port controller, Tesla Model Y (2025+ / Juniper; community mapping) 2026.26.6.5 VEH CAN"
description: "Charge port controller message: thermal status. Tesla Model Y (2025+ / Juniper; community mapping) CAN bus message CP_thermalStatus (0x37D) of Charge port controller, firmware 2026.26.6.5, 6 signals (CP_thermalStatusSelect, CP_pinTemperature1, CP_pinTemperature2, CP_pinTemperature3 and 2 more). Bit layout, scaling, units and value tables."
---

# CP_thermalStatus (0x37D) — Charge port controller, Tesla Model Y (2025+ / Juniper; community mapping) 2026.26.6.5 VEH CAN

Charge port controller message: thermal status; frame length observed on a vehicle bus. This page documents the 6 signals of CP_thermalStatus as defined for Tesla Model Y (2025+ / Juniper; community mapping) firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `CP_thermalStatus` |
| CAN id | 0x37D (893) |
| ECU | [Charge port controller](../../cp.md) |
| Vehicle | Tesla Model Y (2025+ / Juniper; community mapping) |
| API name / codename | `Bayberry` |
| Coverage scope | Product-metadata signal subset using the Model 3 / Model Y union routing map; no product-specific CAN routing map or complete vehicle coverage is established. |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | CP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 6 |

## Signals of CP_thermalStatus

Tesla Model Y (2025+ / Juniper; community mapping) CAN bus signals in `CP_thermalStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `CP_thermalStatusSelect` | selector | Charge port controller: thermal status select | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `0`<br>1 = `1` | validated |
| `CP_pinTemperature1` | page 1 | Sensed temperature of the charge port inlet pins | 8\|8 | little-endian | unsigned | 0.8039216 | -55 | C | -55 to 149.99 |  | validated |
| `CP_pinTemperature2` | page 1 | Sensed temperature of the charge port inlet pins | 16\|8 | little-endian | unsigned | 0.8039216 | -55 | C | -55 to 149.99 |  | validated |
| `CP_pinTemperature3` | page 1 | Sensed temperature of the charge port inlet pins | 24\|8 | little-endian | unsigned | 0.8039216 | -55 | C | -55 to 149.99 |  | validated |
| `CP_pinTemperature4` | page 1 | Sensed temperature of the charge port inlet pins | 32\|8 | little-endian | unsigned | 0.8039216 | -55 | C | -55 to 149.99 |  | validated |
| `CP_pinTemp4Velocity` | page 1 | Instantaneous temperature velocity (over 1 minute) of Charge Port's temperature 4; raw 511 = signal not available (SNA) | 40\|10 | little-endian | signed | 0.15748 | 0 | C/min | -80.47228 to 80.3148 | 511 = `SNA` | validated |

## Multiplexing

`CP_thermalStatusSelect` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (5 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y (2025+ / Juniper; community mapping) 2026.26.6.5 VEH DBC file](../../../../../dbc/Bayberry/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Bayberry/2026.26.6.5/VEH.json)

## See also

- [All Charge port controller messages (CP)](../../cp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
