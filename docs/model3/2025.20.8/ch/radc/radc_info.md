---
layout: default
title: "RADC_info (0x531) — Radar, Tesla Model 3 2025.20.8 CH CAN"
description: "Radar message: info. Tesla Model 3 CAN bus message RADC_info (0x531) of Radar, firmware 2025.20.8, 17 signals (RADC_infoIndex, RADC_infoBuildType, RADC_infoBuildConfigID, RADC_infoHardwareID and 13 more). Bit layout, scaling, units and value tables."
---

# RADC_info (0x531) — Radar, Tesla Model 3 2025.20.8 CH CAN

Radar message: info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 17 signals of RADC_info as defined for Tesla Model 3 firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `RADC_info` |
| CAN id | 0x531 (1329) |
| ECU | [Radar](../../radc.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | RADC |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 17 |

## Signals of RADC_info

Tesla Model 3 CAN bus signals in `RADC_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `RADC_infoIndex` | selector | Radar: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 10 = `Mux10`<br>11 = `Mux11`<br>13 = `Mux13`<br>19 = `Mux19`<br>20 = `Mux20` | plausible |
| `RADC_infoBuildType` | page 10 | Radar: info build type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | plausible |
| `RADC_infoBuildConfigID` | page 10 | Radar: info build config ID | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `RADC_infoHardwareID` | page 10 | Radar: info hardware ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `RADC_infoComponentID` | page 10 | Radar: info component ID | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `RADC_infoPcbaID` | page 11 | Radar: info pcba ID | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `RADC_infoAssemblyID` | page 11 | Radar: info assembly ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `RADC_infoUsageID` | page 11 | Radar: info usage ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `RADC_infoSubUsageID` | page 11 | Radar: info sub usage ID | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `RADC_infoApplicationCRC` | page 13 | Radar: info application CRC | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `RADC_infoPlatformType` | page 19 | Radar: info platform type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `RADC_infoMajorVersion` | page 19 | Radar: info major version | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `RADC_infoBranchOrigin` | page 19 | Radar: info branch origin | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `RADC_infoMaturity` | page 19 | Radar: info maturity | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `RADC_infoHardwareRevision` | page 19 | Radar: info hardware revision | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `RADC_infoBootUdsProtoVersion` | page 20 | Radar: info boot uds proto version | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `RADC_infoBootloaderCRC` | page 20 | Radar: info bootloader CRC | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |

## Multiplexing

`RADC_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (4 signals), page 11 (4 signals), page 13 (1 signals), page 19 (5 signals), page 20 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 CH DBC file](../../../../../dbc/Model3/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/CH.json)

## See also

- [All Radar messages (RADC)](../../radc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
