---
layout: default
title: "BMS_debugInfo_10Hz (0x7ED) — High-voltage battery management system, Tesla Model 3 2025.20.8 ETH"
description: "High-voltage battery management system message: debug info 10 hz. Ethernet-side message BMS_debugInfo_10Hz of High-voltage battery management system for Tesla Model 3 firmware 2025.20.8, 3 signals (BMS_10HzDebug_Id, BMS_activeCoolCellTargetT, BMS_passiveCoolCellTargetT). Bit layout, scaling, units and value tables."
---

# BMS_debugInfo_10Hz (0x7ED) — High-voltage battery management system, Tesla Model 3 2025.20.8 ETH

High-voltage battery management system message: debug info 10 hz. This page documents the 3 signals of BMS_debugInfo_10Hz as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_debugInfo_10Hz` |
| Ethernet-side id | 0x7ED (2029) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | BMS |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 3 |

## Signals of BMS_debugInfo_10Hz

Tesla Model 3 CAN bus signals in `BMS_debugInfo_10Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_10HzDebug_Id` | selector | High-voltage battery management system: 10 hz debug id | 0\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `STATE`<br>1 = `AHR_COUNTER`<br>2 = `ISOLATION`<br>3 = `SOC_RESTING`<br>12 = `THM_MODEL_DATA_9`<br>13 = `THM_MODEL_DATA_10`<br>14 = `THM_MODEL_DATA_11`<br>15 = `PACK_VOLTAGES`<br>16 = `HYST`<br>17 = `CAC_1`<br>18 = `CAC_2`<br>19 = `CAC_3`<br>20 = `WAKE_TIMERS`<br>21 = `ADC_VREF`<br>22 = `ADC_CP`<br>23 = `ADC_DCLINK`<br>24 = `ADC_MISC`<br>25 = `ADC_FLOOD`<br>26 = `POWER_PREDICTION_1`<br>27 = `POWER_PREDICTION_2`<br>28 = `POWER_PREDICTION_3`<br>29 = `SLEEP_WAKE`<br>30 = `STANDBY_SUPPLY`<br>31 = `DRIVE_LIMITS`<br>32 = `SOC_AND_OCV`<br>33 = `THM_TARGETS`<br>34 = `AGED_SOC_OCV` | plausible |
| `BMS_activeCoolCellTargetT` | page 33 | High-voltage battery management system: active cool cell target t | 6\|9 | little-endian | unsigned | 0.25 | -25 | DegC | -25 to 100 |  | plausible |
| `BMS_passiveCoolCellTargetT` | page 33 | High-voltage battery management system: passive cool cell target t | 15\|9 | little-endian | unsigned | 0.25 | -25 | DegC | -25 to 100 |  | plausible |

## Multiplexing

`BMS_10HzDebug_Id` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 33 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
