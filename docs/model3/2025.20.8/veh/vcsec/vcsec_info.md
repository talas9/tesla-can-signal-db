---
layout: default
title: "VCSEC_info (0x319) — Vehicle security controller, Tesla Model 3 2025.20.8 VEH CAN"
description: "Vehicle security controller message: info. Tesla Model 3 CAN bus message VCSEC_info (0x319) of Vehicle security controller, firmware 2025.20.8, 19 signals (VCSEC_infoIndex, VCSEC_infoBuildType, VCSEC_infoBuildConfigId, VCSEC_infoHardwareId and 15 more). Bit layout, scaling, units and value tables."
---

# VCSEC_info (0x319) — Vehicle security controller, Tesla Model 3 2025.20.8 VEH CAN

Vehicle security controller message: info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 19 signals of VCSEC_info as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEC_info` |
| CAN id | 0x319 (793) |
| ECU | [Vehicle security controller](../../vcsec.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCSEC |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 19 |

## Signals of VCSEC_info

Tesla Model 3 CAN bus signals in `VCSEC_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEC_infoIndex` | selector | Vehicle security controller: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0`<br>1 = `DEPRECATED_1`<br>2 = `DEPRECATED_2`<br>3 = `DEPRECATED_3`<br>4 = `DEPRECATED_4`<br>5 = `DEPRECATED_5`<br>6 = `DEPRECATED_6`<br>7 = `DEPRECATED_7`<br>8 = `DEPRECATED_8`<br>9 = `DEPRECATED_9`<br>10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>15 = `BOOTLOADER_CRC`<br>16 = `SUBCOMPONENT1`<br>17 = `APP_GITHASH`<br>18 = `BOOTLOADER_GITHASH`<br>19 = `VERSION_DEPRECATED`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>23 = `SUBCOMPONENT2`<br>24 = `SUBCOMPONENT3`<br>31 = `SUBCOMPONENT4`<br>32 = `SUBCOMPONENT5`<br>33 = `SUBCOMPONENT6`<br>34 = `SUBCOMPONENT7`<br>35 = `SUBCOMPONENT8`<br>36 = `SUBCOMPONENT9`<br>37 = `SUBCOMPONENT10`<br>38 = `SUBCOMPONENT11`<br>39 = `SUBCOMPONENT12`<br>40 = `SUBCOMPONENT13`<br>41 = `SUBCOMPONENT14`<br>255 = `END` | plausible |
| `VCSEC_infoBuildType` | page 10 | Vehicle security controller: info build type | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | plausible |
| `VCSEC_infoBuildConfigId` | page 10 | Vehicle security controller: info build config id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCSEC_infoHardwareId` | page 10 | Vehicle security controller: info hardware id | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCSEC_infoComponentId` | page 10 | Vehicle security controller: info component id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCSEC_infoPcbaId` | page 11 | Vehicle security controller: info pcba id | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_infoAssemblyId` | page 11 | Vehicle security controller: info assembly id; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 254 | 1 = `ASSEMBLY1`<br>255 = `ASSEMBLY_SNA` | plausible |
| `VCSEC_infoUsageId` | page 11 | Vehicle security controller: info usage id | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCSEC_infoSubUsageId` | page 11 | Vehicle security controller: info sub usage id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCSEC_infoAppCrc` | page 13 | Vehicle security controller: info app crc | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `VCSEC_infoSubcomponent1` | page 16 | Vehicle security controller: info subcomponent1 | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `VCSEC_infoAppGitHash` | page 17 | Vehicle security controller: info app git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | layout-only |
| `VCSEC_infoBootGitHash` | page 18 | Vehicle security controller: info boot git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | layout-only |
| `VCSEC_infoPlatformType` | page 19 | Vehicle security controller: info platform type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCSEC_infoBootUdsProtoVersion` | page 20 | Vehicle security controller: info boot uds proto version | 8\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCSEC_infoBootCrc` | page 20 | Vehicle security controller: info boot crc | 24\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `VCSEC_infoSubcomponent2` | page 23 | Vehicle security controller: info subcomponent2 | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `VCSEC_infoSubcomponent3` | page 24 | Vehicle security controller: info subcomponent3 | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `VCSEC_infoSubcomponent4` | page 31 | Vehicle security controller: info subcomponent4 | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |

## Multiplexing

`VCSEC_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (4 signals), page 11 (4 signals), page 13 (1 signals), page 16 (1 signals), page 17 (1 signals), page 18 (1 signals), page 19 (1 signals), page 20 (2 signals), page 23 (1 signals), page 24 (1 signals), page 31 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All Vehicle security controller messages (VCSEC)](../../vcsec.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
