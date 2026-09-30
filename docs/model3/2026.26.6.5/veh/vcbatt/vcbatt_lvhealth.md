---
layout: default
title: "VCBATT_LVHealth (0x3B1) — VCBATT ECU, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "VCBATT ECU message: LV health. Tesla Model 3 CAN bus message VCBATT_LVHealth (0x3B1) of VCBATT ECU, firmware 2026.26.6.5, 8 signals (VCBATT_LVHealthChecksum, VCBATT_LVHealthCounter, VCBATT_LVHealthStatus, VCBATT_LVStatusForDrive and 4 more). Bit layout, scaling, units and value tables."
---

# VCBATT_LVHealth (0x3B1) — VCBATT ECU, Tesla Model 3 2026.26.6.5 VEH CAN

VCBATT ECU message: LV health; frame length from the layout, not yet observed on a vehicle bus. This page documents the 8 signals of VCBATT_LVHealth as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCBATT_LVHealth` |
| CAN id | 0x3B1 (945) |
| ECU | [VCBATT ECU](../../vcbatt.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCBATT |
| Frame length | 5 bytes |
| Cycle time | 100 ms |
| Signals | 8 |

## Signals of VCBATT_LVHealth

Tesla Model 3 CAN bus signals in `VCBATT_LVHealth`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCBATT_LVHealthChecksum` | VCBATT ECU: LV health checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCBATT_LVHealthCounter` | VCBATT ECU: LV health counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `VCBATT_LVHealthStatus` | Health status of the LV system | 12\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DOMAIN_HEALTHY`<br>1 = `HEALTHY_LIMITED`<br>2 = `LATENT_FAULT`<br>3 = `BACKUP_COMPROMISED`<br>4 = `ENERGY_RESERVE_COMPROMISED`<br>5 = `ENERGY_RESERVE_CRITICAL`<br>6 = `POWER_SUPPLY_COMPROMISED` | validated |
| `VCBATT_LVStatusForDrive` | Status for drive based on health status of the LV system | 15\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STATUS_FOR_DRIVE_NOT_READY`<br>1 = `STATUS_FOR_DRIVE_READY`<br>2 = `STATUS_FOR_DRIVE_READY_LIMITED`<br>3 = `STATUS_FOR_DRIVE_RETURN_TO_SERVICE`<br>4 = `STATUS_FOR_DRIVE_LIMP`<br>5 = `STATUS_FOR_DRIVE_PULL_TO_SHOULDER`<br>6 = `STATUS_FOR_DRIVE_ACTIVE_DECEL` | validated |
| `VCBATT_LVPowerSecondsToSafeHarbor` | Reports the amount of time (in seconds) the Low Voltage (LV) power system indicates the vehicle has to achieve safe harbor. | 18\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 | 65535 = `INDEFINITE` | validated |
| `VCBATT_autonomyBehavior` | Current autonomy mode and expected vehicle behaviors. | 34\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DRIVER`<br>1 = `DRIVERLESS_TAKEOVER`<br>2 = `DRIVERLESS_NO_TAKEOVER` | validated |
| `VCBATT_hardwareProtectionsArmed` | Hardware protections armed | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCBATT_12vStatusForDrive` | VCBATT ECU: 12v status for drive | 38\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_READY_FOR_DRIVE_12V`<br>1 = `READY_FOR_DRIVE_12V`<br>2 = `EXIT_DRIVE_REQUESTED_12V` | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All VCBATT ECU messages (VCBATT)](../../vcbatt.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
