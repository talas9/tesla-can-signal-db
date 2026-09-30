---
layout: default
title: "VEH_billing (0x453) — VEH ECU, Tesla Model 3 2025.20.8 VEH CAN"
description: "VEH ECU message: billing. Tesla Model 3 CAN bus message VEH_billing (0x453) of VEH ECU, firmware 2025.20.8, 1 signals (VEH_pricebookId). Bit layout, scaling, units and value tables."
---

# VEH_billing (0x453) — VEH ECU, Tesla Model 3 2025.20.8 VEH CAN

VEH ECU message: billing; forwarded onto this bus by the gateway; frame length observed on a vehicle bus. This page documents the 1 signals of VEH_billing as defined for Tesla Model 3 firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VEH_billing` |
| CAN id | 0x453 (1107) |
| ECU | [VEH ECU](../../veh.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 4 bytes |
| Cycle time | 1000 ms |
| Signals | 1 |

## Signals of VEH_billing

Tesla Model 3 CAN bus signals in `VEH_billing`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VEH_pricebookId` | VEH ECU: pricebook id | 0\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 VEH DBC file](../../../../../dbc/Model3/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/VEH.json)

## See also

- [All VEH ECU messages (VEH)](../../veh.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
