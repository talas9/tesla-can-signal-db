---
layout: default
title: "PMF_mfgData (0x524) — PMF ECU, Tesla Model Y 2025.20.8 PARTY CAN"
description: "PMF ECU message: mfg data. Tesla Model Y CAN bus message PMF_mfgData (0x524) of PMF ECU, firmware 2025.20.8, 4 signals (PMF_processorDieIdLot, PMF_processorDieIdWafer, PMF_processorDieIdX, PMF_processorDieIdY). Bit layout, scaling, units and value tables."
---

# PMF_mfgData (0x524) — PMF ECU, Tesla Model Y 2025.20.8 PARTY CAN

PMF ECU message: mfg data; frame length from the layout, not yet observed on a vehicle bus. This page documents the 4 signals of PMF_mfgData as defined for Tesla Model Y firmware 2025.20.8 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PMF_mfgData` |
| CAN id | 0x524 (1316) |
| ECU | [PMF ECU](../../pmf.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | PMF |
| Frame length | 7 bytes |
| Cycle time | 1000 ms |
| Signals | 4 |

## Signals of PMF_mfgData

Tesla Model Y CAN bus signals in `PMF_mfgData`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PMF_processorDieIdLot` | PMF ECU: processor die id lot | 0\|24 | little-endian | unsigned | 1 | 0 |  | 0 to 16777215 |  | validated |
| `PMF_processorDieIdWafer` | PMF ECU: processor die id wafer | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `PMF_processorDieIdX` | PMF ECU: processor die id x | 32\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | validated |
| `PMF_processorDieIdY` | PMF ECU: processor die id y | 44\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | validated |

## Download the DBC file

- [Tesla Model Y 2025.20.8 PARTY DBC file](../../../../../dbc/ModelY/2025.20.8/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/PARTY.json)

## See also

- [All PMF ECU messages (PMF)](../../pmf.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
