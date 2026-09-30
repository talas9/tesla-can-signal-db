---
layout: default
title: "DIF_status (0x2D5) — Front drive inverter, Tesla Model Y 2026.26.6.5 PARTY CAN"
description: "Front drive inverter message: status. Tesla Model Y CAN bus message DIF_status (0x2D5) of Front drive inverter, firmware 2026.26.6.5, 15 signals (DIF_statusChecksum, DIF_statusCounter, DIF_state, DIF_soptState and 11 more). Bit layout, scaling, units and value tables."
---

# DIF_status (0x2D5) — Front drive inverter, Tesla Model Y 2026.26.6.5 PARTY CAN

Front drive inverter message: status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 15 signals of DIF_status as defined for Tesla Model Y firmware 2026.26.6.5 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DIF_status` |
| CAN id | 0x2D5 (725) |
| ECU | [Front drive inverter](../../dif.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | DIF |
| Frame length | 8 bytes |
| Cycle time | 10 ms |
| Signals | 15 |

## Signals of DIF_status

Tesla Model Y CAN bus signals in `DIF_status`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIF_statusChecksum` | Front drive inverter: status checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `DIF_statusCounter` | Front drive inverter: status counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `DIF_state` | DI unit state machine state. | 12\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DI_STATE_UNAVAILABLE`<br>1 = `DI_STATE_STANDBY`<br>2 = `DI_STATE_FAULT`<br>3 = `DI_STATE_ABORT`<br>4 = `DI_STATE_ENABLE` | validated |
| `DIF_soptState` | Detects the state of the the Switch Off Path Test (SOPT); raw 8 = signal not available (SNA) | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `SOPT_INIT`<br>1 = `SOPT_PSTG_BRING_UP`<br>2 = `SOPT_PSTG_BRING_UP_AT_SPEED`<br>3 = `SOPT_ASC_TEST`<br>4 = `SOPT_CURRENT_TEST`<br>5 = `SOPT_TEST_PASSED`<br>6 = `SOPT_TEST_SKIPPED`<br>7 = `SOPT_TEST_FAILED`<br>8 = `SOPT_SNA`<br>9 = `SOPT_DISABLED` | plausible |
| `DIF_sysLimpRequest` | Front drive inverter: sys limp request | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_softSysLimpRequest` | Front drive inverter: soft sys limp request | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_adState` | Front drive inverter: ad state | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `AD_STATE_STARTUP`<br>1 = `AD_STATE_NORMAL`<br>2 = `AD_STATE_BACKUP`<br>3 = `AD_STATE_FAULTED` | plausible |
| `DIF_lvSupplyV` | Front drive inverter: lv supply v | 24\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | validated |
| `DIF_driveModeState` | Reports the system drive mode state. | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DM_STATE_NONDRIVE`<br>1 = `DM_STATE_DRIVE` | plausible |
| `DIF_wasteState` | Reports the Drive Inverter (DI) waste heat state. | 33\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DI_WASTE_UNAVAILABLE`<br>1 = `DI_WASTE_AVAILABLE`<br>2 = `DI_WASTE_ON`<br>3 = `DI_WASTE_STATIONARY` | plausible |
| `DIF_haltRequest` | Front drive inverter: halt request | 35\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DI_HALT_NONE`<br>1 = `DI_HALT_IMMEDIATE`<br>2 = `DI_HALT_GRACEFUL` | plausible |
| `DIF_axleSpeedLimitRequest` | Front drive inverter: axle speed limit request | 40\|12 | little-endian | unsigned | 1 | 40 | RPM | 40 to 2750 |  | plausible |
| `DIF_adDirection` | Front drive inverter: ad direction | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `AD_BACKWARD`<br>1 = `AD_FORWARD` | plausible |
| `DIF_spinDownLearningState` | Front drive inverter: spin down learning state | 56\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `SPINDOWN_STATE_INIT`<br>1 = `SPINDOWN_STATE_PRECHECK`<br>2 = `SPINDOWN_STATE_WAIT`<br>3 = `SPINDOWN_STATE_ACCELERATE`<br>4 = `SPINDOWN_STATE_COAST`<br>5 = `SPINDOWN_STATE_MEASURE`<br>6 = `SPINDOWN_STATE_CORRECT`<br>7 = `SPINDOWN_STATE_VERIFY`<br>8 = `SPINDOWN_STATE_WRITE`<br>9 = `SPINDOWN_STATE_DONE` | plausible |
| `DIF_spinDownLearningMode` | Front drive inverter: spin down learning mode | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SPINDOWN_MODE_ON_LIFT`<br>1 = `SPINDOWN_MODE_ON_GROUND` | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 PARTY DBC file](../../../../../dbc/ModelY/2026.26.6.5/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/PARTY.json)

## See also

- [All Front drive inverter messages (DIF)](../../dif.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
