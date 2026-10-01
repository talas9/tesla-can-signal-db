---
layout: default
title: "VCLEFT_status (0x3A2) — Left body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Left body controller message: status. Tesla Model 3 / Model Y CAN bus message VCLEFT_status (0x3A2) of Left body controller, firmware 2026.26.6.5, 29 signals (VCLEFT_statusIndex, VCLEFT_securityControllerEnable, VCLEFT_securityControllerVoltage, VCLEFT_consoleDoorAssist and 25 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_status (0x3A2) — Left body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Left body controller message: status; frame length observed on a vehicle bus. This page documents the 29 signals of VCLEFT_status as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_status` |
| CAN id | 0x3A2 (930) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | 33 ms |
| Signals | 29 |

## Signals of VCLEFT_status

Tesla Model 3 / Model Y CAN bus signals in `VCLEFT_status`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_statusIndex` | selector | Left body controller: status index | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `MUX0`<br>1 = `MUX1`<br>2 = `MUX2` | validated |
| `VCLEFT_securityControllerEnable` | page 0 | Left body controller: security controller enable | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_securityControllerVoltage` | page 0 | Voltage of the VCSEC power feed | 6\|5 | little-endian | unsigned | 0.625 | 0 | V | 0 to 19.375 |  | validated |
| `VCLEFT_consoleDoorAssist` | page 0 | Left body controller: console door assist | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_OTAState` | page 0 | Left body controller: OTA state | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_5AVoltage` | page 0 | Left body controller: 5 a voltage | 13\|10 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 5.568880548 |  | validated |
| `VCLEFT_vbatProt` | page 0 | Left body controller: vbat prot | 23\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | validated |
| `VCLEFT_footwellLightCurrent` | page 0 | Left body controller: footwell light current | 35\|12 | little-endian | signed | 0.1 | 0 | mA | -204.8 to 204.7 |  | validated |
| `VCLEFT_swcInputVoltage` | page 0 | Input voltage reported by steering wheel controller module; raw 255 = signal not available (SNA) | 47\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.4 | 255 = `SNA` | validated |
| `VCLEFT_swcPCBATemperature` | page 0 | Left body controller: swc PCBA temperature; raw 128 = signal not available (SNA) | 55\|8 | little-endian | signed | 1 | 68 | degC | -59 to 195 | -128 = `SNA` | validated |
| `VCLEFT_obdEthernetActive` | page 0 | Left body controller: obd ethernet active | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_rationalityAggregateCurrent` | page 1 | Left body controller: rationality aggregate current | 12\|8 | little-endian | unsigned | 0.5 | 0 | A | 0 to 127.5 |  | validated |
| `VCLEFT_LVBatteryTypeDBG` | page 1 | Left body controller: LV battery type DBG | 20\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `LV_BATTERY_TYPE_UNKNOWN`<br>1 = `LV_BATTERY_TYPE_ATLASBX_B24_FLOODED`<br>2 = `LV_BATTERY_TYPE_CLARIOS_B24_FLOODED`<br>3 = `LV_BATTERY_TYPE_CATL_LI_ION`<br>4 = `LV_BATTERY_TYPE_TESLA_16V_LI_ION`<br>5 = `LV_BATTERY_TYPE_TESLA_48V_LI_ION` | validated |
| `VCLEFT_DIeFuseFault` | page 1 | Left body controller: d ie fuse fault | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_eFuseMgmtVoltageMonitor` | page 1 | Left body controller: e fuse mgmt voltage monitor | 25\|7 | little-endian | unsigned | 0.125 | 0 | V | 0 to 15.875 |  | validated |
| `VCLEFT_trailerAuxCurrent` | page 1 | Current Draw of the trailer aux output; raw 4095 = signal not available (SNA) | 32\|12 | little-endian | unsigned | 0.025 | 0 | A | 0 to 102.35 | 4095 = `SNA` | validated |
| `VCLEFT_swcHeatTmp` | page 1 | Temperature of steering wheel heater as reported by NTC; raw 1023 = signal not available (SNA) | 44\|10 | little-endian | unsigned | 0.1 | -35 | degC | -35 to 65 | 1023 = `SNA` | validated |
| `VCLEFT_swcHeatStatus` | page 1 | Status of steering wheel heater; raw 0 = signal not available (SNA) | 54\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `HEATER_STATE_SNA`<br>1 = `HEATER_STATE_ON`<br>2 = `HEATER_STATE_OFF`<br>3 = `HEATER_STATE_OFF_UNAVAILABLE`<br>4 = `HEATER_STATE_FAULT` | validated |
| `VCLEFT_swcHeatInhibited` | page 1 | Status describing whether steering wheel heat is inhibited | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_obdDeviceDetected` | page 1 | Reports whether the Left Vehicle Controller (VCLEFT) detects that an external device is connected to the OBD port. | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_pcbaTemperature` | page 2 | Left body controller: pcba temperature | 4\|11 | little-endian | unsigned | 0.125 | -40 | degC | -40 to 150 |  | validated |
| `VCLEFT_swcHeatPwr` | page 2 | Power of steering wheel heater; raw 511 = signal not available (SNA) | 15\|9 | little-endian | unsigned | 0.5 | 0 | W | 0 to 254 | 511 = `SNA` | validated |
| `VCLEFT_swcHeatDutyCycle` | page 2 | Steering wheel heater duty cycle; raw 127 = signal not available (SNA) | 24\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 | 127 = `SNA` | validated |
| `VCLEFT_DIeFuseCurrent` | page 2 | Left body controller: d ie fuse current | 31\|6 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6.3 |  | validated |
| `VCLEFT_SWCpresent` | page 2 | Left body controller: SW cpresent | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_trailerBrakeControllerCurrent` | page 2 | Value of the trailer brake controller HSD (high side driver) current sense. | 38\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 25.5 |  | validated |
| `VCLEFT_autonomyBehaviorStatus` | page 2 | Left body controller: autonomy behavior status | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DRIVER`<br>1 = `DRIVERLESS_TAKEOVER`<br>2 = `DRIVERLESS_NO_TAKEOVER` | validated |
| `VCLEFT_thirdRowLeftMapLightStatus` | page 2 | Reports the status of the third row left overhead map light; raw 3 = signal not available (SNA) | 48\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |
| `VCLEFT_thirdRowRightMapLightStatus` | page 2 | Reports the status of the third row right overhead map light; raw 3 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | validated |

## Multiplexing

`VCLEFT_statusIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (10 signals), page 1 (9 signals), page 2 (9 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
