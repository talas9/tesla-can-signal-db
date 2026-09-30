---
layout: default
title: "UI_chargeRequest (0x333) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Touchscreen user interface computer message: charge request. Ethernet-side message UI_chargeRequest of Touchscreen user interface computer for Tesla Model 3 / Model Y firmware 2025.20.8, 18 signals (UI_openChargePortDoorRequest, UI_closeChargePortDoorRequest, UI_chargeEnableRequest, UI_brickVLoggingRequest and 14 more). Bit layout, scaling, units and value tables."
---

# UI_chargeRequest (0x333) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 ETH

Touchscreen user interface computer message: charge request. This page documents the 18 signals of UI_chargeRequest as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_chargeRequest` |
| Ethernet-side id | 0x333 (819) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 5 bytes |
| Cycle time | 500 ms |
| Signals | 18 |

## Signals of UI_chargeRequest

Tesla Model 3 / Model Y CAN bus signals in `UI_chargeRequest`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_openChargePortDoorRequest` | Request to open charge port. | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_closeChargePortDoorRequest` | Request to close charge port. | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_chargeEnableRequest` | Charging request initiated | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_brickVLoggingRequest` | Touchscreen user interface computer: brick v logging request | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FALSE`<br>1 = `TRUE` | plausible |
| `UI_brickBalancingDisabled` | Touchscreen user interface computer: brick balancing disabled | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FALSE`<br>1 = `TRUE` | plausible |
| `UI_dSocAlertThreshold` | Touchscreen user interface computer: d soc alert threshold | 5\|3 | little-endian | unsigned | 0.5 | -4 | % | -4 to -0.5 |  | plausible |
| `UI_acChargeCurrentLimit` | UI charging line current request; raw 127 = signal not available (SNA) | 8\|7 | little-endian | unsigned | 1 | 0 | A | 0 to 126 | 127 = `SNA` | validated |
| `UI_dSocAlertEnable` | Set when the BMS_a117_SW_Delta_SOC_Weak_Short alert for the BMS should have a functional response | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_chargeTerminationPct` | Charge Termination Limit Percent | 16\|10 | little-endian | unsigned | 0.1 | 0 | % | 5 to 100 |  | validated |
| `UI_chargeFeature1` | Touchscreen user interface computer: charge feature1 | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_chargeFeature2` | Touchscreen user interface computer: charge feature2 | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_chargeFeature3` | Touchscreen user interface computer: charge feature3 | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_scheduledDepartureEnabled` | Reports scheduled departure feature enablement. | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `UI_chargePortLatchRequest` | Request to engage or disengage the latch. | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UI_LATCH_REQUEST_NONE`<br>1 = `UI_LATCH_REQUEST_ENGAGE`<br>2 = `UI_LATCH_REQUEST_DISENGAGE` | validated |
| `UI_socSnapshotExpirationTime` | Touchscreen user interface computer: soc snapshot expiration time | 32\|4 | little-endian | unsigned | 2 | 2 | weeks | 2 to 32 |  | plausible |
| `UI_cpInletHeaterRequest` | Enable charge port inlet heater | 36\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HEATER_OFF`<br>1 = `HEATER_AUTO`<br>2 = `HEATER_MANUAL_OVERRIDE` | validated |
| `UI_chargePowerSampleRequest` | Touchscreen user interface computer: charge power sample request | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_enableIso15118` | Touchscreen user interface computer: enable iso15118 | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
