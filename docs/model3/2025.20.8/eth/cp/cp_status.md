---
layout: default
title: "CP_status (0x210) — Charge port controller, Tesla Model 3 2025.20.8 ETH"
description: "Charge port controller message: status. Ethernet-side message CP_status of Charge port controller for Tesla Model 3 firmware 2025.20.8, 22 signals (CP_type, CP_insertEnableLine, CP_latchState, CP_permanentPowerRequest and 18 more). Bit layout, scaling, units and value tables."
---

# CP_status (0x210) — Charge port controller, Tesla Model 3 2025.20.8 ETH

Charge port controller message: status. This page documents the 22 signals of CP_status as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `CP_status` |
| Ethernet-side id | 0x210 (528) |
| ECU | [Charge port controller](../../cp.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | CP |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 22 |

## Signals of CP_status

Tesla Model 3 CAN bus signals in `CP_status`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `CP_type` | Charge port controller: type | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CP_TYPE_US_TESLA`<br>1 = `CP_TYPE_EURO_IEC`<br>2 = `CP_TYPE_GB`<br>3 = `CP_TYPE_IEC_CCS` | validated |
| `CP_insertEnableLine` | Sensed state of the charge port latch drive enable hardline | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_latchState` | Sensed state of the charge port latch; raw 0 = signal not available (SNA) | 3\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `CP_LATCH_SNA`<br>1 = `CP_LATCH_DISENGAGED`<br>2 = `CP_LATCH_ENGAGED`<br>3 = `CP_LATCH_BLOCKING` | validated |
| `CP_permanentPowerRequest` | Charge port controller: permanent power request | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_chargeDoorOpen` | Indicates whether the charge port door is open based on all door sensors | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_doorControlState` | State of the charge port door controller | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CP_doorInit`<br>1 = `CP_doorIdle`<br>2 = `CP_doorOpenRequested`<br>3 = `CP_doorOpening`<br>4 = `CP_doorSenseOpen`<br>5 = `CP_doorClosing`<br>6 = `CP_doorSenseClosed` | validated |
| `CP_doorButtonPressed` | Indicates whether the charge door button has been pressed | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_swcanRelayClosed` | Indicates whether the single wire CAN relay is closed | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_inhibitOta` | Reports the charge port's request to prevent scheduled Over-The-Air (OTA) updates during critical charging operations. | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_chargeCableState` | Charge cable connection state; raw 0 = signal not available (SNA) | 14\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `CHARGE_CABLE_UNKNOWN_SNA`<br>1 = `CHARGE_CABLE_NOT_CONNECTED`<br>2 = `CHARGE_CABLE_CONNECTED` | validated |
| `CP_latchControlState` | Control state of the charge port latch | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CP_latchInit`<br>1 = `CP_latchIdle`<br>2 = `CP_latchDisengageRequested`<br>3 = `CP_latchDisengaging`<br>4 = `CP_latchDisengaged`<br>5 = `CP_latchEngaging` | validated |
| `CP_ledColor` | Color of the charge port LED | 19\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `CP_LEDS_OFF`<br>1 = `CP_LEDS_RED`<br>2 = `CP_LEDS_GREEN`<br>3 = `CP_LEDS_BLUE`<br>4 = `CP_LEDS_WHITE`<br>5 = `CP_LEDS_FLASHING_GREEN`<br>6 = `CP_LEDS_FLASHING_AMBER`<br>7 = `CP_LEDS_AMBER`<br>8 = `CP_LEDS_RAVE`<br>9 = `CP_LEDS_DEBUG`<br>10 = `CP_LEDS_FLASHING_BLUE`<br>11 = `CP_LEDS_FLASHING_PURPLE`<br>12 = `CP_LEDS_FADING_OUT`<br>13 = `CP_LEDS_FLASHING_WHITE` | validated |
| `CP_UHF_handleFound` | Indicates whether a charge handle has been found with UHF | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_faultLineSensed` | A signal indicating the set / cleared state of the CP-HVP bi-directional fault line, as sensed by the CP | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FAULT_LINE_CLEARED`<br>1 = `FAULT_LINE_SET` | validated |
| `CP_doorPresenceState` | State of door as detected by the presence sensor | 25\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CP_DOOR_PRESENCE_STATE_INIT`<br>1 = `CP_DOOR_PRESENCE_STATE_INIT_FROM_CHARGE`<br>2 = `CP_DOOR_PRESENCE_STATE_INIT_FROM_DRIVE`<br>3 = `CP_DOOR_PRESENCE_STATE_PRESENT`<br>4 = `CP_DOOR_PRESENCE_STATE_NOT_PRESENT`<br>5 = `CP_DOOR_PRESENCE_STATE_OFF_DRIVE`<br>6 = `CP_DOOR_PRESENCE_STATE_OFF_CHARGE`<br>7 = `CP_DOOR_PRESENCE_STATE_FAULT` | validated |
| `CP_inductiveSensorState` | State of inductive door sensor | 28\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CP_INDUCTIVE_SENSOR_INIT`<br>1 = `CP_INDUCTIVE_SENSOR_POLL`<br>2 = `CP_INDUCTIVE_SENSOR_SHUTDOWN`<br>3 = `CP_INDUCTIVE_SENSOR_PAUSE`<br>4 = `CP_INDUCTIVE_SENSOR_WAIT_FOR_INIT`<br>5 = `CP_INDUCTIVE_SENSOR_FAULT`<br>6 = `CP_INDUCTIVE_SENSOR_RESET`<br>7 = `CP_INDUCTIVE_SENSOR_CONFIG` | validated |
| `CP_chargeDoorOpenUI` | Indicates whether the charge port door is open based only on the door poteniometer | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_vehicleUnlockRequest` | Request to unlock the vehicle | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_coldWeatherMode` | Indicates whether the charge port is in cold weather mode | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CP_COLD_WEATHER_NONE`<br>1 = `CP_COLD_WEATHER_LATCH_MITIGATION` | validated |
| `CP_hvInletExposed` | Charge port controller: hv inlet exposed | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CP_latchEngaged` | Charge port controller: latch engaged | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `CP_inletHeaterUiState` | Reports to the User Interface (UI) the state of the inlet heater. | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CP_HEATER_NOT_SUPPORTED`<br>1 = `CP_HEATER_NOT_AVAILABLE`<br>2 = `CP_HEATER_AVAILABLE`<br>3 = `CP_HEATER_ENABLED`<br>4 = `CP_HEATER_FAULTED` | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Charge port controller messages (CP)](../../cp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
