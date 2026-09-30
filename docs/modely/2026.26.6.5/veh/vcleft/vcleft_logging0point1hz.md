---
layout: default
title: "VCLEFT_logging0point1Hz (0x70A) — Left body controller, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Left body controller message: logging0point1 hz. Tesla Model Y CAN bus message VCLEFT_logging0point1Hz (0x70A) of Left body controller, firmware 2026.26.6.5, 6 signals (VCLEFT_logging0point1HzIndex, VCLEFT_leftBrakeTailLightCurrent, VCLEFT_leftBrakeTailLightCurrentSenseState, VCLEFT_leftRearTurnLightCurrent and 2 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_logging0point1Hz (0x70A) — Left body controller, Tesla Model Y 2026.26.6.5 VEH CAN

Left body controller message: logging0point1 hz; frame length observed on a vehicle bus. This page documents the 6 signals of VCLEFT_logging0point1Hz as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_logging0point1Hz` |
| CAN id | 0x70A (1802) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCLEFT |
| Frame length | 5 bytes |
| Cycle time | 10000 ms |
| Signals | 6 |

## Signals of VCLEFT_logging0point1Hz

Tesla Model Y CAN bus signals in `VCLEFT_logging0point1Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_logging0point1HzIndex` | selector | Left body controller: logging0point1 hz index | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `MISC`<br>1 = `END` | plausible |
| `VCLEFT_leftBrakeTailLightCurrent` | page 0 | Current sensed by the left brake tail light HSD (high side driver); raw 511 = signal not available (SNA) | 2\|9 | little-endian | unsigned | 0.005 | 0 | A | 0 to 2.55 | 511 = `SNA` | validated |
| `VCLEFT_leftBrakeTailLightCurrentSenseState` | page 0 | State representing validity of the left brake tail light HSD (high side driver) current sense; raw 0 = signal not available (SNA) | 11\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `SNA`<br>1 = `STEADY_STATE_OFF`<br>2 = `RISING_EDGE_TRANSIENT`<br>3 = `STEADY_STATE_ON`<br>4 = `FALLING_EDGE_TRANSIENT` | validated |
| `VCLEFT_leftRearTurnLightCurrent` | page 0 | Current sensed by the left rear turn signal HSD (high side driver); raw 511 = signal not available (SNA) | 14\|9 | little-endian | unsigned | 0.002 | 0 | A | 0 to 1.02 | 511 = `SNA` | validated |
| `VCLEFT_leftRearTurnLightCurrentSenseState` | page 0 | State representing validity of the left rear turn signal HSD (high side driver) current sense; raw 0 = signal not available (SNA) | 24\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `SNA`<br>1 = `STEADY_STATE_OFF`<br>2 = `RISING_EDGE_TRANSIENT`<br>3 = `STEADY_STATE_ON`<br>4 = `FALLING_EDGE_TRANSIENT` | validated |
| `VCLEFT_phoneTemperatureFL` | page 0 | Temperature of front left wireless phone charger (if installed); raw 128 = signal not available (SNA) | 32\|8 | little-endian | signed | 1 | -50 | degC | -177 to 77 | -128 = `SNA` | validated |

## Multiplexing

`VCLEFT_logging0point1HzIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (5 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
