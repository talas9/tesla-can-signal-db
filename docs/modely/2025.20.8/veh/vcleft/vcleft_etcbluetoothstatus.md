---
layout: default
title: "VCLEFT_etcBluetoothStatus (0x4A2) — Left body controller, Tesla Model Y 2025.20.8 VEH CAN"
description: "Left body controller message: etc bluetooth status. Tesla Model Y CAN bus message VCLEFT_etcBluetoothStatus (0x4A2) of Left body controller, firmware 2025.20.8, 1 signals (VCLEFT_etcBluetoothStatus). Bit layout, scaling, units and value tables."
---

# VCLEFT_etcBluetoothStatus (0x4A2) — Left body controller, Tesla Model Y 2025.20.8 VEH CAN

Left body controller message: etc bluetooth status; frame length from the layout, not yet observed on a vehicle bus. This page documents the 1 signals of VCLEFT_etcBluetoothStatus as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_etcBluetoothStatus` |
| CAN id | 0x4A2 (1186) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCLEFT |
| Frame length | 1 bytes |
| Cycle time | 1000 ms |
| Signals | 1 |

## Signals of VCLEFT_etcBluetoothStatus

Tesla Model Y CAN bus signals in `VCLEFT_etcBluetoothStatus`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_etcBluetoothStatus` | Left body controller: etc bluetooth status | 0\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `ETC_BLUETOOTH_STATE_INACTIVE`<br>1 = `ETC_BLUETOOTH_STATE_OFF`<br>2 = `ETC_BLUETOOTH_STATE_ON`<br>3 = `ETC_BLUETOOTH_STATE_RESERVED` | plausible |

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
