---
layout: default
title: "VC_pcsInterface (0x441) — VC ECU, Tesla Model Y 2025.20.8 ETH"
description: "VC ECU message: pcs interface. Ethernet-side message VC_pcsInterface of VC ECU for Tesla Model Y firmware 2025.20.8, 12 signals (VC_pcsInterfaceMuxIndex, VC_pcsInterfaceCounter, VC_pcsInterfaceChecksum, VC_pcsLVVoltageTarget and 8 more). Bit layout, scaling, units and value tables."
---

# VC_pcsInterface (0x441) — VC ECU, Tesla Model Y 2025.20.8 ETH

VC ECU message: pcs interface. This page documents the 12 signals of VC_pcsInterface as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VC_pcsInterface` |
| Ethernet-side id | 0x441 (1089) |
| ECU | [VC ECU](../../vc.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VC |
| Frame length | 8 bytes |
| Cycle time | 50 ms |
| Signals | 12 |

## Signals of VC_pcsInterface

Tesla Model Y CAN bus signals in `VC_pcsInterface`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VC_pcsInterfaceMuxIndex` | selector | VC ECU: pcs interface mux index | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `0`<br>1 = `1` | plausible |
| `VC_pcsInterfaceCounter` |  | VC ECU: pcs interface counter | 50\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `VC_pcsInterfaceChecksum` |  | VC ECU: pcs interface checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VC_pcsLVVoltageTarget` | page 0 | VC ECU: pcs LV voltage target | 0\|13 | little-endian | unsigned | 0.01 | 0 | V | 0 to 65.535 |  | validated |
| `VC_pcsLVMinVoltageLimit` | page 0 | VC ECU: pcs LV min voltage limit | 13\|13 | little-endian | unsigned | 0.01 | 0 | V | 0 to 65.535 |  | validated |
| `VC_pcsLVMaxVoltageLimit` | page 0 | VC ECU: pcs LV max voltage limit | 27\|13 | little-endian | unsigned | 0.01 | 0 | V | 0 to 65.535 |  | validated |
| `VC_goodForPCSPowerCycle` | page 0 | VC ECU: good for PCS power cycle | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_LVBatteryCannotSupportVehicle` | page 0 | VC ECU: LV battery cannot support vehicle | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VC_pcsResistanceFiltered` | page 1 | VC ECU: pcs resistance filtered; raw 65535 = signal not available (SNA) | 0\|16 | little-endian | unsigned | 0.01 | 0 | mOhm | 0 to 655.34 | 65535 = `SNA` | validated |
| `VC_pcsLVMaxDchrgCurrentLimit` | page 1 | VC ECU: pcs LV max dchrg current limit | 16\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 400 |  | validated |
| `VC_defaultPcsLVVoltageTarget` | page 1 | VC ECU: default pcs LV voltage target | 28\|13 | little-endian | unsigned | 0.01 | 0 | V | 0 to 65.535 |  | validated |
| `VC_lvHwProtSelfTestActive` | page 1 | Reports whether Low Voltage (LV) Hardware (HW) protection self-tests are running or about to run due to a retry. | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Multiplexing

`VC_pcsInterfaceMuxIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (5 signals), page 1 (4 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All VC ECU messages (VC)](../../vc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
