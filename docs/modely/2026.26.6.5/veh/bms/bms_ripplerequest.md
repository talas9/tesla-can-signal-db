---
layout: default
title: "BMS_rippleRequest (0x2A2) — High-voltage battery management system, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "High-voltage battery management system message: ripple request. Tesla Model Y CAN bus message BMS_rippleRequest (0x2A2) of High-voltage battery management system, firmware 2026.26.6.5, 6 signals (BMS_acRippleCurrentAmplitudeLimit, BMS_acRippleMaxVoltageLimit, BMS_acRippleMinVoltageLimit, BMS_acRippleFrequencyRequest and 2 more). Bit layout, scaling, units and value tables."
---

# BMS_rippleRequest (0x2A2) — High-voltage battery management system, Tesla Model Y 2026.26.6.5 VEH CAN

High-voltage battery management system message: ripple request; frame length from the layout, not yet observed on a vehicle bus. This page documents the 6 signals of BMS_rippleRequest as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_rippleRequest` |
| CAN id | 0x2A2 (674) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | BMS |
| Frame length | 7 bytes |
| Cycle time | 1000 ms |
| Signals | 6 |

## Signals of BMS_rippleRequest

Tesla Model Y CAN bus signals in `BMS_rippleRequest`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_acRippleCurrentAmplitudeLimit` | Transmits the Battery Management System (BMS) AC ripple current amplitude limit to the Electric Vehicle Supply Equipment (EVSE). | 0\|10 | little-endian | unsigned | 1 | 0 | A | 0 to 1023 |  | validated |
| `BMS_acRippleMaxVoltageLimit` | Reports the maximum voltage limit when the Electric Vehicle Supply Equipment (EVSE) is performing the AC ripple. | 10\|10 | little-endian | unsigned | 1 | 0 | V | 0 to 1023 |  | validated |
| `BMS_acRippleMinVoltageLimit` | Reports the minimum voltage limit when the Electric Vehicle Supply Equipment (EVSE) is performing the AC ripple. | 20\|10 | little-endian | unsigned | 1 | 0 | V | 0 to 1023 |  | validated |
| `BMS_acRippleFrequencyRequest` | Transmits the Battery Management System (BMS) AC ripple frequency request to the Electric Vehicle Supply Equipment (EVSE); raw 1023 = signal not available (SNA) | 30\|10 | little-endian | unsigned | 1 | 0 | Hz | 0 to 1022 | 1023 = `SNA` | validated |
| `BMS_acRippleCurrentAmplitudeRequest` | Transmits the Battery Management System (BMS) AC ripple current amplitude request to the Electric Vehicle Supply Equipment (EVSE). | 40\|10 | little-endian | unsigned | 1 | 0 | A | 0 to 1023 |  | validated |
| `BMS_acRippleRequest` | High-voltage battery management system: ac ripple request | 50\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `RIPPLE_NOT_SUPPORTED`<br>1 = `RIPPLE_OFF`<br>2 = `RIPPLE_STANDBY`<br>3 = `RIPPLE_ON`<br>4 = `RIPPLE_FAULTED` | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
