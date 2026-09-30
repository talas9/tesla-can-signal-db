---
layout: default
title: "PTC_info (0x345) — Cabin heater, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Cabin heater message: info. Tesla Model 3 / Model Y CAN bus message PTC_info (0x345) of Cabin heater, firmware 2025.20.8, 13 signals (PTC_infoIndex, PTC_infoBuildType, PTC_infoBuildConfigId, PTC_infoHardwareId and 9 more). Bit layout, scaling, units and value tables."
---

# PTC_info (0x345) — Cabin heater, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Cabin heater message: info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 13 signals of PTC_info as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PTC_info` |
| CAN id | 0x345 (837) |
| ECU | [Cabin heater](../../ptc.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | PTC |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 13 |

## Signals of PTC_info

Tesla Model 3 / Model Y CAN bus signals in `PTC_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `PTC_infoIndex` | selector | Cabin heater: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0`<br>1 = `DEPRECATED_1`<br>2 = `DEPRECATED_2`<br>3 = `DEPRECATED_3`<br>4 = `DEPRECATED_4`<br>5 = `DEPRECATED_5`<br>6 = `DEPRECATED_6`<br>7 = `DEPRECATED_7`<br>8 = `DEPRECATED_8`<br>9 = `DEPRECATED_9`<br>10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>15 = `BOOTLOADER_CRC`<br>16 = `SUBCOMPONENT`<br>17 = `APP_GITHASH`<br>18 = `BOOTLOADER_GITHASH`<br>19 = `VERSION_DEPRECATED`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>22 = `VARIANTCRC`<br>23 = `SUBCOMPONENT2`<br>25 = `PACKAGE_PN_1_7`<br>26 = `PACKAGE_PN_8_14`<br>27 = `PACKAGE_PN_15_20`<br>29 = `PACKAGE_SN_1_7`<br>30 = `PACKAGE_SN_8_14`<br>31 = `SUBCOMPONENT_GITHASH`<br>255 = `END` | plausible |
| `PTC_infoBuildType` | page 10 | Cabin heater: info build type | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | validated |
| `PTC_infoBuildConfigId` | page 10 | Cabin heater: info build config id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `PTC_infoHardwareId` | page 10 | Cabin heater: info hardware id | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `PTC_infoComponentId` | page 10 | Cabin heater: info component id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `PTC_infoPcbaId` | page 11 | Cabin heater: info pcba id | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `PTC_infoAssemblyId` | page 11 | Cabin heater: info assembly id; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 254 | 1 = `ASSEMBLY1`<br>255 = `ASSEMBLY_SNA` | validated |
| `PTC_infoUsageId` | page 11 | Cabin heater: info usage id | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `PTC_infoSubUsageId` | page 11 | Cabin heater: info sub usage id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `PTC_infoPlatformType` | page 13 | Cabin heater: info platform type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `PTC_infoAppCrc` | page 13 | Cabin heater: info app crc | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `PTC_infoBootUdsProtoVersion` | page 20 | Cabin heater: info boot uds proto version | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `PTC_infoBootCrc` | page 20 | Cabin heater: info boot crc | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |

## Multiplexing

`PTC_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (4 signals), page 11 (4 signals), page 13 (2 signals), page 20 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Cabin heater messages (PTC)](../../ptc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
