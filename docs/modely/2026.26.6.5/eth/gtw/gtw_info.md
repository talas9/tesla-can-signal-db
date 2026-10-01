---
layout: default
title: "GTW_info (0x3C) — Gateway, Tesla Model Y 2026.26.6.5 ETH"
description: "Gateway message: info. Ethernet-side message GTW_info of Gateway for Tesla Model Y firmware 2026.26.6.5, 7 signals (GTW_infoIndex, GTW_buildType, GTW_hardwareId, GTW_platformType and 3 more). Bit layout, scaling, units and value tables."
---

# GTW_info (0x3C) — Gateway, Tesla Model Y 2026.26.6.5 ETH

Gateway message: info. This page documents the 7 signals of GTW_info as defined for Tesla Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `GTW_info` |
| Ethernet-side id | 0x3C (60) |
| ECU | [Gateway](../../gtw.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 2000 ms |
| Signals | 7 |

## Signals of GTW_info

Tesla Model Y CAN bus signals in `GTW_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `GTW_infoIndex` | selector | Gateway: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0`<br>1 = `DEPRECATED_1`<br>2 = `DEPRECATED_2`<br>3 = `DEPRECATED_3`<br>4 = `DEPRECATED_4`<br>5 = `DEPRECATED_5`<br>6 = `DEPRECATED_6`<br>7 = `DEPRECATED_7`<br>8 = `DEPRECATED_8`<br>9 = `DEPRECATED_9`<br>10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>15 = `BOOTLOADER_CRC`<br>16 = `SUBCOMPONENT`<br>17 = `APP_GITHASH`<br>18 = `BOOTLOADER_GITHASH`<br>19 = `VERSION_DEPRECATED`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>22 = `VARIANTCRC`<br>23 = `SUBCOMPONENT2`<br>25 = `PACKAGE_PN_1_7`<br>26 = `PACKAGE_PN_8_14`<br>27 = `PACKAGE_PN_15_20`<br>29 = `PACKAGE_SN_1_7`<br>30 = `PACKAGE_SN_8_14`<br>31 = `SUBCOMPONENT_GITHASH`<br>255 = `END` | plausible |
| `GTW_buildType` | page 10 | Gateway: build type | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | plausible |
| `GTW_hardwareId` | page 10 | GTW hardware ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | plausible |
| `GTW_platformType` | page 13 | Gateway: platform type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `GTW_PLATFORM_UNKNOWN`<br>3 = `GTW_PLATFORM_MODEL3`<br>255 = `GTW_PLATFORM_END` | plausible |
| `GTW_appCrc` | page 13 | Gateway: app crc | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `GTW_applicationGitHash` | page 17 | Gateway: application git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | layout-only |
| `GTW_bootGitHash` | page 18 | Gateway: boot git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | layout-only |

## Multiplexing

`GTW_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (2 signals), page 13 (2 signals), page 17 (1 signals), page 18 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/ModelY/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Gateway messages (GTW)](../../gtw.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
