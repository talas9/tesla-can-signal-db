---
layout: default
title: "PMF_alertMatrix2 (0x7E6) — PMF ECU, Tesla Model 3 2025.20.8 ETH"
description: "PMF ECU message: alert matrix2. Ethernet-side message PMF_alertMatrix2 of PMF ECU for Tesla Model 3 firmware 2025.20.8, 13 signals (PMF_a080_exceptionPrefetchAbort, PMF_a081_exceptionDataAbort, PMF_a082_exceptionDataAbort2, PMF_a083_ahbWriteError and 9 more). Bit layout, scaling, units and value tables."
---

# PMF_alertMatrix2 (0x7E6) — PMF ECU, Tesla Model 3 2025.20.8 ETH

PMF ECU message: alert matrix2. This page documents the 13 signals of PMF_alertMatrix2 as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `PMF_alertMatrix2` |
| Ethernet-side id | 0x7E6 (2022) |
| ECU | [PMF ECU](../../pmf.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | PMF |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 13 |

## Signals of PMF_alertMatrix2

Tesla Model 3 CAN bus signals in `PMF_alertMatrix2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PMF_a080_exceptionPrefetchAbort` | PMF ECU: a080 exception prefetch abort | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a081_exceptionDataAbort` | PMF ECU: a081 exception data abort | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a082_exceptionDataAbort2` | PMF ECU: a082 exception data abort2 | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a083_ahbWriteError` | PMF ECU: a083 ahb write error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a084_exceptionMpuFirewall` | PMF ECU: a084 exception mpu firewall | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a086_exceptionUndefinedInstruction` | PMF ECU: a086 exception undefined instruction | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a092_xtalOscillator` | PMF ECU: a092 xtal oscillator | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a094_safetyICWarn` | PMF ECU: a094 safety IC warn | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a095_safetyICFault` | PMF ECU: a095 safety IC fault | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a096_safetyICDebug` | PMF ECU: a096 safety IC debug | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a097_lowFlowAlmostTripped` | PMF ECU: a097 low flow almost tripped | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a100_diTraceInfo1` | PMF ECU: a100 di trace info1 | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PMF_a121_unintendedReset2` | PMF ECU: a121 unintended reset2 | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All PMF ECU messages (PMF)](../../pmf.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
