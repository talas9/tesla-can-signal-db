---
layout: default
title: "FC_alertLog (0x52A) — FC ECU, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "FC ECU message: alert log. Tesla Model Y CAN bus message FC_alertLog (0x52A) of FC ECU, firmware 2026.26.6.5, 8 signals (FC_alertID, FC_alertType, FC_a130_CA_flybackSwOvType, FC_a146_CA_flybackOnTime and 4 more). Bit layout, scaling, units and value tables."
---

# FC_alertLog (0x52A) — FC ECU, Tesla Model Y 2026.26.6.5 VEH CAN

FC ECU message: alert log; frame length from the layout, not yet observed on a vehicle bus. This page documents the 8 signals of FC_alertLog as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `FC_alertLog` |
| CAN id | 0x52A (1322) |
| ECU | [FC ECU](../../fc.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | FC |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 8 |

## Signals of FC_alertLog

Tesla Model Y CAN bus signals in `FC_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `FC_alertID` | selector | FC ECU: alert ID | 0\|15 | little-endian | unsigned | 1 | 0 |  | 0 to 32767 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>129 = `a129_CA_flyback_HW_OC`<br>130 = `a130_CA_flyback_SW_OV`<br>131 = `a131_CA_flyback_HW_OV`<br>132 = `a132_CA_bmsMia`<br>133 = `a133_CA_evseMia`<br>134 = `a134_CA_vehTxBufOvf`<br>135 = `a135_CA_vehRxBufOvf`<br>136 = `a136_CA_evseTxBufOvf`<br>137 = `a137_CA_evseRxBufOvf`<br>138 = `a138_CA_hwProxTrip`<br>139 = `a139_CA_ss2NotLow`<br>140 = `a140_CA_bmsIncompatible`<br>141 = `a141_CA_vehConn_OT`<br>142 = `a142_CA_evseConn_OT`<br>143 = `a143_CA_pcb_OT`<br>144 = `a144_CA_flybackUnstable`<br>145 = `a145_CA_flybackDataStale`<br>146 = `a146_CA_flybackBusLoadHi`<br>147 = `a147_CA_vehConn_UT`<br>148 = `a148_CA_evseConn_UT`<br>149 = `a149_CA_pcb_UT`<br>150 = `a150_CA_vehToEvseDeltaHi`<br>151 = `a151_CA_vehToEvseDeltaLo`<br>152 = `a152_CA_vehToPcbDeltaHi`<br>153 = `a153_CA_evseToPcbDeltaHi`<br>154 = `a154_CA_vehToPcbDeltaLo`<br>155 = `a155_CA_evseToPcbDeltaLo`<br>156 = `a156_CA_flybackRunTimeout`<br>157 = `a157_CA_unused`<br>158 = `a158_CA_evseOverCurrent`<br>159 = `a159_CA_wdtExpired`<br>160 = `a160_CA_ss2Deasserted`<br>161 = `a161_CA_vehTempHiFoldBk`<br>162 = `a162_CA_evseTempHiFoldBk`<br>163 = `a163_CA_pcbTempHiFoldBk`<br>164 = `a164_CA_proxDisconnected`<br>165 = `a165_CA_evseConnUnlocked`<br>166 = `a166_CA_vehConnUnlocked`<br>167 = `a167_CA_isoVoltageLow`<br>168 = `a168_CA_proxTimeout`<br>169 = `a169_CA_pilotAcceptTimeout`<br>170 = `a170_CA_vehDataTimeout`<br>171 = `a171_CA_vehConLockTimeout`<br>172 = `a172_CA_ss2LowTimeout`<br>173 = `a173_CA_evseDataTimeout`<br>174 = `a174_CA_vehReadyTimeout`<br>175 = `a175_CA_evseIsoTestTimeout`<br>176 = `a176_CA_chargingBusTimeout`<br>177 = `a177_CA_bmsCtrCloseTimeout`<br>178 = `a178_CA_evseStartTimeout`<br>179 = `a179_CA_startupProblem`<br>180 = `a180_CA_chargingProblem`<br>181 = `a181_CA_vRegBrownout`<br>182 = `a182_CA_evseChrMalfunc`<br>183 = `a183_CA_evseBatIncompat`<br>184 = `a184_CA_evseBatMalfunc`<br>185 = `a185_CA_vehReadyDeasserted`<br>186 = `a186_CA_fcContOpenTimeout`<br>187 = `a187_CA_evseConLockTimeout`<br>193 = `a193_FCAlertPlaceholder`<br>257 = `a257_GB_bmsMia`<br>258 = `a258_GB_evseMia`<br>259 = `a259_GB_vehTxBufOvf`<br>260 = `a260_GB_vehRxBufOvf`<br>261 = `a261_GB_evseTxBufOvf`<br>262 = `a262_GB_evseRxBufOvf`<br>263 = `a263_GB_hwProxTrip`<br>264 = `a264_GB_timeoutCHM`<br>265 = `a265_GB_bmsIncompatible`<br>266 = `a266_GB_negPin_OT`<br>267 = `a267_GB_posPin_OT`<br>268 = `a268_GB_pcb_OT`<br>269 = `a269_GB_timeoutCRM`<br>270 = `a270_GB_timeoutCML`<br>271 = `a271_GB_timeoutCRO`<br>272 = `a272_GB_negToPosDeltaHi`<br>273 = `a273_GB_negToPosDeltaLo`<br>274 = `a274_GB_negToPcbDeltaHi`<br>275 = `a275_GB_posToPcbDeltaHi`<br>276 = `a276_GB_negToPcbDeltaLo`<br>277 = `a277_GB_posToPcbDeltaLo`<br>278 = `a278_GB_timeoutCCS`<br>279 = `a279_GB_evseOverCurrent`<br>280 = `a280_GB_retryLimitExceeded`<br>281 = `a281_GB_evseOutOfService`<br>282 = `a282_GB_negTempHiFoldBk`<br>283 = `a283_GB_posTempHiFoldBk`<br>284 = `a284_GB_pcbTempHiFoldBk`<br>285 = `a285_GB_proxDisconnected`<br>286 = `a286_GB_evseConnUnlocked`<br>287 = `a287_GB_vehConnUnlocked`<br>288 = `a288_GB_evseAbnormalStopReq`<br>289 = `a289_GB_proxTimeout`<br>290 = `a290_GB_pilotAcceptTimeout`<br>291 = `a291_GB_vehDataTimeout`<br>292 = `a292_GB_vehConLockTimeout`<br>293 = `a293_GB_proxRationality`<br>294 = `a294_GB_unused`<br>295 = `a295_GB_pilotRationality`<br>296 = `a296_GB_invalidPilotTransitio`<br>297 = `a297_GB_unused`<br>298 = `a298_GB_bmsCtrCloseTimeout`<br>299 = `a299_GB_evseReadyTimeout`<br>300 = `a300_GB_unused`<br>301 = `a301_GB_unused`<br>302 = `a302_GB_unused`<br>303 = `a303_GB_negRecogTimeout`<br>304 = `a304_GB_unused`<br>305 = `a305_GB_posRecogTimeout`<br>306 = `a306_GB_vehReadyDeasserted`<br>307 = `a307_GB_fcContOpenTimeout`<br>308 = `a308_GB_evseConLockTimeout`<br>309 = `a309_GB_unused`<br>310 = `a310_GB_unused`<br>311 = `a311_GB_battParamsTimeout`<br>312 = `a312_GB_evseLimitsTimeout`<br>313 = `a313_GB_inputVoltageRailOv`<br>321 = `a321_FCAlertPlaceholder` | plausible |
| `FC_alertType` |  | FC ECU: alert type | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `WARNING`<br>1 = `FAULT` | plausible |
| `FC_a130_CA_flybackSwOvType` | page 130 | FC ECU: a130 CA flyback sw ov type | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `FC_a146_CA_flybackOnTime` | page 146 | FC ECU: a146 CA flyback on time | 16\|16 | little-endian | unsigned | 0.0007629511 | 0 | uS | 0 to 50.0000003385 |  | plausible |
| `FC_a146_CA_flybackV` | page 146 | FC ECU: a146 CA flyback v | 32\|16 | little-endian | unsigned | 0.0128332730383 | 0 | V | 0 to 841.028548565 |  | plausible |
| `FC_a146_CA_flybackTargetV` | page 146 | FC ECU: a146 CA flyback target v | 48\|16 | little-endian | unsigned | 0.0128332730383 | 0 | V | 0 to 841.028548565 |  | plausible |
| `FC_a159_CA_wdtTaskList1` | page 159 | FC ECU: a159 CA wdt task list1 | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |
| `FC_a159_CA_wdtTaskList2` | page 159 | FC ECU: a159 CA wdt task list2 | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | layout-only |

## Multiplexing

`FC_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 130 (1 signals), page 146 (3 signals), page 159 (2 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All FC ECU messages (FC)](../../fc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
