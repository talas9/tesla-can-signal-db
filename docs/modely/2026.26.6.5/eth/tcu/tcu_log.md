---
layout: default
title: "TCU_log (0x483) — TCU ECU, Tesla Model Y 2026.26.6.5 ETH"
description: "TCU ECU message: log. Ethernet-side message TCU_log of TCU ECU for Tesla Model Y firmware 2026.26.6.5, 32 signals (TCU_logMux, TCU_cpuTemp, TCU_cpuUsage, TCU_mdmCoreTemperature and 28 more). Bit layout, scaling, units and value tables."
---

# TCU_log (0x483) — TCU ECU, Tesla Model Y 2026.26.6.5 ETH

TCU ECU message: log. This page documents the 32 signals of TCU_log as defined for Tesla Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `TCU_log` |
| Ethernet-side id | 0x483 (1155) |
| ECU | [TCU ECU](../../tcu.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | TCU |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 32 |

## Signals of TCU_log

Tesla Model Y CAN bus signals in `TCU_log`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `TCU_logMux` | selector | TCU ECU: log mux | 0\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 | 0 = `cpuTemp`<br>1 = `cpuUsage`<br>2 = `mdmCoreTemperature`<br>3 = `availableMemory`<br>4 = `pwm`<br>5 = `pwmcap`<br>6 = `totalResumes`<br>7 = `mdmUplinkQueueSize`<br>8 = `mdmRSRP`<br>9 = `mdmSINR`<br>10 = `mdmUplinkAllowedRate`<br>11 = `mdmUplinkAvgRate`<br>12 = `mdmServiceState`<br>13 = `mdmIMSStatus`<br>14 = `mdmSIMStatus`<br>15 = `mdmBusyActive`<br>16 = `modemUptime`<br>17 = `mdmDataRat`<br>18 = `mdmDataCallStatus`<br>19 = `mdmNSAAvailable`<br>20 = `mdmPCIID`<br>21 = `mdmMnc`<br>22 = `mdmMcc`<br>23 = `mdmTxKiloBytes`<br>24 = `mdmDataCallTermReason`<br>25 = `mdmDataCallTermCode`<br>26 = `cellularSMState`<br>27 = `tcuSMState`<br>28 = `checkInternetFailCount`<br>29 = `mdmBand`<br>30 = `wakeSource` | plausible |
| `TCU_cpuTemp` | page 0 | Indicates the current temperature reported by the Central Processing Unit (CPU) in the modem application processor | 32\|32 | little-endian | unsigned | 1 | 0 | C | 0 to 4294967295 |  | plausible |
| `TCU_cpuUsage` | page 1 | Indicates the current CPU usage in percentage reported by the modem application processor | 32\|32 | little-endian | unsigned | 1 | 0 | % | 0 to 4294967295 |  | plausible |
| `TCU_mdmCoreTemperature` | page 2 | Indicates the current Communication Processor (CP) temperature reported by the modem CP. | 32\|32 | little-endian | unsigned | 1 | 0 | C | 0 to 4294967295 |  | plausible |
| `TCU_availableMemory` | page 3 | Indicates the currently available Random Access Memory in the modem application processor | 32\|32 | little-endian | unsigned | 1 | 0 | KB | 0 to 4294967295 |  | plausible |
| `TCU_pwm` | page 4 | Indicates the active Pulse Width Modulation (PWM) duty cycle applied to the modem fan. | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `TCU_pwmcap` | page 5 | Indicates the active Pulse Width Modulation (PWM) duty cycle restriciton applied to the modem fan. | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `TCU_totalResumes` | page 6 | Indicates the total amount of times the modem has been resumed | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `TCU_mdmUplinkQueueSize` | page 7 | TCU ECU: mdm uplink queue size | 32\|32 | little-endian | unsigned | 1 | 0 | bytes | 0 to 4294967295 |  | plausible |
| `TCU_mdmRSRP` | page 8 | TCU ECU: mdm RSRP | 32\|32 | little-endian | signed | 1 | 0 | dBm | -2147483648 to 2147483647 |  | plausible |
| `TCU_mdmSINR` | page 9 | TCU ECU: mdm SINR | 32\|32 | little-endian | signed | 1 | 0 | dBm | -2147483648 to 2147483647 |  | plausible |
| `TCU_mdmUplinkAllowedRate` | page 10 | TCU ECU: mdm uplink allowed rate | 32\|32 | little-endian | unsigned | 1 | 0 | Kbps | 0 to 4294967295 |  | plausible |
| `TCU_mdmUplinkAvgRate` | page 11 | TCU ECU: mdm uplink avg rate | 32\|32 | little-endian | unsigned | 1 | 0 | Kbps | 0 to 4294967295 |  | plausible |
| `TCU_mdmServiceState` | page 12 | TCU ECU: mdm service state | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TCU_mdmIMSStatus` | page 13 | Indicates the current IP Multimedia System (IMS) registration state. | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `TCU_mdmSIMStatus` | page 14 | TCU ECU: mdm SIM status | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TCU_mdmBusyActive` | page 15 | Reports whether the modem busy service is active on the modem application processor; raw 4294967295 = signal not available (SNA) | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967294 | 4294967295 = `SNA` | plausible |
| `TCU_modemUptime` | page 16 | Indicates the current modem Application Processor uptime. | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `TCU_mdmDataRat` | page 17 | Reports which Radio Access Technology (RAT) is active for the current data bearer. | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `RAT_UNKNOWN`<br>1 = `RAT_GSM`<br>2 = `RAT_WCDMA`<br>3 = `RAT_LTE`<br>4 = `RAT_NR5G_NSA`<br>5 = `RAT_NR5G_SA`<br>6 = `RAT_NR5G_UNKNOWN` | plausible |
| `TCU_mdmDataCallStatus` | page 18 | Indicates the current state of the Packet Data Protocol (PDP) context. | 32\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `CONNECTING`<br>2 = `CONNECTED`<br>3 = `DISCONNECTING`<br>4 = `DISCONNECTED` | plausible |
| `TCU_mdmNSAAvailable` | page 19 | TCU ECU: mdm NSA available | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NSA_UNKNOWN`<br>1 = `NSA_AVAILABLE`<br>2 = `NSA_NOT_AVAILABLE` | plausible |
| `TCU_mdmPCIID` | page 20 | TCU ECU: mdm PCIID | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TCU_mdmMnc` | page 21 | TCU ECU: mdm mnc | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TCU_mdmMcc` | page 22 | TCU ECU: mdm mcc | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TCU_mdmTxKiloBytes` | page 23 | TCU ECU: mdm tx kilo bytes | 32\|32 | little-endian | unsigned | 1 | 0 | KB | 0 to 4294967295 |  | plausible |
| `TCU_mdmDataCallTermReason` | page 24 | Indicates the internal reason which the Data Call was terminated. | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `TCU_mdmDataCallTermCode` | page 25 | Indicates the termination code informed by the network that caused the Data Call termination. | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `TCU_cellularSMState` | page 26 | Indicates the current state of cellular state machine. | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 | 0 = `UNKNOWN`<br>1 = `WAITING_COMPONENT`<br>2 = `OUT_OF_SERVICE`<br>3 = `IN_SERVICE`<br>4 = `DATA_CONNECTED`<br>5 = `CHECKING_INTERNET`<br>6 = `LINK_CONNECTED`<br>7 = `RECOVERING` | plausible |
| `TCU_tcuSMState` | page 27 | Reports the state of the Telematics Control Unit (TCU) state machine. | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 | 0 = `UNKNOWN`<br>1 = `SEARCHING_COMPONENT`<br>2 = `IN_OPERATION`<br>3 = `POWER_CYCLING`<br>4 = `PREPARING_SLEEP`<br>5 = `SUSPENDED`<br>6 = `RESUMING`<br>7 = `UPDATING` | plausible |
| `TCU_checkInternetFailCount` | page 28 | Reports the count of unsuccessful cellular connectivity checks. | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `TCU_mdmBand` | page 29 | Indicates the band which the baseband processor is currently attached to the cellular network. | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `TCU_wakeSource` | page 30 | Indicates the source of wake event in the modem. | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `SMS`<br>2 = `WOIP`<br>3 = `ETHERNET` | plausible |

## Multiplexing

`TCU_logMux` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (1 signals), page 1 (1 signals), page 2 (1 signals), page 3 (1 signals), page 4 (1 signals), page 5 (1 signals), page 6 (1 signals), page 7 (1 signals), page 8 (1 signals), page 9 (1 signals), page 10 (1 signals), page 11 (1 signals), page 12 (1 signals), page 13 (1 signals), page 14 (1 signals), page 15 (1 signals), page 16 (1 signals), page 17 (1 signals), page 18 (1 signals), page 19 (1 signals), page 20 (1 signals), page 21 (1 signals), page 22 (1 signals), page 23 (1 signals), page 24 (1 signals), page 25 (1 signals), page 26 (1 signals), page 27 (1 signals), page 28 (1 signals), page 29 (1 signals), page 30 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/ModelY/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All TCU ECU messages (TCU)](../../tcu.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
