---
layout: default
title: "BMS_thermalStatus (0x312) — High-voltage battery management system, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "High-voltage battery management system message: thermal status. Tesla Model 3 / Model Y CAN bus message BMS_thermalStatus (0x312) of High-voltage battery management system, firmware 2026.26.6.5, 18 signals (BMS_thermalStatusMultiplexer, BMS_inletActiveCoolTargetT, BMS_inletPassiveTargetT, BMS_inletActiveHeatTargetT and 14 more). Bit layout, scaling, units and value tables."
---

# BMS_thermalStatus (0x312) — High-voltage battery management system, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

High-voltage battery management system message: thermal status; frame length observed on a vehicle bus. This page documents the 18 signals of BMS_thermalStatus as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_thermalStatus` |
| CAN id | 0x312 (786) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 18 |

## Signals of BMS_thermalStatus

Tesla Model 3 / Model Y CAN bus signals in `BMS_thermalStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_thermalStatusMultiplexer` | selector | High-voltage battery management system: thermal status multiplexer | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `Mux0`<br>1 = `Mux1` | plausible |
| `BMS_inletActiveCoolTargetT` | page 0 | Calculated active cooling temperature target at the inlet | 2\|9 | little-endian | unsigned | 0.25 | -25 | DegC | -25 to 100 |  | validated |
| `BMS_inletPassiveTargetT` | page 0 | Calculated passive temperature target at the inlet | 11\|9 | little-endian | unsigned | 0.25 | -25 | DegC | -25 to 100 |  | validated |
| `BMS_inletActiveHeatTargetT` | page 0 | Calculated active heating temperature target at the inlet | 20\|9 | little-endian | unsigned | 0.25 | -25 | DegC | -25 to 100 |  | validated |
| `BMS_requestDischarge` | page 0 | Flag identifying when the Battery Management System (BMS) is requesting the battery pack to be discharged | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_activeHeatingWorthwhile` | page 0 | Determination by the Battery Management System (BMS) if active heating is worthwhile | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_pcsNoFlowRequest` | page 0 | High-voltage battery management system: pcs no flow request | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_minPackTemperature` | page 0 | Minimum pack temperature for consumption by external entities | 32\|10 | little-endian | unsigned | 0.2 | -40 | DegC | -40 to 164.6 |  | validated |
| `BMS_noFlowRequest` | page 0 | High-voltage battery management system: no flow request | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_maxPackTemperature` | page 0 | Maximum pack temperature for consumption by external entities | 43\|11 | little-endian | unsigned | 0.1 | -40 | DegC | -40 to 164.7 |  | validated |
| `BMS_flowRequest` | page 0 | Requested coolant flow rate in liters per minute (LPM) from the Battery Management System (BMS) to the thermal module | 56\|8 | little-endian | unsigned | 0.25 | 0 | LPM | 0 to 60 |  | validated |
| `BMS_coldStagnationLimit` | page 1 | Minimum temperature at which the pack is allowed to be used as a heat-energy source | 2\|9 | little-endian | unsigned | 0.25 | -25 | DegC | -25 to 100 |  | validated |
| `BMS_hotStagnationLimit` | page 1 | Maximum temperature at which we allow the pack to be used for heat-energy storage | 11\|9 | little-endian | unsigned | 0.25 | -25 | DegC | -25 to 100 |  | validated |
| `BMS_hotCellTempLimit` | page 1 | Maximum temperature at which the pack will allow limp mode levels of current | 20\|9 | little-endian | unsigned | 0.25 | -25 | DegC | -25 to 100 |  | validated |
| `BMS_i2tDeratingEnabled` | page 1 | High-voltage battery management system: i2t derating enabled | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `BMS_activeCoolCellReferenceT` | page 1 | Desired cell temperature reference which composes the temperature trajectory portion of the active cooling target temperature controls | 32\|9 | little-endian | unsigned | 0.25 | -25 | DegC | -25 to 100 |  | validated |
| `BMS_activeHeatCellTargetT` | page 1 | Desired cell temperature which feeds as an input to the active heating target temperature, before any additional controls calculations | 41\|9 | little-endian | unsigned | 0.25 | -25 | DegC | -25 to 100 |  | validated |
| `BMS_powerDissipation` | page 1 | High-voltage battery management system: power dissipation | 50\|10 | little-endian | unsigned | 0.02 | 0 | kW | 0 to 20 |  | validated |

## Multiplexing

`BMS_thermalStatusMultiplexer` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (10 signals), page 1 (7 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
