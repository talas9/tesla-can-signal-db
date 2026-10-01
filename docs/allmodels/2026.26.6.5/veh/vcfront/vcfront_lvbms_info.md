---
layout: default
title: "VCFRONT_LVBMS_info (0x737) — Front body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Front body controller message: LVBMS info. Tesla Model 3 / Model Y CAN bus message VCFRONT_LVBMS_info (0x737) of Front body controller, firmware 2026.26.6.5, 7 signals (VCFRONT_LVBMS_InfoIndex, VCFRONT_LVBMS_PcbaId, VCFRONT_LVBMS_AssemblyId, VCFRONT_LVBMS_SubUsageId and 3 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_LVBMS_info (0x737) — Front body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Front body controller message: LVBMS info; frame length observed on a vehicle bus. This page documents the 7 signals of VCFRONT_LVBMS_info as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_LVBMS_info` |
| CAN id | 0x737 (1847) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT |
| Frame length | 7 bytes |
| Cycle time | 1000 ms |
| Signals | 7 |

## Signals of VCFRONT_LVBMS_info

Tesla Model 3 / Model Y CAN bus signals in `VCFRONT_LVBMS_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_LVBMS_InfoIndex` | selector | Front body controller: LVBMS info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `PCBAID_ASSYID`<br>1 = `APP_USAGEID_CRC`<br>2 = `GITHASH`<br>3 = `BUILDTYPE`<br>4 = `SERIAL_NUMBER`<br>5 = `INVALID` | validated |
| `VCFRONT_LVBMS_PcbaId` | page 0 | Front body controller: LVBMS pcba id | 8\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCFRONT_LVBMS_AssemblyId` | page 0 | Front body controller: LVBMS assembly id | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCFRONT_LVBMS_SubUsageId` | page 0 | LVBMS Sub Usage ID; raw 65535 = signal not available (SNA) | 40\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65534 | 65535 = `SNA` | validated |
| `VCFRONT_LVBMS_UsageId` | page 1 | Front body controller: LVBMS usage id | 8\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCFRONT_LVBMS_AppCRC` | page 1 | LVBMS application cyclic redundancy check | 24\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCFRONT_LVBMS_FWBuildType` | page 3 | Front body controller: LVBMS FW build type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | validated |

## Multiplexing

`VCFRONT_LVBMS_InfoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (3 signals), page 1 (2 signals), page 3 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
