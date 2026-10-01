---
layout: default
title: "UI_status (0x353) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 CH CAN"
description: "Touchscreen user interface computer message: status. Tesla Model 3 CAN bus message UI_status (0x353) of Touchscreen user interface computer, firmware 2025.20.8, 26 signals (UI_touchActive, UI_audioActive, UI_bluetoothActive, UI_cellActive and 22 more). Bit layout, scaling, units and value tables."
---

# UI_status (0x353) — Touchscreen user interface computer, Tesla Model 3 2025.20.8 CH CAN

Touchscreen user interface computer message: status; forwarded onto this bus by the gateway; frame length from the layout, not yet observed on a vehicle bus. This page documents the 26 signals of UI_status as defined for Tesla Model 3 firmware 2025.20.8 on the CH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `UI_status` |
| CAN id | 0x353 (851) |
| ECU | [Touchscreen user interface computer](../../ui.md) |
| Vehicle | Tesla Model 3 |
| Firmware | 2025.20.8 |
| Bus | CH (chassis CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 26 |

## Signals of UI_status

Tesla Model 3 CAN bus signals in `UI_status`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `UI_touchActive` | No touchscreen errors | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_audioActive` | Audio system is ready. | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_bluetoothActive` | Touchscreen user interface computer: bluetooth active | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_cellActive` | Cell is powered | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_displayReady` | UI is ready (GUI_allReady) and display is ok (GUI_displayHardwareOK) | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_displayOn` | UI display on/off status | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_wifiActive` | WiFi active. | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_wifiConnected` | WiFi Connected. | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_systemActive` | Touchscreen user interface computer: system active | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_readyForDrive` | Ready for drive (UI ready or self park request) | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_cellConnected` | Detects if the cell is connected to a network. | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_vpnActive` | VPN connected. | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_autopilotTrial` | Touchscreen user interface computer: autopilot trial | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `START`<br>2 = `STOP`<br>3 = `ACTIVE` | plausible |
| `UI_factoryReset` | UI request for factory reset; raw 0 = signal not available (SNA) | 14\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `NONE_SNA`<br>1 = `DEVELOPER`<br>2 = `DIAGNOSTIC`<br>3 = `CUSTOMER` | plausible |
| `UI_gpsActive` | GPS has valid fix | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_screenshotActive` | Touchscreen user interface computer: screenshot active | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_radioActive` | Touchscreen user interface computer: radio active | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_cellNetworkTechnology` | Describes the type of cellular network to which the car computer is connected: GPRS_2G(114Kbps) &lt; EGDE_2G(368Kbps) &lt; 3G(3Mbps) &lt; HSDPA_3G(14Mbps) &lt; HSPAplus_4Gg(168Mbps) &lt; 4G_LTE(299Mbps); raw 15 = signal not available (SNA) | 19\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 14 | 0 = `CELL_NETWORK_NONE`<br>1 = `CELL_NETWORK_GPRS`<br>2 = `CELL_NETWORK_EDGE`<br>3 = `CELL_NETWORK_UMTS`<br>4 = `CELL_NETWORK_HSDPA`<br>5 = `CELL_NETWORK_HSUPA`<br>6 = `CELL_NETWORK_HSPA`<br>7 = `CELL_NETWORK_LTE`<br>8 = `CELL_NETWORK_GSM`<br>9 = `CELL_NETWORK_CDMA`<br>10 = `CELL_NETWORK_WCDMA`<br>11 = `CELL_NETWORK_LTE5GCN`<br>12 = `CELL_NETWORK_5GNSA`<br>13 = `CELL_NETWORK_5GSA`<br>14 = `CELL_NETWORK_NGRAN`<br>15 = `CELL_NETWORK_SNA` | plausible |
| `UI_cellReceiverPower` | Touchscreen user interface computer: cell receiver power | 24\|8 | little-endian | unsigned | 1 | -128 | dB | -128 to 127 |  | plausible |
| `UI_falseTouchCounter` | Count false touches after display is off. | 32\|8 | little-endian | unsigned | 1 | 0 | 1 | 0 to 255 |  | plausible |
| `UI_developmentCar` | Touchscreen user interface computer: development car | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_cameraActive` | Touchscreen user interface computer: camera active | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | plausible |
| `UI_cellSignalBars` | Number of cellular signal bars displayed on the UI, derived from cellSignalStrength; raw 7 = signal not available (SNA) | 42\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `ZERO`<br>1 = `ONE`<br>2 = `TWO`<br>3 = `THREE`<br>4 = `FOUR`<br>5 = `FIVE`<br>7 = `SNA` | plausible |
| `UI_trailerModeTelltale` | Color of the trailer mode telltale | 45\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TRAILER_MODE_TELLTALE_OFF`<br>1 = `TRAILER_MODE_TELLTALE_BLUE`<br>2 = `TRAILER_MODE_TELLTALE_YELLOW`<br>3 = `TRAILER_MODE_TELLTALE_RED` | plausible |
| `UI_pcbTemperature` | PCB digital temp sensor reading in DegC | 48\|8 | little-endian | signed | 1 | 40 | degC | -20 to 100 |  | validated |
| `UI_cpuTemperature` | Apollo Lake SOC temperature in DegC | 56\|8 | little-endian | signed | 1 | 40 | degC | -20 to 100 |  | validated |

## Download the DBC file

- [Tesla Model 3 2025.20.8 CH DBC file](../../../../../dbc/Model3/2025.20.8/CH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/Model3/2025.20.8/CH.json)

## See also

- [All Touchscreen user interface computer messages (UI)](../../ui.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
