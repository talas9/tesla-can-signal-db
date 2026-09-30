---
layout: default
title: "TCU_alertLog (0x582) — TCU ECU, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "TCU ECU message: alert log. Ethernet-side message TCU_alertLog of TCU ECU for Tesla Model 3 / Model Y firmware 2025.20.8, 7 signals (TCU_alertID, TCU_alertState, TCU_w001_FailCode, TCU_w002_RejCause and 3 more). Bit layout, scaling, units and value tables."
---

# TCU_alertLog (0x582) — TCU ECU, Tesla Model 3 / Model Y 2025.20.8 ETH

TCU ECU message: alert log. This page documents the 7 signals of TCU_alertLog as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `TCU_alertLog` |
| Ethernet-side id | 0x582 (1410) |
| ECU | [TCU ECU](../../tcu.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | TCU |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 7 |

## Signals of TCU_alertLog

Tesla Model 3 / Model Y CAN bus signals in `TCU_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `TCU_alertID` | selector | TCU ECU: alert ID | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `w001_IMSRegistrationFailed`<br>2 = `w002_CellRegRejected`<br>3 = `w003_ECallFailed`<br>4 = `w004_MSDTransmissionFailed`<br>5 = `w005_SIMSlotError`<br>6 = `w006_MpssUnavailable` | plausible |
| `TCU_alertState` |  | TCU ECU: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `TCU_w001_FailCode` | page 1 | TCU ECU: w001 fail code | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TCU_w002_RejCause` | page 2 | TCU ECU: w002 rej cause | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TCU_w003_CallFailCode` | page 3 | TCU ECU: w003 call fail code | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TCU_w004_MSDFailCode` | page 4 | TCU ECU: w004 MSD fail code | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TCU_w006_Count` | page 6 | TCU ECU: w006 count | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |

## Multiplexing

`TCU_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (1 signals), page 2 (1 signals), page 3 (1 signals), page 4 (1 signals), page 6 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All TCU ECU messages (TCU)](../../tcu.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
