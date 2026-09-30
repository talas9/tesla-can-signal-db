---
layout: default
title: "ADSP_state (0x567) — Audio amplifier, Tesla Model Y 2026.26.6.5 CH CAN"
description: "Audio amplifier message: state. Tesla Model Y CAN bus message ADSP_state (0x567) of Audio amplifier, firmware 2026.26.6.5, 26 signals (ADSP_a2baState, ADSP_a2bbState, ADSP_baseamp0State, ADSP_baseamp1State and 22 more). Bit layout, scaling, units and value tables."
---

# ADSP_state (0x567) — Audio amplifier, Tesla Model Y 2026.26.6.5 CH CAN

Audio amplifier message: state; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 26 signals of ADSP_state as defined for Tesla Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `ADSP_state` |
| CAN id | 0x567 (1383) |
| ECU | [Audio amplifier](../../adsp.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 200 ms |
| Signals | 26 |

## Signals of ADSP_state

Tesla Model Y CAN bus signals in `ADSP_state`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `ADSP_a2baState` | Reports the state of the Automotive Audio Bus A (A2B-A) network. | 0\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `INIT`<br>1 = `DOWN`<br>2 = `RESTART`<br>3 = `DISCOVER`<br>4 = `DISCOVER_WAIT`<br>5 = `IDLE`<br>6 = `DIAG`<br>7 = `DISCOVER_RETRY`<br>8 = `GOING_DOWN`<br>9 = `NODE_TEST`<br>10 = `EXT_REQ`<br>11 = `BUS_IDLE`<br>12 = `BUS_ECALL`<br>13 = `COMMAND_STOP`<br>14 = `COMMAND_START`<br>15 = `BUS_DOWN`<br>16 = `REDISCOVER_RETRY_WAIT`<br>17 = `BUS_PARTIAL`<br>18 = `PRE_IDLE`<br>19 = `INTERRUPT` | validated |
| `ADSP_a2bbState` | Reports the state of the Automotive Audio Bus B (A2B-B) network. | 8\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `INIT`<br>1 = `DOWN`<br>2 = `RESTART`<br>3 = `DISCOVER`<br>4 = `DISCOVER_WAIT`<br>5 = `IDLE`<br>6 = `DIAG`<br>7 = `DISCOVER_RETRY`<br>8 = `GOING_DOWN`<br>9 = `NODE_TEST`<br>10 = `EXT_REQ`<br>11 = `BUS_IDLE`<br>12 = `BUS_ECALL`<br>13 = `COMMAND_STOP`<br>14 = `COMMAND_START`<br>15 = `BUS_DOWN`<br>16 = `REDISCOVER_RETRY_WAIT`<br>17 = `BUS_PARTIAL`<br>18 = `PRE_IDLE`<br>19 = `INTERRUPT` | validated |
| `ADSP_baseamp0State` | Audio amplifier: baseamp0 state | 13\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INIT`<br>1 = `CONFIGURED`<br>2 = `ENABLED`<br>3 = `HALT`<br>4 = `TURN_OFF`<br>5 = `OFF`<br>6 = `DIAG`<br>7 = `LDSHD_SELF_TEST` | validated |
| `ADSP_baseamp1State` | Audio amplifier: baseamp1 state | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INIT`<br>1 = `CONFIGURED`<br>2 = `ENABLED`<br>3 = `HALT`<br>4 = `TURN_OFF`<br>5 = `OFF`<br>6 = `DIAG`<br>7 = `LDSHD_SELF_TEST` | validated |
| `ADSP_baseamp2State` | Audio amplifier: baseamp2 state | 19\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INIT`<br>1 = `CONFIGURED`<br>2 = `ENABLED`<br>3 = `HALT`<br>4 = `TURN_OFF`<br>5 = `OFF`<br>6 = `DIAG`<br>7 = `LDSHD_SELF_TEST` | validated |
| `ADSP_baseamp3State` | Audio amplifier: baseamp3 state | 24\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INIT`<br>1 = `CONFIGURED`<br>2 = `ENABLED`<br>3 = `HALT`<br>4 = `TURN_OFF`<br>5 = `OFF`<br>6 = `DIAG`<br>7 = `LDSHD_SELF_TEST` | validated |
| `ADSP_audioReady` | Audio is ready | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `ADSP_extSpkCheckRan` | True once the external speaker diagnostic check (check_diag_result) has run on this boot. Stays false on platforms without CONFIG_EXTSPK_CHECK. | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `ADSP_tcuI2SEnabled` | Reports whether the Telematics Control Unit (TCU) Integrated-circuit Sound (I2S) clock is enabled. | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `ADSP_telephonyRxMute` | Reports the telephony receive mute status. | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `ADSP_ancState` | Reports the state of the Active Noise Canceling (ANC) Digital Signal Processing (DSP). | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `INIT`<br>1 = `DSP_OFF`<br>2 = `DSP_ON`<br>3 = `ENABLED`<br>4 = `DISABLED` | validated |
| `ADSP_sourceSelect` | Reports the current audio source. | 35\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `MEDIA`<br>1 = `TUNER`<br>2 = `SINE`<br>3 = `PINK` | validated |
| `ADSP_tunerSelect` | Audio amplifier: tuner select | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FM`<br>1 = `XM` | validated |
| `ADSP_ancMode` | Reports the Active Noise Cancelling (ANC) mode. | 38\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `OFF`<br>1 = `FRONT`<br>2 = `REAR`<br>3 = `ALL`<br>4 = `CALIBRATING_00`<br>5 = `DISABLED_REASON_A2BA`<br>6 = `DISABLED_REASON_A2BB`<br>7 = `DISABLED_REASON_CLOSURE_OPEN`<br>8 = `DISABLED_REASON_HVAC`<br>9 = `DISABLED_REASON_SEAT_MOVING`<br>10 = `DISABLED_REASON_REAR_OCCUPANT`<br>11 = `DISABLED_REASON_WINDOW_OPEN`<br>12 = `DISABLED_REASON_PARKED`<br>13 = `DISABLED_REASON_ACCELS`<br>14 = `DISABLED_REASON_DOOR_OPEN`<br>15 = `DISABLED_REASON_FRUNK_OPEN`<br>16 = `DISABLED_REASON_MUSIC_LOUD`<br>17 = `DISABLED_REASON_SENSOR_IMBALANCE`<br>18 = `CALIBRATING_20`<br>19 = `CALIBRATING_40`<br>20 = `CALIBRATING_60`<br>21 = `CALIBRATING_80`<br>22 = `UNKNOWN` | validated |
| `ADSP_spkMuteAll` | Reports when all audio speakers are muted. | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `ADSP_eCall_ENS_state` | ADSP-ECALL-ENS state | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKOWN`<br>1 = `SIGNAL_ERROR`<br>2 = `SOURCE_MISSING`<br>3 = `SOURCE_ERROR`<br>4 = `EMERGENCY`<br>5 = `NORMAL` | validated |
| `ADSP_eCallSelfTest` | eCall seft-test result | 47\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_RUN_YET`<br>1 = `PASSED`<br>2 = `FAILED` | validated |
| `ADSP_eCallState` | eCall State | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `INACTIVE`<br>1 = `ACTIVE` | validated |
| `ADSP_allAudioReady` | Reports when all audio peripherals are ready. | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `ADSP_callState` | Reports the current call state. | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `ADSP_telephonyTxMute` | Reports the telephony transmit mute status. | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `ADSP_eCallMicrophoneStatus` | status of microphone | 53\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_RUN_YET`<br>1 = `PASSED`<br>2 = `FAILED` | validated |
| `ADSP_eCallSpeakerStatus` | status of eCall speakers | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_RUN_YET`<br>1 = `PASSED`<br>2 = `FAILED_DISCONNECT`<br>3 = `FAILED_DIAG` | validated |
| `ADSP_a2baLoadShedded` | Audio amplifier: a2ba load shedded | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `ADSP_requestFailoverSpeaker` | Reports requests for failover speaker for chimes. | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `FALSE`<br>1 = `TRUE` | validated |
| `ADSP_microphoneDataState` | Audio amplifier: microphone data state | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `VALID`<br>1 = `A2B_DOWN` | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/ModelY/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/CH.json)

## See also

- [All Audio amplifier messages (ADSP)](../../adsp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
