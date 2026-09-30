---
layout: default
title: "VCFRONT_LVHealth (0x7E1) — Front body controller, Tesla Model 3 2025.20.8 ETH"
description: "Front body controller message: LV health. Ethernet-side message VCFRONT_LVHealth of Front body controller for Tesla Model 3 firmware 2025.20.8, 5 signals (VCFRONT_LVHealthStatus, VCFRONT_LVStatusForDrive, VCFRONT_LVPowerSecondsToSafeHarbor, VCFRONT_LVHealthCounter and 1 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_LVHealth (0x7E1) — Front body controller, Tesla Model 3 2025.20.8 ETH

Front body controller message: LV health. This page documents the 5 signals of VCFRONT_LVHealth as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_LVHealth` |
| Ethernet-side id | 0x7E1 (2017) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCFRONT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 5 |

## Signals of VCFRONT_LVHealth

Tesla Model 3 CAN bus signals in `VCFRONT_LVHealth`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_LVHealthStatus` | Health status of the LV system | 5\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DOMAIN_HEALTHY`<br>1 = `HEALTHY_LIMITED`<br>2 = `LATENT_FAULT`<br>3 = `BACKUP_COMPROMISED` | plausible |
| `VCFRONT_LVStatusForDrive` | Front body controller: LV status for drive | 9\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STATUS_FOR_DRIVE_NOT_READY`<br>1 = `STATUS_FOR_DRIVE_READY`<br>2 = `STATUS_FOR_DRIVE_READY_LIMITED`<br>3 = `STATUS_FOR_DRIVE_RETURN_TO_SERVICE`<br>4 = `STATUS_FOR_DRIVE_LIMP`<br>5 = `STATUS_FOR_DRIVE_PULL_TO_SHOULDER`<br>6 = `STATUS_FOR_DRIVE_ACTIVE_DECEL` | plausible |
| `VCFRONT_LVPowerSecondsToSafeHarbor` | Reports the amount of time (in seconds) the Low Voltage (LV) power system indicates the vehicle has to achieve safe harbor. | 13\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 | 65535 = `INDEFINITE` | plausible |
| `VCFRONT_LVHealthCounter` | Front body controller: LV health counter | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `VCFRONT_LVHealthChecksum` | Front body controller: LV health checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
