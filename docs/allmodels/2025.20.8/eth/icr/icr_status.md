---
layout: default
title: "ICR_status (0x7E7) — ICR ECU, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "ICR ECU message: status. Ethernet-side message ICR_status of ICR ECU for Tesla Model 3 / Model Y firmware 2025.20.8, 7 signals (ICR_sensorMode, ICR_blocked, ICR_algoVersion, ICR_l2HeapUsage and 3 more). Bit layout, scaling, units and value tables."
---

# ICR_status (0x7E7) — ICR ECU, Tesla Model 3 / Model Y 2025.20.8 ETH

ICR ECU message: status. This page documents the 7 signals of ICR_status as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `ICR_status` |
| Ethernet-side id | 0x7E7 (2023) |
| ECU | [ICR ECU](../../icr.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | ICR |
| Frame length | 5 bytes |
| Cycle time | 100 ms |
| Signals | 7 |

## Signals of ICR_status

Tesla Model 3 / Model Y CAN bus signals in `ICR_status`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `ICR_sensorMode` | ICR ECU: sensor mode | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `ICR_SENSOR_MODE_SENSOR_STOPPED`<br>1 = `ICR_SENSOR_MODE_INTRUSTION`<br>2 = `ICR_SENSOR_MODE_END_OF_LINE_TEST`<br>3 = `ICR_SENSOR_INTERFACE_MODE_CW`<br>4 = `ICR_SENSOR_INTERFACE_MODE_CALIBRATION`<br>5 = `ICR_SENSOR_INTERFACE_MODE_HPM_TEST`<br>6 = `ICR_SENSOR_INTERFACE_MODE_OCCUPANCY_DETECTION`<br>7 = `ICR_SENSOR_INTERFACE_MODE_LPM_TEST`<br>15 = `ICR_SENSOR_INTERFACE_MODE_ERROR` | plausible |
| `ICR_blocked` | Indicates if sensor is blocked or not; raw 0 = signal not available (SNA) | 8\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `ICR_BLOCKED_SNA`<br>1 = `ICR_BLOCKED_FALSE`<br>2 = `ICR_BLOCKED_TRUE` | plausible |
| `ICR_algoVersion` | ICR ECU: algo version | 10\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `ICR_ALGO_VERSION_NONE`<br>1 = `ICR_ALGO_VERSION_EXPERIMENTAL`<br>2 = `ICR_ALGO_VERSION_V204`<br>3 = `ICR_ALGO_VERSION_V711`<br>4 = `ICR_ALGO_VERSION_V715`<br>5 = `ICR_ALGO_VERSION_V803`<br>6 = `ICR_ALGO_VERSION_V826`<br>7 = `ICR_ALGO_VERSION_V902`<br>8 = `ICR_ALGO_VERSION_V927`<br>9 = `ICR_ALGO_VERSION_V1006`<br>10 = `ICR_ALGO_VERSION_V1013`<br>11 = `ICR_ALGO_VERSION_V1103`<br>12 = `ICR_ALGO_VERSION_V1118`<br>13 = `ICR_ALGO_VERSION_V1125`<br>14 = `ICR_ALGO_VERSION_V1222`<br>15 = `ICR_ALGO_VERSION_V04262023`<br>16 = `ICR_ALGO_VERSION_V05192023`<br>17 = `ICR_ALGO_VERSION_V06072023`<br>18 = `ICR_ALGO_VERSION_V06152023`<br>19 = `ICR_ALGO_VERSION_V07172023`<br>20 = `ICR_ALGO_VERSION_V08302023`<br>21 = `ICR_ALGO_VERSION_v09222023`<br>22 = `ICR_ALGO_VERSION_v10112023`<br>23 = `ICR_ALGO_VERSION_v10252023`<br>24 = `ICR_ALGO_VERSION_v12192023`<br>25 = `ICR_ALGO_VERSION_v01312024`<br>26 = `ICR_ALGO_VERSION_v03142024`<br>27 = `ICR_ALGO_VERSION_v04242024`<br>28 = `ICR_ALGO_VERSION_v06122024`<br>29 = `ICR_ALGO_VERSION_v07172024`<br>30 = `ICR_ALGO_VERSION_v08282024`<br>31 = `ICR_ALGO_VERSION_v10072024`<br>32 = `ICR_ALGO_VERSION_v01222025`<br>33 = `ICR_ALGO_VERSION_v02142025`<br>34 = `ICR_ALGO_VERSION_v03192025`<br>35 = `ICR_ALGO_VERSION_v04232025`<br>36 = `ICR_ALGO_VERSION_v06112025`<br>37 = `ICR_ALGO_VERSION_FUTURE_RELEASE_37` | plausible |
| `ICR_l2HeapUsage` | ICR ECU: l2 heap usage | 25\|7 | little-endian | unsigned | 1 | 0 | PCT | 0 to 127 |  | plausible |
| `ICR_intrusionStatus` | ICR ECU: intrusion status | 32\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INSTRUSION_STATUS_UNKNOWN`<br>1 = `INSTRUSION_STATUS_NONE`<br>2 = `INSTRUSION_STATUS_INTRUSION_DETECTED` | plausible |
| `ICR_booted` | Indicates if ICR has rebooted | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `ICR_rdMapDumpCompleted` | ICR ECU: rd map dump completed | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All ICR ECU messages (ICR)](../../icr.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
