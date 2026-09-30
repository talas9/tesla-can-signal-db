---
layout: default
title: "VCLEFT_logging10Hz (0x289) — Left body controller, Tesla Model 3 2026.26.6.5 ETH"
description: "Left body controller message: logging10 hz. Ethernet-side message VCLEFT_logging10Hz of Left body controller for Tesla Model 3 firmware 2026.26.6.5, 15 signals (VCLEFT_logging10HzIndex, VCLEFT_hvacBlowerRs, VCLEFT_hvacBlowerIPhase0, VCLEFT_hvacBlowerIPhase1 and 11 more). Bit layout, scaling, units and value tables."
---

# VCLEFT_logging10Hz (0x289) — Left body controller, Tesla Model 3 2026.26.6.5 ETH

Left body controller message: logging10 hz. This page documents the 15 signals of VCLEFT_logging10Hz as defined for Tesla Model 3 firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `VCLEFT_logging10Hz` |
| Ethernet-side id | 0x289 (649) |
| ECU | [Left body controller](../../vcleft.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | VCLEFT |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 15 |

## Signals of VCLEFT_logging10Hz

Tesla Model 3 CAN bus signals in `VCLEFT_logging10Hz`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCLEFT_logging10HzIndex` | selector | Left body controller: logging10 hz index | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `HVAC_VARS`<br>1 = `END` | plausible |
| `VCLEFT_hvacBlowerRs` | page 0 | Left body controller: hvac blower rs; raw 255 = signal not available (SNA) | 1\|8 | little-endian | unsigned | 0.25 | 0 | mOhm | 0 to 60 | 255 = `SNA` | validated |
| `VCLEFT_hvacBlowerIPhase0` | page 0 | Left body controller: hvac blower i phase0; raw 127 = signal not available (SNA) | 9\|7 | little-endian | unsigned | 0.4 | 0 | A | 0 to 50 | 127 = `SNA` | validated |
| `VCLEFT_hvacBlowerIPhase1` | page 0 | Left body controller: hvac blower i phase1; raw 127 = signal not available (SNA) | 16\|7 | little-endian | unsigned | 0.4 | 0 | A | 0 to 50 | 127 = `SNA` | validated |
| `VCLEFT_hvacBlowerIPhase2` | page 0 | Left body controller: hvac blower i phase2; raw 127 = signal not available (SNA) | 23\|7 | little-endian | unsigned | 0.4 | 0 | A | 0 to 50 | 127 = `SNA` | validated |
| `VCLEFT_hvacBlower_IO_CBC_HEAD` | page 0 | Left body controller: hvac blower IO CBC HEAD | 30\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `VCLEFT_hvacBlower_IO_CBC_TAIL` | page 0 | Left body controller: hvac blower IO CBC TAIL | 34\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 |  | validated |
| `VCLEFT_hvacBlower_IO_CBC_TAIL_valid` | page 0 | Left body controller: hvac blower IO CBC TAIL valid | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_hvacBlower_IO_CBC_Status` | page 0 | Left body controller: hvac blower IO CBC status | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `IDLE`<br>1 = `RX` | validated |
| `VCLEFT_hvacBlower_IO_CBC_numUartErr` | page 0 | Left body controller: hvac blower IO CBC num uart err | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCLEFT_hvacBlowerCBCEstState` | page 0 | Left body controller: hvac blower CBC est state | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `ERROR`<br>1 = `IDLE`<br>2 = `ROVERL`<br>3 = `RS`<br>4 = `RAMPUP`<br>5 = `IDRATED`<br>6 = `RATEDFLUX_OL`<br>7 = `RATEDFLUX`<br>8 = `RAMPDOWN`<br>9 = `LOCKROTOR`<br>10 = `INDUCTANCE_EST`<br>11 = `ROTOR_RESISTANCE`<br>12 = `MOTOR_IDENTIFIED`<br>13 = `ONLINE`<br>14 = `COUNT` | validated |
| `VCLEFT_hvacBlowerCBCCtrlState` | page 0 | Left body controller: hvac blower CBC ctrl state | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ERROR`<br>1 = `IDLE`<br>2 = `OFFLINE`<br>3 = `ONLINE`<br>4 = `COUNT` | validated |
| `VCLEFT_hvacBlowerITerm` | page 0 | Left body controller: hvac blower i term; raw 127 = signal not available (SNA) | 55\|7 | little-endian | unsigned | 0.05 | -1.5 | Nm | -1.5 to 4.5 | 127 = `SNA` | validated |
| `VCLEFT_hvacBlowerSpiError` | page 0 | Left body controller: hvac blower spi error | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCLEFT_hvacBlowerRsOnlineActive` | page 0 | Left body controller: hvac blower rs online active | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Multiplexing

`VCLEFT_logging10HzIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (14 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 ETH DBC file](../../../../../dbc/Model3/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Left body controller messages (VCLEFT)](../../vcleft.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
