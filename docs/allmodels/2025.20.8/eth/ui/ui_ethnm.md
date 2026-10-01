---
layout: default
title: "UI_ethNm (0x473) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Touchscreen user interface computer message: eth nm. Ethernet-side message UI_ethNm of Touchscreen user interface computer for Tesla Model 3 / Model Y firmware 2025.20.8, 3 signals (UI_nmGoingToSleep, UI_nmKeepAwakeReason, UI_wakeupTime). Bit layout, scaling, units and value tables."
---

# UI_ethNm (0x473) — Touchscreen user interface computer, Tesla Model 3 / Model Y 2025.20.8 ETH

Touchscreen user interface computer message: eth nm. This page documents the 3 signals of UI_ethNm as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_ethNm` |
| Ethernet-side id | 0x473 (1139) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 3 |

## Signals of UI_ethNm

Tesla Model 3 / Model Y CAN bus signals in `UI_ethNm`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_nmGoingToSleep` | Touchscreen user interface computer: nm going to sleep | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_nmKeepAwakeReason` | reason UI is being kept awake; raw 0 = signal not available (SNA) | 16\|5 | little-endian | unsigned | 1 | 0 |  | 1 to 31 | 0 = `UI_KEEPAWAKE_REASON_NONE_SNA`<br>1 = `UI_KEEPAWAKE_REASON_KEEPALIVEACTIVE`<br>2 = `UI_KEEPAWAKE_REASON_GUI_NEVER_SLEEP_SET`<br>3 = `UI_KEEPAWAKE_REASON_PM_CHECKING`<br>4 = `UI_KEEPAWAKE_REASON_UNKNOWN_REMOTE_REQUEST`<br>5 = `UI_KEEPAWAKE_REASON_MODEM_RESET`<br>6 = `UI_KEEPAWAKE_REASON_UPDATER`<br>7 = `UI_KEEPAWAKE_REASON_HERMES`<br>8 = `UI_KEEPAWAKE_REASON_AUTOFUSER`<br>9 = `UI_KEEPAWAKE_REASON_UPDATE_COUNTDOWN`<br>10 = `UI_KEEPAWAKE_REASON_ECALL_ACTIVE`<br>11 = `UI_KEEPAWAKE_REASON_SELFTEST`<br>12 = `UI_KEEPAWAKE_REASON_SENTRY_MODE`<br>13 = `UI_KEEPAWAKE_REASON_MEDIA_DOWNLOAD`<br>14 = `UI_KEEPAWAKE_REASON_ODIN`<br>15 = `UI_KEEPAWAKE_REASON_USER_NOTIFICATION_TIMER`<br>16 = `UI_KEEPAWAKE_REASON_UI_HVAC_REQUEST`<br>17 = `UI_KEEPAWAKE_REASON_CHARGING`<br>18 = `UI_KEEPAWAKE_REASON_STEAM`<br>19 = `UI_KEEPAWAKE_REASON_UI_REQUEST_AP_KEEPALIVE`<br>20 = `UI_KEEPAWAKE_REASON_URGENT_UPLOAD`<br>21 = `UI_KEEPAWAKE_REASON_DIAG_VITALS`<br>22 = `UI_KEEPAWAKE_REASON_VEHICLE_DATA`<br>23 = `UI_KEEPAWAKE_REASON_FIRMWARE_HANDSHAKE`<br>24 = `UI_KEEPAWAKE_REASON_WAKE_UP`<br>25 = `UI_KEEPAWAKE_REASON_MOTHERSHIP_SMS_YOUVE_GOT_MAIL`<br>26 = `UI_KEEPAWAKE_REASON_MOTHERSHIP_SMS_VEHICLE_TASK`<br>27 = `UI_KEEPAWAKE_REASON_MOTHERSHIP_SMS_GARAGE_WAKE_UP`<br>28 = `UI_KEEPAWAKE_REASON_MOTHERSHIP_SMS_OWNER_WAKE_UP`<br>29 = `UI_KEEPAWAKE_REASON_GET_VEHICLE_CONFIGURATION`<br>30 = `UI_KEEPAWAKE_REASON_WINDOW_CONTROL`<br>31 = `UI_KEEPAWAKE_REASON_AUTO_CONDITIONING_START` | plausible |
| `UI_wakeupTime` | Unix epoch time at which vehicle should wake for scheduled charge or update. | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
