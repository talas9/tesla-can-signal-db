---
layout: default
title: "DIF_info (0x656) — Front drive inverter, Tesla Model Y 2025.20.8 ETH"
description: "Front drive inverter message: info. Ethernet-side message DIF_info of Front drive inverter for Tesla Model Y firmware 2025.20.8, 28 signals (DIF_infoIndex, DIF_buildType, DIF_buildConfigurationId, DIF_hardwareId and 24 more). Bit layout, scaling, units and value tables."
---

# DIF_info (0x656) — Front drive inverter, Tesla Model Y 2025.20.8 ETH

Front drive inverter message: info. This page documents the 28 signals of DIF_info as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DIF_info` |
| Ethernet-side id | 0x656 (1622) |
| ECU | [Front drive inverter](../../dif.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DIF |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 28 |

## Signals of DIF_info

Tesla Model Y CAN bus signals in `DIF_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `DIF_infoIndex` | selector | Front drive inverter: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `INFO_DEPRECATED_0`<br>1 = `INFO_DEPRECATED_1`<br>2 = `INFO_DEPRECATED_2`<br>3 = `INFO_DEPRECATED_3`<br>4 = `INFO_DEPRECATED_4`<br>5 = `INFO_DEPRECATED_5`<br>6 = `INFO_DEPRECATED_6`<br>7 = `INFO_DEPRECATED_7`<br>8 = `INFO_DEPRECATED_8`<br>9 = `INFO_DEPRECATED_9`<br>10 = `INFO_BUILD_HWID_COMPONENTID`<br>11 = `INFO_PCBAID_ASSYID_USAGEID`<br>13 = `INFO_APP_CRC`<br>14 = `INFO_BOOTLOADER_SVN`<br>15 = `INFO_BOOTLOADER_CRC`<br>16 = `INFO_SUBCOMPONENT`<br>17 = `INFO_APP_GITHASH`<br>18 = `INFO_BOOTLOADER_GITHASH`<br>19 = `INFO_VERSION_DEPRECATED`<br>20 = `INFO_UDS_PROTOCOL_BOOTCRC`<br>23 = `INFO_SUBCOMPONENT2`<br>31 = `INFO_SUBCOMPONENT_GITHASH`<br>32 = `INFO_SUBCOMPONENT2_GITHASH`<br>33 = `INFO_SUBCOMPONENT_HWID`<br>34 = `INFO_SUBCOMPONENT2_HWID`<br>40 = `TRACKING_DATA_1`<br>41 = `TRACKING_DATA_2`<br>42 = `TRACKING_DATA_3`<br>43 = `TRACKING_DATA_4`<br>44 = `TRACKING_DATA_5`<br>255 = `INFO_END` | plausible |
| `DIF_buildType` | page 10 | Front drive inverter: build type | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | validated |
| `DIF_buildConfigurationId` | page 10 | Front drive inverter: build configuration id | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `DIF_hardwareId` | page 10 | Front drive inverter: hardware id | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 252 | 252 = `CONFIGURABLE_HWID_PLACEHOLDER` | validated |
| `DIF_componentId` | page 10 | Front drive inverter: component id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `DIF_pcbaId` | page 11 | Front drive inverter: pcba id | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `DIF_assemblyId` | page 11 | Front drive inverter: assembly id | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `DIF_usageId` | page 11 | Front drive inverter: usage id | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `DIF_subUsageId` | page 11 | Front drive inverter: sub usage id | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `DIF_motorType` | page 12 | Front drive inverter: motor type; raw 0 = signal not available (SNA) | 8\|5 | little-endian | unsigned | 1 | 0 |  | 1 to 31 | 0 = `DI_MOTOR_SNA`<br>1 = `DI_MOTOR_PM216D`<br>2 = `DI_MOTOR_IM130D`<br>3 = `DI_MOTOR_IM130D_AL`<br>4 = `DI_MOTOR_PM275B`<br>5 = `DI_MOTOR_PM350B`<br>6 = `DI_MOTOR_PM228C`<br>7 = `DI_MOTOR_PM291C`<br>8 = `DI_MOTOR_PM291D`<br>9 = `DI_MOTOR_PM275C`<br>10 = `DI_MOTOR_PM228HEA`<br>11 = `DI_MOTOR_IM228HEA`<br>12 = `DI_MOTOR_IM260A_1KV`<br>13 = `DI_MOTOR_PM215A_1KV`<br>14 = `DI_MOTOR_IM260C_1KV`<br>15 = `DI_MOTOR_PM215C_1KV`<br>16 = `DI_MOTOR_PM261C`<br>17 = `DI_MOTOR_IM260D_1KV`<br>18 = `DI_MOTOR_IM260E_1KV`<br>20 = `DI_MOTOR_PM215D_1KV`<br>31 = `DI_MOTOR_PM216E` | plausible |
| `DIF_siliconType` | page 12 | Front drive inverter: silicon type | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `MOSFET`<br>1 = `IGBT` | validated |
| `DIF_mechSafeStateType` | page 12 | Front drive inverter: mech safe state type; raw 0 = signal not available (SNA) | 24\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `DI_MECH_SAFE_STATE_TYPE_SNA`<br>1 = `DI_MECH_SAFE_STATE_TYPE_NONE`<br>2 = `DI_MECH_SAFE_STATE_TYPE_PRESENT` | validated |
| `DIF_applicationCrc` | page 13 | Front drive inverter: application crc | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `DIF_oilPumpBuildType` | page 16 | Front drive inverter: oil pump build type | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INFO_UNKNOWN_BUILD`<br>1 = `INFO_PLATFORM_BUILD`<br>2 = `INFO_LOCAL_BUILD`<br>3 = `INFO_TRACEABLE_CI_BUILD`<br>4 = `INFO_MFG_BUILD` | validated |
| `DIF_oilPumpAppCrc` | page 16 | Front drive inverter: oil pump app crc | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `DIF_FPGA_version` | page 16 | Front drive inverter: FPGA version; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 254 | 254 = `LOCAL_BUILD`<br>255 = `SNA` | validated |
| `DIF_appGitHash` | page 17 | Front drive inverter: app git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | validated |
| `DIF_bootGitHash` | page 18 | Front drive inverter: boot git hash | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | validated |
| `DIF_platformTyp` | page 19 | Front drive inverter: platform typ | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `DIF_infoBootLdUdsProtocolVersion` | page 20 | Front drive inverter: info boot ld uds protocol version | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `DIF_bootloaderCrc` | page 20 | Front drive inverter: bootloader crc | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `DIF_oilPumpPcbaId` | page 33 | Front drive inverter: oil pump pcba id | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `DIF_oilPumpAssemblyId` | page 33 | Front drive inverter: oil pump assembly id | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `DIF_oilPumpUsageId` | page 33 | Front drive inverter: oil pump usage id | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `DIF_refRotorFlux` | page 35 | Front drive inverter: ref rotor flux | 8\|16 | little-endian | unsigned | 0.0001 | 0 | Wb | 0 to 6.5535 |  | validated |
| `DIF_refRotorOffset` | page 35 | Front drive inverter: ref rotor offset; raw 2048 = signal not available (SNA) | 24\|12 | little-endian | signed | 0.1 | 0 | deg | -180 to 180 | -2048 = `SNA` | validated |
| `DIF_speedWearTotal` | page 36 | Front drive inverter: speed wear total; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 | 255 = `SNA` | validated |
| `DIF_torqueWearTotal` | page 36 | Front drive inverter: torque wear total; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.02 | 0 | 1 | 0 to 5.08 | 255 = `SNA` | validated |

## Multiplexing

`DIF_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 10 (4 signals), page 11 (4 signals), page 12 (3 signals), page 13 (1 signals), page 16 (3 signals), page 17 (1 signals), page 18 (1 signals), page 19 (1 signals), page 20 (2 signals), page 33 (3 signals), page 35 (2 signals), page 36 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Front drive inverter messages (DIF)](../../dif.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
