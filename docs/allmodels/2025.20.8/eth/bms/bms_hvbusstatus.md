---
layout: default
title: "BMS_hvBusStatus (0x132) — High-voltage battery management system, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "High-voltage battery management system message: hv bus status. Ethernet-side message BMS_hvBusStatus of High-voltage battery management system for Tesla Model 3 / Model Y firmware 2025.20.8, 4 signals (BMS_packVoltage, BMS_packCurrent, BMS_currentUnfiltered, BMS_chgTimeToFull). Bit layout, scaling, units and value tables."
---

# BMS_hvBusStatus (0x132) — High-voltage battery management system, Tesla Model 3 / Model Y 2025.20.8 ETH

High-voltage battery management system message: hv bus status. This page documents the 4 signals of BMS_hvBusStatus as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_hvBusStatus` |
| Ethernet-side id | 0x132 (306) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 10 ms |
| Signals | 4 |

## Signals of BMS_hvBusStatus

Tesla Model 3 / Model Y CAN bus signals in `BMS_hvBusStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_packVoltage` | Measures voltage on the battery side of the High Voltage (HV) contactors. | 0\|16 | little-endian | unsigned | 0.01 | 0 | V | 0 to 655.35 |  | plausible |
| `BMS_packCurrent` | Current measured at the HV contactors of the HV battery; raw 32768 = signal not available (SNA) | 16\|16 | little-endian | signed | 0.1 | 0 | A | -3276.7 to 3276.7 | -32768 = `SNA` | validated |
| `BMS_currentUnfiltered` | Pack current with no filters applied; raw 32768 = signal not available (SNA) | 32\|16 | little-endian | signed | 0.05 | -822 | A | -2460.3 to 816.3 | -32768 = `SNA` | plausible |
| `BMS_chgTimeToFull` | Estimated time remaining until charge termination percent will be reached; raw 4095 = signal not available (SNA) | 48\|12 | little-endian | unsigned | 0.01666667 | 0 | Hours | 0 to 68.23334698 | 4095 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
