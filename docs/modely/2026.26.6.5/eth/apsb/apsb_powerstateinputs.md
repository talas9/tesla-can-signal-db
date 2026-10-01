---
layout: default
title: "APSB_powerStateInputs (0x3E0) — APSB ECU, Tesla Model Y 2026.26.6.5 ETH"
description: "APSB ECU message: power state inputs. Ethernet-side message APSB_powerStateInputs of APSB ECU for Tesla Model Y firmware 2026.26.6.5, 6 signals (APSB_A_lowPowerRequest, APSB_A_lowPowerRequestor, APSB_A_forcePowerOffRequest, APSB_B_lowPowerRequest and 2 more). Bit layout, scaling, units and value tables."
---

# APSB_powerStateInputs (0x3E0) — APSB ECU, Tesla Model Y 2026.26.6.5 ETH

APSB ECU message: power state inputs. This page documents the 6 signals of APSB_powerStateInputs as defined for Tesla Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `APSB_powerStateInputs` |
| Ethernet-side id | 0x3E0 (992) |
| ECU | [APSB ECU](../../apsb.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | APSB |
| Frame length | 3 bytes |
| Cycle time | 100 ms |
| Signals | 6 |

## Signals of APSB_powerStateInputs

Tesla Model Y CAN bus signals in `APSB_powerStateInputs`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `APSB_A_lowPowerRequest` | APSB ECU: a low power request | 0\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `APS_LOW_POWER_NONE`<br>1 = `APS_LOW_POWER_SUSPEND`<br>2 = `APS_LOW_POWER_OFF`<br>3 = `APS_LOW_POWER_AP_WARM_RESET`<br>4 = `APS_LOW_POWER_SOC_WARM_RESET`<br>5 = `APS_LOW_POWER_COLD_RESET` | plausible |
| `APSB_A_lowPowerRequestor` | APSB ECU: a low power requestor | 4\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `APS_LOW_POWER_REQ_NONE`<br>1 = `APS_LOW_POWER_REQ_AP_ATF`<br>2 = `APS_LOW_POWER_REQ_AP_MAILBOX`<br>3 = `APS_LOW_POWER_REQ_SGK_POWER`<br>4 = `APS_LOW_POWER_REQ_SGK_FM`<br>5 = `APS_LOW_POWER_REQ_SGK_BRIDGE`<br>6 = `APS_LOW_POWER_REQ_SGK_UDS`<br>7 = `APS_LOW_POWER_REQ_SGK_SLEEP`<br>8 = `APS_LOW_POWER_REQ_SGK_CONSOLE`<br>9 = `APS_LOW_POWER_REQ_SGK_PGOOD_IRQ`<br>10 = `APS_LOW_POWER_REQ_COUNT` | plausible |
| `APSB_A_forcePowerOffRequest` | APSB ECU: a force power off request | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `APSB_B_lowPowerRequest` | APSB ECU: b low power request | 9\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `APS_LOW_POWER_NONE`<br>1 = `APS_LOW_POWER_SUSPEND`<br>2 = `APS_LOW_POWER_OFF`<br>3 = `APS_LOW_POWER_AP_WARM_RESET`<br>4 = `APS_LOW_POWER_SOC_WARM_RESET`<br>5 = `APS_LOW_POWER_COLD_RESET` | plausible |
| `APSB_B_lowPowerRequestor` | APSB ECU: b low power requestor | 12\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `APS_LOW_POWER_REQ_NONE`<br>1 = `APS_LOW_POWER_REQ_AP_ATF`<br>2 = `APS_LOW_POWER_REQ_AP_MAILBOX`<br>3 = `APS_LOW_POWER_REQ_SGK_POWER`<br>4 = `APS_LOW_POWER_REQ_SGK_FM`<br>5 = `APS_LOW_POWER_REQ_SGK_BRIDGE`<br>6 = `APS_LOW_POWER_REQ_SGK_UDS`<br>7 = `APS_LOW_POWER_REQ_SGK_SLEEP`<br>8 = `APS_LOW_POWER_REQ_SGK_CONSOLE`<br>9 = `APS_LOW_POWER_REQ_SGK_PGOOD_IRQ`<br>10 = `APS_LOW_POWER_REQ_COUNT` | plausible |
| `APSB_B_forcePowerOffRequest` | APSB ECU: b force power off request | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/ModelY/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All APSB ECU messages (APSB)](../../apsb.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
