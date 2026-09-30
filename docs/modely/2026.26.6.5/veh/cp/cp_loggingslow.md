---
layout: default
title: "CP_loggingSlow (0x3DD) — Charge port controller, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Charge port controller message: logging slow. Tesla Model Y CAN bus message CP_loggingSlow (0x3DD) of Charge port controller, firmware 2026.26.6.5, 33 signals (CP_loggingSlowSelect, CP_UHF_chipState, CP_UHF_rssi, CP_UHF_rxOverflow and 29 more). Bit layout, scaling, units and value tables."
---

# CP_loggingSlow (0x3DD) — Charge port controller, Tesla Model Y 2026.26.6.5 VEH CAN

Charge port controller message: logging slow; frame length from the layout, not yet observed on a vehicle bus. This page documents the 33 signals of CP_loggingSlow as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `CP_loggingSlow` |
| CAN id | 0x3DD (989) |
| ECU | [Charge port controller](../../cp.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | CP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 33 |

## Signals of CP_loggingSlow

Tesla Model Y CAN bus signals in `CP_loggingSlow`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `CP_loggingSlowSelect` | selector | Charge port controller: logging slow select | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `0`<br>1 = `1`<br>2 = `2`<br>3 = `3`<br>4 = `4`<br>5 = `5`<br>6 = `6`<br>7 = `7`<br>8 = `8` | plausible |
| `CP_UHF_chipState` | page 3 | Charge port controller: UHF chip state | 4\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | validated |
| `CP_UHF_rssi` | page 3 | Signal strength of received UHF signal | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `CP_UHF_rxOverflow` | page 3 | Charge port controller: UHF rx overflow | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_UHF_rxNumBytes` | page 3 | Charge port controller: UHF rx num bytes | 17\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `CP_UHF_selfTestRssi` | page 3 | Signal strength of received self-test UHF signal | 25\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `CP_latchI` | page 3 | Charge port controller: latch i | 33\|12 | little-endian | unsigned | 0.0025 | 0 | A | 0 to 10.2375 |  | validated |
| `CP_inlet1HarnessIdState` | page 3 | State of the CP's inlet 1 harness pedigree; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `HARNESS_PEDIGREE_UNKNOWN_SNA`<br>1 = `HARNESS_PEDIGREE_INVALID`<br>2 = `HARNESS_PEDIGREE_VALID` | validated |
| `CP_inlet1HarnessIdValue` | page 3 | Pedigree of the CP's inlet 1 harness | 47\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | validated |
| `CP_inlet2HarnessIdState` | page 3 | State of the CP's inlet 2 harness pedigree; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `HARNESS_PEDIGREE_UNKNOWN_SNA`<br>1 = `HARNESS_PEDIGREE_INVALID`<br>2 = `HARNESS_PEDIGREE_VALID` | validated |
| `CP_inlet2HarnessIdValue` | page 3 | Pedigree of the CP's inlet 2 harness | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | validated |
| `CP_inletHeaterState` | page 3 | Reports the present state of the inlet heater. | 55\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INLET_HEATER_DISABLED`<br>1 = `INLET_HEATER_ENABLED_HIGHTEMP`<br>2 = `INLET_HEATER_ENABLED_LOWTEMP`<br>3 = `INLET_HEATER_FAULTED` | validated |
| `CP_inletHeaterDuty` | page 3 | Inlet heater PWM duty cycle | 57\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | validated |
| `CP_5vSwV` | page 4 | Charge port controller: 5v sw v | 4\|8 | little-endian | unsigned | 0.02745098 | 0 | V | 0 to 6.9999999 |  | validated |
| `CP_boardTemperature` | page 4 | Charge port controller: board temperature | 12\|8 | little-endian | unsigned | 1.29411768913 | -50 | C | -50 to 280 |  | validated |
| `CP_refVoltage` | page 4 | Charge port controller: ref voltage | 20\|8 | little-endian | unsigned | 0.0070588234812 | 0 | V | 0 to 1.79999998771 |  | validated |
| `CP_doorId_intervalMin10s` | page 4 | Charge port controller: door id interval min10s | 28\|8 | little-endian | unsigned | 0.0196078438312 | 0 | V | 0 to 5 |  | validated |
| `CP_doorId_intervalMax10s` | page 4 | Charge port controller: door id interval max10s | 36\|8 | little-endian | unsigned | 0.0196078438312 | 0 | V | 0 to 5 |  | validated |
| `CP_wakeOnPushCounter` | page 4 | Charge port controller: wake on push counter | 60\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | validated |
| `CP_doorPushLockoutActive` | page 4 | Reports whether the Charge Port (CP) wake on press has been disabled due to rate-limiting. | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_nvm_dataValid` | page 5 | Charge port controller: nvm data valid | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_nvm_doorOpenCycles` | page 5 | Charge port controller: nvm door open cycles | 5\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `CP_nvm_doorCloseCycles` | page 5 | Charge port controller: nvm door close cycles | 21\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `CP_nvm_doorOpen` | page 5 | Charge port controller: nvm door open | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_nvm_doorPresent` | page 5 | Charge port controller: nvm door present | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_nvm_doorPresentValid` | page 5 | Charge port controller: nvm door present valid | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_nvm_badPilotDiodeDetected` | page 5 | Charge port controller: nvm bad pilot diode detected | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_nvm_pilotDiodeFaultCount` | page 5 | Charge port controller: nvm pilot diode fault count | 41\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | validated |
| `CP_doorOpenLimiterMaxCount` | page 5 | Charge port controller: door open limiter max count | 44\|4 | little-endian | unsigned | 1 | 0 | counts | 0 to 15 |  | validated |
| `CP_doorOpenLimiterMaxRequestType` | page 5 | Charge port controller: door open limiter max request type | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `CPD_OPEN_REQ_NONE`<br>1 = `CPD_OPEN_REQ_UI`<br>2 = `CPD_OPEN_REQ_SEC`<br>3 = `CPD_OPEN_REQ_UHF`<br>4 = `CPD_OPEN_REQ_PUSH_TO_OPEN`<br>5 = `CPD_OPEN_REQ_CLOSING_FAILED`<br>6 = `CPD_OPEN_REQ_VCFRONT`<br>7 = `CPD_OPEN_REQ_CABLE_RECONNECTED`<br>8 = `CPD_OPEN_REQ_NUM` | validated |
| `CP_doorCloseLimiterMaxCount` | page 5 | Charge port controller: door close limiter max count | 52\|4 | little-endian | unsigned | 1 | 0 | counts | 0 to 15 |  | validated |
| `CP_doorCloseLimiterMaxRequestType` | page 5 | Charge port controller: door close limiter max request type | 56\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `CPD_CLOSE_REQ_NONE`<br>1 = `CPD_CLOSE_REQ_CABLE_UNPLUGGED`<br>2 = `CPD_CLOSE_REQ_DOOR_OPEN_TIMEOUT`<br>3 = `CPD_CLOSE_REQ_UI`<br>4 = `CPD_CLOSE_REQ_SEC`<br>5 = `CPD_CLOSE_REQ_PUSH_TO_CLOSE`<br>6 = `CPD_CLOSE_REQ_CAR_WASH`<br>7 = `CPD_CLOSE_REQ_FAULT_LINE`<br>8 = `CPD_CLOSE_REQ_ENTER_DRIVE`<br>9 = `CPD_CLOSE_REQ_OPENED_IN_DRIVE_STATE`<br>10 = `CPD_CLOSE_REQ_INITIAL_CINCH`<br>11 = `CPD_CLOSE_REQ_SENSOR_MISMATCH`<br>12 = `CPD_CLOSE_REQ_SENSOR_COMMS_RECOVERED`<br>13 = `CPD_CLOSE_REQ_OPEN_ON_WAKE`<br>14 = `CPD_CLOSE_REQ_VCFRONT`<br>15 = `CPD_CLOSE_REQ_COVER_OPEN`<br>16 = `CPD_CLOSE_REQ_NUM` | validated |
| `CP_proximityWakeCounter` | page 5 | Charge port controller: proximity wake counter | 61\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | validated |

## Multiplexing

`CP_loggingSlowSelect` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 3 (12 signals), page 4 (7 signals), page 5 (13 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Charge port controller messages (CP)](../../cp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
