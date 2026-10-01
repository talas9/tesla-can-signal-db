---
layout: default
title: "HVP_contactorState (0x20A) — High-voltage processor (pack contactor and isolation controller), Tesla Model 3 2025.20.8 ETH"
description: "High-voltage processor (pack contactor and isolation controller) message: contactor state. Ethernet-side message HVP_contactorState of High-voltage processor (pack contactor and isolation controller) for Tesla Model 3 firmware 2025.20.8, 22 signals (HVP_packContNegativeState, HVP_packContPositiveState, HVP_fcContPositiveAuxOpen, HVP_fcContNegativeAuxOpen and 18 more). Bit layout, scaling, units and value tables."
---

# HVP_contactorState (0x20A) — High-voltage processor (pack contactor and isolation controller), Tesla Model 3 2025.20.8 ETH

High-voltage processor (pack contactor and isolation controller) message: contactor state. This page documents the 22 signals of HVP_contactorState as defined for Tesla Model 3 firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `HVP_contactorState` |
| Ethernet-side id | 0x20A (522) |
| ECU | [High-voltage processor (pack contactor and isolation controller)](../../hvp.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | HVP |
| Frame length | 6 bytes |
| Cycle time | 1000 ms |
| Signals | 22 |

## Signals of HVP_contactorState

Tesla Model 3 CAN bus signals in `HVP_contactorState`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `HVP_packContNegativeState` | High-voltage processor (pack contactor and isolation controller): pack cont negative state; raw 0 = signal not available (SNA) | 0\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `CONTACTOR_STATE_SNA`<br>1 = `CONTACTOR_STATE_OPEN`<br>2 = `CONTACTOR_STATE_PRECHARGE`<br>3 = `CONTACTOR_STATE_BLOCKED`<br>4 = `CONTACTOR_STATE_PULLED_IN`<br>5 = `CONTACTOR_STATE_OPENING`<br>6 = `CONTACTOR_STATE_ECONOMIZED`<br>7 = `CONTACTOR_STATE_WELDED` | plausible |
| `HVP_packContPositiveState` | Current state of positive pack contactor; raw 0 = signal not available (SNA) | 3\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `CONTACTOR_STATE_SNA`<br>1 = `CONTACTOR_STATE_OPEN`<br>2 = `CONTACTOR_STATE_PRECHARGE`<br>3 = `CONTACTOR_STATE_BLOCKED`<br>4 = `CONTACTOR_STATE_PULLED_IN`<br>5 = `CONTACTOR_STATE_OPENING`<br>6 = `CONTACTOR_STATE_ECONOMIZED`<br>7 = `CONTACTOR_STATE_WELDED` | plausible |
| `HVP_fcContPositiveAuxOpen` | High-voltage processor (pack contactor and isolation controller): fc cont positive aux open | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_fcContNegativeAuxOpen` | High-voltage processor (pack contactor and isolation controller): fc cont negative aux open | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_packContactorSetState` | The current state of the pack contactors; raw 0 = signal not available (SNA) | 8\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `CONTACTOR_SET_STATE_SNA`<br>1 = `CONTACTOR_SET_STATE_OPEN`<br>2 = `CONTACTOR_SET_STATE_CLOSING`<br>3 = `CONTACTOR_SET_STATE_BLOCKED`<br>4 = `CONTACTOR_SET_STATE_OPENING`<br>5 = `CONTACTOR_SET_STATE_CLOSED`<br>6 = `CONTACTOR_SET_STATE_PARTIAL_WELD`<br>7 = `CONTACTOR_SET_STATE_WELDED`<br>8 = `CONTACTOR_SET_STATE_POSITIVE_CLOSED`<br>9 = `CONTACTOR_SET_STATE_NEGATIVE_CLOSED` | plausible |
| `HVP_fcContNegativeState` | Current state of the negative FC contactor; raw 0 = signal not available (SNA) | 12\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `CONTACTOR_STATE_SNA`<br>1 = `CONTACTOR_STATE_OPEN`<br>2 = `CONTACTOR_STATE_PRECHARGE`<br>3 = `CONTACTOR_STATE_BLOCKED`<br>4 = `CONTACTOR_STATE_PULLED_IN`<br>5 = `CONTACTOR_STATE_OPENING`<br>6 = `CONTACTOR_STATE_ECONOMIZED`<br>7 = `CONTACTOR_STATE_WELDED` | plausible |
| `HVP_fcContPositiveState` | Current state of the positive FC contactor; raw 0 = signal not available (SNA) | 16\|3 | little-endian | unsigned | 1 | 0 |  | 1 to 7 | 0 = `CONTACTOR_STATE_SNA`<br>1 = `CONTACTOR_STATE_OPEN`<br>2 = `CONTACTOR_STATE_PRECHARGE`<br>3 = `CONTACTOR_STATE_BLOCKED`<br>4 = `CONTACTOR_STATE_PULLED_IN`<br>5 = `CONTACTOR_STATE_OPENING`<br>6 = `CONTACTOR_STATE_ECONOMIZED`<br>7 = `CONTACTOR_STATE_WELDED` | plausible |
| `HVP_fcContactorSetState` | The current state of the fast charge contactors; raw 0 = signal not available (SNA) | 19\|4 | little-endian | unsigned | 1 | 0 |  | 1 to 15 | 0 = `CONTACTOR_SET_STATE_SNA`<br>1 = `CONTACTOR_SET_STATE_OPEN`<br>2 = `CONTACTOR_SET_STATE_CLOSING`<br>3 = `CONTACTOR_SET_STATE_BLOCKED`<br>4 = `CONTACTOR_SET_STATE_OPENING`<br>5 = `CONTACTOR_SET_STATE_CLOSED`<br>6 = `CONTACTOR_SET_STATE_PARTIAL_WELD`<br>7 = `CONTACTOR_SET_STATE_WELDED`<br>8 = `CONTACTOR_SET_STATE_POSITIVE_CLOSED`<br>9 = `CONTACTOR_SET_STATE_NEGATIVE_CLOSED` | plausible |
| `HVP_fcCtrsRequestStatus` | Current status of FC contactor request | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `REQUEST_NOT_ACTIVE`<br>1 = `REQUEST_ACTIVE`<br>2 = `REQUEST_COMPLETED` | plausible |
| `HVP_fcCtrsResetRequestRequired` | High-voltage processor (pack contactor and isolation controller): fc ctrs reset request required | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_fcCtrsOpenNowRequested` | Flag indicated immediate-opening request of FC contactors | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `HVP_fcCtrsOpenRequested` | Flag indicating opening request of FC contactors | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `HVP_fcCtrsClosingAllowed` | Flag indicating closure allowance of FC contactors | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `HVP_packCtrsRequestStatus` | Current request status of pack contactors | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `REQUEST_NOT_ACTIVE`<br>1 = `REQUEST_ACTIVE`<br>2 = `REQUEST_COMPLETED` | plausible |
| `HVP_packCtrsResetRequestRequired` | High-voltage processor (pack contactor and isolation controller): pack ctrs reset request required | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_packCtrsOpenNowRequested` | Flag indicating immediate-opening request of pack contactors | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `HVP_packCtrsOpenRequested` | Flag indicating opening request of pack contactors | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `HVP_packCtrsClosingAllowed` | Flag indicating closure allowance of pack contactors | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `HVP_dcLinkAllowedToEnergize` | Indicates there should be no HV exposure if the FC link is energized by an internal or external source | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `HVP_pyroTestInProgress` | High-voltage processor (pack contactor and isolation controller): pyro test in progress | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `HVP_hvilDiag` | Diagnostic status of HVIL circuit, including specific FAULT types; raw 14 = signal not available (SNA) | 40\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `UNKNOWN`<br>1 = `OK`<br>2 = `CURRENT_SOURCE_OR_GROUND_LEAK_FAULT`<br>3 = `INTERNAL_OPEN_FAULT`<br>4 = `VEHICLE_OPEN_FAULT`<br>5 = `PENTHOUSE_LID_OPEN_FAULT`<br>6 = `UNKNOWN_LOCATION_OPEN_FAULT`<br>7 = `VEHICLE_NODE_FAULT`<br>8 = `NO_12V_SUPPLY`<br>9 = `VEHICLE_OR_PENTHOUSE_LID_OPEN_FAULT`<br>10 = `DI_STATUS_MISSING_FAULT`<br>11 = `PM_STATUS_MISSING_FAULT`<br>12 = `DI_OPEN_FAULT`<br>13 = `PM_OPEN_FAULT`<br>14 = `SNA` | validated |
| `HVP_fcLinkAllowedToEnergize` | The type of charge that is allowed to energize the FC link. Indicates that the HVP has disabled the dynamic FC weld check for DC charge, or has enabled the PCS charging hardware for AC charge | 44\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `FC_LINK_ENERGY_NONE`<br>1 = `FC_LINK_ENERGY_AC`<br>2 = `FC_LINK_ENERGY_DC` | plausible |

## Download the DBC file

- [Tesla Model 3 2025.20.8 ETH DBC file](../../../../../dbc/Model3/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All High-voltage processor (pack contactor and isolation controller) messages (HVP)](../../hvp.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
