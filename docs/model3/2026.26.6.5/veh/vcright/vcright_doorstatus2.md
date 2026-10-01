---
layout: default
title: "VCRIGHT_doorStatus2 (0x123) — Right body controller, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Right body controller message: door status2. Tesla Model 3 CAN bus message VCRIGHT_doorStatus2 (0x123) of Right body controller, firmware 2026.26.6.5, 8 signals (VCRIGHT_doorStatus2Index, VCRIGHT_frontLatchRelDuty, VCRIGHT_BPillarCameraHeaterState, VCRIGHT_doorLatchAjarSwitchVoltageF and 4 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_doorStatus2 (0x123) — Right body controller, Tesla Model 3 2026.26.6.5 VEH CAN

Right body controller message: door status2; frame length observed on a vehicle bus. This page documents the 8 signals of VCRIGHT_doorStatus2 as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_doorStatus2` |
| CAN id | 0x123 (291) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 8 |

## Signals of VCRIGHT_doorStatus2

Tesla Model 3 CAN bus signals in `VCRIGHT_doorStatus2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_doorStatus2Index` | selector | Right body controller: door status2 index | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `MUX0`<br>1 = `MUX1` | validated |
| `VCRIGHT_frontLatchRelDuty` | page 1 | Front left door latch motor duty cycle. | 8\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 255 |  | validated |
| `VCRIGHT_BPillarCameraHeaterState` | page 1 | Indicates the state of the right b-pillar camera heater; raw 0 = signal not available (SNA) | 16\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `HEATER_STATE_SNA`<br>1 = `HEATER_STATE_ON`<br>2 = `HEATER_STATE_OFF`<br>3 = `HEATER_STATE_OFF_UNAVAILABLE`<br>4 = `HEATER_STATE_FAULT` | validated |
| `VCRIGHT_doorLatchAjarSwitchVoltageF` | page 1 | Door latch switch voltage feeding switch logic | 24\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_doorLatchAjarSwitchVoltageR` | page 1 | Door latch switch voltage feeding switch logic | 32\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCRIGHT_BPillarCameraHeaterCurrent` | page 1 | Current drawn by the right b-pillar camera heater; raw 63 = signal not available (SNA) | 40\|6 | little-endian | unsigned | 0.02 | 0 | A | 0 to 1.24 | 63 = `SNA` | validated |
| `VCRIGHT_mirrorTiltXOffset` | page 1 | Communicates post calibration position offset of right side view mirror tilt horizontal position | 48\|8 | little-endian | signed | 0.02 | 0 | V | -2.5 to 2.5 |  | validated |
| `VCRIGHT_mirrorTiltYOffset` | page 1 | Communicates post calibration position offset of right side view mirror tilt vertical position | 56\|8 | little-endian | signed | 0.02 | 0 | V | -2.5 to 2.5 |  | validated |

## Multiplexing

`VCRIGHT_doorStatus2Index` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (7 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
