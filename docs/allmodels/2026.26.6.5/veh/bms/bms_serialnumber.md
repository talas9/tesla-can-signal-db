---
layout: default
title: "BMS_serialNumber (0x72A) — High-voltage battery management system, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "High-voltage battery management system message: serial number. Tesla Model 3 / Model Y CAN bus message BMS_serialNumber (0x72A) of High-voltage battery management system, firmware 2026.26.6.5, 16 signals (BMS_serialNumberMultiplexer, BMS_packSerialNumberByte01, BMS_packSerialNumberByte02, BMS_packSerialNumberByte03 and 12 more). Bit layout, scaling, units and value tables."
---

# BMS_serialNumber (0x72A) — High-voltage battery management system, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

High-voltage battery management system message: serial number; frame length observed on a vehicle bus. This page documents the 16 signals of BMS_serialNumber as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_serialNumber` |
| CAN id | 0x72A (1834) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 16 |

## Signals of BMS_serialNumber

Tesla Model 3 / Model Y CAN bus signals in `BMS_serialNumber`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_serialNumberMultiplexer` | selector | High-voltage battery management system: serial number multiplexer | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `BMS_SERIAL_MUX0`<br>1 = `BMS_SERIAL_MUX1`<br>2 = `BMS_SERIAL_MUX2` | plausible |
| `BMS_packSerialNumberByte01` | page 0 | Pack serial number, character 1 (ASCII) | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `BMS_packSerialNumberByte02` | page 0 | Pack serial number, character 2 (ASCII) | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `BMS_packSerialNumberByte03` | page 0 | Pack serial number, character 3 (ASCII) | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `BMS_packSerialNumberByte04` | page 0 | Pack serial number, character 4 (ASCII) | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `BMS_packSerialNumberByte05` | page 0 | Pack serial number, character 5 (ASCII) | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `BMS_packSerialNumberByte06` | page 0 | Pack serial number, character 6 (ASCII) | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `BMS_packSerialNumberByte07` | page 0 | Pack serial number, character 7 (ASCII) | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `BMS_packSerialNumberByte08` | page 1 | Pack serial number, character 8 (ASCII) | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `BMS_packSerialNumberByte09` | page 1 | Pack serial number, character 9 (ASCII) | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `BMS_packSerialNumberByte10` | page 1 | Pack serial number, character 10 (ASCII) | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `BMS_packSerialNumberByte11` | page 1 | Pack serial number, character 11 (ASCII) | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `BMS_packSerialNumberByte12` | page 1 | Pack serial number, character 12 (ASCII) | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `BMS_packSerialNumberByte13` | page 1 | Pack serial number, character 13 (ASCII) | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `BMS_packSerialNumberByte14` | page 1 | Pack serial number, character 14 (ASCII) | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `BMS_packSerialBirthDateBinned` | page 2 | High-voltage battery management system: pack serial birth date binned | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |

## Multiplexing

`BMS_serialNumberMultiplexer` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (7 signals), page 1 (7 signals), page 2 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
