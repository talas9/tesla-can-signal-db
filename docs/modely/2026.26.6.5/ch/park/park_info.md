---
layout: default
title: "PARK_info (0x326) — Parking assist sensors, Tesla Model Y 2026.26.6.5 CH CAN"
description: "Parking assist sensors message: info. Tesla Model Y CAN bus message PARK_info (0x326) of Parking assist sensors, firmware 2026.26.6.5, 9 signals (PARK_infoIndex, PARK_infoBuildType, PARK_infoComponentID, PARK_infoPcbaID and 5 more). Bit layout, scaling, units and value tables."
---

# PARK_info (0x326) — Parking assist sensors, Tesla Model Y 2026.26.6.5 CH CAN

Parking assist sensors message: info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 9 signals of PARK_info as defined for Tesla Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PARK_info` |
| CAN id | 0x326 (806) |
| ECU | [Parking assist sensors](../../park.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | PARK |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 9 |

## Signals of PARK_info

Tesla Model Y CAN bus signals in `PARK_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `PARK_infoIndex` | selector | Parking assist sensors: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0`<br>1 = `DEPRECATED_1`<br>2 = `DEPRECATED_2`<br>3 = `DEPRECATED_3`<br>4 = `DEPRECATED_4`<br>5 = `DEPRECATED_5`<br>6 = `DEPRECATED_6`<br>7 = `DEPRECATED_7`<br>8 = `DEPRECATED_8`<br>9 = `DEPRECATED_9`<br>10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>15 = `BOOTLOADER_CRC`<br>16 = `SUBCOMPONENT`<br>17 = `APP_GITHASH`<br>18 = `BOOTLOADER_GITHASH`<br>19 = `VERSION_DEPRECATED`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>22 = `VARIANTCRC`<br>23 = `SUBCOMPONENT2`<br>25 = `PACKAGE_PN_1_7`<br>26 = `PACKAGE_PN_8_14`<br>27 = `PACKAGE_PN_15_20`<br>29 = `PACKAGE_SN_1_7`<br>30 = `PACKAGE_SN_8_14`<br>31 = `SUBCOMPONENT_GITHASH`<br>255 = `END` | plausible |
| `PARK_infoBuildType` | page 10 | Parking assist sensors: info build type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | validated |
| `PARK_infoComponentID` | page 10 | Parking assist sensors: info component ID | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `PARK_infoPcbaID` | page 11 | Parking assist sensors: info pcba ID | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `PARK_infoAssemblyID` | page 11 | Parking assist sensors: info assembly ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `PARK_infoUsageID` | page 11 | Parking assist sensors: info usage ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `PARK_infoApplicationCRC` | page 13 | Parking assist sensors: info application CRC | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `PARK_infoBootUdsProtoVersion` | page 20 | Parking assist sensors: info boot uds proto version | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `PARK_infoBootloaderCRC` | page 20 | Parking assist sensors: info bootloader CRC | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |

## Multiplexing

`PARK_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (2 signals), page 11 (3 signals), page 13 (1 signals), page 20 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/ModelY/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/CH.json)

## See also

- [All Parking assist sensors messages (PARK)](../../park.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
