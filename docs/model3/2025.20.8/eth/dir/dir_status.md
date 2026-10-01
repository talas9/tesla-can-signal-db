---
layout: default
title: "DIR_status (0x256) — Rear drive inverter, Tesla Model 3 2025.20.8 ETH"
description: "Rear drive inverter message: status. Ethernet-side message DIR_status of Rear drive inverter for Tesla Model 3 firmware 2025.20.8, 16 signals (DIR_statusChecksum, DIR_statusCounter, DIR_state, DIR_keepAliveRequest and 12 more). Bit layout, scaling, units and value tables."
---

# DIR_status (0x256) — Rear drive inverter, Tesla Model 3 2025.20.8 ETH

Rear drive inverter message: status. This page documents the 16 signals of DIR_status as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DIR_status` |
| Ethernet-side id | 0x256 (598) |
| ECU | [Rear drive inverter](../../dir.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DIR |
| Frame length | 7 bytes |
| Cycle time | 10 ms |
| Signals | 16 |

## Signals of DIR_status

Tesla Model 3 CAN bus signals in `DIR_status`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIR_statusChecksum` | Rear drive inverter: status checksum | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `DIR_statusCounter` | Rear drive inverter: status counter | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `DIR_state` | DI unit state machine state. | 12\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DI_STATE_UNAVAILABLE`<br>1 = `DI_STATE_STANDBY`<br>2 = `DI_STATE_FAULT`<br>3 = `DI_STATE_ABORT`<br>4 = `DI_STATE_ENABLE` | plausible |
| `DIR_keepAliveRequest` | Used to detect that the Drive Inverter (DI) expects 12V and High Voltage (HV) to be kept up in order to protect hardware. | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NO_REQUEST`<br>1 = `KEEP_ALIVE` | plausible |
| `DIR_soptState` | Detects the state of the the Switch Off Path Test (SOPT); raw 8 = signal not available (SNA) | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `SOPT_INIT`<br>1 = `SOPT_PSTG_BRING_UP`<br>2 = `SOPT_PSTG_BRING_UP_AT_SPEED`<br>3 = `SOPT_ASC_TEST`<br>4 = `SOPT_CURRENT_TEST`<br>5 = `SOPT_TEST_PASSED`<br>6 = `SOPT_TEST_SKIPPED`<br>7 = `SOPT_TEST_FAILED`<br>8 = `SOPT_SNA`<br>9 = `SOPT_DISABLED` | plausible |
| `DIR_sysLimpRequest` | Rear drive inverter: sys limp request | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_adState` | Rear drive inverter: ad state | 21\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `AD_STATE_STARTUP`<br>1 = `AD_STATE_NORMAL`<br>2 = `AD_STATE_BACKUP`<br>3 = `AD_STATE_FAULTED` | plausible |
| `DIR_driveModeState` | Rear drive inverter: drive mode state | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DM_STATE_NONDRIVE`<br>1 = `DM_STATE_DRIVE` | plausible |
| `DIR_lvSupplyV` | Rear drive inverter: lv supply v | 24\|8 | little-endian | unsigned | 0.1 | 0 | V | 0 to 25.5 |  | plausible |
| `DIR_wasteState` | Reports the Drive Inverter (DI) waste heat state. | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DI_WASTE_UNAVAILABLE`<br>1 = `DI_WASTE_AVAILABLE`<br>2 = `DI_WASTE_ON`<br>3 = `DI_WASTE_STATIONARY` | plausible |
| `DIR_haltRequest` | Rear drive inverter: halt request | 34\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DI_HALT_NONE`<br>1 = `DI_HALT_IMMEDIATE`<br>2 = `DI_HALT_GRACEFUL` | plausible |
| `DIR_axleSpeedLimitRequest` | Rear drive inverter: axle speed limit request | 36\|12 | little-endian | unsigned | 1 | 40 | RPM | 400 to 2750 |  | plausible |
| `DIR_adDirection` | Rear drive inverter: ad direction | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `AD_BACKWARD`<br>1 = `AD_FORWARD` | plausible |
| `DIR_spinDownLearningState` | Rear drive inverter: spin down learning state | 49\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `SPINDOWN_STATE_INIT`<br>1 = `SPINDOWN_STATE_PRECHECK`<br>2 = `SPINDOWN_STATE_WAIT`<br>3 = `SPINDOWN_STATE_ACCELERATE`<br>4 = `SPINDOWN_STATE_COAST`<br>5 = `SPINDOWN_STATE_MEASURE`<br>6 = `SPINDOWN_STATE_CORRECT`<br>7 = `SPINDOWN_STATE_VERIFY`<br>8 = `SPINDOWN_STATE_WRITE`<br>9 = `SPINDOWN_STATE_DONE` | plausible |
| `DIR_spinDownLearningMode` | Rear drive inverter: spin down learning mode | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SPINDOWN_MODE_ON_LIFT`<br>1 = `SPINDOWN_MODE_ON_GROUND` | plausible |
| `DIR_unitRecoveredFromResetAtSpeed` | Rear drive inverter: unit recovered from reset at speed | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Rear drive inverter messages (DIR)](../../dir.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
