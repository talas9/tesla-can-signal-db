---
layout: default
title: "BMS_contactorRequest (0x232) — High-voltage battery management system, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "High-voltage battery management system message: contactor request. Tesla Model Y CAN bus message BMS_contactorRequest (0x232) of High-voltage battery management system, firmware 2026.26.6.5, 8 signals (BMS_fcContactorRequest, BMS_packContactorRequest, BMS_gpoHasCompleted, BMS_ensShouldBeActiveForDrive and 4 more). Bit layout, scaling, units and value tables."
---

# BMS_contactorRequest (0x232) — High-voltage battery management system, Tesla Model Y 2026.26.6.5 VEH CAN

High-voltage battery management system message: contactor request; frame length from the layout, not yet observed on a vehicle bus. This page documents the 8 signals of BMS_contactorRequest as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_contactorRequest` |
| CAN id | 0x232 (562) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 8 |

## Signals of BMS_contactorRequest

Tesla Model Y CAN bus signals in `BMS_contactorRequest`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_fcContactorRequest` | Request indicating which state the BMS would like the fast charge contactors to enter. Position from firmware; message assignment inferred. | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SET_REQUEST_SNA`<br>1 = `SET_REQUEST_CLOSE`<br>2 = `SET_REQUEST_OPEN`<br>3 = `SET_REQUEST_OPEN_IMMEDIATELY`<br>4 = `SET_REQUEST_CLOSE_NEGATIVE_ONLY`<br>5 = `SET_REQUEST_CLOSE_POSITIVE_ONLY` | plausible |
| `BMS_packContactorRequest` | Request indicating which state the BMS would like the pack contactors to enter. Position from firmware; message assignment inferred. | 3\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `SET_REQUEST_SNA`<br>1 = `SET_REQUEST_CLOSE`<br>2 = `SET_REQUEST_OPEN`<br>3 = `SET_REQUEST_OPEN_IMMEDIATELY`<br>4 = `SET_REQUEST_CLOSE_NEGATIVE_ONLY`<br>5 = `SET_REQUEST_CLOSE_POSITIVE_ONLY` | plausible |
| `BMS_gpoHasCompleted` | Position from firmware; message assignment inferred. | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `BMS_ensShouldBeActiveForDrive` | Position from firmware; message assignment inferred. | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `BMS_pcsPwmDisable` | Position from firmware; message assignment inferred. | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `BMS_fcLinkOkToEnergizeRequest` | Position from firmware; message assignment inferred. | 9\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `FC_LINK_ENERGY_NONE`<br>1 = `FC_LINK_ENERGY_AC`<br>2 = `FC_LINK_ENERGY_DC` | plausible |
| `BMS_internalHvilSenseV` | High-voltage battery management system: internal hvil sense v | 16\|16 | little-endian | unsigned | 0.001 | 0 | V | 0 to 65.534 | 65535 = `SNA` | plausible |
| `BMS_hvilCoverVSense` | High-voltage battery management system: hvil cover v sense | 32\|16 | little-endian | unsigned | 0.001 | 0 | V | 0 to 65.534 | 65535 = `SNA` | plausible |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
