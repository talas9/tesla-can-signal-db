---
layout: default
title: "PM_systemState (0x1CF) — PM ECU, Tesla Model Y 2025.20.8 ETH"
description: "PM ECU message: system state. Ethernet-side message PM_systemState of PM ECU for Tesla Model Y firmware 2025.20.8, 11 signals (PM_torqueCheckState, PM_limpRequest, PM_torqueCommand, PM_torqueState and 7 more). Bit layout, scaling, units and value tables."
---

# PM_systemState (0x1CF) — PM ECU, Tesla Model Y 2025.20.8 ETH

PM ECU message: system state. This page documents the 11 signals of PM_systemState as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `PM_systemState` |
| Ethernet-side id | 0x1CF (463) |
| ECU | [PM ECU](../../pm.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | PM |
| Frame length | 8 bytes |
| Cycle time | 10 ms |
| Signals | 11 |

## Signals of PM_systemState

Tesla Model Y CAN bus signals in `PM_systemState`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PM_torqueCheckState` | PM ECU: torque check state | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `START`<br>1 = `POLICING`<br>2 = `CANNOT_POLICE_COMMAND`<br>3 = `CANNOT_POLICE_MEASUREMENT`<br>4 = `CANNOT_POLICE_AT_ALL` | plausible |
| `PM_limpRequest` | PM ECU: limp request | 3\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `OK`<br>1 = `UNIT`<br>2 = `SYSTEM` | plausible |
| `PM_torqueCommand` | PM ECU: torque command; raw 4096 = signal not available (SNA) | 8\|13 | little-endian | signed | 2 | 0 | Nm | -8192 to 8190 | -4096 = `SNA` | plausible |
| `PM_torqueState` | PM ECU: torque state | 21\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `ALLOWED`<br>1 = `DISALLOWED`<br>2 = `INHIBITED` | plausible |
| `PM_hvilSystemStatus` | HVIL system status; raw 3 = signal not available (SNA) | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `DISABLED`<br>1 = `OPEN`<br>2 = `CLOSED`<br>3 = `SNA` | plausible |
| `PM_sysElecPower` | PM ECU: sys elec power; raw 1024 = signal not available (SNA) | 26\|11 | little-endian | signed | 1 | 250 | kW | -774 to 1273 | -1024 = `SNA` | plausible |
| `PM_sysNumUnitsMia` | PM ECU: sys num units mia | 37\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | layout-only |
| `PM_sysNumUnitsSna` | PM ECU: sys num units sna | 39\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | layout-only |
| `PM_sysElecPowerVeryLow` | PM ECU: sys elec power very low | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_systemStateCounter` | PM ECU: system state counter | 53\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | layout-only |
| `PM_systemStateChecksum` | PM ECU: system state checksum | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All PM ECU messages (PM)](../../pm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
