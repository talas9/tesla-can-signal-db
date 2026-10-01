---
layout: default
title: "HVP_debugMessage (0x7AA) — High-voltage processor (pack contactor and isolation controller), Tesla Model 3 2025.20.8 ETH"
description: "High-voltage processor (pack contactor and isolation controller) message: debug message. Ethernet-side message HVP_debugMessage of High-voltage processor (pack contactor and isolation controller) for Tesla Model 3 firmware 2025.20.8, 49 signals (HVP_debugMessageMultiplexer, HVP_gpioPassivePyroDepl, HVP_gpioPyroIsoEn, HVP_gpioCpFaultIn and 45 more). Bit layout, scaling, units and value tables."
---

# HVP_debugMessage (0x7AA) — High-voltage processor (pack contactor and isolation controller), Tesla Model 3 2025.20.8 ETH

High-voltage processor (pack contactor and isolation controller) message: debug message. This page documents the 49 signals of HVP_debugMessage as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `HVP_debugMessage` |
| Ethernet-side id | 0x7AA (1962) |
| ECU | [High-voltage processor (pack contactor and isolation controller)](../../hvp.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | HVP |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 49 |

## Signals of HVP_debugMessage

Tesla Model 3 CAN bus signals in `HVP_debugMessage`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `HVP_debugMessageMultiplexer` | selector | High-voltage processor (pack contactor and isolation controller): debug message multiplexer | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `Mux0`<br>1 = `Mux1`<br>2 = `Mux2`<br>3 = `Mux3`<br>4 = `Mux4`<br>5 = `Mux5`<br>6 = `Mux6`<br>7 = `Mux7`<br>8 = `Mux8`<br>9 = `Mux9`<br>10 = `Mux10`<br>11 = `Mux11`<br>12 = `Mux12` | plausible |
| `HVP_gpioPassivePyroDepl` | page 0 | High-voltage processor (pack contactor and isolation controller): gpio passive pyro depl | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_gpioPyroIsoEn` | page 0 | High-voltage processor (pack contactor and isolation controller): gpio pyro iso en | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_gpioCpFaultIn` | page 0 | High-voltage processor (pack contactor and isolation controller): gpio cp fault in | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_gpioPackContPowerEn` | page 0 | High-voltage processor (pack contactor and isolation controller): gpio pack cont power en | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_gpioHvCablesOk` | page 0 | CPIL fault monitoring signal | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `HVP_gpioHvpSelfEnable` | page 0 | High-voltage processor (pack contactor and isolation controller): gpio hvp self enable | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_gpioLed` | page 0 | High-voltage processor (pack contactor and isolation controller): gpio led | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_gpioCrashSignal` | page 0 | Crash signal from RCM | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `HVP_gpioShuntDataReady` | page 0 | High-voltage processor (pack contactor and isolation controller): gpio shunt data ready | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_gpioFcContPosAux` | page 0 | Aux contact line from positive FC contactor | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `HVP_gpioFcContNegAux` | page 0 | Aux contact line from negative FC contactor | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `HVP_gpioBmsEout` | page 0 | High-voltage processor (pack contactor and isolation controller): gpio bms eout | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_gpioCpFaultOut` | page 0 | High-voltage processor (pack contactor and isolation controller): gpio cp fault out | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_gpioPyroPor` | page 0 | High-voltage processor (pack contactor and isolation controller): gpio pyro por | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_gpioShuntEn` | page 0 | High-voltage processor (pack contactor and isolation controller): gpio shunt en | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_gpioHvpVerEn` | page 0 | High-voltage processor (pack contactor and isolation controller): gpio hvp ver en | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_gpioFcContFlywheelEnable` | page 0 | High-voltage processor (pack contactor and isolation controller): gpio fc cont flywheel enable | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_gpioCpLatchEnable` | page 0 | High-voltage processor (pack contactor and isolation controller): gpio cp latch enable | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_gpioFcContPowerEnable` | page 0 | High-voltage processor (pack contactor and isolation controller): gpio fc cont power enable | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_gpioHvilEnable` | page 0 | High-voltage processor (pack contactor and isolation controller): gpio hvil enable | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_gpioPortSelSpiRdy` | page 0 | High-voltage processor (pack contactor and isolation controller): gpio port sel spi rdy | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_gpioPyroUnlock` | page 0 | High-voltage processor (pack contactor and isolation controller): gpio pyro unlock | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_hvp1v5Ref` | page 0 | High-voltage processor (pack contactor and isolation controller): hvp1v5 ref | 26\|12 | little-endian | unsigned | 0.1 | 0 | V | 0 to 3 |  | plausible |
| `HVP_packCurrentMia` | page 0 | High-voltage processor (pack contactor and isolation controller): pack current mia | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_auxCurrentMia` | page 0 | High-voltage processor (pack contactor and isolation controller): aux current mia | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_currentSenseMia` | page 0 | High-voltage processor (pack contactor and isolation controller): current sense mia | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_shuntRefVoltageMismatch` | page 0 | High-voltage processor (pack contactor and isolation controller): shunt ref voltage mismatch | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_shuntThermistorMissing` | page 0 | High-voltage processor (pack contactor and isolation controller): shunt thermistor missing | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_shuntThermistorExpected` | page 0 | High-voltage processor (pack contactor and isolation controller): shunt thermistor expected | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_shuntThermistorMia` | page 0 | High-voltage processor (pack contactor and isolation controller): shunt thermistor mia | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_shuntUnexpectedThermistor` | page 0 | High-voltage processor (pack contactor and isolation controller): shunt unexpected thermistor | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_shuntHwMia` | page 0 | High-voltage processor (pack contactor and isolation controller): shunt hw mia | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_shuntCurrentIrrational` | page 0 | High-voltage processor (pack contactor and isolation controller): shunt current irrational | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_shuntAsicTCompActive` | page 0 | High-voltage processor (pack contactor and isolation controller): shunt asic t comp active | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_ecuLogUploadRequest` | page 0 | High-voltage processor (pack contactor and isolation controller): ecu log upload request | 49\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `REQUEST_PRIORITY_NONE`<br>1 = `REQUEST_PRIORITY_1`<br>2 = `REQUEST_PRIORITY_2`<br>3 = `REQUEST_PRIORITY_3` | plausible |
| `HVP_packContVoltage` | page 2 | High-voltage processor (pack contactor and isolation controller): pack cont voltage | 4\|12 | little-endian | unsigned | 0.1 | 0 | V | 0 to 30 |  | plausible |
| `HVP_packNegativeV` | page 2 | The HVP's common-mode measurement of PACK-HV-SENSE-NEG relative to chassis ground | 16\|16 | little-endian | signed | 0.1 | 0 | V | -550 to 550 |  | plausible |
| `HVP_packPositiveV` | page 2 | The HVP's common-mode measurement of PACK-HV-SENSE-POS relative to chassis ground | 32\|16 | little-endian | signed | 0.1 | 0 | V | -550 to 550 |  | plausible |
| `HVP_pyroAnalog` | page 2 | High-voltage processor (pack contactor and isolation controller): pyro analog | 48\|12 | little-endian | unsigned | 0.1 | 0 | V | 0 to 3 |  | plausible |
| `HVP_fcContCoilCurrent` | page 4 | High-voltage processor (pack contactor and isolation controller): fc cont coil current | 4\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 7.5 |  | plausible |
| `HVP_fcContVoltage` | page 4 | High-voltage processor (pack contactor and isolation controller): fc cont voltage | 16\|12 | little-endian | unsigned | 0.1 | 0 | V | 0 to 30 |  | plausible |
| `HVP_hvilInVoltage` | page 4 | Measured HVIL input voltage | 28\|12 | little-endian | unsigned | 0.1 | 0 | V | 0 to 30 |  | plausible |
| `HVP_hvilOutVoltage` | page 4 | Measured HVIL output voltage | 40\|12 | little-endian | unsigned | 0.1 | 0 | V | 0 to 30 |  | plausible |
| `HVP_shuntGainInvalidCountDbg` | page 4 | High-voltage processor (pack contactor and isolation controller): shunt gain invalid count dbg | 56\|8 | little-endian | unsigned | 1 | 0 | counts | 0 to 255 |  | plausible |
| `HVP_fcLinkPositiveV` | page 5 | High-voltage processor (pack contactor and isolation controller): fc link positive v | 8\|16 | little-endian | signed | 0.1 | 0 | V | -550 to 550 |  | plausible |
| `HVP_packContCoilCurrent` | page 5 | High-voltage processor (pack contactor and isolation controller): pack cont coil current | 24\|12 | little-endian | unsigned | 0.1 | 0 | A | 0 to 7.5 |  | plausible |
| `HVP_battery12V` | page 5 | Monitored voltage sense of 12V battery | 36\|12 | little-endian | unsigned | 0.1 | 0 | V | 0 to 30 |  | plausible |
| `HVP_shuntRefVoltageDbg` | page 5 | High-voltage processor (pack contactor and isolation controller): shunt ref voltage dbg | 48\|16 | little-endian | signed | 0.001 | 0 | V | -32.768 to 32.767 |  | plausible |

## Multiplexing

`HVP_debugMessageMultiplexer` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (35 signals), page 2 (4 signals), page 4 (5 signals), page 5 (4 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All High-voltage processor (pack contactor and isolation controller) messages (HVP)](../../hvp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
