---
layout: default
title: "UI_tripPlannerInfo (0x4EF) — Touchscreen user interface computer, Tesla Model Y 2026.26.6.5 ETH"
description: "Touchscreen user interface computer message: trip planner info. Ethernet-side message UI_tripPlannerInfo of Touchscreen user interface computer for Tesla Model Y firmware 2026.26.6.5, 3 signals (UI_fwHeatOnNavArrivalSOE, UI_voyagerHeatOnNavArrivalSOE, UI_usingVoyagerPreconditioning). Bit layout, scaling, units and value tables."
---

# UI_tripPlannerInfo (0x4EF) — Touchscreen user interface computer, Tesla Model Y 2026.26.6.5 ETH

Touchscreen user interface computer message: trip planner info. This page documents the 3 signals of UI_tripPlannerInfo as defined for Tesla Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_tripPlannerInfo` |
| Ethernet-side id | 0x4EF (1263) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 5 bytes |
| Cycle time | 1000 ms |
| Signals | 3 |

## Signals of UI_tripPlannerInfo

Tesla Model Y CAN bus signals in `UI_tripPlannerInfo`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_fwHeatOnNavArrivalSOE` | Energy percentages shown in the UI | 0\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 100 |  | validated |
| `UI_voyagerHeatOnNavArrivalSOE` | Energy percentages shown in the UI | 16\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 100 |  | validated |
| `UI_usingVoyagerPreconditioning` | Touchscreen user interface computer: using voyager preconditioning | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/ModelY/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
