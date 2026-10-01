---
layout: default
title: "FC_info (0x51E) — FC ECU, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "FC ECU message: info. Tesla Model 3 / Model Y CAN bus message FC_info (0x51E) of FC ECU, firmware 2025.20.8, 37 signals (FC_infoIndex, FC_infoBuildType, FC_infoBuildConfigID, FC_infoHardwareID and 33 more). Bit layout, scaling, units and value tables."
---

# FC_info (0x51E) — FC ECU, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

FC ECU message: info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 37 signals of FC_info as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `FC_info` |
| CAN id | 0x51E (1310) |
| ECU | [FC ECU](../../fc.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | FC |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 37 |

## Signals of FC_info

Tesla Model 3 / Model Y CAN bus signals in `FC_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `FC_infoIndex` | selector | FC ECU: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0_FC`<br>1 = `DEPRECATED_1_FC`<br>2 = `DEPRECATED_2_FC`<br>3 = `DEPRECATED_3_FC`<br>4 = `DEPRECATED_4_FC`<br>5 = `DEPRECATED_5_FC`<br>6 = `DEPRECATED_6_FC`<br>7 = `DEPRECATED_7_FC`<br>8 = `DEPRECATED_8_FC`<br>9 = `DEPRECATED_9_FC`<br>10 = `BUILD_HWID_COMPONENTID_FC`<br>11 = `PCBAID_ASSYID_USAGEID_FC`<br>13 = `APP_CRC_FC`<br>14 = `BOOTLOADER_SVN_FC`<br>15 = `BOOTLOADER_CRC_FC`<br>16 = `SUBCOMPONENT_FC`<br>17 = `APP_GITHASH_FC`<br>18 = `BOOTLOADER_GITHASH_FC`<br>19 = `VERSION_DEPRECATED_FC`<br>20 = `UDS_PROTOCOL_BOOTCRC_FC`<br>22 = `VARIANT_CRC_FC`<br>25 = `PART_NUM_1`<br>26 = `PART_NUM_2`<br>27 = `PART_NUM_3`<br>255 = `END_FC` | plausible |
| `FC_infoBuildType` | page 10 | FC ECU: info build type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `INFO_UNKNOWN_BUILD_FC`<br>1 = `INFO_PLATFORM_BUILD_FC`<br>2 = `INFO_LOCAL_BUILD_FC`<br>3 = `INFO_TRACEABLE_CI_BUILD_FC`<br>4 = `INFO_MFG_BUILD_FC` | plausible |
| `FC_infoBuildConfigID` | page 10 | FC ECU: info build config ID | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `FC_infoHardwareID` | page 10 | FC ECU: info hardware ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `FC_infoComponentID` | page 10 | FC ECU: info component ID | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `FC_infoPcbaID` | page 11 | FC ECU: info pcba ID | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `FC_infoAssemblyID` | page 11 | FC ECU: info assembly ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `FC_infoUsageID` | page 11 | FC ECU: info usage ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `FC_infoSubUsageID` | page 11 | FC ECU: info sub usage ID | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `FC_infoApplicationCRC` | page 13 | FC ECU: info application CRC | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `FC_infoAppGitHashBytes` | page 17 | FC ECU: info app git hash bytes | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | layout-only |
| `FC_infoBootGitHashBytes` | page 18 | FC ECU: info boot git hash bytes | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | layout-only |
| `FC_infoPlatformType` | page 19 | FC ECU: info platform type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `FC_infoMajorVersion` | page 19 | Fast charger firmware major version number | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `FC_infoBranchOrigin` | page 19 | Fast charger branch origin | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `FC_infoMaturity` | page 19 | Fast charger firmware info | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `FC_infoHardwareRevision` | page 19 | FC ECU: info hardware revision | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `FC_partNumChar01` | page 25 | FC ECU: part num char01 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `FC_partNumChar02` | page 25 | FC ECU: part num char02 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `FC_partNumChar03` | page 25 | FC ECU: part num char03 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `FC_partNumChar04` | page 25 | FC ECU: part num char04 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `FC_partNumChar05` | page 25 | FC ECU: part num char05 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `FC_partNumChar06` | page 25 | FC ECU: part num char06 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `FC_partNumChar07` | page 25 | FC ECU: part num char07 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `FC_partNumChar08` | page 26 | FC ECU: part num char08 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `FC_partNumChar09` | page 26 | FC ECU: part num char09 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `FC_partNumChar10` | page 26 | FC ECU: part num char10 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `FC_partNumChar11` | page 26 | FC ECU: part num char11 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `FC_partNumChar12` | page 26 | FC ECU: part num char12 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `FC_partNumChar13` | page 26 | FC ECU: part num char13 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `FC_partNumChar14` | page 26 | FC ECU: part num char14 | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `FC_partNumChar15` | page 27 | FC ECU: part num char15 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `FC_partNumChar16` | page 27 | FC ECU: part num char16 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `FC_partNumChar17` | page 27 | FC ECU: part num char17 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `FC_partNumChar18` | page 27 | FC ECU: part num char18 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `FC_partNumChar19` | page 27 | FC ECU: part num char19 | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `FC_partNumChar20` | page 27 | FC ECU: part num char20 | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Multiplexing

`FC_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (4 signals), page 11 (4 signals), page 13 (1 signals), page 17 (1 signals), page 18 (1 signals), page 19 (5 signals), page 25 (7 signals), page 26 (7 signals), page 27 (6 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All FC ECU messages (FC)](../../fc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
