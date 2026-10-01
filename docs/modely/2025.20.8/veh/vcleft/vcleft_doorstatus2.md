---
layout: default
title: "VCLEFT_doorStatus2 (0x122) — Left body controller, Tesla Model Y 2025.20.8 VEH CAN"
description: "Left body controller message: door status2. Tesla Model Y CAN bus message VCLEFT_doorStatus2 (0x122) of Left body controller, firmware 2025.20.8, 8 signals (VCLEFT_doorStatus2Index, VCLEFT_frontLatchRelDuty, VCLEFT_BPillarCameraHeaterState, VCLEFT_doorLatchAjarSwitchVoltageF and 4 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_doorStatus2 (0x122) — Left body controller, Tesla Model Y 2025.20.8 VEH CAN

Left body controller message: door status2; frame length observed on a vehicle bus. This page documents the 8 signals of VCLEFT_doorStatus2 as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_doorStatus2` |
| CAN id | 0x122 (290) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 8 |

## Signals of VCLEFT_doorStatus2

Tesla Model Y CAN bus signals in `VCLEFT_doorStatus2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_doorStatus2Index` | selector | Left body controller: door status2 index | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `MUX0`<br>1 = `MUX1` | plausible |
| `VCLEFT_frontLatchRelDuty` | page 1 | Front left door latch motor duty cycle. | 8\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 255 |  | plausible |
| `VCLEFT_BPillarCameraHeaterState` | page 1 | Indicates the state of the left b-pillar camera heater; raw 0 = signal not available (SNA) | 16\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `HEATER_STATE_SNA`<br>1 = `HEATER_STATE_ON`<br>2 = `HEATER_STATE_OFF`<br>3 = `HEATER_STATE_OFF_UNAVAILABLE`<br>4 = `HEATER_STATE_FAULT` | plausible |
| `VCLEFT_doorLatchAjarSwitchVoltageF` | page 1 | Door latch switch voltage feeding switch logic | 24\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCLEFT_doorLatchAjarSwitchVoltageR` | page 1 | Door latch switch voltage feeding switch logic | 32\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | plausible |
| `VCLEFT_BPillarCameraHeaterCurrent` | page 1 | Current drawn by the left b-pillar camera heater; raw 63 = signal not available (SNA) | 40\|6 | little-endian | unsigned | 0.02 | 0 | A | 0 to 1.24 | 63 = `SNA` | plausible |
| `VCLEFT_mirrorTiltXOffset` | page 1 | Communicates post calibration position offset of left side view mirror tilt horizontal position | 48\|8 | little-endian | signed | 0.02 | 0 | V | -2.5 to 2.5 |  | plausible |
| `VCLEFT_mirrorTiltYOffset` | page 1 | Communicates post calibration position offset of left side view mirror tilt vertical position | 56\|8 | little-endian | signed | 0.02 | 0 | V | -2.5 to 2.5 |  | plausible |

## Multiplexing

`VCLEFT_doorStatus2Index` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (7 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
