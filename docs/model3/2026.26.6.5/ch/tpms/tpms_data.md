---
layout: default
title: "TPMS_data (0x31F) — Tire pressure monitoring, Tesla Model 3 2026.26.6.5 CH CAN"
description: "Tire pressure monitoring message: data. Tesla Model 3 CAN bus message TPMS_data (0x31F) of Tire pressure monitoring, firmware 2026.26.6.5, 8 signals (TPMS_pressureFL, TPMS_temperatureFL, TPMS_pressureFR, TPMS_temperatureFR and 4 more). Bit layout, scaling, units and value tables."
---

# TPMS_data (0x31F) — Tire pressure monitoring, Tesla Model 3 2026.26.6.5 CH CAN

Tire pressure monitoring message: data; frame length from the layout, not yet observed on a vehicle bus. This page documents the 8 signals of TPMS_data as defined for Tesla Model 3 firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `TPMS_data` |
| CAN id | 0x31F (799) |
| ECU | [Tire pressure monitoring](../../tpms.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | TPMS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 8 |

## Signals of TPMS_data

Tesla Model 3 CAN bus signals in `TPMS_data`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `TPMS_pressureFL` | front left tire pressure; raw 255 = signal not available (SNA) | 0\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.35 | 254 = `OVER_RANGE`<br>255 = `SNA` | validated |
| `TPMS_temperatureFL` | front left tire temperature; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 214 | 255 = `TPMS_TEMPERATURE_SNA` | validated |
| `TPMS_pressureFR` | front right tire pressure; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.35 | 254 = `OVER_RANGE`<br>255 = `SNA` | validated |
| `TPMS_temperatureFR` | front right tire temperature; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 214 | 255 = `TPMS_TEMPERATURE_SNA` | validated |
| `TPMS_pressureRL` | rear left tire pressure; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.35 | 254 = `OVER_RANGE`<br>255 = `SNA` | validated |
| `TPMS_temperatureRL` | rear left tire temperature; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 214 | 255 = `TPMS_TEMPERATURE_SNA` | validated |
| `TPMS_pressureRR` | rear right tire pressure; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.35 | 254 = `OVER_RANGE`<br>255 = `SNA` | validated |
| `TPMS_temperatureRR` | rear right tire temperature; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 214 | 255 = `TPMS_TEMPERATURE_SNA` | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 CH DBC file](../../../../../dbc/Model3/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/CH.json)

## See also

- [All Tire pressure monitoring messages (TPMS)](../../tpms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
