---
layout: default
title: "TCU2_alertLog (0x585) — TCU2 ECU, Tesla Model Y 2026.26.6.5 ETH"
description: "TCU2 ECU message: alert log. Ethernet-side message TCU2_alertLog of TCU2 ECU for Tesla Model Y firmware 2026.26.6.5, 22 signals (TCU2_alertID, TCU2_alertState, TCU2_w001_FailCode, TCU2_w002_RejCause and 18 more). Bit layout, scaling, units and value tables."
---

# TCU2_alertLog (0x585) — TCU2 ECU, Tesla Model Y 2026.26.6.5 ETH

TCU2 ECU message: alert log. This page documents the 22 signals of TCU2_alertLog as defined for Tesla Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `TCU2_alertLog` |
| Ethernet-side id | 0x585 (1413) |
| ECU | [TCU2 ECU](../../tcu2.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | TCU2 |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 22 |

## Signals of TCU2_alertLog

Tesla Model Y CAN bus signals in `TCU2_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `TCU2_alertID` | selector | TCU2 ECU: alert ID | 0\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `w001_IMSRegistrationFailed`<br>2 = `w002_CellRegRejected`<br>3 = `w003_ECallFailed`<br>4 = `w004_MSDTransmissionFailed`<br>5 = `w005_SIMSlotError`<br>6 = `w006_MpssUnavailable`<br>7 = `w007_ModemUnreachable`<br>8 = `w008_KernelPanic`<br>9 = `w009_WifiFirmwareCrash`<br>10 = `w010_WifiDumpDetected`<br>11 = `w011_CellDumpDetected`<br>12 = `w012_UplinkDegraded`<br>13 = `w013_UplinkQueueFull`<br>14 = `w014_HostapdCrash`<br>15 = `w015_NPNSubscriptionActive`<br>16 = `w016_IMEIMismatch` | plausible |
| `TCU2_alertState` |  | TCU2 ECU: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `TCU2_w001_FailCode` | page 1 | TCU2 ECU: w001 fail code | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TCU2_w002_RejCause` | page 2 | TCU2 ECU: w002 rej cause | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TCU2_w003_CallFailCode` | page 3 | TCU2 ECU: w003 call fail code | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TCU2_w004_MSDFailCode` | page 4 | TCU2 ECU: w004 MSD fail code | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TCU2_w006_Count` | page 6 | TCU2 ECU: w006 count | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TCU2_w007_Count` | page 7 | TCU2 ECU: w007 count | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TCU2_w009_CrashCode` | page 9 | TCU2 ECU: w009 crash code | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TCU2_w012_DataRAT` | page 12 | TCU2 ECU: w012 data RAT | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `GSM`<br>2 = `WCDMA`<br>3 = `LTE`<br>4 = `NR5G_NSA`<br>5 = `NR5G_SA`<br>6 = `NR5G_UNKNOWN` | plausible |
| `TCU2_w012_RSRP` | page 12 | TCU2 ECU: w012 RSRP | 20\|8 | little-endian | signed | 1 | 0 | dBm | -128 to 127 |  | plausible |
| `TCU2_w012_RSRQ` | page 12 | TCU2 ECU: w012 RSRQ | 28\|7 | little-endian | signed | 1 | 0 | dBm | -64 to 63 |  | plausible |
| `TCU2_w012_MNC` | page 12 | TCU2 ECU: w012 MNC | 45\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 |  | layout-only |
| `TCU2_w012_AvgQueueUsage` | page 12 | TCU2 ECU: w012 avg queue usage | 55\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `TCU2_w012_NSAAvailable` | page 12 | TCU2 ECU: w012 NSA available | 62\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `AVAILABLE`<br>2 = `NOT_AVAILABLE` | plausible |
| `TCU2_w013_DataRAT` | page 13 | TCU2 ECU: w013 data RAT | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `GSM`<br>2 = `WCDMA`<br>3 = `LTE`<br>4 = `NR5G_NSA`<br>5 = `NR5G_SA`<br>6 = `NR5G_UNKNOWN` | plausible |
| `TCU2_w013_RSRP` | page 13 | TCU2 ECU: w013 RSRP | 20\|8 | little-endian | signed | 1 | 0 | dBm | -128 to 127 |  | plausible |
| `TCU2_w013_RSRQ` | page 13 | TCU2 ECU: w013 RSRQ | 28\|7 | little-endian | signed | 1 | 0 | dBm | -64 to 63 |  | plausible |
| `TCU2_w013_MNC` | page 13 | TCU2 ECU: w013 MNC | 45\|10 | little-endian | unsigned | 1 | 0 |  | 0 to 1023 |  | layout-only |
| `TCU2_w013_AvgQueueUsage` | page 13 | TCU2 ECU: w013 avg queue usage | 55\|7 | little-endian | unsigned | 1 | 0 | % | 0 to 127 |  | plausible |
| `TCU2_w013_NSAAvailable` | page 13 | TCU2 ECU: w013 NSA available | 62\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `AVAILABLE`<br>2 = `NOT_AVAILABLE` | plausible |
| `TCU2_w014_Reason` | page 14 | TCU2 ECU: w014 reason | 16\|32 | little-endian | signed | 1 | 0 |  | -2147483648 to 2147483647 |  | layout-only |

## Multiplexing

`TCU2_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (1 signals), page 2 (1 signals), page 3 (1 signals), page 4 (1 signals), page 6 (1 signals), page 7 (1 signals), page 9 (1 signals), page 12 (6 signals), page 13 (6 signals), page 14 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/ModelY/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All TCU2 ECU messages (TCU2)](../../tcu2.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
