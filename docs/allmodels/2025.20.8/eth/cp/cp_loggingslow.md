---
layout: default
title: "CP_loggingSlow (0x7FA) — Charge port controller, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Charge port controller message: logging slow. Ethernet-side message CP_loggingSlow of Charge port controller for Tesla Model 3 / Model Y firmware 2025.20.8, 25 signals (CP_loggingSlowSelect, CP_UHF_chipState, CP_UHF_rssi, CP_UHF_rxOverflow and 21 more). Bit layout, scaling, units and value tables."
---

# CP_loggingSlow (0x7FA) — Charge port controller, Tesla Model 3 / Model Y 2025.20.8 ETH

Charge port controller message: logging slow. This page documents the 25 signals of CP_loggingSlow as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `CP_loggingSlow` |
| Ethernet-side id | 0x7FA (2042) |
| ECU | [Charge port controller](../../cp.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | CP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 25 |

## Signals of CP_loggingSlow

Tesla Model 3 / Model Y CAN bus signals in `CP_loggingSlow`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `CP_loggingSlowSelect` | selector | Charge port controller: logging slow select | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `0`<br>1 = `1`<br>2 = `2`<br>3 = `3`<br>4 = `4`<br>5 = `5`<br>6 = `6`<br>7 = `7` | plausible |
| `CP_UHF_chipState` | page 3 | Charge port controller: UHF chip state | 4\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `CP_UHF_rssi` | page 3 | Signal strength of received UHF signal | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `CP_UHF_rxOverflow` | page 3 | Charge port controller: UHF rx overflow | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CP_UHF_rxNumBytes` | page 3 | Charge port controller: UHF rx num bytes | 17\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `CP_UHF_selfTestRssi` | page 3 | Signal strength of received self-test UHF signal | 25\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `CP_latchI` | page 3 | Charge port controller: latch i | 33\|12 | little-endian | unsigned | 0.0025 | 0 | A | 0 to 10.2375 |  | plausible |
| `CP_inlet1HarnessIdState` | page 3 | State of the CP's inlet 1 harness pedigree; raw 0 = signal not available (SNA) | 45\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `HARNESS_PEDIGREE_UNKNOWN_SNA`<br>1 = `HARNESS_PEDIGREE_INVALID`<br>2 = `HARNESS_PEDIGREE_VALID` | plausible |
| `CP_inlet1HarnessIdValue` | page 3 | Pedigree of the CP's inlet 1 harness | 47\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | plausible |
| `CP_inlet2HarnessIdState` | page 3 | State of the CP's inlet 2 harness pedigree; raw 0 = signal not available (SNA) | 50\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `HARNESS_PEDIGREE_UNKNOWN_SNA`<br>1 = `HARNESS_PEDIGREE_INVALID`<br>2 = `HARNESS_PEDIGREE_VALID` | plausible |
| `CP_inlet2HarnessIdValue` | page 3 | Pedigree of the CP's inlet 2 harness | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | plausible |
| `CP_inletHeaterState` | page 3 | Reports the present state of the inlet heater. | 55\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INLET_HEATER_DISABLED`<br>1 = `INLET_HEATER_ENABLED_HIGHTEMP`<br>2 = `INLET_HEATER_ENABLED_LOWTEMP`<br>3 = `INLET_HEATER_FAULTED` | plausible |
| `CP_inletHeaterDuty` | page 3 | Inlet heater PWM duty cycle | 57\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 100 |  | plausible |
| `CP_nvm_dataValid` | page 5 | Charge port controller: nvm data valid | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CP_nvm_doorOpenCycles` | page 5 | Charge port controller: nvm door open cycles | 8\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `CP_nvm_doorCloseCycles` | page 5 | Charge port controller: nvm door close cycles | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `CP_nvm_doorOpen` | page 5 | Charge port controller: nvm door open | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CP_nvm_doorPresent` | page 5 | Charge port controller: nvm door present | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CP_nvm_doorPresentValid` | page 5 | Charge port controller: nvm door present valid | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CP_nvm_badPilotDiodeDetected` | page 5 | Charge port controller: nvm bad pilot diode detected | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CP_nvm_pilotDiodeFaultCount` | page 5 | Charge port controller: nvm pilot diode fault count | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `CP_doorOpenLimiterMaxCount` | page 5 | Charge port controller: door open limiter max count | 47\|4 | little-endian | unsigned | 1 | 0 | counts | 0 to 15 |  | plausible |
| `CP_doorOpenLimiterMaxRequestType` | page 5 | Charge port controller: door open limiter max request type | 51\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `CPD_OPEN_REQ_NONE`<br>1 = `CPD_OPEN_REQ_UI`<br>2 = `CPD_OPEN_REQ_SEC`<br>3 = `CPD_OPEN_REQ_UHF`<br>4 = `CPD_OPEN_REQ_PUSH_TO_OPEN`<br>5 = `CPD_OPEN_REQ_CLOSING_FAILED`<br>6 = `CPD_OPEN_REQ_VCFRONT`<br>7 = `CPD_OPEN_REQ_CABLE_RECONNECTED`<br>8 = `CPD_OPEN_REQ_NUM` | plausible |
| `CP_doorCloseLimiterMaxCount` | page 5 | Charge port controller: door close limiter max count | 55\|4 | little-endian | unsigned | 1 | 0 | counts | 0 to 15 |  | plausible |
| `CP_doorCloseLimiterMaxRequestType` | page 5 | Charge port controller: door close limiter max request type | 59\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `CPD_CLOSE_REQ_NONE`<br>1 = `CPD_CLOSE_REQ_CABLE_UNPLUGGED`<br>2 = `CPD_CLOSE_REQ_DOOR_OPEN_TIMEOUT`<br>3 = `CPD_CLOSE_REQ_UI`<br>4 = `CPD_CLOSE_REQ_SEC`<br>5 = `CPD_CLOSE_REQ_PUSH_TO_CLOSE`<br>6 = `CPD_CLOSE_REQ_CAR_WASH`<br>7 = `CPD_CLOSE_REQ_FAULT_LINE`<br>8 = `CPD_CLOSE_REQ_ENTER_DRIVE`<br>9 = `CPD_CLOSE_REQ_OPENED_IN_DRIVE_STATE`<br>10 = `CPD_CLOSE_REQ_INITIAL_CINCH`<br>11 = `CPD_CLOSE_REQ_SENSOR_MISMATCH`<br>12 = `CPD_CLOSE_REQ_SENSOR_COMMS_RECOVERED`<br>13 = `CPD_CLOSE_REQ_OPEN_ON_WAKE`<br>14 = `CPD_CLOSE_REQ_VCFRONT`<br>15 = `CPD_CLOSE_REQ_COVER_OPEN`<br>16 = `CPD_CLOSE_REQ_NUM` | plausible |

## Multiplexing

`CP_loggingSlowSelect` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 3 (12 signals), page 5 (12 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Charge port controller messages (CP)](../../cp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
