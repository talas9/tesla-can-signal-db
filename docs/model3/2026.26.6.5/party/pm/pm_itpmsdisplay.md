---
layout: default
title: "PM_itpmsDisplay (0x7B5) — PM ECU, Tesla Model 3 2026.26.6.5 PARTY CAN"
description: "PM ECU message: itpms display. Tesla Model 3 CAN bus message PM_itpmsDisplay (0x7B5) of PM ECU, firmware 2026.26.6.5, 14 signals (PM_itpmsDisplaySelector, PM_indirectTPMSTellTale, PM_indirectTPMSDisplayState, PM_indirectTPMSDisplayProgress and 10 more). Bit layout, scaling, units and value tables."
---

# PM_itpmsDisplay (0x7B5) — PM ECU, Tesla Model 3 2026.26.6.5 PARTY CAN

PM ECU message: itpms display; frame length from the layout, not yet observed on a vehicle bus. This page documents the 14 signals of PM_itpmsDisplay as defined for Tesla Model 3 firmware 2026.26.6.5 on the bus1 bus.

## Message details

| Property | Value |
|---|---|
| Message name | `PM_itpmsDisplay` |
| CAN id | 0x7B5 (1973) |
| ECU | [PM ECU](../../pm.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | bus1 (inferred PARTY) |
| Transmitter | PM |
| Frame length | 3 bytes |
| Cycle time | 1000 ms |
| Signals | 14 |

## Signals of PM_itpmsDisplay

Tesla Model 3 CAN bus signals in `PM_itpmsDisplay`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `PM_itpmsDisplaySelector` | selector | PM ECU: itpms display selector | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `Mux0`<br>1 = `Mux1`<br>2 = `Mux2`<br>3 = `Mux3` | plausible |
| `PM_indirectTPMSTellTale` | page 0 | Indirect TPMS UI telltale status to indicate system availability | 2\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TPMS_TELLTALE_OFF`<br>1 = `TPMS_TELLTALE_SOLID`<br>2 = `TPMS_TELLTALE_FLASHING` | validated |
| `PM_indirectTPMSDisplayState` | page 0 | Indirect TPMS UI calibration state | 4\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNAVAILABLE`<br>1 = `CALIBRATING`<br>2 = `CALIBRATED`<br>3 = `FAULTED` | validated |
| `PM_indirectTPMSDisplayProgress` | page 0 | PM ECU: indirect TPMS display progress | 8\|5 | little-endian | unsigned | 0.05 | 0 | - | 0 to 1 |  | validated |
| `PM_indirectTPMSDisplayWarningIndicatorFL` | page 0 | Pressure loss warning indicator per wheel determined by indirect TPMS | 13\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `SOFT`<br>2 = `HARD` | validated |
| `PM_indirectTPMSDisplayWarningIndicatorFR` | page 0 | Pressure loss warning indicator per wheel determined by indirect TPMS | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `SOFT`<br>2 = `HARD` | validated |
| `PM_indirectTPMSDisplayWarningIndicatorRL` | page 0 | Pressure loss warning indicator per wheel determined by indirect TPMS | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `SOFT`<br>2 = `HARD` | validated |
| `PM_indirectTPMSDisplayWarningIndicatorRR` | page 0 | Pressure loss warning indicator per wheel determined by indirect TPMS | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `SOFT`<br>2 = `HARD` | validated |
| `PM_indirectTPMSRecommendedColdPressureFront` | page 1 | Reports the recommended cold pressure for the front or rear tires as provided by the Indirect Tire Pressure Monitoring System (ITPMS); raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.35 | 254 = `OVER_RANGE`<br>255 = `SNA` | validated |
| `PM_indirectTPMSRecommendedColdPressureRear` | page 1 | Reports the recommended cold pressure for the front or rear tires as provided by the Indirect Tire Pressure Monitoring System (ITPMS); raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.35 | 254 = `OVER_RANGE`<br>255 = `SNA` | validated |
| `PM_fusedPressureEstimateFrL` | page 2 | Reports the estimated tire pressure at each wheel based on Indirect Tire Pressure Monitoring System (ITPMS) relative wheel speed and Global Navigation Satellite System (GNSS) absolute radius data. | 2\|9 | little-endian | unsigned | 0.008 | 0 | bar | 0 to 4 |  | validated |
| `PM_fusedPressureEstimateFrR` | page 2 | Reports the estimated tire pressure at each wheel based on Indirect Tire Pressure Monitoring System (ITPMS) relative wheel speed and Global Navigation Satellite System (GNSS) absolute radius data. | 11\|9 | little-endian | unsigned | 0.008 | 0 | bar | 0 to 4 |  | validated |
| `PM_fusedPressureEstimateReL` | page 3 | Reports the estimated tire pressure at each wheel based on Indirect Tire Pressure Monitoring System (ITPMS) relative wheel speed and Global Navigation Satellite System (GNSS) absolute radius data. | 2\|9 | little-endian | unsigned | 0.008 | 0 | bar | 0 to 4 |  | validated |
| `PM_fusedPressureEstimateReR` | page 3 | Reports the estimated tire pressure at each wheel based on Indirect Tire Pressure Monitoring System (ITPMS) relative wheel speed and Global Navigation Satellite System (GNSS) absolute radius data. | 11\|9 | little-endian | unsigned | 0.008 | 0 | bar | 0 to 4 |  | validated |

## Multiplexing

`PM_itpmsDisplaySelector` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (7 signals), page 1 (2 signals), page 2 (2 signals), page 3 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 PARTY DBC file](../../../../../dbc/Model3/2026.26.6.5/PARTY.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/PARTY.json)

## See also

- [All PM ECU messages (PM)](../../pm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
