---
layout: default
title: "VCCC_info (0x7CA) — VCCC ECU, Tesla Model 3 2026.26.6.5 PARTY CAN"
description: "VCCC ECU message: info. Tesla Model 3 CAN bus message VCCC_info (0x7CA) of VCCC ECU, firmware 2026.26.6.5, 14 signals (VCCC_infoIndex, VCCC_infoBuildType, VCCC_infoBuildConfigId, VCCC_infoHardwareId and 10 more). Bit layout, scaling, units and value tables."
---

# VCCC_info (0x7CA) — VCCC ECU, Tesla Model 3 2026.26.6.5 PARTY CAN

VCCC ECU message: info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 14 signals of VCCC_info as defined for Tesla Model 3 firmware 2026.26.6.5 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCCC_info` |
| CAN id | 0x7CA (1994) |
| ECU | [VCCC ECU](../../vccc.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | VCCC |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 14 |

## Signals of VCCC_info

Tesla Model 3 CAN bus signals in `VCCC_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCCC_infoIndex` | selector | VCCC ECU: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0`<br>1 = `DEPRECATED_1`<br>2 = `DEPRECATED_2`<br>3 = `DEPRECATED_3`<br>4 = `DEPRECATED_4`<br>5 = `DEPRECATED_5`<br>6 = `DEPRECATED_6`<br>7 = `DEPRECATED_7`<br>8 = `DEPRECATED_8`<br>9 = `DEPRECATED_9`<br>10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>15 = `BOOTLOADER_CRC`<br>16 = `SUBCOMPONENT1`<br>17 = `APP_GITHASH`<br>18 = `BOOTLOADER_GITHASH`<br>19 = `VERSION_DEPRECATED`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>23 = `SUBCOMPONENT2`<br>24 = `SUBCOMPONENT3`<br>31 = `SUBCOMPONENT4`<br>32 = `SUBCOMPONENT5`<br>33 = `SUBCOMPONENT6`<br>34 = `SUBCOMPONENT7`<br>35 = `SUBCOMPONENT8`<br>36 = `SUBCOMPONENT9`<br>37 = `SUBCOMPONENT10`<br>38 = `SUBCOMPONENT11`<br>39 = `SUBCOMPONENT12`<br>40 = `SUBCOMPONENT13`<br>41 = `SUBCOMPONENT14`<br>255 = `END` | plausible |
| `VCCC_infoBuildType` | page 10 | VCCC ECU: info build type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | plausible |
| `VCCC_infoBuildConfigId` | page 10 | VCCC ECU: info build config id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCCC_infoHardwareId` | page 10 | VCCC ECU: info hardware id | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCCC_infoComponentId` | page 10 | VCCC ECU: info component id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCCC_infoPcbaId` | page 11 | VCCC ECU: info pcba id | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCCC_infoAssemblyId` | page 11 | VCCC ECU: info assembly id; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 254 | 1 = `ASSEMBLY1`<br>255 = `ASSEMBLY_SNA` | plausible |
| `VCCC_infoUsageId` | page 11 | VCCC ECU: info usage id | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCCC_infoSubUsageId` | page 11 | VCCC ECU: info sub usage id | 40\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `VCCC_infoAppCrc` | page 13 | VCCC ECU: info app crc | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `VCCC_infoAppGitHash` | page 17 | VCCC ECU: info app git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | layout-only |
| `VCCC_infoBootGitHash` | page 18 | VCCC ECU: info boot git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | layout-only |
| `VCCC_infoBootUdsProtoVersion` | page 20 | VCCC ECU: info boot uds proto version | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `VCCC_infoBootCrc` | page 20 | VCCC ECU: info boot crc | 24\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |

## Multiplexing

`VCCC_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (4 signals), page 11 (4 signals), page 13 (1 signals), page 17 (1 signals), page 18 (1 signals), page 20 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 PARTY DBC file](../../../../../dbc/Model3/2026.26.6.5/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/PARTY.json)

## See also

- [All VCCC ECU messages (VCCC)](../../vccc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
