---
layout: default
title: "Touchscreen user interface computer (UI) CAN messages and signals — Tesla Model 3 2025.20.8"
description: "Tesla Model 3 UI CAN bus messages and signals of the Touchscreen user interface computer (UI) for firmware 2025.20.8: 76 messages, 1331 signals with bit layout, scaling and value tables."
---

# Touchscreen user interface computer (UI) CAN messages and signals — Tesla Model 3 2025.20.8

All 76 messages of the Touchscreen user interface computer (UI) documented for Tesla Model 3 firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`UI_chassisControl`](veh/ui/ui_chassiscontrol.md) | VEH | 0x293 | 8 | 500 ms | 28 |
| [`UI_debugECU`](veh/ui/ui_debugecu.md) | VEH | 0x500 | 2 | 5000 ms | 15 |
| [`UI_debugTas`](veh/ui/ui_debugtas.md) | VEH | 0x7FB | 8 | 2000 ms | 8 |
| [`UI_driverAssistMapData`](veh/ui/ui_driverassistmapdata.md) | VEH | 0x238 | 8 | 500 ms | 30 |
| [`UI_driverProfileRecall2`](veh/ui/ui_driverprofilerecall2.md) | VEH | 0x28B | 5 | 500 ms | 5 |
| [`UI_elevationStatus`](veh/ui/ui_elevationstatus.md) | VEH | 0x3D8 | 4 | 1000 ms | 2 |
| [`UI_gpsTime`](veh/ui/ui_gpstime.md) | VEH | 0x324 | 8 | 1000 ms | 1 |
| [`UI_gpsVehicleSpeed`](veh/ui/ui_gpsvehiclespeed.md) | VEH | 0x373 | 8 | 1000 ms | 11 |
| [`UI_hvacRequest`](veh/ui/ui_hvacrequest.md) | VEH | 0x2F3 | 8 | 500 ms | 26 |
| [`UI_IsoTpPipeRemoteVCSEC`](veh/ui/ui_isotppiperemotevcsec.md) | VEH | 0x482 | 8 |  | 8 |
| [`UI_IsoTpUDPPipeVCSEC`](veh/ui/ui_isotpudppipevcsec.md) | VEH | 0x481 | 8 |  | 8 |
| [`UI_locationStatus`](veh/ui/ui_locationstatus.md) | VEH | 0x309 | 8 | 1000 ms | 3 |
| [`UI_odo`](veh/ui/ui_odo.md) | VEH | 0x5F3 | 3 | 1000 ms | 1 |
| [`UI_peripheralPowerRequests`](veh/ui/ui_peripheralpowerrequests.md) | VEH | 0x3B4 | 1 | 500 ms | 1 |
| [`UI_powerEstimates`](veh/ui/ui_powerestimates.md) | VEH | 0x33B | 6 | 1000 ms | 4 |
| [`UI_powerRationalityConfig`](veh/ui/ui_powerrationalityconfig.md) | VEH | 0x295 | 8 | 5000 ms | 41 |
| [`UI_range`](veh/ui/ui_range.md) | VEH | 0x33A | 8 | 1000 ms | 6 |
| [`UI_solarData`](veh/ui/ui_solardata.md) | VEH | 0x2D3 | 8 | 1000 ms | 7 |
| [`UI_status`](veh/ui/ui_status.md) | VEH | 0x353 | 8 | 1000 ms | 26 |
| [`UI_suspensionControl`](veh/ui/ui_suspensioncontrol.md) | VEH | 0x297 | 8 | 500 ms | 12 |
| [`UI_vehicleControl`](veh/ui/ui_vehiclecontrol.md) | VEH | 0x273 | 8 | 500 ms | 39 |
| [`UI_chassisControl`](ch/ui/ui_chassiscontrol.md) | CH | 0x293 | 8 | 500 ms | 28 |
| [`UI_csaOfframpCurvature`](ch/ui/ui_csaofframpcurvature.md) | CH | 0x298 | 8 | 500 ms | 7 |
| [`UI_csaRoadCurvature`](ch/ui/ui_csaroadcurvature.md) | CH | 0x2A7 | 8 | 500 ms | 7 |
| [`UI_driverAssistAnonDebugParams`](ch/ui/ui_driverassistanondebugparams.md) | CH | 0x448 | 8 | 1000 ms | 12 |
| [`UI_driverAssistControl`](ch/ui/ui_driverassistcontrol.md) | CH | 0x3F8 | 8 | 1000 ms | 45 |
| [`UI_driverAssistMapData`](ch/ui/ui_driverassistmapdata.md) | CH | 0x238 | 8 | 500 ms | 30 |
| [`UI_driverAssistRoadSign`](ch/ui/ui_driverassistroadsign.md) | CH | 0x218 | 8 | 500 ms | 20 |
| [`UI_dynamicTriggersCampaignFired`](ch/ui/ui_dynamictriggerscampaignfired.md) | CH | 0x7B3 | 8 | 500 ms | 1 |
| [`UI_gpsVehicleSpeed`](ch/ui/ui_gpsvehiclespeed.md) | CH | 0x2F8 | 8 | 1000 ms | 11 |
| [`UI_locationOffset`](ch/ui/ui_locationoffset.md) | CH | 0x3D9 | 8 | 1000 ms | 2 |
| [`UI_locationStatus`](ch/ui/ui_locationstatus.md) | CH | 0x309 | 8 | 1000 ms | 3 |
| [`UI_odo`](ch/ui/ui_odo.md) | CH | 0x3F3 | 3 | 1000 ms | 1 |
| [`UI_phoneLocationStatus`](ch/ui/ui_phonelocationstatus.md) | CH | 0x3DB | 8 | 1000 ms | 3 |
| [`UI_radarMapData`](ch/ui/ui_radarmapdata.md) | CH | 0x2BA | 8 | 500 ms | 6 |
| [`UI_roadCurvature`](ch/ui/ui_roadcurvature.md) | CH | 0x278 | 8 | 500 ms | 7 |
| [`UI_solarData`](ch/ui/ui_solardata.md) | CH | 0x2D3 | 8 | 1000 ms | 7 |
| [`UI_status`](ch/ui/ui_status.md) | CH | 0x353 | 8 | 1000 ms | 26 |
| [`UI_summonGoal`](ch/ui/ui_summongoal.md) | CH | 0x3DC | 8 | 1000 ms | 3 |
| [`UI_telemetryControl`](ch/ui/ui_telemetrycontrol.md) | CH | 0x428 | 8 | 1000 ms | 17 |
| [`UI_tpmsMode`](ch/ui/ui_tpmsmode.md) | CH | 0x358 | 4 |  | 4 |
| [`UI_ussThresholdsX`](ch/ui/ui_ussthresholdsx.md) | CH | 0x723 | 8 |  | 14 |
| [`UI_ussThresholdsY`](ch/ui/ui_ussthresholdsy.md) | CH | 0x725 | 8 |  | 14 |
| [`UI_airbagCutoffStatus`](eth/ui/ui_airbagcutoffstatus.md) | ETH | 0x3D3 | 1 | 500 ms | 2 |
| [`UI_alertLog`](eth/ui/ui_alertlog.md) | ETH | 0x5F3 | 8 |  | 89 |
| [`UI_alertMatrix1`](eth/ui/ui_alertmatrix1.md) | ETH | 0x123 | 8 | 1000 ms | 63 |
| [`UI_alertMatrix2`](eth/ui/ui_alertmatrix2.md) | ETH | 0x124 | 8 | 1000 ms | 63 |
| [`UI_alertMatrix3`](eth/ui/ui_alertmatrix3.md) | ETH | 0x125 | 8 | 1000 ms | 63 |
| [`UI_alertMatrix4`](eth/ui/ui_alertmatrix4.md) | ETH | 0x126 | 8 | 1000 ms | 47 |
| [`UI_ambientLightingCtrls`](eth/ui/ui_ambientlightingctrls.md) | ETH | 0x679 | 7 | 500 ms | 13 |
| [`UI_autopilotControl`](eth/ui/ui_autopilotcontrol.md) | ETH | 0x3FD | 8 | 500 ms | 74 |
| [`UI_chargeRequest`](eth/ui/ui_chargerequest.md) | ETH | 0x333 | 5 | 500 ms | 18 |
| [`UI_cruiseControl`](eth/ui/ui_cruisecontrol.md) | ETH | 0x213 | 2 | 500 ms | 4 |
| [`UI_driverProfileRecall`](eth/ui/ui_driverprofilerecall.md) | ETH | 0x285 | 8 | 500 ms | 23 |
| [`UI_energyConsumptionInfo`](eth/ui/ui_energyconsumptioninfo.md) | ETH | 0x4FF | 8 | 1000 ms | 63 |
| [`UI_ethNm`](eth/ui/ui_ethnm.md) | ETH | 0x473 | 8 | 500 ms | 3 |
| [`UI_frontSeatRequests`](eth/ui/ui_frontseatrequests.md) | ETH | 0x4F3 | 3 | 500 ms | 8 |
| [`UI_power`](eth/ui/ui_power.md) | ETH | 0x3BB | 2 | 1000 ms | 2 |
| [`UI_powertrainControl`](eth/ui/ui_powertraincontrol.md) | ETH | 0x334 | 8 | 500 ms | 18 |
| [`UI_stalklessControl`](eth/ui/ui_stalklesscontrol.md) | ETH | 0x233 | 6 | 500 ms | 16 |
| [`UI_stalklessHealthStatus`](eth/ui/ui_stalklesshealthstatus.md) | ETH | 0x2BB | 2 | 500 ms | 7 |
| [`UI_status2`](eth/ui/ui_status2.md) | ETH | 0x3DF | 8 | 500 ms | 21 |
| [`UI_systemMonitor`](eth/ui/ui_systemmonitor.md) | ETH | 0x295 | 8 | 15000 ms | 12 |
| [`UI_tpmsRCPsetting`](eth/ui/ui_tpmsrcpsetting.md) | ETH | 0x3B8 | 4 | 1000 ms | 2 |
| [`UI_trackModeSettings`](eth/ui/ui_trackmodesettings.md) | ETH | 0x313 | 8 | 500 ms | 9 |
| [`UI_tripPlanning`](eth/ui/ui_tripplanning.md) | ETH | 0x82 | 8 | 1000 ms | 9 |
| [`UI_tripPlanning2`](eth/ui/ui_tripplanning2.md) | ETH | 0x8B | 6 | 1000 ms | 3 |
| [`UI_tripPlanning3`](eth/ui/ui_tripplanning3.md) | ETH | 0x495 | 8 | 1000 ms | 4 |
| [`UI_tripPlanning4`](eth/ui/ui_tripplanning4.md) | ETH | 0x496 | 6 | 1000 ms | 4 |
| [`UI_tripPlanning5`](eth/ui/ui_tripplanning5.md) | ETH | 0x497 | 6 | 1000 ms | 3 |
| [`UI_vehicleControl2`](eth/ui/ui_vehiclecontrol2.md) | ETH | 0x3B3 | 8 | 500 ms | 41 |
| [`UI_vehicleControl3`](eth/ui/ui_vehiclecontrol3.md) | ETH | 0x274 | 8 | 500 ms | 41 |
| [`UI_vehicleControlThermal`](eth/ui/ui_vehiclecontrolthermal.md) | ETH | 0x355 | 6 | 1000 ms | 15 |
| [`UI_vehicleModes`](eth/ui/ui_vehiclemodes.md) | ETH | 0x284 | 8 | 500 ms | 22 |
| [`UI_ventPanelControlRequest`](eth/ui/ui_ventpanelcontrolrequest.md) | ETH | 0x253 | 8 | 500 ms | 14 |
| [`UI_weatherDataService`](eth/ui/ui_weatherdataservice.md) | ETH | 0x621 | 8 | 500 ms | 5 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

