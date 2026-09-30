---
layout: default
title: "VC_pcsManagement (0x443) — VC ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "VC ECU message: pcs management. Tesla Model 3 / Model Y CAN bus message VC_pcsManagement (0x443) of VC ECU, firmware 2026.26.6.5, 6 signals (VC_pcsManagementChecksum, VC_pcsManagementCounter, VC_pcsManagementMuxIndex, VC_dcdcLVVoltageTargetMax and 2 more). Bit layout, scaling, units and value tables."
---

# VC_pcsManagement (0x443) — VC ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

VC ECU message: pcs management; frame length observed on a vehicle bus. This page documents the 6 signals of VC_pcsManagement as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VC_pcsManagement` |
| CAN id | 0x443 (1091) |
| ECU | [VC ECU](../../vc.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VC |
| Frame length | 6 bytes |
| Cycle time | 500 ms |
| Signals | 6 |

## Signals of VC_pcsManagement

Tesla Model 3 / Model Y CAN bus signals in `VC_pcsManagement`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VC_pcsManagementChecksum` |  | VC ECU: pcs management checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VC_pcsManagementCounter` |  | VC ECU: pcs management counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `VC_pcsManagementMuxIndex` | selector | VC ECU: pcs management mux index | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `INDEX_0` | plausible |
| `VC_dcdcLVVoltageTargetMax` | page 0 | VC ECU: dcdc LV voltage target max | 16\|10 | little-endian | unsigned | 0.1 | 0 | V | 0 to 102.3 | 1023 = `UNRESTRICTED` | validated |
| `VC_dcdcLVVoltageTargetMin` | page 0 | VC ECU: dcdc LV voltage target min | 26\|10 | little-endian | unsigned | 0.1 | 0 | V | 0 to 102.3 | 0 = `UNRESTRICTED` | validated |
| `VC_dcdcLVInputPowerLimit` | page 0 | VC ECU: dcdc LV input power limit | 36\|8 | little-endian | unsigned | 50 | 0 | W | 0 to 12750 | 255 = `UNRESTRICTED` | validated |

## Multiplexing

`VC_pcsManagementMuxIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (3 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All VC ECU messages (VC)](../../vc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
