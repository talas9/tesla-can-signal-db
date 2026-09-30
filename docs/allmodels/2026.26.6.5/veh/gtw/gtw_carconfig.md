---
layout: default
title: "GTW_carConfig (0x7FF) — Gateway, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN"
description: "Gateway message: car config. Tesla Model 3 / Model Y CAN bus message GTW_carConfig (0x7FF) of Gateway, firmware 2026.26.6.5, 200 signals (GTW_carConfigMultiplexer, GTW_deliveryStatus, GTW_cabinPTCHeaterType, GTW_rightHandDrive and 196 more). Bit layout, scaling, units and value tables."
---

# GTW_carConfig (0x7FF) — Gateway, Tesla Model 3 / Model Y 2026.26.6.5 VEH CAN

Gateway message: car config; frame length observed on a vehicle bus. This page documents the 200 signals of GTW_carConfig as defined for Tesla Model 3 / Model Y firmware 2026.26.6.5 on the VEH bus.

## Message details

| Property | Value |
|---|---|
| Message name | `GTW_carConfig` |
| CAN id | 0x7FF (2047) |
| ECU | [Gateway](../../gtw.md) |
| Vehicle | Tesla Model 3 / Model Y |
| Firmware | 2026.26.6.5 |
| Bus | VEH (vehicle CAN) |
| Transmitter | GTW |
| Frame length | 8 bytes |
| Cycle time | 100 ms |
| Signals | 200 |

## Signals of GTW_carConfig

