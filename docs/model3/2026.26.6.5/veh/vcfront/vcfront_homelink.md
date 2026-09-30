---
layout: default
title: "VCFRONT_homelink (0x549) — Front body controller, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Front body controller message: homelink. Tesla Model 3 CAN bus message VCFRONT_homelink (0x549) of Front body controller, firmware 2026.26.6.5, 6 signals (VCFRONT_homelinkV2Response0, VCFRONT_homelinkV2Response1, VCFRONT_homelinkV2Response2, VCFRONT_homelinkV2Response3 and 2 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_homelink (0x549) — Front body controller, Tesla Model 3 2026.26.6.5 VEH CAN

Front body controller message: homelink; frame length observed on a vehicle bus. This page documents the 6 signals of VCFRONT_homelink as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_homelink` |
| CAN id | 0x549 (1353) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT |
| Frame length | 6 bytes |
| Cycle time | 10000 ms |
| Signals | 6 |

## Signals of VCFRONT_homelink

Tesla Model 3 CAN bus signals in `VCFRONT_homelink`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_homelinkV2Response0` | Front body controller: homelink V2 response0 | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCFRONT_homelinkV2Response1` | Front body controller: homelink V2 response1 | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCFRONT_homelinkV2Response2` | Front body controller: homelink V2 response2 | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCFRONT_homelinkV2Response3` | Front body controller: homelink V2 response3 | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCFRONT_homelinkV2Response4` | Front body controller: homelink V2 response4 | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCFRONT_homelinkCommStatus` | Homelink communication status; raw 0 = signal not available (SNA) | 40\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `HOMELINK_COMM_STATUS_SNA`<br>1 = `HOMELINK_COMM_STATUS_OFF`<br>2 = `HOMELINK_COMM_STATUS_ON`<br>3 = `HOMELINK_COMM_STATUS_FAULT` | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
