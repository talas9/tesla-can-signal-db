---
layout: default
title: "DAS_lanes (0x239) — Driver assistance computer, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Driver assistance computer message: lanes. Tesla Model 3 / Model Y CAN bus message DAS_lanes (0x239) of Driver assistance computer, firmware 2026.26.6.5, 13 signals (DAS_leftLaneExists, DAS_rightLaneExists, DAS_virtualLaneWidth, DAS_virtualLaneViewRange and 9 more). Bit layout, scaling, units and value tables."
---

# DAS_lanes (0x239) — Driver assistance computer, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Driver assistance computer message: lanes; frame length from the layout, not yet observed on a vehicle bus. This page documents the 13 signals of DAS_lanes as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DAS_lanes` |
| CAN id | 0x239 (569) |
| ECU | [Driver assistance computer](../../das.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | DAS |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 13 |

## Signals of DAS_lanes

Tesla Model 3 / Model Y CAN bus signals in `DAS_lanes`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DAS_leftLaneExists` | Driver assistance computer: left lane exists | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_rightLaneExists` | Driver assistance computer: right lane exists | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DAS_virtualLaneWidth` | Driver assistance computer: virtual lane width | 4\|4 | little-endian | unsigned | 0.3125 | 2 | m | 2 to 6.6875 |  | plausible |
| `DAS_virtualLaneViewRange` | Driver assistance computer: virtual lane view range | 8\|8 | little-endian | unsigned | 1 | 0 | m | 0 to 160 |  | plausible |
| `DAS_virtualLaneC0` | Driver assistance computer: virtual lane C0 | 16\|8 | little-endian | unsigned | 0.035 | -3.5 | m | -3.5 to 3.5 |  | plausible |
| `DAS_virtualLaneC1` | Driver assistance computer: virtual lane C1 | 24\|8 | little-endian | unsigned | 0.0016 | -0.2 | rad | -0.2 to 0.2 |  | plausible |
| `DAS_virtualLaneC2` | Driver assistance computer: virtual lane C2 | 32\|8 | little-endian | unsigned | 2.0e-05 | -0.0025 | m-1 | -0.0025 to 0.0025 |  | plausible |
| `DAS_virtualLaneC3` | Driver assistance computer: virtual lane C3 | 40\|8 | little-endian | unsigned | 2.4e-07 | -3.0e-05 | m-2 | -3.0e-05 to 3.0e-05 |  | plausible |
| `DAS_leftLineUsage` | Driver assistance computer: left line usage | 48\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `REJECTED_UNAVAILABLE`<br>1 = `AVAILABLE`<br>2 = `FUSED`<br>3 = `BLACKLISTED` | plausible |
| `DAS_rightLineUsage` | Driver assistance computer: right line usage | 50\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `REJECTED_UNAVAILABLE`<br>1 = `AVAILABLE`<br>2 = `FUSED`<br>3 = `BLACKLISTED` | plausible |
| `DAS_leftFork` | Driver assistance computer: left fork | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `FORK_NONE`<br>1 = `FORK_AVAILABLE`<br>2 = `FORK_SELECTED`<br>3 = `FORK_UNAVAILABLE` | plausible |
| `DAS_rightFork` | Driver assistance computer: right fork | 54\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `FORK_NONE`<br>1 = `FORK_AVAILABLE`<br>2 = `FORK_SELECTED`<br>3 = `FORK_UNAVAILABLE` | plausible |
| `DAS_lanesCounter` | Driver assistance computer: lanes counter | 60\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer messages (DAS)](../../das.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
