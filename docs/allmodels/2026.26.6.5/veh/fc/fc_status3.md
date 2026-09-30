---
layout: default
title: "FC_status3 (0x217) — FC ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "FC ECU message: status3. Tesla Model 3 / Model Y CAN bus message FC_status3 (0x217) of FC ECU, firmware 2026.26.6.5, 9 signals (FC_status3DataSelect, FC_status3DummySig, FC_class, FC_brand and 5 more). Bit layout, scaling, units and value tables."
---

# FC_status3 (0x217) — FC ECU, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

FC ECU message: status3; frame length from the layout, not yet observed on a vehicle bus. This page documents the 9 signals of FC_status3 as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `FC_status3` |
| CAN id | 0x217 (535) |
| ECU | [FC ECU](../../fc.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | FC |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 9 |

## Signals of FC_status3

Tesla Model 3 / Model Y CAN bus signals in `FC_status3`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `FC_status3DataSelect` | selector | FC ECU: status3 data select | 0\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 | 0 = `Mux0`<br>1 = `Mux1` | plausible |
| `FC_status3DummySig` |  | FC ECU: status3 dummy sig | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `FC_class` | page 0 | FC ECU: class; raw 0 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 1 | 0 |  | 1 to 255 | 0 = `FC_CLASS_SNA`<br>1 = `FC_CLASS_SUPERCHARGER`<br>2 = `FC_CLASS_URBANCHARGER` | validated |
| `FC_brand` | page 0 | Fast charger brand; raw 0 = signal not available (SNA) | 16\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `SNA`<br>1 = `TESLA` | validated |
| `FC_coolingType` | page 0 | Type of cooling used for the supercharger; raw 0 = signal not available (SNA) | 20\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `FC_COOLING_TYPE_SNA`<br>1 = `FC_COOLING_TYPE_LIQUID`<br>2 = `FC_COOLING_TYPE_CONVECTION`<br>3 = `FC_COOLING_TYPE_IMMERSION` | validated |
| `FC_uiStopType` | page 0 | Type of stop type supported from the UI; raw 0 = signal not available (SNA) | 24\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `FC_UI_STOP_TYPE_SNA`<br>1 = `FC_UI_STOP_TYPE_TOGGLE`<br>2 = `FC_UI_STOP_TYPE_MOMENTARY` | validated |
| `FC_emergencyShutdownSupported` | page 0 | Indicates if the supercharger supports fast emergency shutdown requests from vehicle | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `FC_generation` | page 0 | Hardware generation of the Tesla EVSE; raw 0 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 1 | 0 |  | 1 to 255 | 0 = `GENERATION_SNA` | validated |
| `FC_billingEnergy` | page 1 | Total billable charge energy (integrated by EVSE). Position from firmware; message assignment inferred. | 8\|16 | little-endian | unsigned | 0.015259 | 0 | kWh | 0 to 999.998565 |  | plausible |

## Multiplexing

`FC_status3DataSelect` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (6 signals), page 1 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All FC ECU messages (FC)](../../fc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
