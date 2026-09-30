---
layout: default
title: "DI_autonomyHealth (0x54) — Drive inverter, Tesla Model 3 2026.26.6.5 PARTY CAN"
description: "Drive inverter message: autonomy health. Tesla Model 3 CAN bus message DI_autonomyHealth (0x54) of Drive inverter, firmware 2026.26.6.5, 15 signals (DI_ah_vehicleSpeedLimit, DI_ah_vehicleReverseSpeedLimit, DI_autonomyBehavior, DI_ah_vehicleNoGradeAccelMax and 11 more). Bit layout, scaling, units and value tables."
---

# DI_autonomyHealth (0x54) — Drive inverter, Tesla Model 3 2026.26.6.5 PARTY CAN

Drive inverter message: autonomy health; frame length from the layout, not yet observed on a vehicle bus. This page documents the 15 signals of DI_autonomyHealth as defined for Tesla Model 3 firmware 2026.26.6.5 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DI_autonomyHealth` |
| CAN id | 0x54 (84) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | DI |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 15 |

## Signals of DI_autonomyHealth

Tesla Model 3 CAN bus signals in `DI_autonomyHealth`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_ah_vehicleSpeedLimit` | Drive inverter: ah vehicle speed limit | 0\|9 | little-endian | unsigned | 1 | 0 | kph | 0 to 300 |  | validated |
| `DI_ah_vehicleReverseSpeedLimit` | Drive inverter: ah vehicle reverse speed limit | 9\|5 | little-endian | unsigned | 1 | 0 | kph | 0 to 31 |  | validated |
| `DI_autonomyBehavior` | Drive inverter: autonomy behavior | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DRIVER`<br>1 = `DRIVERLESS_TAKEOVER`<br>2 = `DRIVERLESS_NO_TAKEOVER` | validated |
| `DI_ah_vehicleNoGradeAccelMax` | Drive inverter: ah vehicle no grade accel max | 16\|8 | little-endian | unsigned | 0.04 | 0 | m/s^2 | 0 to 10 |  | validated |
| `DI_ah_vehicleNoGradeDecelMax` | Drive inverter: ah vehicle no grade decel max | 24\|9 | little-endian | unsigned | 0.04 | 0 | m/s^2 | 0 to 15 |  | validated |
| `DI_ah_timeToNoPropulsion` | Drive inverter: ah time to no propulsion | 33\|12 | little-endian | unsigned | 1 | 0 | s | 0 to 4094 | 4095 = `INDEFINITE` | validated |
| `DI_ah_dGearAvailable` | Drive inverter: ah d gear available | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_ah_rGearAvailable` | Drive inverter: ah r gear available | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_ah_pGearAvailable` | Drive inverter: ah p gear available | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_loncDegradedAvailable` | Drive inverter: lonc degraded available | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_loncSuppressCancelModeAvailable` | Drive inverter: lonc suppress cancel mode available | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_loncDegradedReason` | Drive inverter: lonc degraded reason | 50\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `DI_LONC_DEGRADED_NONE`<br>1 = `DI_LONC_DEGRADED_VHLD_FAULTED`<br>2 = `DI_LONC_DEGRADED_VHLD_UNAVAILABLE`<br>3 = `DI_LONC_DEGRADED_TC_FAULT`<br>4 = `DI_LONC_DEGRADED_VDC_FAULT`<br>5 = `DI_LONC_DEGRADED_EBR`<br>6 = `DI_LONC_DEGRADED_VELOCITY_ESTIMATE_NOT_NORMAL`<br>7 = `DI_LONC_DEGRADED_BRAKE_INVALID`<br>8 = `DI_LONC_DEGRADED_ESP_MIA`<br>9 = `DI_LONC_DEGRADED_ABS_UNAVAILABLE`<br>10 = `DI_LONC_DEGRADED_REDUNDANT_BRAKES_ACTIVE` | validated |
| `DI_opdAvailableForPedalInterface` | Drive inverter: opd available for pedal interface | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_epbUnavailable` | Drive inverter: epb unavailable | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_loncInPreFaultStopping` | Drive inverter: lonc in pre fault stopping | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 PARTY DBC file](../../../../../dbc/Model3/2026.26.6.5/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/PARTY.json)

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
