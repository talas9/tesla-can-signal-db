---
layout: default
title: "DIR_motorStatus (0x126) — Rear drive inverter, Tesla Model 3 2026.26.6.5 PARTY CAN"
description: "Rear drive inverter message: motor status. Tesla Model 3 CAN bus message DIR_motorStatus (0x126) of Rear drive inverter, firmware 2026.26.6.5, 7 signals (DIR_motorCurrent, DIR_switchingFrequency, DIR_targetFluxMode, DIR_switchShortTestRetryCount and 3 more). Bit layout, scaling, units and value tables."
---

# DIR_motorStatus (0x126) — Rear drive inverter, Tesla Model 3 2026.26.6.5 PARTY CAN

Rear drive inverter message: motor status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 7 signals of DIR_motorStatus as defined for Tesla Model 3 firmware 2026.26.6.5 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DIR_motorStatus` |
| CAN id | 0x126 (294) |
| ECU | [Rear drive inverter](../../dir.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | DIR |
| Frame length | 5 bytes |
| Cycle time | 100 ms |
| Signals | 7 |

## Signals of DIR_motorStatus

Tesla Model 3 CAN bus signals in `DIR_motorStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIR_motorCurrent` | Drive Inverer measured motor RMS phase current. | 0\|11 | little-endian | unsigned | 1 | 0 | A | 0 to 2047 |  | plausible |
| `DIR_switchingFrequency` | Rear drive inverter: switching frequency | 11\|11 | little-endian | unsigned | 0.01 | 0 | kHz | 0 to 20 |  | plausible |
| `DIR_targetFluxMode` | Rear drive inverter: target flux mode | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DI_FLUXMODE_OPTIMUM`<br>1 = `DI_FLUXMODE_FS`<br>2 = `DI_FLUXMODE_FW` | plausible |
| `DIR_switchShortTestRetryCount` | Rear drive inverter: switch short test retry count | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | layout-only |
| `DIR_keepAliveRequest` | Used to detect that the Drive Inverter (DI) expects 12V and High Voltage (HV) to be kept up in order to protect hardware. | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NO_REQUEST`<br>1 = `KEEP_ALIVE` | plausible |
| `DIR_motorStatusCounter` | Rear drive inverter: motor status counter | 27\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `DIR_motorStatusChecksum` | Rear drive inverter: motor status checksum | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 PARTY DBC file](../../../../../dbc/Model3/2026.26.6.5/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/PARTY.json)

## See also

- [All Rear drive inverter messages (DIR)](../../dir.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
