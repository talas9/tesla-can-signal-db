---
layout: default
title: "DIR_motorStatus (0x7F7) — Rear drive inverter, Tesla Model Y 2025.20.8 ETH"
description: "Rear drive inverter message: motor status. Ethernet-side message DIR_motorStatus of Rear drive inverter for Tesla Model Y firmware 2025.20.8, 4 signals (DIR_motorCurrent, DIR_switchingFrequency, DIR_targetFluxMode, DIR_switchShortTestRetryCount). Bit layout, scaling, units and value tables."
---

# DIR_motorStatus (0x7F7) — Rear drive inverter, Tesla Model Y 2025.20.8 ETH

Rear drive inverter message: motor status. This page documents the 4 signals of DIR_motorStatus as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DIR_motorStatus` |
| Ethernet-side id | 0x7F7 (2039) |
| ECU | [Rear drive inverter](../../dir.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DIR |
| Frame length | 4 bytes |
| Cycle time | 100 ms |
| Signals | 4 |

## Signals of DIR_motorStatus

Tesla Model Y CAN bus signals in `DIR_motorStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIR_motorCurrent` | Drive Inverer measured motor RMS phase current. | 0\|11 | little-endian | unsigned | 1 | 0 | A | 0 to 2047 |  | plausible |
| `DIR_switchingFrequency` | Rear drive inverter: switching frequency | 11\|11 | little-endian | unsigned | 0.01 | 0 | kHz | 0 to 20 |  | plausible |
| `DIR_targetFluxMode` | Rear drive inverter: target flux mode | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DI_FLUXMODE_OPTIMUM`<br>1 = `DI_FLUXMODE_FS`<br>2 = `DI_FLUXMODE_FW` | plausible |
| `DIR_switchShortTestRetryCount` | Rear drive inverter: switch short test retry count | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Rear drive inverter messages (DIR)](../../dir.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
