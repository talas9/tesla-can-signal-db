---
layout: default
title: "UI_status3 (0x3DA) — Touchscreen user interface computer, Tesla Model Y 2026.26.6.5 ETH"
description: "Touchscreen user interface computer message: status3. Ethernet-side message UI_status3 of Touchscreen user interface computer for Tesla Model Y firmware 2026.26.6.5, 2 signals (UI_wifiRegDomain, UI_wifiTethered). Bit layout, scaling, units and value tables."
---

# UI_status3 (0x3DA) — Touchscreen user interface computer, Tesla Model Y 2026.26.6.5 ETH

Touchscreen user interface computer message: status3. This page documents the 2 signals of UI_status3 as defined for Tesla Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `UI_status3` |
| Ethernet-side id | 0x3DA (986) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | UI |
| Frame length | 1 bytes |
| Cycle time | 1000 ms |
| Signals | 2 |

## Signals of UI_status3

Tesla Model Y CAN bus signals in `UI_status3`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_wifiRegDomain` | Indicates the Wi-Fi regulatory domain. | 0\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 | 0 = `UNKNOWN`<br>1 = `US`<br>2 = `CA`<br>3 = `DE`<br>4 = `FR`<br>5 = `IT`<br>6 = `NL`<br>7 = `AT`<br>8 = `BE`<br>9 = `DK`<br>10 = `NO`<br>11 = `CH`<br>12 = `SE`<br>13 = `UK`<br>14 = `CN`<br>15 = `HK`<br>16 = `JP`<br>17 = `AU`<br>18 = `IL`<br>19 = `GB`<br>20 = `RU`<br>21 = `KR`<br>22 = `TW`<br>23 = `MX`<br>24 = `JO`<br>25 = `SG`<br>26 = `TH`<br>27 = `MY`<br>28 = `CL`<br>29 = `QA`<br>30 = `CO`<br>31 = `PH`<br>32 = `SA`<br>33 = `MO`<br>34 = `NZ`<br>35 = `CZ`<br>36 = `HR`<br>37 = `FI`<br>38 = `GR`<br>39 = `HU`<br>40 = `PL`<br>41 = `PR`<br>42 = `RO`<br>43 = `SK`<br>44 = `SI`<br>45 = `ES`<br>46 = `TR`<br>47 = `AE`<br>48 = `IS`<br>49 = `IE`<br>50 = `IN`<br>51 = `BR`<br>52 = `BG`<br>53 = `EE`<br>54 = `LU`<br>55 = `MU`<br>56 = `PT`<br>57 = `AD`<br>58 = `CY`<br>59 = `GI`<br>60 = `LI`<br>61 = `LT`<br>62 = `LV`<br>63 = `MT`<br>64 = `MS`<br>65 = `SM`<br>66 = `SR`<br>67 = `AZ` | validated |
| `UI_wifiTethered` | Monitors whether Wi-Fi is connected while driving. | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/ModelY/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
