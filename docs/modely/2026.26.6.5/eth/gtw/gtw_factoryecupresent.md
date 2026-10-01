---
layout: default
title: "GTW_factoryEcuPresent (0x560) — Gateway, Tesla Model Y 2026.26.6.5 ETH"
description: "Gateway message: factory ecu present. Ethernet-side message GTW_factoryEcuPresent of Gateway for Tesla Model Y firmware 2026.26.6.5, 28 signals (GTW_OCS1Ppresent, GTW_PCSpresent, GTW_HVPpresent, GTW_BMSpresent and 24 more). Bit layout, scaling, units and value tables."
---

# GTW_factoryEcuPresent (0x560) — Gateway, Tesla Model Y 2026.26.6.5 ETH

Gateway message: factory ecu present. This page documents the 28 signals of GTW_factoryEcuPresent as defined for Tesla Model Y firmware 2026.26.6.5 (Ethernet-side id, not a CAN id).

## Message details

| Property | Value |
|---|---|
| Message name | `GTW_factoryEcuPresent` |
| Ethernet-side id | 0x560 (1376) |
| ECU | [Gateway](../../gtw.md) |
| Vehicle | Tesla Model Y |
| Firmware | 2026.26.6.5 |
| Bus | ETH (Ethernet-side ids, not CAN ids) |
| Transmitter | GTW |
| Frame length | 4 bytes |
| Cycle time | 1000 ms |
| Signals | 28 |

## Signals of GTW_factoryEcuPresent

Tesla Model Y CAN bus signals in `GTW_factoryEcuPresent`: start bit and length, byte order, scaling, unit, range, value table and confidence.

| Signal | Meaning | Start\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| `GTW_OCS1Ppresent` | Gateway: OCS1 ppresent | 0\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_PCSpresent` | Gateway: PC spresent | 1\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_HVPpresent` | Gateway: HV ppresent | 2\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_BMSpresent` | Gateway: BM spresent | 3\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_CPpresent` | Gateway: c ppresent | 4\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_RCMpresent` | Gateway: RC mpresent | 5\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_SCCMpresent` | Gateway: SCC mpresent | 6\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_VCSECpresent` | Gateway: VCSE cpresent | 7\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_EPAS3Ppresent` | Gateway: EPAS3 ppresent | 8\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_EPBLpresent` | Gateway: EPB lpresent | 9\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_EPBRpresent` | Gateway: EPB rpresent | 10\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_ESPpresent` | Gateway: ES ppresent | 11\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_IBSTpresent` | Gateway: IBS tpresent | 12\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_PARKpresent` | Gateway: PAR kpresent | 13\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_RADCpresent` | Gateway: RAD cpresent | 14\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_TPMSpresent` | Gateway: TPM spresent | 15\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_VCFRONTpresent` | Gateway: VCFRON tpresent | 16\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_VCLEFTpresent` | Gateway: VCLEF tpresent | 17\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_VCRIGHTpresent` | Gateway: VCRIGH tpresent | 18\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_EPAS3Spresent` | Gateway: EPAS3 spresent | 19\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_CMPpresent` | Gateway: CM ppresent | 20\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_DASpresent` | Gateway: DA spresent | 21\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_PTCpresent` | Gateway: PT cpresent | 22\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_SWCpresent` | Gateway: SW cpresent | 23\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_PMRpresent` | Gateway: PM rpresent | 25\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_PMFpresent` | Gateway: PM fpresent | 26\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_DIRpresent` | Gateway: DI rpresent | 27\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |
| `GTW_DIFpresent` | Gateway: DI fpresent | 28\|1 | little-endian | unsigned | 1 | 0 |  | 0 to 1 |  | layout-only |

## Download the DBC file

- [Tesla Model Y 2026.26.6.5 ETH DBC file](../../../../../dbc/ModelY/2026.26.6.5/ETH.dbc) (Vector DBC)
- [Same data as JSON](../../../../../dbc/ModelY/2026.26.6.5/ETH.json)

Ethernet-side ids differ from CAN ids; do not load this file on a CAN bus.

## See also

- [All Gateway messages (GTW)](../../gtw.md)
- [Signal index A-Z](../../../../signals/index.md)
- [All messages](../../../../messages.md)
- [Documentation home](../../../../index.md)
