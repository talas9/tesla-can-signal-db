---
layout: default
title: "PMR_mfgData (0x554) — PMR ECU, Tesla Model 3 / Model Y 2025.20.8 PARTY CAN"
description: "PMR ECU message: mfg data. Tesla Model 3 / Model Y CAN bus message PMR_mfgData (0x554) of PMR ECU, firmware 2025.20.8, 4 signals (PMR_processorDieIdLot, PMR_processorDieIdWafer, PMR_processorDieIdX, PMR_processorDieIdY). Bit layout, scaling, units and value tables."
---

# PMR_mfgData (0x554) — PMR ECU, Tesla Model 3 / Model Y 2025.20.8 PARTY CAN

PMR ECU message: mfg data; frame length from the layout, not yet observed on a vehicle bus. This page documents the 4 signals of PMR_mfgData as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PMR_mfgData` |
| CAN id | 0x554 (1364) |
| ECU | [PMR ECU](../../pmr.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | PMR |
| Frame length | 7 bytes |
| Cycle time | 1000 ms |
| Signals | 4 |

## Signals of PMR_mfgData

Tesla Model 3 / Model Y CAN bus signals in `PMR_mfgData`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PMR_processorDieIdLot` | PMR ECU: processor die id lot | 0\|24 | little-endian | unsigned | 1 | 0 |  | 0 to 16777215 |  | validated |
| `PMR_processorDieIdWafer` | PMR ECU: processor die id wafer | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `PMR_processorDieIdX` | PMR ECU: processor die id x | 32\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | validated |
| `PMR_processorDieIdY` | PMR ECU: processor die id y | 44\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 PARTY DBC file](../../../../../dbc/AllModels/2025.20.8/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/PARTY.json)

## See also

- [All PMR ECU messages (PMR)](../../pmr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
