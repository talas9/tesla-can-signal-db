---
layout: default
title: "DIF_debug (0x757) — Front drive inverter, Tesla Model Y 2026.26.6.5 PARTY CAN"
description: "Front drive inverter message: debug. Tesla Model Y CAN bus message DIF_debug (0x757) of Front drive inverter, firmware 2026.26.6.5, 79 signals (DIF_debugSelector, DIF_motorIA, DIF_motorIB, DIF_motorIC and 75 more). Bit layout, scaling, units and value tables."
---

# DIF_debug (0x757) — Front drive inverter, Tesla Model Y 2026.26.6.5 PARTY CAN

Front drive inverter message: debug; frame length from the layout, not yet observed on a vehicle bus. This page documents the 79 signals of DIF_debug as defined for Tesla Model Y firmware 2026.26.6.5 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DIF_debug` |
| CAN id | 0x757 (1879) |
| ECU | [Front drive inverter](../../dif.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | DIF |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 79 |

## Signals of DIF_debug

Tesla Model Y CAN bus signals in `DIF_debug`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `DIF_debugSelector` | selector | Front drive inverter: debug selector | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 32 = `Mux32`<br>33 = `Mux33`<br>34 = `Mux34`<br>35 = `Mux35`<br>36 = `Mux36`<br>37 = `Mux37`<br>38 = `Mux38`<br>39 = `Mux39`<br>40 = `Mux40`<br>41 = `Mux41`<br>42 = `Mux42`<br>43 = `Mux43`<br>44 = `Mux44`<br>46 = `Mux46`<br>47 = `Mux47`<br>48 = `Mux48`<br>49 = `Mux49`<br>50 = `Mux50`<br>52 = `Mux52`<br>63 = `Mux63`<br>64 = `Mux64`<br>66 = `Mux66`<br>67 = `Mux67`<br>68 = `Mux68`<br>69 = `Mux69`<br>70 = `Mux70`<br>72 = `Mux72`<br>73 = `Mux73`<br>128 = `Mux128`<br>131 = `Mux131`<br>132 = `Mux132` | plausible |
| `DIF_motorIA` | page 32 | Position from firmware; message assignment inferred. | 8\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `DIF_motorIB` | page 32 | Position from firmware; message assignment inferred. | 24\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `DIF_motorIC` | page 32 | Position from firmware; message assignment inferred. | 40\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `DIF_statorIDref` | page 33 | Position from firmware; message assignment inferred. | 8\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 |  | plausible |
| `DIF_statorIDfdb` | page 33 | Position from firmware; message assignment inferred. | 24\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 |  | plausible |
| `DIF_torquePerAmp` | page 33 | Position from firmware; message assignment inferred. | 40\|16 | little-endian | unsigned | 0.0001 | 0 | Nm/A | 0 to 6.5535 |  | plausible |
| `DIF_rsScale` | page 34 | Position from firmware; message assignment inferred. | 8\|8 | little-endian | unsigned | 0.01 | 0 | scale | 0 to 2.55 |  | plausible |
| `DIF_statorIQref` | page 34 | Position from firmware; message assignment inferred. | 16\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 |  | plausible |
| `DIF_statorIQfdb` | page 34 | Position from firmware; message assignment inferred. | 32\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 |  | plausible |
| `DIF_motorV` | page 34 | Position from firmware; message assignment inferred. | 48\|16 | little-endian | unsigned | 2.0e-05 | 0 | mindex | 0 to 1.3107 |  | plausible |
| `DIF_tqScaleDifferential` | page 35 | Position from firmware; message assignment inferred. | 8\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 |  | plausible |
| `DIF_statorFluxRef` | page 35 | Position from firmware; message assignment inferred. | 16\|16 | little-endian | unsigned | 0.0001 | 0 | Wb | 0 to 6.5535 |  | plausible |
| `DIF_statorFluxFdb` | page 35 | Position from firmware; message assignment inferred. | 32\|16 | little-endian | unsigned | 0.0001 | 0 | Wb | 0 to 6.5535 |  | plausible |
| `DIF_lmScale` | page 36 | Position from firmware; message assignment inferred. | 8\|8 | little-endian | unsigned | 0.004 | 0 | scale | 0 to 1.02 |  | plausible |
| `DIF_statorVQ` | page 36 | Position from firmware; message assignment inferred. | 16\|16 | little-endian | signed | 4.0e-05 | 0 | mindex | -1.31072 to 1.31068 |  | plausible |
| `DIF_statorVD` | page 36 | Position from firmware; message assignment inferred. | 32\|16 | little-endian | signed | 4.0e-05 | 0 | mindex | -1.31072 to 1.31068 |  | plausible |
| `DIF_peakFlux` | page 36 | Position from firmware; message assignment inferred. | 48\|16 | little-endian | unsigned | 0.0001 | 0 | Wb | 0 to 6.5535 |  | plausible |
| `DIF_gainScale` | page 37 | Position from firmware; message assignment inferred. | 8\|8 | little-endian | unsigned | 0.01 | 0 | scale | 0 to 2.55 |  | plausible |
| `DIF_usmState` | page 38 | Position from firmware; message assignment inferred. | 12\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `USM_STATE_START`<br>1 = `USM_STATE_STANDBY`<br>2 = `USM_STATE_RETRY`<br>3 = `USM_STATE_ABORT`<br>4 = `USM_STATE_ENABLE`<br>5 = `USM_STATE_FAULT`<br>6 = `USM_STATE_UNAVAILABLE`<br>7 = `USM_STATE_WAIT_FOR_RETRY` | plausible |
| `DIF_peakIQref` | page 38 | Position from firmware; message assignment inferred. | 16\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `DIF_motorIAavg` | page 38 | Position from firmware; message assignment inferred. | 32\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 |  | plausible |
| `DIF_motorIBavg` | page 38 | Position from firmware; message assignment inferred. | 48\|16 | little-endian | signed | 0.1 | 0 | A | -3276.8 to 3276.7 |  | plausible |
| `DIF_tqSatThermal` | page 39 | Position from firmware; message assignment inferred. | 8\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 |  | plausible |
| `DIF_tqSatMotorVoltage` | page 39 | Position from firmware; message assignment inferred. | 32\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 |  | plausible |
| `DIF_tqSatMotorCurrent` | page 39 | Position from firmware; message assignment inferred. | 40\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 |  | plausible |
| `DIF_tcMaxRequest` | page 40 | Position from firmware; message assignment inferred. | 16\|8 | little-endian | unsigned | 5 | 0 | Nm | 0 to 1275 |  | plausible |
| `DIF_tcMinRequest` | page 40 | Position from firmware; message assignment inferred. | 24\|8 | little-endian | unsigned | 5 | 0 | Nm | 0 to 1275 |  | plausible |
| `DIF_tqScaleMaxMotorSpeed` | page 40 | Position from firmware; message assignment inferred. | 48\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 |  | plausible |
| `DIF_wasteCurrentLimit` | page 41 | Position from firmware; message assignment inferred. | 32\|16 | little-endian | unsigned | 0.1 | 0 | A | 0 to 6553.5 |  | plausible |
| `DIF_llsScale` | page 42 | Position from firmware; message assignment inferred. | 24\|8 | little-endian | unsigned | 0.004 | 0 | scale | 0 to 1.02 |  | plausible |
| `DIF_llrScale` | page 42 | Position from firmware; message assignment inferred. | 32\|8 | little-endian | unsigned | 0.015 | 0 | scale | 0 to 3.825 |  | plausible |
| `DIF_oilPumpMotorSpeed` | page 46 | Position from firmware; message assignment inferred. | 8\|8 | little-endian | unsigned | 40 | 0 | RPM | 0 to 10200 |  | plausible |
| `DIF_rotorFlux` | page 47 | Position from firmware; message assignment inferred. | 16\|16 | little-endian | unsigned | 0.0001 | 0 | Wb | 0 to 6.5535 |  | plausible |
| `DIF_dcCableHeat` | page 47 | Position from firmware; message assignment inferred. | 32\|16 | little-endian | unsigned | 0.001 | 0 | kA2s | 0 to 65.535 |  | plausible |
| `DIF_magnetTempEst` | page 47 | Position from firmware; message assignment inferred. | 48\|8 | little-endian | unsigned | 1 | -40 | DegC | -40 to 215 |  | plausible |
| `DIF_resolverReady` | page 48 | Position from firmware; message assignment inferred. | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `DIF_resolverNoCarrier` | page 48 | Position from firmware; message assignment inferred. | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `DIF_resolverNoPhaseLock` | page 48 | Position from firmware; message assignment inferred. | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `DIF_resolverClaMIA` | page 48 | Position from firmware; message assignment inferred. | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `DIF_soptMaxCurrentMagSqrd` | page 49 | Position from firmware; message assignment inferred. | 40\|16 | little-endian | unsigned | 100 | 0 | A2 | 0 to 6553500 |  | plausible |
| `DIF_statorVDFiltered` | page 63 | Position from firmware; message assignment inferred. | 16\|16 | little-endian | signed | 4.0e-05 | 0 | mindex | -1.31072 to 1.31068 |  | plausible |
| `DIF_statorVQFiltered` | page 63 | Position from firmware; message assignment inferred. | 32\|16 | little-endian | signed | 4.0e-05 | 0 | mindex | -1.31072 to 1.31068 |  | plausible |
| `DIF_pwmState` | page 63 | Position from firmware; message assignment inferred. | 48\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PWMSTATE_SVPWM`<br>1 = `PWMSTATE_DPWM2`<br>2 = `PWMSTATE_OPWM1`<br>3 = `PWMSTATE_OPWM2` | plausible |
| `DIF_dcCapTemp` | page 64 | Position from firmware; message assignment inferred. | 8\|8 | little-endian | unsigned | 1 | -40 | DegC | -40 to 215 |  | plausible |
| `DIF_busbarTemp` | page 64 | Position from firmware; message assignment inferred. | 16\|8 | little-endian | unsigned | 1 | -40 | DegC | -40 to 215 |  | plausible |
| `DIF_pcsTemp` | page 64 | Position from firmware; message assignment inferred. | 24\|8 | little-endian | unsigned | 1 | -40 | DegC | -40 to 215 |  | plausible |
| `DIF_statorTemp1` | page 64 | Position from firmware; message assignment inferred. | 32\|8 | little-endian | unsigned | 1 | -40 | DegC | -40 to 215 |  | plausible |
| `DIF_statorTemp2` | page 64 | Position from firmware; message assignment inferred. | 40\|8 | little-endian | unsigned | 1 | -40 | DegC | -40 to 215 |  | plausible |
| `DIF_cpu10HzMin` | page 66 | Position from firmware; message assignment inferred. | 8\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 |  | plausible |
| `DIF_cpu10HzAvg` | page 66 | Position from firmware; message assignment inferred. | 16\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 |  | plausible |
| `DIF_cpu100HzMin` | page 66 | Position from firmware; message assignment inferred. | 24\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 |  | plausible |
| `DIF_cpu100HzAvg` | page 66 | Position from firmware; message assignment inferred. | 32\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 |  | plausible |
| `DIF_cpu10msMin` | page 66 | Position from firmware; message assignment inferred. | 40\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 |  | plausible |
| `DIF_cpu1kHzMin` | page 67 | Position from firmware; message assignment inferred. | 8\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 |  | plausible |
| `DIF_cpu1kHzAvg` | page 67 | Position from firmware; message assignment inferred. | 16\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 |  | plausible |
| `DIF_cpu20kHzMin` | page 67 | Position from firmware; message assignment inferred. | 24\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 |  | plausible |
| `DIF_cpu20kHzAvg` | page 67 | Position from firmware; message assignment inferred. | 32\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 |  | plausible |
| `DIF_hwFaultCount` | page 69 | Position from firmware; message assignment inferred. | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | plausible |
| `DIF_driveUnitOdometer` | page 69 | Position from firmware; message assignment inferred. | 32\|32 | little-endian | unsigned | 10 | 0 | rev | 0 to 42949672950 |  | plausible |
| `DIF_phaseOutBusbarTemp` | page 70 | Front drive inverter: phase out busbar temp; raw 0 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | validated |
| `DIF_phaseOutBusbarWeldTemp` | page 70 | Front drive inverter: phase out busbar weld temp; raw 0 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | validated |
| `DIF_phaseOutLugTemp` | page 70 | Front drive inverter: phase out lug temp; raw 0 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | validated |
| `DIF_dcLinkCapTemp` | page 70 | Front drive inverter: dc link cap temp; raw 0 = signal not available (SNA) | 32\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | validated |
| `DIF_hvDcCableTemp` | page 70 | Front drive inverter: hv dc cable temp; raw 0 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | validated |
| `DIF_negDcBusbarTemp` | page 70 | Front drive inverter: neg dc busbar temp; raw 0 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | validated |
| `DIF_posDcBusbarTemp` | page 70 | Front drive inverter: pos dc busbar temp; raw 0 = signal not available (SNA) | 56\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | validated |
| `DIF_statorEndWindingTemp` | page 72 | Front drive inverter: stator end winding temp; raw 0 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | validated |
| `DIF_rotorMaxMagnetTemp` | page 72 | Reports the maximum temperature of the rotor magnet; raw 0 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | validated |
| `DIF_lightSenseV` | page 72 | Front drive inverter: light sense v | 24\|6 | little-endian | unsigned | 0.1 | 0 | V | 0 to 3.3 |  | validated |
| `DIF_pyroSenseV` | page 72 | Front drive inverter: pyro sense v | 30\|8 | little-endian | unsigned | 0.02 | 0 | V | 0 to 3.3 |  | validated |
| `DIF_statorSlotWindingTemp` | page 72 | Front drive inverter: stator slot winding temp; raw 0 = signal not available (SNA) | 46\|8 | little-endian | unsigned | 1 | -40 | DegC | -39 to 215 | 0 = `SNA` | validated |
| `DIF_intervalMaxHvBusV` | page 72 | Front drive inverter: interval max hv bus v | 54\|10 | little-endian | unsigned | 1 | 0 | V | 0 to 1023 |  | validated |
| `DIF_cpu1HzMin` | page 128 | Position from firmware; message assignment inferred. | 8\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 |  | plausible |
| `DIF_cpu1HzAvg` | page 128 | Position from firmware; message assignment inferred. | 16\|8 | little-endian | unsigned | 0.4 | 0 | % | 0 to 102 |  | plausible |
| `DIF_cpuIDWord0` | page 131 | Position from firmware; message assignment inferred. | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | plausible |
| `DIF_cpuIDWord1` | page 132 | Position from firmware; message assignment inferred. | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | plausible |
| `DIF_cpuIDWord2` | page 132 | Position from firmware; message assignment inferred. | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | plausible |
| `DIF_cpuIDWord3` | page 132 | Position from firmware; message assignment inferred. | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | plausible |

## Multiplexing

`DIF_debugSelector` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 32 (3 signals), page 33 (3 signals), page 34 (4 signals), page 35 (3 signals), page 36 (4 signals), page 37 (1 signals), page 38 (4 signals), page 39 (3 signals), page 40 (3 signals), page 41 (1 signals), page 42 (2 signals), page 46 (1 signals), page 47 (3 signals), page 48 (4 signals), page 49 (1 signals), page 63 (3 signals), page 64 (5 signals), page 66 (5 signals), page 67 (4 signals), page 69 (2 signals), page 70 (7 signals), page 72 (6 signals), page 128 (2 signals), page 131 (1 signals), page 132 (3 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 PARTY DBC file](../../../../../dbc/ModelY/2026.26.6.5/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/PARTY.json)

## See also

- [All Front drive inverter messages (DIF)](../../dif.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
