---
layout: default
title: "DIF_motorStatus (0x1A5) — Front drive inverter, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Front drive inverter message: motor status. Ethernet-side message DIF_motorStatus of Front drive inverter for Tesla Model 3 / Model Y firmware 2025.20.8, 4 signals (DIF_motorCurrent, DIF_switchingFrequency, DIF_targetFluxMode, DIF_switchShortTestRetryCount). Bit layout, scaling, units and value tables."
---

# DIF_motorStatus (0x1A5) — Front drive inverter, Tesla Model 3 / Model Y 2025.20.8 ETH

Front drive inverter message: motor status. This page documents the 4 signals of DIF_motorStatus as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DIF_motorStatus` |
| Ethernet-side id | 0x1A5 (421) |
| ECU | [Front drive inverter](../../dif.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DIF |
| Frame length | 4 bytes |
| Cycle time | 100 ms |
| Signals | 4 |

## Signals of DIF_motorStatus

Tesla Model 3 / Model Y CAN bus signals in `DIF_motorStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIF_motorCurrent` | Drive Inverer measured motor RMS phase current. | 0\|11 | little-endian | unsigned | 1 | 0 | A | 0 to 2047 |  | plausible |
| `DIF_switchingFrequency` | Front drive inverter: switching frequency | 11\|11 | little-endian | unsigned | 0.01 | 0 | kHz | 0 to 20 |  | plausible |
| `DIF_targetFluxMode` | Front drive inverter: target flux mode | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DI_FLUXMODE_OPTIMUM`<br>1 = `DI_FLUXMODE_FS`<br>2 = `DI_FLUXMODE_FW` | plausible |
| `DIF_switchShortTestRetryCount` | Front drive inverter: switch short test retry count | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Front drive inverter messages (DIF)](../../dif.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
