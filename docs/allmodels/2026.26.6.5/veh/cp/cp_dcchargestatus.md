---
layout: default
title: "CP_dcChargeStatus (0x29D) — Charge port controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Charge port controller message: dc charge status. Tesla Model 3 / Model Y CAN bus message CP_dcChargeStatus (0x29D) of Charge port controller, firmware 2026.26.6.5, 5 signals (CP_evseOutputDcCurrent, CP_evseOutputDcVoltage, CP_evseOutputDcCurrentStale, CP_evRelocationRecommended and 1 more). Bit layout, scaling, units and value tables."
---

# CP_dcChargeStatus (0x29D) — Charge port controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Charge port controller message: dc charge status; frame length observed on a vehicle bus. This page documents the 5 signals of CP_dcChargeStatus as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `CP_dcChargeStatus` |
| CAN id | 0x29D (669) |
| ECU | [Charge port controller](../../cp.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | CP |
| Frame length | 5 bytes |
| Cycle time | 100 ms |
| Signals | 5 |

## Signals of CP_dcChargeStatus

Tesla Model 3 / Model Y CAN bus signals in `CP_dcChargeStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `CP_evseOutputDcCurrent` | The DC EVSE's measured output current | 0\|15 | little-endian | signed | 0.125 | 0 | A | -2048 to 2047.875 |  | validated |
| `CP_evseOutputDcVoltage` | The DC EVSE's measured output voltage | 16\|13 | little-endian | unsigned | 0.07324219 | 0 | V | 0 to 599.92675822 |  | validated |
| `CP_evseOutputDcCurrentStale` | Indicates whether the data in CP_evseOutputDcCurrent has not been updated with new info from the DC EVSE recently | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_evRelocationRecommended` | Indicates whether the supercharger EVSE recommends relocating the vehicle | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `CP_evseDeratingReason` | Reports the derating reason from Supercharger EVSE | 32\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `EVSE_DERATING_NONE`<br>1 = `EVSE_DERATING_CABLE_TEMP_FOLDBACK`<br>2 = `EVSE_DERATING_POST_SYSTEM_FAULT`<br>31 = `EVSE_DERATING_INVALID` | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Charge port controller messages (CP)](../../cp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
