---
layout: default
title: "PM_alertMatrix2 (0x380) — PM ECU, Tesla Model Y 2025.20.8 ETH"
description: "PM ECU message: alert matrix2. Ethernet-side message PM_alertMatrix2 of PM ECU for Tesla Model Y firmware 2025.20.8, 39 signals (PM_a066_pmfMIA, PM_a067_pmrMIA, PM_a068_brakePedalMonitor, PM_a069_brakeMonitorsUnhealthy and 35 more). Bit layout, scaling, units and value tables."
---

# PM_alertMatrix2 (0x380) — PM ECU, Tesla Model Y 2025.20.8 ETH

PM ECU message: alert matrix2. This page documents the 39 signals of PM_alertMatrix2 as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `PM_alertMatrix2` |
| Ethernet-side id | 0x380 (896) |
| ECU | [PM ECU](../../pm.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | PM |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 39 |

## Signals of PM_alertMatrix2

Tesla Model Y CAN bus signals in `PM_alertMatrix2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `PM_a066_pmfMIA` | PM ECU: a066 pmf MIA | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a067_pmrMIA` | PM ECU: a067 pmr MIA | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a068_brakePedalMonitor` | PM ECU: a068 brake pedal monitor | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a069_brakeMonitorsUnhealthy` | PM ECU: a069 brake monitors unhealthy | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a070_brakeTorqueSplitMonitorTrip` | PM ECU: a070 brake torque split monitor trip | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a071_baseBrakingMonitor` | PM ECU: a071 base braking monitor | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a072_brakeTorqueCommandInterface` | PM ECU: a072 brake torque command interface | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a073_canDataBusC` | PM ECU: a073 can data bus c | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a074_canHardwareBusC` | PM ECU: a074 can hardware bus c | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a075_canDataBusD` | PM ECU: a075 can data bus d | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a076_canHardwareBusD` | PM ECU: a076 can hardware bus d | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a077_canDataBusE` | PM ECU: a077 can data bus e | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a078_canHardwareBusE` | PM ECU: a078 can hardware bus e | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a079_rcuMIA` | PM ECU: a079 rcu MIA | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a080_exceptionPrefetchAbort` | PM ECU: a080 exception prefetch abort | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a081_exceptionDataAbort` | PM ECU: a081 exception data abort | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a082_exceptionDataAbort2` | PM ECU: a082 exception data abort2 | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a083_ahbWriteError` | PM ECU: a083 ahb write error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a084_exceptionMpuFirewall` | PM ECU: a084 exception mpu firewall | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a085_dpbMIA` | PM ECU: a085 dpb MIA | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a086_exceptionUndefinedInstruction` | PM ECU: a086 exception undefined instruction | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a087_canHardwareBusLIPC` | PM ECU: a087 can hardware bus LIPC | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a092_xtalOscillator` | PM ECU: a092 xtal oscillator | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a093_accelPedalSupply` | PM ECU: a093 accel pedal supply | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a095_ITPMSTimeoutGNSSConvergence` | PM ECU: a095 ITPMS timeout GNSS convergence | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a096_ITPMSConvergedGNSSAbsRadiusTimes` | PM ECU: a096 ITPMS converged GNSS abs radius times | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a098_ITPMSTriggerDebug` | PM ECU: a098 ITPMS trigger debug | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a099_ITPMSCalibrated` | PM ECU: a099 ITPMS calibrated | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a100_diTraceInfo1` | PM ECU: a100 di trace info1 | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a110_indirectTPMSSoftWarningFrontLeft` | PM ECU: a110 indirect TPMS soft warning front left | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a111_indirectTPMSSoftWarningFrontRight` | PM ECU: a111 indirect TPMS soft warning front right | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a112_indirectTPMSSoftWarningRearLeft` | PM ECU: a112 indirect TPMS soft warning rear left | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a113_indirectTPMSSoftWarningRearRight` | PM ECU: a113 indirect TPMS soft warning rear right | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a114_indirectTPMSHardWarningFrontLeft` | PM ECU: a114 indirect TPMS hard warning front left | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a115_indirectTPMSHardWarningFrontRight` | PM ECU: a115 indirect TPMS hard warning front right | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a116_indirectTPMSHardWarningRearLeft` | PM ECU: a116 indirect TPMS hard warning rear left | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a117_indirectTPMSHardWarningRearRight` | PM ECU: a117 indirect TPMS hard warning rear right | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a120_indirectTPMSFaulted` | PM ECU: a120 indirect TPMS faulted | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PM_a121_unintendedReset2` | PM ECU: a121 unintended reset2 | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All PM ECU messages (PM)](../../pm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
