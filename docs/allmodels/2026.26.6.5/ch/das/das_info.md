---
layout: default
title: "DAS_info (0x539) — Driver assistance computer, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Driver assistance computer message: info. Tesla Model 3 / Model Y CAN bus message DAS_info (0x539) of Driver assistance computer, firmware 2026.26.6.5, 12 signals (DAS_infoIndex, DAS_infoBuildType, DAS_infoBuildConfigID, DAS_infoHardwareID and 8 more). Bit layout, scaling, units and value tables."
---

# DAS_info (0x539) — Driver assistance computer, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Driver assistance computer message: info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 12 signals of DAS_info as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DAS_info` |
| CAN id | 0x539 (1337) |
| ECU | [Driver assistance computer](../../das.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | DAS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 12 |

## Signals of DAS_info

Tesla Model 3 / Model Y CAN bus signals in `DAS_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `DAS_infoIndex` | selector | Driver assistance computer: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0`<br>1 = `DEPRECATED_1`<br>2 = `DEPRECATED_2`<br>3 = `DEPRECATED_3`<br>4 = `DEPRECATED_4`<br>5 = `DEPRECATED_5`<br>6 = `DEPRECATED_6`<br>7 = `DEPRECATED_7`<br>8 = `DEPRECATED_8`<br>9 = `DEPRECATED_9`<br>10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>15 = `BOOTLOADER_CRC`<br>16 = `EYEQ_BOOT`<br>17 = `APP_GITHASH`<br>18 = `BOOTLOADER_GITHASH`<br>19 = `VERSION_DEPRECATED`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>23 = `EYEQ_APP`<br>24 = `EYEQ_FFS`<br>255 = `END` | plausible |
| `DAS_infoBuildType` | page 10 | Driver assistance computer: info build type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | plausible |
| `DAS_infoBuildConfigID` | page 10 | Driver assistance computer: info build config ID | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `DAS_infoHardwareID` | page 10 | Driver assistance computer: info hardware ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `DAS_infoComponentID` | page 10 | Driver assistance computer: info component ID | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `DAS_infoPcbaID` | page 11 | Driver assistance computer: info pcba ID | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `DAS_infoAssemblyID` | page 11 | Driver assistance computer: info assembly ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `DAS_infoUsageID` | page 11 | Driver assistance computer: info usage ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `DAS_infoSubUsageID` | page 11 | Driver assistance computer: info sub usage ID | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `DAS_infoApplicationCRC` | page 13 | Driver assistance computer: info application CRC | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `DAS_infoAppGitHashBytes` | page 17 | Driver assistance computer: info app git hash bytes | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | layout-only |
| `DAS_infoBootGitHashBytes` | page 18 | Driver assistance computer: info boot git hash bytes | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | layout-only |

## Multiplexing

`DAS_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (4 signals), page 11 (4 signals), page 13 (1 signals), page 17 (1 signals), page 18 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer messages (DAS)](../../das.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
