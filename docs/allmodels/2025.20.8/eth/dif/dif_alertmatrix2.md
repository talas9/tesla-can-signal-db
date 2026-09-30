---
layout: default
title: "DIF_alertMatrix2 (0x357) — Front drive inverter, Tesla Model 3 / Model Y 2025.20.8 ETH"
description: "Front drive inverter message: alert matrix2. Ethernet-side message DIF_alertMatrix2 of Front drive inverter for Tesla Model 3 / Model Y firmware 2025.20.8, 54 signals (DIF_a065_canHardwareBusB, DIF_a066_canDataBusB, DIF_a067_canOverrunBusB, DIF_a069_rotorTempLimit and 50 more). Bit layout, scaling, units and value tables."
---

# DIF_alertMatrix2 (0x357) — Front drive inverter, Tesla Model 3 / Model Y 2025.20.8 ETH

Front drive inverter message: alert matrix2. This page documents the 54 signals of DIF_alertMatrix2 as defined for Tesla Model 3 / Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DIF_alertMatrix2` |
| Ethernet-side id | 0x357 (855) |
| ECU | [Front drive inverter](../../dif.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DIF |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 54 |

## Signals of DIF_alertMatrix2

Tesla Model 3 / Model Y CAN bus signals in `DIF_alertMatrix2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DIF_a065_canHardwareBusB` | Front drive inverter: a065 can hardware bus b | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a066_canDataBusB` | Front drive inverter: a066 can data bus b | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a067_canOverrunBusB` | Front drive inverter: a067 can overrun bus b | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a069_rotorTempLimit` | Front drive inverter: a069 rotor temp limit | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a070_udsTransactionInitiated` | Front drive inverter: a070 uds transaction initiated | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a071_busDisconnected` | Front drive inverter: a071 bus disconnected | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a072_gateDriveFaultCounter` | Front drive inverter: a072 gate drive fault counter | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a073_motorSpeed` | Front drive inverter: a073 motor speed | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a074_motorEncoder` | Front drive inverter: a074 motor encoder | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a075_motorSpeedMismatch` | Front drive inverter: a075 motor speed mismatch | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a076_lvSupplyOV` | Front drive inverter: a076 lv supply OV | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a077_lvSupplyUV` | Front drive inverter: a077 lv supply UV | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a078_adcRefLow` | Front drive inverter: a078 adc ref low | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a079_adcRefHigh` | Front drive inverter: a079 adc ref high | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a081_P0BFF_DIF_EM_CurrentHigh` | Front drive inverter: a081 P0 BFF DIF EM current high | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a082_P7837_DIF_ECU_DemoTimer` | Front drive inverter: a082 P7837 DIF ECU demo timer | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a083_PABCD_DIF_ECU_DemoWindow` | Front drive inverter: a083 PABCD DIF ECU demo window | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a084_eccTestData0` | Front drive inverter: a084 ecc test data0 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a086_activeDischargeOn` | Front drive inverter: a086 active discharge on | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a087_gtwMIA` | Front drive inverter: a087 gtw MIA | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a088_uiMIA` | Front drive inverter: a088 ui MIA | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a090_pmMIA` | Front drive inverter: a090 pm MIA | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a091_espMIA` | Front drive inverter: a091 esp MIA | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a092_bmsMIA` | Front drive inverter: a092 bms MIA | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a093_canHardwareBusA` | Front drive inverter: a093 can hardware bus a | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a094_canDataBusA` | Front drive inverter: a094 can data bus a | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a095_canOverrunBusA` | Front drive inverter: a095 can overrun bus a | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a096_memoryError` | Front drive inverter: a096 memory error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a097_eepromError` | Front drive inverter: a097 eeprom error | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a098_intTimeTooLong` | Front drive inverter: a098 int time too long | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a099_threadOverrun` | Front drive inverter: a099 thread overrun | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a100_assertion` | Front drive inverter: a100 assertion | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a101_eccTestData1` | Front drive inverter: a101 ecc test data1 | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a102_exceptionPrefetchAbort` | Front drive inverter: a102 exception prefetch abort | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a103_lowFlow` | Front drive inverter: a103 low flow | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a107_fpgaError` | Front drive inverter: a107 fpga error | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a108_stateTrans` | Front drive inverter: a108 state trans | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a109_ahbWriteError` | Front drive inverter: a109 ahb write error | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a110_brakeMIA` | Front drive inverter: a110 brake MIA | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a111_badPhaseSensorCalib` | Front drive inverter: a111 bad phase sensor calib | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a112_noPhaseCurrent` | Front drive inverter: a112 no phase current | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a113_noFuncHeatsinkSensor` | Front drive inverter: a113 no func heatsink sensor | 48\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a114_exceptionDataAbort` | Front drive inverter: a114 exception data abort | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a115_exceptionDataAbort2` | Front drive inverter: a115 exception data abort2 | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a116_highSpeedWearCounter` | Front drive inverter: a116 high speed wear counter | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a117_diMIA` | Front drive inverter: a117 di MIA | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a119_hvpMIA` | Front drive inverter: a119 hvp MIA | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a120_hvlinkMIA` | Front drive inverter: a120 hvlink MIA | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a121_motorControlRegulation` | Front drive inverter: a121 motor control regulation | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a122_highStackUsage` | Front drive inverter: a122 high stack usage | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a123_lossMotorControl` | Front drive inverter: a123 loss motor control | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a126_limpMode` | Front drive inverter: a126 limp mode | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a127_gracefulPowerOff` | Front drive inverter: a127 graceful power off | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DIF_a128_fpgaVersionMismatch` | Front drive inverter: a128 fpga version mismatch | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model 3 / Model Y 2025.20.8 ETH DBC file](../../../../../dbc/AllModels/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Front drive inverter messages (DIF)](../../dif.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
