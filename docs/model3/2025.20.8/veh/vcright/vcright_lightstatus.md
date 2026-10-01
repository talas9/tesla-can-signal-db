---
layout: default
title: "VCRIGHT_lightStatus (0x3E3) — Right body controller, Tesla Model 3 2025.20.8 VEH CAN"
description: "Right body controller message: light status. Tesla Model 3 CAN bus message VCRIGHT_lightStatus (0x3E3) of Right body controller, firmware 2025.20.8, 13 signals (VCRIGHT_brakeLightStatus, VCRIGHT_tailLightStatus, VCRIGHT_turnSignalStatus, VCRIGHT_reverseLightStatus and 9 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_lightStatus (0x3E3) — Right body controller, Tesla Model 3 2025.20.8 VEH CAN

Right body controller message: light status; frame length observed on a vehicle bus. This page documents the 13 signals of VCRIGHT_lightStatus as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_lightStatus` |
| CAN id | 0x3E3 (995) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCRIGHT |
| Frame length | 4 bytes |
| Cycle time | 200 ms |
| Signals | 13 |

## Signals of VCRIGHT_lightStatus

Tesla Model 3 CAN bus signals in `VCRIGHT_lightStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_brakeLightStatus` | Status of rear right brake light source; raw 3 = signal not available (SNA) | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | plausible |
| `VCRIGHT_tailLightStatus` | Status of right tail (rear position) light source; raw 3 = signal not available (SNA) | 2\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | plausible |
| `VCRIGHT_turnSignalStatus` | Status of rear right turn signal light source; raw 3 = signal not available (SNA) | 4\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | plausible |
| `VCRIGHT_reverseLightStatus` | Status of the reverse light source(s); raw 3 = signal not available (SNA) | 6\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | plausible |
| `VCRIGHT_rearFogLightStatus` | The desired on/off state of the rear fog light source(s); raw 3 = signal not available (SNA) | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | plausible |
| `VCRIGHT_leftInteriorTrunkLightReq` | Right body controller: left interior trunk light req | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_audioCurrentSpikeDetected` | Right body controller: audio current spike detected | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_fasciaReverseLightStatus` | Status of fascia reverse lamp; raw 3 = signal not available (SNA) | 13\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | plausible |
| `VCRIGHT_fasciaRearFogStatus` | Status of fascia rear fog lamp; raw 3 = signal not available (SNA) | 15\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | plausible |
| `VCRIGHT_fasciaTailLightStatus` | Status of fascia tail lamp; raw 3 = signal not available (SNA) | 17\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | plausible |
| `VCRIGHT_fasciaLeftTurnSignalStatus` | Status of fascia left turn signal; raw 3 = signal not available (SNA) | 19\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | plausible |
| `VCRIGHT_fasciaRightTurnSignalStatus` | Status of fascia right turn signal; raw 3 = signal not available (SNA) | 21\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | plausible |
| `VCRIGHT_CHMSLLightStatus` | Status of center high mount stop lamp; raw 3 = signal not available (SNA) | 29\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
