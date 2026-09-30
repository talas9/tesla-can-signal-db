---
layout: default
title: "VCFRONT_LVHealthDebug (0x495) — Front body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Front body controller message: LV health debug. Tesla Model 3 / Model Y CAN bus message VCFRONT_LVHealthDebug (0x495) of Front body controller, firmware 2026.26.6.5, 19 signals (VCFRONT_LVHealthDebugIndex, VCFRONT_LVHEALTH_placeholder, VCFRONT_LVHEALTH_activeDecelEnergyWarning, VCFRONT_LVHEALTH_criticalPulloverEnergyWarning and 15 more). Bit layout, scaling, units and value tables."
---

# VCFRONT_LVHealthDebug (0x495) — Front body controller, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Front body controller message: LV health debug; frame length from the layout, not yet observed on a vehicle bus. This page documents the 19 signals of VCFRONT_LVHealthDebug as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCFRONT_LVHealthDebug` |
| CAN id | 0x495 (1173) |
| ECU | [Front body controller](../../vcfront.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCFRONT |
| Frame length | 6 bytes |
| Cycle time | 1000 ms |
| Signals | 19 |

## Signals of VCFRONT_LVHealthDebug

Tesla Model 3 / Model Y CAN bus signals in `VCFRONT_LVHealthDebug`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCFRONT_LVHealthDebugIndex` | selector | Front body controller: LV health debug index | 0\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNHEALTHY_REASONS`<br>1 = `FRONT_CHECK_RESULTS_1` | plausible |
| `VCFRONT_LVHEALTH_placeholder` | page 0 | Whether the LV health has determined that the &lt;placeholder&gt; | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_LVHEALTH_activeDecelEnergyWarning` | page 0 | Whether the VCFRONT cannot confirm that the battery has sufficient energy to support an active decel scenario | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_LVHEALTH_criticalPulloverEnergyWarning` | page 0 | Whether the VCFRONT cannot confirm that the battery has sufficient energy to support a critical pullover scenario | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_LVHEALTH_revBattEFuseOff` | page 0 | Whether the LV health has determined that the LVBMB EFuse has opened | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_LVHEALTH_LVBMBEFuseOpen` | page 0 | Whether the LV health has determined that the LVBMB EFuse has opened | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_LVHEALTH_lvBatteryCommsMia` | page 0 | Whether the LV health has determined that LV battery communications are missing | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_LVHEALTH_pcsEFuseOff` | page 0 | Whether VCFRONT has determined that the PCS eFuse is off or faulted when it's needed to be on | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_LVHEALTH_pcsNotActive` | page 0 | Whether the LV health has determined that the PCS is not actively providing LV support | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_LVHEALTH_pcsMIA` | page 0 | Whether the LV health has determined that messages are missing from PCS critical for determining health | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_LVHEALTH_IBSMIA` | page 0 | Whether the LV health has determined that the INA228 LV battery sensor signals are invalid or not yet configured | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_LVHEALTH_LVBatteryElecDisc` | page 0 | Whether the VCFRONT has determined that the LV battery is electrically disconnected | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_LVHEALTH_LVBatteryElecDiscUnknown` | page 0 | Whether the VCFRONT has determined that the LV battery electrical connection status has been unknown for too long | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_LVHEALTH_pcsOpenCircuit` | page 0 | Whether VCFRONT has determined that the electrical connection between the PCS and VCFRONT is disconnected | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_LVHEALTH_activeDecelPowerWarning` | page 0 | Whether the VCFRONT cannot confirm that the battery has sufficient power to support a active decel scenario | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_LVHEALTH_lvBatteryCapabilityLowAccuracy` | page 0 | Whether the LV health has determined that LV battery power/energy capability estimation accuracy is too low | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_LVHEALTH_lvBatteryConfiguration` | page 0 | Whether the LV health has determined that LV battery configuration is incorrect | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_LVHEALTH_lvBatteryImpedance` | page 0 | Whether the LV health has determined that LV battery impedance is too high | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCFRONT_LVHEALTH_lvBatteryExtendedOverVoltage` | page 0 | Whether the LV health has determined that an extended over voltage event has occurred | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Multiplexing

`VCFRONT_LVHealthDebugIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (18 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Front body controller messages (VCFRONT)](../../vcfront.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
