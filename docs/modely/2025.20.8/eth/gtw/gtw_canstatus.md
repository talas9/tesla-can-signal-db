---
layout: default
title: "GTW_canStatus (0x388) — Gateway, Tesla Model Y 2025.20.8 ETH"
description: "Gateway message: can status. Ethernet-side message GTW_canStatus of Gateway for Tesla Model Y firmware 2025.20.8, 16 signals (GTW_VEH_canBusActivity, GTW_PARTY_canBusActivity, GTW_CH_canBusActivity, GTW_VEH_txWarning and 12 more). Bit layout, scaling, units and value tables."
---

# GTW_canStatus (0x388) — Gateway, Tesla Model Y 2025.20.8 ETH

Gateway message: can status. This page documents the 16 signals of GTW_canStatus as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `GTW_canStatus` |
| Ethernet-side id | 0x388 (904) |
| ECU | [Gateway](../../gtw.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | GTW |
| Frame length | 3 bytes |
| Cycle time | 1000 ms |
| Signals | 16 |

## Signals of GTW_canStatus

Tesla Model Y CAN bus signals in `GTW_canStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `GTW_VEH_canBusActivity` | Active if any frame detected on the bus | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_PARTY_canBusActivity` | Active if any frame detected on the bus | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_CH_canBusActivity` | Active if any frame detected on the bus | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_VEH_txWarning` | Gateway: VEH tx warning | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_PARTY_txWarning` | Gateway: PARTY tx warning | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_CH_txWarning` | Gateway: CH tx warning | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_VEH_rxWarning` | Gateway: VEH rx warning | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_PARTY_rxWarning` | Gateway: PARTY rx warning | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_CH_rxWarning` | Gateway: CH rx warning | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_VEH_faultConfinement` | Fault confinement as per CAN spec | 9\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `ERROR_ACTIVE`<br>1 = `ERROR_PASSIVE`<br>2 = `BUS_OFF` | plausible |
| `GTW_PARTY_faultConfinement` | Fault confinement as per CAN spec | 11\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `ERROR_ACTIVE`<br>1 = `ERROR_PASSIVE`<br>2 = `BUS_OFF` | plausible |
| `GTW_CH_faultConfinement` | Fault confinement as per CAN spec | 13\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `ERROR_ACTIVE`<br>1 = `ERROR_PASSIVE`<br>2 = `BUS_OFF` | plausible |
| `GTW_BDY_canBusActivity` | Active if any frame detected on the bus | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `GTW_BDY_txWarning` | Gateway: BDY tx warning | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_BDY_rxWarning` | Gateway: BDY rx warning | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_BDY_faultConfinement` | Fault confinement as per CAN spec | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `ERROR_ACTIVE`<br>1 = `ERROR_PASSIVE`<br>2 = `BUS_OFF` | plausible |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Gateway messages (GTW)](../../gtw.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
