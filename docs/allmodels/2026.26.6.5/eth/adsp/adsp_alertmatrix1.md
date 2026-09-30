---
layout: default
title: "ADSP_alertMatrix1 (0x551) — Audio amplifier, Tesla Model 3 / Model Y 2026.26.6.5 ETH"
description: "Audio amplifier message: alert matrix1. Ethernet-side message ADSP_alertMatrix1 of Audio amplifier for Tesla Model 3 / Model Y firmware 2026.26.6.5, 60 signals (ADSP_w001_flashInit, ADSP_w002_exception, ADSP_w003_assert, ADSP_w004_malloc and 56 more). Bit layout, scaling, units and value tables."
---

# ADSP_alertMatrix1 (0x551) — Audio amplifier, Tesla Model 3 / Model Y 2026.26.6.5 ETH

Audio amplifier message: alert matrix1. This page documents the 60 signals of ADSP_alertMatrix1 as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `ADSP_alertMatrix1` |
| Ethernet-side id | 0x551 (1361) |
| ECU | [Audio amplifier](../../adsp.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | ADSP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 60 |

## Signals of ADSP_alertMatrix1

Tesla Model 3 / Model Y CAN bus signals in `ADSP_alertMatrix1`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `ADSP_w001_flashInit` | Audio amplifier: w001 flash init | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w002_exception` | Audio amplifier: w002 exception | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w003_assert` | Audio amplifier: w003 assert | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w004_malloc` | Audio amplifier: w004 malloc | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w005_stackOverflow` | Audio amplifier: w005 stack overflow | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w006_eavbSeqno` | Audio amplifier: w006 eavb seqno | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w007_ethLinkErr` | Audio amplifier: w007 eth link err | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w008_internalTempHigh` | Audio amplifier: w008 internal temp high | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w010_12vAudioFiltLow` | Audio amplifier: w010 12v audio filt low | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w011_armHighCpuUsage` | Audio amplifier: w011 arm high cpu usage | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w012_sharc0HighCpuUsage` | Audio amplifier: w012 sharc0 high cpu usage | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w013_sharc1HighCpuUsage` | Audio amplifier: w013 sharc1 high cpu usage | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w014_eavbOverrun` | Audio amplifier: w014 eavb overrun | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w015_eavbUnderrun` | Audio amplifier: w015 eavb underrun | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w016_usbRxOverrun` | Audio amplifier: w016 usb rx overrun | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w017_usbRxUnderrun` | Audio amplifier: w017 usb rx underrun | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w018_usbTxOverrun` | Audio amplifier: w018 usb tx overrun | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w019_usbTxUnderrun` | Audio amplifier: w019 usb tx underrun | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w020_usbTxFailed` | Audio amplifier: w020 usb tx failed | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w021_usbTxAborted` | Audio amplifier: w021 usb tx aborted | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w022_emacErr` | Audio amplifier: w022 emac err | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w023_ethEtharpErr` | Audio amplifier: w023 eth etharp err | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w024_ethIpfragErr` | Audio amplifier: w024 eth ipfrag err | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w025_ethIpErr` | Audio amplifier: w025 eth ip err | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w026_ethIcmpErr` | Audio amplifier: w026 eth icmp err | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w027_ethUdpErr` | Audio amplifier: w027 eth udp err | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w028_ethTcpErr` | Audio amplifier: w028 eth tcp err | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w029_baseamp0SmFault` | Audio amplifier: w029 baseamp0 sm fault | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w030_ethSysErr` | Audio amplifier: w030 eth sys err | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w031_baseamp1SmFault` | Audio amplifier: w031 baseamp1 sm fault | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w032_baseamp2SmFault` | Audio amplifier: w032 baseamp2 sm fault | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w033_a2baDiscoveryFailed` | Audio amplifier: w033 a2ba discovery failed | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w034_a2bbDiscoveryFailed` | Audio amplifier: w034 a2bb discovery failed | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w035_a2baFault` | Audio amplifier: w035 a2ba fault | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w036_a2bbFault` | Audio amplifier: w036 a2bb fault | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w037_a2baIdleFailed` | Audio amplifier: w037 a2ba idle failed | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w038_a2bbIdleFailed` | Audio amplifier: w038 a2bb idle failed | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w039_ancPing` | Audio amplifier: w039 anc ping | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w040_socSciHeartbeat` | Audio amplifier: w040 soc sci heartbeat | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w041_twiWriteError` | Audio amplifier: w041 twi write error | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w042_twiReadError` | Audio amplifier: w042 twi read error | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w043_aweControlError` | Audio amplifier: w043 awe control error | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w044_canethChecksum` | Audio amplifier: w044 caneth checksum | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w045_ancEnableFail` | Audio amplifier: w045 anc enable fail | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w046_sharc0AweFrameOverload` | Audio amplifier: w046 sharc0 awe frame overload | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w047_sharc1AweFrameOverload` | Audio amplifier: w047 sharc1 awe frame overload | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w048_eCallSelfTestFailed` | Audio amplifier: w048 e call self test failed | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w049_sae` | Audio amplifier: w049 sae | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w050_extSpkFault` | Audio amplifier: w050 ext spk fault | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w051_extspkFailure` | Audio amplifier: w051 extspk failure | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w052_criticalReset` | Audio amplifier: w052 critical reset | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w053_audioSystemUnavailable` | Audio amplifier: w053 audio system unavailable | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w054_canethRxError` | Audio amplifier: w054 caneth rx error | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w055_hfpMathExcept1NAN` | Audio amplifier: w055 hfp math except1 NAN | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w056_hfpMathExcept1INF` | Audio amplifier: w056 hfp math except1 INF | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w057_hfpMathExcept2NAN` | Audio amplifier: w057 hfp math except2 NAN | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w058_hfpMathExcept2INF` | Audio amplifier: w058 hfp math except2 INF | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w059_nvmmError` | Audio amplifier: w059 nvmm error | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w060_baseamp3SmFault` | Audio amplifier: w060 baseamp3 sm fault | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `ADSP_w061_tcuGpioServiceError` | Audio amplifier: w061 tcu gpio service error | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/AllModels/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Audio amplifier messages (ADSP)](../../adsp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
