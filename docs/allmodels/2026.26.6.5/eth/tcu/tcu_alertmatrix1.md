---
layout: default
title: "TCU_alertMatrix1 (0x486) — TCU ECU, Tesla Model 3 / Model Y 2026.26.6.5 ETH"
description: "TCU ECU message: alert matrix1. Ethernet-side message TCU_alertMatrix1 of TCU ECU for Tesla Model 3 / Model Y firmware 2026.26.6.5, 16 signals (TCU_w001_IMSRegistrationFailed, TCU_w002_CellRegRejected, TCU_w003_ECallFailed, TCU_w004_MSDTransmissionFailed and 12 more). Bit layout, scaling, units and value tables."
---

# TCU_alertMatrix1 (0x486) — TCU ECU, Tesla Model 3 / Model Y 2026.26.6.5 ETH

TCU ECU message: alert matrix1. This page documents the 16 signals of TCU_alertMatrix1 as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `TCU_alertMatrix1` |
| Ethernet-side id | 0x486 (1158) |
| ECU | [TCU ECU](../../tcu.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | TCU |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 16 |

## Signals of TCU_alertMatrix1

Tesla Model 3 / Model Y CAN bus signals in `TCU_alertMatrix1`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `TCU_w001_IMSRegistrationFailed` | TCU ECU: w001 IMS registration failed | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU_w002_CellRegRejected` | TCU ECU: w002 cell reg rejected | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU_w003_ECallFailed` | TCU ECU: w003 e call failed | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU_w004_MSDTransmissionFailed` | TCU ECU: w004 MSD transmission failed | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU_w005_SIMSlotError` | TCU ECU: w005 SIM slot error | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU_w006_MpssUnavailable` | TCU ECU: w006 mpss unavailable | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU_w007_ModemUnreachable` | TCU ECU: w007 modem unreachable | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU_w008_KernelPanic` | TCU ECU: w008 kernel panic | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU_w009_WifiFirmwareCrash` | TCU ECU: w009 wifi firmware crash | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU_w010_WifiDumpDetected` | TCU ECU: w010 wifi dump detected | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU_w011_CellDumpDetected` | TCU ECU: w011 cell dump detected | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU_w012_UplinkDegraded` | TCU ECU: w012 uplink degraded | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU_w013_UplinkQueueFull` | TCU ECU: w013 uplink queue full | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU_w014_HostapdCrash` | TCU ECU: w014 hostapd crash | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU_w015_NPNSubscriptionActive` | TCU ECU: w015 NPN subscription active | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU_w016_IMEIMismatch` | TCU ECU: w016 IMEI mismatch | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/AllModels/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All TCU ECU messages (TCU)](../../tcu.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
