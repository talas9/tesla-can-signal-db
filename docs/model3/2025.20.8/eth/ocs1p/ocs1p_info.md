---
layout: default
title: "OCS1P_info (0x2FE) — Occupant classification system, Tesla Model 3 2025.20.8 ETH"
description: "Occupant classification system message: info. Ethernet-side message OCS1P_info of Occupant classification system for Tesla Model 3 firmware 2025.20.8, 16 signals (OCS1P_infoIndex, OCS1P_infoBuildType, OCS1P_infoBuildConfigID, OCS1P_infoHardwareID and 12 more). Bit layout, scaling, units and value tables."
---

# OCS1P_info (0x2FE) — Occupant classification system, Tesla Model 3 2025.20.8 ETH

Occupant classification system message: info. This page documents the 16 signals of OCS1P_info as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `OCS1P_info` |
| Ethernet-side id | 0x2FE (766) |
| ECU | [Occupant classification system](../../ocs1p.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | OCS1P |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 16 |

## Signals of OCS1P_info

Tesla Model 3 CAN bus signals in `OCS1P_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `OCS1P_infoIndex` | selector | Occupant classification system: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 10 = `Mux10`<br>11 = `Mux11`<br>13 = `Mux13`<br>14 = `Mux14`<br>17 = `Mux17`<br>18 = `Mux18`<br>19 = `Mux19`<br>20 = `Mux20` | plausible |
| `OCS1P_infoBuildType` | page 10 | Occupant classification system: info build type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | validated |
| `OCS1P_infoBuildConfigID` | page 10 | Occupant classification system: info build config ID | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `OCS1P_infoHardwareID` | page 10 | Occupant classification system: info hardware ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `OCS1P_infoComponentID` | page 10 | Occupant classification system: info component ID | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `OCS1P_infoPcbaID` | page 11 | Occupant classification system: info pcba ID | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `OCS1P_infoAssemblyID` | page 11 | Occupant classification system: info assembly ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `OCS1P_infoUsageID` | page 11 | Occupant classification system: info usage ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `OCS1P_infoSubUsageID` | page 11 | Occupant classification system: info sub usage ID | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `OCS1P_infoApplicationCRC` | page 13 | Occupant classification system: info application CRC | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `OCS1P_infoBootSvnRev` | page 14 | Occupant classification system: info boot svn rev | 8\|24 | little-endian | unsigned | 1 | 0 |  | 0 to 16777215 |  | validated |
| `OCS1P_infoAppGitHashBytes` | page 17 | Occupant classification system: info app git hash bytes | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | validated |
| `OCS1P_infoBootGitHashBytes` | page 18 | Occupant classification system: info boot git hash bytes | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | validated |
| `OCS1P_infoPlatformType` | page 19 | Occupant classification system: info platform type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `OCS1P_infoBootUdsProtoVersion` | page 20 | Occupant classification system: info boot uds proto version | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `OCS1P_infoBootloaderCRC` | page 20 | Occupant classification system: info bootloader CRC | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |

## Multiplexing

`OCS1P_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (4 signals), page 11 (4 signals), page 13 (1 signals), page 14 (1 signals), page 17 (1 signals), page 18 (1 signals), page 19 (1 signals), page 20 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Occupant classification system messages (OCS1P)](../../ocs1p.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
