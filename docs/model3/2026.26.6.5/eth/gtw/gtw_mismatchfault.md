---
layout: default
title: "GTW_mismatchFault (0x55A) — Gateway, Tesla Model 3 2026.26.6.5 ETH"
description: "Gateway message: mismatch fault. Ethernet-side message GTW_mismatchFault of Gateway for Tesla Model 3 firmware 2026.26.6.5, 49 signals (GTW_mismatchFaultIndex, GTW_mismatchFaultChecksum, GTW_mismatchFaultCounter, GTW_GTWmismatchFault and 45 more). Bit layout, scaling, units and value tables."
---

# GTW_mismatchFault (0x55A) — Gateway, Tesla Model 3 2026.26.6.5 ETH

Gateway message: mismatch fault. This page documents the 49 signals of GTW_mismatchFault as defined for Tesla Model 3 firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `GTW_mismatchFault` |
| Ethernet-side id | 0x55A (1370) |
| ECU | [Gateway](../../gtw.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 250 ms |
| Signals | 49 |

## Signals of GTW_mismatchFault

Tesla Model 3 CAN bus signals in `GTW_mismatchFault`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `GTW_mismatchFaultIndex` | selector | Gateway: mismatch fault index | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 1 = `Mux1`<br>2 = `Mux2`<br>3 = `Mux3`<br>4 = `Mux4`<br>5 = `Mux5` | plausible |
| `GTW_mismatchFaultChecksum` |  | Gateway: mismatch fault checksum | 3\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `GTW_mismatchFaultCounter` |  | Gateway: mismatch fault counter | 11\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `GTW_GTWmismatchFault` | page 1 | Reports the Gateway (GTW) running a firmware version that does not match the rest of the vehicle | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_BMSmismatchFault` | page 1 | Reports the high voltage Battery Management System (BMS) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_APSmismatchFault` | page 1 | Reports the Autopilot Processor Secondary (APS) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_BLEEPCENTERmismatchFault` | page 1 | Reports the Bluetooth Low Energy End Point Center (BLEEPCENTER) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_BLEEPLEFTmismatchFault` | page 1 | Reports the Bluetooth Low Energy End Point Left (BLEEPLEFT) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_BLEEPREARmismatchFault` | page 1 | Reports the Bluetooth Low Energy End Point Rear (BLEEPREAR) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_BLEEPRIGHTmismatchFault` | page 1 | Reports the Bluetooth Low Energy End Point Right (BLEEPRIGHT) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_CBCmismatchFault` | page 1 | Reports the Cabin Blower Controller (CBC) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_CMPmismatchFault` | page 1 | Reports the air conditioning compressor (CMP) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_CPmismatchFault` | page 1 | Reports the Charge Port (CP) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_DIFmismatchFault` | page 1 | Reports the front drive inverter (DIF) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_DIRmismatchFault` | page 1 | Reports the rear drive inverter (DIR) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_EPAS3PmismatchFault` | page 1 | Reports the primary Electronic Power Assisted Steering (EPAS3P) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_EPAS3SmismatchFault` | page 1 | Reports the secondary Electronic Power Assisted Steering (EPAS3S) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_EPBLmismatchFault` | page 1 | Reports the left Electronic Park Brake (EPBL) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_EPBRmismatchFault` | page 1 | Reports the right Electronic Park Brake (EPBR) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_ESPCALmismatchFault` | page 1 | Reports the Electronic Stability Program Calibration (ESPCAL) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_ESPmismatchFault` | page 1 | Reports the Electronic Stability Program (ESP) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_HCM3LmismatchFault` | page 1 | Reports the left LED matrix Headlamp Control Module (HCM3L) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_HCM3RmismatchFault` | page 1 | Reports the right LED matrix Headlamp Control Module (HCM3R) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_HCMLmismatchFault` | page 1 | Reports the left Headlamp Control Module (HCML) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_HCMRmismatchFault` | page 1 | Reports the right Headlamp Control Module (HCMR) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_HVPmismatchFault` | page 1 | Reports the High Voltage Processor (HVP) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_IBSTCALmismatchFault` | page 1 | Reports the electromechanical brake booster calibration, or iBooster Calibration (IBSTCAL), electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_IBSTmismatchFault` | page 1 | Reports the electromechanical brake booster, or iBooster (IBST), electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_LVBMSmismatchFault` | page 1 | Reports the Low Voltage Battery Management System (LVBMS) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_OCS1PmismatchFault` | page 1 | Reports the Occupancy Classification System - 1st Row Passenger (OCS1P) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_OPCFmismatchFault` | page 1 | Reports the front Oil Pump Controller (OPCF) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_OPCRmismatchFault` | page 1 | Reports the rear Oil Pump Controller (OPCR) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_PARKmismatchFault` | page 1 | Reports the Park Assist (PARK) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_PCSCPU2mismatchFault` | page 1 | Reports the Power Conversion System AC charging core (PCSCPU2) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_PCSmismatchFault` | page 1 | Reports the Power Conversion System (PCS) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_PMFmismatchFault` | page 1 | Reports the front Pedal Monitor (PMF) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_PMRmismatchFault` | page 1 | Reports the rear Pedal Monitor (PMR) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_PTCmismatchFault` | page 1 | Reports the Positive Temperature Coefficient (PTC) heater electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_RCMCALmismatchFault` | page 1 | Reports the Restraint Control Module Calibration (RCMCAL) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_RCMmismatchFault` | page 1 | Reports the Restraint Control Module (RCM) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_SCCMmismatchFault` | page 1 | Reports the Steering Column Control Module (SCCM) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_SDCRmismatchFault` | page 1 | Reports the Secondary Disconnect Controller (SDCR) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_SWCmismatchFault` | page 1 | Reports the Steering Wheel Controller (SWC) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_THSmismatchFault` | page 1 | Reports the Temperature Humidity Sensor (THS) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_VCFRONTmismatchFault` | page 1 | Reports the front vehicle controller (VCFRONT) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_VCLEFTmismatchFault` | page 1 | Reports the left vehicle controller (VCLEFT) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_VCRIGHTmismatchFault` | page 1 | Reports the right vehicle controller (VCRIGHT) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_VCSECmismatchFault` | page 1 | Reports the vehicle security controller (VCSEC) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_PMmismatchFault` | page 1 | Reports the Pedal Monitor (PM) electronic control unit (ECU) running a firmware version that does not match the rest of the vehicle | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Multiplexing

`GTW_mismatchFaultIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (46 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 ETH DBC file](../../../../../dbc/Model3/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Gateway messages (GTW)](../../gtw.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
