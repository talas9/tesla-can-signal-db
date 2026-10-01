---
layout: default
title: "IBST_status (0x39D) — Electric brake booster, Tesla Model 3 / Model Y 2026.26.6.5 PARTY CAN"
description: "Electric brake booster message: status. Tesla Model 3 / Model Y CAN bus message IBST_status (0x39D) of Electric brake booster, firmware 2026.26.6.5, 7 signals (IBST_statusChecksum, IBST_statusCounter, IBST_iBoosterStatus, IBST_driverBrakeApply and 3 more). Bit layout, scaling, units and value tables."
---

# IBST_status (0x39D) — Electric brake booster, Tesla Model 3 / Model Y 2026.26.6.5 PARTY CAN

Electric brake booster message: status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 7 signals of IBST_status as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `IBST_status` |
| CAN id | 0x39D (925) |
| ECU | [Electric brake booster](../../ibst.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | IBST |
| Frame length | 5 bytes |
| Cycle time | 40 ms |
| Signals | 7 |

## Signals of IBST_status

Tesla Model 3 / Model Y CAN bus signals in `IBST_status`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `IBST_statusChecksum` | Electric brake booster: status checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `IBST_statusCounter` | Electric brake booster: status counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `IBST_iBoosterStatus` | Indication of iBooster functional state | 12\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `IBOOSTER_OFF`<br>1 = `IBOOSTER_INIT`<br>2 = `IBOOSTER_FAILURE`<br>3 = `IBOOSTER_DIAGNOSTIC`<br>4 = `IBOOSTER_ACTIVE_GOOD_CHECK`<br>5 = `IBOOSTER_READY`<br>6 = `IBOOSTER_ACTUATION` | plausible |
| `IBST_driverBrakeApply` | Indicates when the driver applies the brake pedal. | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_INIT_OR_OFF`<br>1 = `BRAKES_NOT_APPLIED`<br>2 = `DRIVER_APPLYING_BRAKES`<br>3 = `FAULT` | plausible |
| `IBST_internalState` | Indication of iBooster internal state | 18\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NO_MODE_ACTIVE`<br>1 = `PRE_DRIVE_CHECK`<br>2 = `LOCAL_BRAKE_REQUEST`<br>3 = `EXTERNAL_BRAKE_REQUEST`<br>4 = `DIAGNOSTIC`<br>5 = `TRANSITION_TO_IDLE`<br>6 = `POST_DRIVE_CHECK` | plausible |
| `IBST_sInputRodDriver` | IBST estimated input rod stroke | 21\|12 | little-endian | unsigned | 0.015625 | -5 | mm | -5 to 47 |  | plausible |
| `IBST_LVPowerModeState` | Electric brake booster: LV power mode state | 35\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PEAK_POWER_REDUCTION_NOT_SUPPORTED`<br>1 = `PEAK_POWER_REDUCTION_AVAILABLE`<br>2 = `PEAK_POWER_REDUCTION_ACTIVE_MAX600W_NOMINAL350W`<br>3 = `PEAK_POWER_REDUCTION_RESERVED` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 PARTY DBC file](../../../../../dbc/AllModels/2026.26.6.5/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/PARTY.json)

## See also

- [All Electric brake booster messages (IBST)](../../ibst.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
