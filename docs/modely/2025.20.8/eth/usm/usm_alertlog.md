---
layout: default
title: "USM_alertLog (0x5F0) — USM ECU, Tesla Model Y 2025.20.8 ETH"
description: "USM ECU message: alert log. Ethernet-side message USM_alertLog of USM ECU for Tesla Model Y firmware 2025.20.8, 941 signals (USM_alertID, USM_alertState, USM_a001_InternalWatchdog, USM_a002_CPUUndervoltage and 937 more). Bit layout, scaling, units and value tables."
---

# USM_alertLog (0x5F0) — USM ECU, Tesla Model Y 2025.20.8 ETH

USM ECU message: alert log. This page documents the 941 signals of USM_alertLog as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `USM_alertLog` |
| Ethernet-side id | 0x5F0 (1520) |
| ECU | [USM ECU](../../usm.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | USM |
| Frame length | 8 bytes |
| Cycle time | not cyclic or not known |
| Signals | 941 |

## Signals of USM_alertLog

Tesla Model Y CAN bus signals in `USM_alertLog`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `USM_alertID` | selector | USM ECU: alert ID | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `ALERT_DO_NOT_USE_ZERO`<br>1 = `a001_WatchdogReset`<br>2 = `a002_PowerLossReset`<br>3 = `a003_SWAssertion`<br>5 = `a005_CANTXError`<br>6 = `a006_CANTX_cyclicError`<br>12 = `a012_CPUReset`<br>13 = `a013_AlertManagerFault`<br>15 = `a015_NVMMError`<br>16 = `a016_NVMMRecordError`<br>21 = `a021_TaskSchedulerError`<br>22 = `a022_TaskInitError`<br>29 = `a029_CoreDump`<br>30 = `a030_ECULogUploadRequest`<br>31 = `a031_UDSActive`<br>41 = `a041_HighCPULoad`<br>42 = `a042_HighStackUsage`<br>43 = `a043_Task1msError`<br>44 = `a044_Task10msError`<br>45 = `a045_Task100msError`<br>46 = `a046_Task1000msError`<br>57 = `a057_HVP_MIA`<br>58 = `a058_inputRHighSyncDebug`<br>59 = `a059_inputResistanceHigh`<br>60 = `a060_engineeringBuild`<br>61 = `a061_XCPConnected`<br>62 = `a062_XCPWasConnected`<br>63 = `a063_SwitchFault`<br>64 = `a064_busSleepReqTimeout`<br>82 = `a082_VCRIGHT_IPC_MIA`<br>83 = `a083_VCLEFT_IPC_MIA`<br>84 = `a084_TPMS_MIA`<br>85 = `a085_CCCM_MIA`<br>86 = `a086_VCBATT_MIA`<br>87 = `a087_DIREL_MIA`<br>88 = `a088_DIRER_MIA`<br>89 = `a089_IBST_MIA`<br>90 = `a090_APS_MIA`<br>91 = `a091_CMPD_MIA`<br>92 = `a092_VCSEATD_MIA`<br>93 = `a093_VCSEATP_MIA`<br>94 = `a094_EPAS3P_MIA`<br>95 = `a095_CHG_MIA`<br>96 = `a096_OCS1P_MIA`<br>97 = `a097_CMP_MIA`<br>98 = `a098_DIR_MIA`<br>99 = `a099_PARK_MIA`<br>100 = `a100_CANbus_MIA`<br>101 = `a101_PM_MIA`<br>102 = `a102_PTC_MIA`<br>103 = `a103_CP_MIA`<br>104 = `a104_DAS_MIA`<br>105 = `a105_TAS_MIA`<br>106 = `a106_PCS_MIA`<br>107 = `a107_BMS_MIA`<br>108 = `a108_DIF_MIA`<br>109 = `a109_RCM_MIA`<br>110 = `a110_GTW_MIA`<br>111 = `a111_EPBR_MIA`<br>112 = `a112_EPBL_MIA`<br>113 = `a113_UI_MIA`<br>114 = `a114_ESP_MIA`<br>115 = `a115_VCSEC_MIA`<br>116 = `a116_VCRIGHT_MIA`<br>117 = `a117_VCLEFT_MIA`<br>118 = `a118_VCFRONT_MIA`<br>119 = `a119_SCCM_MIA`<br>120 = `a120_DI_DRIVE_MIA`<br>131 = `a131_s1ComError`<br>132 = `a132_s2ComError`<br>133 = `a133_s3ComError`<br>134 = `a134_s4ComError`<br>135 = `a135_s5ComError`<br>136 = `a136_s6ComError`<br>137 = `a137_s7ComError`<br>138 = `a138_s8ComError`<br>139 = `a139_s9ComError`<br>140 = `a140_s10ComError`<br>141 = `a141_s11ComError`<br>142 = `a142_s12ComError`<br>143 = `a143_s1HwError`<br>144 = `a144_s2HwError`<br>145 = `a145_s3HwError`<br>146 = `a146_s4HwError`<br>147 = `a147_s5HwError`<br>148 = `a148_s6HwError`<br>149 = `a149_s7HwError`<br>150 = `a150_s8HwError`<br>151 = `a151_s9HwError`<br>152 = `a152_s10HwError`<br>153 = `a153_s11HwError`<br>154 = `a154_s12HwError`<br>155 = `a155_s1OverTemp`<br>156 = `a156_s2OverTemp`<br>157 = `a157_s3OverTemp`<br>158 = `a158_s4OverTemp`<br>159 = `a159_s5OverTemp`<br>160 = `a160_s6OverTemp`<br>161 = `a161_s7OverTemp`<br>162 = `a162_s8OverTemp`<br>163 = `a163_s9OverTemp`<br>164 = `a164_s10OverTemp`<br>165 = `a165_s11OverTemp`<br>166 = `a166_s12OverTemp`<br>177 = `a177_s1Blocked`<br>178 = `a178_s2Blocked`<br>179 = `a179_s3Blocked`<br>180 = `a180_s4Blocked`<br>181 = `a181_s5Blocked`<br>182 = `a182_s6Blocked`<br>183 = `a183_s7Blocked`<br>184 = `a184_s8Blocked`<br>185 = `a185_s9Blocked`<br>186 = `a186_s10Blocked`<br>187 = `a187_s11Blocked`<br>188 = `a188_s12Blocked`<br>189 = `a189_s1Disconnected`<br>190 = `a190_s2Disconnected`<br>191 = `a191_s3Disconnected`<br>192 = `a192_s4Disconnected`<br>193 = `a193_s5Disconnected`<br>194 = `a194_s6Disconnected`<br>195 = `a195_s7Disconnected`<br>196 = `a196_s8Disconnected`<br>197 = `a197_s9Disconnected`<br>198 = `a198_s10Disconnected`<br>199 = `a199_s11Disconnected`<br>200 = `a200_s12Disconnected`<br>201 = `a201_e52142Fault`<br>202 = `a202_e52417Fault`<br>203 = `a203_s1NearFieldDetected`<br>204 = `a204_s2NearFieldDetected`<br>205 = `a205_s3NearFieldDetected`<br>206 = `a206_s4NearFieldDetected`<br>207 = `a207_s5NearFieldDetected`<br>208 = `a208_s6NearFieldDetected`<br>209 = `a209_s7NearFieldDetected`<br>210 = `a210_s8NearFieldDetected`<br>211 = `a211_s9NearFieldDetected`<br>212 = `a212_s10NearFieldDetected`<br>213 = `a213_s11NearFieldDetected`<br>214 = `a214_s12NearFieldDetected`<br>215 = `a215_s1DebugEepromInvalid`<br>216 = `a216_s2DebugEepromInvalid`<br>217 = `a217_s3DebugEepromInvalid`<br>218 = `a218_s4DebugEepromInvalid`<br>219 = `a219_s5DebugEepromInvalid`<br>220 = `a220_s6DebugEepromInvalid`<br>221 = `a221_s7DebugEepromInvalid`<br>222 = `a222_s8DebugEepromInvalid`<br>223 = `a223_s9DebugEepromInvalid`<br>224 = `a224_s10DebugEepromInvalid`<br>225 = `a225_s11DebugEepromInvalid`<br>226 = `a226_s12DebugEepromInvalid`<br>227 = `a227_s1InitError`<br>228 = `a228_s2InitError`<br>229 = `a229_s3InitError`<br>230 = `a230_s4InitError`<br>231 = `a231_s5InitError`<br>232 = `a232_s6InitError`<br>233 = `a233_s7InitError`<br>234 = `a234_s8InitError`<br>235 = `a235_s9InitError`<br>236 = `a236_s10InitError`<br>237 = `a237_s11InitError`<br>238 = `a238_s12InitError`<br>240 = `a240_s1HwComErrDiagnostics`<br>241 = `a241_s2HwComErrDiagnostics`<br>242 = `a242_s3HwComErrDiagnostics`<br>243 = `a243_s4HwComErrDiagnostics`<br>244 = `a244_s5HwComErrDiagnostics`<br>245 = `a245_s6HwComErrDiagnostics`<br>246 = `a246_s7HwComErrDiagnostics`<br>247 = `a247_s8HwComErrDiagnostics`<br>248 = `a248_s9HwComErrDiagnostics`<br>249 = `a249_s10HwComErrDiagnostics`<br>250 = `a250_s11HwComErrDiagnostics`<br>251 = `a251_s12HwComErrDiagnostics`<br>252 = `a252_anyComErrorSet`<br>253 = `a253_anyHwErrorSet`<br>254 = `a254_frontSensorsOvercurrent`<br>255 = `a255_rearSensorsOvercurrent` | plausible |
| `USM_alertState` |  | USM ECU: alert state | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CLEARED`<br>1 = `SET` | plausible |
| `USM_a001_InternalWatchdog` | page 1 | USM ECU: a001 internal watchdog | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a002_CPUUndervoltage` | page 2 | USM ECU: a002 CPU undervoltage | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a002_PowerOnReset` | page 2 | USM ECU: a002 power on reset | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a015_NVMMMemOverflow` | page 15 | USM ECU: a015 NVMM mem overflow | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a015_NVMMFilesystemError` | page 15 | USM ECU: a015 NVMM filesystem error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a015_NVMMRecordIDError` | page 15 | USM ECU: a015 NVMM record ID error | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a057_VEH_cpControl` | page 57 | USM ECU: a057 VEH cp control | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a059_voltageDrop` | page 59 | USM ECU: a059 voltage drop | 16\|12 | little-endian | unsigned | 0.005443676 | 0 | V | 0 to 22.29185322 |  | plausible |
| `USM_a059_resistanceEstimate` | page 59 | USM ECU: a059 resistance estimate | 28\|12 | little-endian | unsigned | 0.00244 | 0 | Ohms | 0 to 9.9918 |  | plausible |
| `USM_a059_current` | page 59 | USM ECU: a059 current | 40\|12 | little-endian | unsigned | 0.05 | 0 | A | 0 to 204.75 |  | plausible |
| `USM_a063_switchChannel` | page 63 | USM ECU: a063 switch channel | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a063_switchType` | page 63 | USM ECU: a063 switch type | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a063_ADCVoltage` | page 63 | USM ECU: a063 ADC voltage | 32\|8 | little-endian | unsigned | 0.025 | 0 | V | 0 to 6.375 |  | plausible |
| `USM_a063_disconnected` | page 63 | USM ECU: a063 disconnected | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a063_indeterminate` | page 63 | USM ECU: a063 indeterminate | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a063_stuckActive` | page 63 | USM ECU: a063 stuck active | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a063_faulted` | page 63 | USM ECU: a063 faulted | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a082_RIPC_epbPrivateState` | page 82 | USM ECU: a082 RIPC epb private state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a082_RIPC_remoteHSD` | page 82 | USM ECU: a082 RIPC remote HSD | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a082_RIPC_railStatus` | page 82 | USM ECU: a082 RIPC rail status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a082_RIPC_remoteMux` | page 82 | USM ECU: a082 RIPC remote mux | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a083_LIPC_epbPrivateState` | page 83 | USM ECU: a083 LIPC epb private state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a083_LIPC_remoteHSD` | page 83 | USM ECU: a083 LIPC remote HSD | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a083_LIPC_railStatus` | page 83 | USM ECU: a083 LIPC rail status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a083_LIPC_HSDFaults` | page 83 | USM ECU: a083 LIPC HSD faults | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a084_CH_StatusC` | page 84 | USM ECU: a084 CH status c | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a085_PARTY_buttonStatus` | page 85 | USM ECU: a085 PARTY button status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a086_VEH_LVBMS_statusHigh` | page 86 | USM ECU: a086 VEH LVBMS status high | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a086_VEH_LVBMS_statusLow` | page 86 | USM ECU: a086 VEH LVBMS status low | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a086_VEH_status` | page 86 | USM ECU: a086 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a086_VEH_12VBatteryStatus` | page 86 | USM ECU: a086 VEH 12 v battery status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a086_VEH_LVPowerState` | page 86 | USM ECU: a086 VEH LV power state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a086_VEH_lightStatus` | page 86 | USM ECU: a086 VEH light status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a086_VEH_systemStatus` | page 86 | USM ECU: a086 VEH system status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a086_VEH_thermalStatus` | page 86 | USM ECU: a086 VEH thermal status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a086_VEH_vehNm` | page 86 | USM ECU: a086 VEH veh nm | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a087_VEH_temperature` | page 87 | USM ECU: a087 VEH temperature | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a087_VEH_thermalControl` | page 87 | USM ECU: a087 VEH thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a087_VEH_torque` | page 87 | USM ECU: a087 VEH torque | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a087_VEH_status` | page 87 | USM ECU: a087 VEH status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a087_PARTY_torque` | page 87 | USM ECU: a087 PARTY torque | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a087_PARTY_status` | page 87 | USM ECU: a087 PARTY status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a087_PARTY_temperature` | page 87 | USM ECU: a087 PARTY temperature | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a087_PARTY_thermalControl` | page 87 | USM ECU: a087 PARTY thermal control | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a088_VEH_temperature` | page 88 | USM ECU: a088 VEH temperature | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a088_VEH_thermalControl` | page 88 | USM ECU: a088 VEH thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a088_VEH_torque` | page 88 | USM ECU: a088 VEH torque | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a088_VEH_status` | page 88 | USM ECU: a088 VEH status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a088_PARTY_torque` | page 88 | USM ECU: a088 PARTY torque | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a088_PARTY_status` | page 88 | USM ECU: a088 PARTY status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a088_PARTY_temperature` | page 88 | USM ECU: a088 PARTY temperature | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a088_PARTY_thermalControl` | page 88 | USM ECU: a088 PARTY thermal control | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a089_PARTY_party1` | page 89 | USM ECU: a089 PARTY party1 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a089_PARTY_status` | page 89 | USM ECU: a089 PARTY status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a089_VEH_status` | page 89 | USM ECU: a089 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a089_BDY_party1` | page 89 | USM ECU: a089 BDY party1 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a089_BDY_status` | page 89 | USM ECU: a089 BDY status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a089_CH_status` | page 89 | USM ECU: a089 CH status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a089_CH_party1` | page 89 | USM ECU: a089 CH party1 | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a089_CH_party3` | page 89 | USM ECU: a089 CH party3 | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a089_VEH_party1` | page 89 | USM ECU: a089 VEH party1 | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a089_VEH_party3` | page 89 | USM ECU: a089 VEH party3 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a091_VEH_faultsAndExtras` | page 91 | USM ECU: a091 VEH faults and extras | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a091_VEH_info` | page 91 | USM ECU: a091 VEH info | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a091_VEH_state` | page 91 | USM ECU: a091 VEH state | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a092_VEH_restraintStatus` | page 92 | USM ECU: a092 VEH restraint status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a092_VEH_switchStatus` | page 92 | USM ECU: a092 VEH switch status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a092_VEH_seatStatus2` | page 92 | USM ECU: a092 VEH seat status2 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a092_VEH_vehNm` | page 92 | USM ECU: a092 VEH veh nm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a093_VEH_restraintStatus` | page 93 | USM ECU: a093 VEH restraint status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a093_VEH_switchStatus` | page 93 | USM ECU: a093 VEH switch status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a093_VEH_seatStatus2` | page 93 | USM ECU: a093 VEH seat status2 | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a093_VEH_vehNm` | page 93 | USM ECU: a093 VEH veh nm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a094_VEH_sysStatus` | page 94 | USM ECU: a094 VEH sys status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a094_PARTY_sysStatus` | page 94 | USM ECU: a094 PARTY sys status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a095_PT_ptNm` | page 95 | USM ECU: a095 PT pt nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a095_PT_status` | page 95 | USM ECU: a095 PT status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a096_VEH_status` | page 96 | USM ECU: a096 VEH status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a096_CH_status` | page 96 | USM ECU: a096 CH status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a098_CH_torque` | page 98 | USM ECU: a098 CH torque | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a098_VEH_hvStatus` | page 98 | USM ECU: a098 VEH hv status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a098_VEH_status` | page 98 | USM ECU: a098 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a098_VEH_thermalControl` | page 98 | USM ECU: a098 VEH thermal control | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a098_VEH_temperature` | page 98 | USM ECU: a098 VEH temperature | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a098_VEH_torque` | page 98 | USM ECU: a098 VEH torque | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a098_PARTY_status` | page 98 | USM ECU: a098 PARTY status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a098_PARTY_temperature` | page 98 | USM ECU: a098 PARTY temperature | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a098_PARTY_thermalControl` | page 98 | USM ECU: a098 PARTY thermal control | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a098_PARTY_torque` | page 98 | USM ECU: a098 PARTY torque | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a098_PT_thermalControl` | page 98 | USM ECU: a098 PT thermal control | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a098_PT_temperature` | page 98 | USM ECU: a098 PT temperature | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a099_VEH_oocStatus` | page 99 | USM ECU: a099 VEH ooc status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a100_VEH` | page 100 | USM ECU: a100 VEH | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a100_PARTY` | page 100 | USM ECU: a100 PARTY | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a100_PT` | page 100 | USM ECU: a100 PT | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a100_CH` | page 100 | USM ECU: a100 CH | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a100_OBD` | page 100 | USM ECU: a100 OBD | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a101_VEH_state` | page 101 | USM ECU: a101 VEH state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a101_PARTY_locState` | page 101 | USM ECU: a101 PARTY loc state | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a101_LIPC_externalWatchdogHeartBeat` | page 101 | USM ECU: a101 LIPC external watchdog heart beat | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a101_VEH_locState` | page 101 | USM ECU: a101 VEH loc state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a101_BDY_locState` | page 101 | USM ECU: a101 BDY loc state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a102_VEH_faultsAndExtras` | page 102 | USM ECU: a102 VEH faults and extras | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a102_VEH_feedbackStatus` | page 102 | USM ECU: a102 VEH feedback status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a102_VEH_sensorStatus` | page 102 | USM ECU: a102 VEH sensor status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a102_VEH_rods` | page 102 | USM ECU: a102 VEH rods | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a103_VEH_hvsNm` | page 103 | USM ECU: a103 VEH hvs nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a103_VEH_vehNm` | page 103 | USM ECU: a103 VEH veh nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a103_VEH_status` | page 103 | USM ECU: a103 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a103_PT_ptNm` | page 103 | USM ECU: a103 PT pt nm | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a103_PT_status` | page 103 | USM ECU: a103 PT status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a103_VEH_evseStatus` | page 103 | USM ECU: a103 VEH evse status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a105_VEH_states` | page 105 | USM ECU: a105 VEH states | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a105_VEH_chNm` | page 105 | USM ECU: a105 VEH ch nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a105_VEH_dampingStates` | page 105 | USM ECU: a105 VEH damping states | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a106_VEH_dcdcStatus` | page 106 | USM ECU: a106 VEH dcdc status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a106_VEH_thermalControl` | page 106 | USM ECU: a106 VEH thermal control | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a106_VEH_thermalInterface` | page 106 | USM ECU: a106 VEH thermal interface | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a106_VEH_dcdcRailStatus` | page 106 | USM ECU: a106 VEH dcdc rail status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a106_CH_dcdcRailStatus` | page 106 | USM ECU: a106 CH dcdc rail status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a106_CH_alertMatrix` | page 106 | USM ECU: a106 CH alert matrix | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a107_VEH_hvsNm` | page 107 | USM ECU: a107 VEH hvs nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a107_VEH_vehNm` | page 107 | USM ECU: a107 VEH veh nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a107_VEH_status` | page 107 | USM ECU: a107 VEH status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a107_VEH_thermalStatus` | page 107 | USM ECU: a107 VEH thermal status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a107_VEH_thermalStatus2` | page 107 | USM ECU: a107 VEH thermal status2 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a107_VEH_bmbMinMax` | page 107 | USM ECU: a107 VEH bmb min max | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a107_VEH_powerAvailable` | page 107 | USM ECU: a107 VEH power available | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a107_PT_ptNm` | page 107 | USM ECU: a107 PT pt nm | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a107_PT_status` | page 107 | USM ECU: a107 PT status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a107_PT_thermalStatus` | page 107 | USM ECU: a107 PT thermal status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a107_PT_socStatus` | page 107 | USM ECU: a107 PT soc status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a107_VEH_socStatus` | page 107 | USM ECU: a107 VEH soc status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a107_VEH_packConfig` | page 107 | USM ECU: a107 VEH pack config | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a107_VEH_energyStatus` | page 107 | USM ECU: a107 VEH energy status | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a107_VEH_chargeInfo` | page 107 | USM ECU: a107 VEH charge info | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a108_VEH_hvStatus` | page 108 | USM ECU: a108 VEH hv status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a108_VEH_temperature` | page 108 | USM ECU: a108 VEH temperature | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a108_VEH_thermalControl` | page 108 | USM ECU: a108 VEH thermal control | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a108_VEH_torque` | page 108 | USM ECU: a108 VEH torque | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a108_VEH_status` | page 108 | USM ECU: a108 VEH status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a108_PARTY_torque` | page 108 | USM ECU: a108 PARTY torque | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a108_PARTY_status` | page 108 | USM ECU: a108 PARTY status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a108_PARTY_temperature` | page 108 | USM ECU: a108 PARTY temperature | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a108_PARTY_thermalControl` | page 108 | USM ECU: a108 PARTY thermal control | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a108_PT_temperature` | page 108 | USM ECU: a108 PT temperature | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a108_PT_thermalControl` | page 108 | USM ECU: a108 PT thermal control | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a109_PARTY_status` | page 109 | USM ECU: a109 PARTY status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a109_PARTY_inertial2` | page 109 | USM ECU: a109 PARTY inertial2 | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a109_PARTY_nearDeploy` | page 109 | USM ECU: a109 PARTY near deploy | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a109_PARTY_collision` | page 109 | USM ECU: a109 PARTY collision | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a109_VEH_status` | page 109 | USM ECU: a109 VEH status | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a109_VEH_imuOffsets` | page 109 | USM ECU: a109 VEH imu offsets | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a109_PARTY_inertial1` | page 109 | USM ECU: a109 PARTY inertial1 | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a109_BDY_imuOffsets` | page 109 | USM ECU: a109 BDY imu offsets | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a109_BDY_inertial1` | page 109 | USM ECU: a109 BDY inertial1 | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a109_BDY_inertial2` | page 109 | USM ECU: a109 BDY inertial2 | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a109_BDY_status` | page 109 | USM ECU: a109 BDY status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a109_VEH_inertial1` | page 109 | USM ECU: a109 VEH inertial1 | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a109_VEH_inertial2` | page 109 | USM ECU: a109 VEH inertial2 | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a109_CH_inertial1` | page 109 | USM ECU: a109 CH inertial1 | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a109_CH_inertial2` | page 109 | USM ECU: a109 CH inertial2 | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a109_CH_status` | page 109 | USM ECU: a109 CH status | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a110_VEH_carState` | page 110 | USM ECU: a110 VEH car state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a110_VEH_carConfig` | page 110 | USM ECU: a110 VEH car config | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a110_VEH_time` | page 110 | USM ECU: a110 VEH time | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a110_VEH_updateStatus` | page 110 | USM ECU: a110 VEH update status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a110_VEH_vehNm` | page 110 | USM ECU: a110 VEH veh nm | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a110_VEH_mismatchFault` | page 110 | USM ECU: a110 VEH mismatch fault | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a110_VEH_vin` | page 110 | USM ECU: a110 VEH vin | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a110_VEH_bmpDebug` | page 110 | USM ECU: a110 VEH bmp debug | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a110_VEH_gearControl` | page 110 | USM ECU: a110 VEH gear control | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a110_VEH_canLogAvailability` | page 110 | USM ECU: a110 VEH can log availability | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a110_CH_airbagCutoffStatus` | page 110 | USM ECU: a110 CH airbag cutoff status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a110_CH_carConfig` | page 110 | USM ECU: a110 CH car config | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a110_CH_carState` | page 110 | USM ECU: a110 CH car state | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a110_CH_vin` | page 110 | USM ECU: a110 CH vin | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a110_CH_chNm` | page 110 | USM ECU: a110 CH ch nm | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a110_CH_epochTimeGtw` | page 110 | USM ECU: a110 CH epoch time gtw | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a111_VEH_internalStatus` | page 111 | USM ECU: a111 VEH internal status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a111_VEH_status` | page 111 | USM ECU: a111 VEH status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a111_VEH_vehNm` | page 111 | USM ECU: a111 VEH veh nm | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a111_RIPC_LVPowerState` | page 111 | USM ECU: a111 RIPC LV power state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a111_RIPC_epbPrivateState` | page 111 | USM ECU: a111 RIPC epb private state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a111_RIPC_railStatus` | page 111 | USM ECU: a111 RIPC rail status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a111_RIPC_remoteADC` | page 111 | USM ECU: a111 RIPC remote ADC | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a111_RIPC_switchStatus` | page 111 | USM ECU: a111 RIPC switch status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a111_VEH_LVPowerState` | page 111 | USM ECU: a111 VEH LV power state | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a111_VEH_seatStatus` | page 111 | USM ECU: a111 VEH seat status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a111_PARTY_status` | page 111 | USM ECU: a111 PARTY status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a111_CH_status` | page 111 | USM ECU: a111 CH status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a112_VEH_internalStatus` | page 112 | USM ECU: a112 VEH internal status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a112_VEH_status` | page 112 | USM ECU: a112 VEH status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a112_VEH_vehNm` | page 112 | USM ECU: a112 VEH veh nm | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a112_LIPC_LVPowerState` | page 112 | USM ECU: a112 LIPC LV power state | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a112_LIPC_epbPrivateState` | page 112 | USM ECU: a112 LIPC epb private state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a112_LIPC_railStatus` | page 112 | USM ECU: a112 LIPC rail status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a112_LIPC_remoteADC` | page 112 | USM ECU: a112 LIPC remote ADC | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a112_LIPC_switchStatus` | page 112 | USM ECU: a112 LIPC switch status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a112_VEH_LVPowerState` | page 112 | USM ECU: a112 VEH LV power state | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a112_PARTY_status` | page 112 | USM ECU: a112 PARTY status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a112_CH_status` | page 112 | USM ECU: a112 CH status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a114_PARTY_status` | page 114 | USM ECU: a114 PARTY status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a114_PARTY_wheelSpeeds` | page 114 | USM ECU: a114 PARTY wheel speeds | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a114_VEH_wheelSpeeds` | page 114 | USM ECU: a114 VEH wheel speeds | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a114_CH_wheelSpeeds` | page 114 | USM ECU: a114 CH wheel speeds | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a114_PARTY_party3` | page 114 | USM ECU: a114 PARTY party3 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a114_VEH_party3` | page 114 | USM ECU: a114 VEH party3 | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a114_VEH_status` | page 114 | USM ECU: a114 VEH status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a114_PARTY_wheelRotation` | page 114 | USM ECU: a114 PARTY wheel rotation | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a114_CH_wheelRotation` | page 114 | USM ECU: a114 CH wheel rotation | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a114_VEH_wheelRotation` | page 114 | USM ECU: a114 VEH wheel rotation | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a114_PARTY_brakeTorque` | page 114 | USM ECU: a114 PARTY brake torque | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a114_PARTY_offsets` | page 114 | USM ECU: a114 PARTY offsets | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a114_BDY_offsets` | page 114 | USM ECU: a114 BDY offsets | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a114_BDY_party3` | page 114 | USM ECU: a114 BDY party3 | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a114_BDY_status` | page 114 | USM ECU: a114 BDY status | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a114_BDY_wheelRotation` | page 114 | USM ECU: a114 BDY wheel rotation | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a114_BDY_wheelSpeeds` | page 114 | USM ECU: a114 BDY wheel speeds | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a114_CH_party1` | page 114 | USM ECU: a114 CH party1 | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a114_CH_party3` | page 114 | USM ECU: a114 CH party3 | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a114_CH_status` | page 114 | USM ECU: a114 CH status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a115_VEH_vehNm` | page 115 | USM ECU: a115 VEH veh nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a115_VEH_authentication` | page 115 | USM ECU: a115 VEH authentication | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a115_VEH_BLEResetRequest` | page 115 | USM ECU: a115 VEH BLE reset request | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a115_VEH_requests` | page 115 | USM ECU: a115 VEH requests | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a115_VEH_requests2` | page 115 | USM ECU: a115 VEH requests2 | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a115_REM_authentication` | page 115 | USM ECU: a115 REM authentication | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a115_UI_corianderVehicleControl` | page 115 | USM ECU: a115 UI coriander vehicle control | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a115_CH_TPMSDisplay` | page 115 | USM ECU: a115 CH TPMS display | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a116_PARTY_epbmStatus` | page 116 | USM ECU: a116 PARTY epbm status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a116_VEH_vehNm` | page 116 | USM ECU: a116 VEH veh nm | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a116_VEH_hvacRequest` | page 116 | USM ECU: a116 VEH hvac request | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a116_VEH_hvacStatus` | page 116 | USM ECU: a116 VEH hvac status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a116_VEH_LVPowerState` | page 116 | USM ECU: a116 VEH LV power state | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a116_VEH_lightStatus` | page 116 | USM ECU: a116 VEH light status | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a116_VEH_seatStatus` | page 116 | USM ECU: a116 VEH seat status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a116_VEH_thsStatus` | page 116 | USM ECU: a116 VEH ths status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a116_VEH_doorStatus` | page 116 | USM ECU: a116 VEH door status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a116_VEH_seatHeatStatus` | page 116 | USM ECU: a116 VEH seat heat status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a116_VEH_restraintStatus` | page 116 | USM ECU: a116 VEH restraint status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a116_VEH_switchStatus` | page 116 | USM ECU: a116 VEH switch status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a116_VEH_logging1Hz` | page 116 | USM ECU: a116 VEH logging1 hz | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a116_VEH_seatStatus2` | page 116 | USM ECU: a116 VEH seat status2 | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a116_VEH_status` | page 116 | USM ECU: a116 VEH status | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a116_VEH_thermalCommand` | page 116 | USM ECU: a116 VEH thermal command | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a116_VEH_windowStatus` | page 116 | USM ECU: a116 VEH window status | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a116_PARTY_restraintStatus` | page 116 | USM ECU: a116 PARTY restraint status | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a116_PARTY_doorStatus` | page 116 | USM ECU: a116 PARTY door status | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a116_BDY_epbmStatus` | page 116 | USM ECU: a116 BDY epbm status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a116_BDY_restraintStatus` | page 116 | USM ECU: a116 BDY restraint status | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a117_BDY_epbmStatus` | page 117 | USM ECU: a117 BDY epbm status | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a117_BDY_restraintStatus` | page 117 | USM ECU: a117 BDY restraint status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a117_VEH_prndStatus` | page 117 | USM ECU: a117 VEH prnd status | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a117_PARTY_epbmStatus` | page 117 | USM ECU: a117 PARTY epbm status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a117_VEH_vehNm` | page 117 | USM ECU: a117 VEH veh nm | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a117_VEH_hvacBlowerFdb` | page 117 | USM ECU: a117 VEH hvac blower fdb | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a117_VEH_LVPowerState` | page 117 | USM ECU: a117 VEH LV power state | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a117_VEH_restraintStatus` | page 117 | USM ECU: a117 VEH restraint status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a117_VEH_lightStatus` | page 117 | USM ECU: a117 VEH light status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a117_VEH_seatStatus` | page 117 | USM ECU: a117 VEH seat status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a117_BDY_falconSwitchStatus` | page 117 | USM ECU: a117 BDY falcon switch status | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a117_VEH_doorStatus` | page 117 | USM ECU: a117 VEH door status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a117_VEH_doorStatus2` | page 117 | USM ECU: a117 VEH door status2 | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a117_VEH_windowStatus` | page 117 | USM ECU: a117 VEH window status | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a117_VEH_switchStatus` | page 117 | USM ECU: a117 VEH switch status | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a117_VEH_intrusionSensorStatus` | page 117 | USM ECU: a117 VEH intrusion sensor status | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a117_VEH_liftgateStatus` | page 117 | USM ECU: a117 VEH liftgate status | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a117_VEH_seatStatus2` | page 117 | USM ECU: a117 VEH seat status2 | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a117_PARTY_restraintStatus` | page 117 | USM ECU: a117 PARTY restraint status | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a117_VEH_thermalStatus` | page 117 | USM ECU: a117 VEH thermal status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a117_PARTY_doorStatus` | page 117 | USM ECU: a117 PARTY door status | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a117_VEH_status` | page 117 | USM ECU: a117 VEH status | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a117_PARTY_prndStatus` | page 117 | USM ECU: a117 PARTY prnd status | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_VEH_vehNm` | page 118 | USM ECU: a118 VEH veh nm | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_VEH_lighting` | page 118 | USM ECU: a118 VEH lighting | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_VEH_sensors` | page 118 | USM ECU: a118 VEH sensors | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_VEH_status` | page 118 | USM ECU: a118 VEH status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_VEH_okToUseHighPwr` | page 118 | USM ECU: a118 VEH ok to use high pwr | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_VEH_LVPowerState` | page 118 | USM ECU: a118 VEH LV power state | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_VEH_coolant` | page 118 | USM ECU: a118 VEH coolant | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_VEH_vehicleStatus` | page 118 | USM ECU: a118 VEH vehicle status | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_VEH_12VBatteryStatus` | page 118 | USM ECU: a118 VEH 12 v battery status | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_VEH_systemStatus` | page 118 | USM ECU: a118 VEH system status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_PARTY_LVPowerState` | page 118 | USM ECU: a118 PARTY LV power state | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_PARTY_outputPowerStatus` | page 118 | USM ECU: a118 PARTY output power status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_PARTY_vehicleTime` | page 118 | USM ECU: a118 PARTY vehicle time | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_VEH_thermalCommand` | page 118 | USM ECU: a118 VEH thermal command | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_CH_LVPowerState` | page 118 | USM ECU: a118 CH LV power state | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_PARTY_sensors` | page 118 | USM ECU: a118 PARTY sensors | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_CH_sensors` | page 118 | USM ECU: a118 CH sensors | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_VEH_interNodeResistance` | page 118 | USM ECU: a118 VEH inter node resistance | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_CH_lighting` | page 118 | USM ECU: a118 CH lighting | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_VEH_lightStatus` | page 118 | USM ECU: a118 VEH light status | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_PARTY_vehNm` | page 118 | USM ECU: a118 PARTY veh nm | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_CH_12VBatteryStatus` | page 118 | USM ECU: a118 CH 12 v battery status | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_CH_LVBMS_statusHigh` | page 118 | USM ECU: a118 CH LVBMS status high | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_CH_alertMatrix` | page 118 | USM ECU: a118 CH alert matrix | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_BDY_outputPowerStatus` | page 118 | USM ECU: a118 BDY output power status | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_BDY_vehicleTime` | page 118 | USM ECU: a118 BDY vehicle time | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_PARTY_AP_vehicleState1HzMuxed` | page 118 | USM ECU: a118 PARTY AP vehicle state1 hz muxed | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a118_BDY_AP_vehicleState1HzMuxed` | page 118 | USM ECU: a118 BDY AP vehicle state1 hz muxed | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a119_VEH_steerAngle` | page 119 | USM ECU: a119 VEH steer angle | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a119_VEH_leftStalk` | page 119 | USM ECU: a119 VEH left stalk | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a119_VEH_rightStalk` | page 119 | USM ECU: a119 VEH right stalk | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a119_PARTY_rightStalk` | page 119 | USM ECU: a119 PARTY right stalk | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a119_CH_steerAngle` | page 119 | USM ECU: a119 CH steer angle | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a119_PARTY_steerAngle` | page 119 | USM ECU: a119 PARTY steer angle | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_PARTY_chassisCntl` | page 120 | USM ECU: a120 PARTY chassis cntl | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_VEH_systemStatus` | page 120 | USM ECU: a120 VEH system status | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_CH_chassisCntl` | page 120 | USM ECU: a120 CH chassis cntl | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_PARTY_systemStatus` | page 120 | USM ECU: a120 PARTY system status | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_PARTY_torque` | page 120 | USM ECU: a120 PARTY torque | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_VEH_torque` | page 120 | USM ECU: a120 VEH torque | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_PARTY_locStatus` | page 120 | USM ECU: a120 PARTY loc status | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_PARTY_speed` | page 120 | USM ECU: a120 PARTY speed | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_VEH_speed` | page 120 | USM ECU: a120 VEH speed | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_PARTY_status` | page 120 | USM ECU: a120 PARTY status | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_PT_speed` | page 120 | USM ECU: a120 PT speed | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_PT_systemStatus` | page 120 | USM ECU: a120 PT system status | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_PARTY_vehicleEstimates` | page 120 | USM ECU: a120 PARTY vehicle estimates | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_VEH_aggregatedAxleSpeed` | page 120 | USM ECU: a120 VEH aggregated axle speed | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_PARTY_aggregatedAxleSpeed` | page 120 | USM ECU: a120 PARTY aggregated axle speed | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_VEH_systemPower` | page 120 | USM ECU: a120 VEH system power | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_PT_systemPower` | page 120 | USM ECU: a120 PT system power | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_PARTY_stalklessInterfaces` | page 120 | USM ECU: a120 PARTY stalkless interfaces | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_CH_speed` | page 120 | USM ECU: a120 CH speed | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_VEH_estimatedBrakeTemp` | page 120 | USM ECU: a120 VEH estimated brake temp | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_PARTY_prndControl` | page 120 | USM ECU: a120 PARTY prnd control | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_PARTY_locStatus2` | page 120 | USM ECU: a120 PARTY loc status2 | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_VEH_chassisCntl` | page 120 | USM ECU: a120 VEH chassis cntl | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_VEH_locStatus` | page 120 | USM ECU: a120 VEH loc status | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_VEH_locStatus2` | page 120 | USM ECU: a120 VEH loc status2 | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_VEH_prndControl` | page 120 | USM ECU: a120 VEH prnd control | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a120_VEH_vehicleEstimates` | page 120 | USM ECU: a120 VEH vehicle estimates | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a131_inDrivePowerState` | page 131 | USM ECU: a131 in drive power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a131_timeSinceInit` | page 131 | USM ECU: a131 time since init | 24\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a131_timeSincePwrStateTransition` | page 131 | USM ECU: a131 time since pwr state transition | 40\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a131_numComErrSinceInit` | page 131 | USM ECU: a131 num com err since init | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a132_inDrivePowerState` | page 132 | USM ECU: a132 in drive power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a132_timeSinceInit` | page 132 | USM ECU: a132 time since init | 24\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a132_timeSincePwrStateTransition` | page 132 | USM ECU: a132 time since pwr state transition | 40\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a132_numComErrSinceInit` | page 132 | USM ECU: a132 num com err since init | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a133_inDrivePowerState` | page 133 | USM ECU: a133 in drive power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a133_timeSinceInit` | page 133 | USM ECU: a133 time since init | 24\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a133_timeSincePwrStateTransition` | page 133 | USM ECU: a133 time since pwr state transition | 40\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a133_numComErrSinceInit` | page 133 | USM ECU: a133 num com err since init | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a134_inDrivePowerState` | page 134 | USM ECU: a134 in drive power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a134_timeSinceInit` | page 134 | USM ECU: a134 time since init | 24\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a134_timeSincePwrStateTransition` | page 134 | USM ECU: a134 time since pwr state transition | 40\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a134_numComErrSinceInit` | page 134 | USM ECU: a134 num com err since init | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a135_inDrivePowerState` | page 135 | USM ECU: a135 in drive power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a135_timeSinceInit` | page 135 | USM ECU: a135 time since init | 24\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a135_timeSincePwrStateTransition` | page 135 | USM ECU: a135 time since pwr state transition | 40\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a135_numComErrSinceInit` | page 135 | USM ECU: a135 num com err since init | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a136_inDrivePowerState` | page 136 | USM ECU: a136 in drive power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a136_timeSinceInit` | page 136 | USM ECU: a136 time since init | 24\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a136_timeSincePwrStateTransition` | page 136 | USM ECU: a136 time since pwr state transition | 40\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a136_numComErrSinceInit` | page 136 | USM ECU: a136 num com err since init | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a137_inDrivePowerState` | page 137 | USM ECU: a137 in drive power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a137_timeSinceInit` | page 137 | USM ECU: a137 time since init | 24\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a137_timeSincePwrStateTransition` | page 137 | USM ECU: a137 time since pwr state transition | 40\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a137_numComErrSinceInit` | page 137 | USM ECU: a137 num com err since init | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a138_inDrivePowerState` | page 138 | USM ECU: a138 in drive power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a138_timeSinceInit` | page 138 | USM ECU: a138 time since init | 24\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a138_timeSincePwrStateTransition` | page 138 | USM ECU: a138 time since pwr state transition | 40\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a138_numComErrSinceInit` | page 138 | USM ECU: a138 num com err since init | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a139_inDrivePowerState` | page 139 | USM ECU: a139 in drive power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a139_timeSinceInit` | page 139 | USM ECU: a139 time since init | 24\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a139_timeSincePwrStateTransition` | page 139 | USM ECU: a139 time since pwr state transition | 40\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a139_numComErrSinceInit` | page 139 | USM ECU: a139 num com err since init | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a140_inDrivePowerState` | page 140 | USM ECU: a140 in drive power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a140_timeSinceInit` | page 140 | USM ECU: a140 time since init | 24\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a140_timeSincePwrStateTransition` | page 140 | USM ECU: a140 time since pwr state transition | 40\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a140_numComErrSinceInit` | page 140 | USM ECU: a140 num com err since init | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a141_inDrivePowerState` | page 141 | USM ECU: a141 in drive power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a141_timeSinceInit` | page 141 | USM ECU: a141 time since init | 24\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a141_timeSincePwrStateTransition` | page 141 | USM ECU: a141 time since pwr state transition | 40\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a141_numComErrSinceInit` | page 141 | USM ECU: a141 num com err since init | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a142_inDrivePowerState` | page 142 | USM ECU: a142 in drive power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a142_timeSinceInit` | page 142 | USM ECU: a142 time since init | 24\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a142_timeSincePwrStateTransition` | page 142 | USM ECU: a142 time since pwr state transition | 40\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a142_numComErrSinceInit` | page 142 | USM ECU: a142 num com err since init | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a143_inDrivePowerState` | page 143 | USM ECU: a143 in drive power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a143_timeSinceInit` | page 143 | USM ECU: a143 time since init | 24\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a143_timeSincePwrStateTransition` | page 143 | USM ECU: a143 time since pwr state transition | 40\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a143_numHwErrSinceInit` | page 143 | USM ECU: a143 num hw err since init | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a144_inDrivePowerState` | page 144 | USM ECU: a144 in drive power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a144_timeSinceInit` | page 144 | USM ECU: a144 time since init | 24\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a144_timeSincePwrStateTransition` | page 144 | USM ECU: a144 time since pwr state transition | 40\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a144_numHwErrSinceInit` | page 144 | USM ECU: a144 num hw err since init | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a145_inDrivePowerState` | page 145 | USM ECU: a145 in drive power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a145_timeSinceInit` | page 145 | USM ECU: a145 time since init | 24\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a145_timeSincePwrStateTransition` | page 145 | USM ECU: a145 time since pwr state transition | 40\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a145_numHwErrSinceInit` | page 145 | USM ECU: a145 num hw err since init | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a146_inDrivePowerState` | page 146 | USM ECU: a146 in drive power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a146_timeSinceInit` | page 146 | USM ECU: a146 time since init | 24\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a146_timeSincePwrStateTransition` | page 146 | USM ECU: a146 time since pwr state transition | 40\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a146_numHwErrSinceInit` | page 146 | USM ECU: a146 num hw err since init | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a147_inDrivePowerState` | page 147 | USM ECU: a147 in drive power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a147_timeSinceInit` | page 147 | USM ECU: a147 time since init | 24\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a147_timeSincePwrStateTransition` | page 147 | USM ECU: a147 time since pwr state transition | 40\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a147_numHwErrSinceInit` | page 147 | USM ECU: a147 num hw err since init | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a148_inDrivePowerState` | page 148 | USM ECU: a148 in drive power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a148_timeSinceInit` | page 148 | USM ECU: a148 time since init | 24\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a148_timeSincePwrStateTransition` | page 148 | USM ECU: a148 time since pwr state transition | 40\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a148_numHwErrSinceInit` | page 148 | USM ECU: a148 num hw err since init | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a149_inDrivePowerState` | page 149 | USM ECU: a149 in drive power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a149_timeSinceInit` | page 149 | USM ECU: a149 time since init | 24\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a149_timeSincePwrStateTransition` | page 149 | USM ECU: a149 time since pwr state transition | 40\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a149_numHwErrSinceInit` | page 149 | USM ECU: a149 num hw err since init | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a150_inDrivePowerState` | page 150 | USM ECU: a150 in drive power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a150_timeSinceInit` | page 150 | USM ECU: a150 time since init | 24\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a150_timeSincePwrStateTransition` | page 150 | USM ECU: a150 time since pwr state transition | 40\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a150_numHwErrSinceInit` | page 150 | USM ECU: a150 num hw err since init | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a151_inDrivePowerState` | page 151 | USM ECU: a151 in drive power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a151_timeSinceInit` | page 151 | USM ECU: a151 time since init | 24\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a151_timeSincePwrStateTransition` | page 151 | USM ECU: a151 time since pwr state transition | 40\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a151_numHwErrSinceInit` | page 151 | USM ECU: a151 num hw err since init | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a152_inDrivePowerState` | page 152 | USM ECU: a152 in drive power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a152_timeSinceInit` | page 152 | USM ECU: a152 time since init | 24\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a152_timeSincePwrStateTransition` | page 152 | USM ECU: a152 time since pwr state transition | 40\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a152_numHwErrSinceInit` | page 152 | USM ECU: a152 num hw err since init | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a153_inDrivePowerState` | page 153 | USM ECU: a153 in drive power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a153_timeSinceInit` | page 153 | USM ECU: a153 time since init | 24\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a153_timeSincePwrStateTransition` | page 153 | USM ECU: a153 time since pwr state transition | 40\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a153_numHwErrSinceInit` | page 153 | USM ECU: a153 num hw err since init | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a154_inDrivePowerState` | page 154 | USM ECU: a154 in drive power state | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a154_timeSinceInit` | page 154 | USM ECU: a154 time since init | 24\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a154_timeSincePwrStateTransition` | page 154 | USM ECU: a154 time since pwr state transition | 40\|16 | little-endian | unsigned | 1 | 0 | secs | 0 to 65535 |  | plausible |
| `USM_a154_numHwErrSinceInit` | page 154 | USM ECU: a154 num hw err since init | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `USM_a155_temperature` | page 155 | USM ECU: a155 temperature | 16\|8 | little-endian | signed | 1 | 33 | degC | -95 to 160 |  | plausible |
| `USM_a156_temperature` | page 156 | USM ECU: a156 temperature | 16\|8 | little-endian | signed | 1 | 33 | degC | -95 to 160 |  | plausible |
| `USM_a157_temperature` | page 157 | USM ECU: a157 temperature | 16\|8 | little-endian | signed | 1 | 33 | degC | -95 to 160 |  | plausible |
| `USM_a158_temperature` | page 158 | USM ECU: a158 temperature | 16\|8 | little-endian | signed | 1 | 33 | degC | -95 to 160 |  | plausible |
| `USM_a159_temperature` | page 159 | USM ECU: a159 temperature | 16\|8 | little-endian | signed | 1 | 33 | degC | -95 to 160 |  | plausible |
| `USM_a160_temperature` | page 160 | USM ECU: a160 temperature | 16\|8 | little-endian | signed | 1 | 33 | degC | -95 to 160 |  | plausible |
| `USM_a161_temperature` | page 161 | USM ECU: a161 temperature | 16\|8 | little-endian | signed | 1 | 33 | degC | -95 to 160 |  | plausible |
| `USM_a162_temperature` | page 162 | USM ECU: a162 temperature | 16\|8 | little-endian | signed | 1 | 33 | degC | -95 to 160 |  | plausible |
| `USM_a163_temperature` | page 163 | USM ECU: a163 temperature | 16\|8 | little-endian | signed | 1 | 33 | degC | -95 to 160 |  | plausible |
| `USM_a164_temperature` | page 164 | USM ECU: a164 temperature | 16\|8 | little-endian | signed | 1 | 33 | degC | -95 to 160 |  | plausible |
| `USM_a165_temperature` | page 165 | USM ECU: a165 temperature | 16\|8 | little-endian | signed | 1 | 33 | degC | -95 to 160 |  | plausible |
| `USM_a166_temperature` | page 166 | USM ECU: a166 temperature | 16\|8 | little-endian | signed | 1 | 33 | degC | -95 to 160 |  | plausible |
| `USM_a177_rtmCompensated` | page 177 | USM ECU: a177 rtm compensated | 16\|8 | little-endian | unsigned | 8 | 0 | us | 0 to 2040 |  | plausible |
| `USM_a177_rtmOffset` | page 177 | USM ECU: a177 rtm offset | 24\|8 | little-endian | signed | 2 | 0 | us | -256 to 254 |  | plausible |
| `USM_a177_rtmOffsetFromInit` | page 177 | USM ECU: a177 rtm offset from init | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a177_ambientTemperature` | page 177 | USM ECU: a177 ambient temperature; raw 0 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `USM_a177_sensorTemperature` | page 177 | USM ECU: a177 sensor temperature | 48\|8 | little-endian | signed | 1 | 33 | degC | -95 to 160 |  | plausible |
| `USM_a178_rtmCompensated` | page 178 | USM ECU: a178 rtm compensated | 16\|8 | little-endian | unsigned | 8 | 0 | us | 0 to 2040 |  | plausible |
| `USM_a178_rtmOffset` | page 178 | USM ECU: a178 rtm offset | 24\|8 | little-endian | signed | 2 | 0 | us | -256 to 254 |  | plausible |
| `USM_a178_rtmOffsetFromInit` | page 178 | USM ECU: a178 rtm offset from init | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a178_ambientTemperature` | page 178 | USM ECU: a178 ambient temperature; raw 0 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `USM_a178_sensorTemperature` | page 178 | USM ECU: a178 sensor temperature | 48\|8 | little-endian | signed | 1 | 33 | degC | -95 to 160 |  | plausible |
| `USM_a179_rtmCompensated` | page 179 | USM ECU: a179 rtm compensated | 16\|8 | little-endian | unsigned | 8 | 0 | us | 0 to 2040 |  | plausible |
| `USM_a179_rtmOffset` | page 179 | USM ECU: a179 rtm offset | 24\|8 | little-endian | signed | 2 | 0 | us | -256 to 254 |  | plausible |
| `USM_a179_rtmOffsetFromInit` | page 179 | USM ECU: a179 rtm offset from init | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a179_ambientTemperature` | page 179 | USM ECU: a179 ambient temperature; raw 0 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `USM_a179_sensorTemperature` | page 179 | USM ECU: a179 sensor temperature | 48\|8 | little-endian | signed | 1 | 33 | degC | -95 to 160 |  | plausible |
| `USM_a180_rtmCompensated` | page 180 | USM ECU: a180 rtm compensated | 16\|8 | little-endian | unsigned | 8 | 0 | us | 0 to 2040 |  | plausible |
| `USM_a180_rtmOffset` | page 180 | USM ECU: a180 rtm offset | 24\|8 | little-endian | signed | 2 | 0 | us | -256 to 254 |  | plausible |
| `USM_a180_rtmOffsetFromInit` | page 180 | USM ECU: a180 rtm offset from init | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a180_ambientTemperature` | page 180 | USM ECU: a180 ambient temperature; raw 0 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `USM_a180_sensorTemperature` | page 180 | USM ECU: a180 sensor temperature | 48\|8 | little-endian | signed | 1 | 33 | degC | -95 to 160 |  | plausible |
| `USM_a181_rtmCompensated` | page 181 | USM ECU: a181 rtm compensated | 16\|8 | little-endian | unsigned | 8 | 0 | us | 0 to 2040 |  | plausible |
| `USM_a181_rtmOffset` | page 181 | USM ECU: a181 rtm offset | 24\|8 | little-endian | signed | 2 | 0 | us | -256 to 254 |  | plausible |
| `USM_a181_rtmOffsetFromInit` | page 181 | USM ECU: a181 rtm offset from init | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a181_ambientTemperature` | page 181 | USM ECU: a181 ambient temperature; raw 0 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `USM_a181_sensorTemperature` | page 181 | USM ECU: a181 sensor temperature | 48\|8 | little-endian | signed | 1 | 33 | degC | -95 to 160 |  | plausible |
| `USM_a182_rtmCompensated` | page 182 | USM ECU: a182 rtm compensated | 16\|8 | little-endian | unsigned | 8 | 0 | us | 0 to 2040 |  | plausible |
| `USM_a182_rtmOffset` | page 182 | USM ECU: a182 rtm offset | 24\|8 | little-endian | signed | 2 | 0 | us | -256 to 254 |  | plausible |
| `USM_a182_rtmOffsetFromInit` | page 182 | USM ECU: a182 rtm offset from init | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a182_ambientTemperature` | page 182 | USM ECU: a182 ambient temperature; raw 0 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `USM_a182_sensorTemperature` | page 182 | USM ECU: a182 sensor temperature | 48\|8 | little-endian | signed | 1 | 33 | degC | -95 to 160 |  | plausible |
| `USM_a183_rtmCompensated` | page 183 | USM ECU: a183 rtm compensated | 16\|8 | little-endian | unsigned | 8 | 0 | us | 0 to 2040 |  | plausible |
| `USM_a183_rtmOffset` | page 183 | USM ECU: a183 rtm offset | 24\|8 | little-endian | signed | 2 | 0 | us | -256 to 254 |  | plausible |
| `USM_a183_rtmOffsetFromInit` | page 183 | USM ECU: a183 rtm offset from init | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a183_ambientTemperature` | page 183 | USM ECU: a183 ambient temperature; raw 0 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `USM_a183_sensorTemperature` | page 183 | USM ECU: a183 sensor temperature | 48\|8 | little-endian | signed | 1 | 33 | degC | -95 to 160 |  | plausible |
| `USM_a184_rtmCompensated` | page 184 | USM ECU: a184 rtm compensated | 16\|8 | little-endian | unsigned | 8 | 0 | us | 0 to 2040 |  | plausible |
| `USM_a184_rtmOffset` | page 184 | USM ECU: a184 rtm offset | 24\|8 | little-endian | signed | 2 | 0 | us | -256 to 254 |  | plausible |
| `USM_a184_rtmOffsetFromInit` | page 184 | USM ECU: a184 rtm offset from init | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a184_ambientTemperature` | page 184 | USM ECU: a184 ambient temperature; raw 0 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `USM_a184_sensorTemperature` | page 184 | USM ECU: a184 sensor temperature | 48\|8 | little-endian | signed | 1 | 33 | degC | -95 to 160 |  | plausible |
| `USM_a185_rtmCompensated` | page 185 | USM ECU: a185 rtm compensated | 16\|8 | little-endian | unsigned | 8 | 0 | us | 0 to 2040 |  | plausible |
| `USM_a185_rtmOffset` | page 185 | USM ECU: a185 rtm offset | 24\|8 | little-endian | signed | 2 | 0 | us | -256 to 254 |  | plausible |
| `USM_a185_rtmOffsetFromInit` | page 185 | USM ECU: a185 rtm offset from init | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a185_ambientTemperature` | page 185 | USM ECU: a185 ambient temperature; raw 0 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `USM_a185_sensorTemperature` | page 185 | USM ECU: a185 sensor temperature | 48\|8 | little-endian | signed | 1 | 33 | degC | -95 to 160 |  | plausible |
| `USM_a186_rtmCompensated` | page 186 | USM ECU: a186 rtm compensated | 16\|8 | little-endian | unsigned | 8 | 0 | us | 0 to 2040 |  | plausible |
| `USM_a186_rtmOffset` | page 186 | USM ECU: a186 rtm offset | 24\|8 | little-endian | signed | 2 | 0 | us | -256 to 254 |  | plausible |
| `USM_a186_rtmOffsetFromInit` | page 186 | USM ECU: a186 rtm offset from init | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a186_ambientTemperature` | page 186 | USM ECU: a186 ambient temperature; raw 0 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `USM_a186_sensorTemperature` | page 186 | USM ECU: a186 sensor temperature | 48\|8 | little-endian | signed | 1 | 33 | degC | -95 to 160 |  | plausible |
| `USM_a187_rtmCompensated` | page 187 | USM ECU: a187 rtm compensated | 16\|8 | little-endian | unsigned | 8 | 0 | us | 0 to 2040 |  | plausible |
| `USM_a187_rtmOffset` | page 187 | USM ECU: a187 rtm offset | 24\|8 | little-endian | signed | 2 | 0 | us | -256 to 254 |  | plausible |
| `USM_a187_rtmOffsetFromInit` | page 187 | USM ECU: a187 rtm offset from init | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a187_ambientTemperature` | page 187 | USM ECU: a187 ambient temperature; raw 0 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `USM_a187_sensorTemperature` | page 187 | USM ECU: a187 sensor temperature | 48\|8 | little-endian | signed | 1 | 33 | degC | -95 to 160 |  | plausible |
| `USM_a188_rtmCompensated` | page 188 | USM ECU: a188 rtm compensated | 16\|8 | little-endian | unsigned | 8 | 0 | us | 0 to 2040 |  | plausible |
| `USM_a188_rtmOffset` | page 188 | USM ECU: a188 rtm offset | 24\|8 | little-endian | signed | 2 | 0 | us | -256 to 254 |  | plausible |
| `USM_a188_rtmOffsetFromInit` | page 188 | USM ECU: a188 rtm offset from init | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a188_ambientTemperature` | page 188 | USM ECU: a188 ambient temperature; raw 0 = signal not available (SNA) | 40\|8 | little-endian | unsigned | 0.5 | -40 | degC | -39.5 to 87.5 | 0 = `SNA` | plausible |
| `USM_a188_sensorTemperature` | page 188 | USM ECU: a188 sensor temperature | 48\|8 | little-endian | signed | 1 | 33 | degC | -95 to 160 |  | plausible |
| `USM_a201_channel` | page 201 | USM ECU: a201 channel | 16\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 |  | layout-only |
| `USM_a201_OT` | page 201 | USM ECU: a201 OT | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a201_VCCUV_RFCB` | page 201 | USM ECU: a201 VCCUV RFCB | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a201_CLKREF_ERROR` | page 201 | USM ECU: a201 CLKREF ERROR | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a201_CMD_INC` | page 201 | USM ECU: a201 CMD INC | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a201_CRC_ERROR` | page 201 | USM ECU: a201 CRC ERROR | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a201_UND_CMD` | page 201 | USM ECU: a201 UND CMD | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a201_DSI1_CMD_OVR` | page 201 | USM ECU: a201 DSI1 CMD OVR | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a201_DSI2_CMD_OVR` | page 201 | USM ECU: a201 DSI2 CMD OVR | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a201_DSI1_UV` | page 201 | USM ECU: a201 DSI1 UV | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a201_DSI2_UV` | page 201 | USM ECU: a201 DSI2 UV | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a201_DSI1_ND` | page 201 | USM ECU: a201 DSI1 ND | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a201_DSI2_ND` | page 201 | USM ECU: a201 DSI2 ND | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a201_DSI1_OR` | page 201 | USM ECU: a201 DSI1 OR | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a201_DSI2_OR` | page 201 | USM ECU: a201 DSI2 OR | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a201_DSI1_DL` | page 201 | USM ECU: a201 DSI1 DL | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a201_DSI2_DL` | page 201 | USM ECU: a201 DSI2 DL | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a201_DSI1_PC` | page 201 | USM ECU: a201 DSI1 PC | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a201_DSI2_PC` | page 201 | USM ECU: a201 DSI2 PC | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a202_channel` | page 202 | USM ECU: a202 channel | 16\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `USM_a202_EE` | page 202 | USM ECU: a202 EE | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a202_LE` | page 202 | USM ECU: a202 LE | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a202_SC` | page 202 | USM ECU: a202 SC | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a202_CR` | page 202 | USM ECU: a202 CR | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a202_SP` | page 202 | USM ECU: a202 SP | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a202_SE` | page 202 | USM ECU: a202 SE | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a202_UV` | page 202 | USM ECU: a202 UV | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a202_CE` | page 202 | USM ECU: a202 CE | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_reset` | page 227 | USM ECU: a227 reset | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_otpCrcError` | page 227 | USM ECU: a227 otp crc error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_trimRegParityErr` | page 227 | USM ECU: a227 trim reg parity err | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_sramParityErr` | page 227 | USM ECU: a227 sram parity err | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_crcMismatchInOtp` | page 227 | USM ECU: a227 crc mismatch in otp | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_crcMismatchInSysrom` | page 227 | USM ECU: a227 crc mismatch in sysrom | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_crcMismatchInEeprom` | page 227 | USM ECU: a227 crc mismatch in eeprom | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_capLossVdddOutOfRange` | page 227 | USM ECU: a227 cap loss vddd out of range | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_capLossVddaOutOfRange` | page 227 | USM ECU: a227 cap loss vdda out of range | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_referenceVoltOutOfRange` | page 227 | USM ECU: a227 reference volt out of range | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_vdddVoltOutOfRange` | page 227 | USM ECU: a227 vddd volt out of range | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_vrefVoldOfOtpOutOfRange` | page 227 | USM ECU: a227 vref vold of otp out of range | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_eepromProgFail` | page 227 | USM ECU: a227 eeprom prog fail | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_eepromProgBuys` | page 227 | USM ECU: a227 eeprom prog buys | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_vsupVoltOutOfRange` | page 227 | USM ECU: a227 vsup volt out of range | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_tempSensOutOfRange` | page 227 | USM ECU: a227 temp sens out of range | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_underVoltAtVtankDuringBurst` | page 227 | USM ECU: a227 under volt at vtank during burst | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_overVoltAtVtankDuringBurst` | page 227 | USM ECU: a227 over volt at vtank during burst | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_drvsFailDuringBurst` | page 227 | USM ECU: a227 drvs fail during burst | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_drv1FailDuringBurst` | page 227 | USM ECU: a227 drv1 fail during burst | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_drv2FailDuringBurst` | page 227 | USM ECU: a227 drv2 fail during burst | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_crcMismatchInRam` | page 227 | USM ECU: a227 crc mismatch in ram | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_verificationOfConfigAndCalcParamsFail` | page 227 | USM ECU: a227 verification of config and calc params fail | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_wdgClockFreqOutOfRange` | page 227 | USM ECU: a227 wdg clock freq out of range | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_atgNoiseMeasOutOfRange` | page 227 | USM ECU: a227 atg noise meas out of range | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_syncCountError` | page 227 | USM ECU: a227 sync count error | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_invalidStartEdge` | page 227 | USM ECU: a227 invalid start edge | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_receiverReachedErrorState` | page 227 | USM ECU: a227 receiver reached error state | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_pdcmPulseInvalid` | page 227 | USM ECU: a227 pdcm pulse invalid | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_crcOfReceivedCmdInvalid` | page 227 | USM ECU: a227 crc of received cmd invalid | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_passwordWrong` | page 227 | USM ECU: a227 password wrong | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_timeIntBetween2PulsesErr` | page 227 | USM ECU: a227 time int between2 pulses err | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a227_numInvalidStartEdgeSinceInit` | page 227 | USM ECU: a227 num invalid start edge since init | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `USM_a227_numAtgNoiseErrorsSinceInit` | page 227 | USM ECU: a227 num atg noise errors since init | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `USM_a228_reset` | page 228 | USM ECU: a228 reset | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_otpCrcError` | page 228 | USM ECU: a228 otp crc error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_trimRegParityErr` | page 228 | USM ECU: a228 trim reg parity err | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_sramParityErr` | page 228 | USM ECU: a228 sram parity err | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_crcMismatchInOtp` | page 228 | USM ECU: a228 crc mismatch in otp | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_crcMismatchInSysrom` | page 228 | USM ECU: a228 crc mismatch in sysrom | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_crcMismatchInEeprom` | page 228 | USM ECU: a228 crc mismatch in eeprom | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_capLossVdddOutOfRange` | page 228 | USM ECU: a228 cap loss vddd out of range | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_capLossVddaOutOfRange` | page 228 | USM ECU: a228 cap loss vdda out of range | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_referenceVoltOutOfRange` | page 228 | USM ECU: a228 reference volt out of range | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_vdddVoltOutOfRange` | page 228 | USM ECU: a228 vddd volt out of range | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_vrefVoldOfOtpOutOfRange` | page 228 | USM ECU: a228 vref vold of otp out of range | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_eepromProgFail` | page 228 | USM ECU: a228 eeprom prog fail | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_eepromProgBuys` | page 228 | USM ECU: a228 eeprom prog buys | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_vsupVoltOutOfRange` | page 228 | USM ECU: a228 vsup volt out of range | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_tempSensOutOfRange` | page 228 | USM ECU: a228 temp sens out of range | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_underVoltAtVtankDuringBurst` | page 228 | USM ECU: a228 under volt at vtank during burst | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_overVoltAtVtankDuringBurst` | page 228 | USM ECU: a228 over volt at vtank during burst | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_drvsFailDuringBurst` | page 228 | USM ECU: a228 drvs fail during burst | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_drv1FailDuringBurst` | page 228 | USM ECU: a228 drv1 fail during burst | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_drv2FailDuringBurst` | page 228 | USM ECU: a228 drv2 fail during burst | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_crcMismatchInRam` | page 228 | USM ECU: a228 crc mismatch in ram | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_verificationOfConfigAndCalcParamsFail` | page 228 | USM ECU: a228 verification of config and calc params fail | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_wdgClockFreqOutOfRange` | page 228 | USM ECU: a228 wdg clock freq out of range | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_atgNoiseMeasOutOfRange` | page 228 | USM ECU: a228 atg noise meas out of range | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_syncCountError` | page 228 | USM ECU: a228 sync count error | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_invalidStartEdge` | page 228 | USM ECU: a228 invalid start edge | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_receiverReachedErrorState` | page 228 | USM ECU: a228 receiver reached error state | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_pdcmPulseInvalid` | page 228 | USM ECU: a228 pdcm pulse invalid | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_crcOfReceivedCmdInvalid` | page 228 | USM ECU: a228 crc of received cmd invalid | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_passwordWrong` | page 228 | USM ECU: a228 password wrong | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_timeIntBetween2PulsesErr` | page 228 | USM ECU: a228 time int between2 pulses err | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a228_numInvalidStartEdgeSinceInit` | page 228 | USM ECU: a228 num invalid start edge since init | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `USM_a228_numAtgNoiseErrorsSinceInit` | page 228 | USM ECU: a228 num atg noise errors since init | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `USM_a229_reset` | page 229 | USM ECU: a229 reset | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_otpCrcError` | page 229 | USM ECU: a229 otp crc error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_trimRegParityErr` | page 229 | USM ECU: a229 trim reg parity err | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_sramParityErr` | page 229 | USM ECU: a229 sram parity err | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_crcMismatchInOtp` | page 229 | USM ECU: a229 crc mismatch in otp | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_crcMismatchInSysrom` | page 229 | USM ECU: a229 crc mismatch in sysrom | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_crcMismatchInEeprom` | page 229 | USM ECU: a229 crc mismatch in eeprom | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_capLossVdddOutOfRange` | page 229 | USM ECU: a229 cap loss vddd out of range | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_capLossVddaOutOfRange` | page 229 | USM ECU: a229 cap loss vdda out of range | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_referenceVoltOutOfRange` | page 229 | USM ECU: a229 reference volt out of range | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_vdddVoltOutOfRange` | page 229 | USM ECU: a229 vddd volt out of range | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_vrefVoldOfOtpOutOfRange` | page 229 | USM ECU: a229 vref vold of otp out of range | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_eepromProgFail` | page 229 | USM ECU: a229 eeprom prog fail | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_eepromProgBuys` | page 229 | USM ECU: a229 eeprom prog buys | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_vsupVoltOutOfRange` | page 229 | USM ECU: a229 vsup volt out of range | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_tempSensOutOfRange` | page 229 | USM ECU: a229 temp sens out of range | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_underVoltAtVtankDuringBurst` | page 229 | USM ECU: a229 under volt at vtank during burst | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_overVoltAtVtankDuringBurst` | page 229 | USM ECU: a229 over volt at vtank during burst | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_drvsFailDuringBurst` | page 229 | USM ECU: a229 drvs fail during burst | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_drv1FailDuringBurst` | page 229 | USM ECU: a229 drv1 fail during burst | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_drv2FailDuringBurst` | page 229 | USM ECU: a229 drv2 fail during burst | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_crcMismatchInRam` | page 229 | USM ECU: a229 crc mismatch in ram | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_verificationOfConfigAndCalcParamsFail` | page 229 | USM ECU: a229 verification of config and calc params fail | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_wdgClockFreqOutOfRange` | page 229 | USM ECU: a229 wdg clock freq out of range | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_atgNoiseMeasOutOfRange` | page 229 | USM ECU: a229 atg noise meas out of range | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_syncCountError` | page 229 | USM ECU: a229 sync count error | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_invalidStartEdge` | page 229 | USM ECU: a229 invalid start edge | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_receiverReachedErrorState` | page 229 | USM ECU: a229 receiver reached error state | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_pdcmPulseInvalid` | page 229 | USM ECU: a229 pdcm pulse invalid | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_crcOfReceivedCmdInvalid` | page 229 | USM ECU: a229 crc of received cmd invalid | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_passwordWrong` | page 229 | USM ECU: a229 password wrong | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_timeIntBetween2PulsesErr` | page 229 | USM ECU: a229 time int between2 pulses err | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a229_numInvalidStartEdgeSinceInit` | page 229 | USM ECU: a229 num invalid start edge since init | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `USM_a229_numAtgNoiseErrorsSinceInit` | page 229 | USM ECU: a229 num atg noise errors since init | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `USM_a230_reset` | page 230 | USM ECU: a230 reset | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_otpCrcError` | page 230 | USM ECU: a230 otp crc error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_trimRegParityErr` | page 230 | USM ECU: a230 trim reg parity err | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_sramParityErr` | page 230 | USM ECU: a230 sram parity err | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_crcMismatchInOtp` | page 230 | USM ECU: a230 crc mismatch in otp | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_crcMismatchInSysrom` | page 230 | USM ECU: a230 crc mismatch in sysrom | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_crcMismatchInEeprom` | page 230 | USM ECU: a230 crc mismatch in eeprom | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_capLossVdddOutOfRange` | page 230 | USM ECU: a230 cap loss vddd out of range | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_capLossVddaOutOfRange` | page 230 | USM ECU: a230 cap loss vdda out of range | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_referenceVoltOutOfRange` | page 230 | USM ECU: a230 reference volt out of range | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_vdddVoltOutOfRange` | page 230 | USM ECU: a230 vddd volt out of range | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_vrefVoldOfOtpOutOfRange` | page 230 | USM ECU: a230 vref vold of otp out of range | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_eepromProgFail` | page 230 | USM ECU: a230 eeprom prog fail | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_eepromProgBuys` | page 230 | USM ECU: a230 eeprom prog buys | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_vsupVoltOutOfRange` | page 230 | USM ECU: a230 vsup volt out of range | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_tempSensOutOfRange` | page 230 | USM ECU: a230 temp sens out of range | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_underVoltAtVtankDuringBurst` | page 230 | USM ECU: a230 under volt at vtank during burst | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_overVoltAtVtankDuringBurst` | page 230 | USM ECU: a230 over volt at vtank during burst | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_drvsFailDuringBurst` | page 230 | USM ECU: a230 drvs fail during burst | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_drv1FailDuringBurst` | page 230 | USM ECU: a230 drv1 fail during burst | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_drv2FailDuringBurst` | page 230 | USM ECU: a230 drv2 fail during burst | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_crcMismatchInRam` | page 230 | USM ECU: a230 crc mismatch in ram | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_verificationOfConfigAndCalcParamsFail` | page 230 | USM ECU: a230 verification of config and calc params fail | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_wdgClockFreqOutOfRange` | page 230 | USM ECU: a230 wdg clock freq out of range | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_atgNoiseMeasOutOfRange` | page 230 | USM ECU: a230 atg noise meas out of range | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_syncCountError` | page 230 | USM ECU: a230 sync count error | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_invalidStartEdge` | page 230 | USM ECU: a230 invalid start edge | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_receiverReachedErrorState` | page 230 | USM ECU: a230 receiver reached error state | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_pdcmPulseInvalid` | page 230 | USM ECU: a230 pdcm pulse invalid | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_crcOfReceivedCmdInvalid` | page 230 | USM ECU: a230 crc of received cmd invalid | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_passwordWrong` | page 230 | USM ECU: a230 password wrong | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_timeIntBetween2PulsesErr` | page 230 | USM ECU: a230 time int between2 pulses err | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a230_numInvalidStartEdgeSinceInit` | page 230 | USM ECU: a230 num invalid start edge since init | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `USM_a230_numAtgNoiseErrorsSinceInit` | page 230 | USM ECU: a230 num atg noise errors since init | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `USM_a231_reset` | page 231 | USM ECU: a231 reset | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_otpCrcError` | page 231 | USM ECU: a231 otp crc error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_trimRegParityErr` | page 231 | USM ECU: a231 trim reg parity err | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_sramParityErr` | page 231 | USM ECU: a231 sram parity err | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_crcMismatchInOtp` | page 231 | USM ECU: a231 crc mismatch in otp | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_crcMismatchInSysrom` | page 231 | USM ECU: a231 crc mismatch in sysrom | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_crcMismatchInEeprom` | page 231 | USM ECU: a231 crc mismatch in eeprom | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_capLossVdddOutOfRange` | page 231 | USM ECU: a231 cap loss vddd out of range | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_capLossVddaOutOfRange` | page 231 | USM ECU: a231 cap loss vdda out of range | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_referenceVoltOutOfRange` | page 231 | USM ECU: a231 reference volt out of range | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_vdddVoltOutOfRange` | page 231 | USM ECU: a231 vddd volt out of range | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_vrefVoldOfOtpOutOfRange` | page 231 | USM ECU: a231 vref vold of otp out of range | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_eepromProgFail` | page 231 | USM ECU: a231 eeprom prog fail | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_eepromProgBuys` | page 231 | USM ECU: a231 eeprom prog buys | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_vsupVoltOutOfRange` | page 231 | USM ECU: a231 vsup volt out of range | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_tempSensOutOfRange` | page 231 | USM ECU: a231 temp sens out of range | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_underVoltAtVtankDuringBurst` | page 231 | USM ECU: a231 under volt at vtank during burst | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_overVoltAtVtankDuringBurst` | page 231 | USM ECU: a231 over volt at vtank during burst | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_drvsFailDuringBurst` | page 231 | USM ECU: a231 drvs fail during burst | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_drv1FailDuringBurst` | page 231 | USM ECU: a231 drv1 fail during burst | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_drv2FailDuringBurst` | page 231 | USM ECU: a231 drv2 fail during burst | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_crcMismatchInRam` | page 231 | USM ECU: a231 crc mismatch in ram | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_verificationOfConfigAndCalcParamsFail` | page 231 | USM ECU: a231 verification of config and calc params fail | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_wdgClockFreqOutOfRange` | page 231 | USM ECU: a231 wdg clock freq out of range | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_atgNoiseMeasOutOfRange` | page 231 | USM ECU: a231 atg noise meas out of range | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_syncCountError` | page 231 | USM ECU: a231 sync count error | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_invalidStartEdge` | page 231 | USM ECU: a231 invalid start edge | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_receiverReachedErrorState` | page 231 | USM ECU: a231 receiver reached error state | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_pdcmPulseInvalid` | page 231 | USM ECU: a231 pdcm pulse invalid | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_crcOfReceivedCmdInvalid` | page 231 | USM ECU: a231 crc of received cmd invalid | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_passwordWrong` | page 231 | USM ECU: a231 password wrong | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_timeIntBetween2PulsesErr` | page 231 | USM ECU: a231 time int between2 pulses err | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a231_numInvalidStartEdgeSinceInit` | page 231 | USM ECU: a231 num invalid start edge since init | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `USM_a231_numAtgNoiseErrorsSinceInit` | page 231 | USM ECU: a231 num atg noise errors since init | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `USM_a232_reset` | page 232 | USM ECU: a232 reset | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_otpCrcError` | page 232 | USM ECU: a232 otp crc error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_trimRegParityErr` | page 232 | USM ECU: a232 trim reg parity err | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_sramParityErr` | page 232 | USM ECU: a232 sram parity err | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_crcMismatchInOtp` | page 232 | USM ECU: a232 crc mismatch in otp | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_crcMismatchInSysrom` | page 232 | USM ECU: a232 crc mismatch in sysrom | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_crcMismatchInEeprom` | page 232 | USM ECU: a232 crc mismatch in eeprom | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_capLossVdddOutOfRange` | page 232 | USM ECU: a232 cap loss vddd out of range | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_capLossVddaOutOfRange` | page 232 | USM ECU: a232 cap loss vdda out of range | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_referenceVoltOutOfRange` | page 232 | USM ECU: a232 reference volt out of range | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_vdddVoltOutOfRange` | page 232 | USM ECU: a232 vddd volt out of range | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_vrefVoldOfOtpOutOfRange` | page 232 | USM ECU: a232 vref vold of otp out of range | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_eepromProgFail` | page 232 | USM ECU: a232 eeprom prog fail | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_eepromProgBuys` | page 232 | USM ECU: a232 eeprom prog buys | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_vsupVoltOutOfRange` | page 232 | USM ECU: a232 vsup volt out of range | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_tempSensOutOfRange` | page 232 | USM ECU: a232 temp sens out of range | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_underVoltAtVtankDuringBurst` | page 232 | USM ECU: a232 under volt at vtank during burst | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_overVoltAtVtankDuringBurst` | page 232 | USM ECU: a232 over volt at vtank during burst | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_drvsFailDuringBurst` | page 232 | USM ECU: a232 drvs fail during burst | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_drv1FailDuringBurst` | page 232 | USM ECU: a232 drv1 fail during burst | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_drv2FailDuringBurst` | page 232 | USM ECU: a232 drv2 fail during burst | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_crcMismatchInRam` | page 232 | USM ECU: a232 crc mismatch in ram | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_verificationOfConfigAndCalcParamsFail` | page 232 | USM ECU: a232 verification of config and calc params fail | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_wdgClockFreqOutOfRange` | page 232 | USM ECU: a232 wdg clock freq out of range | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_atgNoiseMeasOutOfRange` | page 232 | USM ECU: a232 atg noise meas out of range | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_syncCountError` | page 232 | USM ECU: a232 sync count error | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_invalidStartEdge` | page 232 | USM ECU: a232 invalid start edge | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_receiverReachedErrorState` | page 232 | USM ECU: a232 receiver reached error state | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_pdcmPulseInvalid` | page 232 | USM ECU: a232 pdcm pulse invalid | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_crcOfReceivedCmdInvalid` | page 232 | USM ECU: a232 crc of received cmd invalid | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_passwordWrong` | page 232 | USM ECU: a232 password wrong | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_timeIntBetween2PulsesErr` | page 232 | USM ECU: a232 time int between2 pulses err | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a232_numInvalidStartEdgeSinceInit` | page 232 | USM ECU: a232 num invalid start edge since init | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `USM_a232_numAtgNoiseErrorsSinceInit` | page 232 | USM ECU: a232 num atg noise errors since init | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `USM_a233_reset` | page 233 | USM ECU: a233 reset | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_otpCrcError` | page 233 | USM ECU: a233 otp crc error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_trimRegParityErr` | page 233 | USM ECU: a233 trim reg parity err | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_sramParityErr` | page 233 | USM ECU: a233 sram parity err | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_crcMismatchInOtp` | page 233 | USM ECU: a233 crc mismatch in otp | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_crcMismatchInSysrom` | page 233 | USM ECU: a233 crc mismatch in sysrom | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_crcMismatchInEeprom` | page 233 | USM ECU: a233 crc mismatch in eeprom | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_capLossVdddOutOfRange` | page 233 | USM ECU: a233 cap loss vddd out of range | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_capLossVddaOutOfRange` | page 233 | USM ECU: a233 cap loss vdda out of range | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_referenceVoltOutOfRange` | page 233 | USM ECU: a233 reference volt out of range | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_vdddVoltOutOfRange` | page 233 | USM ECU: a233 vddd volt out of range | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_vrefVoldOfOtpOutOfRange` | page 233 | USM ECU: a233 vref vold of otp out of range | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_eepromProgFail` | page 233 | USM ECU: a233 eeprom prog fail | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_eepromProgBuys` | page 233 | USM ECU: a233 eeprom prog buys | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_vsupVoltOutOfRange` | page 233 | USM ECU: a233 vsup volt out of range | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_tempSensOutOfRange` | page 233 | USM ECU: a233 temp sens out of range | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_underVoltAtVtankDuringBurst` | page 233 | USM ECU: a233 under volt at vtank during burst | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_overVoltAtVtankDuringBurst` | page 233 | USM ECU: a233 over volt at vtank during burst | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_drvsFailDuringBurst` | page 233 | USM ECU: a233 drvs fail during burst | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_drv1FailDuringBurst` | page 233 | USM ECU: a233 drv1 fail during burst | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_drv2FailDuringBurst` | page 233 | USM ECU: a233 drv2 fail during burst | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_crcMismatchInRam` | page 233 | USM ECU: a233 crc mismatch in ram | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_verificationOfConfigAndCalcParamsFail` | page 233 | USM ECU: a233 verification of config and calc params fail | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_wdgClockFreqOutOfRange` | page 233 | USM ECU: a233 wdg clock freq out of range | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_atgNoiseMeasOutOfRange` | page 233 | USM ECU: a233 atg noise meas out of range | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_syncCountError` | page 233 | USM ECU: a233 sync count error | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_invalidStartEdge` | page 233 | USM ECU: a233 invalid start edge | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_receiverReachedErrorState` | page 233 | USM ECU: a233 receiver reached error state | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_pdcmPulseInvalid` | page 233 | USM ECU: a233 pdcm pulse invalid | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_crcOfReceivedCmdInvalid` | page 233 | USM ECU: a233 crc of received cmd invalid | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_passwordWrong` | page 233 | USM ECU: a233 password wrong | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_timeIntBetween2PulsesErr` | page 233 | USM ECU: a233 time int between2 pulses err | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a233_numInvalidStartEdgeSinceInit` | page 233 | USM ECU: a233 num invalid start edge since init | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `USM_a233_numAtgNoiseErrorsSinceInit` | page 233 | USM ECU: a233 num atg noise errors since init | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `USM_a234_reset` | page 234 | USM ECU: a234 reset | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_otpCrcError` | page 234 | USM ECU: a234 otp crc error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_trimRegParityErr` | page 234 | USM ECU: a234 trim reg parity err | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_sramParityErr` | page 234 | USM ECU: a234 sram parity err | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_crcMismatchInOtp` | page 234 | USM ECU: a234 crc mismatch in otp | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_crcMismatchInSysrom` | page 234 | USM ECU: a234 crc mismatch in sysrom | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_crcMismatchInEeprom` | page 234 | USM ECU: a234 crc mismatch in eeprom | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_capLossVdddOutOfRange` | page 234 | USM ECU: a234 cap loss vddd out of range | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_capLossVddaOutOfRange` | page 234 | USM ECU: a234 cap loss vdda out of range | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_referenceVoltOutOfRange` | page 234 | USM ECU: a234 reference volt out of range | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_vdddVoltOutOfRange` | page 234 | USM ECU: a234 vddd volt out of range | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_vrefVoldOfOtpOutOfRange` | page 234 | USM ECU: a234 vref vold of otp out of range | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_eepromProgFail` | page 234 | USM ECU: a234 eeprom prog fail | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_eepromProgBuys` | page 234 | USM ECU: a234 eeprom prog buys | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_vsupVoltOutOfRange` | page 234 | USM ECU: a234 vsup volt out of range | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_tempSensOutOfRange` | page 234 | USM ECU: a234 temp sens out of range | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_underVoltAtVtankDuringBurst` | page 234 | USM ECU: a234 under volt at vtank during burst | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_overVoltAtVtankDuringBurst` | page 234 | USM ECU: a234 over volt at vtank during burst | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_drvsFailDuringBurst` | page 234 | USM ECU: a234 drvs fail during burst | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_drv1FailDuringBurst` | page 234 | USM ECU: a234 drv1 fail during burst | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_drv2FailDuringBurst` | page 234 | USM ECU: a234 drv2 fail during burst | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_crcMismatchInRam` | page 234 | USM ECU: a234 crc mismatch in ram | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_verificationOfConfigAndCalcParamsFail` | page 234 | USM ECU: a234 verification of config and calc params fail | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_wdgClockFreqOutOfRange` | page 234 | USM ECU: a234 wdg clock freq out of range | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_atgNoiseMeasOutOfRange` | page 234 | USM ECU: a234 atg noise meas out of range | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_syncCountError` | page 234 | USM ECU: a234 sync count error | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_invalidStartEdge` | page 234 | USM ECU: a234 invalid start edge | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_receiverReachedErrorState` | page 234 | USM ECU: a234 receiver reached error state | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_pdcmPulseInvalid` | page 234 | USM ECU: a234 pdcm pulse invalid | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_crcOfReceivedCmdInvalid` | page 234 | USM ECU: a234 crc of received cmd invalid | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_passwordWrong` | page 234 | USM ECU: a234 password wrong | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_timeIntBetween2PulsesErr` | page 234 | USM ECU: a234 time int between2 pulses err | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a234_numInvalidStartEdgeSinceInit` | page 234 | USM ECU: a234 num invalid start edge since init | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `USM_a234_numAtgNoiseErrorsSinceInit` | page 234 | USM ECU: a234 num atg noise errors since init | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `USM_a235_reset` | page 235 | USM ECU: a235 reset | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_otpCrcError` | page 235 | USM ECU: a235 otp crc error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_trimRegParityErr` | page 235 | USM ECU: a235 trim reg parity err | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_sramParityErr` | page 235 | USM ECU: a235 sram parity err | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_crcMismatchInOtp` | page 235 | USM ECU: a235 crc mismatch in otp | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_crcMismatchInSysrom` | page 235 | USM ECU: a235 crc mismatch in sysrom | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_crcMismatchInEeprom` | page 235 | USM ECU: a235 crc mismatch in eeprom | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_capLossVdddOutOfRange` | page 235 | USM ECU: a235 cap loss vddd out of range | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_capLossVddaOutOfRange` | page 235 | USM ECU: a235 cap loss vdda out of range | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_referenceVoltOutOfRange` | page 235 | USM ECU: a235 reference volt out of range | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_vdddVoltOutOfRange` | page 235 | USM ECU: a235 vddd volt out of range | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_vrefVoldOfOtpOutOfRange` | page 235 | USM ECU: a235 vref vold of otp out of range | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_eepromProgFail` | page 235 | USM ECU: a235 eeprom prog fail | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_eepromProgBuys` | page 235 | USM ECU: a235 eeprom prog buys | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_vsupVoltOutOfRange` | page 235 | USM ECU: a235 vsup volt out of range | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_tempSensOutOfRange` | page 235 | USM ECU: a235 temp sens out of range | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_underVoltAtVtankDuringBurst` | page 235 | USM ECU: a235 under volt at vtank during burst | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_overVoltAtVtankDuringBurst` | page 235 | USM ECU: a235 over volt at vtank during burst | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_drvsFailDuringBurst` | page 235 | USM ECU: a235 drvs fail during burst | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_drv1FailDuringBurst` | page 235 | USM ECU: a235 drv1 fail during burst | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_drv2FailDuringBurst` | page 235 | USM ECU: a235 drv2 fail during burst | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_crcMismatchInRam` | page 235 | USM ECU: a235 crc mismatch in ram | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_verificationOfConfigAndCalcParamsFail` | page 235 | USM ECU: a235 verification of config and calc params fail | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_wdgClockFreqOutOfRange` | page 235 | USM ECU: a235 wdg clock freq out of range | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_atgNoiseMeasOutOfRange` | page 235 | USM ECU: a235 atg noise meas out of range | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_syncCountError` | page 235 | USM ECU: a235 sync count error | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_invalidStartEdge` | page 235 | USM ECU: a235 invalid start edge | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_receiverReachedErrorState` | page 235 | USM ECU: a235 receiver reached error state | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_pdcmPulseInvalid` | page 235 | USM ECU: a235 pdcm pulse invalid | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_crcOfReceivedCmdInvalid` | page 235 | USM ECU: a235 crc of received cmd invalid | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_passwordWrong` | page 235 | USM ECU: a235 password wrong | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_timeIntBetween2PulsesErr` | page 235 | USM ECU: a235 time int between2 pulses err | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a235_numInvalidStartEdgeSinceInit` | page 235 | USM ECU: a235 num invalid start edge since init | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `USM_a235_numAtgNoiseErrorsSinceInit` | page 235 | USM ECU: a235 num atg noise errors since init | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `USM_a236_reset` | page 236 | USM ECU: a236 reset | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_otpCrcError` | page 236 | USM ECU: a236 otp crc error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_trimRegParityErr` | page 236 | USM ECU: a236 trim reg parity err | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_sramParityErr` | page 236 | USM ECU: a236 sram parity err | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_crcMismatchInOtp` | page 236 | USM ECU: a236 crc mismatch in otp | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_crcMismatchInSysrom` | page 236 | USM ECU: a236 crc mismatch in sysrom | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_crcMismatchInEeprom` | page 236 | USM ECU: a236 crc mismatch in eeprom | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_capLossVdddOutOfRange` | page 236 | USM ECU: a236 cap loss vddd out of range | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_capLossVddaOutOfRange` | page 236 | USM ECU: a236 cap loss vdda out of range | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_referenceVoltOutOfRange` | page 236 | USM ECU: a236 reference volt out of range | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_vdddVoltOutOfRange` | page 236 | USM ECU: a236 vddd volt out of range | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_vrefVoldOfOtpOutOfRange` | page 236 | USM ECU: a236 vref vold of otp out of range | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_eepromProgFail` | page 236 | USM ECU: a236 eeprom prog fail | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_eepromProgBuys` | page 236 | USM ECU: a236 eeprom prog buys | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_vsupVoltOutOfRange` | page 236 | USM ECU: a236 vsup volt out of range | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_tempSensOutOfRange` | page 236 | USM ECU: a236 temp sens out of range | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_underVoltAtVtankDuringBurst` | page 236 | USM ECU: a236 under volt at vtank during burst | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_overVoltAtVtankDuringBurst` | page 236 | USM ECU: a236 over volt at vtank during burst | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_drvsFailDuringBurst` | page 236 | USM ECU: a236 drvs fail during burst | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_drv1FailDuringBurst` | page 236 | USM ECU: a236 drv1 fail during burst | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_drv2FailDuringBurst` | page 236 | USM ECU: a236 drv2 fail during burst | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_crcMismatchInRam` | page 236 | USM ECU: a236 crc mismatch in ram | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_verificationOfConfigAndCalcParamsFail` | page 236 | USM ECU: a236 verification of config and calc params fail | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_wdgClockFreqOutOfRange` | page 236 | USM ECU: a236 wdg clock freq out of range | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_atgNoiseMeasOutOfRange` | page 236 | USM ECU: a236 atg noise meas out of range | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_syncCountError` | page 236 | USM ECU: a236 sync count error | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_invalidStartEdge` | page 236 | USM ECU: a236 invalid start edge | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_receiverReachedErrorState` | page 236 | USM ECU: a236 receiver reached error state | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_pdcmPulseInvalid` | page 236 | USM ECU: a236 pdcm pulse invalid | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_crcOfReceivedCmdInvalid` | page 236 | USM ECU: a236 crc of received cmd invalid | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_passwordWrong` | page 236 | USM ECU: a236 password wrong | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_timeIntBetween2PulsesErr` | page 236 | USM ECU: a236 time int between2 pulses err | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a236_numInvalidStartEdgeSinceInit` | page 236 | USM ECU: a236 num invalid start edge since init | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `USM_a236_numAtgNoiseErrorsSinceInit` | page 236 | USM ECU: a236 num atg noise errors since init | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `USM_a237_reset` | page 237 | USM ECU: a237 reset | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_otpCrcError` | page 237 | USM ECU: a237 otp crc error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_trimRegParityErr` | page 237 | USM ECU: a237 trim reg parity err | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_sramParityErr` | page 237 | USM ECU: a237 sram parity err | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_crcMismatchInOtp` | page 237 | USM ECU: a237 crc mismatch in otp | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_crcMismatchInSysrom` | page 237 | USM ECU: a237 crc mismatch in sysrom | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_crcMismatchInEeprom` | page 237 | USM ECU: a237 crc mismatch in eeprom | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_capLossVdddOutOfRange` | page 237 | USM ECU: a237 cap loss vddd out of range | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_capLossVddaOutOfRange` | page 237 | USM ECU: a237 cap loss vdda out of range | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_referenceVoltOutOfRange` | page 237 | USM ECU: a237 reference volt out of range | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_vdddVoltOutOfRange` | page 237 | USM ECU: a237 vddd volt out of range | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_vrefVoldOfOtpOutOfRange` | page 237 | USM ECU: a237 vref vold of otp out of range | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_eepromProgFail` | page 237 | USM ECU: a237 eeprom prog fail | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_eepromProgBuys` | page 237 | USM ECU: a237 eeprom prog buys | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_vsupVoltOutOfRange` | page 237 | USM ECU: a237 vsup volt out of range | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_tempSensOutOfRange` | page 237 | USM ECU: a237 temp sens out of range | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_underVoltAtVtankDuringBurst` | page 237 | USM ECU: a237 under volt at vtank during burst | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_overVoltAtVtankDuringBurst` | page 237 | USM ECU: a237 over volt at vtank during burst | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_drvsFailDuringBurst` | page 237 | USM ECU: a237 drvs fail during burst | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_drv1FailDuringBurst` | page 237 | USM ECU: a237 drv1 fail during burst | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_drv2FailDuringBurst` | page 237 | USM ECU: a237 drv2 fail during burst | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_crcMismatchInRam` | page 237 | USM ECU: a237 crc mismatch in ram | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_verificationOfConfigAndCalcParamsFail` | page 237 | USM ECU: a237 verification of config and calc params fail | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_wdgClockFreqOutOfRange` | page 237 | USM ECU: a237 wdg clock freq out of range | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_atgNoiseMeasOutOfRange` | page 237 | USM ECU: a237 atg noise meas out of range | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_syncCountError` | page 237 | USM ECU: a237 sync count error | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_invalidStartEdge` | page 237 | USM ECU: a237 invalid start edge | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_receiverReachedErrorState` | page 237 | USM ECU: a237 receiver reached error state | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_pdcmPulseInvalid` | page 237 | USM ECU: a237 pdcm pulse invalid | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_crcOfReceivedCmdInvalid` | page 237 | USM ECU: a237 crc of received cmd invalid | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_passwordWrong` | page 237 | USM ECU: a237 password wrong | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_timeIntBetween2PulsesErr` | page 237 | USM ECU: a237 time int between2 pulses err | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a237_numInvalidStartEdgeSinceInit` | page 237 | USM ECU: a237 num invalid start edge since init | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `USM_a237_numAtgNoiseErrorsSinceInit` | page 237 | USM ECU: a237 num atg noise errors since init | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `USM_a238_reset` | page 238 | USM ECU: a238 reset | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_otpCrcError` | page 238 | USM ECU: a238 otp crc error | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_trimRegParityErr` | page 238 | USM ECU: a238 trim reg parity err | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_sramParityErr` | page 238 | USM ECU: a238 sram parity err | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_crcMismatchInOtp` | page 238 | USM ECU: a238 crc mismatch in otp | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_crcMismatchInSysrom` | page 238 | USM ECU: a238 crc mismatch in sysrom | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_crcMismatchInEeprom` | page 238 | USM ECU: a238 crc mismatch in eeprom | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_capLossVdddOutOfRange` | page 238 | USM ECU: a238 cap loss vddd out of range | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_capLossVddaOutOfRange` | page 238 | USM ECU: a238 cap loss vdda out of range | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_referenceVoltOutOfRange` | page 238 | USM ECU: a238 reference volt out of range | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_vdddVoltOutOfRange` | page 238 | USM ECU: a238 vddd volt out of range | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_vrefVoldOfOtpOutOfRange` | page 238 | USM ECU: a238 vref vold of otp out of range | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_eepromProgFail` | page 238 | USM ECU: a238 eeprom prog fail | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_eepromProgBuys` | page 238 | USM ECU: a238 eeprom prog buys | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_vsupVoltOutOfRange` | page 238 | USM ECU: a238 vsup volt out of range | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_tempSensOutOfRange` | page 238 | USM ECU: a238 temp sens out of range | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_underVoltAtVtankDuringBurst` | page 238 | USM ECU: a238 under volt at vtank during burst | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_overVoltAtVtankDuringBurst` | page 238 | USM ECU: a238 over volt at vtank during burst | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_drvsFailDuringBurst` | page 238 | USM ECU: a238 drvs fail during burst | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_drv1FailDuringBurst` | page 238 | USM ECU: a238 drv1 fail during burst | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_drv2FailDuringBurst` | page 238 | USM ECU: a238 drv2 fail during burst | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_crcMismatchInRam` | page 238 | USM ECU: a238 crc mismatch in ram | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_verificationOfConfigAndCalcParamsFail` | page 238 | USM ECU: a238 verification of config and calc params fail | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_wdgClockFreqOutOfRange` | page 238 | USM ECU: a238 wdg clock freq out of range | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_atgNoiseMeasOutOfRange` | page 238 | USM ECU: a238 atg noise meas out of range | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_syncCountError` | page 238 | USM ECU: a238 sync count error | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_invalidStartEdge` | page 238 | USM ECU: a238 invalid start edge | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_receiverReachedErrorState` | page 238 | USM ECU: a238 receiver reached error state | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_pdcmPulseInvalid` | page 238 | USM ECU: a238 pdcm pulse invalid | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_crcOfReceivedCmdInvalid` | page 238 | USM ECU: a238 crc of received cmd invalid | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_passwordWrong` | page 238 | USM ECU: a238 password wrong | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_timeIntBetween2PulsesErr` | page 238 | USM ECU: a238 time int between2 pulses err | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `USM_a238_numInvalidStartEdgeSinceInit` | page 238 | USM ECU: a238 num invalid start edge since init | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |
| `USM_a238_numAtgNoiseErrorsSinceInit` | page 238 | USM ECU: a238 num atg noise errors since init | 52\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | layout-only |

## Multiplexing

`USM_alertID` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (1 signals), page 2 (2 signals), page 15 (3 signals), page 57 (1 signals), page 59 (3 signals), page 63 (7 signals), page 82 (4 signals), page 83 (4 signals), page 84 (1 signals), page 85 (1 signals), page 86 (9 signals), page 87 (8 signals), page 88 (8 signals), page 89 (10 signals), page 91 (3 signals), page 92 (4 signals), page 93 (4 signals), page 94 (2 signals), page 95 (2 signals), page 96 (2 signals), page 98 (12 signals), page 99 (1 signals), page 100 (5 signals), page 101 (5 signals), page 102 (4 signals), page 103 (6 signals), page 105 (3 signals), page 106 (6 signals), page 107 (15 signals), page 108 (11 signals), page 109 (16 signals), page 110 (16 signals), page 111 (12 signals), page 112 (11 signals), page 114 (20 signals), page 115 (8 signals), page 116 (21 signals), page 117 (23 signals), page 118 (28 signals), page 119 (6 signals), page 120 (27 signals), page 131 (4 signals), page 132 (4 signals), page 133 (4 signals), page 134 (4 signals), page 135 (4 signals), page 136 (4 signals), page 137 (4 signals), page 138 (4 signals), page 139 (4 signals), page 140 (4 signals), page 141 (4 signals), page 142 (4 signals), page 143 (4 signals), page 144 (4 signals), page 145 (4 signals), page 146 (4 signals), page 147 (4 signals), page 148 (4 signals), page 149 (4 signals), page 150 (4 signals), page 151 (4 signals), page 152 (4 signals), page 153 (4 signals), page 154 (4 signals), page 155 (1 signals), page 156 (1 signals), page 157 (1 signals), page 158 (1 signals), page 159 (1 signals), page 160 (1 signals), page 161 (1 signals), page 162 (1 signals), page 163 (1 signals), page 164 (1 signals), page 165 (1 signals), page 166 (1 signals), page 177 (5 signals), page 178 (5 signals), page 179 (5 signals), page 180 (5 signals), page 181 (5 signals), page 182 (5 signals), page 183 (5 signals), page 184 (5 signals), page 185 (5 signals), page 186 (5 signals), page 187 (5 signals), page 188 (5 signals), page 201 (19 signals), page 202 (9 signals), page 227 (34 signals), page 228 (34 signals), page 229 (34 signals), page 230 (34 signals), page 231 (34 signals), page 232 (34 signals), page 233 (34 signals), page 234 (34 signals), page 235 (34 signals), page 236 (34 signals), page 237 (34 signals), page 238 (34 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All USM ECU messages (USM)](../../usm.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
