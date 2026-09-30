---
layout: default
title: "VCRIGHT_debugThermal10Hz (0x703) — Right body controller, Tesla Model 3 2025.20.8 ETH"
description: "Right body controller message: debug thermal10 hz. Ethernet-side message VCRIGHT_debugThermal10Hz of Right body controller for Tesla Model 3 firmware 2025.20.8, 36 signals (VCRIGHT_debugThermal10HzIndex, VCRIGHT_hvacPanelFloorSplitRow1, VCRIGHT_hvacDefrostPercent, VCRIGHT_hvacRow2Percent and 32 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_debugThermal10Hz (0x703) — Right body controller, Tesla Model 3 2025.20.8 ETH

Right body controller message: debug thermal10 hz. This page documents the 36 signals of VCRIGHT_debugThermal10Hz as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_debugThermal10Hz` |
| Ethernet-side id | 0x703 (1795) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 10 ms |
| Signals | 36 |

## Signals of VCRIGHT_debugThermal10Hz

Tesla Model 3 CAN bus signals in `VCRIGHT_debugThermal10Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_debugThermal10HzIndex` | selector | Right body controller: debug thermal10 hz index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `heaterAndEvapWatts`<br>1 = `temps`<br>2 = `airflow`<br>3 = `cabinModel`<br>4 = `actuatorStatus`<br>5 = `HVAC_PTC_COI_DEV1`<br>6 = `HVAC_PTC_COI_DEV2`<br>7 = `HVAC_PTC_COI_DEV3`<br>8 = `HVAC_PTC_COI_DEV4`<br>9 = `HVAC_ACTUATOR_TUNNING`<br>10 = `END` | plausible |
| `VCRIGHT_hvacPanelFloorSplitRow1` | page 2 | Right body controller: hvac panel floor split row1 | 8\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvacDefrostPercent` | page 2 | Right body controller: hvac defrost percent | 16\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvacRow2Percent` | page 2 | Right body controller: hvac row2 percent | 24\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvacPanelFloorSplitRow2` | page 2 | Right body controller: hvac panel floor split row2 | 32\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_hvacFreshMassCounter` | page 2 | Right body controller: hvac fresh mass counter | 40\|12 | little-endian | unsigned | 10 | 0 | kg | 0 to 40000 |  | validated |
| `VCRIGHT_hvacRecircMassCounter` | page 2 | Right body controller: hvac recirc mass counter | 52\|12 | little-endian | unsigned | 10 | 0 | kg | 0 to 40000 |  | validated |
| `VCRIGHT_setTempAdjustmentLeft` | page 3 | Right body controller: set temp adjustment left; raw 127 = signal not available (SNA) | 8\|7 | little-endian | unsigned | 0.1 | 0 | degC | 0 to 12 | 127 = `SNA` | validated |
| `VCRIGHT_setTempAdjustmentRight` | page 3 | Right body controller: set temp adjustment right; raw 127 = signal not available (SNA) | 16\|7 | little-endian | unsigned | 0.1 | 0 | degC | 0 to 12 | 127 = `SNA` | validated |
| `VCRIGHT_hvacLHVaneVelocity` | page 3 | Right body controller: hvac LH vane velocity | 24\|8 | little-endian | signed | 0.8 | 0 | deg/s | -100 to 100 |  | validated |
| `VCRIGHT_hvacRHVaneVelocity` | page 3 | Right body controller: hvac RH vane velocity | 32\|8 | little-endian | signed | 0.8 | 0 | deg/s | -100 to 100 |  | validated |
| `VCRIGHT_hvacMassflowCompensated` | page 3 | Right body controller: hvac massflow compensated | 47\|8 | little-endian | unsigned | 1.5 | 0 | g/s | 0 to 250 |  | validated |
| `VCRIGHT_PTCcenterPowerLeft` | page 5 | Right body controller: PT ccenter power left; raw 63 = signal not available (SNA) | 8\|6 | little-endian | unsigned | 30 | 0 | W | 0 to 1800 | 63 = `SNA` | validated |
| `VCRIGHT_PTCouterPowerLeft` | page 5 | Right body controller: PT couter power left; raw 63 = signal not available (SNA) | 16\|6 | little-endian | unsigned | 30 | 0 | W | 0 to 1800 | 63 = `SNA` | validated |
| `VCRIGHT_PTCinnerPowerLeft` | page 5 | Right body controller: PT cinner power left; raw 63 = signal not available (SNA) | 24\|6 | little-endian | unsigned | 30 | 0 | W | 0 to 1800 | 63 = `SNA` | validated |
| `VCRIGHT_PTCcenterPowerRight` | page 5 | Right body controller: PT ccenter power right; raw 63 = signal not available (SNA) | 32\|6 | little-endian | unsigned | 30 | 0 | W | 0 to 1800 | 63 = `SNA` | validated |
| `VCRIGHT_PTCouterPowerRight` | page 5 | Right body controller: PT couter power right; raw 63 = signal not available (SNA) | 40\|6 | little-endian | unsigned | 30 | 0 | W | 0 to 1800 | 63 = `SNA` | validated |
| `VCRIGHT_PTCinnerPowerRight` | page 5 | Right body controller: PT cinner power right; raw 63 = signal not available (SNA) | 48\|6 | little-endian | unsigned | 30 | 0 | W | 0 to 1800 | 63 = `SNA` | validated |
| `VCRIGHT_PTCcenterStoneTempLeft` | page 6 | Right body controller: PT ccenter stone temp left; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 2 | -70 | degC | -70 to 438 | 255 = `SNA` | validated |
| `VCRIGHT_PTCcenterStoneTempRight` | page 6 | Right body controller: PT ccenter stone temp right; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 2 | -70 | degC | -70 to 438 | 255 = `SNA` | validated |
| `VCRIGHT_PTCinnerStoneTempLeft` | page 6 | Right body controller: PT cinner stone temp left; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 2 | -70 | degC | -70 to 438 | 255 = `SNA` | validated |
| `VCRIGHT_PTCinnerStoneTempRight` | page 6 | Right body controller: PT cinner stone temp right; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 2 | -70 | degC | -70 to 438 | 255 = `SNA` | validated |
| `VCRIGHT_PTCouterStoneTempLeft` | page 7 | Right body controller: PT couter stone temp left; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 2 | -70 | degC | -70 to 438 | 255 = `SNA` | validated |
| `VCRIGHT_PTCouterRodTempLeft` | page 7 | Right body controller: PT couter rod temp left; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 2 | -70 | degC | -70 to 438 | 255 = `SNA` | validated |
| `VCRIGHT_PTCouterAirTempLeft` | page 7 | Right body controller: PT couter air temp left; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 2 | -70 | degC | -70 to 438 | 255 = `SNA` | validated |
| `VCRIGHT_PTCcenterRodTempLeft` | page 7 | Right body controller: PT ccenter rod temp left; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 2 | -70 | degC | -70 to 438 | 255 = `SNA` | validated |
| `VCRIGHT_PTCinnerRodTempLeft` | page 7 | Right body controller: PT cinner rod temp left; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 2 | -70 | degC | -70 to 438 | 255 = `SNA` | validated |
| `VCRIGHT_PTCcenterAirTempLeft` | page 7 | Right body controller: PT ccenter air temp left; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 2 | -70 | degC | -70 to 438 | 255 = `SNA` | validated |
| `VCRIGHT_PTCinnerAirTempLeft` | page 7 | Right body controller: PT cinner air temp left; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 2 | -70 | degC | -70 to 438 | 255 = `SNA` | validated |
| `VCRIGHT_PTCouterStoneTempRight` | page 8 | Right body controller: PT couter stone temp right; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 2 | -70 | degC | -70 to 438 | 255 = `SNA` | validated |
| `VCRIGHT_PTCouterRodTempRight` | page 8 | Right body controller: PT couter rod temp right; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 2 | -70 | degC | -70 to 438 | 255 = `SNA` | validated |
| `VCRIGHT_PTCouterAirTempRight` | page 8 | Right body controller: PT couter air temp right; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 2 | -70 | degC | -70 to 438 | 255 = `SNA` | validated |
| `VCRIGHT_PTCcenterRodTempRight` | page 8 | Right body controller: PT ccenter rod temp right; raw 255 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 2 | -70 | degC | -70 to 438 | 255 = `SNA` | validated |
| `VCRIGHT_PTCinnerRodTempRight` | page 8 | Right body controller: PT cinner rod temp right; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 2 | -70 | degC | -70 to 438 | 255 = `SNA` | validated |
| `VCRIGHT_PTCcenterAirTempRight` | page 8 | Right body controller: PT ccenter air temp right; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 2 | -70 | degC | -70 to 438 | 255 = `SNA` | validated |
| `VCRIGHT_PTCinnerAirTempRight` | page 8 | Right body controller: PT cinner air temp right; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 2 | -70 | degC | -70 to 438 | 255 = `SNA` | validated |

## Multiplexing

`VCRIGHT_debugThermal10HzIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 2 (6 signals), page 3 (5 signals), page 5 (6 signals), page 6 (4 signals), page 7 (7 signals), page 8 (7 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
