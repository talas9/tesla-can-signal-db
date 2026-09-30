---
layout: default
title: "CP_thermalStatus (0x37D) — Charge port controller, Tesla Model Y 2025.20.8 ETH"
description: "Charge port controller message: thermal status. Ethernet-side message CP_thermalStatus of Charge port controller for Tesla Model Y firmware 2025.20.8, 4 signals (CP_thermalStatusSelect, CP_pinTemperature1, CP_pinTemperature2, CP_pinTemperature3). Bit layout, scaling, units and value tables."
---

# CP_thermalStatus (0x37D) — Charge port controller, Tesla Model Y 2025.20.8 ETH

Charge port controller message: thermal status. This page documents the 4 signals of CP_thermalStatus as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `CP_thermalStatus` |
| Ethernet-side id | 0x37D (893) |
| ECU | [Charge port controller](../../cp.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | CP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 4 |

## Signals of CP_thermalStatus

Tesla Model Y CAN bus signals in `CP_thermalStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `CP_thermalStatusSelect` | selector | Charge port controller: thermal status select | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `0`<br>1 = `1` | plausible |
| `CP_pinTemperature1` | page 1 | Sensed temperature of the charge port inlet pins | 8\|8 | little-endian | unsigned | 0.8039216 | -55 | C | -55 to 149.99 |  | validated |
| `CP_pinTemperature2` | page 1 | Sensed temperature of the charge port inlet pins | 16\|8 | little-endian | unsigned | 0.8039216 | -55 | C | -55 to 149.99 |  | validated |
| `CP_pinTemperature3` | page 1 | Sensed temperature of the charge port inlet pins | 24\|8 | little-endian | unsigned | 0.8039216 | -55 | C | -55 to 149.99 |  | validated |

## Multiplexing

`CP_thermalStatusSelect` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (3 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Charge port controller messages (CP)](../../cp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
