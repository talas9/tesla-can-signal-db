---
layout: default
title: "DI_alertMatrix2 (0x368) — Drive inverter, Tesla Model Y 2025.20.8 ETH"
description: "Drive inverter message: alert matrix2. Ethernet-side message DI_alertMatrix2 of Drive inverter for Tesla Model Y firmware 2025.20.8, 51 signals (DI_a065_canHardwareBusB, DI_a066_canDataBusB, DI_a067_canOverrunBusB, DI_a068_secondaryWheelSpeedIrrational and 47 more). Bit layout, scaling, units and value tables."
---

# DI_alertMatrix2 (0x368) — Drive inverter, Tesla Model Y 2025.20.8 ETH

Drive inverter message: alert matrix2. This page documents the 51 signals of DI_alertMatrix2 as defined for Tesla Model Y firmware 2025.20.8 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `DI_alertMatrix2` |
| Ethernet-side id | 0x368 (872) |
| ECU | [Drive inverter](../../di.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2025.20.8 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | DI |
| Frame length | 8 bytes |
| Cycle time | 1000 ms |
| Signals | 51 |

## Signals of DI_alertMatrix2

Tesla Model Y CAN bus signals in `DI_alertMatrix2`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `DI_a065_canHardwareBusB` | Drive inverter: a065 can hardware bus b | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a066_canDataBusB` | Drive inverter: a066 can data bus b | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a067_canOverrunBusB` | Drive inverter: a067 can overrun bus b | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a068_secondaryWheelSpeedIrrational` | Drive inverter: a068 secondary wheel speed irrational | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a069_P1234_DI_ECU_DemoWindow` | Drive inverter: a069 P1234 DI ECU demo window | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a070_udsTransactionInitiated` | Drive inverter: a070 uds transaction initiated | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a076_lvSupplyOV` | Drive inverter: a076 lv supply OV | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a077_lvSupplyUV` | Drive inverter: a077 lv supply UV | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a078_adcRefLow` | Drive inverter: a078 adc ref low | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a079_adcRefHigh` | Drive inverter: a079 adc ref high | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a080_accelSynch` | Drive inverter: a080 accel synch | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a081_accelTrack1` | Drive inverter: a081 accel track1 | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a082_accelTrack2` | Drive inverter: a082 accel track2 | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a083_brakePedalSensor` | Drive inverter: a083 brake pedal sensor | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a084_eccTestData0` | Drive inverter: a084 ecc test data0 | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a085_proximityInEnable` | Drive inverter: a085 proximity in enable | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a086_dpbMIA` | Drive inverter: a086 dpb MIA | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a087_gtwMIA` | Drive inverter: a087 gtw MIA | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a088_uiMIA` | Drive inverter: a088 ui MIA | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a089_sccmMIA` | Drive inverter: a089 sccm MIA | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a090_pmMIA` | Drive inverter: a090 pm MIA | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a091_espMIA` | Drive inverter: a091 esp MIA | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a092_bmsMIA` | Drive inverter: a092 bms MIA | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a093_canHardwareBusA` | Drive inverter: a093 can hardware bus a | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a094_canDataBusA` | Drive inverter: a094 can data bus a | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a095_canOverrunBusA` | Drive inverter: a095 can overrun bus a | 30\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a096_memoryError` | Drive inverter: a096 memory error | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a097_eepromError` | Drive inverter: a097 eeprom error | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a098_eepromManagerError` | Drive inverter: a098 eeprom manager error | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a099_threadOverrun` | Drive inverter: a099 thread overrun | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a100_nvramError` | Drive inverter: a100 nvram error | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a101_eccTestData1` | Drive inverter: a101 ecc test data1 | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a102_exceptionPrefetchAbort` | Drive inverter: a102 exception prefetch abort | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a103_bbMIA` | Drive inverter: a103 bb MIA | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a104_proximityIrrational` | Drive inverter: a104 proximity irrational | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a105_cpMIA` | Drive inverter: a105 cp MIA | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a108_appMIA` | Drive inverter: a108 app MIA | 43\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a109_ahbWriteError` | Drive inverter: a109 ahb write error | 44\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a110_brakeMIA` | Drive inverter: a110 brake MIA | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a112_accelTrack1Incons` | Drive inverter: a112 accel track1 incons | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a114_exceptionDataAbort` | Drive inverter: a114 exception data abort | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a115_exceptionDataAbort2` | Drive inverter: a115 exception data abort2 | 50\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a116_motorRecovered` | Drive inverter: a116 motor recovered | 51\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a117_latentFaultCheckTripped` | Drive inverter: a117 latent fault check tripped | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a118_diImmobilizedForFactoryFailsafe` | Drive inverter: a118 di immobilized for factory failsafe | 53\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a119_latentFaultCheckFailedOnce` | Drive inverter: a119 latent fault check failed once | 54\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a120_regenBlendingUnavailable` | Drive inverter: a120 regen blending unavailable | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a121_qualifiedBrakeEventMitigation` | Drive inverter: a121 qualified brake event mitigation | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a122_highStackUsage` | Drive inverter: a122 high stack usage | 57\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a124_cruiseFault` | Drive inverter: a124 cruise fault | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `DI_a125_noBatteryPower` | Drive inverter: a125 no battery power | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2025.20.8 ETH DBC file](../../../../../dbc/ModelY/2025.20.8/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2025.20.8/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Drive inverter messages (DI)](../../di.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
