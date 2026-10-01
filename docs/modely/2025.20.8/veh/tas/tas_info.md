---
layout: default
title: "TAS_info (0x54D) — Air suspension controller, Tesla Model Y 2025.20.8 VEH CAN"
description: "Air suspension controller message: info. Tesla Model Y CAN bus message TAS_info (0x54D) of Air suspension controller, firmware 2025.20.8, 17 signals (TAS_infoIndex, TAS_infoBuildType, TAS_infoBuildConfigId, TAS_infoHardwareId and 13 more). Bit layout, scaling, units and value tables."
---

# TAS_info (0x54D) — Air suspension controller, Tesla Model Y 2025.20.8 VEH CAN

Air suspension controller message: info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 17 signals of TAS_info as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `TAS_info` |
| CAN id | 0x54D (1357) |
| ECU | [Air suspension controller](../../tas.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | TAS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 17 |

## Signals of TAS_info

Tesla Model Y CAN bus signals in `TAS_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `TAS_infoIndex` | selector | Air suspension controller: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0`<br>1 = `DEPRECATED_1`<br>2 = `DEPRECATED_2`<br>3 = `DEPRECATED_3`<br>4 = `DEPRECATED_4`<br>5 = `DEPRECATED_5`<br>6 = `DEPRECATED_6`<br>7 = `DEPRECATED_7`<br>8 = `DEPRECATED_8`<br>9 = `DEPRECATED_9`<br>10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>15 = `BOOTLOADER_CRC`<br>16 = `SUBCOMPONENT1`<br>17 = `APP_GITHASH`<br>18 = `BOOTLOADER_GITHASH`<br>19 = `VERSION_DEPRECATED`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>23 = `SUBCOMPONENT2`<br>24 = `SUBCOMPONENT3`<br>31 = `SUBCOMPONENT4`<br>32 = `SUBCOMPONENT5`<br>33 = `SUBCOMPONENT6`<br>34 = `SUBCOMPONENT7`<br>35 = `SUBCOMPONENT8`<br>36 = `SUBCOMPONENT9`<br>37 = `SUBCOMPONENT10`<br>38 = `SUBCOMPONENT11`<br>39 = `SUBCOMPONENT12`<br>40 = `SUBCOMPONENT13`<br>41 = `SUBCOMPONENT14`<br>255 = `END` | plausible |
| `TAS_infoBuildType` | page 10 | Air suspension controller: info build type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | plausible |
| `TAS_infoBuildConfigId` | page 10 | Air suspension controller: info build config id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `TAS_infoHardwareId` | page 10 | Air suspension controller: info hardware id | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TAS_infoComponentId` | page 10 | Air suspension controller: info component id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `TAS_infoPcbaId` | page 11 | Air suspension controller: info pcba id | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `TAS_infoAssemblyId` | page 11 | Air suspension controller: info assembly id; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 254 | 1 = `ASSEMBLY1`<br>255 = `ASSEMBLY_SNA` | plausible |
| `TAS_infoUsageId` | page 11 | Air suspension controller: info usage id | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `TAS_infoSubUsageId` | page 11 | Air suspension controller: info sub usage id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `TAS_infoAppCrc` | page 13 | Air suspension controller: info app crc | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TAS_infoAppGitHash` | page 17 | Air suspension controller: info app git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | layout-only |
| `TAS_infoBootGitHash` | page 18 | Air suspension controller: info boot git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | layout-only |
| `TAS_infoPlatformType` | page 19 | Air suspension controller: info platform type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `TAS_infoMajorVersion` | page 19 | Air suspension controller: info major version; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 254 | 254 = `LOCAL_BUILD`<br>255 = `SNA` | plausible |
| `TAS_infoBranchOrigin` | page 19 | Air suspension controller: info branch origin; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 254 | 254 = `LOCAL_BUILD`<br>255 = `SNA` | plausible |
| `TAS_infoMaturity` | page 19 | Air suspension controller: info maturity; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 254 | 254 = `LOCAL_BUILD`<br>255 = `SNA` | plausible |
| `TAS_infoHardwareRevision` | page 19 | Air suspension controller: info hardware revision; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 254 | 254 = `LOCAL_BUILD`<br>255 = `SNA` | plausible |

## Multiplexing

`TAS_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (4 signals), page 11 (4 signals), page 13 (1 signals), page 17 (1 signals), page 18 (1 signals), page 19 (5 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All Air suspension controller messages (TAS)](../../tas.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
