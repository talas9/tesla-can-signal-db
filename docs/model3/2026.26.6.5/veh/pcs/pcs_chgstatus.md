---
layout: default
title: "PCS_chgStatus (0x204) — Power conversion system (on-board charger and DC-DC converter), Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Power conversion system (on-board charger and DC-DC converter) message: chg status. Tesla Model 3 CAN bus message PCS_chgStatus (0x204) of Power conversion system (on-board charger and DC-DC converter), firmware 2026.26.6.5, 17 signals (PCS_chgMainState, PCS_powerTransferStatus, PCS_gridConfig, PCS_chgPHAEnable and 13 more). Bit layout, scaling, units and value tables."
---

# PCS_chgStatus (0x204) — Power conversion system (on-board charger and DC-DC converter), Tesla Model 3 2026.26.6.5 VEH CAN

Power conversion system (on-board charger and DC-DC converter) message: chg status; frame length observed on a vehicle bus. This page documents the 17 signals of PCS_chgStatus as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PCS_chgStatus` |
| CAN id | 0x204 (516) |
| ECU | [Power conversion system (on-board charger and DC-DC converter)](../../pcs.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | PCS |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 17 |

## Signals of PCS_chgStatus

Tesla Model 3 CAN bus signals in `PCS_chgStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PCS_chgMainState` | Power conversion system (on-board charger and DC-DC converter): chg main state | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `PCS_CHG_STATE_INIT`<br>1 = `PCS_CHG_STATE_IDLE`<br>2 = `PCS_CHG_STATE_STARTUP`<br>3 = `PCS_CHG_STATE_WAIT_FOR_LINE_VOLTAGE`<br>4 = `PCS_CHG_STATE_QUALIFY_LINE_CONFIG`<br>5 = `PCS_CHG_STATE_SYSTEM_CONFIG`<br>6 = `PCS_CHG_STATE_ENABLE`<br>7 = `PCS_CHG_STATE_SHUTDOWN`<br>8 = `PCS_CHG_STATE_FAULTED`<br>9 = `PCS_CHG_STATE_CLEAR_FAULTS` | validated |
| `PCS_powerTransferStatus` | Reports the AC power transfer interface state of the Power Conversion System (PCS). | 4\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PCS_POWER_TRANSFER_STANDBY`<br>1 = `PCS_POWER_TRANSFER_BLOCKED`<br>2 = `PCS_POWER_TRANSFER_ENABLED`<br>3 = `PCS_POWER_TRANSFER_FAULTED` | validated |
| `PCS_gridConfig` | AC charger sensed grid configuration; raw 0 = signal not available (SNA) | 6\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `GRID_CONFIG_SNA`<br>1 = `GRID_CONFIG_SINGLE_PHASE`<br>2 = `GRID_CONFIG_THREE_PHASE`<br>3 = `GRID_CONFIG_THREE_PHASE_DELTA` | validated |
| `PCS_chgPHAEnable` | Indicates whether AC charger phase A is enabled | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PCS_chgPHBEnable` | Indicates whether AC charger phase B is enabled | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PCS_hvInletConductorEnergizedAc` | Power conversion system (on-board charger and DC-DC converter): hv inlet conductor energized ac | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PCS_chgHighPowerActive` | Power conversion system (on-board charger and DC-DC converter): chg high power active | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PCS_chgPHCEnable` | Indicates whether AC charger phase C is enabled | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PCS_chgInstantAcPowerAvailable` | Instantaneous power capability of the AC charger | 16\|8 | little-endian | unsigned | 0.1 | 0 | kW | 0 to 20 |  | validated |
| `PCS_chgMaxAcPowerAvailable` | Maximum power capability of the AC charger; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.1 | 0 | kW | 0 to 20 | 255 = `SNA` | validated |
| `PCS_chgPHALineCurrentRequest` | AC charger phase A input current command | 32\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 20 |  | validated |
| `PCS_chgPHBLineCurrentRequest` | AC charger phase B input current command | 40\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 20 |  | validated |
| `PCS_chgPHCLineCurrentRequest` | AC charger phase B input current command | 48\|8 | little-endian | unsigned | 0.1 | 0 | A | 0 to 20 |  | validated |
| `PCS_chgPwmEnableLine` | Sensed state of the charger PWM enable hardline | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PCS_powerTransferShutdownRequest` | The Power Conversion System (PCS) request to shut down AC power transfer. | 57\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NO_SHUTDOWN_REQUESTED`<br>1 = `GRACEFUL_SHUTDOWN_REQUESTED`<br>2 = `ESCALATED_SHUTDOWN_REQUESTED`<br>3 = `EMERGENCY_SHUTDOWN_REQUESTED` | validated |
| `PCS_hwVariantType` | Hardware variant of AC charger; raw 3 = signal not available (SNA) | 59\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `PCS_48A_SINGLE_PHASE_VARIANT`<br>1 = `PCS_32A_SINGLE_PHASE_VARIANT`<br>2 = `PCS_THREE_PHASES_VARIANT`<br>3 = `PCS_HW_VARIANT_TYPE_SNA` | validated |
| `PCS_dcacBidirectionalAllowed` | Indicates whether bidirectional DCAC capability is supported by this PCS variant | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Power conversion system (on-board charger and DC-DC converter) messages (PCS)](../../pcs.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
