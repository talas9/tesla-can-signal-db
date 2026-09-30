---
layout: default
title: "VCLEFT_doorStatus (0x102) — Left body controller, Tesla Model Y 2025.20.8 ETH"
description: "Left body controller message: door status. Ethernet-side message VCLEFT_doorStatus of Left body controller for Tesla Model Y firmware 2025.20.8, 23 signals (VCLEFT_doorClosureStatusFront, VCLEFT_doorClosureStatusRear, VCLEFT_frontLatchSwitch, VCLEFT_rearLatchSwitch and 19 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_doorStatus (0x102) — Left body controller, Tesla Model Y 2025.20.8 ETH

Left body controller message: door status. This page documents the 23 signals of VCLEFT_doorStatus as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_doorStatus` |
| Ethernet-side id | 0x102 (258) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 23 |

## Signals of VCLEFT_doorStatus

Tesla Model Y CAN bus signals in `VCLEFT_doorStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_doorClosureStatusFront` | Status of the door from a closures perspective; raw 0 = signal not available (SNA) | 0\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `CLOSURE_STATUS_SNA`<br>1 = `CLOSURE_STATUS_OPEN`<br>2 = `CLOSURE_STATUS_CLOSED`<br>8 = `CLOSURE_STATUS_FAULT` | validated |
| `VCLEFT_doorClosureStatusRear` | Status of the door from a closures perspective; raw 0 = signal not available (SNA) | 4\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `CLOSURE_STATUS_SNA`<br>1 = `CLOSURE_STATUS_OPEN`<br>2 = `CLOSURE_STATUS_CLOSED`<br>8 = `CLOSURE_STATUS_FAULT` | validated |
| `VCLEFT_frontLatchSwitch` | State of front left door latch switch representing door open/closed. 0 is open and 1 is closed | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_rearLatchSwitch` | State of rear left door latch switch representing door open/closed. 0 is open and 1 is closed | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_frontHandlePulled` | Left body controller: front handle pulled | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_rearHandlePulled` | Left body controller: rear handle pulled | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_frontRelActuatorSwitch` | State of front left door latch switch representing latch arm/unarmed. Disarms while door handle is pulled. | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_rearRelActuatorSwitch` | State of rear left door latch switch representing latch arm/unarmed. Disarms while door handle is pulled | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_frontLatchStatus` | Status of left front door latch; raw 0 = signal not available (SNA) | 14\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `LATCH_SNA`<br>1 = `LATCH_OPENED`<br>2 = `LATCH_CLOSED`<br>3 = `LATCH_CLOSING`<br>4 = `LATCH_OPENING`<br>5 = `LATCH_AJAR`<br>6 = `LATCH_TIMEOUT`<br>7 = `LATCH_DEFAULT`<br>8 = `LATCH_FAULT` | validated |
| `VCLEFT_rearLatchStatus` | Status of rear left door latch; raw 0 = signal not available (SNA) | 18\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `LATCH_SNA`<br>1 = `LATCH_OPENED`<br>2 = `LATCH_CLOSED`<br>3 = `LATCH_CLOSING`<br>4 = `LATCH_OPENING`<br>5 = `LATCH_AJAR`<br>6 = `LATCH_TIMEOUT`<br>7 = `LATCH_DEFAULT`<br>8 = `LATCH_FAULT` | validated |
| `VCLEFT_lastDoorReqSourceFront` | last source of front door open request | 22\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOOR_REQUEST_SOURCE_UNKNOWN`<br>1 = `DOOR_REQUEST_SOURCE_INTERIOR_BUTTON`<br>2 = `DOOR_REQUEST_SOURCE_EXTERIOR_HANDLE`<br>3 = `DOOR_REQUEST_SOURCE_VCSEC`<br>4 = `DOOR_REQUEST_SOURCE_ECU` | validated |
| `VCLEFT_lastDoorReqSourceRear` | last source of rear door open request | 25\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOOR_REQUEST_SOURCE_UNKNOWN`<br>1 = `DOOR_REQUEST_SOURCE_INTERIOR_BUTTON`<br>2 = `DOOR_REQUEST_SOURCE_EXTERIOR_HANDLE`<br>3 = `DOOR_REQUEST_SOURCE_VCSEC`<br>4 = `DOOR_REQUEST_SOURCE_ECU` | validated |
| `VCLEFT_frontIntSwitchPressed` | Left body controller: front int switch pressed | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_rearIntSwitchPressed` | Left body controller: rear int switch pressed | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_mirrorTiltXPosition` | Value representing left side view mirror tilt horizontal position | 33\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCLEFT_mirrorTiltYPosition` | Value representing left side view mirror tilt vertical position | 41\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 5 |  | validated |
| `VCLEFT_mirrorState` | State of the left side view mirror. | 49\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `MIRROR_STATE_IDLE`<br>1 = `MIRROR_STATE_TILT_X`<br>2 = `MIRROR_STATE_TILT_Y`<br>3 = `MIRROR_STATE_FOLD_UNFOLD`<br>4 = `MIRROR_STATE_RECALL`<br>5 = `MIRROR_STATE_CALIBRATION` | validated |
| `VCLEFT_mirrorFoldState` | Fold state for the left side view mirror | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `MIRROR_FOLD_STATE_UNKNOWN`<br>1 = `MIRROR_FOLD_STATE_FOLDED`<br>2 = `MIRROR_FOLD_STATE_UNFOLDED`<br>3 = `MIRROR_FOLD_STATE_FOLDING`<br>4 = `MIRROR_FOLD_STATE_UNFOLDING` | validated |
| `VCLEFT_mirrorRecallState` | State of Mirror Recall. | 55\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `MIRROR_RECALL_STATE_INIT`<br>1 = `MIRROR_RECALL_STATE_RECALLING_AXIS_1`<br>2 = `MIRROR_RECALL_STATE_RECALLING_AXIS_2`<br>3 = `MIRROR_RECALL_STATE_RECALLING_COMPLETE`<br>4 = `MIRROR_RECALL_STATE_RECALLING_FAILED`<br>5 = `MIRROR_RECALL_STATE_RECALLING_STOPPED` | validated |
| `VCLEFT_mirrorHeatState` | Left body controller: mirror heat state; raw 0 = signal not available (SNA) | 58\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `HEATER_STATE_SNA`<br>1 = `HEATER_STATE_ON`<br>2 = `HEATER_STATE_OFF`<br>3 = `HEATER_STATE_OFF_UNAVAILABLE`<br>4 = `HEATER_STATE_FAULT` | validated |
| `VCLEFT_rearHandlePulledPersist` | Left body controller: rear handle pulled persist | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_frontHandlePulledPersist` | Left body controller: front handle pulled persist | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_mirrorDipped` | Reports if the side view mirrors in are in the dipped position. | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
