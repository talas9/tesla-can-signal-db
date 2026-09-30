---
layout: default
title: "ADSP_alertMatrix2 (0x552) — Audio amplifier, Tesla Model 3 2025.20.8 ETH"
description: "Audio amplifier message: alert matrix2. Ethernet-side message ADSP_alertMatrix2 of Audio amplifier for Tesla Model 3 firmware 2025.20.8, 12 signals (ADSP_w065_tcuGpioExpanderCriticalError, ADSP_w066_rearPwsFault, ADSP_w067_baseamp0Fault, ADSP_w068_baseamp1Fault and 8 more). Bit layout, scaling, units and value tables."
---

# ADSP_alertMatrix2 (0x552) — Audio amplifier, Tesla Model 3 2025.20.8 ETH

Audio amplifier message: alert matrix2. This page documents the 12 signals of ADSP_alertMatrix2 as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `ADSP_alertMatrix2` |
| Ethernet-side id | 0x552 (1362) |
| ECU | [Audio amplifier](../../adsp.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | ADSP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 12 |

## Signals of ADSP_alertMatrix2

Tesla Model 3 CAN bus signals in `ADSP_alertMatrix2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `ADSP_w065_tcuGpioExpanderCriticalError` | Audio amplifier: w065 tcu gpio expander critical error | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w066_rearPwsFault` | Audio amplifier: w066 rear pws fault | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w067_baseamp0Fault` | Audio amplifier: w067 baseamp0 fault | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w068_baseamp1Fault` | Audio amplifier: w068 baseamp1 fault | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w069_baseamp2Fault` | Audio amplifier: w069 baseamp2 fault | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w070_baseamp3Fault` | Audio amplifier: w070 baseamp3 fault | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w071_versionMismatch` | Audio amplifier: w071 version mismatch | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w072_turnSignalChannelUnderrun` | Audio amplifier: w072 turn signal channel underrun | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w073_romFLError` | Audio amplifier: w073 rom FL error | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w074_tdspArmXrun` | Audio amplifier: w074 tdsp arm xrun | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w075_tdspArmError` | Audio amplifier: w075 tdsp arm error | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w076_activeSafetyChannelUnderrun` | Audio amplifier: w076 active safety channel underrun | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Audio amplifier messages (ADSP)](../../adsp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
