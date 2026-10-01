---
layout: default
title: "DI_info (0x657) — Drive inverter, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Drive inverter message: info. Ethernet-side message DI_info of Drive inverter for Tesla Model 3 / Model Y firmware 2025.20.8, 11 signals (DI_infoIndex, DI_buildType, DI_buildConfigurationId, DI_hardwareId and 7 more). Bit layout, scaling, units and value tables."
---

# DI_info (0x657) — Drive inverter, Tesla Model 3 / Model Y 2025.20.8 ETH

Drive inverter message: info. This page documents the 11 signals of DI_info as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DI_info` |
| Ethernet-side id | 0x657 (1623) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DI |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 11 |

## Signals of DI_info

Tesla Model 3 / Model Y CAN bus signals in `DI_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `DI_infoIndex` | selector | Drive inverter: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `INFO_DEPRECATED_0`<br>1 = `INFO_DEPRECATED_1`<br>2 = `INFO_DEPRECATED_2`<br>3 = `INFO_DEPRECATED_3`<br>4 = `INFO_DEPRECATED_4`<br>5 = `INFO_DEPRECATED_5`<br>6 = `INFO_DEPRECATED_6`<br>7 = `INFO_DEPRECATED_7`<br>8 = `INFO_DEPRECATED_8`<br>9 = `INFO_DEPRECATED_9`<br>10 = `INFO_BUILD_HWID_COMPONENTID`<br>11 = `INFO_PCBAID_ASSYID_USAGEID`<br>13 = `INFO_APP_CRC`<br>14 = `INFO_BOOTLOADER_SVN`<br>15 = `INFO_BOOTLOADER_CRC`<br>16 = `INFO_SUBCOMPONENT`<br>17 = `INFO_APP_GITHASH`<br>18 = `INFO_BOOTLOADER_GITHASH`<br>19 = `INFO_VERSION_DEPRECATED`<br>20 = `INFO_UDS_PROTOCOL_BOOTCRC`<br>23 = `INFO_SUBCOMPONENT2`<br>31 = `INFO_SUBCOMPONENT_GITHASH`<br>32 = `INFO_SUBCOMPONENT2_GITHASH`<br>33 = `INFO_SUBCOMPONENT_HWID`<br>34 = `INFO_SUBCOMPONENT2_HWID`<br>40 = `TRACKING_DATA_1`<br>41 = `TRACKING_DATA_2`<br>42 = `TRACKING_DATA_3`<br>43 = `TRACKING_DATA_4`<br>44 = `TRACKING_DATA_5`<br>255 = `INFO_END` | plausible |
| `DI_buildType` | page 10 | Drive inverter: build type | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | plausible |
| `DI_buildConfigurationId` | page 10 | Drive inverter: build configuration id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `DI_hardwareId` | page 10 | Drive inverter: hardware id | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 252 | 252 = `CONFIGURABLE_HWID_PLACEHOLDER` | plausible |
| `DI_componentId` | page 10 | Drive inverter: component id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `DI_pcbaId` | page 11 | Drive inverter: pcba id | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `DI_assemblyId` | page 11 | Drive inverter: assembly id | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `DI_usageId` | page 11 | Drive inverter: usage id | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `DI_subUsageId` | page 11 | Drive inverter: sub usage id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `DI_applicationCrc` | page 13 | Drive inverter: application crc | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `DI_bootGitHash` | page 18 | Drive inverter: boot git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | layout-only |

## Multiplexing

`DI_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (4 signals), page 11 (4 signals), page 13 (1 signals), page 18 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