Tesla Model 3 / Model Y CAN bus signals in `GTW_carConfig`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Mux | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `GTW_carConfigMultiplexer` | selector | Gateway: car config multiplexer | 0\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 |  | validated |
| `GTW_deliveryStatus` | page 1 | Indicates whether the vehicle has been marked delivered to the customer in Tesla backend systems. | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_DELIVERED`<br>1 = `DELIVERED` | validated |
| `GTW_cabinPTCHeaterType` | page 1 | Gateway: cabin PTC heater type | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `BORGWARNER`<br>1 = `NONE` | validated |
| `GTW_rightHandDrive` | page 1 | Gateway: right hand drive | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEFT`<br>1 = `RIGHT` | validated |
| `GTW_rearLightType` | page 1 | Gateway: rear light type | 12\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NA`<br>1 = `EU_CN`<br>2 = `GLOBAL` | validated |
| `GTW_headlamps` | page 1 | Gateway: headlamps | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `BASE`<br>1 = `PREMIUM`<br>2 = `GLOBAL` | validated |
| `GTW_country` | page 1 | Gateway: country | 16\|16 | little-endian | unsigned | 1 | 0 |  | 0 to 65535 |  | validated |
| `GTW_tireType` | page 1 | Gateway: tire type | 32\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `UNKNOWN`<br>1 = `MICHELIN_ALL_SEASON_18`<br>2 = `MICHELIN_SUMMER_18`<br>3 = `HANKOOK_SUMMER_19`<br>4 = `CONTI_ALL_SEASON_19`<br>5 = `MICHELIN_SUMMER_20`<br>6 = `PIRELLI_ALL_SEASON_20`<br>7 = `GOODYEAR_ALL_TERRAIN_20`<br>16 = `BRIDGESTONE_SUMMER_18`<br>17 = `GOODYEAR_ALL_SEASON_20`<br>18 = `PIRELLI_SUMMER_21`<br>19 = `MICHELIN_ALL_SEASON_21`<br>20 = `PIRELLI_SUMMER_19`<br>21 = `PIRELLI_SUMMER_20`<br>22 = `MICHELIN_SUMMER_21`<br>23 = `CONTI_ALL_SEASON_20`<br>24 = `CONTI_SUMMER_22`<br>25 = `PIRELLI_ALL_SEASON_22`<br>26 = `HANKOOK_ALL_SEASON_18`<br>27 = `GOODYEAR_ALL_SEASON_21`<br>28 = `PIRELLI_ALL_SEASON_19`<br>29 = `HANKOOK_ALL_SEASON_21`<br>30 = `KUMHO_ALL_SEASON_19`<br>31 = `GOODYEAR_SUMMER_19`<br>32 = `HANKOOK_ALL_SEASON_20`<br>33 = `BRIDGESTONE_ALL_SEASON_20`<br>34 = `CONTI_SUMMER_19`<br>35 = `GOODYEAR_ALL_SEASON_18`<br>36 = `KUMHO_ALL_SEASON_18`<br>37 = `GITI_SUMMER_18`<br>38 = `HANKOOK_SUMMER_18` | validated |
| `GTW_dasHw` | page 1 | Indicates the Driver Assistance System (DAS) hardware installed. | 40\|3 | little-endian | unsigned | 1 | 0 |  | 3 to 5 | 3 = `PARKER_PASCAL_2_5`<br>4 = `TESLA_AP3`<br>5 = `TESLA_AP4` | validated |
| `GTW_brakeHWType` | page 1 | Gateway: brake HW type | 43\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `BREMBO_P42_MANDO_43MOC`<br>1 = `BREMBO_LARGE_P42_BREMBO_44MOC`<br>2 = `BREMBO_LARGE_P42_MANDO_43MOC`<br>3 = `BREMBO_LARGE_P42_BREMBO_LARGE_44MOC`<br>6 = `BREMBO_LARGE_P42_V2_BREMBO_44MOC`<br>7 = `BREMBO_LARGE_P42_V2_BREMBO_LARGE_44MOC`<br>8 = `BREMBO_LARGE_P42_V2_MANDO_43MOC`<br>9 = `BREMBO_P42_V2_MANDO_43MOC`<br>13 = `BREMBO_P42_ZF_43MOC`<br>15 = `BREMBO_P42LD_ZF_43MOC`<br>16 = `BREMBO_P42LD_V2_MANDO_43MOC`<br>17 = `HITACHI_P42_V2_MANDO_43MOC`<br>18 = `BREMBO_LARGE_P42_V2_BREMBO_44MOC_GA`<br>20 = `BREMBO_LARGE_P42_V2_MANDO_43MOC_LOW_DRAG`<br>21 = `HITACHI_P42_V2_MANDO_43MOC_LOW_DRAG` | validated |
| `GTW_restraintsHardwareType` | page 1 | Gateway: restraints hardware type | 48\|8 | little-endian | unsigned | 1 | 0 |  | 0 to 255 | 81 = `NA_MYB`<br>82 = `ROW_ECALL_MYB`<br>83 = `ROW_MYB`<br>84 = `ROW_ECALL_PEDPRO_MYB`<br>85 = `EU_ECALL_PEDPRO_MYB`<br>86 = `EU_PERF_ECALL_PEDPRO_MYB`<br>87 = `ROW_PERF_ECALL_PEDPRO_MYB`<br>88 = `ROW_PEDPRO_MYB`<br>89 = `ROW_ECALL_PEDPRO_MYL`<br>232 = `ECE_ECALL_PEDPRO_MYL`<br>233 = `NA_MYL`<br>236 = `NA_E41_MYB`<br>237 = `EU_ECALL_E41_MYB`<br>238 = `ROW_ECALL_E41_MYB`<br>239 = `NA_NO_KAB_MYB` | contradicted |
| `GTW_drivetrainType` | page 1 | Gateway: drivetrain type | 56\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 4 | 0 = `RWD`<br>1 = `AWD` | validated |
| `GTW_radarHeaterType` | page 1 | Gateway: radar heater type | 60\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 5 | 0 = `NONE`<br>1 = `MODELY_BACKER_THIN_3M` | validated |
| `GTW_exteriorTrimType` | page 2 | Gateway: exterior trim type | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `STANDARD_CHROME`<br>1 = `SATIN_BLACK` | validated |
| `GTW_frontSeatHeaters` | page 2 | Gateway: front seat heaters | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NONE`<br>1 = `KONGSBERG_LOW_POWER` | validated |
| `GTW_rearSeatHeaters` | page 2 | Gateway: rear seat heaters | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NONE`<br>1 = `KONGSBERG_LOW_POWER` | validated |
| `GTW_eCallAntennaHW` | page 2 | Gateway: e call antenna HW | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `BACKUP_OR_MAIN_ANT`<br>1 = `MAIN_ANT_ONLY` | validated |
| `GTW_homelinkType` | page 2 | Gateway: homelink type | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NONE`<br>1 = `HOMELINK_V_OPT_2` | validated |
| `GTW_vdcType` | page 2 | Gateway: vdc type | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `BOSCH_VDC`<br>1 = `TESLA_VDC` | validated |
| `GTW_memoryMirrors` | page 2 | Gateway: memory mirrors | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_INSTALLED`<br>1 = `SMR` | validated |
| `GTW_powerLiftgateType` | page 2 | Gateway: power liftgate type | 18\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NOT_INSTALLED`<br>1 = `TESLA_REV1`<br>2 = `HUADE_REV1` | validated |
| `GTW_lumbarECUType` | page 2 | Gateway: lumbar ECU type | 20\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `ALFMEIER`<br>2 = `ALFMEIER_DRIVER_ONLY_LHD`<br>3 = `ALFMEIER_DRIVER_ONLY_RHD`<br>4 = `AEW`<br>5 = `AEW_DRIVER_ONLY_LHD`<br>6 = `AEW_DRIVER_ONLY_RHD`<br>7 = `ND_DRIVER_ONLY_LHD`<br>8 = `ND_DRIVER_ONLY_RHD`<br>9 = `AEW_SINGLE_AXIS_DRIVER_ONLY_LHD`<br>10 = `AEW_SINGLE_AXIS_DRIVER_ONLY_RHD` | validated |
| `GTW_rearSeatHeaterType` | page 2 | Gateway: rear seat heater type | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 1 = `LEFT_RIGHT_ONLY_KONGSBERG`<br>2 = `NONE`<br>3 = `LEFT_RIGHT_ONLY_GENTHERM` | contradicted |
| `GTW_auxParkLamps` | page 2 | Gateway: aux park lamps | 26\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NA_BASE`<br>1 = `NA_PREMIUM`<br>2 = `EU`<br>3 = `NONE` | validated |
| `GTW_interiorCabinRadarType` | page 2 | Gateway: interior cabin radar type | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NONE`<br>1 = `TESLA` | validated |
| `GTW_hvacPanelVaneType` | page 2 | Gateway: hvac panel vane type | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `PARALLEL_V1`<br>1 = `CONVERGENT_V1` | validated |
| `GTW_intakeAirFilterType` | page 2 | Gateway: intake air filter type | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `STANDARD`<br>1 = `HEPA` | validated |
| `GTW_eBuckConfig` | page 2 | Gateway: e buck config | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NONE`<br>1 = `DEV_BUCK` | validated |
| `GTW_steeringHeaterEnabled` | page 2 | Gateway: steering heater enabled | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | validated |
| `GTW_activeHighBeam` | page 2 | Gateway: active high beam | 34\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_ACTIVE`<br>1 = `ACTIVE` | validated |
| `GTW_airbagCutoffSwitch` | page 2 | Gateway: airbag cutoff switch | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CUTOFF_SWITCH_DISABLED`<br>1 = `CUTOFF_SWITCH_ENABLED` | validated |
| `GTW_intrusionSensorType` | page 2 | Gateway: intrusion sensor type | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_INSTALLED`<br>1 = `VODAFONE` | validated |
| `GTW_spoilerType` | page 2 | Gateway: spoiler type | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_INSTALLED`<br>1 = `PASSIVE` | validated |
| `GTW_backupCameraType` | page 2 | Gateway: backup camera type | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NO_HEATER`<br>1 = `INTEGRATED_HEATER_V1` | validated |
| `GTW_rearFogLamps` | page 2 | Gateway: rear fog lamps | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_INSTALLED`<br>1 = `INSTALLED` | validated |
| `GTW_roofType` | page 2 | Gateway: roof type | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 1 = `FIXED_GLASS` | validated |
| `GTW_thirdRowSeatType` | page 2 | Gateway: third row seat type | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NONE`<br>1 = `FLAT_FOLD` | validated |
| `GTW_autopilot` | page 2 | Gateway: autopilot | 42\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>1 = `HIGHWAY`<br>2 = `ENHANCED`<br>3 = `SELF_DRIVING`<br>4 = `BASIC` | validated |
| `GTW_superchargingAccess` | page 2 | Gateway: supercharging access | 45\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_ALLOWED`<br>1 = `ALLOWED`<br>2 = `PAY_AS_YOU_GO` | validated |
| `GTW_exteriorColor` | page 2 | Gateway: exterior color | 48\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `RED_MULTICOAT`<br>1 = `SOLID_BLACK`<br>2 = `SILVER_METALLIC`<br>3 = `MIDNIGHT_SILVER`<br>5 = `DEEP_BLUE`<br>6 = `PEARL_WHITE`<br>7 = `MIDNIGHT_CHERRY_RED`<br>8 = `ABYSS_BLUE`<br>9 = `QUICKSILVER`<br>10 = `ULTRA_RED`<br>11 = `STEALTH_GREY`<br>13 = `FROST_BLUE`<br>14 = `GLACIER_BLUE`<br>15 = `DIAMOND_BLACK`<br>16 = `SILKROAD_SILVER`<br>17 = `MARINE_BLUE`<br>20 = `COASTAL_BLUE` | validated |
| `GTW_pedestrianWarningSound` | page 2 | Gateway: pedestrian warning sound | 53\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `SPEAKER`<br>2 = `EXT_SPEAKER_V2` | validated |
| `GTW_steeringColumnUJointType` | page 2 | Gateway: steering column u joint type | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 1 = `C_SAMPLE_PHASING` | validated |
| `GTW_bPillarNFCParam` | page 2 | Gateway: b pillar NFC param | 56\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `MODEL_3`<br>1 = `MODEL_Y` | validated |
| `GTW_interiorLighting` | page 2 | Gateway: interior lighting | 57\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `BASE`<br>1 = `PREMIUM`<br>2 = `PREMIUM_NO_POCKET_LIGHT`<br>3 = `PREMIUM_WITH_RGB`<br>4 = `PREMIUM_WITH_RGB_IP_ONLY`<br>5 = `FOOTWELL_RGB_IP`<br>6 = `FOOTWELL` | validated |
| `GTW_headlightLevelerType` | page 2 | Gateway: headlight leveler type | 60\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `GEN1`<br>2 = `VIRTUAL_PITCH_SENSOR` | validated |
| `GTW_numberHVILNodes` | page 2 | Gateway: number HVIL nodes | 62\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HVIL_NODES_0`<br>2 = `HVIL_NODES_2`<br>3 = `HVIL_NODES_3` | validated |
| `GTW_mapRegion` | page 3 | Gateway: map region | 8\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `US`<br>1 = `EU`<br>2 = `NONE`<br>3 = `CN`<br>4 = `AU`<br>5 = `JP`<br>6 = `TW`<br>7 = `KR`<br>8 = `ME`<br>9 = `HK`<br>10 = `MO`<br>11 = `SE`<br>12 = `IN`<br>13 = `LA` | validated |
| `GTW_performancePackage` | page 3 | Gateway: performance package | 12\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `BASE`<br>1 = `PERFORMANCE`<br>2 = `BASE_2024`<br>3 = `BASE_PLUS`<br>4 = `BASE_2022` | validated |
| `GTW_chassisType` | page 3 | Indicates the chassis type, which determines physical aspects such as suspension geometry, track width, wheel base, baseline tire size, and trailer capability. | 18\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 2 = `MODEL_3_CHASSIS`<br>3 = `MODEL_Y_CHASSIS`<br>7 = `MODEL_Y_LONG_WHEELBASE_CHASSIS_PATRONUS` | validated |
| `GTW_airSuspension` | page 3 | Gateway: air suspension | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>3 = `COIL_ADAPTIVE_DAMPING` | validated |
| `GTW_centerConsoleControllerType` | page 3 | Gateway: center console controller type | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `INSTALLED_V1`<br>2 = `INSTALLED_NO_AIRWAVE` | validated |
| `GTW_autopilotCameraType` | page 3 | Gateway: autopilot camera type | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `RCCB_CAMERAS`<br>1 = `RGGB_CAMERAS` | validated |
| `GTW_connectivityPackage` | page 3 | Gateway: connectivity package | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `BASE`<br>1 = `PREMIUM` | validated |
| `GTW_plcSupportType` | page 3 | Gateway: plc support type | 28\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `ONBOARD_ADAPTER`<br>2 = `NATIVE_CHARGE_PORT` | validated |
| `GTW_badgingVersion` | page 3 | Gateway: badging version | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VERSION_0`<br>1 = `VERSION_1`<br>2 = `VERSION_2` | validated |
| `GTW_packEnergy` | page 3 | Gateway: pack energy | 32\|5 | little-endian | unsigned | 1 | 0 |  | 0 to 31 | 0 = `SR`<br>1 = `LR`<br>2 = `MR` | validated |
| `GTW_frontSeatReclinerHardware` | page 3 | Gateway: front seat recliner hardware | 37\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `STANDARD_RANGE`<br>1 = `RIGHT_SEAT_REDUCED_RANGE`<br>2 = `LEFT_SEAT_REDUCED_RANGE`<br>3 = `LEFT_RIGHT_SEAT_REDUCED_RANGE` | validated |
| `GTW_brakeLineSwitchType` | page 3 | Gateway: brake line switch type | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DI_VC_SHARED`<br>1 = `VC_ONLY` | validated |
| `GTW_espValveType` | page 3 | Gateway: esp valve type | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `VALVE_TYPE_1`<br>2 = `VALVE_TYPE_2` | validated |
| `GTW_softRange` | page 3 | Gateway: soft range | 42\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STANDARD`<br>1 = `RANGE_220_MILES`<br>2 = `RANGE_93_MILES`<br>3 = `RANGE_343_MILES`<br>4 = `RANGE_260_MILES` | validated |
| `GTW_refrigerantType` | page 3 | Gateway: refrigerant type | 45\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `Default`<br>1 = `R134A`<br>2 = `R1234YF` | validated |
| `GTW_wheelType` | page 3 | Gateway: wheel type | 48\|7 | little-endian | unsigned | 1 | 0 |  | 0 to 127 | 0 = `PINWHEEL_18`<br>1 = `STILETTO_19`<br>2 = `STILETTO_20`<br>3 = `STILETTO_20_DARK_STAGGERED`<br>4 = `GEMINI_19_SQUARE`<br>5 = `GEMINI_19_STAGGERED`<br>14 = `STILETTO_20_DARK_SQUARE`<br>18 = `PINWHEEL_18_CAP_KIT`<br>19 = `ZEROG_20_GUNPOWDER`<br>21 = `STILETTO_REFRESH_19`<br>22 = `PINWHEEL_REFRESH_18`<br>23 = `UBERTURBINE_20_GUNPOWDER`<br>24 = `PINWHEEL_REFRESH_18_CAP_KIT`<br>27 = `ZEROG_19_GUNPOWDER`<br>30 = `GLIDER_18`<br>31 = `HELIX_19`<br>33 = `WISHBONE_20_STAGGERED`<br>39 = `CROSSFLOW_19`<br>40 = `HELIX_V2_20`<br>41 = `ARACHNID_V2_21`<br>46 = `APERTURE_18`<br>47 = `GLIDER_18_CAP_KIT`<br>48 = `MACHINA_V2_19_STAGGERED`<br>50 = `HELIX_V2_20_DARK`<br>51 = `GEMINI_19_DARK_STAGGERED`<br>52 = `UBERHELIX_20` | validated |
| `GTW_ptcControlMode` | page 3 | Gateway: ptc control mode | 55\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `BASELINE`<br>1 = `SEQ_ROD`<br>2 = `MESH_INSTALLED`<br>3 = `SEQ_ROD_LIMITED` | validated |
| `GTW_brakeActuationType` | page 3 | Gateway: brake actuation type | 57\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 4 | 0 = `ESP_IBST`<br>1 = `IDB_RCU`<br>2 = `ESP_DPB` | validated |
| `GTW_secondRowSeatType` | page 3 | Gateway: second row seat type | 60\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 3 = `POWERED_RECLINE`<br>4 = `EASY_ENTRY_POWERED_RECLINE`<br>5 = `FLAT_FOLD_V2`<br>6 = `TWO_SEATS_POWERED_RECLINE` | contradicted |
| `GTW_secondRowSeatMotorType` | page 3 | Gateway: second row seat motor type | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SHB`<br>1 = `KEIPER` | validated |
| `GTW_birthday` | page 4 | Gateway: birthday | 8\|32 | little-endian | unsigned | 1 | 0 |  | 0 to 4294967295 |  | validated |
| `GTW_eCallEnabled` | page 4 | Gateway: e call enabled | 40\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DISABLED`<br>1 = `ENABLED_OHC_SOS`<br>2 = `ENABLED_UI_SOS` | validated |
| `GTW_parkAssistECUType` | page 4 | Gateway: park assist ECU type | 42\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VALEO`<br>1 = `TESLA`<br>2 = `NONE` | validated |
| `GTW_passengerAirbagType` | page 4 | Gateway: passenger airbag type | 44\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `FULL_SUPPRESSION`<br>1 = `SAFETY_VENT`<br>2 = `EUROW` | validated |
| `GTW_forwardRadarHw` | page 4 | Gateway: forward radar hw | 46\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `CONTI_ARS410`<br>2 = `NONE` | validated |
| `GTW_frontSeatType` | page 4 | Gateway: front seat type | 48\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `BASE_TESLA`<br>1 = `PREMIUM_TESLA`<br>2 = `PREMIUM_L_YANFENG_R_TESLA`<br>3 = `PREMIUM_L_TESLA_R_YANFENG`<br>4 = `PREMIUM_YANFENG`<br>5 = `PREMIUM_BROSE`<br>6 = `PREMIUM_L_TESLA_R_TESLA_MINITILT`<br>7 = `PREMIUM_L_TESLA_MINITILT_R_TESLA`<br>8 = `PREMIUM_L_TESLA_MINITILT_R_TESLA_MINITILT`<br>9 = `PREMIUM_L_TESLA_MINITILT_R_YANFENG_MINITILT`<br>10 = `PREMIUM_L_YANFENG_R_YANFENG_MINITILT`<br>11 = `PREMIUM_L_YANFENG_MINITILT_R_YANFENG`<br>12 = `PREMIUM_L_YANFENG_MINITILT_R_YANFENG_MINITILT`<br>13 = `PREMIUM_L_YANFENG_MINITILT_R_TESLA_MINITILT` | validated |
| `GTW_secondRowDisplayType` | page 4 | Gateway: second row display type | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NONE`<br>1 = `TYPE_1` | validated |
| `GTW_wirelessPhoneChargerType` | page 4 | Gateway: wireless phone charger type | 53\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE_OR_USB`<br>1 = `FRONT_LIN`<br>3 = `FRONT_HIGH_POWER_UART` | validated |
| `GTW_ethernetTunerType` | page 4 | Gateway: ethernet tuner type | 55\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `HARMAN`<br>1 = `NONE`<br>2 = `HIRSCHMANN`<br>3 = `HARMAN_GEN3` | validated |
| `GTW_interiorTrimType` | page 4 | Gateway: interior trim type | 60\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `BLACK`<br>1 = `WHITE`<br>2 = `BLACK_CONSOLE_2`<br>3 = `WHITE_CONSOLE_2` | validated |
| `GTW_gloveboxUSBType` | page 5 | Gateway: glovebox USB type | 8\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_INSTALLED`<br>1 = `TSC_USB3_A`<br>2 = `TSC_USB3_A_PLUS_BT` | validated |
| `GTW_coolantPumpType` | page 5 | Gateway: coolant pump type | 10\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DUAL`<br>1 = `SINGLE_PUMP_BATT`<br>2 = `DUAL_SAN_P4`<br>4 = `DUAL_SAN_P4_LUB`<br>5 = `DUAL_MIX` | validated |
| `GTW_epblHwType` | page 5 | Gateway: epbl hw type | 13\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NOT_SET`<br>1 = `MANDO_V1`<br>2 = `MANDO_V2`<br>4 = `BREMBO_V1`<br>5 = `BREMBO_V2`<br>8 = `ZF` | validated |
| `GTW_epbrHwType` | page 5 | Gateway: epbr hw type | 17\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NOT_SET`<br>1 = `MANDO_V1`<br>2 = `MANDO_V2`<br>4 = `BREMBO_V1`<br>5 = `BREMBO_V2`<br>8 = `ZF` | validated |
| `GTW_blowerMotorType` | page 5 | Gateway: blower motor type | 21\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SHINANO`<br>1 = `DELTA` | validated |
| `GTW_rearLeftBLEEndpointParameterType` | page 5 | Gateway: rear left BLE endpoint parameter type | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NONE`<br>1 = `VIVALDI_ANTENNA` | validated |
| `GTW_powerMirrorFoldType` | page 5 | Gateway: power mirror fold type | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_INSTALLED`<br>1 = `TYPE_1` | validated |
| `GTW_frontUsbHubType` | page 5 | Gateway: front usb hub type | 27\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 5 | 0 = `2`<br>4 = `NO_DATA` | validated |
| `GTW_superManifoldType` | page 5 | Type of HVAC super manifold installed | 30\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `TYPE0`<br>1 = `TYPE1`<br>2 = `TYPE2` | validated |
| `GTW_rcmLocation` | page 5 | Gateway: rcm location | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CENTER_CONSOLE` | validated |
| `GTW_autopilotExteriorCameraType` | page 5 | Gateway: autopilot exterior camera type | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DEFAULT_FOR_APHW`<br>1 = `IMX00N` | validated |
| `GTW_interiorCamBeautyCoverType` | page 5 | Gateway: interior cam beauty cover type | 35\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `STANDARD`<br>1 = `PITCHED_UP`<br>2 = `PITCHED_DOWN` | validated |
| `GTW_sirenType` | page 5 | Gateway: siren type | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NONE`<br>1 = `VODAPHONE_IF_INTRUSION` | validated |
| `GTW_hornType` | page 5 | Gateway: horn type | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TRUMPET`<br>1 = `EXT_SPEAKER_V2` | validated |
| `GTW_passengerTrackMotorType` | page 5 | Gateway: passenger track motor type | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `INSTALLED_DEFAULT`<br>1 = `L_AND_V` | validated |
| `GTW_steeringColumnMotorType` | page 5 | Gateway: steering column motor type | 42\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `BOSCH`<br>1 = `JE`<br>2 = `BOSCH_COMMON_TO_JE`<br>3 = `NEXTEER` | validated |
| `GTW_refrigACLineType` | page 5 | Gateway: refrig AC line type | 48\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNLIMITED`<br>1 = `SAAA_LIMITED`<br>2 = `CONTI_LIMITED` | validated |
| `GTW_refrigFilterType` | page 5 | Gateway: refrig filter type | 50\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNBLOCKED`<br>1 = `BLOCKED_V1`<br>2 = `BLOCKED_V2` | validated |
| `GTW_diBurnInType` | page 5 | Gateway: di burn in type | 52\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NONE`<br>1 = `ENABLED_V1` | validated |
| `GTW_specialBadgingType` | page 5 | Gateway: special badging type | 53\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>2 = `LAUNCH_SERIES` | validated |
| `GTW_chassisSubType` | page 5 | Reports chassis sub-variant type. | 55\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNKNOWN`<br>1 = `BASE`<br>2 = `PERFORMANCE`<br>3 = `TRIM_DEVIATION_1`<br>4 = `MARKET_VARIANT_2` | validated |
| `GTW_towPackage` | page 5 | Gateway: tow package | 58\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `TESLA_REV1`<br>2 = `TESLA_REV2` | validated |
| `GTW_refrigLccType` | page 5 | Gateway: refrig lcc type | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LCC`<br>1 = `LCCR` | validated |
| `GTW_restraintControlsType` | page 5 | Gateway: restraint controls type | 61\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `BOSCH`<br>1 = `TESLA` | validated |
| `GTW_caliperColorType` | page 5 | Gateway: caliper color type | 62\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN`<br>1 = `GREY`<br>2 = `RED` | validated |
| `GTW_wiperMotorType` | page 6 | Gateway: wiper motor type | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_UPDATEABLE`<br>1 = `SHB` | validated |
| `GTW_frontOverheadConsoleType` | page 6 | Gateway: front overhead console type | 10\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `VALEO`<br>1 = `BITRON`<br>2 = `PREH`<br>3 = `KOSTAL` | validated |
| `GTW_shifterType` | page 6 | Gateway: shifter type | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `STALK`<br>1 = `DISPLAY` | validated |
| `GTW_compressorType` | page 6 | Gateway: compressor type | 13\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `HANON_33CC`<br>1 = `DENSO_41CC_8K`<br>2 = `DENSO_41CC_11K`<br>3 = `SANDEN`<br>4 = `DENSO_11K_COP1_ENABLED`<br>5 = `SANDEN_V2`<br>6 = `SANDEN_V1_1`<br>7 = `SANDEN_V3`<br>8 = `SANDEN_V4`<br>10 = `SANDEN_V4_1` | validated |
| `GTW_twelveVBatteryType` | page 6 | Gateway: twelve v battery type | 17\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `ATLASBX_B24_FLOODED`<br>1 = `CLARIOS_B24_FLOODED`<br>2 = `CATL_LI_ION`<br>3 = `TESLA_16V_LI_ION` | validated |
| `GTW_efuseSWConfig` | page 6 | Gateway: efuse SW config | 20\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `DISABLED`<br>1 = `ROUND_ENABLED`<br>2 = `SQUARE_ENABLED`<br>3 = `ALL_ENABLED` | validated |
| `GTW_tollCollectionModuleType` | page 6 | Gateway: toll collection module type | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NONE`<br>1 = `WANJI_V1` | validated |
| `GTW_bleEndpointUpdateMethod` | page 6 | Gateway: ble endpoint update method | 24\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 1 = `BOOTLOADER_UPDATE` | validated |
| `GTW_steeringWheelControllerType` | page 6 | Gateway: steering wheel controller type | 25\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 1 = `DUAL_PREH`<br>2 = `DUAL_KOSTAL`<br>5 = `DUAL_TESLA_GEN5` | contradicted |
| `GTW_frontSeatVentilationEnabled` | page 6 | Gateway: front seat ventilation enabled | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | validated |
| `GTW_gloveboxActuatorType` | page 6 | Gateway: glovebox actuator type | 29\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `SOLENOID`<br>1 = `SMA`<br>2 = `ELECTROMAGNET` | validated |
| `GTW_epasType` | page 6 | Gateway: epas type | 32\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 11 | 0 = `MANDO_VGR69_GEN3`<br>3 = `MANDO_VGR69_GEN3_SINGLE_ECU`<br>4 = `MANDO_CGR69`<br>5 = `MANDO_CGR69_SINGLE_ECU`<br>6 = `THYSSENKRUPP_VGR69`<br>7 = `MANDO_CGR65`<br>8 = `THYSSENKRUPP_CGR65` | validated |
| `GTW_homologationRegionOverride` | page 6 | Gateway: homologation region override | 36\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DEFAULT_FOR_COUNTRY_CODE`<br>1 = `KR_UNECE`<br>2 = `MX_UNECE` | validated |
| `GTW_windowCommandsPermissionType` | page 6 | Gateway: window commands permission type | 38\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `ROW_OR_US_FMVSS_S5`<br>1 = `US_FMVSS_S4`<br>2 = `US_FMVSS_S6` | validated |
| `GTW_headlightStepperStallDetectMode` | page 6 | Gateway: headlight stepper stall detect mode | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | validated |
| `GTW_rgbInteriorLightingEnabled` | page 6 | Gateway: rgb interior lighting enabled | 43\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DISABLED_OR_NA`<br>1 = `WHITE_ONLY`<br>2 = `ALL_COLORS` | validated |
| `GTW_windshieldWiperHeaterType` | page 6 | Gateway: windshield wiper heater type | 45\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_INSTALLED`<br>1 = `TYPE_1` | validated |
| `GTW_thirdRowSeatReclinerType` | page 6 | Gateway: third row seat recliner type | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `MANUAL_OR_NA`<br>1 = `POWERED_SHB` | validated |
| `GTW_driveInterfaceType` | page 6 | Gateway: drive interface type | 47\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `COMBINED`<br>1 = `EXTERNAL` | validated |
| `GTW_efficiencyPackage` | page 6 | Gateway: efficiency package | 49\|6 | little-endian | unsigned | 1 | 0 |  | 0 to 63 | 0 = `DEFAULT`<br>5 = `MY_2020`<br>7 = `MY_2021`<br>9 = `MY_SR_PLUS_2021_Q3_GFSH`<br>11 = `MY_SR_PLUS_2022_Q1_TX`<br>12 = `MY_RWD_EU_2022`<br>15 = `MY_2023_GFSH_EXPORT_NA`<br>16 = `MY_2024`<br>20 = `MY_2023_SR_RWD`<br>23 = `MY_2024C`<br>24 = `MY_2024_GFSH_EXPORT_NA_SR_RWD`<br>32 = `MY_REFRESH_2025_ROW`<br>33 = `MY_REFRESH_2025_CN_ALL_US_LR_RWD`<br>34 = `MY_STANDARD_2026`<br>38 = `MY_2026_M53`<br>39 = `MY_2025_CN_PLUS`<br>42 = `MY_2026_US` | contradicted |
| `GTW_visorLightType` | page 6 | Gateway: visor light type | 55\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NON_DIMMABLE`<br>1 = `DIMMABLE_TYPE_1` | validated |
| `GTW_gnssAntennaType` | page 6 | Gateway: gnss antenna type | 58\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NA_OR_GEN1`<br>1 = `GEN2_NO_METAL_INSERT`<br>2 = `GEN2_WITH_METAL_INSERT` | validated |
| `GTW_airDistributionBoxType` | page 6 | Gateway: air distribution box type | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NONE`<br>1 = `TYPE_1` | validated |
| `GTW_frontSeatHeatersEnabled` | page 6 | Gateway: front seat heaters enabled | 62\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED` | validated |
| `GTW_windshieldWiperHeaterEnabled` | page 6 | Gateway: windshield wiper heater enabled | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISABLED`<br>1 = `ENABLED_OR_NA` | validated |
| `GTW_alcoholInterlockType` | page 7 | Gateway: alcohol interlock type | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NONE`<br>1 = `TYPE_1` | validated |
| `GTW_fasciaType` | page 7 | Gateway: fascia type | 9\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `ORIGINAL`<br>3 = `BASE_BAYBERRY`<br>4 = `PERFORMANCE_BAYBERRY`<br>8 = `E41_BAYBERRY` | validated |
| `GTW_powerSteeringColumn` | page 7 | Gateway: power steering column | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_INSTALLED`<br>1 = `TK` | validated |
| `GTW_frontSeatHeaterType` | page 7 | Gateway: front seat heater type | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `KONGSBERG`<br>1 = `GENTHERM` | validated |
| `GTW_softPerformanceLimit` | page 7 | Gateway: soft performance limit | 15\|4 | little-endian | unsigned | 1 | 0 |  | 0 to 15 | 0 = `NONE`<br>1 = `LIMIT_160_KW`<br>2 = `LIMIT_110_KW`<br>4 = `LIMIT_110_MPH`<br>6 = `LIMIT_230_KW` | validated |
| `GTW_gsrFeatureType` | page 7 | Gateway: gsr feature type | 21\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NONE`<br>2 = `TYPE_2_GSR` | validated |
| `GTW_immersiveAudio` | page 7 | Gateway: immersive audio | 23\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DISABLED`<br>1 = `BASE`<br>2 = `PREMIUM` | validated |
| `GTW_frontSeatVentilationType` | page 7 | Gateway: front seat ventilation type | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NONE`<br>1 = `TYPE_1` | validated |
| `GTW_passengerOccupancySensorType` | page 7 | Gateway: passenger occupancy sensor type | 26\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `OCS`<br>1 = `RESISTIVE_PAD`<br>4 = `NONE` | validated |
| `GTW_packPerformanceDeviation` | page 7 | Measures deviation from standard pack mass or power output capability associated with the vehicle packEnergy configuration. | 30\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NO_DEVIATION`<br>1 = `PACK_MASS_DEVIATION_1`<br>2 = `PACK_POWER_DEVIATION_1`<br>3 = `PACK_STRUCTURAL_DEVIATION_1`<br>4 = `PACK_MASS_DEVIATION_2`<br>5 = `PACK_POWER_DEVIATION_2` | validated |
| `GTW_pressurePadType` | page 7 | Gateway: pressure pad type | 33\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `BOSCH_B2_300N`<br>2 = `BOSCH_B2_400N`<br>3 = `BOSCH_LINDA_300N` | plausible |
| `GTW_frontFogLamps` | page 7 | Gateway: front fog lamps | 35\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_INSTALLED`<br>1 = `INSTALLED` | validated |
| `GTW_driverOccupancySensorType` | page 7 | Gateway: driver occupancy sensor type | 36\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `RESISTIVE_PAD`<br>1 = `NONE` | validated |
| `GTW_audioType` | page 7 | Gateway: audio type | 37\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `BASE`<br>1 = `PREMIUM`<br>3 = `ESSENTIAL`<br>4 = `ESSENTIAL_WITH_COMMODITY100` | validated |
| `GTW_thighExtenderType` | page 7 | Gateway: thigh extender type | 41\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NONE`<br>1 = `YANFENG` | validated |
| `GTW_occupancyClassificationFeatureType` | page 7 | Gateway: occupancy classification feature type | 42\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISCRETE_SENSOR_OR_NA`<br>1 = `TESLA_CABIN_RADAR` | validated |
| `GTW_frontControllerArchitectureType` | page 7 | Reports internal microcontroller architecture of the Front Controller assembly, which contains the Front Vehicle Controller (VCFRONT) and may contain a Vehicle Battery Controller (VCBATT). | 46\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `ALPHA_TYPE`<br>1 = `BETA_TYPE` | validated |
| `GTW_domeLightType` | page 7 | Gateway: dome light type | 47\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 2 = `2R`<br>3 = `2R_3R` | validated |
| `GTW_tpmsType` | page 7 | Gateway: tpms type | 49\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `CONTI_2`<br>1 = `TESLA_BLE`<br>2 = `INDIRECT` | validated |
| `GTW_authenticationEndpointLayout` | page 7 | Gateway: authentication endpoint layout | 52\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 6 | 0 = `LAYOUT_1`<br>1 = `M3_LAYOUT_2`<br>2 = `MY_LAYOUT_2`<br>5 = `MY_LAYOUT_3`<br>6 = `M3_LAYOUT_3` | validated |
| `GTW_socSleepOverride` | page 7 | Gateway: soc sleep override | 57\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PN_DERIVED`<br>1 = `FORCE_S3`<br>2 = `FORCE_SHALLOW` | validated |
| `GTW_r79BehaviorOverride` | page 7 | Gateway: r79 behavior override | 59\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NO_OVERRIDE`<br>1 = `R79_ENABLED` | validated |
| `GTW_steeringHeaterType` | page 7 | Gateway: steering heater type | 60\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>4 = `ZF_ROUND`<br>7 = `YF_V2` | validated |
| `GTW_narrowWipingSupported` | page 7 | Gateway: narrow wiping supported | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_SUPPORTED`<br>1 = `SUPPORTED` | validated |
| `GTW_frontSeatHeaterGridType` | page 8 | Gateway: front seat heater grid type | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `STANDARD`<br>1 = `LARGER_SURFACE_AREA` | validated |
| `GTW_frontSeatSideSwitchType` | page 8 | Gateway: front seat side switch type | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `STANDARD`<br>1 = `NONE` | validated |
| `GTW_sohRegulatoryStatus` | page 8 | Gateway: soh regulatory status | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NON_REGULATED_SOH`<br>1 = `REGULATED_SOH` | validated |
| `GTW_passengerTiltMotorType` | page 8 | Gateway: passenger tilt motor type | 11\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INSTALLED_DEFAULT`<br>1 = `NONE`<br>2 = `MINITILT` | validated |
| `GTW_frunkInteriorReleaseType` | page 8 | Gateway: frunk interior release type | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `TYPE_1`<br>1 = `NOT_INSTALLED` | validated |
| `GTW_m3yBusArchitecture` | page 8 | Reports notable features of vehicle communication bus architecture. Used for firmware artifact selection during update installation process. | 17\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `PUBLIC_TORQUE`<br>1 = `PRIVATE_TORQUE`<br>2 = `PRIVATE_TORQUE_CHASSIS` | validated |
| `GTW_passengerLiftMotorType` | page 8 | Gateway: passenger lift motor type | 19\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `INSTALLED_DEFAULT`<br>1 = `NONE`<br>2 = `BOSCH_KEIPER_COMMON` | validated |
| `GTW_interiorUpperTrimType` | page 8 | Gateway: interior upper trim type | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `POLAR_GREY`<br>1 = `MAMMOTH_BLACK` | validated |
| `GTW_blindSpotIndicatorLightType` | page 8 | Gateway: blind spot indicator light type | 22\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NOT_INSTALLED`<br>1 = `INSTALLED_TYPE_1`<br>2 = `INSTALLED_TYPE_2` | validated |
| `GTW_wiperMotorAsicType` | page 8 | Gateway: wiper motor asic type | 24\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKNOWN_OR_NA`<br>1 = `TYPE_1`<br>2 = `TYPE_2` | validated |
| `GTW_hvacCaseDoorType` | page 8 | Gateway: hvac case door type | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `SERRATED_EDGE`<br>1 = `FLAT_EDGE` | validated |
| `GTW_occupancyDetectionSourceRequest` | page 8 | Gateway: occupancy detection source request | 29\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DISCRETE_SENSOR_OR_NA`<br>1 = `TESLA_CABIN_RADAR` | validated |
| `GTW_rduCableType` | page 8 | Indicates type of rear drive unit cable installed on vehicle. | 31\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `ALUMINUM`<br>1 = `COPPER` | validated |
| `GTW_parkTelltaleBehaviorType` | page 8 | Gateway: park telltale behavior type | 32\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `LEGACY_BEHAVIOR`<br>1 = `TYPE_1_REVISED_BEHAVIOR` | validated |
| `GTW_numberKeyCardsPairedInFactory` | page 8 | Gateway: number key cards paired in factory | 35\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 1 = `1`<br>2 = `2` | validated |
| `GTW_secondRowSeatVentilationType` | page 8 | Gateway: second row seat ventilation type | 37\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NONE`<br>1 = `TWO_SEATS_GENTHERM` | validated |
| `GTW_thirdRowSeatHeaterType` | page 8 | Gateway: third row seat heater type | 38\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NONE`<br>1 = `TWO_SEATS_KONGSBERG` | validated |
| `GTW_interiorCameraType` | page 8 | Gateway: interior camera type | 39\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `AR0136`<br>1 = `VD6763`<br>2 = `VD1942` | validated |
| `GTW_frontFasciaCameraType` | page 8 | Reports type of forward facing fascia camera installed. | 41\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `NONE`<br>1 = `IMX963`<br>2 = `IMX00N` | validated |
| `GTW_interiorCamFanType` | page 8 | Gateway: interior cam fan type | 45\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `NONE`<br>2 = `DELTA_FDB`<br>3 = `NIDEC` | validated |
| `GTW_puddleLampType` | page 8 | Gateway: puddle lamp type | 50\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `NOT_INSTALLED`<br>1 = `INSTALLED_TYPE_1`<br>2 = `INSTALLED_1R_ONLY_TYPE_1` | validated |
| `GTW_solarLensType` | page 8 | Gateway: solar lens type | 52\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `BCS`<br>1 = `PEGATRON` | validated |
| `GTW_liftgateGeometryType` | page 8 | Gateway: liftgate geometry type | 56\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DEFAULT`<br>1 = `TYPE_1`<br>2 = `TYPE_2` | validated |
| `GTW_repeaterAeroRibType` | page 8 | Gateway: repeater aero rib type | 60\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `UNOPTIMIZED`<br>3 = `OPTIMIZED`<br>4 = `RETROFIT_OPTIMIZED` | validated |
| `GTW_highTipForceWiperArmsType` | page 8 | Gateway: high tip force wiper arms type | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NOT_INSTALLED`<br>1 = `INSTALLED_TYPE_1` | validated |
| `GTW_rcmUndersideAbuseZThreshold` | page 9 | Gateway: rcm underside abuse z threshold | 8\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `threshold0`<br>1 = `threshold1`<br>2 = `threshold2`<br>3 = `threshold3`<br>4 = `threshold4`<br>5 = `threshold5`<br>6 = `threshold6`<br>7 = `threshold7` | validated |
| `GTW_rcmUndersideAbuseYThreshold` | page 9 | Gateway: rcm underside abuse y threshold | 11\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `threshold0`<br>1 = `threshold1`<br>2 = `threshold2`<br>3 = `threshold3`<br>4 = `threshold4`<br>5 = `threshold5`<br>6 = `threshold6`<br>7 = `threshold7` | validated |
| `GTW_rcmUndersideAbuseWindow` | page 9 | Gateway: rcm underside abuse window | 14\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `window0`<br>1 = `window1`<br>2 = `window2`<br>3 = `window3` | validated |
| `GTW_uhfChargePortEnabled` | page 9 | Gateway: uhf charge port enabled | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `ENABLED`<br>1 = `DISABLED` | validated |
| `GTW_automaticFeatureResetPackage` | page 9 | Gateway: automatic feature reset package | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NONE`<br>1 = `TYPE_1` | validated |
| `GTW_autopilotFeaturePackage` | page 9 | Gateway: autopilot feature package | 20\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `LEGACY_AND_FSD`<br>1 = `TACC_AND_FSD_ONLY` | validated |
| `GTW_doorLatchType` | page 9 | Gateway: door latch type | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DIGITAL`<br>1 = `SELF_TESTABLE` | validated |
| `GTW_headlinerMaterialType` | page 9 | Gateway: headliner material type | 25\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `POLYCARBONATE_ABS`<br>1 = `POLYURETHANE_FIBERGLASS`<br>2 = `POLYURETHANE_FIBERGLASS_LIGHT` | validated |
| `GTW_glareShieldHeaterType` | page 9 | Gateway: glare shield heater type | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NONE`<br>1 = `TYPE_1` | validated |
| `GTW_rearLightHardwareVariant` | page 9 | Gateway: rear light hardware variant | 29\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `V1`<br>1 = `V2`<br>2 = `V3` | validated |
| `GTW_fasciaHarnessCleanPointType` | page 9 | Gateway: fascia harness clean point type | 31\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `UNKOWN`<br>1 = `PRE_CLEANPOINT`<br>2 = `POST_CLEANPOINT` | validated |
| `GTW_epasSubType` | page 9 | Gateway: epas sub type | 33\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `GEN3_OR_NA`<br>1 = `GEN4` | validated |
| `GTW_wiperSupplyChainOrigin` | page 9 | Gateway: wiper supply chain origin; raw 0 = signal not available (SNA) | 35\|2 | little-endian | unsigned | 1 | 0 |  | 1 to 3 | 0 = `UNKNOWN_OR_SNA`<br>1 = `CN_SUPPLY_CHAIN`<br>2 = `NA_SUPPLY_CHAIN` | validated |
| `GTW_windowPinchParameterType` | page 9 | Gateway: window pinch parameter type | 37\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 3 | 0 = `DEFAULT`<br>1 = `TYPE_1`<br>2 = `TYPE_2` | validated |
| `GTW_badgingMaterialType` | page 9 | Gateway: badging material type | 39\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `CHROME_SILVER`<br>1 = `BLACK_MATTE` | validated |
| `GTW_mRecordVersion` | page 9 | Gateway: m record version | 40\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `VER_2016_OR_NA`<br>1 = `VER_2025` | validated |
| `GTW_tcuType` | page 9 | Gateway: tcu type | 47\|2 | little-endian | unsigned | 1 | 0 |  | 0 to 2 | 0 = `4G`<br>1 = `5G` | validated |
| `GTW_carbComplianceBehaviorType` | page 9 | Gateway: carb compliance behavior type | 49\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NONE`<br>1 = `ACCII_2026_BEHAVIOR` | validated |
| `GTW_indirectTPMSCalibrationType` | page 9 | Indirect TPMS calibration type. | 55\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `STANDARD`<br>1 = `STANDARD_EU`<br>2 = `EXPERIMENTAL_V1`<br>3 = `EXPERIMENTAL_V1_EU`<br>4 = `EXPERIMENTAL_V2` | validated |
| `GTW_v2xEnabled` | page 9 | Gateway: v2x enabled | 58\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `ENABLED`<br>1 = `DISABLED` | validated |
| `GTW_liftgateStrutType` | page 9 | Gateway: liftgate strut type | 60\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `DEFAULT`<br>1 = `TYPE_1` | validated |
| `GTW_exteriorMicrophoneType` | page 9 | Gateway: exterior microphone type | 63\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NONE`<br>1 = `TWO_EXT_MICS` | validated |
| `GTW_contactorPowerSource` | page 10 | Gateway: contactor power source | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `VCRIGHT`<br>1 = `VCFRONT` | validated |
| `GTW_roofGlassType` | page 10 | Gateway: roof glass type | 21\|3 | little-endian | unsigned | 1 | 0 |  | 0 to 7 | 0 = `TSA3_PET`<br>1 = `TSA5_NOPET`<br>2 = `NONE`<br>3 = `UNCOATED`<br>4 = `AG3` | validated |
| `GTW_pedalMapNameOverride` | page 10 | Gateway: pedal map name override | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 | 0 = `NO_OVERRIDE`<br>1 = `CHILL_STANDARD` | validated |

## Multiplexing

`GTW_carConfigMultiplexer` is the multiplexer selector of this message. Its value picks which group of signals is valid in a frame: page 1 (12 signals), page 2 (33 signals), page 3 (20 signals), page 4 (10 signals), page 5 (25 signals), page 6 (25 signals), page 7 (24 signals), page 8 (25 signals), page 9 (22 signals), page 10 (3 signals). Signals without a page are present in every frame.

## Download the DBC file

- [Tesla Model 3 / Model Y 2026.26.6.5 VEH DBC file](../../../../../dbc/AllModels/2026.26.6.5/VEH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/AllModels/2026.26.6.5/VEH.json)

## See also

- [All Gateway messages (GTW)](../../gtw.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
