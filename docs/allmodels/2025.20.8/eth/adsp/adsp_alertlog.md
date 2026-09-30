---
layout: default
title: "ADSP_alertLog (0x550) — Audio amplifier, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Audio amplifier message: alert log. Ethernet-side message ADSP_alertLog of Audio amplifier for Tesla Model 3 / Model Y firmware 2025.20.8, 28 signals (ADSP_alertID, ADSP_alertState, ADSP_a035_a2baFaultNode, ADSP_a035_timeout and 24 more). Bit layout, scaling, units and value tables."
---

# ADSP_alertLog (0x550) — Audio amplifier, Tesla Model 3 / Model Y 2025.20.8 ETH

Audio amplifier message: alert log. This page documents the 28 signals of ADSP_alertLog as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `ADSP_alertLog` |
| Ethernet-side id | 0x550 (1360) |
| ECU | [Audio amplifier](../../adsp.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | ADSP |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 28 |

## Signals of ADSP_alertLog

Tesla Model 3 / Model Y CAN bus signals in `ADSP_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `ADSP_alertID` | selector | Audio amplifier: alert ID | 0\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `w001_flashInit`<br>2 = `w002_exception`<br>3 = `w003_assert`<br>4 = `w004_malloc`<br>5 = `w005_stackOverflow`<br>6 = `w006_eavbSeqno`<br>7 = `w007_ethLinkErr`<br>8 = `w008_internalTempHigh`<br>10 = `w010_12vAudioFiltLow`<br>11 = `w011_armHighCpuUsage`<br>12 = `w012_sharc0HighCpuUsage`<br>13 = `w013_sharc1HighCpuUsage`<br>14 = `w014_eavbOverrun`<br>15 = `w015_eavbUnderrun`<br>16 = `w016_usbRxOverrun`<br>17 = `w017_usbRxUnderrun`<br>18 = `w018_usbTxOverrun`<br>19 = `w019_usbTxUnderrun`<br>20 = `w020_usbTxFailed`<br>21 = `w021_usbTxAborted`<br>22 = `w022_emacErr`<br>23 = `w023_ethEtharpErr`<br>24 = `w024_ethIpfragErr`<br>25 = `w025_ethIpErr`<br>26 = `w026_ethIcmpErr`<br>27 = `w027_ethUdpErr`<br>28 = `w028_ethTcpErr`<br>29 = `w029_baseamp0SmFault`<br>30 = `w030_ethSysErr`<br>31 = `w031_baseamp1SmFault`<br>32 = `w032_baseamp2SmFault`<br>33 = `w033_a2baDiscoveryFailed`<br>34 = `w034_a2bbDiscoveryFailed`<br>35 = `w035_a2baFault`<br>36 = `w036_a2bbFault`<br>37 = `w037_a2baIdleFailed`<br>38 = `w038_a2bbIdleFailed`<br>39 = `w039_ancPing`<br>40 = `w040_socSciHeartbeat`<br>41 = `w041_twiWriteError`<br>42 = `w042_twiReadError`<br>43 = `w043_aweControlError`<br>44 = `w044_canethChecksum`<br>45 = `w045_ancEnableFail`<br>46 = `w046_sharc0AweFrameOverload`<br>47 = `w047_sharc1AweFrameOverload`<br>48 = `w048_eCallSelfTestFailed`<br>49 = `w049_sae`<br>50 = `w050_extSpkFault`<br>51 = `w051_extspkFailure`<br>52 = `w052_criticalReset`<br>53 = `w053_audioSystemUnavailable`<br>54 = `w054_canethRxError`<br>55 = `w055_hfpMathExcept1NAN`<br>56 = `w056_hfpMathExcept1INF`<br>57 = `w057_hfpMathExcept2NAN`<br>58 = `w058_hfpMathExcept2INF`<br>59 = `w059_nvmmError`<br>60 = `w060_baseamp3SmFault`<br>61 = `w061_tcuGpioServiceError`<br>65 = `w065_tcuGpioExpanderCriticalError`<br>66 = `w066_rearPwsFault`<br>67 = `w067_baseamp0Fault`<br>68 = `w068_baseamp1Fault`<br>69 = `w069_baseamp2Fault`<br>70 = `w070_baseamp3Fault`<br>71 = `w071_versionMismatch`<br>72 = `w072_turnSignalChannelUnderrun`<br>73 = `w073_romFLError`<br>74 = `w074_tdspArmXrun`<br>75 = `w075_tdspArmError`<br>76 = `w076_activeSafetyChannelUnderrun` | plausible |
| `ADSP_alertState` |  | Audio amplifier: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `ADSP_a035_a2baFaultNode` | page 35 | Audio amplifier: a035 a2ba fault node | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `ADSP_a035_timeout` | page 35 | Audio amplifier: a035 timeout | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_a035_a2baIntrType` | page 35 | Audio amplifier: a035 a2ba intr type | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `HEADER_COUNT_ERR`<br>1 = `DATA_DECODING_ERR`<br>2 = `CRC_ERR`<br>3 = `DATA_PARITY_ERR`<br>4 = `BIT_ERR_COUNT_OVERFLOW`<br>5 = `SRFERR`<br>9 = `PWRERR_CABLE_SHORTED_GND`<br>10 = `PWRERR_CABLE_SHORTED_VBAT`<br>11 = `PWRERR_CABLE_SHORTED_TOGETHER`<br>12 = `PWRERR_CABLE_DISCONNECTED_OR_OPEN_CIRCUIT`<br>13 = `PWRERR_CABLE_REVERSE_CONNECTED`<br>15 = `PWRERR_INDETERMINATE_FAULT`<br>16 = `IO0PND`<br>17 = `IO1PND`<br>18 = `IO2PND`<br>19 = `IO3PND`<br>20 = `IO4PND`<br>21 = `IO5PND`<br>22 = `IO6PND`<br>23 = `IO7PND`<br>24 = `DSCDONE`<br>25 = `I2CERR`<br>26 = `ICRCERR`<br>41 = `PWRERR_NON_LOCALIZED_SHORT_GND`<br>42 = `PWRERR_NON_LOCALIZED_SHORT_VBAT`<br>48 = `MBOX0_FULL`<br>49 = `MBOX0_EMPTY`<br>50 = `MBOX1_FULL`<br>51 = `MBOX1_EMPTY`<br>128 = `IRPT_MSG_ERR`<br>251 = `NONE`<br>252 = `STRTUP_ERR_RTF`<br>253 = `SLAVE_INTTYPE_ERR`<br>254 = `STANDBY_DONE`<br>255 = `MSTR_RUNNING` | plausible |
| `ADSP_a035_a2baFaultType` | page 35 | Audio amplifier: a035 a2ba fault type | 32\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `EMPTY`<br>1 = `BUS_OK`<br>2 = `DISCOVERY_DIAG_TIMEOUT`<br>3 = `PWRERR_CS_GND`<br>4 = `PWRERR_CS_VBAT`<br>5 = `PWRERR_CS`<br>6 = `PWRERR_CDISC`<br>7 = `PWRERR_CREV`<br>8 = `PWRERR_FAULT`<br>9 = `PWRERR_NLS_GND`<br>10 = `PWRERR_NLS_VBAT`<br>11 = `BECOVF`<br>12 = `STRTUP_ERR_RTF`<br>13 = `SUCCESS`<br>14 = `ERROR`<br>15 = `CFG_ERROR`<br>16 = `BUS_ERROR`<br>17 = `BUS_TIMEOUT`<br>18 = `ODD_I2C_ADDRESS_ERROR`<br>19 = `CORRUPT_INIT_FILE`<br>20 = `UNSUPPORTED_INIT_FILE`<br>21 = `UNSUPPORTED_READ_LENGTH`<br>22 = `UNSUPPORTED_DATA_WIDTH`<br>23 = `UNSUPPORTED_ADDR_BYTES`<br>24 = `UNSUPPORTED_PROTOCOL`<br>25 = `A2B_I2C_WRITE_ERROR`<br>26 = `A2B_I2C_READ_ERROR`<br>27 = `A2B_MEMORY_ERROR`<br>28 = `A2B_BUS_POS_SHORT_TO_GROUND`<br>29 = `A2B_BUS_NEG_SHORT_TO_VBAT`<br>30 = `A2B_BUS_SHORT_TOGETHER`<br>31 = `A2B_BUS_OPEN_OR_WRONG_PORT`<br>32 = `A2B_BUS_REVERSED_OR_OPEN`<br>33 = `A2B_BUS_REVERSED_OR_WRONG_PORT`<br>34 = `A2B_BUS_INDETERMINATE_FAULT`<br>35 = `A2B_BUS_UNKNOWN_FAULT`<br>36 = `A2B_BUS_NO_FAULT`<br>37 = `A2B_BUS_SHORT_TO_GROUND`<br>38 = `A2B_BUS_SHORT_TO_VBAT`<br>39 = `A2B_BUS_DISCONNECT_OR_OPEN_CIRCUIT`<br>40 = `A2B_BUS_REVERSE_CONNECTED`<br>41 = `A2B_BAD_NODE`<br>42 = `A2B_NOT_LAST_NODE`<br>43 = `END`<br>44 = `UNKNOWN` | plausible |
| `ADSP_a036_a2bbFaultNode` | page 36 | Audio amplifier: a036 a2bb fault node | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `ADSP_a036_timeout` | page 36 | Audio amplifier: a036 timeout | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_a036_a2bbIntrType` | page 36 | Audio amplifier: a036 a2bb intr type | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `HEADER_COUNT_ERR`<br>1 = `DATA_DECODING_ERR`<br>2 = `CRC_ERR`<br>3 = `DATA_PARITY_ERR`<br>4 = `BIT_ERR_COUNT_OVERFLOW`<br>5 = `SRFERR`<br>9 = `PWRERR_CABLE_SHORTED_GND`<br>10 = `PWRERR_CABLE_SHORTED_VBAT`<br>11 = `PWRERR_CABLE_SHORTED_TOGETHER`<br>12 = `PWRERR_CABLE_DISCONNECTED_OR_OPEN_CIRCUIT`<br>13 = `PWRERR_CABLE_REVERSE_CONNECTED`<br>15 = `PWRERR_INDETERMINATE_FAULT`<br>16 = `IO0PND`<br>17 = `IO1PND`<br>18 = `IO2PND`<br>19 = `IO3PND`<br>20 = `IO4PND`<br>21 = `IO5PND`<br>22 = `IO6PND`<br>23 = `IO7PND`<br>24 = `DSCDONE`<br>25 = `I2CERR`<br>26 = `ICRCERR`<br>41 = `PWRERR_NON_LOCALIZED_SHORT_GND`<br>42 = `PWRERR_NON_LOCALIZED_SHORT_VBAT`<br>48 = `MBOX0_FULL`<br>49 = `MBOX0_EMPTY`<br>50 = `MBOX1_FULL`<br>51 = `MBOX1_EMPTY`<br>128 = `IRPT_MSG_ERR`<br>251 = `NONE`<br>252 = `STRTUP_ERR_RTF`<br>253 = `SLAVE_INTTYPE_ERR`<br>254 = `STANDBY_DONE`<br>255 = `MSTR_RUNNING` | plausible |
| `ADSP_a036_a2bbFaultType` | page 36 | Audio amplifier: a036 a2bb fault type | 32\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `EMPTY`<br>1 = `BUS_OK`<br>2 = `DISCOVERY_DIAG_TIMEOUT`<br>3 = `PWRERR_CS_GND`<br>4 = `PWRERR_CS_VBAT`<br>5 = `PWRERR_CS`<br>6 = `PWRERR_CDISC`<br>7 = `PWRERR_CREV`<br>8 = `PWRERR_FAULT`<br>9 = `PWRERR_NLS_GND`<br>10 = `PWRERR_NLS_VBAT`<br>11 = `BECOVF`<br>12 = `STRTUP_ERR_RTF`<br>13 = `SUCCESS`<br>14 = `ERROR`<br>15 = `CFG_ERROR`<br>16 = `BUS_ERROR`<br>17 = `BUS_TIMEOUT`<br>18 = `ODD_I2C_ADDRESS_ERROR`<br>19 = `CORRUPT_INIT_FILE`<br>20 = `UNSUPPORTED_INIT_FILE`<br>21 = `UNSUPPORTED_READ_LENGTH`<br>22 = `UNSUPPORTED_DATA_WIDTH`<br>23 = `UNSUPPORTED_ADDR_BYTES`<br>24 = `UNSUPPORTED_PROTOCOL`<br>25 = `A2B_I2C_WRITE_ERROR`<br>26 = `A2B_I2C_READ_ERROR`<br>27 = `A2B_MEMORY_ERROR`<br>28 = `A2B_BUS_POS_SHORT_TO_GROUND`<br>29 = `A2B_BUS_NEG_SHORT_TO_VBAT`<br>30 = `A2B_BUS_SHORT_TOGETHER`<br>31 = `A2B_BUS_OPEN_OR_WRONG_PORT`<br>32 = `A2B_BUS_REVERSED_OR_OPEN`<br>33 = `A2B_BUS_REVERSED_OR_WRONG_PORT`<br>34 = `A2B_BUS_INDETERMINATE_FAULT`<br>35 = `A2B_BUS_UNKNOWN_FAULT`<br>36 = `A2B_BUS_NO_FAULT`<br>37 = `A2B_BUS_SHORT_TO_GROUND`<br>38 = `A2B_BUS_SHORT_TO_VBAT`<br>39 = `A2B_BUS_DISCONNECT_OR_OPEN_CIRCUIT`<br>40 = `A2B_BUS_REVERSE_CONNECTED`<br>41 = `A2B_BAD_NODE`<br>42 = `A2B_NOT_LAST_NODE`<br>43 = `END`<br>44 = `UNKNOWN` | plausible |
| `ADSP_a050_open_load` | page 50 | Audio amplifier: a050 open load | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_a050_short_vcc` | page 50 | Audio amplifier: a050 short vcc | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_a050_short_gnd` | page 50 | Audio amplifier: a050 short gnd | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_a050_short_load` | page 50 | Audio amplifier: a050 short load | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_a050_diag_failed_to_start` | page 50 | Audio amplifier: a050 diag failed to start | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_a050_diag_failed` | page 50 | Audio amplifier: a050 diag failed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_a053_audioSystemUnavailable` | page 53 | Audio amplifier: a053 audio system unavailable | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `EXTERNAL_SPEAKER_BASEAMP_FAULT`<br>2 = `EXTERNAL_SPEAKER_BASEAMP_NOT_AVAILABLE`<br>3 = `EXTERNAL_SPEAKER_CONNECTION_FAULT`<br>4 = `CHIME_SYSTEM_FAULT` | plausible |
| `ADSP_a066_open_load` | page 66 | Audio amplifier: a066 open load | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_a066_short_vcc` | page 66 | Audio amplifier: a066 short vcc | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_a066_short_gnd` | page 66 | Audio amplifier: a066 short gnd | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_a066_short_load` | page 66 | Audio amplifier: a066 short load | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_a066_diag_failed_to_start` | page 66 | Audio amplifier: a066 diag failed to start | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_a066_diag_failed` | page 66 | Audio amplifier: a066 diag failed | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_a067_baseamp0Fault` | page 67 | Audio amplifier: a067 baseamp0 fault | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `OVER_TEMP`<br>2 = `CLOCK_PLL`<br>3 = `OVER_CURRENT`<br>4 = `OVER_VOLTAGE`<br>5 = `UNDER_VOLTAGE`<br>6 = `DC`<br>7 = `OTHER` | plausible |
| `ADSP_a068_baseamp1Fault` | page 68 | Audio amplifier: a068 baseamp1 fault | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `OVER_TEMP`<br>2 = `CLOCK_PLL`<br>3 = `OVER_CURRENT`<br>4 = `OVER_VOLTAGE`<br>5 = `UNDER_VOLTAGE`<br>6 = `DC`<br>7 = `OTHER` | plausible |
| `ADSP_a069_baseamp2Fault` | page 69 | Audio amplifier: a069 baseamp2 fault | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `OVER_TEMP`<br>2 = `CLOCK_PLL`<br>3 = `OVER_CURRENT`<br>4 = `OVER_VOLTAGE`<br>5 = `UNDER_VOLTAGE`<br>6 = `DC`<br>7 = `OTHER` | plausible |
| `ADSP_a070_baseamp3Fault` | page 70 | Audio amplifier: a070 baseamp3 fault | 16\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `OVER_TEMP`<br>2 = `CLOCK_PLL`<br>3 = `OVER_CURRENT`<br>4 = `OVER_VOLTAGE`<br>5 = `UNDER_VOLTAGE`<br>6 = `DC`<br>7 = `OTHER` | plausible |
| `ADSP_a071_versionMismatch` | page 71 | Audio amplifier: a071 version mismatch | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `MATCH`<br>1 = `MISMATCH` | plausible |

## Multiplexing

`ADSP_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 35 (4 signals), page 36 (4 signals), page 50 (6 signals), page 53 (1 signals), page 66 (6 signals), page 67 (1 signals), page 68 (1 signals), page 69 (1 signals), page 70 (1 signals), page 71 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Audio amplifier messages (ADSP)](../../adsp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
