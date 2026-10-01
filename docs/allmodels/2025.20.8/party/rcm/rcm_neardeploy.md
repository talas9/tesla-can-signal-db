---
layout: default
title: "RCM_nearDeploy (0x121) — Restraint control module, Tesla Model 3 / Model Y 2025.20.8 PARTY CAN"
description: "Restraint control module message: near deploy. Tesla Model 3 / Model Y CAN bus message RCM_nearDeploy (0x121) of Restraint control module, firmware 2025.20.8, 8 signals (RCM_nearDeployChecksum, RCM_nearDeployCounter, RCM_nearDeployRear, RCM_nearDeployRight and 4 more). Bit layout, scaling, units and value tables."
---

# RCM_nearDeploy (0x121) — Restraint control module, Tesla Model 3 / Model Y 2025.20.8 PARTY CAN

Restraint control module message: near deploy; frame length from the layout, not yet observed on a vehicle bus. This page documents the 8 signals of RCM_nearDeploy as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `RCM_nearDeploy` |
| CAN id | 0x121 (289) |
| ECU | [Restraint control module](../../rcm.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | RCM |
| Frame length | 4 bytes |
| Cycle time | 10 ms |
| Signals | 8 |

## Signals of RCM_nearDeploy

Tesla Model 3 / Model Y CAN bus signals in `RCM_nearDeploy`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `RCM_nearDeployChecksum` | Restraint control module: near deploy checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `RCM_nearDeployCounter` | Restraint control module: near deploy counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `RCM_nearDeployRear` | Indicates that a rear near deploy event has occurred. No airbags have been deployed; raw 3 = signal not available (SNA) | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `RCM_NEAR_DEPLOY_EVENT_INACTIVE`<br>1 = `RCM_NEAR_DEPLOY_EVENT_ACTIVE`<br>3 = `RCM_NEAR_DEPLOY_EVENT_SNA` | plausible |
| `RCM_nearDeployRight` | Indicates that a right side near deploy event has occurred. No airbags have been deployed; raw 3 = signal not available (SNA) | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `RCM_NEAR_DEPLOY_EVENT_INACTIVE`<br>1 = `RCM_NEAR_DEPLOY_EVENT_ACTIVE`<br>3 = `RCM_NEAR_DEPLOY_EVENT_SNA` | plausible |
| `RCM_nearDeployLeft` | Indicates that a left side near deploy event has occurred. No airbags have been deployed; raw 3 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `RCM_NEAR_DEPLOY_EVENT_INACTIVE`<br>1 = `RCM_NEAR_DEPLOY_EVENT_ACTIVE`<br>3 = `RCM_NEAR_DEPLOY_EVENT_SNA` | plausible |
| `RCM_nearDeployFront` | Indicates that a frontal near deploy event has occurred. No airbags have been deployed; raw 3 = signal not available (SNA) | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `RCM_NEAR_DEPLOY_EVENT_INACTIVE`<br>1 = `RCM_NEAR_DEPLOY_EVENT_ACTIVE`<br>3 = `RCM_NEAR_DEPLOY_EVENT_SNA` | plausible |
| `RCM_nearDeployRollover` | Indicates that a roll over near deploy event has occurred. No airbags have been deployed; raw 3 = signal not available (SNA) | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `RCM_NEAR_DEPLOY_EVENT_INACTIVE`<br>1 = `RCM_NEAR_DEPLOY_EVENT_ACTIVE`<br>3 = `RCM_NEAR_DEPLOY_EVENT_SNA` | plausible |
| `RCM_crashAlgoWakeup` | Crash Algorithm Wakeup status; raw 3 = signal not available (SNA) | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `RCM_CRASH_ALGO_WAKEUP_EVENT_INACTIVE`<br>1 = `RCM_CRASH_ALGO_WAKEUP_EVENT_ACTIVE`<br>3 = `RCM_CRASH_ALGO_WAKEUP_EVENT_SNA` | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 PARTY DBC file](../../../../../dbc/AllModels/2025.20.8/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/PARTY.json)

## See also

- [All Restraint control module messages (RCM)](../../rcm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
