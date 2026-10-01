---
layout: default
title: "IDB_info (0x33C) — IDB ECU, Tesla Model 3 / Model Y 2025.20.8 CH CAN"
description: "IDB ECU message: info. Tesla Model 3 / Model Y CAN bus message IDB_info (0x33C) of IDB ECU, firmware 2025.20.8, 5 signals (IDB_infoIndex, IDB_infoPcbaID, IDB_infoAssemblyID, IDB_infoUsageID and 1 more). Bit layout, scaling, units and value tables."
---

# IDB_info (0x33C) — IDB ECU, Tesla Model 3 / Model Y 2025.20.8 CH CAN

IDB ECU message: info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 5 signals of IDB_info as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `IDB_info` |
| CAN id | 0x33C (828) |
| ECU | [IDB ECU](../../idb.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | IDB |
| Frame length | 8 bytes |
| Cycle time | 10000 ms |
| Signals | 5 |

## Signals of IDB_info

Tesla Model 3 / Model Y CAN bus signals in `IDB_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `IDB_infoIndex` | selector | IDB ECU: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0`<br>1 = `DEPRECATED_1`<br>2 = `DEPRECATED_2`<br>3 = `DEPRECATED_3`<br>4 = `DEPRECATED_4`<br>5 = `DEPRECATED_5`<br>6 = `DEPRECATED_6`<br>7 = `DEPRECATED_7`<br>8 = `DEPRECATED_8`<br>9 = `DEPRECATED_9`<br>10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>15 = `BOOTLOADER_CRC`<br>16 = `SUBCOMPONENT`<br>17 = `APP_GITHASH`<br>18 = `BOOTLOADER_GITHASH`<br>19 = `VERSION_DEPRECATED`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>22 = `VARIANTCRC`<br>23 = `SUBCOMPONENT2`<br>25 = `PACKAGE_PN_1_7`<br>26 = `PACKAGE_PN_8_14`<br>27 = `PACKAGE_PN_15_20`<br>29 = `PACKAGE_SN_1_7`<br>30 = `PACKAGE_SN_8_14`<br>31 = `SUBCOMPONENT_GITHASH`<br>255 = `END` | plausible |
| `IDB_infoPcbaID` | page 11 | IDB ECU: info pcba ID | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `IDB_infoAssemblyID` | page 11 | IDB ECU: info assembly ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `IDB_infoUsageID` | page 11 | IDB ECU: info usage ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `IDB_infoSubUsageID` | page 11 | IDB ECU: info sub usage ID | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |

## Multiplexing

`IDB_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 11 (4 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 CH DBC file](../../../../../dbc/AllModels/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/CH.json)

## See also

- [All IDB ECU messages (IDB)](../../idb.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
