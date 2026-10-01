---
layout: default
title: "VCRIGHT_logging0point1Hz (0x70B) — Right body controller, Tesla Model 3 2025.20.8 ETH"
description: "Right body controller message: logging0point1 hz. Ethernet-side message VCRIGHT_logging0point1Hz of Right body controller for Tesla Model 3 firmware 2025.20.8, 32 signals (VCRIGHT_logging0point1HzIndex, VCRIGHT_cabinAirFilterLifeRemaining, VCRIGHT_HEPAAirFilterLifeRemaining, VCRIGHT_leftPTCCompromisedRod and 28 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_logging0point1Hz (0x70B) — Right body controller, Tesla Model 3 2025.20.8 ETH

Right body controller message: logging0point1 hz. This page documents the 32 signals of VCRIGHT_logging0point1Hz as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_logging0point1Hz` |
| Ethernet-side id | 0x70B (1803) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 1250 ms |
| Signals | 32 |

## Signals of VCRIGHT_logging0point1Hz

Tesla Model 3 CAN bus signals in `VCRIGHT_logging0point1Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_logging0point1HzIndex` | selector | Right body controller: logging0point1 hz index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `LIGHT_CURRENTS_0`<br>1 = `LIGHT_CURRENTS_1`<br>2 = `HVAC`<br>3 = `HVAC_ACTUATOR_ENDSTOP`<br>4 = `HVAC_ACTUATOR_ZEROSTOP`<br>5 = `LIGHT_CURRENTS_2`<br>6 = `HVAC_2`<br>7 = `HVAC_3`<br>8 = `END` | plausible |
| `VCRIGHT_cabinAirFilterLifeRemaining` | page 2 | Life remaining on the cabin air filter | 8\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCRIGHT_HEPAAirFilterLifeRemaining` | page 2 | Life remaining on the cabin air filter | 16\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCRIGHT_leftPTCCompromisedRod` | page 2 | Right body controller: left PTC compromised rod | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `ALL`<br>2 = `INNER`<br>3 = `CENTER`<br>4 = `OUTER`<br>5 = `OUTER_INNER`<br>6 = `OUTER_CENTER`<br>7 = `CENTER_INNER` | plausible |
| `VCRIGHT_rightPTCCompromisedRod` | page 2 | Right body controller: right PTC compromised rod | 27\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `ALL`<br>2 = `INNER`<br>3 = `CENTER`<br>4 = `OUTER`<br>5 = `OUTER_INNER`<br>6 = `OUTER_CENTER`<br>7 = `CENTER_INNER` | plausible |
| `VCRIGHT_hepaFilterHealthScore` | page 2 | Right body controller: hepa filter health score | 32\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCRIGHT_cabinFilterHealthScore` | page 2 | Right body controller: cabin filter health score | 40\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `VCRIGHT_cabinTempBreathLevelFOff` | page 2 | Right body controller: cabin temp breath level f off; raw 255 = signal not available (SNA) | 47\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | plausible |
| `VCRIGHT_airDistributionModeAdjustmentFactor` | page 2 | Right body controller: air distribution mode adjustment factor | 55\|9 | little-endian | unsigned | 0.001 | 1 | - | 1 to 1.5 |  | plausible |
| `VCRIGHT_hvacLHBleedEndStop` | page 3 | Right body controller: hvac LH bleed end stop | 8\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCRIGHT_hvacRHBleedEndStop` | page 3 | Right body controller: hvac RH bleed end stop | 16\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCRIGHT_hvacLHVaneEndStop` | page 3 | Right body controller: hvac LH vane end stop | 24\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCRIGHT_hvacRHVaneEndStop` | page 3 | Right body controller: hvac RH vane end stop | 32\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCRIGHT_hvacUpperModeEndStop` | page 3 | Right body controller: hvac upper mode end stop | 40\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCRIGHT_hvacLowerModeEndStop` | page 3 | Right body controller: hvac lower mode end stop | 48\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCRIGHT_hvacIntakeEndStop` | page 3 | Right body controller: hvac intake end stop | 56\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCRIGHT_hvacLHBleedZeroStop` | page 4 | Right body controller: hvac LH bleed zero stop | 8\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCRIGHT_hvacRHBleedZeroStop` | page 4 | Right body controller: hvac RH bleed zero stop | 16\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCRIGHT_hvacLHVaneZeroStop` | page 4 | Right body controller: hvac LH vane zero stop | 24\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCRIGHT_hvacRHVaneZeroStop` | page 4 | Right body controller: hvac RH vane zero stop | 32\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCRIGHT_hvacUpperModeZeroStop` | page 4 | Right body controller: hvac upper mode zero stop | 40\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCRIGHT_hvacLowerModeZeroStop` | page 4 | Right body controller: hvac lower mode zero stop | 48\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCRIGHT_hvacIntakeZeroStop` | page 4 | Right body controller: hvac intake zero stop | 56\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCRIGHT_ambientTempLimp` | page 6 | Reports the estimated ambient temperature in limp mode; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | plausible |
| `VCRIGHT_cabinProbeTempLimp` | page 6 | Reports the estimated cabin probe temperature in limp mode; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | plausible |
| `VCRIGHT_thsTempLimp` | page 6 | Reports the estimated Tesla HVAC Sensor (THS) temperature in limp mode; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.5 | -40 | degC | -40 to 80 | 255 = `SNA` | plausible |
| `VCRIGHT_thsCabinWaterMassLimp` | page 6 | Reports the estimated Tesla HVAC Sensor (THS) humidity cabin water mass backup in limp mode. | 32\|8 | little-endian | unsigned | 0.5 | 0 | g/kg | 0 to 124 |  | plausible |
| `VCRIGHT_thsSolarIrradianceLimp` | page 6 | Reports the estimated Tesla HVAC Sensor (THS) solar irradiance backup in limp mode; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 5 | 0 | W/m2 | 0 to 1270 | 255 = `SNA` | plausible |
| `VCRIGHT_silentWakeRecordCount` | page 6 | Reports the number of records recorded during silent wake events. | 48\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | plausible |
| `VCRIGHT_evapCondensateMass` | page 7 | Right body controller: evap condensate mass | 8\|8 | little-endian | unsigned | 2 | 0 | g | 0 to 500 |  | plausible |
| `VCRIGHT_airwaveRightLateralTotalTravel` | page 7 | Right body controller: airwave right lateral total travel | 16\|16 | little-endian | unsigned | 6100 | 0 | deg | 0 to 399763500 |  | plausible |
| `VCRIGHT_airwaveLeftLateralTotalTravel` | page 7 | Right body controller: airwave left lateral total travel | 32\|16 | little-endian | unsigned | 6100 | 0 | deg | 0 to 399763500 |  | plausible |

## Multiplexing

`VCRIGHT_logging0point1HzIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 2 (8 signals), page 3 (7 signals), page 4 (7 signals), page 6 (6 signals), page 7 (3 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
