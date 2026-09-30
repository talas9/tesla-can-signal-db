---
layout: default
title: "CP_evseStatus (0x21D) — Charge port controller, Tesla Model 3 2025.20.8 ETH"
description: "Charge port controller message: evse status. Ethernet-side message CP_evseStatus of Charge port controller for Tesla Model 3 firmware 2025.20.8, 18 signals (CP_evseAccept, CP_evseRequest, CP_proximity, CP_pilot and 14 more). Bit layout, scaling, units and value tables."
---

# CP_evseStatus (0x21D) — Charge port controller, Tesla Model 3 2025.20.8 ETH

Charge port controller message: evse status. This page documents the 18 signals of CP_evseStatus as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `CP_evseStatus` |
| Ethernet-side id | 0x21D (541) |
| ECU | [Charge port controller](../../cp.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | CP |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 18 |

## Signals of CP_evseStatus

Tesla Model 3 CAN bus signals in `CP_evseStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `CP_evseAccept` | State of pilot EVSE accept state | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_evseRequest` | Request to close AC EVSE relays, used when digital communications have been established | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_proximity` | Sensed state of proximity for all inlets; raw 0 = signal not available (SNA) | 2\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `CHG_PROXIMITY_SNA`<br>1 = `CHG_PROXIMITY_DISCONNECTED`<br>2 = `CHG_PROXIMITY_UNLATCHED`<br>3 = `CHG_PROXIMITY_LATCHED` | validated |
| `CP_pilot` | State of EVSE pilot signal sensed by the charge port; raw 7 = signal not available (SNA) | 4\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `CHG_PILOT_NONE`<br>1 = `CHG_PILOT_FAULTED`<br>2 = `CHG_PILOT_LINE_CHARGE`<br>3 = `CHG_PILOT_FAST_CHARGE`<br>4 = `CHG_PILOT_IDLE`<br>5 = `CHG_PILOT_INVALID`<br>6 = `CHG_PILOT_UNUSED_6`<br>7 = `CHG_PILOT_SNA` | validated |
| `CP_digitalCommsEstablished` | Indicates whether digital communications have been established with an EVSE | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_pilotCurrent` | Line current limit detected from pilot signal | 8\|8 | little-endian | unsigned | 0.5 | 0 | A | 0 to 127.5 |  | validated |
| `CP_cableType` | Type of charge cable detected; raw 4 = signal not available (SNA) | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CHG_CABLE_TYPE_IEC`<br>1 = `CHG_CABLE_TYPE_SAE`<br>2 = `CHG_CABLE_TYPE_GB_AC`<br>3 = `CHG_CABLE_TYPE_GB_DC`<br>4 = `CHG_CABLE_TYPE_MCS`<br>5 = `CHG_CABLE_TYPE_SNA` | validated |
| `CP_iecPilotState` | State of the control pilot as defined in IEC-61851-1; raw 9 = signal not available (SNA) | 19\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `IEC_PILOT_B1`<br>1 = `IEC_PILOT_B2`<br>2 = `IEC_PILOT_B3`<br>3 = `IEC_PILOT_C1`<br>4 = `IEC_PILOT_C2`<br>5 = `IEC_PILOT_C3`<br>6 = `IEC_PILOT_E`<br>7 = `IEC_PILOT_F`<br>8 = `IEC_PILOT_NUM`<br>9 = `IEC_PILOT_SNA` | validated |
| `CP_plcSupported` | Indicates whether PLC hardware is populated for CCS charging support | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_cableCurrentLimit` | Charge port controller: cable current limit | 24\|7 | little-endian | unsigned | 1 | 0 | A | 0 to 127 |  | validated |
| `CP_teslaSwcanState` | Charge port controller: tesla swcan state | 34\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `TESLA_SWCAN_INACTIVE`<br>1 = `TESLA_SWCAN_ACCEPT`<br>2 = `TESLA_SWCAN_RECEIVE`<br>3 = `TESLA_SWCAN_ESTABLISHED`<br>4 = `TESLA_SWCAN_FAULT`<br>5 = `TESLA_SWCAN_GO_TO_SLEEP`<br>6 = `TESLA_SWCAN_OFFBOARD_UPDATE_IN_PROGRESS`<br>7 = `TESLA_SWCAN_V2L_RECEIVE`<br>8 = `TESLA_SWCAN_V2L_ESTABLISHED` | validated |
| `CP_evseChargeType_UI` | Reports the type of Electric Vehicle Supply Equipment (EVSE) connected. | 38\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NO_CHARGER_PRESENT`<br>1 = `DC_CHARGER_PRESENT`<br>2 = `AC_CHARGER_PRESENT` | validated |
| `CP_gbState` | State of GB DC charging | 40\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `GBDC_INACTIVE`<br>1 = `GBDC_WAIT_FOR_COMMS`<br>2 = `GBDC_COMMS_RECEIVED`<br>3 = `GBDC_HANDSHAKING_EXT_ISO`<br>4 = `GBDC_RECOGNITION`<br>5 = `GBDC_CHARGE_PARAM_CONFIG`<br>6 = `GBDC_VEH_PACK_PRECHARGE`<br>7 = `GBDC_READY_TO_CHARGE`<br>8 = `GBDC_CHARGING`<br>9 = `GBDC_STOP_CHARGE_REQUESTED`<br>10 = `GBDC_CHARGE_DISABLING`<br>11 = `GBDC_END_OF_CHARGE`<br>12 = `GBDC_ERROR_HANDLING`<br>13 = `GBDC_RETRY_CHARGE`<br>14 = `GBDC_FAULTED`<br>15 = `GBDC_TESTER_PRESENT` | validated |
| `CP_gbdcStopChargeReason` | Reason for stopping GB DC charging | 44\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `GBDC_STOP_REASON_NONE`<br>1 = `GBDC_VEH_REQUESTED`<br>2 = `GBDC_EVSE_REQUESTED`<br>3 = `GBDC_COMMS_TIMEOUT`<br>4 = `GBDC_EVSE_FAULT`<br>5 = `GBDC_EVSE_CRITICAL_FAULT`<br>6 = `GBDC_LIVE_DISCONNECT`<br>7 = `GBDC_SUPERCHARGER_COMMS_TIMEOUT`<br>8 = `GBDC_PARAM_MISMATCH` | validated |
| `CP_gbdcFailureReason` | Reason for failure of GB DC charging | 48\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `GBDC_FAILURE_NONE`<br>1 = `GBDC_ATTEMPTS_EXPIRED`<br>2 = `GBDC_SHUTDOWN_FAILURE`<br>3 = `GBDC_CRITICAL_FAILURE` | validated |
| `CP_gbdcChargeAttempts` | Number of GB DC charging retries used | 50\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | validated |
| `CP_acChargeState` | Charge port controller: ac charge state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `AC_CHARGE_INACTIVE`<br>1 = `AC_CHARGE_CONNECTED_CHARGE_BLOCKED`<br>2 = `AC_CHARGE_STANDBY`<br>3 = `AC_CHARGE_ENABLED`<br>4 = `AC_CHARGE_ONBOARD_CHARGER_SHUTDOWN`<br>5 = `AC_CHARGE_VEH_SHUTDOWN`<br>6 = `AC_CHARGE_FAULT` | validated |
| `CP_teslaDcState` | Reports the state of the Tesla direct current (DC) state machine. | 56\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `TESLA_DC_INACTIVE`<br>1 = `TESLA_DC_CONNECTED_CHARGE_BLOCKED`<br>2 = `TESLA_DC_STANDBY`<br>3 = `TESLA_DC_EXT_TESTS_ENABLED`<br>4 = `TESLA_DC_EXT_TEST_ACTIVE`<br>5 = `TESLA_DC_EXT_PRECHARGE_ACTIVE`<br>6 = `TESLA_DC_ENABLED`<br>7 = `TESLA_DC_EVSE_SHUTDOWN`<br>8 = `TESLA_DC_VEH_SHUTDOWN`<br>9 = `TESLA_DC_EMERGENCY_SHUTDOWN`<br>10 = `TESLA_DC_FAULT` | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Charge port controller messages (CP)](../../cp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
