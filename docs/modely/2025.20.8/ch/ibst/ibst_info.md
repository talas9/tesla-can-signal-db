---
layout: default
title: "IBST_info (0x32D) — Electric brake booster, Tesla Model Y 2025.20.8 CH CAN"
description: "Electric brake booster message: info. Tesla Model Y CAN bus message IBST_info (0x32D) of Electric brake booster, firmware 2025.20.8, 11 signals (IBST_infoIndex, IBST_infoBuildType, IBST_infoComponentID, IBST_infoPcbaID and 7 more). Bit layout, scaling, units and value tables."
---

# IBST_info (0x32D) — Electric brake booster, Tesla Model Y 2025.20.8 CH CAN

Electric brake booster message: info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 11 signals of IBST_info as defined for Tesla Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `IBST_info` |
| CAN id | 0x32D (813) |
| ECU | [Electric brake booster](../../ibst.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | IBST |
| Frame length | 8 bytes |
| Cycle time | 10000 ms |
| Signals | 11 |

## Signals of IBST_info

Tesla Model Y CAN bus signals in `IBST_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `IBST_infoIndex` | selector | Electric brake booster: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0`<br>1 = `DEPRECATED_1`<br>2 = `DEPRECATED_2`<br>3 = `DEPRECATED_3`<br>4 = `DEPRECATED_4`<br>5 = `DEPRECATED_5`<br>6 = `DEPRECATED_6`<br>7 = `DEPRECATED_7`<br>8 = `DEPRECATED_8`<br>9 = `DEPRECATED_9`<br>10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>15 = `BOOTLOADER_CRC`<br>16 = `SUBCOMPONENT`<br>17 = `APP_GITHASH`<br>18 = `BOOTLOADER_GITHASH`<br>19 = `VERSION_DEPRECATED`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>22 = `VARIANTCRC`<br>23 = `SUBCOMPONENT2`<br>25 = `PACKAGE_PN_1_7`<br>26 = `PACKAGE_PN_8_14`<br>27 = `PACKAGE_PN_15_20`<br>29 = `PACKAGE_SN_1_7`<br>30 = `PACKAGE_SN_8_14`<br>31 = `SUBCOMPONENT_GITHASH`<br>255 = `END` | plausible |
| `IBST_infoBuildType` | page 10 | Electric brake booster: info build type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | validated |
| `IBST_infoComponentID` | page 10 | Electric brake booster: info component ID | 55\|16 | big-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `IBST_infoPcbaID` | page 11 | Electric brake booster: info pcba ID | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `IBST_infoAssemblyID` | page 11 | Electric brake booster: info assembly ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `IBST_infoUsageID` | page 11 | Electric brake booster: info usage ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `IBST_infoSubUsageID` | page 11 | Electric brake booster: info sub usage ID | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `IBST_infoApplicationCRC` | page 13 | Indicating the Application CRC value of firmware running in system. | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `IBST_infoBootUdsProtoVersion` | page 20 | Electric brake booster: info boot uds proto version | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `IBST_infoBootloaderCRC` | page 20 | Electric brake booster: info bootloader CRC | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `IBST_infoVariantCRC` | page 22 | Indicating the Calibration CRC value of firmware running in system. | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |

## Multiplexing

`IBST_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (2 signals), page 11 (4 signals), page 13 (1 signals), page 20 (2 signals), page 22 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 CH DBC file](../../../../../dbc/ModelY/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/CH.json)

## See also

- [All Electric brake booster messages (IBST)](../../ibst.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
