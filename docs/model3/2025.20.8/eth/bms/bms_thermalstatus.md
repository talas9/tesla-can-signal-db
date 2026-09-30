---
layout: default
title: "BMS_thermalStatus (0x312) — High-voltage battery management system, Tesla Model 3 2025.20.8 ETH"
description: "High-voltage battery management system message: thermal status. Ethernet-side message BMS_thermalStatus of High-voltage battery management system for Tesla Model 3 firmware 2025.20.8, 9 signals (BMS_powerDissipation, BMS_flowRequest, BMS_inletActiveCoolTargetT, BMS_inletPassiveTargetT and 5 more). Bit layout, scaling, units and value tables."
---

# BMS_thermalStatus (0x312) — High-voltage battery management system, Tesla Model 3 2025.20.8 ETH

High-voltage battery management system message: thermal status. This page documents the 9 signals of BMS_thermalStatus as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_thermalStatus` |
| Ethernet-side id | 0x312 (786) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 9 |

## Signals of BMS_thermalStatus

Tesla Model 3 CAN bus signals in `BMS_thermalStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_powerDissipation` | High-voltage battery management system: power dissipation | 0\|10 | little-endian | unsigned | 0.02 | 0 | kW | 0 to 20 |  | plausible |
| `BMS_flowRequest` | Requested coolant flow rate in liters per minute (LPM) from the Battery Management System (BMS) to the thermal module | 10\|7 | little-endian | unsigned | 0.3 | 0 | LPM | 0 to 38.1 |  | plausible |
| `BMS_inletActiveCoolTargetT` | Calculated active cooling temperature target at the inlet | 17\|9 | little-endian | unsigned | 0.25 | -25 | DegC | -25 to 100 |  | plausible |
| `BMS_inletPassiveTargetT` | Calculated passive temperature target at the inlet | 26\|9 | little-endian | unsigned | 0.25 | -25 | DegC | -25 to 100 |  | plausible |
| `BMS_inletActiveHeatTargetT` | Calculated active heating temperature target at the inlet | 35\|9 | little-endian | unsigned | 0.25 | -25 | DegC | -25 to 100 |  | plausible |
| `BMS_minPackTemperature` | Minimum pack temperature for consumption by external entities | 44\|9 | little-endian | unsigned | 0.25 | -25 | DegC | -25 to 102.75 |  | plausible |
| `BMS_maxPackTemperature` | Maximum pack temperature for consumption by external entities | 53\|9 | little-endian | unsigned | 0.25 | -25 | DegC | -25 to 102.75 |  | plausible |
| `BMS_pcsNoFlowRequest` | High-voltage battery management system: pcs no flow request | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `BMS_noFlowRequest` | High-voltage battery management system: no flow request | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
