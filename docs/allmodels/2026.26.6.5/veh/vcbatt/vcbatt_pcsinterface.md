---
layout: default
title: "VCBATT_pcsInterface (0x442) — VCBATT ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "VCBATT ECU message: pcs interface. Tesla Model 3 / Model Y CAN bus message VCBATT_pcsInterface (0x442) of VCBATT ECU, firmware 2026.26.6.5, 13 signals (VCBATT_pcsInterfaceMuxIndex, VCBATT_pcsInterfaceCounter, VCBATT_pcsInterfaceChecksum, VCBATT_pcsLVVoltageTarget and 9 more). Bit layout, scaling, units and value tables."
---

# VCBATT_pcsInterface (0x442) — VCBATT ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

VCBATT ECU message: pcs interface; frame length from the layout, not yet observed on a vehicle bus. This page documents the 13 signals of VCBATT_pcsInterface as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCBATT_pcsInterface` |
| CAN id | 0x442 (1090) |
| ECU | [VCBATT ECU](../../vcbatt.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCBATT |
| Frame length | 8 bytes |
| Cycle time | 50 ms |
| Signals | 13 |

## Signals of VCBATT_pcsInterface

Tesla Model 3 / Model Y CAN bus signals in `VCBATT_pcsInterface`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCBATT_pcsInterfaceMuxIndex` | selector | VCBATT ECU: pcs interface mux index | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `0`<br>1 = `1` | plausible |
| `VCBATT_pcsInterfaceCounter` |  | VCBATT ECU: pcs interface counter | 50\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `VCBATT_pcsInterfaceChecksum` |  | VCBATT ECU: pcs interface checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCBATT_pcsLVVoltageTarget` | page 0 | VCBATT ECU: pcs LV voltage target | 0\|13 | little-endian | unsigned | 0.01 | 0 | V | 0 to 65.535 |  | validated |
| `VCBATT_pcsLVMinVoltageLimit` | page 0 | VCBATT ECU: pcs LV min voltage limit | 13\|13 | little-endian | unsigned | 0.01 | 0 | V | 0 to 65.535 |  | validated |
| `VCBATT_pcsLVMaxVoltageLimit` | page 0 | VCBATT ECU: pcs LV max voltage limit | 27\|13 | little-endian | unsigned | 0.01 | 0 | V | 0 to 65.535 |  | validated |
| `VCBATT_goodForPCSPowerCycle` | page 0 | VCBATT ECU: good for PCS power cycle | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT_LVBatteryCannotSupportVehicle` | page 0 | VCBATT ECU: LV battery cannot support vehicle | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT_pcsResistanceFiltered` | page 1 | VCBATT ECU: pcs resistance filtered; raw 65535 = signal not available (SNA) | 0\|16 | little-endian | unsigned | 0.01 | 0 | mOhm | 0 to 655.34 | 65535 = `SNA` | validated |
| `VCBATT_pcsLVMaxDchrgCurrentLimit` | page 1 | VCBATT ECU: pcs LV max dchrg current limit | 16\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 400 |  | validated |
| `VCBATT_defaultPcsLVVoltageTarget` | page 1 | VCBATT ECU: default pcs LV voltage target | 28\|13 | little-endian | unsigned | 0.01 | 0 | V | 0 to 65.535 |  | validated |
| `VCBATT_lvHwProtSelfTestActive` | page 1 | Reports whether Low Voltage (LV) Hardware (HW) protection self-tests are running or about to run due to a retry. | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT_lvBatteryDischargeRequest` | page 1 | VCBATT ECU: lv battery discharge request | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Multiplexing

`VCBATT_pcsInterfaceMuxIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (5 signals), page 1 (5 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All VCBATT ECU messages (VCBATT)](../../vcbatt.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
