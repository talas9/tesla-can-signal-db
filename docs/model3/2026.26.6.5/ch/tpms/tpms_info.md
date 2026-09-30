---
layout: default
title: "TPMS_info (0x5EF) — Tire pressure monitoring, Tesla Model 3 2026.26.6.5 CH CAN"
description: "Tire pressure monitoring message: info. Tesla Model 3 CAN bus message TPMS_info (0x5EF) of Tire pressure monitoring, firmware 2026.26.6.5, 8 signals (TPMS_infoIndex, TPMS_infoComponentID, TPMS_infoPcbaID, TPMS_infoAssemblyID and 4 more). Bit layout, scaling, units and value tables."
---

# TPMS_info (0x5EF) — Tire pressure monitoring, Tesla Model 3 2026.26.6.5 CH CAN

Tire pressure monitoring message: info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 8 signals of TPMS_info as defined for Tesla Model 3 firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `TPMS_info` |
| CAN id | 0x5EF (1519) |
| ECU | [Tire pressure monitoring](../../tpms.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | TPMS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 8 |

## Signals of TPMS_info

Tesla Model 3 CAN bus signals in `TPMS_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `TPMS_infoIndex` | selector | Tire pressure monitoring: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0`<br>1 = `DEPRECATED_1`<br>2 = `DEPRECATED_2`<br>3 = `DEPRECATED_3`<br>4 = `DEPRECATED_4`<br>5 = `DEPRECATED_5`<br>6 = `DEPRECATED_6`<br>7 = `DEPRECATED_7`<br>8 = `DEPRECATED_8`<br>9 = `DEPRECATED_9`<br>10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>15 = `BOOTLOADER_CRC`<br>16 = `SUBCOMPONENT`<br>17 = `APP_GITHASH`<br>18 = `BOOTLOADER_GITHASH`<br>19 = `VERSION_DEPRECATED`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>22 = `VARIANTCRC`<br>23 = `SUBCOMPONENT2`<br>25 = `PACKAGE_PN_1_7`<br>26 = `PACKAGE_PN_8_14`<br>27 = `PACKAGE_PN_15_20`<br>29 = `PACKAGE_SN_1_7`<br>30 = `PACKAGE_SN_8_14`<br>31 = `SUBCOMPONENT_GITHASH`<br>255 = `END` | plausible |
| `TPMS_infoComponentID` | page 10 | Tire pressure monitoring: info component ID | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `TPMS_infoPcbaID` | page 11 | Tire pressure monitoring: info pcba ID | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `TPMS_infoAssemblyID` | page 11 | Tire pressure monitoring: info assembly ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `TPMS_infoUsageID` | page 11 | Tire pressure monitoring: info usage ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `TPMS_infoApplicationCRC` | page 13 | Tire pressure monitoring: info application CRC | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `TPMS_infoBootUdsProtoVersion` | page 20 | Tire pressure monitoring: info boot uds proto version | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `TPMS_infoBootloaderCRC` | page 20 | Tire pressure monitoring: info bootloader CRC | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |

## Multiplexing

`TPMS_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (1 signals), page 11 (3 signals), page 13 (1 signals), page 20 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 CH DBC file](../../../../../dbc/Model3/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/CH.json)

## See also

- [All Tire pressure monitoring messages (TPMS)](../../tpms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
