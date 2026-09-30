---
layout: default
title: "HVP_hvsControl (0x22A) — High-voltage processor (pack contactor and isolation controller), Tesla Model Y 2026.26.6.5 VEH CAN"
description: "High-voltage processor (pack contactor and isolation controller) message: hvs control. Tesla Model Y CAN bus message HVP_hvsControl (0x22A) of High-voltage processor (pack contactor and isolation controller), firmware 2026.26.6.5, 5 signals (HVP_dcLinkVoltageRequest, HVP_pcsControlRequest, HVP_pcsChargeHwEnabled, HVP_pcsDcdcHwEnabled and 1 more). Bit layout, scaling, units and value tables."
---

# HVP_hvsControl (0x22A) — High-voltage processor (pack contactor and isolation controller), Tesla Model Y 2026.26.6.5 VEH CAN

High-voltage processor (pack contactor and isolation controller) message: hvs control; frame length from the layout, not yet observed on a vehicle bus. This page documents the 5 signals of HVP_hvsControl as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `HVP_hvsControl` |
| CAN id | 0x22A (554) |
| ECU | [High-voltage processor (pack contactor and isolation controller)](../../hvp.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | HVP |
| Frame length | 4 bytes |
| Cycle time | 100 ms |
| Signals | 5 |

## Signals of HVP_hvsControl

Tesla Model Y CAN bus signals in `HVP_hvsControl`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `HVP_dcLinkVoltageRequest` | High-voltage processor (pack contactor and isolation controller): dc link voltage request | 0\|16 | little-endian | signed | 0.1 | 0 | V | -550 to 550 |  | validated |
| `HVP_pcsControlRequest` | The operating state that the HVP would like the PCS to be in | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SHUTDOWN`<br>1 = `SUPPORT`<br>2 = `PRECHARGE`<br>3 = `DISCHARGE` | validated |
| `HVP_pcsChargeHwEnabled` | The state of the PCS's charge enable line | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_pcsDcdcHwEnabled` | The state of the PCS's DCDC enable line | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `HVP_dcLinkVoltageFiltered` | High-voltage processor (pack contactor and isolation controller): dc link voltage filtered; raw 1498 = signal not available (SNA) | 20\|11 | little-endian | signed | 1 | 0 | V | -550 to 550 | -550 = `SNA` | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All High-voltage processor (pack contactor and isolation controller) messages (HVP)](../../hvp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
