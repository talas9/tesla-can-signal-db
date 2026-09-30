---
layout: default
title: "PARK_alertLog (0x5CE) — Parking assist sensors, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Parking assist sensors message: alert log. Tesla Model 3 / Model Y CAN bus message PARK_alertLog (0x5CE) of Parking assist sensors, firmware 2026.26.6.5, 268 signals (PARK_alertID, PARK_alertState, PARK_sw001_sensorTemperature, PARK_sw002_membraneDisconct and 264 more). Bit layout, scaling, units and value tables."
---

# PARK_alertLog (0x5CE) — Parking assist sensors, Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Parking assist sensors message: alert log; frame length from the layout, not yet observed on a vehicle bus. This page documents the 268 signals of PARK_alertLog as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PARK_alertLog` |
| CAN id | 0x5CE (1486) |
| ECU | [Parking assist sensors](../../park.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | PARK |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 268 |

## Signals of PARK_alertLog

Tesla Model 3 / Model Y CAN bus signals in `PARK_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `PARK_alertID` | selector | Parking assist sensors: alert ID | 0\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_s1_overTemp`<br>2 = `a002_s1_internalFail`<br>3 = `a003_s1_linCommError`<br>4 = `a004_s1_blocked`<br>5 = `a005_s1_crossTalk`<br>6 = `a006_s2_overTemp`<br>7 = `a007_s2_internalFail`<br>8 = `a008_s2_linCommError`<br>9 = `a009_s2_blocked`<br>10 = `a010_s2_crossTalk`<br>11 = `a011_s3_overTemp`<br>12 = `a012_s3_internalFail`<br>13 = `a013_s3_linCommError`<br>14 = `a014_s3_blocked`<br>15 = `a015_s3_crossTalk`<br>16 = `a016_s4_overTemp`<br>17 = `a017_s4_internalFail`<br>18 = `a018_s4_linCommError`<br>19 = `a019_s4_blocked`<br>20 = `a020_s4_crossTalk`<br>21 = `a021_s5_overTemp`<br>22 = `a022_s5_internalFail`<br>23 = `a023_s5_linCommError`<br>24 = `a024_s5_blocked`<br>25 = `a025_s5_crossTalk`<br>26 = `a026_s6_overTemp`<br>27 = `a027_s6_internalFail`<br>28 = `a028_s6_linCommError`<br>29 = `a029_s6_blocked`<br>30 = `a030_s6_crossTalk`<br>31 = `a031_s7_overTemp`<br>32 = `a032_s7_internalFail`<br>33 = `a033_s7_linCommError`<br>34 = `a034_s7_blocked`<br>35 = `a035_s7_crossTalk`<br>36 = `a036_s8_overTemp`<br>37 = `a037_s8_internalFail`<br>38 = `a038_s8_linCommError`<br>39 = `a039_s8_blocked`<br>40 = `a040_s8_crossTalk`<br>41 = `a041_s9_overTemp`<br>42 = `a042_s9_internalFail`<br>43 = `a043_s9_linCommError`<br>44 = `a044_s9_blocked`<br>45 = `a045_s9_crossTalk`<br>46 = `a046_s10_overTemp`<br>47 = `a047_s10_internalFail`<br>48 = `a048_s10_linCommError`<br>49 = `a049_s10_blocked`<br>50 = `a050_s10_crossTalk`<br>51 = `a051_s11_overTemp`<br>52 = `a052_s11_internalFail`<br>53 = `a053_s11_linCommError`<br>54 = `a054_s11_blocked`<br>55 = `a055_s11_crossTalk`<br>56 = `a056_s12_overTemp`<br>57 = `a057_s12_internalFail`<br>58 = `a058_s12_linCommError`<br>59 = `a059_s12_blocked`<br>60 = `a060_s12_crossTalk`<br>61 = `a061_ecuUnderVoltage`<br>62 = `a062_ecuOverVoltage`<br>63 = `a063_sensorVoltage`<br>64 = `a064_ecuFault`<br>65 = `a065_crcFault`<br>66 = `a066_calibrationMissing`<br>67 = `a067_privateCANBusOff`<br>68 = `a068_hardwareWatchDog`<br>69 = `a069_dasMia`<br>70 = `a070_sccmMia`<br>71 = `a071_diMia`<br>72 = `a072_epasMia`<br>73 = `a073_epbMia`<br>74 = `a074_espMia`<br>75 = `a075_rcmMia`<br>76 = `a076_vcFrontMia`<br>77 = `a077_dasError`<br>78 = `a078_diError`<br>79 = `a079_epasError`<br>80 = `a080_epbError`<br>81 = `a081_espError`<br>82 = `a082_rcmError`<br>83 = `a083_vcFrontError`<br>84 = `a084_sccmError`<br>85 = `a085_watchdogReset`<br>86 = `a086_nvmFault`<br>87 = `a087_sensorMismatchError` | plausible |
| `PARK_alertState` |  | Parking assist sensors: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `PARK_sw001_sensorTemperature` | page 1 | Parking assist sensors: sw001 sensor temperature | 16\|16 | little-endian | unsigned | 0.1 | -40 | deg | -40 to 6513.5 |  | plausible |
| `PARK_sw002_membraneDisconct` | page 2 | Parking assist sensors: sw002 membrane disconct | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw002_dampResistorFail` | page 2 | Parking assist sensors: sw002 damp resistor fail | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw002_resonanceDrift` | page 2 | Parking assist sensors: sw002 resonance drift | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw002_sensorCRC` | page 2 | Parking assist sensors: sw002 sensor CRC | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw002_recieveFailure` | page 2 | Parking assist sensors: sw002 recieve failure | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw002_diagnosticTransferError` | page 2 | Parking assist sensors: sw002 diagnostic transfer error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw003_linError` | page 3 | Parking assist sensors: sw003 lin error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw003_linBusError` | page 3 | Parking assist sensors: sw003 lin bus error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw003_linFrameCountError` | page 3 | Parking assist sensors: sw003 lin frame count error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw004_reverbPeriod` | page 4 | Parking assist sensors: sw004 reverb period | 16\|16 | little-endian | unsigned | 1 | 0 | microseconds | 0 to 65535 |  | plausible |
| `PARK_sw004_reverbTime` | page 4 | Parking assist sensors: sw004 reverb time | 32\|16 | little-endian | unsigned | 1 | 0 | microseconds | 0 to 65535 |  | plausible |
| `PARK_sw004_highAttenTime` | page 4 | Parking assist sensors: sw004 high atten time | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw004_closeConstEcho` | page 4 | Parking assist sensors: sw004 close const echo | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw004_lowAttenTime` | page 4 | Parking assist sensors: sw004 low atten time | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw004_attenTimeJitter` | page 4 | Parking assist sensors: sw004 atten time jitter | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw004_reverbFreqJitter` | page 4 | Parking assist sensors: sw004 reverb freq jitter | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw006_sensorTemperature` | page 6 | Parking assist sensors: sw006 sensor temperature | 16\|16 | little-endian | unsigned | 0.1 | -40 | deg | -40 to 6513.5 |  | plausible |
| `PARK_sw007_membraneDisconct` | page 7 | Parking assist sensors: sw007 membrane disconct | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw007_dampResistorFail` | page 7 | Parking assist sensors: sw007 damp resistor fail | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw007_resonanceDrift` | page 7 | Parking assist sensors: sw007 resonance drift | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw007_sensorCRC` | page 7 | Parking assist sensors: sw007 sensor CRC | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw007_recieveFailure` | page 7 | Parking assist sensors: sw007 recieve failure | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw007_diagnosticTransferError` | page 7 | Parking assist sensors: sw007 diagnostic transfer error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw008_linError` | page 8 | Parking assist sensors: sw008 lin error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw008_linBusError` | page 8 | Parking assist sensors: sw008 lin bus error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw008_linFrameCountError` | page 8 | Parking assist sensors: sw008 lin frame count error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw009_reverbPeriod` | page 9 | Parking assist sensors: sw009 reverb period | 16\|16 | little-endian | unsigned | 1 | 0 | microseconds | 0 to 65535 |  | plausible |
| `PARK_sw009_reverbTime` | page 9 | Parking assist sensors: sw009 reverb time | 32\|16 | little-endian | unsigned | 1 | 0 | microseconds | 0 to 65535 |  | plausible |
| `PARK_sw009_highAttenTime` | page 9 | Parking assist sensors: sw009 high atten time | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw009_closeConstEcho` | page 9 | Parking assist sensors: sw009 close const echo | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw009_lowAttenTime` | page 9 | Parking assist sensors: sw009 low atten time | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw009_attenTimeJitter` | page 9 | Parking assist sensors: sw009 atten time jitter | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw009_reverbFreqJitter` | page 9 | Parking assist sensors: sw009 reverb freq jitter | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw011_sensorTemperature` | page 11 | Parking assist sensors: sw011 sensor temperature | 16\|16 | little-endian | unsigned | 0.1 | -40 | deg | -40 to 6513.5 |  | plausible |
| `PARK_sw012_membraneDisconct` | page 12 | Parking assist sensors: sw012 membrane disconct | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw012_dampResistorFail` | page 12 | Parking assist sensors: sw012 damp resistor fail | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw012_resonanceDrift` | page 12 | Parking assist sensors: sw012 resonance drift | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw012_sensorCRC` | page 12 | Parking assist sensors: sw012 sensor CRC | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw012_recieveFailure` | page 12 | Parking assist sensors: sw012 recieve failure | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw012_diagnosticTransferError` | page 12 | Parking assist sensors: sw012 diagnostic transfer error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw013_linError` | page 13 | Parking assist sensors: sw013 lin error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw013_linBusError` | page 13 | Parking assist sensors: sw013 lin bus error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw013_linFrameCountError` | page 13 | Parking assist sensors: sw013 lin frame count error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw014_reverbPeriod` | page 14 | Parking assist sensors: sw014 reverb period | 16\|16 | little-endian | unsigned | 1 | 0 | microseconds | 0 to 65535 |  | plausible |
| `PARK_sw014_reverbTime` | page 14 | Parking assist sensors: sw014 reverb time | 32\|16 | little-endian | unsigned | 1 | 0 | microseconds | 0 to 65535 |  | plausible |
| `PARK_sw014_highAttenTime` | page 14 | Parking assist sensors: sw014 high atten time | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw014_closeConstEcho` | page 14 | Parking assist sensors: sw014 close const echo | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw014_lowAttenTime` | page 14 | Parking assist sensors: sw014 low atten time | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw014_attenTimeJitter` | page 14 | Parking assist sensors: sw014 atten time jitter | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw014_reverbFreqJitter` | page 14 | Parking assist sensors: sw014 reverb freq jitter | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw016_sensorTemperature` | page 16 | Parking assist sensors: sw016 sensor temperature | 16\|16 | little-endian | unsigned | 0.1 | -40 | deg | -40 to 6513.5 |  | plausible |
| `PARK_sw017_membraneDisconct` | page 17 | Parking assist sensors: sw017 membrane disconct | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw017_dampResistorFail` | page 17 | Parking assist sensors: sw017 damp resistor fail | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw017_resonanceDrift` | page 17 | Parking assist sensors: sw017 resonance drift | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw017_sensorCRC` | page 17 | Parking assist sensors: sw017 sensor CRC | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw017_recieveFailure` | page 17 | Parking assist sensors: sw017 recieve failure | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw017_diagnosticTransferError` | page 17 | Parking assist sensors: sw017 diagnostic transfer error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw018_linError` | page 18 | Parking assist sensors: sw018 lin error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw018_linBusError` | page 18 | Parking assist sensors: sw018 lin bus error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw018_linFrameCountError` | page 18 | Parking assist sensors: sw018 lin frame count error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw019_reverbPeriod` | page 19 | Parking assist sensors: sw019 reverb period | 16\|16 | little-endian | unsigned | 1 | 0 | microseconds | 0 to 65535 |  | plausible |
| `PARK_sw019_reverbTime` | page 19 | Parking assist sensors: sw019 reverb time | 32\|16 | little-endian | unsigned | 1 | 0 | microseconds | 0 to 65535 |  | plausible |
| `PARK_sw019_highAttenTime` | page 19 | Parking assist sensors: sw019 high atten time | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw019_closeConstEcho` | page 19 | Parking assist sensors: sw019 close const echo | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw019_lowAttenTime` | page 19 | Parking assist sensors: sw019 low atten time | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw019_attenTimeJitter` | page 19 | Parking assist sensors: sw019 atten time jitter | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw019_reverbFreqJitter` | page 19 | Parking assist sensors: sw019 reverb freq jitter | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw021_sensorTemperature` | page 21 | Parking assist sensors: sw021 sensor temperature | 16\|16 | little-endian | unsigned | 0.1 | -40 | deg | -40 to 6513.5 |  | plausible |
| `PARK_sw022_membraneDisconct` | page 22 | Parking assist sensors: sw022 membrane disconct | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw022_dampResistorFail` | page 22 | Parking assist sensors: sw022 damp resistor fail | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw022_resonanceDrift` | page 22 | Parking assist sensors: sw022 resonance drift | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw022_sensorCRC` | page 22 | Parking assist sensors: sw022 sensor CRC | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw022_recieveFailure` | page 22 | Parking assist sensors: sw022 recieve failure | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw022_diagnosticTransferError` | page 22 | Parking assist sensors: sw022 diagnostic transfer error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw023_linError` | page 23 | Parking assist sensors: sw023 lin error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw023_linBusError` | page 23 | Parking assist sensors: sw023 lin bus error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw023_linFrameCountError` | page 23 | Parking assist sensors: sw023 lin frame count error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw024_reverbPeriod` | page 24 | Parking assist sensors: sw024 reverb period | 16\|16 | little-endian | unsigned | 1 | 0 | microseconds | 0 to 65535 |  | plausible |
| `PARK_sw024_reverbTime` | page 24 | Parking assist sensors: sw024 reverb time | 32\|16 | little-endian | unsigned | 1 | 0 | microseconds | 0 to 65535 |  | plausible |
| `PARK_sw024_highAttenTime` | page 24 | Parking assist sensors: sw024 high atten time | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw024_closeConstEcho` | page 24 | Parking assist sensors: sw024 close const echo | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw024_lowAttenTime` | page 24 | Parking assist sensors: sw024 low atten time | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw024_attenTimeJitter` | page 24 | Parking assist sensors: sw024 atten time jitter | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw024_reverbFreqJitter` | page 24 | Parking assist sensors: sw024 reverb freq jitter | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw026_sensorTemperature` | page 26 | Parking assist sensors: sw026 sensor temperature | 16\|16 | little-endian | unsigned | 0.1 | -40 | deg | -40 to 6513.5 |  | plausible |
| `PARK_sw027_membraneDisconct` | page 27 | Parking assist sensors: sw027 membrane disconct | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw027_dampResistorFail` | page 27 | Parking assist sensors: sw027 damp resistor fail | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw027_resonanceDrift` | page 27 | Parking assist sensors: sw027 resonance drift | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw027_sensorCRC` | page 27 | Parking assist sensors: sw027 sensor CRC | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw027_recieveFailure` | page 27 | Parking assist sensors: sw027 recieve failure | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw027_diagnosticTransferError` | page 27 | Parking assist sensors: sw027 diagnostic transfer error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw028_linError` | page 28 | Parking assist sensors: sw028 lin error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw028_linBusError` | page 28 | Parking assist sensors: sw028 lin bus error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw028_linFrameCountError` | page 28 | Parking assist sensors: sw028 lin frame count error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw029_reverbPeriod` | page 29 | Parking assist sensors: sw029 reverb period | 16\|16 | little-endian | unsigned | 1 | 0 | microseconds | 0 to 65535 |  | plausible |
| `PARK_sw029_reverbTime` | page 29 | Parking assist sensors: sw029 reverb time | 32\|16 | little-endian | unsigned | 1 | 0 | microseconds | 0 to 65535 |  | plausible |
| `PARK_sw029_highAttenTime` | page 29 | Parking assist sensors: sw029 high atten time | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw029_closeConstEcho` | page 29 | Parking assist sensors: sw029 close const echo | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw029_lowAttenTime` | page 29 | Parking assist sensors: sw029 low atten time | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw029_attenTimeJitter` | page 29 | Parking assist sensors: sw029 atten time jitter | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw029_reverbFreqJitter` | page 29 | Parking assist sensors: sw029 reverb freq jitter | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw031_sensorTemperature` | page 31 | Parking assist sensors: sw031 sensor temperature | 16\|16 | little-endian | unsigned | 0.1 | -40 | deg | -40 to 6513.5 |  | plausible |
| `PARK_sw032_membraneDisconct` | page 32 | Parking assist sensors: sw032 membrane disconct | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw032_dampResistorFail` | page 32 | Parking assist sensors: sw032 damp resistor fail | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw032_resonanceDrift` | page 32 | Parking assist sensors: sw032 resonance drift | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw032_sensorCRC` | page 32 | Parking assist sensors: sw032 sensor CRC | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw032_recieveFailure` | page 32 | Parking assist sensors: sw032 recieve failure | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw032_diagnosticTransferError` | page 32 | Parking assist sensors: sw032 diagnostic transfer error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw033_linError` | page 33 | Parking assist sensors: sw033 lin error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw033_linBusError` | page 33 | Parking assist sensors: sw033 lin bus error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw033_linFrameCountError` | page 33 | Parking assist sensors: sw033 lin frame count error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw034_reverbPeriod` | page 34 | Parking assist sensors: sw034 reverb period | 16\|16 | little-endian | unsigned | 1 | 0 | microseconds | 0 to 65535 |  | plausible |
| `PARK_sw034_reverbTime` | page 34 | Parking assist sensors: sw034 reverb time | 32\|16 | little-endian | unsigned | 1 | 0 | microseconds | 0 to 65535 |  | plausible |
| `PARK_sw034_highAttenTime` | page 34 | Parking assist sensors: sw034 high atten time | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw034_closeConstEcho` | page 34 | Parking assist sensors: sw034 close const echo | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw034_lowAttenTime` | page 34 | Parking assist sensors: sw034 low atten time | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw034_attenTimeJitter` | page 34 | Parking assist sensors: sw034 atten time jitter | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw034_reverbFreqJitter` | page 34 | Parking assist sensors: sw034 reverb freq jitter | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw036_sensorTemperature` | page 36 | Parking assist sensors: sw036 sensor temperature | 16\|16 | little-endian | unsigned | 0.1 | -40 | deg | -40 to 6513.5 |  | plausible |
| `PARK_sw037_membraneDisconct` | page 37 | Parking assist sensors: sw037 membrane disconct | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw037_dampResistorFail` | page 37 | Parking assist sensors: sw037 damp resistor fail | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw037_resonanceDrift` | page 37 | Parking assist sensors: sw037 resonance drift | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw037_sensorCRC` | page 37 | Parking assist sensors: sw037 sensor CRC | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw037_recieveFailure` | page 37 | Parking assist sensors: sw037 recieve failure | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw037_diagnosticTransferError` | page 37 | Parking assist sensors: sw037 diagnostic transfer error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw038_linError` | page 38 | Parking assist sensors: sw038 lin error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw038_linBusError` | page 38 | Parking assist sensors: sw038 lin bus error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw038_linFrameCountError` | page 38 | Parking assist sensors: sw038 lin frame count error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw039_reverbPeriod` | page 39 | Parking assist sensors: sw039 reverb period | 16\|16 | little-endian | unsigned | 1 | 0 | microseconds | 0 to 65535 |  | plausible |
| `PARK_sw039_reverbTime` | page 39 | Parking assist sensors: sw039 reverb time | 32\|16 | little-endian | unsigned | 1 | 0 | microseconds | 0 to 65535 |  | plausible |
| `PARK_sw039_highAttenTime` | page 39 | Parking assist sensors: sw039 high atten time | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw039_closeConstEcho` | page 39 | Parking assist sensors: sw039 close const echo | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw039_lowAttenTime` | page 39 | Parking assist sensors: sw039 low atten time | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw039_attenTimeJitter` | page 39 | Parking assist sensors: sw039 atten time jitter | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw039_reverbFreqJitter` | page 39 | Parking assist sensors: sw039 reverb freq jitter | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw041_sensorTemperature` | page 41 | Parking assist sensors: sw041 sensor temperature | 16\|16 | little-endian | unsigned | 0.1 | -40 | deg | -40 to 6513.5 |  | plausible |
| `PARK_sw042_membraneDisconct` | page 42 | Parking assist sensors: sw042 membrane disconct | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw042_dampResistorFail` | page 42 | Parking assist sensors: sw042 damp resistor fail | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw042_resonanceDrift` | page 42 | Parking assist sensors: sw042 resonance drift | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw042_sensorCRC` | page 42 | Parking assist sensors: sw042 sensor CRC | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw042_recieveFailure` | page 42 | Parking assist sensors: sw042 recieve failure | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw042_diagnosticTransferError` | page 42 | Parking assist sensors: sw042 diagnostic transfer error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw043_linError` | page 43 | Parking assist sensors: sw043 lin error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw043_linBusError` | page 43 | Parking assist sensors: sw043 lin bus error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw043_linFrameCountError` | page 43 | Parking assist sensors: sw043 lin frame count error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw044_reverbPeriod` | page 44 | Parking assist sensors: sw044 reverb period | 16\|16 | little-endian | unsigned | 1 | 0 | microseconds | 0 to 65535 |  | plausible |
| `PARK_sw044_reverbTime` | page 44 | Parking assist sensors: sw044 reverb time | 32\|16 | little-endian | unsigned | 1 | 0 | microseconds | 0 to 65535 |  | plausible |
| `PARK_sw044_highAttenTime` | page 44 | Parking assist sensors: sw044 high atten time | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw044_closeConstEcho` | page 44 | Parking assist sensors: sw044 close const echo | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw044_lowAttenTime` | page 44 | Parking assist sensors: sw044 low atten time | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw044_attenTimeJitter` | page 44 | Parking assist sensors: sw044 atten time jitter | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw044_reverbFreqJitter` | page 44 | Parking assist sensors: sw044 reverb freq jitter | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw046_sensorTemperature` | page 46 | Parking assist sensors: sw046 sensor temperature | 16\|16 | little-endian | unsigned | 0.1 | -40 | deg | -40 to 6513.5 |  | plausible |
| `PARK_sw047_membraneDisconct` | page 47 | Parking assist sensors: sw047 membrane disconct | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw047_dampResistorFail` | page 47 | Parking assist sensors: sw047 damp resistor fail | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw047_resonanceDrift` | page 47 | Parking assist sensors: sw047 resonance drift | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw047_sensorCRC` | page 47 | Parking assist sensors: sw047 sensor CRC | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw047_recieveFailure` | page 47 | Parking assist sensors: sw047 recieve failure | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw047_diagnosticTransferError` | page 47 | Parking assist sensors: sw047 diagnostic transfer error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw048_linError` | page 48 | Parking assist sensors: sw048 lin error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw048_linBusError` | page 48 | Parking assist sensors: sw048 lin bus error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw048_linFrameCountError` | page 48 | Parking assist sensors: sw048 lin frame count error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw049_reverbPeriod` | page 49 | Parking assist sensors: sw049 reverb period | 16\|16 | little-endian | unsigned | 1 | 0 | microseconds | 0 to 65535 |  | plausible |
| `PARK_sw049_reverbTime` | page 49 | Parking assist sensors: sw049 reverb time | 32\|16 | little-endian | unsigned | 1 | 0 | microseconds | 0 to 65535 |  | plausible |
| `PARK_sw049_highAttenTime` | page 49 | Parking assist sensors: sw049 high atten time | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw049_closeConstEcho` | page 49 | Parking assist sensors: sw049 close const echo | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw049_lowAttenTime` | page 49 | Parking assist sensors: sw049 low atten time | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw049_attenTimeJitter` | page 49 | Parking assist sensors: sw049 atten time jitter | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw049_reverbFreqJitter` | page 49 | Parking assist sensors: sw049 reverb freq jitter | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw051_sensorTemperature` | page 51 | Parking assist sensors: sw051 sensor temperature | 16\|16 | little-endian | unsigned | 0.1 | -40 | deg | -40 to 6513.5 |  | plausible |
| `PARK_sw052_membraneDisconct` | page 52 | Parking assist sensors: sw052 membrane disconct | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw052_dampResistorFail` | page 52 | Parking assist sensors: sw052 damp resistor fail | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw052_resonanceDrift` | page 52 | Parking assist sensors: sw052 resonance drift | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw052_sensorCRC` | page 52 | Parking assist sensors: sw052 sensor CRC | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw052_recieveFailure` | page 52 | Parking assist sensors: sw052 recieve failure | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw052_diagnosticTransferError` | page 52 | Parking assist sensors: sw052 diagnostic transfer error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw053_linError` | page 53 | Parking assist sensors: sw053 lin error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw053_linBusError` | page 53 | Parking assist sensors: sw053 lin bus error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw053_linFrameCountError` | page 53 | Parking assist sensors: sw053 lin frame count error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw054_reverbPeriod` | page 54 | Parking assist sensors: sw054 reverb period | 16\|16 | little-endian | unsigned | 1 | 0 | microseconds | 0 to 65535 |  | plausible |
| `PARK_sw054_reverbTime` | page 54 | Parking assist sensors: sw054 reverb time | 32\|16 | little-endian | unsigned | 1 | 0 | microseconds | 0 to 65535 |  | plausible |
| `PARK_sw054_highAttenTime` | page 54 | Parking assist sensors: sw054 high atten time | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw054_closeConstEcho` | page 54 | Parking assist sensors: sw054 close const echo | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw054_lowAttenTime` | page 54 | Parking assist sensors: sw054 low atten time | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw054_attenTimeJitter` | page 54 | Parking assist sensors: sw054 atten time jitter | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw054_reverbFreqJitter` | page 54 | Parking assist sensors: sw054 reverb freq jitter | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw056_sensorTemperature` | page 56 | Parking assist sensors: sw056 sensor temperature | 16\|16 | little-endian | unsigned | 0.1 | -40 | deg | -40 to 6513.5 |  | plausible |
| `PARK_sw057_membraneDisconct` | page 57 | Parking assist sensors: sw057 membrane disconct | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw057_dampResistorFail` | page 57 | Parking assist sensors: sw057 damp resistor fail | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw057_resonanceDrift` | page 57 | Parking assist sensors: sw057 resonance drift | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw057_sensorCRC` | page 57 | Parking assist sensors: sw057 sensor CRC | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw057_recieveFailure` | page 57 | Parking assist sensors: sw057 recieve failure | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw057_diagnosticTransferError` | page 57 | Parking assist sensors: sw057 diagnostic transfer error | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw058_linError` | page 58 | Parking assist sensors: sw058 lin error | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw058_linBusError` | page 58 | Parking assist sensors: sw058 lin bus error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw058_linFrameCountError` | page 58 | Parking assist sensors: sw058 lin frame count error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw059_reverbPeriod` | page 59 | Parking assist sensors: sw059 reverb period | 16\|16 | little-endian | unsigned | 1 | 0 | microseconds | 0 to 65535 |  | plausible |
| `PARK_sw059_reverbTime` | page 59 | Parking assist sensors: sw059 reverb time | 32\|16 | little-endian | unsigned | 1 | 0 | microseconds | 0 to 65535 |  | plausible |
| `PARK_sw059_highAttenTime` | page 59 | Parking assist sensors: sw059 high atten time | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw059_closeConstEcho` | page 59 | Parking assist sensors: sw059 close const echo | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw059_lowAttenTime` | page 59 | Parking assist sensors: sw059 low atten time | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw059_attenTimeJitter` | page 59 | Parking assist sensors: sw059 atten time jitter | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw059_reverbFreqJitter` | page 59 | Parking assist sensors: sw059 reverb freq jitter | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw061_voltage` | page 61 | Parking assist sensors: sw061 voltage | 16\|16 | little-endian | unsigned | 0.1 | 0 | volts | 0 to 6553.5 |  | plausible |
| `PARK_sw063_voltage` | page 63 | Parking assist sensors: sw063 voltage | 16\|16 | little-endian | unsigned | 0.1 | 0 | volts | 0 to 6553.5 |  | plausible |
| `PARK_sw064_faultCode` | page 64 | Parking assist sensors: sw064 fault code | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PARK_sw065_expectedCRC` | page 65 | Parking assist sensors: sw065 expected CRC | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PARK_sw065_calculatedCRC` | page 65 | Parking assist sensors: sw065 calculated CRC | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PARK_sw066_placeHolder` | page 66 | Parking assist sensors: sw066 place holder | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw068_placeHolder` | page 68 | Parking assist sensors: sw068 place holder | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `PARK_sw069_messageID` | page 69 | Parking assist sensors: sw069 message ID | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PARK_sw070_messageID` | page 70 | Parking assist sensors: sw070 message ID | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PARK_sw071_messageID` | page 71 | Parking assist sensors: sw071 message ID | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PARK_sw072_messageID` | page 72 | Parking assist sensors: sw072 message ID | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PARK_sw073_messageID` | page 73 | Parking assist sensors: sw073 message ID | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PARK_sw074_messageID` | page 74 | Parking assist sensors: sw074 message ID | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PARK_sw075_messageID` | page 75 | Parking assist sensors: sw075 message ID | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PARK_sw076_messageID` | page 76 | Parking assist sensors: sw076 message ID | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `PARK_sw077_errorExp` | page 77 | Parking assist sensors: sw077 error exp | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PARK_sw077_errorRx` | page 77 | Parking assist sensors: sw077 error rx | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PARK_sw077_messageID` | page 77 | Parking assist sensors: sw077 message ID | 32\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `PARK_sw077_errorType` | page 77 | Parking assist sensors: sw077 error type | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `LENGTH`<br>2 = `CHECKSUM`<br>3 = `SEQUENCE`<br>4 = `INVALID_DATA`<br>5 = `OVERRUN` | plausible |
| `PARK_sw078_errorExp` | page 78 | Parking assist sensors: sw078 error exp | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PARK_sw078_errorRx` | page 78 | Parking assist sensors: sw078 error rx | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PARK_sw078_messageID` | page 78 | Parking assist sensors: sw078 message ID | 32\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `PARK_sw078_errorType` | page 78 | Parking assist sensors: sw078 error type | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `LENGTH`<br>2 = `CHECKSUM`<br>3 = `SEQUENCE`<br>4 = `INVALID_DATA`<br>5 = `OVERRUN` | plausible |
| `PARK_sw079_errorExp` | page 79 | Parking assist sensors: sw079 error exp | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PARK_sw079_errorRx` | page 79 | Parking assist sensors: sw079 error rx | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PARK_sw079_messageID` | page 79 | Parking assist sensors: sw079 message ID | 32\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `PARK_sw079_errorType` | page 79 | Parking assist sensors: sw079 error type | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `LENGTH`<br>2 = `CHECKSUM`<br>3 = `SEQUENCE`<br>4 = `INVALID_DATA`<br>5 = `OVERRUN` | plausible |
| `PARK_sw080_errorExp` | page 80 | Parking assist sensors: sw080 error exp | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PARK_sw080_errorRx` | page 80 | Parking assist sensors: sw080 error rx | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PARK_sw080_messageID` | page 80 | Parking assist sensors: sw080 message ID | 32\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `PARK_sw080_errorType` | page 80 | Parking assist sensors: sw080 error type | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `LENGTH`<br>2 = `CHECKSUM`<br>3 = `SEQUENCE`<br>4 = `INVALID_DATA`<br>5 = `OVERRUN` | plausible |
| `PARK_sw081_errorExp` | page 81 | Parking assist sensors: sw081 error exp | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PARK_sw081_errorRx` | page 81 | Parking assist sensors: sw081 error rx | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PARK_sw081_messageID` | page 81 | Parking assist sensors: sw081 message ID | 32\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `PARK_sw081_errorType` | page 81 | Parking assist sensors: sw081 error type | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `LENGTH`<br>2 = `CHECKSUM`<br>3 = `SEQUENCE`<br>4 = `INVALID_DATA`<br>5 = `OVERRUN` | plausible |
| `PARK_sw082_errorExp` | page 82 | Parking assist sensors: sw082 error exp | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PARK_sw082_errorRx` | page 82 | Parking assist sensors: sw082 error rx | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PARK_sw082_messageID` | page 82 | Parking assist sensors: sw082 message ID | 32\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `PARK_sw082_errorType` | page 82 | Parking assist sensors: sw082 error type | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `LENGTH`<br>2 = `CHECKSUM`<br>3 = `SEQUENCE`<br>4 = `INVALID_DATA`<br>5 = `OVERRUN` | plausible |
| `PARK_sw083_errorExp` | page 83 | Parking assist sensors: sw083 error exp | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PARK_sw083_errorRx` | page 83 | Parking assist sensors: sw083 error rx | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PARK_sw083_messageID` | page 83 | Parking assist sensors: sw083 message ID | 32\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `PARK_sw083_errorType` | page 83 | Parking assist sensors: sw083 error type | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `LENGTH`<br>2 = `CHECKSUM`<br>3 = `SEQUENCE`<br>4 = `INVALID_DATA`<br>5 = `OVERRUN` | plausible |
| `PARK_sw084_errorExp` | page 84 | Parking assist sensors: sw084 error exp | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PARK_sw084_errorRx` | page 84 | Parking assist sensors: sw084 error rx | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PARK_sw084_messageID` | page 84 | Parking assist sensors: sw084 message ID | 32\|12 | little-endian | unsigned | 1 | 0 |  | 0 to 4095 |  | layout-only |
| `PARK_sw084_errorType` | page 84 | Parking assist sensors: sw084 error type | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `LENGTH`<br>2 = `CHECKSUM`<br>3 = `SEQUENCE`<br>4 = `INVALID_DATA`<br>5 = `OVERRUN` | plausible |
| `PARK_sw086_writeRetryCounter` | page 86 | Parking assist sensors: sw086 write retry counter | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PARK_sw086_readRetryCounter` | page 86 | Parking assist sensors: sw086 read retry counter | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PARK_sw086_currentErrorCode` | page 86 | Parking assist sensors: sw086 current error code | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `PARK_sw087_s1_sensorType` | page 87 | Parking assist sensors: sw087 s1 sensor type; raw 3 = signal not available (SNA) | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NONE`<br>1 = `VALEO_HPFL`<br>2 = `VALEO_HP`<br>3 = `SNA` | plausible |
| `PARK_sw087_s2_sensorType` | page 87 | Parking assist sensors: sw087 s2 sensor type; raw 3 = signal not available (SNA) | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NONE`<br>1 = `VALEO_HPFL`<br>2 = `VALEO_HP`<br>3 = `SNA` | plausible |
| `PARK_sw087_s3_sensorType` | page 87 | Parking assist sensors: sw087 s3 sensor type; raw 3 = signal not available (SNA) | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NONE`<br>1 = `VALEO_HPFL`<br>2 = `VALEO_HP`<br>3 = `SNA` | plausible |
| `PARK_sw087_s4_sensorType` | page 87 | Parking assist sensors: sw087 s4 sensor type; raw 3 = signal not available (SNA) | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NONE`<br>1 = `VALEO_HPFL`<br>2 = `VALEO_HP`<br>3 = `SNA` | plausible |
| `PARK_sw087_s5_sensorType` | page 87 | Parking assist sensors: sw087 s5 sensor type; raw 3 = signal not available (SNA) | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NONE`<br>1 = `VALEO_HPFL`<br>2 = `VALEO_HP`<br>3 = `SNA` | plausible |
| `PARK_sw087_s6_sensorType` | page 87 | Parking assist sensors: sw087 s6 sensor type; raw 3 = signal not available (SNA) | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NONE`<br>1 = `VALEO_HPFL`<br>2 = `VALEO_HP`<br>3 = `SNA` | plausible |
| `PARK_sw087_s7_sensorType` | page 87 | Parking assist sensors: sw087 s7 sensor type; raw 3 = signal not available (SNA) | 28\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NONE`<br>1 = `VALEO_HPFL`<br>2 = `VALEO_HP`<br>3 = `SNA` | plausible |
| `PARK_sw087_s8_sensorType` | page 87 | Parking assist sensors: sw087 s8 sensor type; raw 3 = signal not available (SNA) | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NONE`<br>1 = `VALEO_HPFL`<br>2 = `VALEO_HP`<br>3 = `SNA` | plausible |
| `PARK_sw087_s9_sensorType` | page 87 | Parking assist sensors: sw087 s9 sensor type; raw 3 = signal not available (SNA) | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NONE`<br>1 = `VALEO_HPFL`<br>2 = `VALEO_HP`<br>3 = `SNA` | plausible |
| `PARK_sw087_s10_sensorType` | page 87 | Parking assist sensors: sw087 s10 sensor type; raw 3 = signal not available (SNA) | 34\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NONE`<br>1 = `VALEO_HPFL`<br>2 = `VALEO_HP`<br>3 = `SNA` | plausible |
| `PARK_sw087_s11_sensorType` | page 87 | Parking assist sensors: sw087 s11 sensor type; raw 3 = signal not available (SNA) | 36\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NONE`<br>1 = `VALEO_HPFL`<br>2 = `VALEO_HP`<br>3 = `SNA` | plausible |
| `PARK_sw087_s12_sensorType` | page 87 | Parking assist sensors: sw087 s12 sensor type; raw 3 = signal not available (SNA) | 38\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NONE`<br>1 = `VALEO_HPFL`<br>2 = `VALEO_HP`<br>3 = `SNA` | plausible |

## Multiplexing

`PARK_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (1 signals), page 2 (6 signals), page 3 (3 signals), page 4 (7 signals), page 6 (1 signals), page 7 (6 signals), page 8 (3 signals), page 9 (7 signals), page 11 (1 signals), page 12 (6 signals), page 13 (3 signals), page 14 (7 signals), page 16 (1 signals), page 17 (6 signals), page 18 (3 signals), page 19 (7 signals), page 21 (1 signals), page 22 (6 signals), page 23 (3 signals), page 24 (7 signals), page 26 (1 signals), page 27 (6 signals), page 28 (3 signals), page 29 (7 signals), page 31 (1 signals), page 32 (6 signals), page 33 (3 signals), page 34 (7 signals), page 36 (1 signals), page 37 (6 signals), page 38 (3 signals), page 39 (7 signals), page 41 (1 signals), page 42 (6 signals), page 43 (3 signals), page 44 (7 signals), page 46 (1 signals), page 47 (6 signals), page 48 (3 signals), page 49 (7 signals), page 51 (1 signals), page 52 (6 signals), page 53 (3 signals), page 54 (7 signals), page 56 (1 signals), page 57 (6 signals), page 58 (3 signals), page 59 (7 signals), page 61 (1 signals), page 63 (1 signals), page 64 (1 signals), page 65 (2 signals), page 66 (1 signals), page 68 (1 signals), page 69 (1 signals), page 70 (1 signals), page 71 (1 signals), page 72 (1 signals), page 73 (1 signals), page 74 (1 signals), page 75 (1 signals), page 76 (1 signals), page 77 (4 signals), page 78 (4 signals), page 79 (4 signals), page 80 (4 signals), page 81 (4 signals), page 82 (4 signals), page 83 (4 signals), page 84 (4 signals), page 86 (3 signals), page 87 (12 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Parking assist sensors messages (PARK)](../../park.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
