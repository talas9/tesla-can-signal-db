---
layout: default
title: "PM_info (0x60F) — PM ECU, Tesla Model 3 2025.20.8 VEH CAN"
description: "PM ECU message: info. Tesla Model 3 CAN bus message PM_info (0x60F) of PM ECU, firmware 2025.20.8, 12 signals (PM_infoIndex, PM_buildType, PM_buildConfigurationId, PM_hardwareId and 8 more). Bit layout, scaling, units and value tables."
---

# PM_info (0x60F) — PM ECU, Tesla Model 3 2025.20.8 VEH CAN

PM ECU message: info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 12 signals of PM_info as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PM_info` |
| CAN id | 0x60F (1551) |
| ECU | [PM ECU](../../pm.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | PM |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 12 |

## Signals of PM_info

Tesla Model 3 CAN bus signals in `PM_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `PM_infoIndex` | selector | PM ECU: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0`<br>1 = `DEPRECATED_1`<br>2 = `DEPRECATED_2`<br>3 = `DEPRECATED_3`<br>4 = `DEPRECATED_4`<br>5 = `DEPRECATED_5`<br>6 = `DEPRECATED_6`<br>7 = `DEPRECATED_7`<br>8 = `DEPRECATED_8`<br>9 = `DEPRECATED_9`<br>10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>15 = `BOOTLOADER_CRC`<br>16 = `SUBCOMPONENT`<br>17 = `APP_GITHASH`<br>18 = `BOOTLOADER_GITHASH`<br>19 = `VERSION_DEPRECATED`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>21 = `DI_BUILD_DATA`<br>255 = `END` | plausible |
| `PM_buildType` | page 10 | PM ECU: build type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | validated |
| `PM_buildConfigurationId` | page 10 | PM ECU: build configuration id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `PM_hardwareId` | page 10 | PM ECU: hardware id | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 252 | 252 = `CONFIGURABLE_HWID_PLACEHOLDER` | validated |
| `PM_deviceFused` | page 10 | PM ECU: device fused | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PM_componentId` | page 10 | PM ECU: component id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `PM_pcbaId` | page 11 | PM ECU: pcba id | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `PM_assemblyId` | page 11 | PM ECU: assembly id | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `PM_usageId` | page 11 | PM ECU: usage id | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `PM_subUsageId` | page 11 | PM ECU: sub usage id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `PM_applicationCrc` | page 13 | PM ECU: application crc | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `PM_bootGitHash` | page 18 | PM ECU: boot git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | validated |

## Multiplexing

`PM_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (5 signals), page 11 (4 signals), page 13 (1 signals), page 18 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All PM ECU messages (PM)](../../pm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
