---
layout: default
title: "UI_alertMatrix3 (0x125) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 ETH"
description: "Touchscreen user interface computer message: alert matrix3. Ethernet-side message UI_alertMatrix3 of Touchscreen user interface computer for Tesla Model Y firmware 2025.20.8, 63 signals (UI_a129_dgpuOperationFailure, UI_a130_QtCarClusterExitError, UI_a131_DisplayPortFailure, UI_a132_AdspWatchdogRecoveryTriggered and 59 more). Bit layout, scaling, units and value tables."
---

# UI_alertMatrix3 (0x125) — Touchscreen user interface computer, Tesla Model Y 2025.20.8 ETH

Touchscreen user interface computer message: alert matrix3. This page documents the 63 signals of UI_alertMatrix3 as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_alertMatrix3` |
| Ethernet-side id | 0x125 (293) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 63 |

## Signals of UI_alertMatrix3

Tesla Model Y CAN bus signals in `UI_alertMatrix3`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_a129_dgpuOperationFailure` | Touchscreen user interface computer: a129 dgpu operation failure | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a130_QtCarClusterExitError` | Signal reported by Touchscreen user interface computer | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a131_DisplayPortFailure` | Touchscreen user interface computer: a131 display port failure | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a132_AdspWatchdogRecoveryTriggered` | Touchscreen user interface computer: a132 adsp watchdog recovery triggered | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a133_AdspWatchdogRecoveryFailed` | Touchscreen user interface computer: a133 adsp watchdog recovery failed | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a134_DashcamUsbDriveNoMedium` | Touchscreen user interface computer: a134 dashcam usb drive no medium | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a135_warnRunOverlayExists` | Touchscreen user interface computer: a135 warn run overlay exists | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a136_warnSettingsConfExists` | Touchscreen user interface computer: a136 warn settings conf exists | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a137_ServiceShellActiveConnection` | Touchscreen user interface computer: a137 service shell active connection | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a138_applyingConfigChange` | Touchscreen user interface computer: a138 applying config change | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a139_postponedConfigChange` | Touchscreen user interface computer: a139 postponed config change | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a140_NeverSleepActive` | Touchscreen user interface computer: a140 never sleep active | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a141_falconDoorOpen` | Touchscreen user interface computer: a141 falcon door open | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a142_CorrectableMemoryError` | Touchscreen user interface computer: a142 correctable memory error | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a143_FPSCrawling` | Touchscreen user interface computer: a143 FPS crawling | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a144_nvmeWarning` | Touchscreen user interface computer: a144 nvme warning | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a145_nvmeUnsafeShutdown` | Touchscreen user interface computer: a145 nvme unsafe shutdown | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a146_nvmeNeedsReplacement` | Touchscreen user interface computer: a146 nvme needs replacement | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a147_ASILGlobalError` | Touchscreen user interface computer: a147 ASIL global error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a148_SleepFailure` | Touchscreen user interface computer: a148 sleep failure | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a149_DisplayCheckFailure` | Touchscreen user interface computer: a149 display check failure | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a150_infoCPURunningHot` | Touchscreen user interface computer: a150 info CPU running hot | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a151_carComputerThermalProblem` | Touchscreen user interface computer: a151 car computer thermal problem | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a152_infoThrottling` | Touchscreen user interface computer: a152 info throttling | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a153_serviceRestarted` | Touchscreen user interface computer: a153 service restarted | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a154_AudiodBufferError` | Touchscreen user interface computer: a154 audiod buffer error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a155_UsbFrontHubUnavailable` | Touchscreen user interface computer: a155 usb front hub unavailable | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a156_UsbFrontHubInstallMismatch` | Touchscreen user interface computer: a156 usb front hub install mismatch | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a157_MCUActiveCoolingRequested` | Touchscreen user interface computer: a157 MCU active cooling requested | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a158_UsbDeviceMountError` | Touchscreen user interface computer: a158 usb device mount error | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a159_AudioHeartbeatFailure` | Touchscreen user interface computer: a159 audio heartbeat failure | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a160_SystemWatchdogFailure` | Touchscreen user interface computer: a160 system watchdog failure | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a161_ECallTemporarilyUnavailable` | Touchscreen user interface computer: a161 e call temporarily unavailable | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a162_voiceRecClipsUploaded` | Touchscreen user interface computer: a162 voice rec clips uploaded | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a163_QtCarVehicleExitError` | Signal reported by Touchscreen user interface computer | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a164_AudiodConnTimeout` | Touchscreen user interface computer: a164 audiod conn timeout | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a165_fsCorrupted` | Touchscreen user interface computer: a165 fs corrupted | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a166_fsError` | Touchscreen user interface computer: a166 fs error | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a167_CgroupOverMemKill` | Touchscreen user interface computer: a167 cgroup over mem kill | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a168_dgpuPowerOnSelfTestFailure` | Touchscreen user interface computer: a168 dgpu power on self test failure | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a169_SteamLoadShedFailure` | Touchscreen user interface computer: a169 steam load shed failure | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a170_AMDdGPULoadShedFailure` | Touchscreen user interface computer: a170 AM dd GPU load shed failure | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a171_GraphicsLoadShedRequested` | Touchscreen user interface computer: a171 graphics load shed requested | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a172_GraphicsLoadShedUIFailure` | Touchscreen user interface computer: a172 graphics load shed UI failure | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a173_pmSuspendFailure` | Touchscreen user interface computer: a173 pm suspend failure | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a174_HistorySaveLoop` | Touchscreen user interface computer: a174 history save loop | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a176_CellularAntennaAlert` | Touchscreen user interface computer: a176 cellular antenna alert | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a177_MediaPlayerFailure` | Touchscreen user interface computer: a177 media player failure | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a178_irqDisabled` | Touchscreen user interface computer: a178 irq disabled | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a179_TestDriveVideoDownloadFailure` | Touchscreen user interface computer: a179 test drive video download failure | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a180_AudiodInputRestarted` | Touchscreen user interface computer: a180 audiod input restarted | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a181_ModemFirmwareVersionMismatch` | Touchscreen user interface computer: a181 modem firmware version mismatch | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a182_VideoPipelineOverrun` | Touchscreen user interface computer: a182 video pipeline overrun | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a183_DDAWFaulted` | Touchscreen user interface computer: a183 DDAW faulted | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a184_ISAFaulted` | Touchscreen user interface computer: a184 ISA faulted | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a185_ELKSDisabled` | Touchscreen user interface computer: a185 ELKS disabled | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a186_ELKSUnavailable` | Touchscreen user interface computer: a186 ELKS unavailable | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a187_TunerFirmwareMismatchedVersion` | Touchscreen user interface computer: a187 tuner firmware mismatched version | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a188_TunerFirmwareMismatchedAPI` | Touchscreen user interface computer: a188 tuner firmware mismatched API | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a189_TunerWatchdogReset` | Touchscreen user interface computer: a189 tuner watchdog reset | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a190_TunerMIA` | Touchscreen user interface computer: a190 tuner MIA | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a191_TunerUpdateFailed` | Touchscreen user interface computer: a191 tuner update failed | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a192_AudioWatchdogReboot` | Touchscreen user interface computer: a192 audio watchdog reboot | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
