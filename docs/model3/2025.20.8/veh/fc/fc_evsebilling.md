---
layout: default
title: "FC_evseBilling (0x45D) — FC ECU, Tesla Model 3 2025.20.8 VEH CAN"
description: "FC ECU message: evse billing. Tesla Model 3 CAN bus message FC_evseBilling (0x45D) of FC ECU, firmware 2025.20.8, 6 signals (FC_evseBillingDataSelect, FC_evseBillingEnergy, FC_evseMeterPower, FC_evseMeterCurrent and 2 more). Bit layout, scaling, units and value tables."
---

# FC_evseBilling (0x45D) — FC ECU, Tesla Model 3 2025.20.8 VEH CAN

FC ECU message: evse billing; frame length from the layout, not yet observed on a vehicle bus. This page documents the 6 signals of FC_evseBilling as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `FC_evseBilling` |
| CAN id | 0x45D (1117) |
| ECU | [FC ECU](../../fc.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | FC |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 6 |

## Signals of FC_evseBilling

Tesla Model 3 CAN bus signals in `FC_evseBilling`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `FC_evseBillingDataSelect` | selector | FC ECU: evse billing data select | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `0`<br>1 = `1` | plausible |
| `FC_evseBillingEnergy` | page 0 | FC ECU: evse billing energy | 4\|20 | little-endian | unsigned | 0.001 | 0 | kWh | 0 to 1048.575 |  | plausible |
| `FC_evseMeterPower` | page 0 | FC ECU: evse meter power | 24\|20 | little-endian | unsigned | 0.001 | 0 | kW | 0 to 1048.575 |  | plausible |
| `FC_evseMeterCurrent` | page 0 | FC ECU: evse meter current | 44\|10 | little-endian | unsigned | 1 | 0 | A | 0 to 1023 |  | plausible |
| `FC_evseMeterVoltage` | page 0 | FC ECU: evse meter voltage | 54\|10 | little-endian | unsigned | 1 | 0 | V | 0 to 1023 |  | plausible |
| `FC_evseMeterFwGitHash` | page 1 | FC ECU: evse meter fw git hash | 4\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | layout-only |

## Multiplexing

`FC_evseBillingDataSelect` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (4 signals), page 1 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All FC ECU messages (FC)](../../fc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
