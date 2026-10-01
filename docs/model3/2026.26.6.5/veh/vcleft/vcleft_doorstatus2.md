---
layout: default
title: "VCLEFT_doorStatus2 (0x122) — Left body controller, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Left body controller message: door status2. Tesla Model 3 CAN bus message VCLEFT_doorStatus2 (0x122) of Left body controller, firmware 2026.26.6.5, 14 signals (VCLEFT_doorStatus2Index, VCLEFT_rearLatchRelDuty, VCLEFT_vehicleInMotion, VCLEFT_frontDoorState and 10 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_doorStatus2 (0x122) — Left body controller, Tesla Model 3 2026.26.6.5 VEH CAN

Left body controller message: door status2; frame length observed on a vehicle bus. This page documents the 14 signals of VCLEFT_doorStatus2 as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_doorStatus2` |
| CAN id | 0x122 (290) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 14 |

## Signals of VCLEFT_doorStatus2

Tesla Model 3 CAN bus signals in `VCLEFT_doorStatus2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_doorStatus2Index` | selector | Left body controller: door status2 index | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `MUX0`<br>1 = `MUX1` | validated |
| `VCLEFT_rearLatchRelDuty` |  | Rear left door latch motor duty cycle. Position from firmware; message assignment inferred. | 8\|8 | little-endian | unsigned | 1 | 0 | % | 0 to 255 |  | plausible |
| `VCLEFT_vehicleInMotion` |  | Position from firmware; message assignment inferred. | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_frontDoorState` |  | Status of front left door. Position from firmware; message assignment inferred. | 17\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOOR_STATE_UNKNOWN`<br>1 = `DOOR_STATE_CLOSED`<br>2 = `DOOR_STATE_WAIT_FOR_SHORT_DROP`<br>3 = `DOOR_STATE_RELEASING_LATCH`<br>4 = `DOOR_STATE_OPEN`<br>5 = `DOOR_STATE_AJAR`<br>6 = `DOOR_STATE_INIT` | plausible |
| `VCLEFT_rearDoorState` |  | Status of rear left door. Position from firmware; message assignment inferred. | 20\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOOR_STATE_UNKNOWN`<br>1 = `DOOR_STATE_CLOSED`<br>2 = `DOOR_STATE_WAIT_FOR_SHORT_DROP`<br>3 = `DOOR_STATE_RELEASING_LATCH`<br>4 = `DOOR_STATE_OPEN`<br>5 = `DOOR_STATE_AJAR`<br>6 = `DOOR_STATE_INIT` | plausible |
| `VCLEFT_frontHandleRawStatus` |  | State machine state that represents physical state of the front left door handle for debugging. Position from firmware; message assignment inferred. | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `EXTERIOR_HANDLE_STATUS_SNA`<br>1 = `EXTERIOR_HANDLE_STATUS_INDETERMINATE`<br>2 = `EXTERIOR_HANDLE_STATUS_NOT_ACTIVE`<br>3 = `EXTERIOR_HANDLE_STATUS_ACTIVE`<br>4 = `EXTERIOR_HANDLE_STATUS_DISCONNECTED`<br>5 = `EXTERIOR_HANDLE_STATUS_FAULT` | plausible |
| `VCLEFT_rearHandleRawStatus` |  | State machine state that represents physical state of the rear left door handle for debugging. Position from firmware; message assignment inferred. | 27\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `EXTERIOR_HANDLE_STATUS_SNA`<br>1 = `EXTERIOR_HANDLE_STATUS_INDETERMINATE`<br>2 = `EXTERIOR_HANDLE_STATUS_NOT_ACTIVE`<br>3 = `EXTERIOR_HANDLE_STATUS_ACTIVE`<br>4 = `EXTERIOR_HANDLE_STATUS_DISCONNECTED`<br>5 = `EXTERIOR_HANDLE_STATUS_FAULT` | plausible |
| `VCLEFT_frontHandleDebounceStatus` |  | State machine state that represents physical state of the front left door handle for debugging. Position from firmware; message assignment inferred. | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `EXTERIOR_HANDLE_STATUS_SNA`<br>1 = `EXTERIOR_HANDLE_STATUS_INDETERMINATE`<br>2 = `EXTERIOR_HANDLE_STATUS_NOT_ACTIVE`<br>3 = `EXTERIOR_HANDLE_STATUS_ACTIVE`<br>4 = `EXTERIOR_HANDLE_STATUS_DISCONNECTED`<br>5 = `EXTERIOR_HANDLE_STATUS_FAULT` | plausible |
| `VCLEFT_rearHandleDebounceStatus` |  | State machine state that represents physical state of the front left door handle for debugging. Position from firmware; message assignment inferred. | 35\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `EXTERIOR_HANDLE_STATUS_SNA`<br>1 = `EXTERIOR_HANDLE_STATUS_INDETERMINATE`<br>2 = `EXTERIOR_HANDLE_STATUS_NOT_ACTIVE`<br>3 = `EXTERIOR_HANDLE_STATUS_ACTIVE`<br>4 = `EXTERIOR_HANDLE_STATUS_DISCONNECTED`<br>5 = `EXTERIOR_HANDLE_STATUS_FAULT` | plausible |
| `VCLEFT_frontHandle5vEnable` |  | Status of power going to the front left exterior door handle sensor. Position from firmware; message assignment inferred. | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_rearHandle5vEnable` |  | Status of power going to the rear left exterior door handle sensor. Position from firmware; message assignment inferred. | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `VCLEFT_BPillarCameraHeaterCurrent` | page 1 | Current drawn by the left b-pillar camera heater; raw 63 = signal not available (SNA) | 40\|6 | little-endian | unsigned | 0.02 | 0 | A | 0 to 1.24 | 63 = `SNA` | validated |
| `VCLEFT_mirrorTiltXOffset` | page 1 | Communicates post calibration position offset of left side view mirror tilt horizontal position | 48\|8 | little-endian | signed | 0.02 | 0 | V | -2.5 to 2.5 |  | validated |
| `VCLEFT_mirrorTiltYOffset` | page 1 | Communicates post calibration position offset of left side view mirror tilt vertical position | 56\|8 | little-endian | signed | 0.02 | 0 | V | -2.5 to 2.5 |  | validated |

## Multiplexing

`VCLEFT_doorStatus2Index` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (3 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
