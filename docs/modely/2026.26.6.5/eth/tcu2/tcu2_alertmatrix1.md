---
layout: default
title: "TCU2_alertMatrix1 (0x586) — TCU2 ECU, Tesla Model Y 2026.26.6.5 ETH"
description: "TCU2 ECU message: alert matrix1. Ethernet-side message TCU2_alertMatrix1 of TCU2 ECU for Tesla Model Y firmware 2026.26.6.5, 16 signals (TCU2_w001_IMSRegistrationFailed, TCU2_w002_CellRegRejected, TCU2_w003_ECallFailed, TCU2_w004_MSDTransmissionFailed and 12 more). Bit layout, scaling, units and value tables."
---

# TCU2_alertMatrix1 (0x586) — TCU2 ECU, Tesla Model Y 2026.26.6.5 ETH

TCU2 ECU message: alert matrix1. This page documents the 16 signals of TCU2_alertMatrix1 as defined for Tesla Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `TCU2_alertMatrix1` |
| Ethernet-side id | 0x586 (1414) |
| ECU | [TCU2 ECU](../../tcu2.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | TCU2 |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 16 |

## Signals of TCU2_alertMatrix1

Tesla Model Y CAN bus signals in `TCU2_alertMatrix1`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `TCU2_w001_IMSRegistrationFailed` | TCU2 ECU: w001 IMS registration failed | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU2_w002_CellRegRejected` | TCU2 ECU: w002 cell reg rejected | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU2_w003_ECallFailed` | TCU2 ECU: w003 e call failed | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU2_w004_MSDTransmissionFailed` | TCU2 ECU: w004 MSD transmission failed | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU2_w005_SIMSlotError` | TCU2 ECU: w005 SIM slot error | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU2_w006_MpssUnavailable` | TCU2 ECU: w006 mpss unavailable | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU2_w007_ModemUnreachable` | TCU2 ECU: w007 modem unreachable | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU2_w008_KernelPanic` | TCU2 ECU: w008 kernel panic | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU2_w009_WifiFirmwareCrash` | TCU2 ECU: w009 wifi firmware crash | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU2_w010_WifiDumpDetected` | TCU2 ECU: w010 wifi dump detected | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU2_w011_CellDumpDetected` | TCU2 ECU: w011 cell dump detected | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU2_w012_UplinkDegraded` | TCU2 ECU: w012 uplink degraded | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU2_w013_UplinkQueueFull` | TCU2 ECU: w013 uplink queue full | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU2_w014_HostapdCrash` | TCU2 ECU: w014 hostapd crash | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU2_w015_NPNSubscriptionActive` | TCU2 ECU: w015 NPN subscription active | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `TCU2_w016_IMEIMismatch` | TCU2 ECU: w016 IMEI mismatch | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/ModelY/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All TCU2 ECU messages (TCU2)](../../tcu2.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
