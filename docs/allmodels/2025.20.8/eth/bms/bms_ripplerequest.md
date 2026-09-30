---
layout: default
title: "BMS_rippleRequest (0x2A2) — High-voltage battery management system, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "High-voltage battery management system message: ripple request. Ethernet-side message BMS_rippleRequest of High-voltage battery management system for Tesla Model 3 / Model Y firmware 2025.20.8, 6 signals (BMS_acRippleCurrentAmplitudeLimit, BMS_acRippleMaxVoltageLimit, BMS_acRippleMinVoltageLimit, BMS_acRippleFrequencyRequest and 2 more). Bit layout, scaling, units and value tables."
---

# BMS_rippleRequest (0x2A2) — High-voltage battery management system, Tesla Model 3 / Model Y 2025.20.8 ETH

High-voltage battery management system message: ripple request. This page documents the 6 signals of BMS_rippleRequest as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_rippleRequest` |
| Ethernet-side id | 0x2A2 (674) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | BMS |
| Frame length | 7 bytes |
| Cycle time | 100 ms |
| Signals | 6 |

## Signals of BMS_rippleRequest

Tesla Model 3 / Model Y CAN bus signals in `BMS_rippleRequest`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_acRippleCurrentAmplitudeLimit` | Transmits the Battery Management System (BMS) AC ripple current amplitude limit to the Electric Vehicle Supply Equipment (EVSE). | 0\|9 | little-endian | unsigned | 1 | 0 | A | 0 to 511 |  | plausible |
| `BMS_acRippleMaxVoltageLimit` | Reports the maximum voltage limit when the Electric Vehicle Supply Equipment (EVSE) is performing the AC ripple. | 9\|9 | little-endian | unsigned | 1 | 0 | V | 0 to 511 |  | plausible |
| `BMS_acRippleMinVoltageLimit` | Reports the minimum voltage limit when the Electric Vehicle Supply Equipment (EVSE) is performing the AC ripple. | 18\|9 | little-endian | unsigned | 1 | 0 | V | 0 to 511 |  | plausible |
| `BMS_acRippleFrequencyRequest` | Transmits the Battery Management System (BMS) AC ripple frequency request to the Electric Vehicle Supply Equipment (EVSE); raw 63 = signal not available (SNA) | 32\|6 | little-endian | unsigned | 1 | 80 | Hz | 80 to 142 | 63 = `SNA` | plausible |
| `BMS_acRippleCurrentAmplitudeRequest` | Transmits the Battery Management System (BMS) AC ripple current amplitude request to the Electric Vehicle Supply Equipment (EVSE). | 38\|9 | little-endian | unsigned | 1 | 0 | A | 0 to 511 |  | plausible |
| `BMS_acRippleRequest` | High-voltage battery management system: ac ripple request | 48\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `RIPPLE_NOT_SUPPORTED`<br>1 = `RIPPLE_OFF`<br>2 = `RIPPLE_STANDBY`<br>3 = `RIPPLE_ON`<br>4 = `RIPPLE_FAULTED` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
