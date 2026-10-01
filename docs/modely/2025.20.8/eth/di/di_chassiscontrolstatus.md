---
layout: default
title: "DI_chassisControlStatus (0x2B6) — Drive inverter, Tesla Model Y 2025.20.8 ETH"
description: "Drive inverter message: chassis control status. Ethernet-side message DI_chassisControlStatus of Drive inverter for Tesla Model Y firmware 2025.20.8, 13 signals (DI_vdcTelltaleFlash, DI_vdcTelltaleOn, DI_tcTelltaleFlash, DI_tcTelltaleOn and 9 more). Bit layout, scaling, units and value tables."
---

# DI_chassisControlStatus (0x2B6) — Drive inverter, Tesla Model Y 2025.20.8 ETH

Drive inverter message: chassis control status. This page documents the 13 signals of DI_chassisControlStatus as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DI_chassisControlStatus` |
| Ethernet-side id | 0x2B6 (694) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DI |
| Frame length | 2 bytes |
| Cycle time | 100 ms |
| Signals | 13 |

## Signals of DI_chassisControlStatus

Tesla Model Y CAN bus signals in `DI_chassisControlStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_vdcTelltaleFlash` | Request to flash telltale in UI when VDC is active | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TELLTALE_OFF`<br>1 = `TELLTALE_ON` | plausible |
| `DI_vdcTelltaleOn` | Request to turn telltale ON in UI when VDC is faulted | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TELLTALE_OFF`<br>1 = `TELLTALE_ON` | plausible |
| `DI_tcTelltaleFlash` | Request to flash telltale in UI when TC is active | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TELLTALE_OFF`<br>1 = `TELLTALE_ON` | plausible |
| `DI_tcTelltaleOn` | Request to turn telltale ON in UI when TC is faulted | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TELLTALE_OFF`<br>1 = `TELLTALE_ON` | plausible |
| `DI_tractionControlModeUI` | Drive inverter: traction control mode UI | 4\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `TC_NORMAL`<br>1 = `TC_SLIP_START`<br>2 = `TC_DEV_MODE_1`<br>3 = `TC_DEV_MODE_2`<br>4 = `TC_ROLLS_MODE`<br>5 = `TC_DYNO_MODE`<br>6 = `TC_OFFROAD_ASSIST`<br>7 = `TC_SLIPPERY_SURFACE` | plausible |
| `DI_ptcStateGlobalUI` | Drive inverter: ptc state global UI; raw 3 = signal not available (SNA) | 7\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `GLOBAL_PTC_STATE_FAULTED`<br>1 = `GLOBAL_PTC_STATE_BACKUP`<br>2 = `GLOBAL_PTC_STATE_ON`<br>3 = `GLOBAL_PTC_STATE_SNA` | plausible |
| `DI_btcStateUI` | Drive inverter: btc state UI | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `OFF`<br>1 = `ON` | plausible |
| `DI_vehicleHoldTelltaleOn` | Drive inverter: vehicle hold telltale on | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TELLTALE_OFF`<br>1 = `TELLTALE_ON` | plausible |
| `DI_opdFeedbackReset` | Drive inverter: opd feedback reset | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_opdFeedbackResetPositiveSpeeds` | Drive inverter: opd feedback reset positive speeds | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_slipperySurfaceOnUI` | Drive inverter: slippery surface on UI | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SLIPPERY_SURFACE_OFF`<br>1 = `SLIPPERY_SURFACE_ON` | plausible |
| `DI_yellowBrakeTelltaleOn` | Request to turn yellow BRAKE telltale ON in UI | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TELLTALE_OFF`<br>1 = `TELLTALE_ON` | plausible |
| `DI_greenABSTelltaleOn` | Drive inverter: green ABS telltale on | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TELLTALE_OFF`<br>1 = `TELLTALE_ON` | plausible |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
