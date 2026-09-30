---
layout: default
title: "VCBATT1_LVBMS_statusHigh (0x742) — VCBATT1 ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "VCBATT1 ECU message: LVBMS status high. Tesla Model Y CAN bus message VCBATT1_LVBMS_statusHigh (0x742) of VCBATT1 ECU, firmware 2026.26.6.5, 30 signals (VCBATT1_lvbmsStatusHighIndex, VCBATT1_LVBMS_packCurrent, VCBATT1_LVBMS_packVoltage, VCBATT1_LVBMS_packTemperature and 26 more). Bit layout, scaling, units and value tables."
---

# VCBATT1_LVBMS_statusHigh (0x742) — VCBATT1 ECU, Tesla Model Y 2026.26.6.5 VEH CAN

VCBATT1 ECU message: LVBMS status high; frame length from the layout, not yet observed on a vehicle bus. This page documents the 30 signals of VCBATT1_LVBMS_statusHigh as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCBATT1_LVBMS_statusHigh` |
| CAN id | 0x742 (1858) |
| ECU | [VCBATT1 ECU](../../vcbatt1.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCBATT1 |
| Frame length | 8 bytes |
| Cycle time | 40 ms |
| Signals | 30 |

## Signals of VCBATT1_LVBMS_statusHigh

Tesla Model Y CAN bus signals in `VCBATT1_LVBMS_statusHigh`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCBATT1_lvbmsStatusHighIndex` | selector | VCBATT1 ECU: lvbms status high index | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `PACK_VITALS_1`<br>1 = `CELL_VITALS_1`<br>2 = `PCS_INTERFACE`<br>3 = `TARGETS`<br>4 = `CELL_VITALS_2_AND_STATE_AND_COMMANDS`<br>5 = `INVALID` | plausible |
| `VCBATT1_LVBMS_packCurrent` | page 0 | Electrical current into the low voltage battery; raw 4194303 = signal not available (SNA) | 3\|22 | little-endian | unsigned | 0.001 | -2000 | A | -2000 to 2194.302 | 4194303 = `SNA` | validated |
| `VCBATT1_LVBMS_packVoltage` | page 0 | Voltage of the low voltage battery; raw 65535 = signal not available (SNA) | 25\|16 | little-endian | unsigned | 0.001 | 0 | V | 0 to 65.534 | 65535 = `SNA` | validated |
| `VCBATT1_LVBMS_packTemperature` | page 0 | Temperature of the low voltage battery; raw 511 = signal not available (SNA) | 41\|9 | little-endian | unsigned | 0.5 | -50 | degC | -50 to 205 | 511 = `SNA` | validated |
| `VCBATT1_LVBMS_MOSTemperature` | page 0 | Temperature of the MOSFET on the low voltage battery; raw 4095 = signal not available (SNA) | 50\|12 | little-endian | unsigned | 0.5 | -50 | degC | -50 to 1997 | 4095 = `SNA` | validated |
| `VCBATT1_LVBMS_sumCellVoltage` | page 1 | Sum of the cell voltage of the low voltage battery; raw 65535 = signal not available (SNA) | 8\|16 | little-endian | unsigned | 0.001 | 0 | V | 0 to 65.534 | 65534 = `INVALID`<br>65535 = `SNA` | validated |
| `VCBATT1_LVBMS_maxBrickVoltage` | page 1 | Maximum cell voltage in the low voltage battery; raw 8191 = signal not available (SNA) | 24\|13 | little-endian | unsigned | 0.001 | 0 | V | 0 to 8.19 | 8191 = `SNA` | validated |
| `VCBATT1_LVBMS_maxBrickVoltageIndex` | page 1 | VCBATT1 ECU: LVBMS max brick voltage index; raw 255 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 254 | 255 = `SNA` | validated |
| `VCBATT1_totalLVLoadCurrent` | page 2 | Total LV load current of the vehicle. | 8\|14 | little-endian | signed | 0.1 | 0 | A | -200 to 400 |  | validated |
| `VCBATT1_LVPackChargeCurrentLimit` | page 2 | Charge current limit for the LV battery pack. | 22\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 400 |  | validated |
| `VCBATT1_LVPackCurrent` | page 2 | Current of the LV battery pack. | 34\|14 | little-endian | signed | 0.1 | 0 | A | -200 to 400 |  | validated |
| `VCBATT1_LVBMS_estimatedPackOcv` | page 2 | VCBATT1 ECU: LVBMS estimated pack ocv | 48\|16 | little-endian | unsigned | 0.001 | 0 | V | 0 to 65.535 |  | validated |
| `VCBATT1_LVBMS_voltageTarget` | page 3 | Voltage target of the LV battery; raw 65535 = signal not available (SNA) | 3\|16 | little-endian | unsigned | 0.001 | 0 | V | 0 to 65.534 | 65535 = `SNA` | validated |
| `VCBATT1_LVBMS_currentTarget` | page 3 | Target current requested by the LV battery; raw 262143 = signal not available (SNA) | 19\|18 | little-endian | unsigned | 0.001 | -122 | A | -120 to 120 | 262143 = `SNA` | validated |
| `VCBATT1_LVBMS_maxAllowedChargeCurrent` | page 3 | Maximum allowed charge current of the battery; raw 8191 = signal not available (SNA) | 37\|13 | little-endian | unsigned | 0.1 | 0 | A | 0 to 819 | 8191 = `SNA` | validated |
| `VCBATT1_LVBMS_maxAllowedDischargeCurrent` | page 3 | Maximum allowed discharge current of the battery; raw 8191 = signal not available (SNA) | 50\|13 | little-endian | unsigned | 0.1 | 0 | A | 0 to 819 | 8191 = `SNA` | validated |
| `VCBATT1_LVBMS_MOSCommand` | page 4 | Current state of the MOS command to the LV battery | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_LVBMS_ClearErrorCntrCommand` | page 4 | VCBATT1 ECU: LVBMS clear error cntr command | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_LVBMS_ClearHistoricFaultCommand` | page 4 | VCBATT1 ECU: LVBMS clear historic fault command | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_LVBMS_ResetLVBMSCommand` | page 4 | Reset command issued to LVBMS, commanded by VC | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_LVBMS_EnterHibernationCommand` | page 4 | VCBATT1 ECU: LVBMS enter hibernation command | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_LVBMS_ECPAState` | page 4 | Current state of the E-CPA on the LV battery; raw 3 = signal not available (SNA) | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LVBMS_ECPA_STATE_OPEN`<br>1 = `LVBMS_ECPA_STATE_CLOSED`<br>2 = `LVBMS_ECPA_STATE_INVALID`<br>3 = `LVBMS_ECPA_STATE_SNA` | validated |
| `VCBATT1_LVBMS_MOSState` | page 4 | Current state of the MOS on the LV battery; raw 3 = signal not available (SNA) | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LVBMS_MOS_STATE_OPEN`<br>1 = `LVBMS_MOS_STATE_CLOSED`<br>2 = `LVBMS_MOS_STATE_INVALID`<br>3 = `LVBMS_MOS_STATE_SNA` | validated |
| `VCBATT1_LVBMS_VehicleState` | page 4 | VCBATT1 ECU: LVBMS vehicle state | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LVBMS_VEHICLE_STATE_DRIVE`<br>1 = `LVBMS_VEHICLE_STATE_ACCESSORY`<br>2 = `LVBMS_VEHICLE_STATE_CONDITIONING`<br>3 = `LVBMS_VEHICLE_STATE_OFF` | validated |
| `VCBATT1_LVBMS_LINWakeDisabled` | page 4 | VCBATT1 ECU: LVBMS LIN wake disabled | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LVBMS_LIN_WAKE_ENABLED`<br>1 = `LVBMS_LIN_WAKE_DISABLED` | validated |
| `VCBATT1_LVBMS_chargeType` | page 4 | VCBATT1 ECU: LVBMS charge type; raw 4 = signal not available (SNA) | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `LVBMS_CHARGE_UNDEFINED`<br>1 = `LVBMS_CHARGE_CONSTANT_CURRENT`<br>2 = `LVBMS_CHARGE_CONSTANT_VOLTAGE`<br>3 = `LVBMS_CHARGE_COMPLETE`<br>4 = `LVBMS_CHARGE_SNA` | validated |
| `VCBATT1_LVBMS_cellAndArcProtEnabled` | page 4 | Indicates whether the VC has commanded cell protections to be active | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT1_LVBMS_avgBrickVoltage` | page 4 | Average voltage of all cells in the low voltage battery; raw 8191 = signal not available (SNA) | 24\|13 | little-endian | unsigned | 0.001 | 0 | V | 0 to 8.19 | 8191 = `SNA` | validated |
| `VCBATT1_LVBMS_minBrickVoltage` | page 4 | Minimum cell voltage in the low voltage battery; raw 8191 = signal not available (SNA) | 40\|13 | little-endian | unsigned | 0.001 | 0 | V | 0 to 8.19 | 8191 = `SNA` | validated |
| `VCBATT1_LVBMS_minBrickVoltageIndex` | page 4 | VCBATT1 ECU: LVBMS min brick voltage index; raw 255 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 254 | 255 = `SNA` | validated |

## Multiplexing

`VCBATT1_lvbmsStatusHighIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (4 signals), page 1 (3 signals), page 2 (4 signals), page 3 (4 signals), page 4 (14 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All VCBATT1 ECU messages (VCBATT1)](../../vcbatt1.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
