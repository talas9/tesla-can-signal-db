---
layout: default
title: "DIR_alertMatrix2 (0x3B5) — Rear drive inverter, Tesla Model Y 2025.20.8 ETH"
description: "Rear drive inverter message: alert matrix2. Ethernet-side message DIR_alertMatrix2 of Rear drive inverter for Tesla Model Y firmware 2025.20.8, 55 signals (DIR_a065_canHardwareBusB, DIR_a066_canDataBusB, DIR_a067_canOverrunBusB, DIR_a069_rotorTempLimit and 51 more). Bit layout, scaling, units and value tables."
---

# DIR_alertMatrix2 (0x3B5) — Rear drive inverter, Tesla Model Y 2025.20.8 ETH

Rear drive inverter message: alert matrix2. This page documents the 55 signals of DIR_alertMatrix2 as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DIR_alertMatrix2` |
| Ethernet-side id | 0x3B5 (949) |
| ECU | [Rear drive inverter](../../dir.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DIR |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 55 |

## Signals of DIR_alertMatrix2

Tesla Model Y CAN bus signals in `DIR_alertMatrix2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIR_a065_canHardwareBusB` | Rear drive inverter: a065 can hardware bus b | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a066_canDataBusB` | Rear drive inverter: a066 can data bus b | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a067_canOverrunBusB` | Rear drive inverter: a067 can overrun bus b | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a069_rotorTempLimit` | Rear drive inverter: a069 rotor temp limit | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a070_udsTransactionInitiated` | Rear drive inverter: a070 uds transaction initiated | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a071_busDisconnected` | Rear drive inverter: a071 bus disconnected | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a072_gateDriveFaultCounter` | Rear drive inverter: a072 gate drive fault counter | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a073_motorSpeed` | Rear drive inverter: a073 motor speed | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a074_motorEncoder` | Rear drive inverter: a074 motor encoder | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a075_motorSpeedMismatch` | Rear drive inverter: a075 motor speed mismatch | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a076_lvSupplyOV` | Rear drive inverter: a076 lv supply OV | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a077_lvSupplyUV` | Rear drive inverter: a077 lv supply UV | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a078_adcRefLow` | Rear drive inverter: a078 adc ref low | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a079_adcRefHigh` | Rear drive inverter: a079 adc ref high | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a080_adcInfo` | Rear drive inverter: a080 adc info | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a081_P0BFF_DIR_EM_CurrentHigh` | Rear drive inverter: a081 P0 BFF DIR EM current high | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a082_P0F45_DIR_ECU_DemoTimer` | Rear drive inverter: a082 P0 F45 DIR ECU demo timer | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a083_P98B3_DIR_ECU_DemoWindow` | Rear drive inverter: a083 P98 B3 DIR ECU demo window | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a084_eccTestData0` | Rear drive inverter: a084 ecc test data0 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a086_activeDischargeOn` | Rear drive inverter: a086 active discharge on | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a087_gtwMIA` | Rear drive inverter: a087 gtw MIA | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a088_uiMIA` | Rear drive inverter: a088 ui MIA | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a090_pmMIA` | Rear drive inverter: a090 pm MIA | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a091_espMIA` | Rear drive inverter: a091 esp MIA | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a092_bmsMIA` | Rear drive inverter: a092 bms MIA | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a093_canHardwareBusA` | Rear drive inverter: a093 can hardware bus a | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a094_canDataBusA` | Rear drive inverter: a094 can data bus a | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a095_canOverrunBusA` | Rear drive inverter: a095 can overrun bus a | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a096_memoryError` | Rear drive inverter: a096 memory error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a097_eepromError` | Rear drive inverter: a097 eeprom error | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a098_intTimeTooLong` | Rear drive inverter: a098 int time too long | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a099_threadOverrun` | Rear drive inverter: a099 thread overrun | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a100_assertion` | Rear drive inverter: a100 assertion | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a101_eccTestData1` | Rear drive inverter: a101 ecc test data1 | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a102_exceptionPrefetchAbort` | Rear drive inverter: a102 exception prefetch abort | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a103_lowFlow` | Rear drive inverter: a103 low flow | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a107_fpgaError` | Rear drive inverter: a107 fpga error | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a108_stateTrans` | Rear drive inverter: a108 state trans | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a109_ahbWriteError` | Rear drive inverter: a109 ahb write error | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a110_brakeMIA` | Rear drive inverter: a110 brake MIA | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a111_badPhaseSensorCalib` | Rear drive inverter: a111 bad phase sensor calib | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a112_noPhaseCurrent` | Rear drive inverter: a112 no phase current | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a113_noFuncHeatsinkSensor` | Rear drive inverter: a113 no func heatsink sensor | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a114_exceptionDataAbort` | Rear drive inverter: a114 exception data abort | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a115_exceptionDataAbort2` | Rear drive inverter: a115 exception data abort2 | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a116_highSpeedWearCounter` | Rear drive inverter: a116 high speed wear counter | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a117_diMIA` | Rear drive inverter: a117 di MIA | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a119_hvpMIA` | Rear drive inverter: a119 hvp MIA | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a120_hvlinkMIA` | Rear drive inverter: a120 hvlink MIA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a121_motorControlRegulation` | Rear drive inverter: a121 motor control regulation | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a122_highStackUsage` | Rear drive inverter: a122 high stack usage | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a123_lossMotorControl` | Rear drive inverter: a123 loss motor control | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a126_limpMode` | Rear drive inverter: a126 limp mode | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a127_gracefulPowerOff` | Rear drive inverter: a127 graceful power off | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIR_a128_fpgaVersionMismatch` | Rear drive inverter: a128 fpga version mismatch | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Rear drive inverter messages (DIR)](../../dir.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
