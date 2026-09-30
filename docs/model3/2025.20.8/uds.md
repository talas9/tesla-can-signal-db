---
layout: default
title: "UDS ECU (UDS) CAN messages and signals — Tesla Model 3 2025.20.8"
description: "Tesla Model 3 UDS CAN bus messages and signals of the UDS ECU (UDS) for firmware 2025.20.8: 44 messages, 56 signals with bit layout, scaling and value tables."
---

# UDS ECU (UDS) CAN messages and signals — Tesla Model 3 2025.20.8

All 44 messages of the UDS ECU (UDS) documented for Tesla Model 3 firmware 2025.20.8, across the buses that carry them.

| Message | Bus | Id | Length | Cycle | Signals |
|---|---|---|---:|---:|---:|
| [`UDS_bmsRequest`](eth/uds/uds_bmsrequest.md) | ETH | 0x602 | 8 |  | 1 |
| [`UDS_ccRequest`](eth/uds/uds_ccrequest.md) | ETH | 0x62B | 8 |  | 1 |
| [`UDS_cmpdRequest`](eth/uds/uds_cmpdrequest.md) | ETH | 0x607 | 8 |  | 1 |
| [`UDS_cmpRequest`](eth/uds/uds_cmprequest.md) | ETH | 0x603 | 8 |  | 1 |
| [`UDS_cpRequest`](eth/uds/uds_cprequest.md) | ETH | 0x60E | 8 |  | 1 |
| [`UDS_dasRequest`](eth/uds/uds_dasrequest.md) | ETH | 0x649 | 8 |  | 1 |
| [`UDS_difRequest`](eth/uds/uds_difrequest.md) | ETH | 0x605 | 8 |  | 1 |
| [`UDS_diRequest`](eth/uds/uds_direquest.md) | ETH | 0x635 | 8 |  | 1 |
| [`UDS_dirRequest`](eth/uds/uds_dirrequest.md) | ETH | 0x606 | 8 |  | 1 |
| [`UDS_epas3pRequest`](eth/uds/uds_epas3prequest.md) | ETH | 0x630 | 8 |  | 1 |
| [`UDS_epas3sRequest`](eth/uds/uds_epas3srequest.md) | ETH | 0x730 | 8 |  | 1 |
| [`UDS_epblRequest`](eth/uds/uds_epblrequest.md) | ETH | 0x624 | 8 |  | 2 |
| [`UDS_epbrRequest`](eth/uds/uds_epbrrequest.md) | ETH | 0x626 | 8 |  | 2 |
| [`UDS_espRequest`](eth/uds/uds_esprequest.md) | ETH | 0x645 | 8 |  | 1 |
| [`UDS_functionalRequest`](eth/uds/uds_functionalrequest.md) | ETH | 0x7DF | 8 |  | 8 |
| [`UDS_functionalRequest_CH`](eth/uds/uds_functionalrequest_ch.md) | ETH | 0x7DE | 8 |  | 1 |
| [`UDS_hvpRequest`](eth/uds/uds_hvprequest.md) | ETH | 0x610 | 8 |  | 1 |
| [`UDS_ibstRequest`](eth/uds/uds_ibstrequest.md) | ETH | 0x64D | 8 |  | 1 |
| [`UDS_icrRequest`](eth/uds/uds_icrrequest.md) | ETH | 0x618 | 8 |  | 1 |
| [`UDS_KOSTIAsccmRequest`](eth/uds/uds_kostiasccmrequest.md) | ETH | 0x669 | 8 |  | 1 |
| [`UDS_ocs1pRequest`](eth/uds/uds_ocs1prequest.md) | ETH | 0x643 | 8 |  | 1 |
| [`UDS_parkRequest`](eth/uds/uds_parkrequest.md) | ETH | 0x64E | 8 |  | 1 |
| [`UDS_pcsRequest`](eth/uds/uds_pcsrequest.md) | ETH | 0x628 | 8 |  | 1 |
| [`UDS_plgRequest`](eth/uds/uds_plgrequest.md) | ETH | 0x662 | 8 |  | 1 |
| [`UDS_pmfRequest`](eth/uds/uds_pmfrequest.md) | ETH | 0x644 | 8 |  | 1 |
| [`UDS_pmRequest`](eth/uds/uds_pmrequest.md) | ETH | 0x620 | 8 |  | 1 |
| [`UDS_pmrRequest`](eth/uds/uds_pmrrequest.md) | ETH | 0x604 | 8 |  | 1 |
| [`UDS_ptcRequest`](eth/uds/uds_ptcrequest.md) | ETH | 0x6C6 | 8 |  | 1 |
| [`UDS_radcRequest`](eth/uds/uds_radcrequest.md) | ETH | 0x671 | 8 |  | 1 |
| [`UDS_rcmRequest`](eth/uds/uds_rcmrequest.md) | ETH | 0x641 | 8 |  | 1 |
| [`UDS_sccmRequest`](eth/uds/uds_sccmrequest.md) | ETH | 0x680 | 8 |  | 1 |
| [`UDS_sdcrRequest`](eth/uds/uds_sdcrrequest.md) | ETH | 0x6BB | 8 |  | 1 |
| [`UDS_tasRequest`](eth/uds/uds_tasrequest.md) | ETH | 0x64B | 8 |  | 1 |
| [`UDS_thcRequest`](eth/uds/uds_thcrequest.md) | ETH | 0x60F | 8 |  | 2 |
| [`UDS_tpmsRequest`](eth/uds/uds_tpmsrequest.md) | ETH | 0x64F | 8 |  | 1 |
| [`UDS_vcbatt1Request`](eth/uds/uds_vcbatt1request.md) | ETH | 0x62A | 8 |  | 1 |
| [`UDS_vcbatt2Request`](eth/uds/uds_vcbatt2request.md) | ETH | 0x634 | 8 |  | 1 |
| [`UDS_vcbattRequest`](eth/uds/uds_vcbattrequest.md) | ETH | 0x664 | 8 |  | 1 |
| [`UDS_vcfront1Request`](eth/uds/uds_vcfront1request.md) | ETH | 0x62C | 8 |  | 1 |
| [`UDS_vcfront2Request`](eth/uds/uds_vcfront2request.md) | ETH | 0x62E | 8 |  | 1 |
| [`UDS_vcfrontRequest`](eth/uds/uds_vcfrontrequest.md) | ETH | 0x600 | 8 |  | 1 |
| [`UDS_vcleftRequest`](eth/uds/uds_vcleftrequest.md) | ETH | 0x622 | 8 |  | 2 |
| [`UDS_vcrightRequest`](eth/uds/uds_vcrightrequest.md) | ETH | 0x608 | 8 |  | 2 |
| [`UDS_vcsecRequest`](eth/uds/uds_vcsecrequest.md) | ETH | 0x60A | 8 |  | 1 |

[Documentation home](../../index.md) | [Signal index A-Z](../../signals/index.md)

