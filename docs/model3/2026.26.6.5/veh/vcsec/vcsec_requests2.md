---
layout: default
title: "VCSEC_requests2 (0x119) — Vehicle security controller, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Vehicle security controller message: requests2. Tesla Model 3 CAN bus message VCSEC_requests2 (0x119) of Vehicle security controller, firmware 2026.26.6.5, 9 signals (VCSEC_activeImmobilizerAuthLevel, VCSEC_smartTrunkLightRequest, VCSEC_smartTrunkSoundRequest, VCSEC_hvacRunScreenProtectOnly and 5 more). Bit layout, scaling, units and value tables."
---

# VCSEC_requests2 (0x119) — Vehicle security controller, Tesla Model 3 2026.26.6.5 VEH CAN

Vehicle security controller message: requests2; frame length from the layout, not yet observed on a vehicle bus. This page documents the 9 signals of VCSEC_requests2 as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEC_requests2` |
| CAN id | 0x119 (281) |
| ECU | [Vehicle security controller](../../vcsec.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCSEC |
| Frame length | 4 bytes |
| Cycle time | 100 ms |
| Signals | 9 |

## Signals of VCSEC_requests2

Tesla Model 3 CAN bus signals in `VCSEC_requests2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEC_activeImmobilizerAuthLevel` | The level of auth VCSEC will respond with when the Drive Inverter asks for auth | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `IMMOBILIZER_AUTH_LEVEL_NONE`<br>1 = `IMMOBILIZER_AUTH_LEVEL_USER_DRIVE`<br>2 = `IMMOBILIZER_AUTH_LEVEL_AUTONOMY`<br>3 = `IMMOBILIZER_AUTH_LEVEL_MANUAL_RECOVERY` | validated |
| `VCSEC_smartTrunkLightRequest` | Request to signal indication lights for the smart trunk feature | 2\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VCSEC_LIGHT_REQUEST_TYPE_NONE`<br>1 = `VCSEC_LIGHT_REQUEST_TYPE_ON`<br>2 = `VCSEC_LIGHT_REQUEST_TYPE_BLINK`<br>3 = `VCSEC_LIGHT_REQUEST_TYPE_DIM` | validated |
| `VCSEC_smartTrunkSoundRequest` | Vehicle security controller: smart trunk sound request | 4\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VCSEC_SOUND_REQUEST_TYPE_NONE`<br>1 = `VCSEC_SOUND_REQUEST_TYPE_VICINITY`<br>2 = `VCSEC_SOUND_REQUEST_TYPE_NEAR` | validated |
| `VCSEC_hvacRunScreenProtectOnly` | Vehicle security controller: hvac run screen protect only | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_chargeHandleRequestModel` | Vehicle security controller: charge handle request model | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `VCSEC_CHARGE_HANDLE_MODEL_UNKNOWN`<br>2 = `VCSEC_CHARGE_HANDLE_MODEL_WC3_NACS`<br>3 = `VCSEC_CHARGE_HANDLE_MODEL_UMC3_NACS`<br>4 = `VCSEC_CHARGE_HANDLE_MODEL_UMC3_GB`<br>5 = `VCSEC_CHARGE_HANDLE_MODEL_UMC3_TYPE_2`<br>6 = `VCSEC_CHARGE_HANDLE_MODEL_WC3_TYPE2`<br>7 = `VCSEC_CHARGE_HANDLE_MODEL_SC_NACS`<br>8 = `VCSEC_CHARGE_HANDLE_MODEL_SC_CCS2` | validated |
| `VCSEC_recoveryModeRequested` | Vehicle security controller: recovery mode requested | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_infotainmentResetRequested` | Vehicle security controller: infotainment reset requested | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_mobileToAPRequest` | Vehicle security controller: mobile to AP request | 23\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `VCSEC_MOBILE_TO_AP_REQUEST_NONE`<br>1 = `VCSEC_MOBILE_TO_AP_REQUEST_EMERGENCY_PULL_OVER`<br>2 = `VCSEC_MOBILE_TO_AP_REQUEST_DISENGAGE_AUTONOMY`<br>4 = `VCSEC_MOBILE_TO_AP_REQUEST_MAX` | validated |
| `VCSEC_riderKeyPresent` | Vehicle security controller: rider key present | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Vehicle security controller messages (VCSEC)](../../vcsec.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
