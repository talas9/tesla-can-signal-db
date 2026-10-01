---
layout: default
title: "EPBL_info (0x7C8) — Left electric parking brake, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Left electric parking brake message: info. Tesla Model 3 CAN bus message EPBL_info (0x7C8) of Left electric parking brake, firmware 2026.26.6.5, 15 signals (EPBL_infoIndex, EPBL_infoBuildType, EPBL_infoBuildConfigId, EPBL_infoHardwareId and 11 more). Bit layout, scaling, units and value tables."
---

# EPBL_info (0x7C8) — Left electric parking brake, Tesla Model 3 2026.26.6.5 VEH CAN

Left electric parking brake message: info; frame length observed on a vehicle bus. This page documents the 15 signals of EPBL_info as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `EPBL_info` |
| CAN id | 0x7C8 (1992) |
| ECU | [Left electric parking brake](../../epbl.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | EPBL |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 15 |

## Signals of EPBL_info

Tesla Model 3 CAN bus signals in `EPBL_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `EPBL_infoIndex` | selector | Left electric parking brake: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0`<br>1 = `DEPRECATED_1`<br>2 = `DEPRECATED_2`<br>3 = `DEPRECATED_3`<br>4 = `DEPRECATED_4`<br>5 = `DEPRECATED_5`<br>6 = `DEPRECATED_6`<br>7 = `DEPRECATED_7`<br>8 = `DEPRECATED_8`<br>9 = `DEPRECATED_9`<br>10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>15 = `BOOTLOADER_CRC`<br>16 = `SUBCOMPONENT1`<br>17 = `APP_GITHASH`<br>18 = `BOOTLOADER_GITHASH`<br>19 = `VERSION_DEPRECATED`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>23 = `SUBCOMPONENT2`<br>24 = `SUBCOMPONENT3`<br>31 = `SUBCOMPONENT4`<br>32 = `SUBCOMPONENT5`<br>33 = `SUBCOMPONENT6`<br>34 = `SUBCOMPONENT7`<br>35 = `SUBCOMPONENT8`<br>36 = `SUBCOMPONENT9`<br>37 = `SUBCOMPONENT10`<br>38 = `SUBCOMPONENT11`<br>39 = `SUBCOMPONENT12`<br>40 = `SUBCOMPONENT13`<br>41 = `SUBCOMPONENT14`<br>255 = `END` | validated |
| `EPBL_infoBuildType` | page 10 | Left electric parking brake: info build type | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | validated |
| `EPBL_infoBuildConfigId` | page 10 | Left electric parking brake: info build config id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `EPBL_infoHardwareId` | page 10 | Left electric parking brake: info hardware id | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `EPBL_infoComponentId` | page 10 | Left electric parking brake: info component id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `EPBL_infoPcbaId` | page 11 | Left electric parking brake: info pcba id | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `EPBL_infoAssemblyId` | page 11 | Left electric parking brake: info assembly id; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 254 | 1 = `ASSEMBLY1`<br>255 = `ASSEMBLY_SNA` | validated |
| `EPBL_infoUsageId` | page 11 | Left electric parking brake: info usage id | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `EPBL_infoSubUsageId` | page 11 | Left electric parking brake: info sub usage id | 40\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `EPBL_infoAppCrc` | page 13 | Left electric parking brake: info app crc | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `EPBL_infoAppGitHash` | page 17 | Left electric parking brake: info app git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | validated |
| `EPBL_infoBootGitHash` | page 18 | Left electric parking brake: info boot git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | validated |
| `EPBL_infoPlatformType` | page 19 | Left electric parking brake: info platform type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `EPBL_infoBootUdsProtoVersion` | page 20 | Left electric parking brake: info boot uds proto version | 8\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `EPBL_infoBootCrc` | page 20 | Left electric parking brake: info boot crc | 24\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |

## Multiplexing

`EPBL_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (4 signals), page 11 (4 signals), page 13 (1 signals), page 17 (1 signals), page 18 (1 signals), page 19 (1 signals), page 20 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Left electric parking brake messages (EPBL)](../../epbl.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
