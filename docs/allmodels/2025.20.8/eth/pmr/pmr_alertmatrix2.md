---
layout: default
title: "PMR_alertMatrix2 (0x3A0) — PMR ECU, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "PMR ECU message: alert matrix2. Ethernet-side message PMR_alertMatrix2 of PMR ECU for Tesla Model 3 / Model Y firmware 2025.20.8, 14 signals (PMR_a080_exceptionPrefetchAbort, PMR_a081_exceptionDataAbort, PMR_a082_exceptionDataAbort2, PMR_a083_ahbWriteError and 10 more). Bit layout, scaling, units and value tables."
---

# PMR_alertMatrix2 (0x3A0) — PMR ECU, Tesla Model 3 / Model Y 2025.20.8 ETH

PMR ECU message: alert matrix2. This page documents the 14 signals of PMR_alertMatrix2 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `PMR_alertMatrix2` |
| Ethernet-side id | 0x3A0 (928) |
| ECU | [PMR ECU](../../pmr.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | PMR |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 14 |

## Signals of PMR_alertMatrix2

Tesla Model 3 / Model Y CAN bus signals in `PMR_alertMatrix2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PMR_a080_exceptionPrefetchAbort` | PMR ECU: a080 exception prefetch abort | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a081_exceptionDataAbort` | PMR ECU: a081 exception data abort | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a082_exceptionDataAbort2` | PMR ECU: a082 exception data abort2 | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a083_ahbWriteError` | PMR ECU: a083 ahb write error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a084_exceptionMpuFirewall` | PMR ECU: a084 exception mpu firewall | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a086_exceptionUndefinedInstruction` | PMR ECU: a086 exception undefined instruction | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a092_xtalOscillator` | PMR ECU: a092 xtal oscillator | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a094_safetyICWarn` | PMR ECU: a094 safety IC warn | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a095_safetyICFault` | PMR ECU: a095 safety IC fault | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a096_safetyICDebug` | PMR ECU: a096 safety IC debug | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a097_lowFlowAlmostTripped` | PMR ECU: a097 low flow almost tripped | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a100_diTraceInfo1` | PMR ECU: a100 di trace info1 | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a101_hwVoltageMonitorTrip` | PMR ECU: a101 hw voltage monitor trip | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMR_a121_unintendedReset2` | PMR ECU: a121 unintended reset2 | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All PMR ECU messages (PMR)](../../pmr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
