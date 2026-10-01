---
layout: default
title: "UI_status2 (0x3DF) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 ETH"
description: "Touchscreen user interface computer message: status2. Ethernet-side message UI_status2 of Touchscreen user interface computer for Tesla Model 3 firmware 2025.20.8, 21 signals (UI_mobileAppStepCount, UI_userRequestSnapshot, UI_touchDetected, UI_validDeviceForEUSummon and 17 more). Bit layout, scaling, units and value tables."
---

# UI_status2 (0x3DF) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 ETH

Touchscreen user interface computer message: status2. This page documents the 21 signals of UI_status2 as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_status2` |
| Ethernet-side id | 0x3DF (991) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 8 bytes |
| Cycle time | 500 ms |
| Signals | 21 |

## Signals of UI_status2

Tesla Model 3 CAN bus signals in `UI_status2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_mobileAppStepCount` | Touchscreen user interface computer: mobile app step count | 0\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | plausible |
| `UI_userRequestSnapshot` | Touchscreen user interface computer: user request snapshot | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_touchDetected` | Touchscreen user interface computer: touch detected | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_validDeviceForEUSummon` | Touchscreen user interface computer: valid device for EU summon | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_locatedAtHome` | Touchscreen user interface computer: located at home | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_locatedAtWork` | Touchscreen user interface computer: located at work | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_locatedAtFavorite` | Touchscreen user interface computer: located at favorite | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_displayInDarkMode` | Touchscreen user interface computer: display in dark mode | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_userActivity` | Indicates user interaction with the center display | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `USER_IDLE`<br>1 = `USER_ACTIVE` | plausible |
| `UI_activeTouchPoints` | Quantity of active touch points on the Center Display | 24\|8 | little-endian | unsigned | 1 | 0 | 1 | 0 to 255 |  | plausible |
| `UI_linkState` | Connectivity link state | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `LINK_STATE_NONE`<br>1 = `LINK_STATE_CELL`<br>2 = `LINK_STATE_WIFI` | plausible |
| `UI_sentryModeState` | Touchscreen user interface computer: sentry mode state; raw 6 = signal not available (SNA) | 34\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OFF`<br>1 = `IDLE`<br>2 = `ARMED`<br>3 = `AWARE`<br>4 = `PANIC`<br>5 = `QUIET`<br>6 = `SNA` | plausible |
| `UI_autopilotSentryRequest` | whether AP sentry mode should be enabled | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_mobileAppConnected` | Reports if Web Real-Time Communication (WebRTC) connection is connected while summon screen is open on the mobile app. | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_CONNECTED`<br>1 = `CONNECTED` | plausible |
| `UI_autoshiftDRState` | Reports the User Interface (UI) autoshift Drive/Reverse state. | 40\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `AUTOSHIFT_DR_STATE_INACTIVE`<br>1 = `AUTOSHIFT_DR_STATE_PROMPT_SHOWING_UNCONFIRMED`<br>2 = `AUTOSHIFT_DR_STATE_ONLY_BRAKE_CONFIRMED`<br>3 = `AUTOSHIFT_DR_STATE_ONLY_STEERING_CONFIRMED`<br>4 = `AUTOSHIFT_DR_STATE_BRAKE_STEERING_AND_BRAKE_CONFIRMED`<br>5 = `AUTOSHIFT_DR_STATE_BRAKE_GEAR_SHIFT_CONFIRMED_R`<br>6 = `AUTOSHIFT_DR_STATE_BRAKE_GEAR_SHIFT_CONFIRMED_D` | plausible |
| `UI_wifiBtModuleType` | Reports the type of Wi-Fi and Bluetooth (BT) module. | 43\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `QCA6595`<br>2 = `BCM4359`<br>3 = `TCU4G`<br>4 = `ELEKTRA` | plausible |
| `UI_sohHealthStatus` | Touchscreen user interface computer: soh health status | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `NO_INTERNET`<br>2 = `REDUCED`<br>3 = `OK` | plausible |
| `UI_selfParkState` | Reports the auto park state changes; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 254 | 0 = `SELF_PARK_DISABLED`<br>1 = `SELF_PARK_DRIVING`<br>2 = `SELF_PARK_IDLE`<br>3 = `SELF_PARK_UNAVAILABLE`<br>4 = `SELF_PARK_UNAVAILABLE_NOT_PARKED`<br>5 = `SELF_PARK_UNAVAILABLE_PLUGGED_IN`<br>6 = `SELF_PARK_UNAVAILABLE_FRUNK_OPEN`<br>7 = `SELF_PARK_UNAVAILABLE_TRUNK_OPEN`<br>8 = `SELF_PARK_UNAVAILABLE_DOOR_OPEN`<br>9 = `SELF_PARK_UNAVAILABLE_PARKED_TOO_LONG`<br>10 = `SELF_PARK_UNAVAILABLE_ON_PUBLIC_ROAD`<br>11 = `SELF_PARK_UNAVAILABLE_LV_BUS_SUPPORT_ISSUE`<br>12 = `SELF_PARK_UNAVAILABLE_AUTOSTEER_NOT_ENABLED`<br>13 = `SELF_PARK_UNAVAILABLE_PARK_SENSOR_ISSUE`<br>14 = `SELF_PARK_UNAVAILABLE_KEY_FOB_NOT_DETECTED`<br>15 = `SELF_PARK_UNAVAILABLE_KEY_FOB_BATTERY_LOW`<br>16 = `SELF_PARK_UNAVAILABLE_TRAILER_MODE`<br>17 = `SELF_PARK_UNAVAILABLE_ROAD_GRADE`<br>18 = `SELF_PARK_UNAVAILABLE_BRAKE_PRESSED`<br>19 = `SELF_PARK_UNAVAILABLE_NO_BLUETOOTH_DEVICES_PAIRED`<br>20 = `SELF_PARK_UNAVAILABLE_WAKEUP_TIMEOUT`<br>21 = `SELF_PARK_UNAVAILABLE_BLUETOOTH_CONNECT_TIMEOUT`<br>22 = `SELF_PARK_UNAVAILABLE_GAME_MODE`<br>23 = `SELF_PARK_UNAVAILABLE_DOG_MODE`<br>24 = `SELF_PARK_UNAVAILABLE_SERVICE_MODE`<br>25 = `SELF_PARK_UNAVAILABLE_TRACK_MODE`<br>26 = `SELF_PARK_UNAVAILABLE_DRAG_STRIP_MODE`<br>27 = `SELF_PARK_UNAVAILABLE_CRASH_STATE`<br>28 = `SELF_PARK_UNAVAILABLE_CAR_ALARM`<br>29 = `SELF_PARK_UNAVAILABLE_CAR_WASH_MODE`<br>30 = `SELF_PARK_CONNECTING_BLUETOOTH`<br>31 = `SELF_PARK_WAKE_UP_BUSES`<br>32 = `SELF_PARK_DETECT_KEY_FOB`<br>33 = `SELF_PARK_TURN_ON_DRIVE_RAIL`<br>34 = `SELF_PARK_PREPRIMED`<br>35 = `SELF_PARK_PRIMED`<br>36 = `SELF_PARK_NOT_STARTED_TIMEOUT`<br>37 = `SELF_PARK_STARTED_FORWARD`<br>38 = `SELF_PARK_STARTED_REVERSE`<br>39 = `SELF_PARK_ACTIVE`<br>40 = `SELF_PARK_OPEN_GATE`<br>41 = `SELF_PARK_OBSTACLE_CLEARED`<br>42 = `SELF_PARK_OBSTACLE_NOT_CLEARED`<br>43 = `SELF_PARK_REMOTE_ABORT`<br>44 = `SELF_PARK_CANCEL_AUTO_SUMMON`<br>45 = `SELF_PARK_POST_ACTIVE_SUCCESS`<br>46 = `SELF_PARK_POST_ACTIVE_FAILURE`<br>47 = `SELF_PARK_DI_PANIC`<br>48 = `SELF_PARK_DV_MISMATCH`<br>49 = `SELF_PARK_PAUSE`<br>50 = `SELF_PARK_RESUME`<br>51 = `SELF_PARK_REMOTE_PRE_ABORT`<br>52 = `SELF_PARK_USER_PAUSED`<br>255 = `SNA` | plausible |
| `UI_summonDeviceIndex` | Reports which device is being used to control summon. | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DEVICE_0`<br>1 = `DEVICE_1`<br>2 = `DEVICE_2`<br>3 = `UNKNOWN` | plausible |
| `UI_sentryModeCameraDetection` | Touchscreen user interface computer: sentry mode camera detection | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_wakeOnIPActive` | Touchscreen user interface computer: wake on IP active | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
