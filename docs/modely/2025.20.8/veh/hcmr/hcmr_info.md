---
layout: default
title: "HCMR_info (0x7BC) — HCMR ECU, Tesla Model Y 2025.20.8 VEH CAN"
description: "HCMR ECU message: info. Tesla Model Y CAN bus message HCMR_info (0x7BC) of HCMR ECU, firmware 2025.20.8, 6 signals (VC_hcmrInfoIndex, VC_infoHCMRBuildConfigId, VC_rightHeadlampLMMVariant, VC_infoHCMRAssemblyId and 2 more). Bit layout, scaling, units and value tables."
---

# HCMR_info (0x7BC) — HCMR ECU, Tesla Model Y 2025.20.8 VEH CAN

HCMR ECU message: info; frame length observed on a vehicle bus. This page documents the 6 signals of HCMR_info as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `HCMR_info` |
| CAN id | 0x7BC (1980) |
| ECU | [HCMR ECU](../../hcmr.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | HCMR |
| Frame length | 7 bytes |
| Cycle time | 10000 ms |
| Signals | 6 |

## Signals of HCMR_info

Tesla Model Y CAN bus signals in `HCMR_info`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VC_hcmrInfoIndex` | selector | HCMR ECU: hcmr info index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `HCMR_BUILD_CONFIG_ID_LMM_VARIANT`<br>1 = `HCMR_ASSEMBLY_PCBA_USAGE_ID`<br>2 = `ECULESS_IC400_HB_FAULTS`<br>3 = `ECULESS_IC500_LB_FAULTS`<br>4 = `ECULESS_IC600_DRL_TURN_FAULTS`<br>5 = `ECULESS_IC700_SM_FAULTS`<br>6 = `ECULESS_LED_VOLTAGES`<br>7 = `ECULESS_MISC`<br>8 = `END` | plausible |
| `VC_infoHCMRBuildConfigId` | page 0 | HCM Diagnostic Field. | 8\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VC_rightHeadlampLMMVariant` | page 0 | Reports the detected right headlamp LED Matrix Manager (LMM) variant; raw 0 = signal not available (SNA) | 24\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `LMM_VARIANT_SNA`<br>1 = `LMM_VARIANT_NOT_LMM4_OR_UNKNOWN`<br>2 = `LMM_VARIANT_LMM4` | validated |
| `VC_infoHCMRAssemblyId` | page 1 | HCM Diagnostic Field. | 8\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VC_infoHCMRPcbaId` | page 1 | HCM Diagnostic Field. | 24\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VC_infoHCMRUsageId` | page 1 | HCM Diagnostic Field. | 40\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |

## Multiplexing

`VC_hcmrInfoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (2 signals), page 1 (3 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All HCMR ECU messages (HCMR)](../../hcmr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
