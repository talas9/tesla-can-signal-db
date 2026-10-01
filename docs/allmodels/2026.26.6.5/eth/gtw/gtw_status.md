---
layout: default
title: "GTW_status (0x348) — Gateway, Tesla Model 3 / Model Y 2026.26.6.5 ETH"
description: "Gateway message: status. Ethernet-side message GTW_status of Gateway for Tesla Model 3 / Model Y firmware 2026.26.6.5, 10 signals (GTW_vehicleVersionMatchStatus, GTW_hwtype, GTW_jcanProductName, GTW_uptimeSeconds and 6 more). Bit layout, scaling, units and value tables."
---

# GTW_status (0x348) — Gateway, Tesla Model 3 / Model Y 2026.26.6.5 ETH

Gateway message: status. This page documents the 10 signals of GTW_status as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `GTW_status` |
| Ethernet-side id | 0x348 (840) |
| ECU | [Gateway](../../gtw.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 10 |

## Signals of GTW_status

Tesla Model 3 / Model Y CAN bus signals in `GTW_status`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `GTW_vehicleVersionMatchStatus` | Signal to indicate if the vehicle ECUs are all on a matched production version | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_CALCULATED_YET`<br>1 = `MISMATCHED`<br>2 = `MATCHED` | plausible |
| `GTW_hwtype` | Describes the chip GTW is running on; raw 0 = signal not available (SNA) | 2\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `MPC57`<br>2 = `SPC58`<br>3 = `TRAVEO2` | plausible |
| `GTW_jcanProductName` | Describes the JCAN reference (product) name; raw 0 = signal not available (SNA) | 4\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `SNA`<br>1 = `MODEL3`<br>2 = `MODELY`<br>3 = `LYCHEE`<br>4 = `TAMARIND`<br>5 = `SEMITRUCK`<br>6 = `POPPYSEED`<br>7 = `CYBERTRUCK`<br>8 = `BAYBERRY`<br>10 = `GOLDENSNITCH`<br>11 = `SEMITRUCKV2` | plausible |
| `GTW_uptimeSeconds` | GTW uptime in seconds | 15\|32 | big-endian | unsigned | 1 | 0 | s | 0 to 4294967295 |  | plausible |
| `GTW_boardRevision` | Board revision ID of the MCU PCBA | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `GTW_touchcoreOsType` | Gateway: touchcore os type | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `GTW_OS_FREERTOS`<br>1 = `GTW_OS_RT` | plausible |
| `GTW_sentryModeState` | Sentry Mode state; raw 6 = signal not available (SNA) | 49\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OFF`<br>1 = `IDLE`<br>2 = `ARMED`<br>3 = `AWARE`<br>4 = `PANIC`<br>5 = `QUIET`<br>6 = `SNA` | plausible |
| `GTW_secureBootEnabled` | Gateway: secure boot enabled | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FALSE`<br>1 = `TRUE` | plausible |
| `GTW_socSleepType` | Describes the sleep type GTW is expecting from the SoC; raw 0 = signal not available (SNA) | 56\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `SNA`<br>1 = `S3`<br>2 = `SHALLOW` | plausible |
| `GTW_resetType` | Describes the type of reset GTW experienced; raw 0 = signal not available (SNA) | 58\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `SNA`<br>1 = `POR`<br>2 = `SOFTWARE`<br>3 = `BUTTON`<br>4 = `WAKE`<br>5 = `MAINCORE_WATCHDOG`<br>6 = `CANCORE_WATCHDOG`<br>7 = `TOUCHCORE_WATCHDOG`<br>8 = `OTHER` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/AllModels/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Gateway messages (GTW)](../../gtw.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
