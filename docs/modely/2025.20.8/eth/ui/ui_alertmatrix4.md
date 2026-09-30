---
layout: default
title: "UI_alertMatrix4 (0x126) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 ETH"
description: "Touchscreen user interface computer message: alert matrix4. Ethernet-side message UI_alertMatrix4 of Touchscreen user interface computer for Tesla Model Y firmware 2025.20.8, 47 signals (UI_a193_TcuRNandFwVersionMismatch, UI_a194_AudioweaverRestarted, UI_a195_gtwMfdUdpApiFired, UI_a196_AMDI2C3BusInoperable and 43 more). Bit layout, scaling, units and value tables."
---

# UI_alertMatrix4 (0x126) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 ETH

Touchscreen user interface computer message: alert matrix4. This page documents the 47 signals of UI_alertMatrix4 as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_alertMatrix4` |
| Ethernet-side id | 0x126 (294) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 47 |

## Signals of UI_alertMatrix4

Tesla Model Y CAN bus signals in `UI_alertMatrix4`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_a193_TcuRNandFwVersionMismatch` | Touchscreen user interface computer: a193 tcu r nand fw version mismatch | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a194_AudioweaverRestarted` | Touchscreen user interface computer: a194 audioweaver restarted | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a195_gtwMfdUdpApiFired` | Touchscreen user interface computer: a195 gtw mfd udp api fired | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a196_AMDI2C3BusInoperable` | Touchscreen user interface computer: a196 AMDI2 C3 bus inoperable | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a197_AMDI2C1BusInoperable` | Touchscreen user interface computer: a197 AMDI2 C1 bus inoperable | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a198_IncompatibleBTUSBHubHardware` | Touchscreen user interface computer: a198 incompatible BTUSB hub hardware | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a199_HighAPedalDetectedAtCollision` | Touchscreen user interface computer: a199 high a pedal detected at collision | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a200_UIFirmwareVersionMismatch` | Touchscreen user interface computer: a200 UI firmware version mismatch | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a201_rearDisplayDisconnected` | Touchscreen user interface computer: a201 rear display disconnected | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a202_sysMemoryIncorrect` | Touchscreen user interface computer: a202 sys memory incorrect | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a204_ModemSleepFailure` | Touchscreen user interface computer: a204 modem sleep failure | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a205_ModemSleepSignalMismatch` | Touchscreen user interface computer: a205 modem sleep signal mismatch | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a206_ModemMIAAfterWake` | Touchscreen user interface computer: a206 modem MIA after wake | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a207_mqttClientDisconnected` | Touchscreen user interface computer: a207 mqtt client disconnected | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a208_mqttDisconnectReason` | Touchscreen user interface computer: a208 mqtt disconnect reason | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a209_dataCallDisconnected` | Touchscreen user interface computer: a209 data call disconnected | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a210_CellularCSRegFail` | Touchscreen user interface computer: a210 cellular CS reg fail | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a211_AEBSDisabled` | Touchscreen user interface computer: a211 AEBS disabled | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a212_AEBSFaulted` | Touchscreen user interface computer: a212 AEBS faulted | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a213_ISADisabled` | Touchscreen user interface computer: a213 ISA disabled | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a214_pmHelperFailure` | Touchscreen user interface computer: a214 pm helper failure | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a215_compositorStallDetected` | Touchscreen user interface computer: a215 compositor stall detected | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a216_AudioA2bCircuitProblem` | Touchscreen user interface computer: a216 audio a2b circuit problem | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a217_CgroupMemoryPressure` | Touchscreen user interface computer: a217 cgroup memory pressure | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a218_AudiodNoAudioDevices` | Touchscreen user interface computer: a218 audiod no audio devices | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a219_CompositorWatchdog` | Touchscreen user interface computer: a219 compositor watchdog | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a220_MediaBrowseError` | Touchscreen user interface computer: a220 media browse error | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a221_NavigationServiceError` | Touchscreen user interface computer: a221 navigation service error | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a222_QtCarRestart` | Signal reported by Touchscreen user interface computer | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a223_databaseError` | Touchscreen user interface computer: a223 database error | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a224_centerDisplayDisconnected` | Touchscreen user interface computer: a224 center display disconnected | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a225_clusterDisplayDisconnected` | Touchscreen user interface computer: a225 cluster display disconnected | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a226_largePhoneContactSync` | Touchscreen user interface computer: a226 large phone contact sync | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a228_pipewireXrunBurst` | Touchscreen user interface computer: a228 pipewire xrun burst | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a229_SerDesError` | Touchscreen user interface computer: a229 ser des error | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a230_ModemSimCardMismatch` | Touchscreen user interface computer: a230 modem sim card mismatch | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a231_SleepCancelled` | Touchscreen user interface computer: a231 sleep cancelled | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a232_processExitError` | Touchscreen user interface computer: a232 process exit error | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a233_ModemRFFailure` | Touchscreen user interface computer: a233 modem RF failure | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a234_AMDI2C0Timeout` | Touchscreen user interface computer: a234 AMDI2 C0 timeout | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a235_AMDI2C1Timeout` | Touchscreen user interface computer: a235 AMDI2 C1 timeout | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a236_ModemOnResetState` | Touchscreen user interface computer: a236 modem on reset state | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a237_ClipUploadActive` | Touchscreen user interface computer: a237 clip upload active | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a238_ModemConfigMismatch` | Touchscreen user interface computer: a238 modem config mismatch | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a239_stateOfVehiclesFunctionsFeedback` | Touchscreen user interface computer: a239 state of vehicles functions feedback | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a240_ethError` | Touchscreen user interface computer: a240 eth error | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a241_AxCPError` | Touchscreen user interface computer: a241 ax CP error | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
