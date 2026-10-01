---
layout: default
title: "UMC_smartAdapterInfo (0x505) — UMC ECU, Tesla Model Y 2025.20.8 VEH CAN"
description: "UMC ECU message: smart adapter info. Tesla Model Y CAN bus message UMC_smartAdapterInfo (0x505) of UMC ECU, firmware 2025.20.8, 9 signals (SA_infoIndex, SA_genealogyVersion, SA_genealogyCrc, SA_region and 5 more). Bit layout, scaling, units and value tables."
---

# UMC_smartAdapterInfo (0x505) — UMC ECU, Tesla Model Y 2025.20.8 VEH CAN

UMC ECU message: smart adapter info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 9 signals of UMC_smartAdapterInfo as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UMC_smartAdapterInfo` |
| CAN id | 0x505 (1285) |
| ECU | [UMC ECU](../../umc.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | UMC |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 9 |

## Signals of UMC_smartAdapterInfo

Tesla Model Y CAN bus signals in `UMC_smartAdapterInfo`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `SA_infoIndex` | selector | UMC ECU: info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `Mux0`<br>11 = `Mux11`<br>25 = `Mux25`<br>26 = `Mux26`<br>27 = `Mux27`<br>29 = `Mux29`<br>30 = `Mux30`<br>31 = `Mux31`<br>32 = `Mux32` | plausible |
| `SA_genealogyVersion` | page 0 | UMC ECU: genealogy version | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | layout-only |
| `SA_genealogyCrc` | page 0 | UMC ECU: genealogy crc | 16\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | layout-only |
| `SA_region` | page 0 | Reports the smart adapter region from Electrically Erasable Programmable Read-Only Memory (EEPROM). | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `SA_REGION_NA`<br>1 = `SA_REGION_EU`<br>2 = `SA_REGION_CHINA`<br>3 = `SA_REGION_JAPAN`<br>4 = `SA_REGION_AUSTRALIA`<br>5 = `SA_REGION_SOUTH_KOREA`<br>6 = `SA_REGION_INDIA` | plausible |
| `SA_OverTempThreshold` | page 0 | Reports the smart adapter overtemperature threshold from Electrically Erasable Programmable Read-Only Memory (EEPROM). | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `SA_partNumInt` | page 31 | Reports the smart adapter part number integer representation. | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | plausible |
| `SA_partNumRev` | page 31 | Reports the smart adapter part number revision. | 40\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `SA_currentLimit` | page 31 | Reports the smart adapter current limit from Electrically Erasable Programmable Read-Only Memory (EEPROM). | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |
| `SA_l1Voltage` | page 31 | Reports the smart adapter nominal voltage request from Electrically Erasable Programmable Read-Only Memory (EEPROM). | 56\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | plausible |

## Multiplexing

`SA_infoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 0 (4 signals), page 31 (4 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All UMC ECU messages (UMC)](../../umc.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
