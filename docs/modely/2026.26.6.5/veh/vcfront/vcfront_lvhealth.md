---
layout: default
title: "VCFRONT_LVHealth (0x474) — Front body controller, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Front body controller message: LV health. Tesla Model Y CAN bus message VCFRONT_LVHealth (0x474) of Front body controller, firmware 2026.26.6.5, 7 signals (VCFRONT_LVHealthChecksum, VCFRONT_LVHealthCounter, VCFRONT_LVHealthStatus, VCFRONT_LVStatusForDrive and 3 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_LVHealth (0x474) — Front body controller, Tesla Model Y 2026.26.6.5 VEH CAN

Front body controller message: LV health; frame length from the layout, not yet observed on a vehicle bus. This page documents the 7 signals of VCFRONT_LVHealth as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_LVHealth` |
| CAN id | 0x474 (1140) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT |
| Frame length | 5 bytes |
| Cycle time | 100 ms |
| Signals | 7 |

## Signals of VCFRONT_LVHealth

Tesla Model Y CAN bus signals in `VCFRONT_LVHealth`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_LVHealthChecksum` | Front body controller: LV health checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCFRONT_LVHealthCounter` | Front body controller: LV health counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `VCFRONT_LVHealthStatus` | Health status of the LV system | 12\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOMAIN_HEALTHY`<br>1 = `HEALTHY_LIMITED`<br>2 = `LATENT_FAULT`<br>3 = `BACKUP_COMPROMISED`<br>4 = `ENERGY_RESERVE_COMPROMISED`<br>5 = `ENERGY_RESERVE_CRITICAL`<br>6 = `POWER_SUPPLY_COMPROMISED` | validated |
| `VCFRONT_LVStatusForDrive` | Front body controller: LV status for drive | 15\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STATUS_FOR_DRIVE_NOT_READY`<br>1 = `STATUS_FOR_DRIVE_READY`<br>2 = `STATUS_FOR_DRIVE_READY_LIMITED`<br>3 = `STATUS_FOR_DRIVE_RETURN_TO_SERVICE`<br>4 = `STATUS_FOR_DRIVE_LIMP`<br>5 = `STATUS_FOR_DRIVE_PULL_TO_SHOULDER`<br>6 = `STATUS_FOR_DRIVE_ACTIVE_DECEL` | validated |
| `VCFRONT_LVPowerSecondsToSafeHarbor` | Reports the amount of time (in seconds) the Low Voltage (LV) power system indicates the vehicle has to achieve safe harbor. | 18\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 | 65535 = `INDEFINITE` | validated |
| `VCFRONT_hardwareProtectionsArmed` | Front body controller: hardware protections armed | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_lockoutStrategy` | Front body controller: lockout strategy | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `POWER_STATE`<br>1 = `PARK_STATUS` | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
