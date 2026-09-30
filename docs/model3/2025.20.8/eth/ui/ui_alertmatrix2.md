---
layout: default
title: "UI_alertMatrix2 (0x124) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 ETH"
description: "Touchscreen user interface computer message: alert matrix2. Ethernet-side message UI_alertMatrix2 of Touchscreen user interface computer for Tesla Model 3 firmware 2025.20.8, 63 signals (UI_a065_WiFiRecoveryReset, UI_a066_GpuHangDetected, UI_a067_WarnOnI915, UI_a068_VideoUnexpectedExit and 59 more). Bit layout, scaling, units and value tables."
---

# UI_alertMatrix2 (0x124) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 ETH

Touchscreen user interface computer message: alert matrix2. This page documents the 63 signals of UI_alertMatrix2 as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_alertMatrix2` |
| Ethernet-side id | 0x124 (292) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 63 |

## Signals of UI_alertMatrix2

Tesla Model 3 CAN bus signals in `UI_alertMatrix2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_a065_WiFiRecoveryReset` | Touchscreen user interface computer: a065 wi fi recovery reset | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a066_GpuHangDetected` | Touchscreen user interface computer: a066 gpu hang detected | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a067_WarnOnI915` | Touchscreen user interface computer: a067 warn on I915 | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a068_VideoUnexpectedExit` | Touchscreen user interface computer: a068 video unexpected exit | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a069_VideoUDPTimeout` | Touchscreen user interface computer: a069 video UDP timeout | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a070_VideoPipelineWarning` | Touchscreen user interface computer: a070 video pipeline warning | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a071_VideoPipelineError` | Touchscreen user interface computer: a071 video pipeline error | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a072_ECallAnalogMicFailed` | Touchscreen user interface computer: a072 e call analog mic failed | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a073_ECallDigitalMicFailed` | Touchscreen user interface computer: a073 e call digital mic failed | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a074_EMMCHangDetected` | Touchscreen user interface computer: a074 EMMC hang detected | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a075_BackupCameraInitError` | Touchscreen user interface computer: a075 backup camera init error | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a076_NumFalseManualECalls` | Touchscreen user interface computer: a076 num false manual e calls | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a077_AudioA2bMicChannelSwap` | Touchscreen user interface computer: a077 audio a2b mic channel swap | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a078_DashcamUsbDriveUnmountable` | Touchscreen user interface computer: a078 dashcam usb drive unmountable | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a079_DashcamUsbDriveFull` | Touchscreen user interface computer: a079 dashcam usb drive full | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a080_DashcamUsbDriveSlow` | Touchscreen user interface computer: a080 dashcam usb drive slow | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a081_CellModemSearchExpired` | Touchscreen user interface computer: a081 cell modem search expired | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a082_NumModemRebootStuckInECall` | Touchscreen user interface computer: a082 num modem reboot stuck in e call | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a083_ECallProxyWatchdogTriggered` | Touchscreen user interface computer: a083 e call proxy watchdog triggered | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a084_SerializerError` | Touchscreen user interface computer: a084 serializer error | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a085_DeserializerError` | Touchscreen user interface computer: a085 deserializer error | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a086_TouchEnumerationError` | Touchscreen user interface computer: a086 touch enumeration error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a087_BmpReset` | Touchscreen user interface computer: a087 bmp reset | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a088_CellRemovableSimMissing` | Touchscreen user interface computer: a088 cell removable sim missing | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a089_RadioSoftResetError` | Touchscreen user interface computer: a089 radio soft reset error | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a090_RadioPingFailError` | Touchscreen user interface computer: a090 radio ping fail error | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a091_VehicleLinkStall` | Touchscreen user interface computer: a091 vehicle link stall | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a092_updateStarted` | Touchscreen user interface computer: a092 update started | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a093_updateEnded` | Touchscreen user interface computer: a093 update ended | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a094_ModemPowerOnFailure` | Touchscreen user interface computer: a094 modem power on failure | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a095_CidStorageRunningLow` | Touchscreen user interface computer: a095 cid storage running low | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a096_VideodPipelineIssueDetected` | Touchscreen user interface computer: a096 videod pipeline issue detected | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a097_AudiodRestarted` | Touchscreen user interface computer: a097 audiod restarted | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a098_DiskCheckFailure` | Touchscreen user interface computer: a098 disk check failure | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a099_eMMCStatusError` | Touchscreen user interface computer: a099 e MMC status error | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a100_eMMCFTLError` | Touchscreen user interface computer: a100 e MMCFTL error | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a101_wifiStackProblem` | Touchscreen user interface computer: a101 wifi stack problem | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a102_A2bDiscoveryFailed` | Touchscreen user interface computer: a102 a2b discovery failed | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a103_UsbHubNotEnumerating` | Touchscreen user interface computer: a103 usb hub not enumerating | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a104_DashcamUsbDriveMissing` | Touchscreen user interface computer: a104 dashcam usb drive missing | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a105_firmwareReinstallRequested` | Touchscreen user interface computer: a105 firmware reinstall requested | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a106_rebootBackstopTriggered` | Touchscreen user interface computer: a106 reboot backstop triggered | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a107_DashcamUsbDriveTooBigForVfatFsck` | Touchscreen user interface computer: a107 dashcam usb drive too big for vfat fsck | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a108_DashcamUsbDriveGettingFull` | Touchscreen user interface computer: a108 dashcam usb drive getting full | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a109_DashcamUsbDriveTooSmall` | Touchscreen user interface computer: a109 dashcam usb drive too small | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a110_DashcamUsbDriveCorrupt` | Touchscreen user interface computer: a110 dashcam usb drive corrupt | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a111_DashcamUsbDriveNotSuperSpeed` | Touchscreen user interface computer: a111 dashcam usb drive not super speed | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a112_badUSBDevice` | Touchscreen user interface computer: a112 bad USB device | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a113_DashcamHasOnboardSentryClips` | Touchscreen user interface computer: a113 dashcam has onboard sentry clips | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a114_drivingVisualizationDegraded` | Touchscreen user interface computer: a114 driving visualization degraded | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a115_IrisEDLMode` | Touchscreen user interface computer: a115 iris EDL mode | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a116_UncorrectableMemoryError` | Touchscreen user interface computer: a116 uncorrectable memory error | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a117_VehicleSelfTestRunning` | Touchscreen user interface computer: a117 vehicle self test running | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a118_NVMeReset` | Touchscreen user interface computer: a118 NV me reset | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a119_nvmeBlockDeviceMissing` | Touchscreen user interface computer: a119 nvme block device missing | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a120_nvmePCIeLinkErrorDetected` | Touchscreen user interface computer: a120 nvme PC ie link error detected | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a121_nvmeSmartLogCritical` | Touchscreen user interface computer: a121 nvme smart log critical | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a122_AMDI2C0LostArbitration` | Touchscreen user interface computer: a122 AMDI2 C0 lost arbitration | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a123_AMDI2C1LostArbitration` | Touchscreen user interface computer: a123 AMDI2 C1 lost arbitration | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a124_AMDI2C0TxRxAborted` | Touchscreen user interface computer: a124 AMDI2 C0 tx rx aborted | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a125_AMDI2C1TxRxAborted` | Touchscreen user interface computer: a125 AMDI2 C1 tx rx aborted | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a126_UsbErrorDriveCorrupt` | Touchscreen user interface computer: a126 usb error drive corrupt | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a128_dgpuNotDetected` | Touchscreen user interface computer: a128 dgpu not detected | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
