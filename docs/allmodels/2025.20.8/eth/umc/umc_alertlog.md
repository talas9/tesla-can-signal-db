---
layout: default
title: "UMC_alertLog (0x5FD) — UMC ECU, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "UMC ECU message: alert log. Ethernet-side message UMC_alertLog of UMC ECU for Tesla Model 3 / Model Y firmware 2025.20.8, 42 signals (UMC_alertID, UMC_alertType, UMC_a001_groundImpedance, UMC_a002_ccidRmsCurrent and 38 more). Bit layout, scaling, units and value tables."
---

# UMC_alertLog (0x5FD) — UMC ECU, Tesla Model 3 / Model Y 2025.20.8 ETH

UMC ECU message: alert log. This page documents the 42 signals of UMC_alertLog as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UMC_alertLog` |
| Ethernet-side id | 0x5FD (1533) |
| ECU | [UMC ECU](../../umc.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UMC |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 42 |

## Signals of UMC_alertLog

Tesla Model 3 / Model Y CAN bus signals in `UMC_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `UMC_alertID` | selector | UMC ECU: alert ID | 0\|15 | little-endian | unsigned | 1 | 0 |  | 0 to 32767 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_gndMonIntrptLineSide`<br>2 = `a002_GFCITripped`<br>3 = `a003_GFCISelfTestFault`<br>4 = `a004_inputOverVoltage`<br>5 = `a005_inputUnderVoltage`<br>6 = `a006_contactorWelded`<br>7 = `a007_pcbaOT`<br>8 = `a008_wallPlugOT`<br>9 = `a009_vehConnOT`<br>10 = `a010_inputOT`<br>11 = `a011_proxDisconnected`<br>12 = `a012_pilotFault`<br>13 = `a013_SA_Temperature`<br>14 = `a014_SA_Genealogy`<br>15 = `a015_SA_Connection`<br>16 = `a016_pcbaOTFoldback`<br>17 = `a017_wallPlugOTFoldback`<br>18 = `a018_vehConnOTFoldback`<br>19 = `a019_inputOTFoldback`<br>20 = `a020_applicationCRC`<br>21 = `a021_dataBus`<br>22 = `a022_criticalRAM`<br>23 = `a023_adcSelfTest`<br>24 = `a024_gndResistanceHigh`<br>25 = `a025_cntrOpenExpectedClose`<br>26 = `a026_vRefOutOfRange`<br>27 = `a027_watchdogExpired`<br>28 = `a028_processorBooted`<br>29 = `a029_acPowerLoss`<br>30 = `a030_acLostPllLock`<br>31 = `a031_relayCoilVIrrational`<br>32 = `a032_chcVitalsRequestFailure`<br>33 = `a033_chcUpdateFault`<br>34 = `a034_v2lSAUnsupported`<br>35 = `a035_v2lHVACDetected`<br>37 = `a037_GFCICalibration`<br>38 = `a038_chcVitalsFault`<br>39 = `a039_inputOverCurrent`<br>40 = `a040_gndDisconnected` | plausible |
| `UMC_alertType` |  | UMC ECU: alert type | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `UMC_a001_groundImpedance` | page 1 | UMC ECU: a001 ground impedance | 32\|32 | little-endian | unsigned | 1 | 0 | Ohm | 0 to 4294967295 |  | plausible |
| `UMC_a002_ccidRmsCurrent` | page 2 | UMC ECU: a002 ccid rms current | 16\|12 | little-endian | unsigned | 0.001 | 0 | A | 0 to 4.095 |  | plausible |
| `UMC_a002_ccidRmsCurrentAvg` | page 2 | UMC ECU: a002 ccid rms current avg | 28\|12 | little-endian | unsigned | 0.001 | 0 | A | 0 to 4.095 |  | plausible |
| `UMC_a002_ccidFaultReason` | page 2 | UMC ECU: a002 ccid fault reason; raw 0 = signal not available (SNA) | 50\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `SNA`<br>1 = `AC_LPF`<br>2 = `AC_PEAK`<br>3 = `DC_LPF`<br>4 = `DC_PEAK` | plausible |
| `UMC_a002_ccidFaultBucket` | page 2 | UMC ECU: a002 ccid fault bucket | 54\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `UMC_a003_faultType` | page 3 | UMC ECU: a003 fault type | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `POWERON`<br>1 = `SELFTEST` | plausible |
| `UMC_a003_ccidSelfTestDuty` | page 3 | UMC ECU: a003 ccid self test duty | 24\|16 | little-endian | unsigned | 0.0001 | 50 | A | 50 to 56.5535 |  | plausible |
| `UMC_a003_ccidSelfTestCurrent` | page 3 | UMC ECU: a003 ccid self test current | 40\|16 | little-endian | unsigned | 0.0001 | 0 | A | 0 to 6.5535 |  | plausible |
| `UMC_a004_lineVoltage` | page 4 | UMC ECU: a004 line voltage | 16\|16 | little-endian | unsigned | 1 | 0 | Vrms | 0 to 65535 |  | plausible |
| `UMC_a004_inputVoltage` | page 4 | UMC ECU: a004 input voltage | 32\|16 | little-endian | unsigned | 0.01 | 0 | V | 0 to 655.35 |  | plausible |
| `UMC_a004_inputNeutralVoltage` | page 4 | UMC ECU: a004 input neutral voltage | 48\|16 | little-endian | unsigned | 0.01 | 0 | V | 0 to 655.35 |  | plausible |
| `UMC_a005_lineVoltage` | page 5 | UMC ECU: a005 line voltage | 16\|16 | little-endian | unsigned | 1 | 0 | Vrms | 0 to 65535 |  | plausible |
| `UMC_a005_inputVoltage` | page 5 | UMC ECU: a005 input voltage | 32\|16 | little-endian | unsigned | 0.01 | 0 | V | 0 to 655.35 |  | plausible |
| `UMC_a005_inputNeutralVoltage` | page 5 | UMC ECU: a005 input neutral voltage | 48\|16 | little-endian | unsigned | 0.01 | 0 | V | 0 to 655.35 |  | plausible |
| `UMC_a006_outputVoltage` | page 6 | UMC ECU: a006 output voltage | 16\|16 | little-endian | unsigned | 1 | 0 | Vrms | 0 to 65535 |  | plausible |
| `UMC_a006_faultType` | page 6 | UMC ECU: a006 fault type | 32\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `WELDED`<br>1 = `OPENED` | plausible |
| `UMC_a006_umcReceptacleVoltage` | page 6 | UMC ECU: a006 umc receptacle voltage | 36\|12 | little-endian | unsigned | 0.1 | 0 | V | 0 to 409.5 |  | plausible |
| `UMC_a006_handleVoltage` | page 6 | UMC ECU: a006 handle voltage | 48\|12 | little-endian | unsigned | 0.1 | 0 | V | 0 to 409.5 |  | plausible |
| `UMC_a006_line1StuckClosed` | page 6 | UMC ECU: a006 line1 stuck closed | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a006_line2StuckClosed` | page 6 | UMC ECU: a006 line2 stuck closed | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `UMC_a007_pcbaTemp` | page 7 | UMC ECU: a007 pcba temp | 16\|16 | little-endian | unsigned | 1 | 0 | degC | 0 to 65535 |  | plausible |
| `UMC_a008_wallPlugTemp` | page 8 | UMC ECU: a008 wall plug temp | 16\|16 | little-endian | unsigned | 1 | 0 | degC | 0 to 65535 |  | plausible |
| `UMC_a008_SA_region` | page 8 | UMC ECU: a008 SA region | 32\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `UMC_a008_SA_current` | page 8 | UMC ECU: a008 SA current | 40\|8 | little-endian | unsigned | 1 | 0 | A | 0 to 255 |  | plausible |
| `UMC_a009_vehConnTemp` | page 9 | UMC ECU: a009 veh conn temp | 16\|16 | little-endian | unsigned | 1 | 0 | degC | 0 to 65535 |  | plausible |
| `UMC_a010_inputTerminalsTemp` | page 10 | UMC ECU: a010 input terminals temp | 16\|16 | little-endian | unsigned | 1 | 0 | degC | 0 to 65535 |  | plausible |
| `UMC_a012_pilotHigh` | page 12 | UMC ECU: a012 pilot high | 16\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `UMC_a012_pilotLow` | page 12 | UMC ECU: a012 pilot low | 28\|12 | little-endian | signed | 0.01 | 0 | V | -20.48 to 20.47 |  | plausible |
| `UMC_a013_SA_region` | page 13 | UMC ECU: a013 SA region | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `UMC_a013_SA_current` | page 13 | UMC ECU: a013 SA current | 24\|8 | little-endian | unsigned | 1 | 0 | A | 0 to 255 |  | plausible |
| `UMC_a015_SA_region` | page 15 | UMC ECU: a015 SA region | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `UMC_a015_SA_current` | page 15 | UMC ECU: a015 SA current | 24\|8 | little-endian | unsigned | 1 | 0 | A | 0 to 255 |  | plausible |
| `UMC_a016_pcbaTemp` | page 16 | UMC ECU: a016 pcba temp | 16\|16 | little-endian | unsigned | 1 | 0 | degC | 0 to 65535 |  | plausible |
| `UMC_a017_wallPlugTemp` | page 17 | UMC ECU: a017 wall plug temp | 16\|16 | little-endian | unsigned | 1 | 0 | degC | 0 to 65535 |  | plausible |
| `UMC_a017_SA_region` | page 17 | UMC ECU: a017 SA region | 32\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `UMC_a017_SA_current` | page 17 | UMC ECU: a017 SA current | 40\|8 | little-endian | unsigned | 1 | 0 | A | 0 to 255 |  | plausible |
| `UMC_a018_vehConnTemp` | page 18 | UMC ECU: a018 veh conn temp | 16\|16 | little-endian | unsigned | 1 | 0 | degC | 0 to 65535 | 214 = `OPENED`<br>215 = `SHORTED` | plausible |
| `UMC_a019_inputTerminalsTemp` | page 19 | UMC ECU: a019 input terminals temp | 16\|16 | little-endian | unsigned | 1 | 0 | degC | 0 to 65535 | 214 = `OPENED`<br>215 = `SHORTED` | plausible |
| `UMC_a024_groundImpedance` | page 24 | UMC ECU: a024 ground impedance | 32\|32 | little-endian | unsigned | 1 | 0 | Ohm | 0 to 4294967295 |  | plausible |
| `UMC_a040_groundImpedance` | page 40 | UMC ECU: a040 ground impedance | 32\|32 | little-endian | unsigned | 1 | 0 | Ohm | 0 to 4294967295 |  | plausible |

## Multiplexing

`UMC_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (1 signals), page 2 (4 signals), page 3 (3 signals), page 4 (3 signals), page 5 (3 signals), page 6 (6 signals), page 7 (1 signals), page 8 (3 signals), page 9 (1 signals), page 10 (1 signals), page 12 (2 signals), page 13 (2 signals), page 15 (2 signals), page 16 (1 signals), page 17 (3 signals), page 18 (1 signals), page 19 (1 signals), page 24 (1 signals), page 40 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All UMC ECU messages (UMC)](../../umc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
