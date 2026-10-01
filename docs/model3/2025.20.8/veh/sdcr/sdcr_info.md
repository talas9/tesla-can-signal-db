---
layout: default
title: "SDCR_info (0x63D) — SDCR ECU, Tesla Model 3 2025.20.8 VEH CAN"
description: "SDCR ECU message: info. Tesla Model 3 CAN bus message SDCR_info (0x63D) of SDCR ECU, firmware 2025.20.8, 11 signals (SDCR_infoIndex, SDCR_infoBuildType, SDCR_infoBuildConfigId, SDCR_infoHardwareId and 7 more). Bit layout, scaling, units and value tables."
---

# SDCR_info (0x63D) — SDCR ECU, Tesla Model 3 2025.20.8 VEH CAN

SDCR ECU message: info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 11 signals of SDCR_info as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `SDCR_info` |
| CAN id | 0x63D (1597) |
| ECU | [SDCR ECU](../../sdcr.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | SDCR |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 11 |

## Signals of SDCR_info

Tesla Model 3 CAN bus signals in `SDCR_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `SDCR_infoIndex` | selector | SDCR ECU: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0`<br>1 = `DEPRECATED_1`<br>2 = `DEPRECATED_2`<br>3 = `DEPRECATED_3`<br>4 = `DEPRECATED_4`<br>5 = `DEPRECATED_5`<br>6 = `DEPRECATED_6`<br>7 = `DEPRECATED_7`<br>8 = `DEPRECATED_8`<br>9 = `DEPRECATED_9`<br>10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>15 = `BOOTLOADER_CRC`<br>16 = `SUBCOMPONENT1`<br>17 = `APP_GITHASH`<br>18 = `BOOTLOADER_GITHASH`<br>19 = `VERSION_DEPRECATED`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>23 = `SUBCOMPONENT2`<br>24 = `SUBCOMPONENT3`<br>31 = `SUBCOMPONENT4`<br>32 = `SUBCOMPONENT5`<br>33 = `SUBCOMPONENT6`<br>34 = `SUBCOMPONENT7`<br>35 = `SUBCOMPONENT8`<br>36 = `SUBCOMPONENT9`<br>37 = `SUBCOMPONENT10`<br>38 = `SUBCOMPONENT11`<br>39 = `SUBCOMPONENT12`<br>40 = `SUBCOMPONENT13`<br>41 = `SUBCOMPONENT14`<br>255 = `END` | plausible |
| `SDCR_infoBuildType` | page 10 | SDCR ECU: info build type | 13\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | plausible |
| `SDCR_infoBuildConfigId` | page 10 | SDCR ECU: info build config id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `SDCR_infoHardwareId` | page 10 | SDCR ECU: info hardware id | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `SDCR_infoComponentId` | page 10 | SDCR ECU: info component id | 55\|16 | big-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `SDCR_infoPcbaId` | page 11 | SDCR ECU: info pcba id | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `SDCR_infoAssemblyId` | page 11 | SDCR ECU: info assembly id | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `SDCR_infoUsageId` | page 11 | SDCR ECU: info usage id | 31\|16 | big-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `SDCR_infoSubUsageId` | page 11 | SDCR ECU: info sub usage id | 40\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `SDCR_infoAppCrc` | page 13 | SDCR ECU: info app crc | 15\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `SDCR_infoBootGitHash` | page 18 | SDCR ECU: info boot git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | layout-only |

## Multiplexing

`SDCR_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (4 signals), page 11 (4 signals), page 13 (1 signals), page 18 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All SDCR ECU messages (SDCR)](../../sdcr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
