---
layout: default
title: "DIF_motorStatus (0x1A5) — Front drive inverter, Tesla Model Y 2026.26.6.5 PARTY CAN"
description: "Front drive inverter message: motor status. Tesla Model Y CAN bus message DIF_motorStatus (0x1A5) of Front drive inverter, firmware 2026.26.6.5, 7 signals (DIF_motorCurrent, DIF_switchingFrequency, DIF_targetFluxMode, DIF_switchShortTestRetryCount and 3 more). Bit layout, scaling, units and value tables."
---

# DIF_motorStatus (0x1A5) — Front drive inverter, Tesla Model Y 2026.26.6.5 PARTY CAN

Front drive inverter message: motor status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 7 signals of DIF_motorStatus as defined for Tesla Model Y firmware 2026.26.6.5 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DIF_motorStatus` |
| CAN id | 0x1A5 (421) |
| ECU | [Front drive inverter](../../dif.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | DIF |
| Frame length | 5 bytes |
| Cycle time | 100 ms |
| Signals | 7 |

## Signals of DIF_motorStatus

Tesla Model Y CAN bus signals in `DIF_motorStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIF_motorCurrent` | Drive Inverer measured motor RMS phase current. | 0\|11 | little-endian | unsigned | 1 | 0 | A | 0 to 2047 |  | validated |
| `DIF_switchingFrequency` | Front drive inverter: switching frequency | 11\|11 | little-endian | unsigned | 0.01 | 0 | kHz | 0 to 20 |  | validated |
| `DIF_targetFluxMode` | Front drive inverter: target flux mode | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DI_FLUXMODE_OPTIMUM`<br>1 = `DI_FLUXMODE_FS`<br>2 = `DI_FLUXMODE_FW` | validated |
| `DIF_switchShortTestRetryCount` | Front drive inverter: switch short test retry count | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | validated |
| `DIF_keepAliveRequest` | Used to detect that the Drive Inverter (DI) expects 12V and High Voltage (HV) to be kept up in order to protect hardware. | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NO_REQUEST`<br>1 = `KEEP_ALIVE` | validated |
| `DIF_motorStatusCounter` | Front drive inverter: motor status counter | 27\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `DIF_motorStatusChecksum` | Front drive inverter: motor status checksum | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 PARTY DBC file](../../../../../dbc/ModelY/2026.26.6.5/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/PARTY.json)

## See also

- [All Front drive inverter messages (DIF)](../../dif.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
