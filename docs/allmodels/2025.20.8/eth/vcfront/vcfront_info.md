---
layout: default
title: "VCFRONT_info (0x301) — Front body controller, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Front body controller message: info. Ethernet-side message VCFRONT_info of Front body controller for Tesla Model 3 / Model Y firmware 2025.20.8, 17 signals (VCFRONT_infoIndex, VCFRONT_infoBuildType, VCFRONT_infoBuildConfigId, VCFRONT_infoHardwareId and 13 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_info (0x301) — Front body controller, Tesla Model 3 / Model Y 2025.20.8 ETH

Front body controller message: info. This page documents the 17 signals of VCFRONT_info as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_info` |
| Ethernet-side id | 0x301 (769) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCFRONT |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 17 |

## Signals of VCFRONT_info

Tesla Model 3 / Model Y CAN bus signals in `VCFRONT_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_infoIndex` | selector | Front body controller: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0`<br>1 = `DEPRECATED_1`<br>2 = `DEPRECATED_2`<br>3 = `DEPRECATED_3`<br>4 = `DEPRECATED_4`<br>5 = `DEPRECATED_5`<br>6 = `DEPRECATED_6`<br>7 = `DEPRECATED_7`<br>8 = `DEPRECATED_8`<br>9 = `DEPRECATED_9`<br>10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>15 = `BOOTLOADER_CRC`<br>16 = `SUBCOMPONENT1`<br>17 = `APP_GITHASH`<br>18 = `BOOTLOADER_GITHASH`<br>19 = `VERSION_DEPRECATED`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>23 = `SUBCOMPONENT2`<br>24 = `SUBCOMPONENT3`<br>31 = `SUBCOMPONENT4`<br>32 = `SUBCOMPONENT5`<br>33 = `SUBCOMPONENT6`<br>34 = `SUBCOMPONENT7`<br>35 = `SUBCOMPONENT8`<br>36 = `SUBCOMPONENT9`<br>37 = `SUBCOMPONENT10`<br>38 = `SUBCOMPONENT11`<br>39 = `SUBCOMPONENT12`<br>40 = `SUBCOMPONENT13`<br>41 = `SUBCOMPONENT14`<br>255 = `END` | plausible |
| `VCFRONT_infoBuildType` | page 10 | Front body controller: info build type | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | validated |
| `VCFRONT_infoBuildConfigId` | page 10 | Front body controller: info build config id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCFRONT_infoHardwareId` | page 10 | Front body controller: info hardware id | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCFRONT_infoComponentId` | page 10 | Front body controller: info component id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCFRONT_infoPcbaId` | page 11 | Front body controller: info pcba id | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCFRONT_infoAssemblyId` | page 11 | Front body controller: info assembly id; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 254 | 1 = `ASSEMBLY1`<br>255 = `ASSEMBLY_SNA` | validated |
| `VCFRONT_infoUsageId` | page 11 | Front body controller: info usage id | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCFRONT_infoSubUsageId` | page 11 | Front body controller: info sub usage id | 40\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCFRONT_infoAppCrc` | page 13 | Front body controller: info app crc | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VC_infoHCMLAppCRC` | page 16 | Front body controller: info HCML app CRC | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCFRONT_infoAppGitHash` | page 17 | Front body controller: info app git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | validated |
| `VCFRONT_infoBootGitHash` | page 18 | Front body controller: info boot git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | validated |
| `VCFRONT_infoPlatformType` | page 19 | Front body controller: info platform type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCFRONT_infoBootUdsProtoVersion` | page 20 | Front body controller: info boot uds proto version | 8\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCFRONT_infoBootCrc` | page 20 | Front body controller: info boot crc | 24\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VC_infoHCMRAppCRC` | page 23 | Front body controller: info HCMR app CRC | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |

## Multiplexing

`VCFRONT_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (4 signals), page 11 (4 signals), page 13 (1 signals), page 16 (1 signals), page 17 (1 signals), page 18 (1 signals), page 19 (1 signals), page 20 (2 signals), page 23 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
