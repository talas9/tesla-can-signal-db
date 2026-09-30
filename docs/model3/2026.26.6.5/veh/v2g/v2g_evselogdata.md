---
layout: default
title: "V2G_evseLogData (0x79D) — V2G ECU, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "V2G ECU message: evse log data. Tesla Model 3 CAN bus message V2G_evseLogData (0x79D) of V2G ECU, firmware 2026.26.6.5, 12 signals (V2G_evseLogDataSelect, V2G_chgParamRes_respCode, V2G_chgParamRes_finished, V2G_chgParamRes_evseStatus and 8 more). Bit layout, scaling, units and value tables."
---

# V2G_evseLogData (0x79D) — V2G ECU, Tesla Model 3 2026.26.6.5 VEH CAN

V2G ECU message: evse log data; frame length from the layout, not yet observed on a vehicle bus. This page documents the 12 signals of V2G_evseLogData as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `V2G_evseLogData` |
| CAN id | 0x79D (1949) |
| ECU | [V2G ECU](../../v2g.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | V2G |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 12 |

## Signals of V2G_evseLogData

Tesla Model 3 CAN bus signals in `V2G_evseLogData`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `V2G_evseLogDataSelect` | selector | V2G ECU: evse log data select | 0\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `SUPPORTED_APP_PROTOCOL`<br>1 = `SESSION_SETUP`<br>2 = `SERVICE_DISCOVERY`<br>3 = `SERVICE_DETAIL`<br>4 = `SERVICE_PAYMENT_SELECTION`<br>5 = `PAYMENT_DETAILS`<br>6 = `CONTRACT_AUTHENTICATION`<br>7 = `CHARGE_PARAMETER_DISCOVERY`<br>8 = `CABLE_CHECK`<br>9 = `PRECHARGE`<br>10 = `POWER_DELIVERY_START`<br>11 = `CURRENT_DEMAND`<br>12 = `CHARGING_STATUS`<br>13 = `POWER_DELIVERY_END`<br>14 = `WELDING_DETECTION`<br>15 = `SESSION_STOP`<br>16 = `MSG_NONE`<br>17 = `NUM_MSG` | plausible |
| `V2G_chgParamRes_respCode` | page 7 | Charge parameter response code reported by CCS DC charger | 8\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `CCS_EVSE_RESP_CODE_OK`<br>1 = `CCS_EVSE_RESP_CODE_OK_NEW_SESSION_ESTABLISHED`<br>2 = `CCS_EVSE_RESP_CODE_OK_OLD_SESSION_JOINED`<br>3 = `CCS_EVSE_RESP_CODE_OK_CERTIFICATE_EXPIRES_SOON`<br>4 = `CCS_EVSE_RESP_CODE_FAILED`<br>5 = `CCS_EVSE_RESP_CODE_FAILED_SEQUENCE_ERROR`<br>6 = `CCS_EVSE_RESP_CODE_FAILED_SERVICE_ID_INVALID`<br>7 = `CCS_EVSE_RESP_CODE_FAILED_UNKNOWN_SESSION`<br>8 = `CCS_EVSE_RESP_CODE_FAILED_SERVICE_SELECTION_INVALID`<br>9 = `CCS_EVSE_RESP_CODE_FAILED_PAYMENT_SELECTION_INVALID`<br>10 = `CCS_EVSE_RESP_CODE_FAILED_CERTIFICATE_EXPIRED`<br>11 = `CCS_EVSE_RESP_CODE_FAILED_SIGNATURE_ERROR`<br>12 = `CCS_EVSE_RESP_CODE_FAILED_NO_CERTIFICATE_AVAILABLE`<br>13 = `CCS_EVSE_RESP_CODE_FAILED_CERT_CHAIN_ERROR`<br>14 = `CCS_EVSE_RESP_CODE_FAILED_CHALLENGE_INVALID`<br>15 = `CCS_EVSE_RESP_CODE_FAILED_CONTRACT_CANCELED`<br>16 = `CCS_EVSE_RESP_CODE_FAILED_WRONG_CHARGE_PARAMETER`<br>17 = `CCS_EVSE_RESP_CODE_FAILED_POWER_DELIVERY_NOT_APPLIED`<br>18 = `CCS_EVSE_RESP_CODE_FAILED_TARIFF_SELECTION_INVALID`<br>19 = `CCS_EVSE_RESP_CODE_FAILED_CHARGING_PROFILE_INVALID`<br>20 = `CCS_EVSE_RESP_CODE_FAILED_EVSE_PRESENT_VOLTAGE_TOO_LOW`<br>21 = `CCS_EVSE_RESP_CODE_FAILED_METERING_SIGNATURE_NOT_VALID`<br>22 = `CCS_EVSE_RESP_CODE_FAILED_WRONG_ENERGY_TRANSFER_TYPE`<br>23 = `CCS_EVSE_RESP_CODE_FAILED_NO_CHARGE_SERVICE_SELECTED`<br>24 = `CCS_EVSE_RESP_CODE_FAILED_CONTACTOR_ERROR`<br>25 = `CCS_EVSE_RESP_CODE_FAILED_CERT_NOT_ALLOWED_AT_EVSE`<br>26 = `CCS_EVSE_RESP_CODE_FAILED_CERT_REVOKED`<br>27 = `CCS_EVSE_RESP_CODE_MAX` | validated |
| `V2G_chgParamRes_finished` | page 7 | V2G ECU: chg param res finished | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `V2G_chgParamRes_evseStatus` | page 7 | Charge parameter discovery status reported by CCS DC charger | 14\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `CCS_DC_EVSE_STATUS_NOT_READY`<br>1 = `CCS_DC_EVSE_STATUS_READY`<br>2 = `CCS_DC_EVSE_STATUS_SHUTDOWN`<br>3 = `CCS_DC_EVSE_STATUS_UTILITY_INTERRUPT_EVENT`<br>4 = `CCS_DC_EVSE_STATUS_ISOLATION_MONITORING_ACTIVE`<br>5 = `CCS_DC_EVSE_STATUS_EMERGENCY_SHUTDOWN`<br>6 = `CCS_DC_EVSE_STATUS_MALFUNCTION`<br>7 = `CCS_DC_EVSE_STATUS_RESERVED_8`<br>8 = `CCS_DC_EVSE_STATUS_RESERVED_9`<br>9 = `CCS_DC_EVSE_STATUS_RESERVED_A`<br>10 = `CCS_DC_EVSE_STATUS_RESERVED_B`<br>11 = `CCS_DC_EVSE_STATUS_RESERVED_C`<br>12 = `CCS_DC_EVSE_STATUS_MAX` | validated |
| `V2G_chgParamRes_evseMaxILim` | page 7 | Maximum current limit reported by CCS DC charger in charge parameter discovery message | 18\|8 | little-endian | unsigned | 7.032 | 0 | A | 0 to 1793.16 |  | validated |
| `V2G_chgParamRes_evseMaxVLim` | page 7 | Maximum voltage limit reported by CCS DC charger in charge parameter discovery message | 26\|8 | little-endian | unsigned | 4.688 | 0 | V | 0 to 1195.44 |  | validated |
| `V2G_chgParamRes_evseMinILim` | page 7 | Minimum current limit reported by CCS DC charger in charge parameter discovery message | 34\|8 | little-endian | unsigned | 7.032 | 0 | A | 0 to 1793.16 |  | validated |
| `V2G_chgParamRes_evseMinVLim` | page 7 | Minimum voltage limit reported by CCS DC charger in charge parameter discovery message | 42\|8 | little-endian | unsigned | 4.688 | 0 | V | 0 to 1195.44 |  | validated |
| `V2G_chgParamRes_evseMaxPowerLim` | page 7 | Maximum power limit reported by CCS DC charger in charge parameter discovery message | 50\|8 | little-endian | unsigned | 5.9766 | 0 | kW | 0 to 1524.033 |  | validated |
| `V2G_chgParamRes_evseMaxPower_val` | page 7 | Whether maximum power limit reported by CCS DC charger is valid in charge parameter discovery message | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `V2G_chgParamRes_isoState` | page 7 | The EVSE's reported isolation status | 59\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `CCS_ISOLATION_STATUS_INVALID`<br>1 = `CCS_ISOLATION_STATUS_VALID`<br>2 = `CCS_ISOLATION_STATUS_WARNING`<br>3 = `CCS_ISOLATION_STATUS_FAULT`<br>4 = `CCS_ISOLATION_STATUS_NO_IMD` | validated |
| `V2G_chgParamRes_isoState_val` | page 7 | The validity of the EVSE's reported isolation status | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Multiplexing

`V2G_evseLogDataSelect` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 7 (11 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All V2G ECU messages (V2G)](../../v2g.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
