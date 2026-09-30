---
layout: default
title: "PTC_feedbackStatus (0x207) — Cabin heater, Tesla Model Y 2025.20.8 ETH"
description: "Cabin heater message: feedback status. Ethernet-side message PTC_feedbackStatus of Cabin heater for Tesla Model Y firmware 2025.20.8, 14 signals (PTC_leftFlagFault, PTC_rightFlagFault, PTC_leftPowerDerating, PTC_rightPowerDerating and 10 more). Bit layout, scaling, units and value tables."
---

# PTC_feedbackStatus (0x207) — Cabin heater, Tesla Model Y 2025.20.8 ETH

Cabin heater message: feedback status. This page documents the 14 signals of PTC_feedbackStatus as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `PTC_feedbackStatus` |
| Ethernet-side id | 0x207 (519) |
| ECU | [Cabin heater](../../ptc.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | PTC |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 14 |

## Signals of PTC_feedbackStatus

Tesla Model Y CAN bus signals in `PTC_feedbackStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PTC_leftFlagFault` | Heater left bank fault indication flag | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PTC_rightFlagFault` | Heater right bank fault indication flag | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PTC_leftPowerDerating` | Heater left bank power derating state | 2\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_DERATED`<br>1 = `OVERTEMPERATURE_PCB`<br>2 = `OVERTEMPERATURE_IGBT`<br>3 = `OVERTEMPERATURE_CORE` | validated |
| `PTC_rightPowerDerating` | Heater right bank power derating state | 4\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_DERATED`<br>1 = `OVERTEMPERATURE_PCB`<br>2 = `OVERTEMPERATURE_IGBT`<br>3 = `OVERTEMPERATURE_CORE` | validated |
| `PTC_ocpEvent` | Indication that an over current protection event has occurred | 6\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NO_OCP_EVENT`<br>1 = `OCP_EVENT_LEFT_SIDE`<br>2 = `OCP_EVENT_RIGHT_SIDE` | validated |
| `PTC_leftDutyFeedback` | Current PWM duty cycle applied to left side of PTC heater | 8\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `PTC_rightDutyFeedback` | Current PWM duty cycle applied to right side of PTC heater | 16\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `PTC_leftPowerHV` | Heater left bank power | 24\|8 | little-endian | unsigned | 30 | 0 | W | 0 to 7650 |  | validated |
| `PTC_rightPowerHV` | Heater right bank power | 32\|8 | little-endian | unsigned | 30 | 0 | W | 0 to 7650 |  | validated |
| `PTC_leftTempEstOutlet` | Cabin heater: left temp est outlet | 40\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 200 |  | validated |
| `PTC_rightTempEstOutlet` | Cabin heater: right temp est outlet | 48\|8 | little-endian | unsigned | 1 | -40 | degC | -40 to 200 |  | validated |
| `PTC_tliErrorCount` | Heater top level interrupt error count | 56\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `PTC_tliEvent` | Indicator of heater top level interrupt event | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `PTC_tliSource` | Heater top level interrupt event source | 61\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NO_ERROR`<br>1 = `IGBT_DRIVER`<br>2 = `12_VOLTS`<br>3 = `OCP`<br>4 = `HV_OVER_VOLTAGE` | validated |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Cabin heater messages (PTC)](../../ptc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
