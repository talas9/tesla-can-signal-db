---
layout: default
title: "SCCM_info (0x330) — Steering column control module, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Steering column control module message: info. Tesla Model 3 / Model Y CAN bus message SCCM_info (0x330) of Steering column control module, firmware 2026.26.6.5, 18 signals (SCCM_infoIndex, SCCM_infoBuildType, SCCM_infoBuildConfigId, SCCM_infoHardwareId and 14 more). Bit layout, scaling, units and value tables."
---

# SCCM_info (0x330) — Steering column control module, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Steering column control module message: info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 18 signals of SCCM_info as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `SCCM_info` |
| CAN id | 0x330 (816) |
| ECU | [Steering column control module](../../sccm.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | SCCM |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 18 |

## Signals of SCCM_info

Tesla Model 3 / Model Y CAN bus signals in `SCCM_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `SCCM_infoIndex` | selector | Steering column control module: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>16 = `SUBCOMPONENT1`<br>17 = `APP_SVNHASH`<br>18 = `BOOTLOADER_SVNHASH`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>255 = `END` | plausible |
| `SCCM_infoBuildType` | page 10 | Steering column control module: info build type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | validated |
| `SCCM_infoBuildConfigId` | page 10 | Steering column control module: info build config id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `SCCM_infoHardwareId` | page 10 | Steering column control module: info hardware id | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `SCCM_infoComponentId` | page 10 | Steering column control module: info component id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `SCCM_infoPcbaId` | page 11 | Steering column control module: info pcba id | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `SCCM_infoAssemblyId` | page 11 | Steering column control module: info assembly id | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `SCCM_infoUsageId` | page 11 | Steering column control module: info usage id | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `SCCM_infoSubUsageId` | page 11 | Steering column control module: info sub usage id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `SCCM_infoPlatformType` | page 13 | Steering column control module: info platform type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `SCCM_infoAppCrc` | page 13 | Steering column control module: info app crc | 39\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `SCCM_infoBootSvnRev` | page 14 | Steering column control module: info boot svn rev | 8\|24 | little-endian | unsigned | 1 | 0 |  | 0 to 16777215 |  | validated |
| `SCCM_infoBootSvnUrlHash` | page 14 | Steering column control module: info boot svn url hash | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `SCCM_infoSubcomponent1Version` | page 16 | Steering column control module: info subcomponent1 version | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `SCCM_infoAppSvnHash` | page 17 | Steering column control module: info app svn hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | validated |
| `SCCM_infoBootSvnHash` | page 18 | Steering column control module: info boot svn hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | validated |
| `SCCM_infoUdsProtoVersion` | page 20 | Steering column control module: info uds proto version | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `SCCM_infoBootCrc` | page 20 | Steering column control module: info boot crc | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |

## Multiplexing

`SCCM_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (4 signals), page 11 (4 signals), page 13 (2 signals), page 14 (2 signals), page 16 (1 signals), page 17 (1 signals), page 18 (1 signals), page 20 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Steering column control module messages (SCCM)](../../sccm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
