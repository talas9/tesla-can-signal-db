---
layout: default
title: "ESP_party3 (0x38D) — Electronic stability control, Tesla Model 3 2025.20.8 PARTY CAN"
description: "Electronic stability control message: party3. Tesla Model 3 CAN bus message ESP_party3 (0x38D) of Electronic stability control, firmware 2025.20.8, 11 signals (ESP_party3Crc, ESP_party3Counter, ESP_absActive, ESP_vehicleStandstill and 7 more). Bit layout, scaling, units and value tables."
---

# ESP_party3 (0x38D) — Electronic stability control, Tesla Model 3 2025.20.8 PARTY CAN

Electronic stability control message: party3; frame length from the layout, not yet observed on a vehicle bus. This page documents the 11 signals of ESP_party3 as defined for Tesla Model 3 firmware 2025.20.8 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `ESP_party3` |
| CAN id | 0x38D (909) |
| ECU | [Electronic stability control](../../esp.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | ESP |
| Frame length | 7 bytes |
| Cycle time | 10 ms |
| Signals | 11 |

## Signals of ESP_party3

Tesla Model 3 CAN bus signals in `ESP_party3`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `ESP_party3Crc` | Electronic stability control: party3 crc | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `ESP_party3Counter` | Electronic stability control: party3 counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `ESP_absActive` | Electronic stability control: abs active | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `ABS_NOT_ACTIVE`<br>1 = `ABS_ACTIVE` | plausible |
| `ESP_vehicleStandstill` | Indicates that the vehicle is completely stationary. | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_STANDSTILL`<br>1 = `STANDSTILL` | plausible |
| `ESP_vehicleStandstillQF` | Qualifier of ESP_vehicleStandstill. | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `STANDSTILL_NOT_INIT`<br>1 = `STANDSTILL_NORMAL`<br>2 = `STANDSTILL_FAULTED` | plausible |
| `ESP_pEstMaximum` | Maximum of estimated wheel braking pressure. | 16\|8 | little-endian | unsigned | 1 | 0 | bar | 0 to 255 |  | plausible |
| `ESP_privateVehicleSpd` | Vehicle speed as calculated by the ESP from the wheel speed sensors. | 24\|8 | little-endian | unsigned | 0.4 | 0 | m/s | 0 to 102 |  | plausible |
| `ESP_decoupledBrakePressOffsetComp` | Master cylinder pressure sensor offset; raw 127 = signal not available (SNA) | 33\|7 | little-endian | unsigned | 0.25 | -16 | bar | -16 to 15.5 | 127 = `SNA` | plausible |
| `ESP_privateVehicleSpdQF` | ESP private vehicle speed qualifier | 41\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NotInit_orOff`<br>1 = `Normal`<br>2 = `Faulty` | plausible |
| `ESP_brakeMasterCylPress` | Master cylinder pressure measured in the ESP; raw 1023 = signal not available (SNA) | 44\|10 | little-endian | unsigned | 0.3 | -30 | bar | -30 to 276.6 | 1023 = `SNA` | plausible |
| `ESP_brakeMasterCylPressQF` | Reports the brake master cylinder pressure signal (ESP_brakeMasterCylPress) qualification status. | 54\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PRESSURE_NOT_INITIALIZED`<br>1 = `PRESSURE_NORMAL`<br>2 = `PRESSURE_FAULTED`<br>3 = `PRESSURE_FAULTED2` | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 PARTY DBC file](../../../../../dbc/Model3/2025.20.8/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/PARTY.json)

## See also

- [All Electronic stability control messages (ESP)](../../esp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
