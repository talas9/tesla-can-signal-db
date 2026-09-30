---
layout: default
title: "VCSEC_BLEEndpointInfo (0x3C9) — Vehicle security controller, Tesla Model Y 2025.20.8 VEH CAN"
description: "Vehicle security controller message: BLE endpoint info. Tesla Model Y CAN bus message VCSEC_BLEEndpointInfo (0x3C9) of Vehicle security controller, firmware 2025.20.8, 93 signals (VCSEC_BLEEndpointInfoIndex, VCSEC_BLECENTERComponentID, VCSEC_BLECENTERPcbaID, VCSEC_BLECENTERAssemblyID and 89 more). Bit layout, scaling, units and value tables."
---

# VCSEC_BLEEndpointInfo (0x3C9) — Vehicle security controller, Tesla Model Y 2025.20.8 VEH CAN

Vehicle security controller message: BLE endpoint info; frame length from the layout, not yet observed on a vehicle bus. This page documents the 93 signals of VCSEC_BLEEndpointInfo as defined for Tesla Model Y firmware 2025.20.8 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `VCSEC_BLEEndpointInfo` |
| CAN id | 0x3C9 (969) |
| ECU | [Vehicle security controller](../../vcsec.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | VEH (vehicle CAN) |
| Transmitter | VCSEC |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 93 |

## Signals of VCSEC_BLEEndpointInfo

Tesla Model Y CAN bus signals in `VCSEC_BLEEndpointInfo`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `VCSEC_BLEEndpointInfoIndex` | selector | Vehicle security controller: BLE endpoint info index | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 0 = `BLECenterAppGithash`<br>1 = `BLECenterGeneology`<br>2 = `BLECenterInfo`<br>3 = `BLELeftAppGithash`<br>4 = `BLELeftGeneology`<br>5 = `BLELeftInfo`<br>6 = `BLERightAppGithash`<br>7 = `BLERightGeneology`<br>8 = `BLERightInfo`<br>9 = `BLERearAppGithash`<br>10 = `BLERearGeneology`<br>11 = `BLERearInfo`<br>12 = `UWBRightInfo`<br>13 = `UWBRightGeneology`<br>14 = `UWBRightAppGithash`<br>15 = `UWBRearRightInfo`<br>16 = `UWBRearRightGeneology`<br>17 = `UWBRearRightAppGithash`<br>18 = `UWBRearLeftInfo`<br>19 = `UWBRearLeftGeneology`<br>20 = `UWBRearLeftAppGithash`<br>21 = `UWBRearInfo`<br>22 = `UWBRearGeneology`<br>23 = `UWBRearAppGithash`<br>24 = `UWBLeftInfo`<br>25 = `UWBLeftGeneology`<br>26 = `UWBLeftAppGithash`<br>27 = `UWBCenterInfo`<br>28 = `UWBCenterGeneology`<br>29 = `UWBCenterAppGithash`<br>30 = `BLERightRearInfo`<br>31 = `BLERightRearGeneology`<br>32 = `BLERightRearAppGithash`<br>33 = `BLENFCCradleInfo`<br>34 = `BLENFCCradleGeneology`<br>35 = `BLENFCCradleAppGithash`<br>36 = `BLELeftRearInfo`<br>37 = `BLELeftRearGeneology`<br>38 = `BLELeftRearAppGithash`<br>127 = `MAX_VALUE_FOR_COEX` | plausible |
| `VCSEC_BLECENTERComponentID` | page 1 | Vehicle security controller: BLECENTER component ID | 8\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_BLECENTERPcbaID` | page 1 | Vehicle security controller: BLECENTER pcba ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_BLECENTERAssemblyID` | page 1 | Vehicle security controller: BLECENTER assembly ID | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_BLECENTERUsageID` | page 1 | Vehicle security controller: BLECENTER usage ID | 40\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_BLECENTERCrc` | page 2 | Vehicle security controller: BLECENTER crc | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_BLELEFTAppGitHashByte` | page 3 | Vehicle security controller: BLELEFT app git hash byte | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | validated |
| `VCSEC_BLELEFTComponentID` | page 4 | Vehicle security controller: BLELEFT component ID | 8\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_BLELEFTPcbaID` | page 4 | Vehicle security controller: BLELEFT pcba ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_BLELEFTAssemblyID` | page 4 | Vehicle security controller: BLELEFT assembly ID | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_BLELEFTUsageID` | page 4 | Vehicle security controller: BLELEFT usage ID | 40\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_BLELEFTCrc` | page 5 | Vehicle security controller: BLELEFT crc | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_BLERIGHTAppGitHashByte` | page 6 | Vehicle security controller: BLERIGHT app git hash byte | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | validated |
| `VCSEC_BLERIGHTComponentID` | page 7 | Vehicle security controller: BLERIGHT component ID | 8\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_BLERIGHTPcbaID` | page 7 | Vehicle security controller: BLERIGHT pcba ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_BLERIGHTAssemblyID` | page 7 | Vehicle security controller: BLERIGHT assembly ID | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_BLERIGHTUsageID` | page 7 | Vehicle security controller: BLERIGHT usage ID | 40\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_BLERIGHTCrc` | page 8 | Vehicle security controller: BLERIGHT crc | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_BLEREARAppGitHashByte` | page 9 | Vehicle security controller: BLEREAR app git hash byte | 8\|56 | little-endian | unsigned | 1 | 0 |  | 0 to 7.20575940379e+16 |  | validated |
| `VCSEC_BLEREARComponentID` | page 10 | Vehicle security controller: BLEREAR component ID | 8\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_BLEREARPcbaID` | page 10 | Vehicle security controller: BLEREAR pcba ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_BLEREARAssemblyID` | page 10 | Vehicle security controller: BLEREAR assembly ID | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_BLEREARUsageID` | page 10 | Vehicle security controller: BLEREAR usage ID | 40\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_BLEREARCrc` | page 11 | Vehicle security controller: BLEREAR crc | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_UWBRightCrc` | page 12 | Vehicle security controller: UWB right crc | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_UWBRightRadioConfigState` | page 12 | Vehicle security controller: UWB right radio config state | 40\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `WAIT_FOR_TRIGGER`<br>1 = `WAIT_AFTER_TRIGGER`<br>2 = `GET_CURRENT_CRC`<br>3 = `WAIT_TO_GET_CURRENT_CRC`<br>4 = `PREPARE_UPDATE`<br>5 = `INIT_CONFIGURATION`<br>6 = `WAIT_FOR_INIT_CONFIGURATION`<br>7 = `DOWNLOAD_DATA`<br>8 = `WAIT_FOR_DOWNLOAD_DATA`<br>9 = `PROGRAM_FLASH`<br>10 = `WAIT_FOR_PROGRAM_FLASH`<br>11 = `START_LOOPBACK_CALIBRATION`<br>12 = `WAIT_FOR_LOOPBACK_CALIBRATION`<br>13 = `DONE_VERIFYING_RADIO_CONFIG` | validated |
| `VCSEC_UWBRightUpdateStatus` | page 12 | Vehicle security controller: UWB right update status; raw 7 = signal not available (SNA) | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `NOT_STARTED`<br>1 = `UP_TO_DATE`<br>2 = `FAIL`<br>3 = `IN_PROGRESS`<br>7 = `SNA` | validated |
| `VCSEC_UWBRightRetryLimitReached` | page 12 | Vehicle security controller: UWB right retry limit reached | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_UWBRightDspVersion` | page 12 | Vehicle security controller: UWB right dsp version | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_UWBRightComponentID` | page 13 | Vehicle security controller: UWB right component ID | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_UWBRightPcbaID` | page 13 | Vehicle security controller: UWB right pcba ID | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_UWBRightAssemblyID` | page 13 | Vehicle security controller: UWB right assembly ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_UWBRightUsageID` | page 13 | Vehicle security controller: UWB right usage ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_UWBRearRightCrc` | page 15 | Vehicle security controller: UWB rear right crc | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_UWBRearRightRadioConfigState` | page 15 | Vehicle security controller: UWB rear right radio config state | 40\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `WAIT_FOR_TRIGGER`<br>1 = `WAIT_AFTER_TRIGGER`<br>2 = `GET_CURRENT_CRC`<br>3 = `WAIT_TO_GET_CURRENT_CRC`<br>4 = `PREPARE_UPDATE`<br>5 = `INIT_CONFIGURATION`<br>6 = `WAIT_FOR_INIT_CONFIGURATION`<br>7 = `DOWNLOAD_DATA`<br>8 = `WAIT_FOR_DOWNLOAD_DATA`<br>9 = `PROGRAM_FLASH`<br>10 = `WAIT_FOR_PROGRAM_FLASH`<br>11 = `START_LOOPBACK_CALIBRATION`<br>12 = `WAIT_FOR_LOOPBACK_CALIBRATION`<br>13 = `DONE_VERIFYING_RADIO_CONFIG` | validated |
| `VCSEC_UWBRearRightUpdateStatus` | page 15 | Vehicle security controller: UWB rear right update status; raw 7 = signal not available (SNA) | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `NOT_STARTED`<br>1 = `UP_TO_DATE`<br>2 = `FAIL`<br>3 = `IN_PROGRESS`<br>7 = `SNA` | validated |
| `VCSEC_UWBRearRightRetryLimitReached` | page 15 | Vehicle security controller: UWB rear right retry limit reached | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_UWBRearRightDspVersion` | page 15 | Vehicle security controller: UWB rear right dsp version | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_UWBRearRightComponentID` | page 16 | Vehicle security controller: UWB rear right component ID | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_UWBRearRightPcbaID` | page 16 | Vehicle security controller: UWB rear right pcba ID | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_UWBRearRightAssemblyID` | page 16 | Vehicle security controller: UWB rear right assembly ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_UWBRearRightUsageID` | page 16 | Vehicle security controller: UWB rear right usage ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_UWBRearLeftCrc` | page 18 | Vehicle security controller: UWB rear left crc | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_UWBRearLeftRadioConfigState` | page 18 | Vehicle security controller: UWB rear left radio config state | 40\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `WAIT_FOR_TRIGGER`<br>1 = `WAIT_AFTER_TRIGGER`<br>2 = `GET_CURRENT_CRC`<br>3 = `WAIT_TO_GET_CURRENT_CRC`<br>4 = `PREPARE_UPDATE`<br>5 = `INIT_CONFIGURATION`<br>6 = `WAIT_FOR_INIT_CONFIGURATION`<br>7 = `DOWNLOAD_DATA`<br>8 = `WAIT_FOR_DOWNLOAD_DATA`<br>9 = `PROGRAM_FLASH`<br>10 = `WAIT_FOR_PROGRAM_FLASH`<br>11 = `START_LOOPBACK_CALIBRATION`<br>12 = `WAIT_FOR_LOOPBACK_CALIBRATION`<br>13 = `DONE_VERIFYING_RADIO_CONFIG` | validated |
| `VCSEC_UWBRearLeftUpdateStatus` | page 18 | Vehicle security controller: UWB rear left update status; raw 7 = signal not available (SNA) | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `NOT_STARTED`<br>1 = `UP_TO_DATE`<br>2 = `FAIL`<br>3 = `IN_PROGRESS`<br>7 = `SNA` | validated |
| `VCSEC_UWBRearLeftRetryLimitReached` | page 18 | Vehicle security controller: UWB rear left retry limit reached | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_UWBRearLeftDspVersion` | page 18 | Vehicle security controller: UWB rear left dsp version | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_UWBRearLeftComponentID` | page 19 | Vehicle security controller: UWB rear left component ID | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_UWBRearLeftPcbaID` | page 19 | Vehicle security controller: UWB rear left pcba ID | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_UWBRearLeftAssemblyID` | page 19 | Vehicle security controller: UWB rear left assembly ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_UWBRearLeftUsageID` | page 19 | Vehicle security controller: UWB rear left usage ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_UWBRearCrc` | page 21 | Vehicle security controller: UWB rear crc | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_UWBRearRadioConfigState` | page 21 | Vehicle security controller: UWB rear radio config state | 40\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `WAIT_FOR_TRIGGER`<br>1 = `WAIT_AFTER_TRIGGER`<br>2 = `GET_CURRENT_CRC`<br>3 = `WAIT_TO_GET_CURRENT_CRC`<br>4 = `PREPARE_UPDATE`<br>5 = `INIT_CONFIGURATION`<br>6 = `WAIT_FOR_INIT_CONFIGURATION`<br>7 = `DOWNLOAD_DATA`<br>8 = `WAIT_FOR_DOWNLOAD_DATA`<br>9 = `PROGRAM_FLASH`<br>10 = `WAIT_FOR_PROGRAM_FLASH`<br>11 = `START_LOOPBACK_CALIBRATION`<br>12 = `WAIT_FOR_LOOPBACK_CALIBRATION`<br>13 = `DONE_VERIFYING_RADIO_CONFIG` | validated |
| `VCSEC_UWBRearUpdateStatus` | page 21 | Vehicle security controller: UWB rear update status; raw 7 = signal not available (SNA) | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `NOT_STARTED`<br>1 = `UP_TO_DATE`<br>2 = `FAIL`<br>3 = `IN_PROGRESS`<br>7 = `SNA` | validated |
| `VCSEC_UWBRearRetryLimitReached` | page 21 | Vehicle security controller: UWB rear retry limit reached | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_UWBRearDspVersion` | page 21 | Vehicle security controller: UWB rear dsp version | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_UWBRearComponentID` | page 22 | Vehicle security controller: UWB rear component ID | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_UWBRearPcbaID` | page 22 | Vehicle security controller: UWB rear pcba ID | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_UWBRearAssemblyID` | page 22 | Vehicle security controller: UWB rear assembly ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_UWBRearUsageID` | page 22 | Vehicle security controller: UWB rear usage ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_UWBLeftCrc` | page 24 | Vehicle security controller: UWB left crc | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_UWBLeftRadioConfigState` | page 24 | Vehicle security controller: UWB left radio config state | 40\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `WAIT_FOR_TRIGGER`<br>1 = `WAIT_AFTER_TRIGGER`<br>2 = `GET_CURRENT_CRC`<br>3 = `WAIT_TO_GET_CURRENT_CRC`<br>4 = `PREPARE_UPDATE`<br>5 = `INIT_CONFIGURATION`<br>6 = `WAIT_FOR_INIT_CONFIGURATION`<br>7 = `DOWNLOAD_DATA`<br>8 = `WAIT_FOR_DOWNLOAD_DATA`<br>9 = `PROGRAM_FLASH`<br>10 = `WAIT_FOR_PROGRAM_FLASH`<br>11 = `START_LOOPBACK_CALIBRATION`<br>12 = `WAIT_FOR_LOOPBACK_CALIBRATION`<br>13 = `DONE_VERIFYING_RADIO_CONFIG` | validated |
| `VCSEC_UWBLeftUpdateStatus` | page 24 | Vehicle security controller: UWB left update status; raw 7 = signal not available (SNA) | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `NOT_STARTED`<br>1 = `UP_TO_DATE`<br>2 = `FAIL`<br>3 = `IN_PROGRESS`<br>7 = `SNA` | validated |
| `VCSEC_UWBLeftRetryLimitReached` | page 24 | Vehicle security controller: UWB left retry limit reached | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_UWBLeftDspVersion` | page 24 | Vehicle security controller: UWB left dsp version | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_UWBLeftComponentID` | page 25 | Vehicle security controller: UWB left component ID | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_UWBLeftPcbaID` | page 25 | Vehicle security controller: UWB left pcba ID | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_UWBLeftAssemblyID` | page 25 | Vehicle security controller: UWB left assembly ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_UWBLeftUsageID` | page 25 | Vehicle security controller: UWB left usage ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_UWBCenterCrc` | page 27 | Vehicle security controller: UWB center crc | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_UWBCenterRadioConfigState` | page 27 | Vehicle security controller: UWB center radio config state | 40\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `WAIT_FOR_TRIGGER`<br>1 = `WAIT_AFTER_TRIGGER`<br>2 = `GET_CURRENT_CRC`<br>3 = `WAIT_TO_GET_CURRENT_CRC`<br>4 = `PREPARE_UPDATE`<br>5 = `INIT_CONFIGURATION`<br>6 = `WAIT_FOR_INIT_CONFIGURATION`<br>7 = `DOWNLOAD_DATA`<br>8 = `WAIT_FOR_DOWNLOAD_DATA`<br>9 = `PROGRAM_FLASH`<br>10 = `WAIT_FOR_PROGRAM_FLASH`<br>11 = `START_LOOPBACK_CALIBRATION`<br>12 = `WAIT_FOR_LOOPBACK_CALIBRATION`<br>13 = `DONE_VERIFYING_RADIO_CONFIG` | validated |
| `VCSEC_UWBCenterUpdateStatus` | page 27 | Vehicle security controller: UWB center update status; raw 7 = signal not available (SNA) | 44\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `NOT_STARTED`<br>1 = `UP_TO_DATE`<br>2 = `FAIL`<br>3 = `IN_PROGRESS`<br>7 = `SNA` | validated |
| `VCSEC_UWBCenterRetryLimitReached` | page 27 | Vehicle security controller: UWB center retry limit reached | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | validated |
| `VCSEC_UWBCenterDspVersion` | page 27 | Vehicle security controller: UWB center dsp version | 48\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_UWBCenterComponentID` | page 28 | Vehicle security controller: UWB center component ID | 8\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_UWBCenterPcbaID` | page 28 | Vehicle security controller: UWB center pcba ID | 16\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_UWBCenterAssemblyID` | page 28 | Vehicle security controller: UWB center assembly ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_UWBCenterUsageID` | page 28 | Vehicle security controller: UWB center usage ID | 32\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_BLERIGHTREARCrc` | page 30 | Vehicle security controller: BLERIGHTREAR crc | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_BLERIGHTREARComponentID` | page 31 | Vehicle security controller: BLERIGHTREAR component ID | 8\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_BLERIGHTREARPcbaID` | page 31 | Vehicle security controller: BLERIGHTREAR pcba ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_BLERIGHTREARAssemblyID` | page 31 | Vehicle security controller: BLERIGHTREAR assembly ID | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_BLERIGHTREARUsageID` | page 31 | Vehicle security controller: BLERIGHTREAR usage ID | 40\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_BLENFCCRADLECrc` | page 33 | Vehicle security controller: BLENFCCRADLE crc | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_BLENFCCRADLEComponentID` | page 34 | Vehicle security controller: BLENFCCRADLE component ID | 8\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_BLENFCCRADLEPcbaID` | page 34 | Vehicle security controller: BLENFCCRADLE pcba ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_BLENFCCRADLEAssemblyID` | page 34 | Vehicle security controller: BLENFCCRADLE assembly ID | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_BLENFCCRADLEUsageID` | page 34 | Vehicle security controller: BLENFCCRADLE usage ID | 40\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_BLELEFTREARCrc` | page 36 | Vehicle security controller: BLELEFTREAR crc | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `VCSEC_BLELEFTREARComponentID` | page 37 | Vehicle security controller: BLELEFTREAR component ID | 8\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `VCSEC_BLELEFTREARPcbaID` | page 37 | Vehicle security controller: BLELEFTREAR pcba ID | 24\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_BLELEFTREARAssemblyID` | page 37 | Vehicle security controller: BLELEFTREAR assembly ID | 32\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `VCSEC_BLELEFTREARUsageID` | page 37 | Vehicle security controller: BLELEFTREAR usage ID | 40\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |

## Multiplexing

`VCSEC_BLEEndpointInfoIndex` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (4 signals), page 2 (1 signals), page 3 (1 signals), page 4 (4 signals), page 5 (1 signals), page 6 (1 signals), page 7 (4 signals), page 8 (1 signals), page 9 (1 signals), page 10 (4 signals), page 11 (1 signals), page 12 (5 signals), page 13 (4 signals), page 15 (5 signals), page 16 (4 signals), page 18 (5 signals), page 19 (4 signals), page 21 (5 signals), page 22 (4 signals), page 24 (5 signals), page 25 (4 signals), page 27 (5 signals), page 28 (4 signals), page 30 (1 signals), page 31 (4 signals), page 33 (1 signals), page 34 (4 signals), page 36 (1 signals), page 37 (4 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model Y 2025.20.8 VEH DBC file](../../../../../dbc/ModelY/2025.20.8/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/VEH.json)

## See also

- [All Vehicle security controller messages (VCSEC)](../../vcsec.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
