---
layout: default
title: "FC_evseBilling2 (0x536) — FC ECU, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "FC ECU message: evse billing2. Tesla Model 3 / Model Y CAN bus message FC_evseBilling2 (0x536) of FC ECU, firmware 2025.20.8, 3 signals (FC_evseBilling2DataSelect, FC_evsePpuEnabled, FC_evseBillingEnergyHighRes). Bit layout, scaling, units and value tables."
---

# FC_evseBilling2 (0x536) — FC ECU, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

FC ECU message: evse billing2; frame length from the layout, not yet observed on a vehicle bus. This page documents the 3 signals of FC_evseBilling2 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `FC_evseBilling2` |
| CAN id | 0x536 (1334) |
| ECU | [FC ECU](../../fc.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | FC |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 3 |

## Signals of FC_evseBilling2

Tesla Model 3 / Model Y CAN bus signals in `FC_evseBilling2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `FC_evseBilling2DataSelect` | selector | FC ECU: evse billing2 data select | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `FC_EVSEBILLING2_DATASELECT_0` | plausible |
| `FC_evsePpuEnabled` | page 0 | FC ECU: evse ppu enabled | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `FC_evseBillingEnergyHighRes` | page 0 | FC ECU: evse billing energy high res; raw 16777215 = signal not available (SNA) | 8\|24 | little-endian | unsigned | 0.0001 | 0 | kWh | 0 to 1677.7214 | 16777215 = `SNA` | validated |

## Multiplexing

`FC_evseBilling2DataSelect` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All FC ECU messages (FC)](../../fc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
