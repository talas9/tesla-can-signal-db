---
layout: default
title: "UDS ECU (UDS) CAN messages and signals — Tesla Model 3 / Model Y 2026.26.6.5"
description: "Tesla Model 3 / Model Y UDS CAN bus messages and signals of the UDS ECU (UDS) for firmware 2026.26.6.5: 44 messages, 56 signals with bit layout, scaling and value tables."
---

# UDS ECU (UDS) CAN messages and signals — Tesla Model 3 / Model Y 2026.26.6.5

All 44 messages of the UDS ECU (UDS) documented for Tesla Model 3 / Model Y firmware 2026.26.6.5, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`UDS_bmsRequest`](veh/uds/uds_bmsrequest.md) | VEH | 0x602 | 8 |  | 1 |
| [`UDS_ccRequest`](veh/uds/uds_ccrequest.md) | VEH | 0x62B | 8 |  | 1 |
| [`UDS_cmpdRequest`](veh/uds/uds_cmpdrequest.md) | VEH | 0x607 | 8 |  | 1 |
| [`UDS_cmpRequest`](veh/uds/uds_cmprequest.md) | VEH | 0x603 | 8 |  | 1 |
| [`UDS_cpRequest`](veh/uds/uds_cprequest.md) | VEH | 0x60E | 8 |  | 1 |
| [`UDS_difRequest`](veh/uds/uds_difrequest.md) | VEH | 0x605 | 8 |  | 1 |
| [`UDS_diRequest`](veh/uds/uds_direquest.md) | VEH | 0x635 | 8 |  | 1 |
| [`UDS_dirRequest`](veh/uds/uds_dirrequest.md) | VEH | 0x606 | 8 |  | 1 |
| [`UDS_epblRequest`](veh/uds/uds_epblrequest.md) | VEH | 0x624 | 8 |  | 2 |
| [`UDS_epbrRequest`](veh/uds/uds_epbrrequest.md) | VEH | 0x626 | 8 |  | 2 |
| [`UDS_functionalRequest`](veh/uds/uds_functionalrequest.md) | VEH | 0x7DF | 8 |  | 8 |
| [`UDS_hvpRequest`](veh/uds/uds_hvprequest.md) | VEH | 0x610 | 8 |  | 1 |
| [`UDS_icrRequest`](veh/uds/uds_icrrequest.md) | VEH | 0x618 | 8 |  | 1 |
| [`UDS_KOSTIAsccmRequest`](veh/uds/uds_kostiasccmrequest.md) | VEH | 0x669 | 8 |  | 1 |
| [`UDS_pcsRequest`](veh/uds/uds_pcsrequest.md) | VEH | 0x628 | 8 |  | 1 |
| [`UDS_plgRequest`](veh/uds/uds_plgrequest.md) | VEH | 0x662 | 8 |  | 1 |
| [`UDS_pmfRequest`](veh/uds/uds_pmfrequest.md) | VEH | 0x644 | 8 |  | 1 |
| [`UDS_pmRequest`](veh/uds/uds_pmrequest.md) | VEH | 0x620 | 8 |  | 1 |
| [`UDS_pmrRequest`](veh/uds/uds_pmrrequest.md) | VEH | 0x604 | 8 |  | 1 |
| [`UDS_ptcRequest`](veh/uds/uds_ptcrequest.md) | VEH | 0x6C6 | 8 |  | 1 |
| [`UDS_sccmRequest`](veh/uds/uds_sccmrequest.md) | VEH | 0x680 | 8 |  | 1 |
| [`UDS_sdcrRequest`](veh/uds/uds_sdcrrequest.md) | VEH | 0x6BB | 8 |  | 1 |
| [`UDS_tasRequest`](veh/uds/uds_tasrequest.md) | VEH | 0x64B | 8 |  | 1 |
| [`UDS_vcbatt1Request`](veh/uds/uds_vcbatt1request.md) | VEH | 0x60C | 8 |  | 1 |
| [`UDS_vcbatt2Request`](veh/uds/uds_vcbatt2request.md) | VEH | 0x61A | 8 |  | 1 |
| [`UDS_vcbattRequest`](veh/uds/uds_vcbattrequest.md) | VEH | 0x661 | 8 |  | 1 |
| [`UDS_vcfront1Request`](veh/uds/uds_vcfront1request.md) | VEH | 0x62C | 8 |  | 1 |
| [`UDS_vcfront2Request`](veh/uds/uds_vcfront2request.md) | VEH | 0x62E | 8 |  | 1 |
| [`UDS_vcfrontRequest`](veh/uds/uds_vcfrontrequest.md) | VEH | 0x600 | 8 |  | 1 |
| [`UDS_vcleftRequest`](veh/uds/uds_vcleftrequest.md) | VEH | 0x622 | 8 |  | 2 |
| [`UDS_vcrightRequest`](veh/uds/uds_vcrightrequest.md) | VEH | 0x608 | 8 |  | 2 |
| [`UDS_vcsecRequest`](veh/uds/uds_vcsecrequest.md) | VEH | 0x60A | 8 |  | 1 |
| [`UDS_dasRequest`](ch/uds/uds_dasrequest.md) | CH | 0x649 | 8 |  | 1 |
| [`UDS_epas3pRequest`](ch/uds/uds_epas3prequest.md) | CH | 0x630 | 8 |  | 1 |
| [`UDS_epas3sRequest`](ch/uds/uds_epas3srequest.md) | CH | 0x730 | 8 |  | 1 |
| [`UDS_espRequest`](ch/uds/uds_esprequest.md) | CH | 0x645 | 8 |  | 1 |
| [`UDS_functionalRequest_CH`](ch/uds/uds_functionalrequest_ch.md) | CH | 0x7DF | 8 |  | 1 |
| [`UDS_ibstRequest`](ch/uds/uds_ibstrequest.md) | CH | 0x64D | 8 |  | 1 |
| [`UDS_parkRequest`](ch/uds/uds_parkrequest.md) | CH | 0x64E | 8 |  | 1 |
| [`UDS_radcRequest`](ch/uds/uds_radcrequest.md) | CH | 0x671 | 8 |  | 1 |
| [`UDS_rcmRequest`](ch/uds/uds_rcmrequest.md) | CH | 0x641 | 8 |  | 1 |
| [`UDS_tpmsRequest`](ch/uds/uds_tpmsrequest.md) | CH | 0x64F | 8 |  | 1 |
| [`UDS_ocs1pRequest`](eth/uds/uds_ocs1prequest.md) | ETH | 0x643 | 8 |  | 1 |
| [`UDS_thcRequest`](eth/uds/uds_thcrequest.md) | ETH | 0x60F | 8 |  | 2 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

