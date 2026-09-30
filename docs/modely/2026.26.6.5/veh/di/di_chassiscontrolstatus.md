---
layout: default
title: "DI_chassisControlStatus (0x2B6) — Drive inverter, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "Drive inverter message: chassis control status. Tesla Model Y CAN bus message DI_chassisControlStatus (0x2B6) of Drive inverter, firmware 2026.26.6.5, 14 signals (DI_vdcTelltaleFlash, DI_vdcTelltaleOn, DI_tcTelltaleFlash, DI_tcTelltaleOn and 10 more). Bit layout, scaling, units and value tables."
---

# DI_chassisControlStatus (0x2B6) — Drive inverter, Tesla Model Y 2026.26.6.5 VEH CAN

Drive inverter message: chassis control status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 14 signals of DI_chassisControlStatus as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `DI_chassisControlStatus` |
| CAN id | 0x2B6 (694) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | DI |
| Frame length | 3 bytes |
| Cycle time | 100 ms |
| Signals | 14 |

## Signals of DI_chassisControlStatus

Tesla Model Y CAN bus signals in `DI_chassisControlStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_vdcTelltaleFlash` | Request to flash telltale in UI when VDC is active | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TELLTALE_OFF`<br>1 = `TELLTALE_ON` | validated |
| `DI_vdcTelltaleOn` | Request to turn telltale ON in UI when VDC is faulted | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TELLTALE_OFF`<br>1 = `TELLTALE_ON` | validated |
| `DI_tcTelltaleFlash` | Request to flash telltale in UI when TC is active | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TELLTALE_OFF`<br>1 = `TELLTALE_ON` | validated |
| `DI_tcTelltaleOn` | Request to turn telltale ON in UI when TC is faulted | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TELLTALE_OFF`<br>1 = `TELLTALE_ON` | validated |
| `DI_tractionControlModeUI` | Drive inverter: traction control mode UI | 4\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `TC_NORMAL`<br>1 = `TC_SLIP_START`<br>2 = `TC_DEV_MODE_1`<br>3 = `TC_DEV_MODE_2`<br>4 = `TC_ROLLS_MODE`<br>5 = `TC_DYNO_MODE`<br>6 = `TC_OFFROAD_ASSIST`<br>7 = `TC_SLIPPERY_SURFACE` | validated |
| `DI_ptcStateGlobalUI` | Drive inverter: ptc state global UI; raw 3 = signal not available (SNA) | 7\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `GLOBAL_PTC_STATE_FAULTED`<br>1 = `GLOBAL_PTC_STATE_BACKUP`<br>2 = `GLOBAL_PTC_STATE_ON`<br>3 = `GLOBAL_PTC_STATE_SNA` | validated |
| `DI_btcStateUI` | Drive inverter: btc state UI | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OFF`<br>1 = `ON` | validated |
| `DI_vehicleHoldTelltaleOn` | Drive inverter: vehicle hold telltale on | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TELLTALE_OFF`<br>1 = `TELLTALE_ON` | validated |
| `DI_opdFeedbackReset` | Drive inverter: opd feedback reset | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_opdFeedbackResetPositiveSpeeds` | Drive inverter: opd feedback reset positive speeds | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `DI_slipperySurfaceOnUI` | Drive inverter: slippery surface on UI | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SLIPPERY_SURFACE_OFF`<br>1 = `SLIPPERY_SURFACE_ON` | validated |
| `DI_yellowBrakeTelltaleOn` | Request to turn yellow BRAKE telltale ON in UI | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TELLTALE_OFF`<br>1 = `TELLTALE_ON` | validated |
| `DI_greenABSTelltaleOn` | Drive inverter: green ABS telltale on | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TELLTALE_OFF`<br>1 = `TELLTALE_ON` | validated |
| `DI_stabilityModeState` | Current stability mode setting being honored by the DI | 21\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNAVAILABLE`<br>1 = `NORMAL`<br>2 = `REDUCED` | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
