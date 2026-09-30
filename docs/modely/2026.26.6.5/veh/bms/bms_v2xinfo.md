---
layout: default
title: "BMS_v2xInfo (0x42F) — High-voltage battery management system, Tesla Model Y 2026.26.6.5 VEH CAN"
description: "High-voltage battery management system message: v2x info. Tesla Model Y CAN bus message BMS_v2xInfo (0x42F) of High-voltage battery management system, firmware 2026.26.6.5, 5 signals (BMS_v2xSoe, BMS_v2xFullEnergy, BMS_v2xPackPower, BMS_acDischargeBlockedReason and 1 more). Bit layout, scaling, units and value tables."
---

# BMS_v2xInfo (0x42F) — High-voltage battery management system, Tesla Model Y 2026.26.6.5 VEH CAN

High-voltage battery management system message: v2x info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 5 signals of BMS_v2xInfo as defined for Tesla Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `BMS_v2xInfo` |
| CAN id | 0x42F (1071) |
| ECU | [High-voltage battery management system](../../bms.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | BMS |
| Frame length | 7 bytes |
| Cycle time | 1000 ms |
| Signals | 5 |

## Signals of BMS_v2xInfo

Tesla Model Y CAN bus signals in `BMS_v2xInfo`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `BMS_v2xSoe` | High-voltage battery management system: v2x soe; raw 65535 = signal not available (SNA) | 0\|16 | little-endian | unsigned | 0.002 | 0 | % | 0 to 100 | 65535 = `SNA` | validated |
| `BMS_v2xFullEnergy` | High-voltage battery management system: v2x full energy; raw 4095 = signal not available (SNA) | 16\|12 | little-endian | unsigned | 0.05 | 0 | kWh | 0 to 200 | 4095 = `SNA` | validated |
| `BMS_v2xPackPower` | High-voltage battery management system: v2x pack power; raw 511 = signal not available (SNA) | 32\|9 | little-endian | unsigned | 0.1 | -25 | kW | -25 to 25 | 511 = `SNA` | validated |
| `BMS_acDischargeBlockedReason` | The enumerated reason why the ECU is blocking AC discharge | 41\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `COND_NONE`<br>1 = `CP_MIA`<br>2 = `PCS_MIA`<br>3 = `CP_EMERGENCY_SHUTDOWN_REQUESTED`<br>4 = `PCS_EMERGENCY_SHUTDOWN_REQUESTED`<br>5 = `CP_FAULT_LINE_ASSERTED`<br>6 = `SYSTEM_DIRECTOR_FAULT_REQUESTED`<br>7 = `POWERSHARE_PROTECTION_TRIPPED`<br>10 = `CP_ESCALATED_SHUTDOWN_REQUESTED`<br>11 = `PCS_ESCALATED_SHUTDOWN_REQUESTED`<br>12 = `ABORT_CHARGE_ALERT_SET`<br>13 = `ABORT_SUPERDISCHARGE_ALERT_SET`<br>14 = `FC_LINK_NOT_ALLOWED_TO_ENERGIZE`<br>15 = `EVSE_NOT_COMPATIBLE`<br>16 = `FC_CONTACTORS_NOT_OPEN`<br>17 = `FC_CONTACTORS_NOT_CLOSED`<br>18 = `FC_LINK_NOT_READY`<br>19 = `STATE_TIMEOUT_EXPIRED`<br>20 = `EVSE_NOT_PRESENT`<br>21 = `EVSE_NOT_READY`<br>22 = `NOT_NEEDED_OR_WANTED`<br>23 = `CP_GRACEFUL_SHUTDOWN_REQUESTED`<br>24 = `PCS_GRACEFUL_SHUTDOWN_REQUESTED`<br>25 = `SYSTEM_NOT_POSSIBLE`<br>26 = `SYSTEM_NOT_ALLOWED`<br>27 = `CP_DISALLOWS`<br>28 = `PCS_DISALLOWS`<br>29 = `SYSTEM_NOT_ENABLED`<br>30 = `CP_NOT_READY`<br>31 = `CP_NOT_ENABLED`<br>32 = `PCS_NOT_ENABLED`<br>33 = `CP_INLET_STILL_ENERGIZED`<br>34 = `PCS_NOT_DISABLED`<br>35 = `AC_RELAYS_NOT_OPEN`<br>36 = `SOE_TOO_LOW`<br>37 = `FEATURE_DISABLED`<br>38 = `TEMP_TOO_LOW`<br>39 = `ALL_RETRIES_EXHAUSTED`<br>40 = `EVSE_OUTPUT_CURRENT_NOT_LOW`<br>41 = `PRECHARGE_NOT_COMPLETE` | validated |
| `BMS_backupTimeRemaining` | High-voltage battery management system: backup time remaining; raw 255 = signal not available (SNA) | 48\|8 | little-endian | unsigned | 1 | 0 | Hours | 0 to 254 | 255 = `SNA` | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/ModelY/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/VEH.json)

## See also

- [All High-voltage battery management system messages (BMS)](../../bms.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
