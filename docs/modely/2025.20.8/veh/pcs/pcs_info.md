---
layout: default
title: "PCS_info (0x3C4) — Power conversion system (on-board charger and DC-DC converter), Tesla Model Y 2025.20.8 VEH CAN"
description: "Power conversion system (on-board charger and DC-DC converter) message: info. Tesla Model Y CAN bus message PCS_info (0x3C4) of Power conversion system (on-board charger and DC-DC converter), firmware 2025.20.8, 16 signals (PCS_infoIndex, PCS_buildType, PCS_buildConfigId, PCS_hardwareId and 12 more). Bit layout, scaling, units and value tables."
---

# PCS_info (0x3C4) — Power conversion system (on-board charger and DC-DC converter), Tesla Model Y 2025.20.8 VEH CAN

Power conversion system (on-board charger and DC-DC converter) message: info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 16 signals of PCS_info as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PCS_info` |
| CAN id | 0x3C4 (964) |
| ECU | [Power conversion system (on-board charger and DC-DC converter)](../../pcs.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | PCS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 16 |

## Signals of PCS_info

Tesla Model Y CAN bus signals in `PCS_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `PCS_infoIndex` | selector | Power conversion system (on-board charger and DC-DC converter): info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0`<br>1 = `DEPRECATED_1`<br>2 = `DEPRECATED_2`<br>3 = `DEPRECATED_3`<br>4 = `DEPRECATED_4`<br>5 = `DEPRECATED_5`<br>6 = `DEPRECATED_6`<br>7 = `DEPRECATED_7`<br>8 = `DEPRECATED_8`<br>9 = `DEPRECATED_9`<br>10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>15 = `BOOTLOADER_CRC`<br>16 = `SUBCOMPONENT`<br>17 = `APP_GITHASH`<br>18 = `BOOTLOADER_GITHASH`<br>19 = `VERSION_DEPRECATED`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>22 = `VARIANTCRC`<br>23 = `SUBCOMPONENT2`<br>25 = `PACKAGE_PN_1_7`<br>26 = `PACKAGE_PN_8_14`<br>27 = `PACKAGE_PN_15_20`<br>29 = `PACKAGE_SN_1_7`<br>30 = `PACKAGE_SN_8_14`<br>31 = `SUBCOMPONENT_GITHASH`<br>255 = `END` | plausible |
| `PCS_buildType` | page 10 | Power conversion system (on-board charger and DC-DC converter): build type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | plausible |
| `PCS_buildConfigId` | page 10 | Power conversion system (on-board charger and DC-DC converter): build config id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PCS_hardwareId` | page 10 | Power conversion system (on-board charger and DC-DC converter): hardware id | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PCS_componentId` | page 10 | Power conversion system (on-board charger and DC-DC converter): component id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PCS_pcbaId` | page 11 | PCBA ID portion of component hardware ID as reported by application | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `PCS_assemblyId` | page 11 | Power conversion system (on-board charger and DC-DC converter): assembly id | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PCS_usageId` | page 11 | Usage ID portion of component hardware ID as reported by application | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | plausible |
| `PCS_subUsageId` | page 11 | Sub-usage ID portion of component hardware ID as reported by application | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | plausible |
| `PCS_platformType` | page 13 | Power conversion system (on-board charger and DC-DC converter): platform type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PCS_appCrc` | page 13 | Power conversion system (on-board charger and DC-DC converter): app crc | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `PCS_cpu2AppCrc` | page 16 | Power conversion system (on-board charger and DC-DC converter): cpu2 app crc | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `PCS_appGitHash` | page 17 | Power conversion system (on-board charger and DC-DC converter): app git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | layout-only |
| `PCS_bootGitHash` | page 18 | Power conversion system (on-board charger and DC-DC converter): boot git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | layout-only |
| `PCS_bootUdsProtoVersion` | page 20 | Power conversion system (on-board charger and DC-DC converter): boot uds proto version | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PCS_bootCrc` | page 20 | Power conversion system (on-board charger and DC-DC converter): boot crc | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |

## Multiplexing

`PCS_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (4 signals), page 11 (4 signals), page 13 (2 signals), page 16 (1 signals), page 17 (1 signals), page 18 (1 signals), page 20 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All Power conversion system (on-board charger and DC-DC converter) messages (PCS)](../../pcs.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
