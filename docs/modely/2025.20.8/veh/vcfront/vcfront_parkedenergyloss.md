---
layout: default
title: "VCFRONT_parkedEnergyLoss (0x3BD) — Front body controller, Tesla Model Y 2025.20.8 VEH CAN"
description: "Front body controller message: parked energy loss. Tesla Model Y CAN bus message VCFRONT_parkedEnergyLoss (0x3BD) of Front body controller, firmware 2025.20.8, 17 signals (VCFRONT_energyLossIndex, VCFRONT_userEnergyLossSinceDrive, VCFRONT_preconditioningEnergyLossSinceDrive, VCFRONT_cabinOverheatEnergyLossSinceDrive and 13 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_parkedEnergyLoss (0x3BD) — Front body controller, Tesla Model Y 2025.20.8 VEH CAN

Front body controller message: parked energy loss; frame length observed on a vehicle bus. This page documents the 17 signals of VCFRONT_parkedEnergyLoss as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_parkedEnergyLoss` |
| CAN id | 0x3BD (957) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 17 |

## Signals of VCFRONT_parkedEnergyLoss

Tesla Model Y CAN bus signals in `VCFRONT_parkedEnergyLoss`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_energyLossIndex` | selector | Front body controller: energy loss index | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STATUS`<br>1 = `SINCE_LAST_DRIVE`<br>2 = `SINCE_LAST_DRIVE2`<br>3 = `SINCE_LAST_CHARGE`<br>4 = `SINCE_LAST_CHARGE2` | plausible |
| `VCFRONT_userEnergyLossSinceDrive` | page 1 | Energy loss due to user interaction since last drive | 8\|14 | little-endian | unsigned | 0.01 | 0 | kWh | 0 to 163.83 |  | validated |
| `VCFRONT_preconditioningEnergyLossSinceDrive` | page 1 | Energy loss due to preconditioning since last drive | 22\|14 | little-endian | unsigned | 0.01 | 0 | kWh | 0 to 163.83 |  | validated |
| `VCFRONT_cabinOverheatEnergyLossSinceDrive` | page 1 | Energy loss due to cabin overheat protection since last drive | 36\|14 | little-endian | unsigned | 0.01 | 0 | kWh | 0 to 163.83 |  | validated |
| `VCFRONT_mobileAppEnergyLossSinceDrive` | page 1 | Energy loss due to mobile app interaction since last drive | 50\|14 | little-endian | unsigned | 0.01 | 0 | kWh | 0 to 163.83 |  | validated |
| `VCFRONT_summonStandbyEnergyLossSinceDrive` | page 2 | Energy loss due to summon standby since last drive | 8\|14 | little-endian | unsigned | 0.01 | 0 | kWh | 0 to 163.83 |  | validated |
| `VCFRONT_sentryModeEnergyLossSinceDrive` | page 2 | Energy loss due to sentry mode since last drive | 22\|14 | little-endian | unsigned | 0.01 | 0 | kWh | 0 to 163.83 |  | validated |
| `VCFRONT_backgroundEnergyLossSinceDrive` | page 2 | Energy loss due to background vehicle op since last drive | 36\|14 | little-endian | unsigned | 0.01 | 0 | kWh | 0 to 163.83 |  | validated |
| `VCFRONT_evapDryingEnergyLossSinceDrive` | page 2 | Energy loss due to evap drying since last drive | 50\|14 | little-endian | unsigned | 0.01 | 0 | kWh | 0 to 163.83 |  | validated |
| `VCFRONT_userEnergyLossSinceCharge` | page 3 | Energy loss due to user interaction since last charge | 8\|14 | little-endian | unsigned | 0.01 | 0 | kWh | 0 to 163.83 |  | validated |
| `VCFRONT_preconditioningEnergyLossSinceCharge` | page 3 | Energy loss due to preconditioning since last charge | 22\|14 | little-endian | unsigned | 0.01 | 0 | kWh | 0 to 163.83 |  | validated |
| `VCFRONT_cabinOverheatEnergyLossSinceCharge` | page 3 | Energy loss due to cabin overheat protection since last charge | 36\|14 | little-endian | unsigned | 0.01 | 0 | kWh | 0 to 163.83 |  | validated |
| `VCFRONT_mobileAppEnergyLossSinceCharge` | page 3 | Energy loss due to mobile app interaction since last charge | 50\|14 | little-endian | unsigned | 0.01 | 0 | kWh | 0 to 163.83 |  | validated |
| `VCFRONT_summonStandbyEnergyLossSinceCharge` | page 4 | Energy loss due to summon standby since last charge | 8\|14 | little-endian | unsigned | 0.01 | 0 | kWh | 0 to 163.83 |  | validated |
| `VCFRONT_sentryModeEnergyLossSinceCharge` | page 4 | Energy loss due to sentry mode since last charge | 22\|14 | little-endian | unsigned | 0.01 | 0 | kWh | 0 to 163.83 |  | validated |
| `VCFRONT_backgroundEnergyLossSinceCharge` | page 4 | Energy loss due to background vehicle op since last charge | 36\|14 | little-endian | unsigned | 0.01 | 0 | kWh | 0 to 163.83 |  | validated |
| `VCFRONT_evapDryingEnergyLossSinceCharge` | page 4 | Energy loss due to evap drying since last charge | 50\|14 | little-endian | unsigned | 0.01 | 0 | kWh | 0 to 163.83 |  | validated |

## Multiplexing

`VCFRONT_energyLossIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (4 signals), page 2 (4 signals), page 3 (4 signals), page 4 (4 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
