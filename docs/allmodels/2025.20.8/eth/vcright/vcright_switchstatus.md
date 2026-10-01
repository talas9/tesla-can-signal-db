---
layout: default
title: "VCRIGHT_switchStatus (0x3C3) — Right body controller, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Right body controller message: switch status. Ethernet-side message VCRIGHT_switchStatus of Right body controller for Tesla Model 3 / Model Y firmware 2025.20.8, 25 signals (VCRIGHT_switchStatusIndex, VCRIGHT_frontBuckleSwitch, VCRIGHT_rearCenterBuckleSwitch, VCRIGHT_rearRightBuckleSwitch and 21 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_switchStatus (0x3C3) — Right body controller, Tesla Model 3 / Model Y 2025.20.8 ETH

Right body controller message: switch status. This page documents the 25 signals of VCRIGHT_switchStatus as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_switchStatus` |
| Ethernet-side id | 0x3C3 (963) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCRIGHT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 25 |

## Signals of VCRIGHT_switchStatus

Tesla Model 3 / Model Y CAN bus signals in `VCRIGHT_switchStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_switchStatusIndex` | selector | Right body controller: switch status index | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `0`<br>1 = `1` | plausible |
| `VCRIGHT_frontBuckleSwitch` | page 0 | Right body controller: front buckle switch | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | plausible |
| `VCRIGHT_rearCenterBuckleSwitch` | page 0 | Right body controller: rear center buckle switch | 44\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | plausible |
| `VCRIGHT_rearRightBuckleSwitch` | page 0 | Right body controller: rear right buckle switch | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | plausible |
| `VCRIGHT_trunkExtReleasePressedPersist` | page 1 | Right body controller: trunk ext release pressed persist | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_frontSeatTrackBack` | page 1 | Right body controller: front seat track back; raw 0 = signal not available (SNA) | 2\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | plausible |
| `VCRIGHT_frontSeatTrackForward` | page 1 | Right body controller: front seat track forward; raw 0 = signal not available (SNA) | 4\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | plausible |
| `VCRIGHT_frontSeatTiltDown` | page 1 | Right body controller: front seat tilt down; raw 0 = signal not available (SNA) | 6\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | plausible |
| `VCRIGHT_frontSeatTiltUp` | page 1 | Right body controller: front seat tilt up; raw 0 = signal not available (SNA) | 8\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | plausible |
| `VCRIGHT_frontSeatLiftDown` | page 1 | Right body controller: front seat lift down; raw 0 = signal not available (SNA) | 10\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | plausible |
| `VCRIGHT_frontSeatLiftUp` | page 1 | Right body controller: front seat lift up; raw 0 = signal not available (SNA) | 12\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | plausible |
| `VCRIGHT_frontSeatBackrestBack` | page 1 | Right body controller: front seat backrest back; raw 0 = signal not available (SNA) | 14\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | plausible |
| `VCRIGHT_frontSeatBackrestForward` | page 1 | Right body controller: front seat backrest forward; raw 0 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | plausible |
| `VCRIGHT_frontSeatLumbarDown` | page 1 | Right body controller: front seat lumbar down; raw 0 = signal not available (SNA) | 18\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | plausible |
| `VCRIGHT_frontSeatLumbarUp` | page 1 | Right body controller: front seat lumbar up; raw 0 = signal not available (SNA) | 20\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | plausible |
| `VCRIGHT_frontSeatLumbarIn` | page 1 | Right body controller: front seat lumbar in; raw 0 = signal not available (SNA) | 22\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | plausible |
| `VCRIGHT_frontSeatLumbarOut` | page 1 | Right body controller: front seat lumbar out; raw 0 = signal not available (SNA) | 24\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | plausible |
| `VCRIGHT_2RowSeatReclineSwitch` | page 1 | Second row seat recline switch | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_2RowSeatBackrestFoldSwitch` | page 1 | Second row seat backrest fold switch | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_frontHandlePWM` | page 1 | Right body controller: front handle PWM | 32\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | plausible |
| `VCRIGHT_rearHandlePWM` | page 1 | Right body controller: rear handle PWM | 40\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | plausible |
| `VCRIGHT_gloveboxLightCurrent` | page 1 | Current through the glovebox LED | 47\|5 | little-endian | unsigned | 2 | 0 | mA | 0 to 62 |  | plausible |
| `VCRIGHT_frontSeatALR` | page 1 | Front right seat automatic locking retractor switch; raw 0 = signal not available (SNA) | 52\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | plausible |
| `VCRIGHT_frontSeatResistiveOccupancy` | page 1 | Front right seat occupancy status; raw 0 = signal not available (SNA) | 54\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SWITCH_SNA`<br>1 = `SWITCH_OFF`<br>2 = `SWITCH_ON`<br>3 = `SWITCH_FAULT` | plausible |
| `VCRIGHT_2RowSeatReclineSwitchpackState` | page 1 | State of the right second row powered recline adjustment switchpack | 56\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DISCONNECTED`<br>1 = `INACTIVE`<br>2 = `FORWARD_SLOW`<br>3 = `FORWARD_FAST`<br>4 = `REARWARD_SLOW`<br>5 = `REARWARD_FAST`<br>6 = `FAULT` | plausible |

## Multiplexing

`VCRIGHT_switchStatusIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (3 signals), page 1 (21 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
