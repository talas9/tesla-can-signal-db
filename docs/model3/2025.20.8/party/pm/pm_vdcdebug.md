---
layout: default
title: "PM_vdcDebug (0x7F6) — PM ECU, Tesla Model 3 2025.20.8 PARTY CAN"
description: "PM ECU message: vdc debug. Tesla Model 3 CAN bus message PM_vdcDebug (0x7F6) of PM ECU, firmware 2025.20.8, 20 signals (PM_vdcDebugSelector, PM_VDCA_TCSlipTargetMod_RA_Fwd, PM_VDCA_TCSlipTargetMod_RA_Rwd, PM_VSE_forceY_RA and 16 more). Bit layout, scaling, units and value tables."
---

# PM_vdcDebug (0x7F6) — PM ECU, Tesla Model 3 2025.20.8 PARTY CAN

PM ECU message: vdc debug; frame length from the layout, not yet observed on a vehicle bus. This page documents the 20 signals of PM_vdcDebug as defined for Tesla Model 3 firmware 2025.20.8 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PM_vdcDebug` |
| CAN id | 0x7F6 (2038) |
| ECU | [PM ECU](../../pm.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | PM |
| Frame length | 8 bytes |
| Cycle time | 20 ms |
| Signals | 20 |

## Signals of PM_vdcDebug

Tesla Model 3 CAN bus signals in `PM_vdcDebug`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `PM_vdcDebugSelector` | selector | PM ECU: vdc debug selector | 0\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `Mux0`<br>1 = `Mux1`<br>2 = `Mux2`<br>3 = `Mux3`<br>4 = `Mux4`<br>5 = `Mux5`<br>6 = `Mux6`<br>7 = `Mux7`<br>8 = `Mux8`<br>9 = `Mux9`<br>10 = `Mux10`<br>11 = `Mux11`<br>12 = `Mux12`<br>13 = `Mux13`<br>14 = `Mux14`<br>15 = `Mux15`<br>16 = `Mux16`<br>17 = `Mux17`<br>18 = `Mux18`<br>19 = `Mux19`<br>20 = `Mux20`<br>21 = `Mux21`<br>22 = `Mux22`<br>23 = `Mux23`<br>24 = `Mux24`<br>25 = `Mux25`<br>26 = `Mux26`<br>27 = `Mux27`<br>28 = `Mux28`<br>29 = `Mux29`<br>30 = `Mux30`<br>31 = `Mux31`<br>32 = `Mux32` | plausible |
| `PM_VDCA_TCSlipTargetMod_RA_Fwd` | page 5 | PM ECU: VDCA TC slip target mod RA fwd | 8\|6 | little-endian | signed | 0.1 | 0 | m/s | -3 to 3 |  | validated |
| `PM_VDCA_TCSlipTargetMod_RA_Rwd` | page 5 | PM ECU: VDCA TC slip target mod RA rwd | 16\|6 | little-endian | signed | 0.1 | 0 | m/s | -3 to 3 |  | validated |
| `PM_VSE_forceY_RA` | page 5 | PM ECU: VSE force y RA | 22\|9 | little-endian | signed | 40 | 240 | N | -10000 to 10440 |  | validated |
| `PM_VDCT_observerSlipAngle_RA` | page 5 | PM ECU: VDCT observer slip angle RA | 31\|9 | little-endian | signed | 0.005 | 0.03 | rad | -1.25 to 1.305 |  | validated |
| `PM_VSE_muVehicleFxLow` | page 5 | PM ECU: VSE mu vehicle fx low | 40\|5 | little-endian | unsigned | 0.05 | 0 | mu | 0 to 1.55 |  | validated |
| `PM_VE_fxmFres` | page 13 | PM ECU: VE fxm fres | 8\|8 | little-endian | signed | 200 | 0 | N | -20000 to 20000 |  | validated |
| `PM_VE_fxAccelMass` | page 13 | PM ECU: VE fx accel mass | 16\|8 | little-endian | signed | 0.16 | 0 | m/s^2 | -20 to 20 |  | validated |
| `PM_VE_vxDotGrade` | page 13 | PM ECU: VE vx dot grade | 24\|8 | little-endian | signed | 0.1 | 0.8 | m/s^2 | -12 to 13.5 |  | validated |
| `PM_VE_betaEst` | page 13 | PM ECU: VE beta est | 32\|8 | little-endian | signed | 0.01 | 0 | rad | -1 to 1 |  | validated |
| `PM_VSE_muVehicleFxHigh` | page 13 | PM ECU: VSE mu vehicle fx high | 40\|5 | little-endian | unsigned | 0.05 | 0 | mu | 0 to 1.55 |  | validated |
| `PM_VSE_muVehicleDecLeakRate` | page 29 | PM ECU: VSE mu vehicle dec leak rate | 6\|5 | little-endian | unsigned | 0.05 | 0 | mu | 0 to 1.55 |  | validated |
| `PM_VSE_muVehicleLearnDown` | page 29 | PM ECU: VSE mu vehicle learn down | 11\|5 | little-endian | unsigned | 0.05 | 0 | mu | 0 to 1.55 |  | validated |
| `PM_VSE_muVehicleDecFilter` | page 29 | PM ECU: VSE mu vehicle dec filter | 16\|5 | little-endian | unsigned | 0.05 | 0 | mu | 0 to 1.55 |  | validated |
| `PM_VSE_muVehicleLatDecLeakRate` | page 29 | PM ECU: VSE mu vehicle lat dec leak rate | 21\|5 | little-endian | unsigned | 0.05 | 0 | mu | 0 to 1.55 |  | validated |
| `PM_VSE_splitMuProbability` | page 29 | PM ECU: VSE split mu probability | 26\|5 | little-endian | unsigned | 0.05 | 0 | probability | 0 to 1.55 |  | validated |
| `PM_VSE_splitMuTotalMz` | page 29 | PM ECU: VSE split mu total mz | 31\|9 | little-endian | signed | 60 | 360 | Nm | -15000 to 15660 |  | validated |
| `PM_VSE_attitudeBankAngle` | page 29 | PM ECU: VSE attitude bank angle | 40\|9 | little-endian | signed | 0.005 | 0.03 | rad | -1.25 to 1.305 |  | validated |
| `PM_VSE_attitudeDBetaInControl` | page 29 | PM ECU: VSE attitude d beta in control | 49\|8 | little-endian | signed | 0.01 | 0.03 | rad | -1.25 to 1.3 |  | validated |
| `PM_VSE_roadWheelAngleAverage` | page 29 | PM ECU: VSE road wheel angle average | 57\|7 | little-endian | signed | 0.015 | 0.255 | rad | -0.7 to 1.2 |  | validated |

## Multiplexing

`PM_vdcDebugSelector` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 5 (5 signals), page 13 (5 signals), page 29 (9 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 PARTY DBC file](../../../../../dbc/Model3/2025.20.8/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/PARTY.json)

## See also

- [All PM ECU messages (PM)](../../pm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
