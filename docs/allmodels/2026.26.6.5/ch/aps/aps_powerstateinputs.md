---
layout: default
title: "APS_powerStateInputs (0x3E0) — Driver assistance computer (secondary), Tesla Model 3 / Model Y 2026.26.6.5 CH CAN"
description: "Driver assistance computer (secondary) message: power state inputs. Tesla Model 3 / Model Y CAN bus message APS_powerStateInputs (0x3E0) of Driver assistance computer (secondary), firmware 2026.26.6.5, 6 signals (APS_A_lowPowerRequest, APS_A_lowPowerRequestor, APS_A_forcePowerOffRequest, APS_B_lowPowerRequest and 2 more). Bit layout, scaling, units and value tables."
---

# APS_powerStateInputs (0x3E0) — Driver assistance computer (secondary), Tesla Model 3 / Model Y 2026.26.6.5 CH CAN

Driver assistance computer (secondary) message: power state inputs; frame length from the layout, not yet observed on a vehicle bus. This page documents the 6 signals of APS_powerStateInputs as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `APS_powerStateInputs` |
| CAN id | 0x3E0 (992) |
| ECU | [Driver assistance computer (secondary)](../../aps.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | CH (chassis CAN) |
| Transmitter | APS |
| Frame length | 3 bytes |
| Cycle time | 100 ms |
| Signals | 6 |

## Signals of APS_powerStateInputs

Tesla Model 3 / Model Y CAN bus signals in `APS_powerStateInputs`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APS_A_lowPowerRequest` | Indicates Autopilot Secondary Processor (APS) low power state request presence. | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `APS_LOW_POWER_NONE`<br>1 = `APS_LOW_POWER_SUSPEND`<br>2 = `APS_LOW_POWER_OFF`<br>3 = `APS_LOW_POWER_AP_WARM_RESET`<br>4 = `APS_LOW_POWER_SOC_WARM_RESET`<br>5 = `APS_LOW_POWER_COLD_RESET` | validated |
| `APS_A_lowPowerRequestor` | Indicates who initiated the Autopilot Secondary Processor (APS) low power request. | 4\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `APS_LOW_POWER_REQ_NONE`<br>1 = `APS_LOW_POWER_REQ_AP_ATF`<br>2 = `APS_LOW_POWER_REQ_AP_MAILBOX`<br>3 = `APS_LOW_POWER_REQ_SGK_POWER`<br>4 = `APS_LOW_POWER_REQ_SGK_FM`<br>5 = `APS_LOW_POWER_REQ_SGK_BRIDGE`<br>6 = `APS_LOW_POWER_REQ_SGK_UDS`<br>7 = `APS_LOW_POWER_REQ_SGK_SLEEP`<br>8 = `APS_LOW_POWER_REQ_SGK_CONSOLE`<br>9 = `APS_LOW_POWER_REQ_SGK_PGOOD_IRQ`<br>10 = `APS_LOW_POWER_REQ_COUNT` | validated |
| `APS_A_forcePowerOffRequest` | Driver assistance computer (secondary): a force power off request | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `APS_B_lowPowerRequest` | Indicates Autopilot Secondary Processor (APS) low power state request presence. | 9\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `APS_LOW_POWER_NONE`<br>1 = `APS_LOW_POWER_SUSPEND`<br>2 = `APS_LOW_POWER_OFF`<br>3 = `APS_LOW_POWER_AP_WARM_RESET`<br>4 = `APS_LOW_POWER_SOC_WARM_RESET`<br>5 = `APS_LOW_POWER_COLD_RESET` | validated |
| `APS_B_lowPowerRequestor` | Indicates who initiated the Autopilot Secondary Processor (APS) low power request. | 12\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `APS_LOW_POWER_REQ_NONE`<br>1 = `APS_LOW_POWER_REQ_AP_ATF`<br>2 = `APS_LOW_POWER_REQ_AP_MAILBOX`<br>3 = `APS_LOW_POWER_REQ_SGK_POWER`<br>4 = `APS_LOW_POWER_REQ_SGK_FM`<br>5 = `APS_LOW_POWER_REQ_SGK_BRIDGE`<br>6 = `APS_LOW_POWER_REQ_SGK_UDS`<br>7 = `APS_LOW_POWER_REQ_SGK_SLEEP`<br>8 = `APS_LOW_POWER_REQ_SGK_CONSOLE`<br>9 = `APS_LOW_POWER_REQ_SGK_PGOOD_IRQ`<br>10 = `APS_LOW_POWER_REQ_COUNT` | validated |
| `APS_B_forcePowerOffRequest` | Driver assistance computer (secondary): b force power off request | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 CH DBC file](../../../../../dbc/AllModels/2026.26.6.5/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/CH.json)

## See also

- [All Driver assistance computer (secondary) messages (APS)](../../aps.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
