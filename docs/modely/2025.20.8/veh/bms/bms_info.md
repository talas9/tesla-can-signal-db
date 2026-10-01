---
layout: default
title: "BMS_info (0x300) — High-voltage battery management system, Tesla Model Y 2025.20.8 VEH CAN"
description: "High-voltage battery management system message: info. Tesla Model Y CAN bus message BMS_info (0x300) of High-voltage battery management system, firmware 2025.20.8, 15 signals (BMS_infoIndex, BMS_buildType, BMS_buildConfigId, BMS_hardwareId and 11 more). Bit layout, scaling, units and value tables."
---

# BMS_info (0x300) — High-voltage battery management system, Tesla Model Y 2025.20.8 VEH CAN

High-voltage battery management system message: info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 15 signals of BMS_info as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_info` |
| CAN id | 0x300 (768) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 15 |

## Signals of BMS_info

Tesla Model Y CAN bus signals in `BMS_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_infoIndex` | selector | High-voltage battery management system: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0`<br>1 = `DEPRECATED_1`<br>2 = `DEPRECATED_2`<br>3 = `DEPRECATED_3`<br>4 = `DEPRECATED_4`<br>5 = `DEPRECATED_5`<br>6 = `DEPRECATED_6`<br>7 = `DEPRECATED_7`<br>8 = `DEPRECATED_8`<br>9 = `DEPRECATED_9`<br>10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>15 = `BOOTLOADER_CRC`<br>16 = `SUBCOMPONENT`<br>17 = `APP_GITHASH`<br>18 = `BOOTLOADER_GITHASH`<br>19 = `VERSION_DEPRECATED`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>22 = `VARIANTCRC`<br>23 = `SUBCOMPONENT2`<br>25 = `PACKAGE_PN_1_7`<br>26 = `PACKAGE_PN_8_14`<br>27 = `PACKAGE_PN_15_20`<br>29 = `PACKAGE_SN_1_7`<br>30 = `PACKAGE_SN_8_14`<br>31 = `SUBCOMPONENT_GITHASH`<br>255 = `END` | plausible |
| `BMS_buildType` | page 10 | High-voltage battery management system: build type | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | plausible |
| `BMS_buildConfigId` | page 10 | High-voltage battery management system: build config id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `BMS_hardwareId` | page 10 | High-voltage battery management system: hardware id | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `BMS_componentId` | page 10 | High-voltage battery management system: component id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `BMS_pcbaId` | page 11 | BMS' assigned PCBA ID | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `BMS_assemblyId` | page 11 | BMS' assigned assembly ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `BMS_usageId` | page 11 | BMS' assigned usage ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | plausible |
| `BMS_subUsageId` | page 11 | BMS' assigned subusage ID | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | plausible |
| `BMS_platformType` | page 13 | High-voltage battery management system: platform type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `BMS_appCrc` | page 13 | High-voltage battery management system: app crc | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `BMS_appGitHash` | page 17 | High-voltage battery management system: app git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | layout-only |
| `BMS_bootGitHash` | page 18 | High-voltage battery management system: boot git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | layout-only |
| `BMS_bootUdsProtoVersion` | page 20 | High-voltage battery management system: boot uds proto version | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `BMS_bootCrc` | page 20 | High-voltage battery management system: boot crc | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |

## Multiplexing

`BMS_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (4 signals), page 11 (4 signals), page 13 (2 signals), page 17 (1 signals), page 18 (1 signals), page 20 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
