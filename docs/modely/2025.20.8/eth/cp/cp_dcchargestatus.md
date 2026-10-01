---
layout: default
title: "CP_dcChargeStatus (0x29D) — Charge port controller, Tesla Model Y 2025.20.8 ETH"
description: "Charge port controller message: dc charge status. Ethernet-side message CP_dcChargeStatus of Charge port controller for Tesla Model Y firmware 2025.20.8, 3 signals (CP_evseOutputDcCurrent, CP_evseOutputDcVoltage, CP_evseOutputDcCurrentStale). Bit layout, scaling, units and value tables."
---

# CP_dcChargeStatus (0x29D) — Charge port controller, Tesla Model Y 2025.20.8 ETH

Charge port controller message: dc charge status. This page documents the 3 signals of CP_dcChargeStatus as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `CP_dcChargeStatus` |
| Ethernet-side id | 0x29D (669) |
| ECU | [Charge port controller](../../cp.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | CP |
| Frame length | 4 bytes |
| Cycle time | 100 ms |
| Signals | 3 |

## Signals of CP_dcChargeStatus

Tesla Model Y CAN bus signals in `CP_dcChargeStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `CP_evseOutputDcCurrent` | The DC EVSE's measured output current | 0\|15 | little-endian | signed | 0.125 | 0 | A | -2048 to 2047.875 |  | plausible |
| `CP_evseOutputDcVoltage` | The DC EVSE's measured output voltage | 16\|13 | little-endian | unsigned | 0.07324219 | 0 | V | 0 to 599.92675822 |  | plausible |
| `CP_evseOutputDcCurrentStale` | Indicates whether the data in CP_evseOutputDcCurrent has not been updated with new info from the DC EVSE recently | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Charge port controller messages (CP)](../../cp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
