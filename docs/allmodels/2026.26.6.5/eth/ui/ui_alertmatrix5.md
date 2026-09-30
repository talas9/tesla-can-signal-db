---
layout: default
title: "UI_alertMatrix5 (0x127) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 ETH"
description: "Touchscreen user interface computer message: alert matrix5. Ethernet-side message UI_alertMatrix5 of Touchscreen user interface computer for Tesla Model 3 / Model Y firmware 2026.26.6.5, 16 signals (UI_a257_modemRebooting, UI_a258_sapFailedToPowerOn, UI_a259_sapChannelMismatch, UI_a260_sapWrongChannel and 12 more). Bit layout, scaling, units and value tables."
---

# UI_alertMatrix5 (0x127) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2026.26.6.5 ETH

Touchscreen user interface computer message: alert matrix5. This page documents the 16 signals of UI_alertMatrix5 as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_alertMatrix5` |
| Ethernet-side id | 0x127 (295) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 16 |

## Signals of UI_alertMatrix5

Tesla Model 3 / Model Y CAN bus signals in `UI_alertMatrix5`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_a257_modemRebooting` | Touchscreen user interface computer: a257 modem rebooting | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a258_sapFailedToPowerOn` | Touchscreen user interface computer: a258 sap failed to power on | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a259_sapChannelMismatch` | Touchscreen user interface computer: a259 sap channel mismatch | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a260_sapWrongChannel` | Touchscreen user interface computer: a260 sap wrong channel | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a261_bluetoothStackPanic` | Touchscreen user interface computer: a261 bluetooth stack panic | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a263_ecuLogUploadFailure` | Touchscreen user interface computer: a263 ecu log upload failure | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a264_invalidEpaRange` | Touchscreen user interface computer: a264 invalid epa range | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a265_USBHostControllerUnrecoverable` | Touchscreen user interface computer: a265 USB host controller unrecoverable | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a266_DashcamRecentBufferDurationReduced` | Touchscreen user interface computer: a266 dashcam recent buffer duration reduced | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a272_eapTlsCSRFailure` | Touchscreen user interface computer: a272 eap tls CSR failure | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a273_AudioDbusFailure` | Touchscreen user interface computer: a273 audio dbus failure | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a274_ContextualHintCardEvent` | Touchscreen user interface computer: a274 contextual hint card event | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a275_ADDWFaulted` | Touchscreen user interface computer: a275 ADDW faulted | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a276_PrivateNetworkProfileActive` | Touchscreen user interface computer: a276 private network profile active | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a277_PONRPopupShown` | Touchscreen user interface computer: a277 PONR popup shown | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UI_a278_gpsHwDegraded` | Touchscreen user interface computer: a278 gps hw degraded | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/AllModels/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
