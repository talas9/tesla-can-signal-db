---
layout: default
title: "SCM_alertLog (0x54C) — SCM ECU, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "SCM ECU message: alert log. Tesla Model 3 / Model Y CAN bus message SCM_alertLog (0x54C) of SCM ECU, firmware 2025.20.8, 4 signals (SCM_alertID, SCM_alertType, SCM_a074_voltageWithRo, SCM_a074_voltageWithoutRo). Bit layout, scaling, units and value tables."
---

# SCM_alertLog (0x54C) — SCM ECU, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

SCM ECU message: alert log; frame length from the layout, not yet observed on a vehicle bus. This page documents the 4 signals of SCM_alertLog as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `SCM_alertLog` |
| CAN id | 0x54C (1356) |
| ECU | [SCM ECU](../../scm.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | SCM |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 4 |

## Signals of SCM_alertLog

Tesla Model 3 / Model Y CAN bus signals in `SCM_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `SCM_alertID` | selector | SCM ECU: alert ID | 0\|15 | little-endian | unsigned | 1 | 0 |  | 0 to 32767 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>27 = `a027_externalIsolationLow`<br>44 = `a044_proximityRationality`<br>74 = `a074_isoVDiffHi`<br>76 = `a076_bmsMIA`<br>78 = `a078_voltageMatchTimeout`<br>91 = `a091_voltageRiseDetection` | plausible |
| `SCM_alertType` |  | SCM ECU: alert type | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `SCM_a074_voltageWithRo` | page 74 | SCM ECU: a074 voltage with ro | 16\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `SCM_a074_voltageWithoutRo` | page 74 | SCM ECU: a074 voltage without ro | 28\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |

## Multiplexing

`SCM_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 74 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All SCM ECU messages (SCM)](../../scm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
