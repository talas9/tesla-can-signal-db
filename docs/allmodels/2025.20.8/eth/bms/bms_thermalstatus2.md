---
layout: default
title: "BMS_thermalStatus2 (0x7EC) — High-voltage battery management system, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "High-voltage battery management system message: thermal status2. Ethernet-side message BMS_thermalStatus2 of High-voltage battery management system for Tesla Model 3 / Model Y firmware 2025.20.8, 7 signals (BMS_coldStagnationLimit, BMS_hotStagnationLimit, BMS_hotCellTempLimit, BMS_activeCoolCellReferenceT and 3 more). Bit layout, scaling, units and value tables."
---

# BMS_thermalStatus2 (0x7EC) — High-voltage battery management system, Tesla Model 3 / Model Y 2025.20.8 ETH

High-voltage battery management system message: thermal status2. This page documents the 7 signals of BMS_thermalStatus2 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_thermalStatus2` |
| Ethernet-side id | 0x7EC (2028) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | BMS |
| Frame length | 7 bytes |
| Cycle time | 1000 ms |
| Signals | 7 |

## Signals of BMS_thermalStatus2

Tesla Model 3 / Model Y CAN bus signals in `BMS_thermalStatus2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_coldStagnationLimit` | Minimum temperature at which the pack is allowed to be used as a heat-energy source | 0\|9 | little-endian | unsigned | 0.25 | -25 | DegC | -25 to 100 |  | plausible |
| `BMS_hotStagnationLimit` | Maximum temperature at which we allow the pack to be used for heat-energy storage | 9\|9 | little-endian | unsigned | 0.25 | -25 | DegC | -25 to 100 |  | plausible |
| `BMS_hotCellTempLimit` | Maximum temperature at which the pack will allow limp mode levels of current | 18\|9 | little-endian | unsigned | 0.25 | -25 | DegC | -25 to 100 |  | plausible |
| `BMS_activeCoolCellReferenceT` | Desired cell temperature reference which composes the temperature trajectory portion of the active cooling target temperature controls | 27\|9 | little-endian | unsigned | 0.25 | -25 | DegC | -25 to 100 |  | plausible |
| `BMS_activeHeatCellTargetT` | Desired cell temperature which feeds as an input to the active heating target temperature, before any additional controls calculations | 36\|9 | little-endian | unsigned | 0.25 | -25 | DegC | -25 to 100 |  | plausible |
| `BMS_cellTempTargetMode` | Operating mode of the thermal controls for the Battery Management System (BMS) | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `DEFAULT`<br>1 = `LOW_POWER_CHARGE`<br>2 = `HIGH_POWER_CHARGE`<br>3 = `CONNECTED_PRECONDITION`<br>4 = `DISCONNECTED_PRECONDITION`<br>5 = `ACTIVE_HEAT_ON_NAV`<br>6 = `PASSIVE_HEAT_ON_NAV`<br>7 = `DRAGSTRIP`<br>8 = `SOH_HEAT_PACK`<br>9 = `ACTIVE_COOL_ON_NAV`<br>10 = `PASSIVE_COOL_ON_NAV`<br>11 = `V2X_SESSION` | plausible |
| `BMS_requestDischarge` | Flag identifying when the Battery Management System (BMS) is requesting the battery pack to be discharged | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
