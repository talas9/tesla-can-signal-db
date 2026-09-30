---
layout: default
title: "VCSEC_TPMSDisplay (0x25A) — Vehicle security controller, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Vehicle security controller message: TPMS display. Tesla Model 3 CAN bus message VCSEC_TPMSDisplay (0x25A) of Vehicle security controller, firmware 2026.26.6.5, 13 signals (VCSEC_TPMSDisplayPressureFL, VCSEC_TPMSDisplayPressureFR, VCSEC_TPMSDisplayPressureRL, VCSEC_TPMSDisplayPressureRR and 9 more). Bit layout, scaling, units and value tables."
---

# VCSEC_TPMSDisplay (0x25A) — Vehicle security controller, Tesla Model 3 2026.26.6.5 VEH CAN

Vehicle security controller message: TPMS display; frame length from the layout, not yet observed on a vehicle bus. This page documents the 13 signals of VCSEC_TPMSDisplay as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEC_TPMSDisplay` |
| CAN id | 0x25A (602) |
| ECU | [Vehicle security controller](../../vcsec.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCSEC |
| Frame length | 6 bytes |
| Cycle time | 1000 ms |
| Signals | 13 |

## Signals of VCSEC_TPMSDisplay

Tesla Model 3 CAN bus signals in `VCSEC_TPMSDisplay`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEC_TPMSDisplayPressureFL` | Indicates Absolute pressure measured by wheel unit; raw 255 = signal not available (SNA) | 0\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.35 | 254 = `OVER_RANGE`<br>255 = `SNA` | validated |
| `VCSEC_TPMSDisplayPressureFR` | Indicates Absolute pressure measured by wheel unit; raw 255 = signal not available (SNA) | 8\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.35 | 254 = `OVER_RANGE`<br>255 = `SNA` | validated |
| `VCSEC_TPMSDisplayPressureRL` | Indicates Absolute pressure measured by wheel unit; raw 255 = signal not available (SNA) | 16\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.35 | 254 = `OVER_RANGE`<br>255 = `SNA` | validated |
| `VCSEC_TPMSDisplayPressureRR` | Indicates Absolute pressure measured by wheel unit; raw 255 = signal not available (SNA) | 24\|8 | little-endian | unsigned | 0.025 | 0 | bar | 0 to 6.35 | 254 = `OVER_RANGE`<br>255 = `SNA` | validated |
| `VCSEC_TPMSTellTale` | TPMS UI telltale status to indicate | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TPMS_TELLTALE_OFF`<br>1 = `TPMS_TELLTALE_SOLID`<br>2 = `TPMS_TELLTALE_FLASHING` | validated |
| `VCSEC_TPMSDisplaySoftWarningIndicationFL` | UI should indicate soft warning | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TPMS_PRESSUREWARNING_NOT_INDICATED`<br>1 = `TPMS_PRESSUREWARNING_INDICATED` | validated |
| `VCSEC_TPMSDisplaySoftWarningIndicationFR` | UI should indicate soft warning | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TPMS_PRESSUREWARNING_NOT_INDICATED`<br>1 = `TPMS_PRESSUREWARNING_INDICATED` | validated |
| `VCSEC_TPMSDisplaySoftWarningIndicationRL` | UI should indicate soft warning | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TPMS_PRESSUREWARNING_NOT_INDICATED`<br>1 = `TPMS_PRESSUREWARNING_INDICATED` | validated |
| `VCSEC_TPMSDisplaySoftWarningIndicationRR` | UI should indicate soft warning | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TPMS_PRESSUREWARNING_NOT_INDICATED`<br>1 = `TPMS_PRESSUREWARNING_INDICATED` | validated |
| `VCSEC_TPMSDisplayHardWarningIndicationFL` | UI should indicate soft warning | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TPMS_PRESSUREWARNING_NOT_INDICATED`<br>1 = `TPMS_PRESSUREWARNING_INDICATED` | validated |
| `VCSEC_TPMSDisplayHardWarningIndicationFR` | UI should indicate soft warning | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TPMS_PRESSUREWARNING_NOT_INDICATED`<br>1 = `TPMS_PRESSUREWARNING_INDICATED` | validated |
| `VCSEC_TPMSDisplayHardWarningIndicationRL` | UI should indicate soft warning | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TPMS_PRESSUREWARNING_NOT_INDICATED`<br>1 = `TPMS_PRESSUREWARNING_INDICATED` | validated |
| `VCSEC_TPMSDisplayHardWarningIndicationRR` | UI should indicate soft warning | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TPMS_PRESSUREWARNING_NOT_INDICATED`<br>1 = `TPMS_PRESSUREWARNING_INDICATED` | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Vehicle security controller messages (VCSEC)](../../vcsec.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
