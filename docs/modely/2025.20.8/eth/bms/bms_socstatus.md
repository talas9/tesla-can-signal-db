---
layout: default
title: "BMS_socStatus (0x292) — High-voltage battery management system, Tesla Model Y 2025.20.8 ETH"
description: "High-voltage battery management system message: soc status. Ethernet-side message BMS_socStatus of High-voltage battery management system for Tesla Model Y firmware 2025.20.8, 7 signals (BMS_socMin, BMS_socUI, BMS_socMax, BMS_socAvg and 3 more). Bit layout, scaling, units and value tables."
---

# BMS_socStatus (0x292) — High-voltage battery management system, Tesla Model Y 2025.20.8 ETH

High-voltage battery management system message: soc status. This page documents the 7 signals of BMS_socStatus as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_socStatus` |
| Ethernet-side id | 0x292 (658) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 7 |

## Signals of BMS_socStatus

Tesla Model Y CAN bus signals in `BMS_socStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_socMin` | BMS State Of Charge (SOC). This is the minimum brick SOC. | 0\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.2 |  | validated |
| `BMS_socUI` | BMS State Of Energy (SOE) for the UI. This is ideal discharge energy from present state / ideal discharge energy from full. | 10\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 100 |  | validated |
| `BMS_socMax` | BMS State Of Charge (SOC). This is the maximum brick SOC. | 20\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.2 |  | validated |
| `BMS_socAvg` | BMS State Of Charge (SOC). This is the average of all the brick SOCs | 30\|10 | little-endian | unsigned | 0.1 | 0 | % | 0 to 102.2 |  | validated |
| `BMS_beginningOfLifePackEnergy` | High-voltage battery management system: beginning of life pack energy; raw 1023 = signal not available (SNA) | 40\|10 | little-endian | unsigned | 0.1 | 0 | KWh | 0 to 102.2 | 1023 = `SNA` | validated |
| `BMS_battTempPct` | High-voltage battery management system: batt temp pct; raw 255 = signal not available (SNA) | 50\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 100 | 255 = `SNA` | plausible |
| `BMS_userChargeCurrentLimitMode` | BMS' user-facing reason for charge being either limited or not limited | 58\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `USR_CHG_LIMIT_NONE`<br>1 = `USR_CHG_LIMIT_EVSE`<br>2 = `USR_CHG_LIMIT_BATT_TEMP_LOW`<br>3 = `USR_CHG_LIMIT_HIGH_SOC`<br>4 = `USR_CHG_LIMIT_EVSE_RELOCATION_RECOMMENDED` | plausible |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
