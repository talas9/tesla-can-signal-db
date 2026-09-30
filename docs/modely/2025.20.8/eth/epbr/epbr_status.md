---
layout: default
title: "EPBR_status (0x2E8) — Right electric parking brake, Tesla Model Y 2025.20.8 ETH"
description: "Right electric parking brake message: status. Ethernet-side message EPBR_status of Right electric parking brake for Tesla Model Y firmware 2025.20.8, 34 signals (EPBR_systemStatus, EPBR_freeRollModeStatus, EPBR_driverIsLeaving, EPBR_driverIsLeavingAnySpeed and 30 more). Bit layout, scaling, units and value tables."
---

# EPBR_status (0x2E8) — Right electric parking brake, Tesla Model Y 2025.20.8 ETH

Right electric parking brake message: status. This page documents the 34 signals of EPBR_status as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `EPBR_status` |
| Ethernet-side id | 0x2E8 (744) |
| ECU | [Right electric parking brake](../../epbr.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | EPBR |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 34 |

## Signals of EPBR_status

Tesla Model Y CAN bus signals in `EPBR_status`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `EPBR_systemStatus` | Coordinated state representing the vehicle level parking brake state. | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `EPB_VEHICLE_STATUS_UNKNOWN`<br>1 = `EPB_VEHICLE_STATUS_RELEASED`<br>2 = `EPB_VEHICLE_STATUS_PARKED`<br>3 = `EPB_VEHICLE_STATUS_DYNAMIC`<br>4 = `EPB_VEHICLE_STATUS_PARKING`<br>5 = `EPB_VEHICLE_STATUS_RELEASING`<br>6 = `EPB_VEHICLE_STATUS_FAULT`<br>7 = `EPB_VEHICLE_STATUS_FAULT_SECURE`<br>8 = `EPB_VEHICLE_STATUS_MISMATCH` | validated |
| `EPBR_freeRollModeStatus` | Right electric parking brake: free roll mode status | 4\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `EPB_FREE_ROLL_MODE_UNAVAILABLE`<br>1 = `EPB_FREE_ROLL_MODE_AVAILABLE`<br>2 = `EPB_FREE_ROLL_MODE_ENABLED` | validated |
| `EPBR_driverIsLeaving` | Right electric parking brake: driver is leaving | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_driverIsLeavingAnySpeed` | Right electric parking brake: driver is leaving any speed | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_systemCdpAvailable` | Right electric parking brake: system cdp available | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_chimeRequest` | Right electric parking brake: chime request | 9\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `EPB_CHIME_REQUEST_NONE`<br>1 = `EPB_CHIME_REQUEST_GENERAL`<br>2 = `EPB_CHIME_REQUEST_GPO`<br>3 = `EPB_CHIME_REQUEST_ABOUT_TO_ACTIVE_DECEL`<br>4 = `EPB_CHIME_REQUEST_ACTIVE_DECEL` | validated |
| `EPBR_telltale` | Controls the telltale illumination on the instrument cluster; raw 7 = signal not available (SNA) | 12\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `EPB_TELLTALE_LAMP_OFF`<br>1 = `EPB_TELLTALE_LAMP_RED_PARKED`<br>2 = `EPB_TELLTALE_LAMP_RED_ON`<br>3 = `EPB_TELLTALE_LAMP_AMBER_ON`<br>4 = `EPB_TELLTALE_LAMP_RED_FLASH`<br>7 = `EPB_TELLTALE_SNA` | validated |
| `EPBR_audioCurrentSpikeDetected` | Right electric parking brake: audio current spike detected | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_redundantBrakingEnabled` | Right electric parking brake: redundant braking enabled | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_summonEnabled` | Right electric parking brake: summon enabled | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_brakeLight` | Right electric parking brake: brake light | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_epbConfigMismatch` | Right electric parking brake: epb config mismatch | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_brakeConfirmedPressed` | Right electric parking brake: brake confirmed pressed | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_requestUserConfirmation` | Right electric parking brake: request user confirmation | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_uiWinchModeMiscBlocking` | Reports the expected appearance of system error message on User Interface (UI) winch mode panel. | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_winchModeActive` | Right electric parking brake: winch mode active | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_updateMode` | Right electric parking brake: update mode | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_winchModePermissive` | Right electric parking brake: winch mode permissive | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_winchModePending` | Right electric parking brake: winch mode pending | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_cdpRequest` | Right electric parking brake: cdp request | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `EPB_CDP_NOT_REQUESTED`<br>1 = `EPB_CDP_REQUESTED` | validated |
| `EPBR_uiParkAvailable` | Reports the expected availability and appearance of the park button on User Interface (UI) safety panel. | 28\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `EPB_AVAIL_NOT_AVAILABLE`<br>1 = `EPB_AVAIL_AVAILABLE`<br>2 = `EPB_AVAIL_REAPPLIED` | validated |
| `EPBR_brakeDiscWipeRequest` | Right electric parking brake: brake disc wipe request; raw 3 = signal not available (SNA) | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `EPB_BRAKEDISCWIPE_REQUEST_NONE`<br>1 = `EPB_BRAKEDISCWIPE_REQUEST_LIGHT`<br>2 = `EPB_BRAKEDISCWIPE_REQUEST_STRONG`<br>3 = `EPB_BRAKEDISCWIPE_REQUEST_SNA` | validated |
| `EPBR_showUiGearShifter` | Right electric parking brake: show ui gear shifter | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_uiWinchModeLvStatus` | Reports the expected availability and appearance of Low Voltage (LV) system status on UI winch mode panel. | 33\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `EPB_LV_BLOCKED_BATTERY`<br>1 = `EPB_LV_BLOCKED_INPUT_VOLTAGE_LOW`<br>2 = `EPB_LV_BLOCKED_TIMER_RUNNING`<br>3 = `EPB_LV_OK` | validated |
| `EPBR_contactorCycleNotNeededForWinchEntry` | Right electric parking brake: contactor cycle not needed for winch entry | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_showStalkFaultedOnUi` | Right electric parking brake: show stalk faulted on ui | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_espPowerRequest` | Right electric parking brake: esp power request | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_okToPark` | Right electric parking brake: ok to park | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_hornRequest` | Right electric parking brake: horn request | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_winchModeAvailable` | Right electric parking brake: winch mode available | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_bothDisconnected` | Right electric parking brake: both disconnected | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_blockDrive` | Right electric parking brake: block drive | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `EPBR_statusCounter` | Right electric parking brake: status counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `EPBR_statusChecksum` | Right electric parking brake: status checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Right electric parking brake messages (EPBR)](../../epbr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
