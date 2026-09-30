---
layout: default
title: "TCU_alertLog (0x485) — TCU ECU, Tesla Model 3 / Model Y 2026.26.6.5 ETH"
description: "TCU ECU message: alert log. Ethernet-side message TCU_alertLog of TCU ECU for Tesla Model 3 / Model Y firmware 2026.26.6.5, 22 signals (TCU_alertID, TCU_alertState, TCU_w001_FailCode, TCU_w002_RejCause and 18 more). Bit layout, scaling, units and value tables."
---

# TCU_alertLog (0x485) — TCU ECU, Tesla Model 3 / Model Y 2026.26.6.5 ETH

TCU ECU message: alert log. This page documents the 22 signals of TCU_alertLog as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `TCU_alertLog` |
| Ethernet-side id | 0x485 (1157) |
| ECU | [TCU ECU](../../tcu.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | TCU |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 22 |

## Signals of TCU_alertLog

Tesla Model 3 / Model Y CAN bus signals in `TCU_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `TCU_alertID` | selector | TCU ECU: alert ID | 0\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `w001_IMSRegistrationFailed`<br>2 = `w002_CellRegRejected`<br>3 = `w003_ECallFailed`<br>4 = `w004_MSDTransmissionFailed`<br>5 = `w005_SIMSlotError`<br>6 = `w006_MpssUnavailable`<br>7 = `w007_ModemUnreachable`<br>8 = `w008_KernelPanic`<br>9 = `w009_WifiFirmwareCrash`<br>10 = `w010_WifiDumpDetected`<br>11 = `w011_CellDumpDetected`<br>12 = `w012_UplinkDegraded`<br>13 = `w013_UplinkQueueFull`<br>14 = `w014_HostapdCrash`<br>15 = `w015_NPNSubscriptionActive`<br>16 = `w016_IMEIMismatch` | plausible |
| `TCU_alertState` |  | TCU ECU: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `TCU_w001_FailCode` | page 1 | TCU ECU: w001 fail code | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TCU_w002_RejCause` | page 2 | TCU ECU: w002 rej cause | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TCU_w003_CallFailCode` | page 3 | TCU ECU: w003 call fail code | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TCU_w004_MSDFailCode` | page 4 | TCU ECU: w004 MSD fail code | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TCU_w006_Count` | page 6 | TCU ECU: w006 count | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TCU_w007_Count` | page 7 | TCU ECU: w007 count | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TCU_w009_CrashCode` | page 9 | TCU ECU: w009 crash code | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TCU_w012_DataRAT` | page 12 | TCU ECU: w012 data RAT | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `GSM`<br>2 = `WCDMA`<br>3 = `LTE`<br>4 = `NR5G_NSA`<br>5 = `NR5G_SA`<br>6 = `NR5G_UNKNOWN` | plausible |
| `TCU_w012_RSRP` | page 12 | TCU ECU: w012 RSRP | 20\|8 | little-endian | signed | 1 | 0 | dBm | -128 to 127 |  | plausible |
| `TCU_w012_RSRQ` | page 12 | TCU ECU: w012 RSRQ | 28\|7 | little-endian | signed | 1 | 0 | dBm | -64 to 63 |  | plausible |
| `TCU_w012_MNC` | page 12 | TCU ECU: w012 MNC | 45\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 |  | layout-only |
| `TCU_w012_AvgQueueUsage` | page 12 | TCU ECU: w012 avg queue usage | 55\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `TCU_w012_NSAAvailable` | page 12 | TCU ECU: w012 NSA available | 62\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `AVAILABLE`<br>2 = `NOT_AVAILABLE` | plausible |
| `TCU_w013_DataRAT` | page 13 | TCU ECU: w013 data RAT | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `GSM`<br>2 = `WCDMA`<br>3 = `LTE`<br>4 = `NR5G_NSA`<br>5 = `NR5G_SA`<br>6 = `NR5G_UNKNOWN` | plausible |
| `TCU_w013_RSRP` | page 13 | TCU ECU: w013 RSRP | 20\|8 | little-endian | signed | 1 | 0 | dBm | -128 to 127 |  | plausible |
| `TCU_w013_RSRQ` | page 13 | TCU ECU: w013 RSRQ | 28\|7 | little-endian | signed | 1 | 0 | dBm | -64 to 63 |  | plausible |
| `TCU_w013_MNC` | page 13 | TCU ECU: w013 MNC | 45\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 |  | layout-only |
| `TCU_w013_AvgQueueUsage` | page 13 | TCU ECU: w013 avg queue usage | 55\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `TCU_w013_NSAAvailable` | page 13 | TCU ECU: w013 NSA available | 62\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `AVAILABLE`<br>2 = `NOT_AVAILABLE` | plausible |
| `TCU_w014_Reason` | page 14 | TCU ECU: w014 reason | 16\|32 | little-endian | signed | 1 | 0 |  | -2147483648 to 2147483647 |  | layout-only |

## Multiplexing

`TCU_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (1 signals), page 2 (1 signals), page 3 (1 signals), page 4 (1 signals), page 6 (1 signals), page 7 (1 signals), page 9 (1 signals), page 12 (6 signals), page 13 (6 signals), page 14 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/AllModels/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All TCU ECU messages (TCU)](../../tcu.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
