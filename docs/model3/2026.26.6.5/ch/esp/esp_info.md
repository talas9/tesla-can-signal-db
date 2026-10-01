---
layout: default
title: "ESP_info (0x325) — Electronic stability control, Tesla Model 3 2026.26.6.5 CH CAN"
description: "Electronic stability control message: info. Tesla Model 3 CAN bus message ESP_info (0x325) of Electronic stability control, firmware 2026.26.6.5, 14 signals (ESP_infoIndex, ESP_infoBuildType, ESP_vehFlashMode, ESP_infoComponentID and 10 more). Bit layout, scaling, units and value tables."
---

# ESP_info (0x325) — Electronic stability control, Tesla Model 3 2026.26.6.5 CH CAN

Electronic stability control message: info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 14 signals of ESP_info as defined for Tesla Model 3 firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `ESP_info` |
| CAN id | 0x325 (805) |
| ECU | [Electronic stability control](../../esp.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | ESP |
| Frame length | 8 bytes |
| Cycle time | 10000 ms |
| Signals | 14 |

## Signals of ESP_info

Tesla Model 3 CAN bus signals in `ESP_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `ESP_infoIndex` | selector | Electronic stability control: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `DEPRECATED_0`<br>1 = `DEPRECATED_1`<br>2 = `DEPRECATED_2`<br>3 = `DEPRECATED_3`<br>4 = `DEPRECATED_4`<br>5 = `DEPRECATED_5`<br>6 = `DEPRECATED_6`<br>7 = `DEPRECATED_7`<br>8 = `DEPRECATED_8`<br>9 = `DEPRECATED_9`<br>10 = `BUILD_HWID_COMPONENTID`<br>11 = `PCBAID_ASSYID_USAGEID`<br>13 = `APP_CRC`<br>14 = `BOOTLOADER_SVN`<br>15 = `BOOTLOADER_CRC`<br>16 = `SUBCOMPONENT`<br>17 = `APP_GITHASH`<br>18 = `BOOTLOADER_GITHASH`<br>19 = `VERSION_DEPRECATED`<br>20 = `UDS_PROTOCOL_BOOTCRC`<br>22 = `VARIANTCRC`<br>23 = `SUBCOMPONENT2`<br>25 = `PACKAGE_PN_1_7`<br>26 = `PACKAGE_PN_8_14`<br>27 = `PACKAGE_PN_15_20`<br>29 = `PACKAGE_SN_1_7`<br>30 = `PACKAGE_SN_8_14`<br>31 = `SUBCOMPONENT_GITHASH`<br>255 = `END` | plausible |
| `ESP_infoBuildType` | page 10 | Electronic stability control: info build type | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | plausible |
| `ESP_vehFlashMode` | page 10 | Electronic stability control: veh flash mode | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `Production_Mode`<br>1 = `Development_Mode` | plausible |
| `ESP_infoComponentID` | page 10 | Electronic stability control: info component ID | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `ESP_infoPcbaID` | page 11 | Electronic stability control: info pcba ID | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `ESP_infoAssemblyID` | page 11 | Electronic stability control: info assembly ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `ESP_infoUsageID` | page 11 | Electronic stability control: info usage ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `ESP_infoSubUsageID` | page 11 | Electronic stability control: info sub usage ID | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 | 0 = `nonXCP_Rev_B_ESP_Cappella`<br>2 = `nonXCP_Rev_C_ESP_Cappella`<br>4 = `XCP_Gladiator_ESP`<br>8 = `nonXCP_Dfour_ESP_CP_CB`<br>16 = `XCP_Dfive_ESP_CP_CB` | plausible |
| `ESP_infoApplicationCRC` | page 13 | Indicating the Application CRC value of firmware running in system. | 39\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `ESP_infoVehicleVariant` | page 16 | Electronic stability control: info vehicle variant | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 1 = `MODEL_3_VARIANT_01`<br>2 = `MODEL_3_VARIANT_02`<br>3 = `MODEL_3_VARIANT_03`<br>4 = `MODEL_3_VARIANT_04`<br>5 = `MODEL_3_VARIANT_05`<br>6 = `MODEL_3_VARIANT_06`<br>7 = `MODEL_3_VARIANT_07`<br>8 = `MODEL_3_VARIANT_08`<br>9 = `MODEL_3_VARIANT_09` | plausible |
| `ESP_infoSubcomponent1` | page 16 | Electronic stability control: info subcomponent1 | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `ESP_infoBootUdsProtoVersion` | page 20 | Electronic stability control: info boot uds proto version | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `ESP_infoBootloaderCRC` | page 20 | Electronic stability control: info bootloader CRC | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `ESP_infoVariantCRC` | page 22 | Indicating the Calibration CRC value of firmware running in system. | 39\|32 | big-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |

## Multiplexing

`ESP_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (3 signals), page 11 (4 signals), page 13 (1 signals), page 16 (2 signals), page 20 (2 signals), page 22 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 CH DBC file](../../../../../dbc/Model3/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/CH.json)

## See also

- [All Electronic stability control messages (ESP)](../../esp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
