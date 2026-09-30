---
layout: default
title: "RCU_info (0x33F) — RCU ECU, Tesla Model 3 2026.26.6.5 ETH"
description: "RCU ECU message: info. Ethernet-side message RCU_info of RCU ECU for Tesla Model 3 firmware 2026.26.6.5, 5 signals (RCU_infoIndex, RCU_infoPcbaID, RCU_infoAssemblyID, RCU_infoUsageID and 1 more). Bit layout, scaling, units and value tables."
---

# RCU_info (0x33F) — RCU ECU, Tesla Model 3 2026.26.6.5 ETH

RCU ECU message: info. This page documents the 5 signals of RCU_info as defined for Tesla Model 3 firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `RCU_info` |
| Ethernet-side id | 0x33F (831) |
| ECU | [RCU ECU](../../rcu.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | RCU |
| Frame length | 8 bytes |
| Cycle time | 10000 ms |
| Signals | 5 |

## Signals of RCU_info

Tesla Model 3 CAN bus signals in `RCU_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `RCU_infoIndex` | selector | RCU ECU: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0`<br>1 = `DEPRECATED_1`<br>2 = `DEPRECATED_2`<br>3 = `DEPRECATED_3`<br>4 = `DEPRECATED_4`<br>5 = `DEPRECATED_5`<br>6 = `DEPRECATED_6`<br>7 = `DEPRECATED_7`<br>8 = `DEPRECATED_8`<br>9 = `DEPRECATED_9`<br>10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>15 = `BOOTLOADER_CRC`<br>16 = `SUBCOMPONENT`<br>17 = `APP_GITHASH`<br>18 = `BOOTLOADER_GITHASH`<br>19 = `VERSION_DEPRECATED`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>22 = `VARIANTCRC`<br>23 = `SUBCOMPONENT2`<br>25 = `PACKAGE_PN_1_7`<br>26 = `PACKAGE_PN_8_14`<br>27 = `PACKAGE_PN_15_20`<br>29 = `PACKAGE_SN_1_7`<br>30 = `PACKAGE_SN_8_14`<br>31 = `SUBCOMPONENT_GITHASH`<br>255 = `END` | plausible |
| `RCU_infoPcbaID` | page 11 | RCU ECU: info pcba ID | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `RCU_infoAssemblyID` | page 11 | RCU ECU: info assembly ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `RCU_infoUsageID` | page 11 | RCU ECU: info usage ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `RCU_infoSubUsageID` | page 11 | RCU ECU: info sub usage ID | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |

## Multiplexing

`RCU_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 11 (4 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 ETH DBC file](../../../../../dbc/Model3/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All RCU ECU messages (RCU)](../../rcu.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
