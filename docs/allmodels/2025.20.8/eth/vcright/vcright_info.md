---
layout: default
title: "VCRIGHT_info (0x306) — Right body controller, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Right body controller message: info. Ethernet-side message VCRIGHT_info of Right body controller for Tesla Model 3 / Model Y firmware 2025.20.8, 15 signals (VCRIGHT_infoIndex, VCRIGHT_infoBuildType, VCRIGHT_infoBuildConfigId, VCRIGHT_infoHardwareId and 11 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_info (0x306) — Right body controller, Tesla Model 3 / Model Y 2025.20.8 ETH

Right body controller message: info. This page documents the 15 signals of VCRIGHT_info as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_info` |
| Ethernet-side id | 0x306 (774) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 15 |

## Signals of VCRIGHT_info

Tesla Model 3 / Model Y CAN bus signals in `VCRIGHT_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_infoIndex` | selector | Right body controller: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0`<br>1 = `DEPRECATED_1`<br>2 = `DEPRECATED_2`<br>3 = `DEPRECATED_3`<br>4 = `DEPRECATED_4`<br>5 = `DEPRECATED_5`<br>6 = `DEPRECATED_6`<br>7 = `DEPRECATED_7`<br>8 = `DEPRECATED_8`<br>9 = `DEPRECATED_9`<br>10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>15 = `BOOTLOADER_CRC`<br>16 = `SUBCOMPONENT1`<br>17 = `APP_GITHASH`<br>18 = `BOOTLOADER_GITHASH`<br>19 = `VERSION_DEPRECATED`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>23 = `SUBCOMPONENT2`<br>24 = `SUBCOMPONENT3`<br>31 = `SUBCOMPONENT4`<br>32 = `SUBCOMPONENT5`<br>33 = `SUBCOMPONENT6`<br>34 = `SUBCOMPONENT7`<br>35 = `SUBCOMPONENT8`<br>36 = `SUBCOMPONENT9`<br>37 = `SUBCOMPONENT10`<br>38 = `SUBCOMPONENT11`<br>39 = `SUBCOMPONENT12`<br>40 = `SUBCOMPONENT13`<br>41 = `SUBCOMPONENT14`<br>255 = `END` | plausible |
| `VCRIGHT_infoBuildType` | page 10 | Right body controller: info build type | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | plausible |
| `VCRIGHT_infoBuildConfigId` | page 10 | Right body controller: info build config id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | plausible |
| `VCRIGHT_infoHardwareId` | page 10 | Right body controller: info hardware id | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | plausible |
| `VCRIGHT_infoComponentId` | page 10 | Right body controller: info component id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | plausible |
| `VCRIGHT_infoPcbaId` | page 11 | Right body controller: info pcba id | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `VCRIGHT_infoAssemblyId` | page 11 | Right body controller: info assembly id; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 254 | 1 = `ASSEMBLY1`<br>255 = `ASSEMBLY_SNA` | plausible |
| `VCRIGHT_infoUsageId` | page 11 | Right body controller: info usage id | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | plausible |
| `VCRIGHT_infoSubUsageId` | page 11 | Right body controller: info sub usage id | 40\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | plausible |
| `VCRIGHT_infoAppCrc` | page 13 | Right body controller: info app crc | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `VCRIGHT_infoAppGitHash` | page 17 | Right body controller: info app git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | plausible |
| `VCRIGHT_infoBootGitHash` | page 18 | Right body controller: info boot git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | plausible |
| `VCRIGHT_infoPlatformType` | page 19 | Right body controller: info platform type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `VCRIGHT_infoBootUdsProtoVersion` | page 20 | Right body controller: info boot uds proto version | 8\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | plausible |
| `VCRIGHT_infoBootCrc` | page 20 | Right body controller: info boot crc | 24\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |

## Multiplexing

`VCRIGHT_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (4 signals), page 11 (4 signals), page 13 (1 signals), page 17 (1 signals), page 18 (1 signals), page 19 (1 signals), page 20 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
