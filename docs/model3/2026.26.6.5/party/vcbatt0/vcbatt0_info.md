---
layout: default
title: "VCBATT0_info (0x652) — VCBATT0 ECU, Tesla Model 3 2026.26.6.5 PARTY CAN"
description: "VCBATT0 ECU message: info. Tesla Model 3 CAN bus message VCBATT0_info (0x652) of VCBATT0 ECU, firmware 2026.26.6.5, 14 signals (VCBATT0_infoIndex, VCBATT0_infoBuildType, VCBATT0_infoBuildConfigId, VCBATT0_infoHardwareId and 10 more). Bit layout, scaling, units and value tables."
---

# VCBATT0_info (0x652) — VCBATT0 ECU, Tesla Model 3 2026.26.6.5 PARTY CAN

VCBATT0 ECU message: info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 14 signals of VCBATT0_info as defined for Tesla Model 3 firmware 2026.26.6.5 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCBATT0_info` |
| CAN id | 0x652 (1618) |
| ECU | [VCBATT0 ECU](../../vcbatt0.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | VCBATT0 |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 14 |

## Signals of VCBATT0_info

Tesla Model 3 CAN bus signals in `VCBATT0_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCBATT0_infoIndex` | selector | VCBATT0 ECU: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0`<br>1 = `DEPRECATED_1`<br>2 = `DEPRECATED_2`<br>3 = `DEPRECATED_3`<br>4 = `DEPRECATED_4`<br>5 = `DEPRECATED_5`<br>6 = `DEPRECATED_6`<br>7 = `DEPRECATED_7`<br>8 = `DEPRECATED_8`<br>9 = `DEPRECATED_9`<br>10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>15 = `BOOTLOADER_CRC`<br>16 = `SUBCOMPONENT1`<br>17 = `APP_GITHASH`<br>18 = `BOOTLOADER_GITHASH`<br>19 = `VERSION_DEPRECATED`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>23 = `SUBCOMPONENT2`<br>24 = `SUBCOMPONENT3`<br>31 = `SUBCOMPONENT4`<br>32 = `SUBCOMPONENT5`<br>33 = `SUBCOMPONENT6`<br>34 = `SUBCOMPONENT7`<br>35 = `SUBCOMPONENT8`<br>36 = `SUBCOMPONENT9`<br>37 = `SUBCOMPONENT10`<br>38 = `SUBCOMPONENT11`<br>39 = `SUBCOMPONENT12`<br>40 = `SUBCOMPONENT13`<br>41 = `SUBCOMPONENT14`<br>255 = `END` | plausible |
| `VCBATT0_infoBuildType` | page 10 | VCBATT0 ECU: info build type | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | plausible |
| `VCBATT0_infoBuildConfigId` | page 10 | VCBATT0 ECU: info build config id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCBATT0_infoHardwareId` | page 10 | VCBATT0 ECU: info hardware id | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCBATT0_infoComponentId` | page 10 | VCBATT0 ECU: info component id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCBATT0_infoPcbaId` | page 11 | VCBATT0 ECU: info pcba id | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCBATT0_infoAssemblyId` | page 11 | VCBATT0 ECU: info assembly id; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 254 | 1 = `ASSEMBLY1`<br>255 = `ASSEMBLY_SNA` | plausible |
| `VCBATT0_infoUsageId` | page 11 | VCBATT0 ECU: info usage id | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCBATT0_infoSubUsageId` | page 11 | VCBATT0 ECU: info sub usage id | 40\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCBATT0_infoAppCrc` | page 13 | VCBATT0 ECU: info app crc | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `VCBATT0_infoAppGitHash` | page 17 | VCBATT0 ECU: info app git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | layout-only |
| `VCBATT0_infoBootGitHash` | page 18 | VCBATT0 ECU: info boot git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | layout-only |
| `VCBATT0_infoBootUdsProtoVersion` | page 20 | VCBATT0 ECU: info boot uds proto version | 8\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCBATT0_infoBootCrc` | page 20 | VCBATT0 ECU: info boot crc | 24\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |

## Multiplexing

`VCBATT0_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (4 signals), page 11 (4 signals), page 13 (1 signals), page 17 (1 signals), page 18 (1 signals), page 20 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 PARTY DBC file](../../../../../dbc/Model3/2026.26.6.5/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/PARTY.json)

## See also

- [All VCBATT0 ECU messages (VCBATT0)](../../vcbatt0.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
