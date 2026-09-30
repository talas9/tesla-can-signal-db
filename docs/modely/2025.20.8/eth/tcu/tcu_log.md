---
layout: default
title: "TCU_log (0x581) — TCU ECU, Tesla Model Y 2025.20.8 ETH"
description: "TCU ECU message: log. Ethernet-side message TCU_log of TCU ECU for Tesla Model Y firmware 2025.20.8, 17 signals (TCU_logMux, TCU_cpuTemp, TCU_cpuUsage, TCU_mdmCoreTemperature and 13 more). Bit layout, scaling, units and value tables."
---

# TCU_log (0x581) — TCU ECU, Tesla Model Y 2025.20.8 ETH

TCU ECU message: log. This page documents the 17 signals of TCU_log as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `TCU_log` |
| Ethernet-side id | 0x581 (1409) |
| ECU | [TCU ECU](../../tcu.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | TCU |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 17 |

## Signals of TCU_log

Tesla Model Y CAN bus signals in `TCU_log`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `TCU_logMux` | selector | TCU ECU: log mux | 0\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 | 0 = `cpuTemp`<br>1 = `cpuUsage`<br>2 = `mdmCoreTemperature`<br>3 = `availableMemory`<br>4 = `pwm`<br>5 = `pwmcap`<br>6 = `totalResumes`<br>7 = `mdmUplinkQueueSize`<br>8 = `mdmRSRP`<br>9 = `mdmSINR`<br>10 = `mdmUplinkAllowedRate`<br>11 = `mdmUplinkAvgRage`<br>12 = `mdmServiceState`<br>13 = `mdmIMSStatus`<br>14 = `mdmSIMStatus`<br>15 = `mdmBusyActive` | plausible |
| `TCU_cpuTemp` | page 0 | Indicates the current temperature reported by the Central Processing Unit (CPU) in the modem application processor | 32\|32 | little-endian | unsigned | 1 | 0 | C | 0 to 4294967295 |  | validated |
| `TCU_cpuUsage` | page 1 | Indicates the current CPU usage in percentage reported by the modem application processor | 32\|32 | little-endian | unsigned | 1 | 0 | % | 0 to 4294967295 |  | validated |
| `TCU_mdmCoreTemperature` | page 2 | Indicates the current Communication Processor (CP) temperature reported by the modem CP. | 32\|32 | little-endian | unsigned | 1 | 0 | C | 0 to 4294967295 |  | validated |
| `TCU_availableMemory` | page 3 | Indicates the currently available Random Access Memory in the modem application processor | 32\|32 | little-endian | unsigned | 1 | 0 | KB | 0 to 4294967295 |  | validated |
| `TCU_pwm` | page 4 | Indicates the active Pulse Width Modulation (PWM) duty cycle applied to the modem fan. | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `TCU_pwmcap` | page 5 | Indicates the active Pulse Width Modulation (PWM) duty cycle restriciton applied to the modem fan. | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `TCU_totalResumes` | page 6 | Indicates the total amount of times the modem has been resumed | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `TCU_mdmUplinkQueueSize` | page 7 | TCU ECU: mdm uplink queue size | 32\|32 | little-endian | unsigned | 1 | 0 | bytes | 0 to 4294967295 |  | validated |
| `TCU_mdmRSRP` | page 8 | TCU ECU: mdm RSRP | 32\|32 | little-endian | signed | 1 | 0 | dBm | -2147483648 to 2147483647 |  | validated |
| `TCU_mdmSINR` | page 9 | TCU ECU: mdm SINR | 32\|32 | little-endian | signed | 1 | 0 | dBm | -2147483648 to 2147483647 |  | validated |
| `TCU_mdmUplinkAllowedRate` | page 10 | TCU ECU: mdm uplink allowed rate | 32\|32 | little-endian | unsigned | 1 | 0 | Kbps | 0 to 4294967295 |  | validated |
| `TCU_mdmUplinkAvgRage` | page 11 | TCU ECU: mdm uplink avg rage | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `TCU_mdmServiceState` | page 12 | TCU ECU: mdm service state | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `TCU_mdmIMSStatus` | page 13 | Indicates the current IP Multimedia System (IMS) registration state. | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `TCU_mdmSIMStatus` | page 14 | TCU ECU: mdm SIM status | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `TCU_mdmBusyActive` | page 15 | Reports whether the modem busy service is active on the modem application processor; raw 4294967295 = signal not available (SNA) | 32\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967294 | 4294967295 = `SNA` | validated |

## Multiplexing

`TCU_logMux` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (1 signals), page 1 (1 signals), page 2 (1 signals), page 3 (1 signals), page 4 (1 signals), page 5 (1 signals), page 6 (1 signals), page 7 (1 signals), page 8 (1 signals), page 9 (1 signals), page 10 (1 signals), page 11 (1 signals), page 12 (1 signals), page 13 (1 signals), page 14 (1 signals), page 15 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All TCU ECU messages (TCU)](../../tcu.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
