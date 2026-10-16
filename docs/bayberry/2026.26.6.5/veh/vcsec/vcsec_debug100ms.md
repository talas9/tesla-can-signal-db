---
layout: default
title: "VCSEC_debug100ms (0x719) — Vehicle security controller, Tesla Model Y (2025+ / Juniper; community mapping) 2026.26.6.5 VEH CAN"
description: "Vehicle security controller message: debug100ms. Tesla Model Y (2025+ / Juniper; community mapping) CAN bus message VCSEC_debug100ms (0x719) of Vehicle security controller, firmware 2026.26.6.5, 19 signals (VCSEC_debug100msIndex, VCSEC_walkAwayLockKeyState, VCSEC_thresholdOffsetVersion, VCSEC_walkAwayLockState and 15 more). Bit layout, scaling, units and value tables."
---

# VCSEC_debug100ms (0x719) — Vehicle security controller, Tesla Model Y (2025+ / Juniper; community mapping) 2026.26.6.5 VEH CAN

Vehicle security controller message: debug100ms; frame length from the layout, not yet observed on a vehicle bus. This page documents the 19 signals of VCSEC_debug100ms as defined for Tesla Model Y (2025+ / Juniper; community mapping) firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEC_debug100ms` |
| CAN id | 0x719 (1817) |
| ECU | [Vehicle security controller](../../vcsec.md) |
| Vehicle | Tesla Model Y (2025+ / Juniper; community mapping) |
| API name / codename | `Bayberry` |
| Coverage scope | Product-metadata signal subset using the Model 3 / Model Y union routing map; no product-specific CAN routing map or complete vehicle coverage is established. |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCSEC |
| Frame length | 8 bytes |
| Cycle time | 50 ms |
| Signals | 19 |

## Signals of VCSEC_debug100ms

Tesla Model Y (2025+ / Juniper; community mapping) CAN bus signals in `VCSEC_debug100ms`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEC_debug100msIndex` | selector | Vehicle security controller: debug100ms index | 0\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `Mux0`<br>1 = `Mux1`<br>2 = `UHFReceiver`<br>3 = `LastAdvertRSSI`<br>5 = `Mux5`<br>7 = `BLEBondingState`<br>8 = `NIState0`<br>9 = `NIState2`<br>10 = `NIStateRemote`<br>12 = `RoutableDebug`<br>13 = `ProtobufDebug`<br>14 = `NNClassifierDebug`<br>19 = `SerialPortDebug`<br>20 = `BLEDeviceDebug`<br>21 = `ConnectionBenchmark0`<br>22 = `ConnectionBenchmark1`<br>23 = `ConnectionBenchmark2` | plausible |
| `VCSEC_walkAwayLockKeyState` | page 0 | Walk away lock key state of the vehicle | 5\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SECURITY_WALKAWAYLOCKING_KEY_STATE_IDLE`<br>1 = `SECURITY_WALKAWAYLOCKING_KEY_STATE_AWAITING_KEY_LEAVING`<br>2 = `SECURITY_WALKAWAYLOCKING_KEY_WAIT_FOR_NO_KEYS_PRESENT`<br>3 = `SECURITY_WALKAWAYLOCKING_NO_KEYS_PRESENT` | validated |
| `VCSEC_thresholdOffsetVersion` | page 0 | Vehicle security controller: threshold offset version | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 |  | validated |
| `VCSEC_walkAwayLockState` | page 0 | Walk away lock state of the vehicle | 11\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SECURITY_WALKAWAYLOCKING_STATE_IDLE`<br>1 = `SECURITY_WALKAWAYLOCKING_STATE_WALK_AWAY_LOCK_ARMING`<br>2 = `SECURITY_WALKAWAYLOCKING_STATE_WAITING_FOR_KEY_LEAVING`<br>3 = `SECURITY_WALKAWAYLOCKING_STATE_LOCK_DESIRED`<br>4 = `SECURITY_WALKAWAYLOCKING_STATE_DISABLED_DUE_TO_KEY_PRESENT`<br>5 = `SECURITY_WALKAWAYLOCKING_STATE_INHIBITED` | validated |
| `VCSEC_rssi0WLEntry` | page 0 | Whitelist entry of the rssi0 device | 16\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | validated |
| `VCSEC_endpointLayout` | page 0 | Vehicle security controller: endpoint layout | 21\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VCSEC_ENDPOINT_LAYOUT_1`<br>1 = `VCSEC_ENDPOINT_LAYOUT_2`<br>2 = `VCSEC_ENDPOINT_LAYOUT_3` | validated |
| `VCSEC_rssi1WLEntry` | page 0 | Whitelist entry of the rssi1 device | 24\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | validated |
| `VCSEC_rssi2WLEntry` | page 0 | Whitelist entry of the rssi2 device | 32\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | validated |
| `VCSEC_walkUpUnlockState` | page 0 | Status of walk up unlock state | 37\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `WALK_UP_UNLOCK_STATE_IDLE`<br>1 = `WALK_UP_UNLOCK_STATE_ARMING`<br>2 = `WALK_UP_UNLOCK_STATE_AWAITING_KEY`<br>3 = `WALK_UP_UNLOCK_STATE_UNLOCK_DESIRED`<br>4 = `WALK_UP_UNLOCK_STATE_DISABLED` | validated |
| `VCSEC_algoHighThreshLeft` | page 0 | Vehicle security controller: algo high thresh left | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_algoHighThreshRight` | page 0 | Vehicle security controller: algo high thresh right | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_algoHighThreshCenter` | page 0 | Vehicle security controller: algo high thresh center | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_pollingReason` | page 0 | Reason that the vehicle is currently polling for location | 43\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `POLLINGREASON_NONE`<br>1 = `POLLINGREASON_IMMOBILIZER`<br>2 = `POLLINGREASON_PASSIVE_AUTHENTICATION`<br>3 = `POLLINGREASON_PASSIVE_UNLOCK`<br>4 = `POLLINGREASON_WALK_AWAY_LOCK`<br>5 = `POLLINGREASON_WALK_UP_UNLOCK`<br>6 = `POLLINGREASON_ACCESSORY_RAIL`<br>7 = `POLLINGREASON_AUTO_PRESENT_DOOR`<br>8 = `POLLINGREASON_DRIVE_AWAY_CHECK_FOR_KEY`<br>9 = `POLLINGREASON_AUTORELOCK`<br>10 = `POLLINGREASON_AUTO_PRESENT_HANDLES`<br>11 = `POLLINGREASON_APPROACH_LIGHTING`<br>12 = `POLLINGREASON_AUTOPILOT`<br>13 = `POLLINGREASON_MULTIPLE` | validated |
| `VCSEC_numberOfPubKeysOnWhitelist` | page 0 | Number of public keys on keys whitelist. | 48\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 |  | validated |
| `VCSEC_thermalDetectState` | page 0 | Reports the current state of thermal detection. | 53\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VCSEC_THERMALDETECTIONSTATE_DISABLED`<br>1 = `VCSEC_THERMALDETECTIONSTATE_MONITORING`<br>2 = `VCSEC_THERMALDETECTIONSTATE_CONFIRMING_THRESHOLD`<br>3 = `VCSEC_THERMALDETECTIONSTATE_TRIPPED` | validated |
| `VCSEC_chargeHandleMitigationActive` | page 0 | Vehicle security controller: charge handle mitigation active | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_device0Offset` | page 5 | Vehicle security controller: device0 offset | 26\|6 | little-endian | signed | 0.5 | 0 | dBm | -16 to 15.5 |  | validated |
| `VCSEC_device1Offset` | page 5 | Vehicle security controller: device1 offset | 32\|6 | little-endian | signed | 0.5 | 0 | dBm | -16 to 15.5 |  | validated |
| `VCSEC_device2Offset` | page 5 | Vehicle security controller: device2 offset | 40\|6 | little-endian | signed | 0.5 | 0 | dBm | -16 to 15.5 |  | validated |

## Multiplexing

`VCSEC_debug100msIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (15 signals), page 5 (3 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y (2025+ / Juniper; community mapping) 2026.26.6.5 VEH DBC file](../../../../../dbc/Bayberry/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Bayberry/2026.26.6.5/VEH.json)

## See also

- [All Vehicle security controller messages (VCSEC)](../../vcsec.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
