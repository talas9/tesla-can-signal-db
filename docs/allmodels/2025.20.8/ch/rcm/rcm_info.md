---
layout: default
title: "RCM_info (0x351) — Restraint control module, Tesla Model 3 / Model Y 2025.20.8 CH CAN"
description: "Restraint control module message: info. Tesla Model 3 / Model Y CAN bus message RCM_info (0x351) of Restraint control module, firmware 2025.20.8, 11 signals (RCM_infoIndex, RCM_infoBuildType, RCM_infoComponentID, RCM_infoPcbaID and 7 more). Bit layout, scaling, units and value tables."
---

# RCM_info (0x351) — Restraint control module, Tesla Model 3 / Model Y 2025.20.8 CH CAN

Restraint control module message: info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 11 signals of RCM_info as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `RCM_info` |
| CAN id | 0x351 (849) |
| ECU | [Restraint control module](../../rcm.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | RCM |
| Frame length | 8 bytes |
| Cycle time | 2000 ms |
| Signals | 11 |

## Signals of RCM_info

Tesla Model 3 / Model Y CAN bus signals in `RCM_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `RCM_infoIndex` | selector | Restraint control module: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0`<br>1 = `DEPRECATED_1`<br>2 = `DEPRECATED_2`<br>3 = `DEPRECATED_3`<br>4 = `DEPRECATED_4`<br>5 = `DEPRECATED_5`<br>6 = `DEPRECATED_6`<br>7 = `DEPRECATED_7`<br>8 = `DEPRECATED_8`<br>9 = `DEPRECATED_9`<br>10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>15 = `BOOTLOADER_CRC`<br>16 = `SUBCOMPONENT`<br>17 = `APP_GITHASH`<br>18 = `BOOTLOADER_GITHASH`<br>19 = `VERSION_DEPRECATED`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>22 = `VARIANTCRC`<br>23 = `SUBCOMPONENT2`<br>25 = `PACKAGE_PN_1_7`<br>26 = `PACKAGE_PN_8_14`<br>27 = `PACKAGE_PN_15_20`<br>29 = `PACKAGE_SN_1_7`<br>30 = `PACKAGE_SN_8_14`<br>31 = `SUBCOMPONENT_GITHASH`<br>255 = `END` | plausible |
| `RCM_infoBuildType` | page 10 | Restraint control module: info build type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | validated |
| `RCM_infoComponentID` | page 10 | Restraint control module: info component ID | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `RCM_infoPcbaID` | page 11 | Reports the Restraint Control Module (RCM) Printed Circuit Board Assembly (PCBA) identifier. | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `RCM_infoAssemblyID` | page 11 | Restraint control module: info assembly ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `RCM_infoUsageID` | page 11 | Reports the Restraint Control Module (RCM) usage identification. | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `RCM_infoApplicationCRC` | page 13 | Reports the Restraint Control Module (RCM) application Cyclic Redundancy Check (CRC). | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `RCM_infoBootUdsProtoVersion` | page 20 | Reports the Restraint Control Module (RCM) boot Unified Diagnostic Services (UDS) protocol version. | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `RCM_infoBootloaderCRC` | page 20 | Reports the Restraint Control Module (RCM) bootloader Cyclic Redundancy Check (CRC). | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `RCM_infoAlgoCalID` | page 22 | Reports the Restraint Control Module (RCM) algorithm calibration identification. | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `RCM_infoVariantCRC` | page 22 | Reports the Restraint Control Module (RCM) variant Cyclic Redundancy Check (CRC). | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |

## Multiplexing

`RCM_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (2 signals), page 11 (3 signals), page 13 (1 signals), page 20 (2 signals), page 22 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 CH DBC file](../../../../../dbc/AllModels/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/CH.json)

## See also

- [All Restraint control module messages (RCM)](../../rcm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
