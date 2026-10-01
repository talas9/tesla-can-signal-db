---
layout: default
title: "BMS_energyStatus (0x352) — High-voltage battery management system, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "High-voltage battery management system message: energy status. Tesla Model Y CAN bus message BMS_energyStatus (0x352) of High-voltage battery management system, firmware 2026.26.6.5, 12 signals (BMS_energyStatusMultiplexer, BMS_nominalFullPackEnergy, BMS_nominalEnergyRemaining, BMS_idealEnergyRemaining and 8 more). Bit layout, scaling, units and value tables."
---

# BMS_energyStatus (0x352) — High-voltage battery management system, Tesla Model Y 2026.26.6.5 VEH CAN

High-voltage battery management system message: energy status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 12 signals of BMS_energyStatus as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_energyStatus` |
| CAN id | 0x352 (850) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 2000 ms |
| Signals | 12 |

## Signals of BMS_energyStatus

Tesla Model Y CAN bus signals in `BMS_energyStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_energyStatusMultiplexer` | selector | High-voltage battery management system: energy status multiplexer | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `Mux0`<br>1 = `Mux1`<br>2 = `Mux2` | validated |
| `BMS_nominalFullPackEnergy` | page 0 | Full pack energy based on calculated pack energy from the full pack discharge energy walk; raw 65535 = signal not available (SNA) | 16\|16 | little-endian | unsigned | 0.02 | 0 | kWh | 0 to 1310.68 | 65535 = `SNA` | validated |
| `BMS_nominalEnergyRemaining` | page 0 | Nominal energy remaining based on calculated pack energy from the nominal discharge energy walk; raw 65535 = signal not available (SNA) | 32\|16 | little-endian | unsigned | 0.02 | 0 | kWh | 0 to 1310.68 | 65535 = `SNA` | validated |
| `BMS_idealEnergyRemaining` | page 0 | Ideal energy remaining based on calculated pack energy from ideal discharge energy walk; raw 65535 = signal not available (SNA) | 48\|16 | little-endian | unsigned | 0.02 | 0 | kWh | 0 to 1310.68 | 65535 = `SNA` | plausible |
| `BMS_fullChargeComplete` | page 1 | Indicates BMS is fully charged | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `BMS_energyBuffer` | page 1 | Rough indication of confidence in the energy estimation; raw 65535 = signal not available (SNA) | 16\|16 | little-endian | unsigned | 0.01 | 0 | kWh | 0 to 655.34 | 65535 = `SNA` | plausible |
| `BMS_expectedEnergyRemaining` | page 1 | High-voltage battery management system: expected energy remaining; raw 65535 = signal not available (SNA) | 32\|16 | little-endian | unsigned | 0.02 | 0 | kWh | 0 to 1310.68 | 65535 = `SNA` | plausible |
| `BMS_energyToChargeComplete` | page 1 | Calculated energy required to reach charge complete; raw 65535 = signal not available (SNA) | 48\|16 | little-endian | unsigned | 0.02 | 0 | kWh | 0 to 1310.68 | 65535 = `SNA` | validated |
| `BMS_energyRemainingDisplay` | page 2 | Rubber-banding energy remaining to be used for the UI facing miles remaining display; raw 65535 = signal not available (SNA) | 8\|16 | little-endian | unsigned | 0.02 | 0 | kWh | 0 to 1310.68 | 65535 = `SNA` | validated |
| `BMS_energyRemainingTDisplay` | page 2 | Rubber-banding energy remaining to be used for the UI facing miles remaining display; raw 65535 = signal not available (SNA) | 24\|16 | little-endian | unsigned | 0.02 | 0 | kWh | 0 to 1310.68 | 65535 = `SNA` | validated |
| `BMS_energyDisplayErrorBlendRate` | page 2 | Rubber-banding blend rate to be used to ensure consistency between the gauge display and UI energy algorithms | 40\|12 | little-endian | unsigned | 0.0156288165599 | 0 | % | 0 to 64 |  | validated |
| `BMS_userFacingSoe` | page 2 | User facing state of energy; raw 2047 = signal not available (SNA) | 52\|11 | little-endian | unsigned | 0.05 | 0 | % | 0 to 100 | 2047 = `SNA` | validated |

## Multiplexing

`BMS_energyStatusMultiplexer` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (3 signals), page 1 (4 signals), page 2 (4 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
