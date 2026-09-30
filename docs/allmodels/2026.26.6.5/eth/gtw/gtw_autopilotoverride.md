---
layout: default
title: "GTW_autopilotOverride (0x346) — Gateway, Tesla Model 3 / Model Y 2026.26.6.5 ETH"
description: "Gateway message: autopilot override. Ethernet-side message GTW_autopilotOverride of Gateway for Tesla Model 3 / Model Y firmware 2026.26.6.5, 5 signals (GTW_autopilotOverrideState, GTW_autopilotConfig, GTW_autopilotOverrideConfig, GTW_autopilotConfigSource and 1 more). Bit layout, scaling, units and value tables."
---

# GTW_autopilotOverride (0x346) — Gateway, Tesla Model 3 / Model Y 2026.26.6.5 ETH

Gateway message: autopilot override. This page documents the 5 signals of GTW_autopilotOverride as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `GTW_autopilotOverride` |
| Ethernet-side id | 0x346 (838) |
| ECU | [Gateway](../../gtw.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 5 |

## Signals of GTW_autopilotOverride

Tesla Model 3 / Model Y CAN bus signals in `GTW_autopilotOverride`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `GTW_autopilotOverrideState` | Signals whether an autopilot trial or subscription is active | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `BASE`<br>1 = `SUBSCRIPTION`<br>2 = `TRIAL`<br>3 = `TIMEBOUND_SUBSCRIPTION`<br>4 = `TIMEBOUND_TRIAL`<br>5 = `OPTION_CODE`<br>6 = `OPTION_OVERRIDE`<br>7 = `VEHICLE_MANAGED`<br>8 = `UNKNOWN` | validated |
| `GTW_autopilotConfig` | Current level of permanent Autopilot firmware | 4\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `HIGHWAY`<br>2 = `ENHANCED`<br>3 = `SELF_DRIVING`<br>4 = `BASIC` | validated |
| `GTW_autopilotOverrideConfig` | Current level of trial or subscription Autopilot firmware | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `HIGHWAY`<br>2 = `ENHANCED`<br>3 = `SELF_DRIVING`<br>4 = `BASIC` | validated |
| `GTW_autopilotConfigSource` | Source of Autopilot configuration broadcast by Gateway | 11\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `GATEWAY`<br>1 = `AUTOPILOT`<br>2 = `AUTOPILOT_NOT_UPDATED` | validated |
| `GTW_autopilotOverrideExpireTime` | Expiration time for the currently active autopilot trial or subscription | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/AllModels/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Gateway messages (GTW)](../../gtw.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
