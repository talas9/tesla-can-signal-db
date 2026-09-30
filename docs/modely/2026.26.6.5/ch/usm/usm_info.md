---
layout: default
title: "USM_info (0x327) — USM ECU, Tesla Model Y 2026.26.6.5 CH CAN"
description: "USM ECU message: info. Tesla Model Y CAN bus message USM_info (0x327) of USM ECU, firmware 2026.26.6.5, 10 signals (USM_infoIndex, USM_infoBuildType, USM_infoBuildConfigId, USM_infoHardwareId and 6 more). Bit layout, scaling, units and value tables."
---

# USM_info (0x327) — USM ECU, Tesla Model Y 2026.26.6.5 CH CAN

USM ECU message: info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 10 signals of USM_info as defined for Tesla Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `USM_info` |
| CAN id | 0x327 (807) |
| ECU | [USM ECU](../../usm.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | USM |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 10 |

## Signals of USM_info

Tesla Model Y CAN bus signals in `USM_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `USM_infoIndex` | selector | USM ECU: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0`<br>1 = `DEPRECATED_1`<br>2 = `DEPRECATED_2`<br>3 = `DEPRECATED_3`<br>4 = `DEPRECATED_4`<br>5 = `DEPRECATED_5`<br>6 = `DEPRECATED_6`<br>7 = `DEPRECATED_7`<br>8 = `DEPRECATED_8`<br>9 = `DEPRECATED_9`<br>10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>15 = `BOOTLOADER_CRC`<br>16 = `SUBCOMPONENT1`<br>17 = `APP_GITHASH`<br>18 = `BOOTLOADER_GITHASH`<br>19 = `VERSION_DEPRECATED`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>23 = `SUBCOMPONENT2`<br>24 = `SUBCOMPONENT3`<br>31 = `SUBCOMPONENT4`<br>32 = `SUBCOMPONENT5`<br>33 = `SUBCOMPONENT6`<br>34 = `SUBCOMPONENT7`<br>35 = `SUBCOMPONENT8`<br>36 = `SUBCOMPONENT9`<br>37 = `SUBCOMPONENT10`<br>38 = `SUBCOMPONENT11`<br>39 = `SUBCOMPONENT12`<br>40 = `SUBCOMPONENT13`<br>41 = `SUBCOMPONENT14`<br>255 = `END` | plausible |
| `USM_infoBuildType` | page 10 | USM ECU: info build type | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | validated |
| `USM_infoBuildConfigId` | page 10 | USM ECU: info build config id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `USM_infoHardwareId` | page 10 | USM ECU: info hardware id | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `USM_infoComponentId` | page 10 | USM ECU: info component id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `USM_infoPcbaId` | page 11 | USM ECU: info pcba id | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `USM_infoAssemblyId` | page 11 | USM ECU: info assembly id; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 254 | 1 = `ASSEMBLY1`<br>255 = `ASSEMBLY_SNA` | validated |
| `USM_infoUsageId` | page 11 | USM ECU: info usage id | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `USM_infoSubUsageId` | page 11 | USM ECU: info sub usage id | 40\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `USM_infoAppCrc` | page 13 | USM ECU: info app crc | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |

## Multiplexing

`USM_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (4 signals), page 11 (4 signals), page 13 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/ModelY/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/CH.json)

## See also

- [All USM ECU messages (USM)](../../usm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
