---
layout: default
title: "VCSEC_TPMSConnectionData (0x42A) — Vehicle security controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN"
description: "Vehicle security controller message: TPMS connection data. Tesla Model 3 / Model Y CAN bus message VCSEC_TPMSConnectionData (0x42A) of Vehicle security controller, firmware 2025.20.8, 20 signals (VCSEC_TPMSSensorState0, VCSEC_TPMSRSSI0, VCSEC_TPMSConnectionTypeCurrent0, VCSEC_TPMSConnectionTypeDesired0 and 16 more). Bit layout, scaling, units and value tables."
---

# VCSEC_TPMSConnectionData (0x42A) — Vehicle security controller, Tesla Model 3 / Model Y 2025.20.8 VEH CAN

Vehicle security controller message: TPMS connection data; frame length from the layout, not yet observed on a vehicle bus. This page documents the 20 signals of VCSEC_TPMSConnectionData as defined for Tesla Model 3 / Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEC_TPMSConnectionData` |
| CAN id | 0x42A (1066) |
| ECU | [Vehicle security controller](../../vcsec.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCSEC |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 20 |

## Signals of VCSEC_TPMSConnectionData

Tesla Model 3 / Model Y CAN bus signals in `VCSEC_TPMSConnectionData`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEC_TPMSSensorState0` | Indicates the sensors pairing/connectivity status | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SENSOR_NOT_PAIRED`<br>1 = `SENSOR_WAIT_FOR_ADV`<br>2 = `SENSOR_WAIT_FOR_CONN`<br>3 = `SENSOR_CONNECTED`<br>4 = `SENSOR_DISCONNECTING`<br>5 = `SENSOR_WAIT_FOR_NEXT_ADV` | validated |
| `VCSEC_TPMSRSSI0` | Received Signal Strength Index reported by sensor. | 3\|7 | little-endian | unsigned | 1 | -127 | dBm | -127 to 0 |  | validated |
| `VCSEC_TPMSConnectionTypeCurrent0` | Vehicle security controller: TPMS connection type current0 | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CONNECTIONTYPE_FAST`<br>1 = `CONNECTIONTYPE_SLOW`<br>2 = `CONNECTIONTYPE_UNKNOWN`<br>3 = `CONNECTIONTYPE_FAST_SLAVE_LATENCY` | validated |
| `VCSEC_TPMSConnectionTypeDesired0` | Vehicle security controller: TPMS connection type desired0 | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CONNECTIONTYPE_FAST`<br>1 = `CONNECTIONTYPE_SLOW`<br>2 = `CONNECTIONTYPE_UNKNOWN`<br>3 = `CONNECTIONTYPE_FAST_SLAVE_LATENCY` | validated |
| `VCSEC_TPMSSensorState1` | Indicates the sensors pairing/connectivity status | 14\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SENSOR_NOT_PAIRED`<br>1 = `SENSOR_WAIT_FOR_ADV`<br>2 = `SENSOR_WAIT_FOR_CONN`<br>3 = `SENSOR_CONNECTED`<br>4 = `SENSOR_DISCONNECTING`<br>5 = `SENSOR_WAIT_FOR_NEXT_ADV` | validated |
| `VCSEC_TPMSRSSI1` | Received Signal Strength Index reported by sensor. | 17\|7 | little-endian | unsigned | 1 | -127 | dBm | -127 to 0 |  | validated |
| `VCSEC_TPMSConnectionTypeCurrent1` | Vehicle security controller: TPMS connection type current1 | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CONNECTIONTYPE_FAST`<br>1 = `CONNECTIONTYPE_SLOW`<br>2 = `CONNECTIONTYPE_UNKNOWN`<br>3 = `CONNECTIONTYPE_FAST_SLAVE_LATENCY` | validated |
| `VCSEC_TPMSConnectionTypeDesired1` | Vehicle security controller: TPMS connection type desired1 | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CONNECTIONTYPE_FAST`<br>1 = `CONNECTIONTYPE_SLOW`<br>2 = `CONNECTIONTYPE_UNKNOWN`<br>3 = `CONNECTIONTYPE_FAST_SLAVE_LATENCY` | validated |
| `VCSEC_TPMSSensorState2` | Indicates the sensors pairing/connectivity status | 28\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SENSOR_NOT_PAIRED`<br>1 = `SENSOR_WAIT_FOR_ADV`<br>2 = `SENSOR_WAIT_FOR_CONN`<br>3 = `SENSOR_CONNECTED`<br>4 = `SENSOR_DISCONNECTING`<br>5 = `SENSOR_WAIT_FOR_NEXT_ADV` | validated |
| `VCSEC_TPMSRSSI2` | Received Signal Strength Index reported by sensor. | 31\|7 | little-endian | unsigned | 1 | -127 | dBm | -127 to 0 |  | validated |
| `VCSEC_TPMSConnectionTypeCurrent2` | Vehicle security controller: TPMS connection type current2 | 38\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CONNECTIONTYPE_FAST`<br>1 = `CONNECTIONTYPE_SLOW`<br>2 = `CONNECTIONTYPE_UNKNOWN`<br>3 = `CONNECTIONTYPE_FAST_SLAVE_LATENCY` | validated |
| `VCSEC_TPMSConnectionTypeDesired2` | Vehicle security controller: TPMS connection type desired2 | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CONNECTIONTYPE_FAST`<br>1 = `CONNECTIONTYPE_SLOW`<br>2 = `CONNECTIONTYPE_UNKNOWN`<br>3 = `CONNECTIONTYPE_FAST_SLAVE_LATENCY` | validated |
| `VCSEC_TPMSSensorState3` | Indicates the sensors pairing/connectivity status | 42\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SENSOR_NOT_PAIRED`<br>1 = `SENSOR_WAIT_FOR_ADV`<br>2 = `SENSOR_WAIT_FOR_CONN`<br>3 = `SENSOR_CONNECTED`<br>4 = `SENSOR_DISCONNECTING`<br>5 = `SENSOR_WAIT_FOR_NEXT_ADV` | validated |
| `VCSEC_TPMSRSSI3` | Received Signal Strength Index reported by sensor. | 45\|7 | little-endian | unsigned | 1 | -127 | dBm | -127 to 0 |  | validated |
| `VCSEC_TPMSConnectionTypeCurrent3` | Vehicle security controller: TPMS connection type current3 | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CONNECTIONTYPE_FAST`<br>1 = `CONNECTIONTYPE_SLOW`<br>2 = `CONNECTIONTYPE_UNKNOWN`<br>3 = `CONNECTIONTYPE_FAST_SLAVE_LATENCY` | validated |
| `VCSEC_TPMSConnectionTypeDesired3` | Vehicle security controller: TPMS connection type desired3 | 54\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CONNECTIONTYPE_FAST`<br>1 = `CONNECTIONTYPE_SLOW`<br>2 = `CONNECTIONTYPE_UNKNOWN`<br>3 = `CONNECTIONTYPE_FAST_SLAVE_LATENCY` | validated |
| `VCSEC_TPMSSensorPresence0` | Indicates the sensors detection status | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_PAIRED`<br>1 = `NOT_PRESENT`<br>2 = `PRESENT` | validated |
| `VCSEC_TPMSSensorPresence1` | Indicates the sensors detection status | 58\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_PAIRED`<br>1 = `NOT_PRESENT`<br>2 = `PRESENT` | validated |
| `VCSEC_TPMSSensorPresence2` | Indicates the sensors detection status | 60\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_PAIRED`<br>1 = `NOT_PRESENT`<br>2 = `PRESENT` | validated |
| `VCSEC_TPMSSensorPresence3` | Indicates the sensors detection status | 62\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_PAIRED`<br>1 = `NOT_PRESENT`<br>2 = `PRESENT` | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 VEH DBC file](../../../../../dbc/AllModels/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/VEH.json)

## See also

- [All Vehicle security controller messages (VCSEC)](../../vcsec.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
