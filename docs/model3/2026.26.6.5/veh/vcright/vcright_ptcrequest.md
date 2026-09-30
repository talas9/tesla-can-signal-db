---
layout: default
title: "VCRIGHT_PTCRequest (0x283) — Right body controller, Tesla Model 3 2026.26.6.5 VEH CAN"
description: "Right body controller message: PTC request. Tesla Model 3 CAN bus message VCRIGHT_PTCRequest (0x283) of Right body controller, firmware 2026.26.6.5, 14 signals (VCRIGHT_PTCLeftTargetPowerHV, VCRIGHT_PTCRightTargetPowerHV, VCRIGHT_PTCLeftTargetDuty, VCRIGHT_PTCRightTargetDuty and 10 more). Bit layout, scaling, units and value tables."
---

# VCRIGHT_PTCRequest (0x283) — Right body controller, Tesla Model 3 2026.26.6.5 VEH CAN

Right body controller message: PTC request; frame length observed on a vehicle bus. This page documents the 14 signals of VCRIGHT_PTCRequest as defined for Tesla Model 3 firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCRIGHT_PTCRequest` |
| CAN id | 0x283 (643) |
| ECU | [Right body controller](../../vcright.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCRIGHT |
| Frame length | 6 bytes |
| Cycle time | 100 ms |
| Signals | 14 |

## Signals of VCRIGHT_PTCRequest

Tesla Model 3 CAN bus signals in `VCRIGHT_PTCRequest`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `VCRIGHT_PTCLeftTargetPowerHV` | Right body controller: PTC left target power HV | 0\|8 | little-endian | unsigned | 30 | 0 | W | 0 to 7650 |  | validated |
| `VCRIGHT_PTCRightTargetPowerHV` | Right body controller: PTC right target power HV | 8\|8 | little-endian | unsigned | 30 | 0 | W | 0 to 7650 |  | validated |
| `VCRIGHT_PTCLeftTargetDuty` | Right body controller: PTC left target duty | 16\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_PTCRightTargetDuty` | Right body controller: PTC right target duty | 24\|8 | little-endian | unsigned | 0.5 | 0 | % | 0 to 100 |  | validated |
| `VCRIGHT_PTCFlagAllowOperation` | Right body controller: PTC flag allow operation | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_PTCRequestMode` | Right body controller: PTC request mode | 33\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `POWER`<br>1 = `DUTY`<br>2 = `DIRECT`<br>3 = `SEQ_ROD_COI`<br>4 = `SEQ_ROD_CIO` | validated |
| `VCRIGHT_PTCResistanceCheckEnable` | Right body controller: PTC resistance check enable | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_PTCReset` | Right body controller: PTC reset | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_PTCLeftDirectDriveIGBTO` | Right body controller: PTC left direct drive IGBTO | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_PTCLeftDirectDriveIGBTC` | Right body controller: PTC left direct drive IGBTC | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_PTCLeftDirectDriveIGBTI` | Right body controller: PTC left direct drive IGBTI | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_PTCRightDirectDriveIGBTI` | Right body controller: PTC right direct drive IGBTI | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_PTCRightDirectDriveIGBTC` | Right body controller: PTC right direct drive IGBTC | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCRIGHT_PTCRightDirectDriveIGBTO` | Right body controller: PTC right direct drive IGBTO | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model 3 2026.26.6.5 VEH DBC file](../../../../../dbc/Model3/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2026.26.6.5/VEH.json)

## See also

- [All Right body controller messages (VCRIGHT)](../../vcright.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
