---
layout: default
title: "OCS1P_alertLog (0x595) — Occupant classification system, Tesla Model 3 2025.20.8 ETH"
description: "Occupant classification system message: alert log. Ethernet-side message OCS1P_alertLog of Occupant classification system for Tesla Model 3 firmware 2025.20.8, 22 signals (OCS1P_alertID, OCS1P_alertState, OCS1P_a121_sandwichFreq, OCS1P_a122_sandwichFreq and 18 more). Bit layout, scaling, units and value tables."
---

# OCS1P_alertLog (0x595) — Occupant classification system, Tesla Model 3 2025.20.8 ETH

Occupant classification system message: alert log. This page documents the 22 signals of OCS1P_alertLog as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `OCS1P_alertLog` |
| Ethernet-side id | 0x595 (1429) |
| ECU | [Occupant classification system](../../ocs1p.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | OCS1P |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 22 |

## Signals of OCS1P_alertLog

Tesla Model 3 CAN bus signals in `OCS1P_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `OCS1P_alertID` | selector | Occupant classification system: alert ID | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>15 = `a015_NVMMAlert`<br>121 = `a121_sandwichOpen`<br>122 = `a122_sandwichLow`<br>123 = `a123_sandwichShort`<br>124 = `a124_cushionSelfOpen`<br>125 = `a125_cushionSelfLow`<br>126 = `a126_cushionSelfShort`<br>127 = `a127_seatbackSelfOpen`<br>128 = `a128_seatbackSelfLow`<br>129 = `a129_seatbackSelfShort`<br>130 = `a130_sandwichNoCalib`<br>131 = `a131_cushionSelfNoCalib`<br>132 = `a132_seatbackSelfNoCalib`<br>133 = `a133_sandwichBadCalib`<br>134 = `a134_uninitializedCalib`<br>135 = `a135_tempNoCalib`<br>136 = `a136_cushionSelfDutyLow`<br>137 = `a137_cushionSelfDutyHigh`<br>138 = `a138_seatbackSelfDutyLow`<br>139 = `a139_seatbackSelfDutyHigh`<br>140 = `a140_tempInvalidCalib`<br>141 = `a141_humidityInvalidCalib`<br>142 = `a142_tempHumidityInvalid`<br>143 = `a143_mismatchPassAirbag`<br>144 = `a144_mismatchCarRegion`<br>145 = `a145_rebaselineTriggered`<br>148 = `a148_classificationMismatch`<br>150 = `a150_rbEntryTriggered`<br>151 = `a151_rbEntryExited`<br>152 = `a152_rbExit1Triggered`<br>153 = `a153_rbExit1Exited`<br>154 = `a154_rbExit2Exited1`<br>155 = `a155_rbExit2Exited2` | plausible |
| `OCS1P_alertState` |  | Occupant classification system: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `OCS1P_a121_sandwichFreq` | page 121 | Occupant classification system: a121 sandwich freq | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `OCS1P_a122_sandwichFreq` | page 122 | Occupant classification system: a122 sandwich freq | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `OCS1P_a123_sandwichFreq` | page 123 | Occupant classification system: a123 sandwich freq | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `OCS1P_a124_cushionSelfFreq` | page 124 | Occupant classification system: a124 cushion self freq | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `OCS1P_a125_cushionSelfFreq` | page 125 | Occupant classification system: a125 cushion self freq | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `OCS1P_a126_cushionSelfFreq` | page 126 | Occupant classification system: a126 cushion self freq | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `OCS1P_a127_seatbackSelfFreq` | page 127 | Occupant classification system: a127 seatback self freq | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `OCS1P_a128_seatbackSelfFreq` | page 128 | Occupant classification system: a128 seatback self freq | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `OCS1P_a129_seatbackSelfFreq` | page 129 | Occupant classification system: a129 seatback self freq | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `OCS1P_a130_sandwichNoCalib` | page 130 | Occupant classification system: a130 sandwich no calib | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_a131_cushionSelfNoCalib` | page 131 | Occupant classification system: a131 cushion self no calib | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_a132_seatbackSelfNoCalib` | page 132 | Occupant classification system: a132 seatback self no calib | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_a133_sandwichBadCalib` | page 133 | Occupant classification system: a133 sandwich bad calib | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_a134_uninitializedCalib` | page 134 | Occupant classification system: a134 uninitialized calib | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_a135_tempNoCalib` | page 135 | Occupant classification system: a135 temp no calib | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_a140_tempInvalidCalib` | page 140 | Occupant classification system: a140 temp invalid calib | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_a141_humidityInvalidCalib` | page 141 | Occupant classification system: a141 humidity invalid calib | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_a142_tempHumidityInvalid` | page 142 | Occupant classification system: a142 temp humidity invalid | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_a143_mismatchPassAirbag` | page 143 | Occupant classification system: a143 mismatch pass airbag | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `OCS1P_a144_mismatchCarRegion` | page 144 | Occupant classification system: a144 mismatch car region | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Multiplexing

`OCS1P_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 121 (1 signals), page 122 (1 signals), page 123 (1 signals), page 124 (1 signals), page 125 (1 signals), page 126 (1 signals), page 127 (1 signals), page 128 (1 signals), page 129 (1 signals), page 130 (1 signals), page 131 (1 signals), page 132 (1 signals), page 133 (1 signals), page 134 (1 signals), page 135 (1 signals), page 140 (1 signals), page 141 (1 signals), page 142 (1 signals), page 143 (1 signals), page 144 (1 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Occupant classification system messages (OCS1P)](../../ocs1p.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
