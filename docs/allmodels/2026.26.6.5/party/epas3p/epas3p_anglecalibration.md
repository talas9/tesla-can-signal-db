---
layout: default
title: "EPAS3P_angleCalibration (0x3D1) — Electric power steering (primary), Tesla Model 3 / Model Y 2026.26.6.5 PARTY CAN"
description: "Electric power steering (primary) message: angle calibration. Tesla Model 3 / Model Y CAN bus message EPAS3P_angleCalibration (0x3D1) of Electric power steering (primary), firmware 2026.26.6.5, 6 signals (EPAS3P_appliedAngleOffset, EPAS3P_calculatedAngleOffset, EPAS3P_resyncStatus, EPAS3P_pullDriftLongTermTrq and 2 more). Bit layout, scaling, units and value tables."
---

# EPAS3P_angleCalibration (0x3D1) — Electric power steering (primary), Tesla Model 3 / Model Y 2026.26.6.5 PARTY CAN

Electric power steering (primary) message: angle calibration; frame length from the layout, not yet observed on a vehicle bus. This page documents the 6 signals of EPAS3P_angleCalibration as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `EPAS3P_angleCalibration` |
| CAN id | 0x3D1 (977) |
| ECU | [Electric power steering (primary)](../../epas3p.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | EPAS3P |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 6 |

## Signals of EPAS3P_angleCalibration

Tesla Model 3 / Model Y CAN bus signals in `EPAS3P_angleCalibration`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `EPAS3P_appliedAngleOffset` | This represents the angle delta between the absolute steering angle reference and what EPAS estimates to be straight ahead. The steering angle offset can change up to 5deg at the beginning of each drive cycle. | 0\|8 | little-endian | unsigned | 0.1 | -12.8 | deg | -12.8 to 12.7 |  | plausible |
| `EPAS3P_calculatedAngleOffset` | Reports the calculated steering angle offset learned between the Steering Column Control Module (SCCM) and the Electronic Power Assist Steering (EPAS) steering angle. | 8\|8 | little-endian | unsigned | 0.1 | -12.8 | deg | -12.8 to 12.7 |  | plausible |
| `EPAS3P_resyncStatus` | Electric power steering (primary): resync status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `RESYNC_PENDING`<br>1 = `RESYNC_COMPLETE` | plausible |
| `EPAS3P_pullDriftLongTermTrq` | The learned, long term pull drift or road crown compensation torque that the rack is applying to the steering wheel. | 17\|12 | little-endian | unsigned | 0.01 | -10 | Nm | -10 to 10 |  | plausible |
| `EPAS3P_pullDriftCompTrq` | The current pull drift or road crown compensation torque that the rack is applying to the steering wheel. | 29\|12 | little-endian | unsigned | 0.01 | -10 | Nm | -10 to 10 |  | plausible |
| `EPAS3P_learnedSCCMOffset` | Electric power steering (primary): learned SCCM offset | 41\|8 | little-endian | unsigned | 0.1 | -12.8 | deg | -12.8 to 12.7 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 PARTY DBC file](../../../../../dbc/AllModels/2026.26.6.5/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/PARTY.json)

## See also

- [All Electric power steering (primary) messages (EPAS3P)](../../epas3p.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
