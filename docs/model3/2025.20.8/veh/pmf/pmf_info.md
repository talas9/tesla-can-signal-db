---
layout: default
title: "PMF_info (0x316) — PMF ECU, Tesla Model 3 2025.20.8 VEH CAN"
description: "PMF ECU message: info. Tesla Model 3 CAN bus message PMF_info (0x316) of PMF ECU, firmware 2025.20.8, 16 signals (PMF_infoIndex, PMF_buildType, PMF_buildConfigurationId, PMF_hardwareId and 12 more). Bit layout, scaling, units and value tables."
---

# PMF_info (0x316) — PMF ECU, Tesla Model 3 2025.20.8 VEH CAN

PMF ECU message: info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 16 signals of PMF_info as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PMF_info` |
| CAN id | 0x316 (790) |
| ECU | [PMF ECU](../../pmf.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | PMF |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 16 |

## Signals of PMF_info

Tesla Model 3 CAN bus signals in `PMF_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `PMF_infoIndex` | selector | PMF ECU: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0`<br>1 = `DEPRECATED_1`<br>2 = `DEPRECATED_2`<br>3 = `DEPRECATED_3`<br>4 = `DEPRECATED_4`<br>5 = `DEPRECATED_5`<br>6 = `DEPRECATED_6`<br>7 = `DEPRECATED_7`<br>8 = `DEPRECATED_8`<br>9 = `DEPRECATED_9`<br>10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>15 = `BOOTLOADER_CRC`<br>16 = `SUBCOMPONENT`<br>17 = `APP_GITHASH`<br>18 = `BOOTLOADER_GITHASH`<br>19 = `VERSION_DEPRECATED`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>21 = `DI_BUILD_DATA`<br>255 = `END` | plausible |
| `PMF_buildType` | page 10 | PMF ECU: build type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | plausible |
| `PMF_buildConfigurationId` | page 10 | PMF ECU: build configuration id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PMF_hardwareId` | page 10 | PMF ECU: hardware id | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 252 | 252 = `CONFIGURABLE_HWID_PLACEHOLDER` | plausible |
| `PMF_deviceFused` | page 10 | PMF ECU: device fused | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_componentId` | page 10 | PMF ECU: component id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PMF_pcbaId` | page 11 | PMF ECU: pcba id | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PMF_assemblyId` | page 11 | PMF ECU: assembly id | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PMF_usageId` | page 11 | PMF ECU: usage id | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PMF_subUsageId` | page 11 | PMF ECU: sub usage id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PMF_applicationCrc` | page 13 | PMF ECU: application crc | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `PMF_appGitHash` | page 17 | PMF ECU: app git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | layout-only |
| `PMF_bootGitHash` | page 18 | PMF ECU: boot git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | layout-only |
| `PMF_platformTyp` | page 19 | PMF ECU: platform typ | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PMF_udsProtocolVersion` | page 20 | PMF ECU: uds protocol version | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PMF_bootloaderCrc` | page 20 | PMF ECU: bootloader crc | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |

## Multiplexing

`PMF_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (5 signals), page 11 (4 signals), page 13 (1 signals), page 17 (1 signals), page 18 (1 signals), page 19 (1 signals), page 20 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All PMF ECU messages (PMF)](../../pmf.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
