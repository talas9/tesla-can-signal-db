---
layout: default
title: "VCRIGHT_lightStatus (0x3E3) — Right body controller, Tesla Model Y (2025+ / Juniper; community mapping) 2025.20.8 VEH CAN"
description: "Right body controller message: light status. Tesla Model Y (2025+ / Juniper; community mapping) CAN bus message VCRIGHT_lightStatus (0x3E3) of Right body controller, firmware 2025.20.8, 7 signals (VCRIGHT_brakeLightStatus, VCRIGHT_tailLightStatus, VCRIGHT_turnSignalStatus, VCRIGHT_reverseLightStatus and 3 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_lightStatus (0x3E3) — Right body controller, Tesla Model Y (2025+ / Juniper; community mapping) 2025.20.8 VEH CAN

Right body controller message: light status; frame length observed on a vehicle bus. This page documents the 7 signals of VCRIGHT_lightStatus as defined for Tesla Model Y (2025+ / Juniper; community mapping) firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_lightStatus` |
| CAN id | 0x3E3 (995) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model Y (2025+ / Juniper; community mapping) |
| API name / codename | `Bayberry` |
| Coverage scope | Product-metadata signal subset using the Model 3 / Model Y union routing map; no product-specific CAN routing map or complete vehicle coverage is established. |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCRIGHT |
| Frame length | 4 bytes |
| Cycle time | 200 ms |
| Signals | 7 |

## Signals of VCRIGHT_lightStatus

Tesla Model Y (2025+ / Juniper; community mapping) CAN bus signals in `VCRIGHT_lightStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_brakeLightStatus` | Status of rear right brake light source; raw 3 = signal not available (SNA) | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | plausible |
| `VCRIGHT_tailLightStatus` | Status of right tail (rear position) light source; raw 3 = signal not available (SNA) | 2\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | plausible |
| `VCRIGHT_turnSignalStatus` | Status of rear right turn signal light source; raw 3 = signal not available (SNA) | 4\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | plausible |
| `VCRIGHT_reverseLightStatus` | Status of the reverse light source(s); raw 3 = signal not available (SNA) | 6\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | plausible |
| `VCRIGHT_rearFogLightStatus` | The desired on/off state of the rear fog light source(s); raw 3 = signal not available (SNA) | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LIGHT_OFF`<br>1 = `LIGHT_ON`<br>2 = `LIGHT_FAULT`<br>3 = `LIGHT_SNA` | plausible |
| `VCRIGHT_leftInteriorTrunkLightReq` | Right body controller: left interior trunk light req | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCRIGHT_audioCurrentSpikeDetected` | Right body controller: audio current spike detected | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Download the DBC file

- [Tesla Model Y (2025+ / Juniper; community mapping) 2025.20.8 VEH DBC file](../../../../../dbc/Bayberry/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Bayberry/2025.20.8/VEH.json)

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
