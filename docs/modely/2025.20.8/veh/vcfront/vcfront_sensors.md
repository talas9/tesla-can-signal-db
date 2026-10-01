---
layout: default
title: "VCFRONT_sensors (0x321) — Front body controller, Tesla Model Y 2025.20.8 VEH CAN"
description: "Front body controller message: sensors. Tesla Model Y CAN bus message VCFRONT_sensors (0x321) of Front body controller, firmware 2025.20.8, 11 signals (VCFRONT_tempCoolantBatInlet, VCFRONT_tempCoolantPTInlet, VCFRONT_coolantLevel, VCFRONT_brakeFluidLevel and 7 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_sensors (0x321) — Front body controller, Tesla Model Y 2025.20.8 VEH CAN

Front body controller message: sensors; frame length observed on a vehicle bus. This page documents the 11 signals of VCFRONT_sensors as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_sensors` |
| CAN id | 0x321 (801) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 11 |

## Signals of VCFRONT_sensors

Tesla Model Y CAN bus signals in `VCFRONT_sensors`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_tempCoolantBatInlet` | Battery measured inlet coolant temperature; raw 1023 = signal not available (SNA) | 0\|10 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 85 | 1023 = `SNA` | plausible |
| `VCFRONT_tempCoolantPTInlet` | Powertrain measured inlet coolant temperature; raw 2047 = signal not available (SNA) | 10\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 200 | 2047 = `SNA` | plausible |
| `VCFRONT_coolantLevel` | Front body controller: coolant level | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_OK`<br>1 = `FILLED` | plausible |
| `VCFRONT_brakeFluidLevel` | Reports detected brake fluid level at the fluid reservoir; raw 0 = signal not available (SNA) | 22\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `LOW`<br>2 = `NORMAL` | plausible |
| `VCFRONT_tempAmbient` | Front body controller: temp ambient; raw 0 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 80 | 0 = `SNA` | plausible |
| `VCFRONT_washerFluidLevel` | Indicates that the sensor has detected low windshield washer fluid; raw 0 = signal not available (SNA) | 32\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `LOW`<br>2 = `NORMAL` | plausible |
| `VCFRONT_tempAmbientFiltered` | Filtered ambient temperature based on vehicle speed; raw 0 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 80 | 0 = `SNA` | plausible |
| `VCFRONT_battSensorIrrational` | Front body controller: batt sensor irrational | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_ptSensorIrrational` | Front body controller: pt sensor irrational | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCFRONT_sensorsCounter` | Front body controller: sensors counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | plausible |
| `VCFRONT_sensorsChecksum` | Front body controller: sensors checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
