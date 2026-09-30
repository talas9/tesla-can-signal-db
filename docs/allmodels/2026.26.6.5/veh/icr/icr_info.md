---
layout: default
title: "ICR_info (0x3AD) — ICR ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "ICR ECU message: info. Tesla Model 3 / Model Y CAN bus message ICR_info (0x3AD) of ICR ECU, firmware 2026.26.6.5, 9 signals (ICR_infoIndex, ICR_infoBuildType, ICR_infoPcbaId, ICR_infoAssemblyId and 5 more). Bit layout, scaling, units and value tables."
---

# ICR_info (0x3AD) — ICR ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

ICR ECU message: info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 9 signals of ICR_info as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `ICR_info` |
| CAN id | 0x3AD (941) |
| ECU | [ICR ECU](../../icr.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | ICR |
| Frame length | 8 bytes |
| Cycle time | 10000 ms |
| Signals | 9 |

## Signals of ICR_info

Tesla Model 3 / Model Y CAN bus signals in `ICR_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `ICR_infoIndex` | selector | ICR ECU: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0`<br>1 = `DEPRECATED_1`<br>2 = `DEPRECATED_2`<br>3 = `DEPRECATED_3`<br>4 = `DEPRECATED_4`<br>5 = `DEPRECATED_5`<br>6 = `DEPRECATED_6`<br>7 = `DEPRECATED_7`<br>8 = `DEPRECATED_8`<br>9 = `DEPRECATED_9`<br>10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>15 = `BOOTLOADER_CRC`<br>16 = `SUBCOMPONENT`<br>17 = `APP_GITHASH`<br>18 = `BOOTLOADER_GITHASH`<br>19 = `VERSION_DEPRECATED`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>22 = `VARIANTCRC`<br>23 = `SUBCOMPONENT2`<br>25 = `PACKAGE_PN_1_7`<br>26 = `PACKAGE_PN_8_14`<br>27 = `PACKAGE_PN_15_20`<br>29 = `PACKAGE_SN_1_7`<br>30 = `PACKAGE_SN_8_14`<br>31 = `SUBCOMPONENT_GITHASH`<br>255 = `END` | plausible |
| `ICR_infoBuildType` | page 10 | ICR ECU: info build type | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | validated |
| `ICR_infoPcbaId` | page 11 | ICR ECU: info pcba id | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `ICR_infoAssemblyId` | page 11 | ICR ECU: info assembly id | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `ICR_infoUsageId` | page 11 | ICR ECU: info usage id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `ICR_infoAppCrc` | page 13 | ICR ECU: info app crc | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `ICR_infoBoardPartNumber17` | page 25 | ICR ECU: info board part number17 | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | validated |
| `ICR_infoBoardPartNumber814` | page 26 | ICR ECU: info board part number814 | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | validated |
| `ICR_infoBoardPartNumber1520` | page 27 | ICR ECU: info board part number1520 | 8\|48 | little-endian | unsigned | 1 | 0 |  | 0 to 281474976710655 |  | validated |

## Multiplexing

`ICR_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (1 signals), page 11 (3 signals), page 13 (1 signals), page 25 (1 signals), page 26 (1 signals), page 27 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All ICR ECU messages (ICR)](../../icr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
