# Signal Database Index

Signal inventory by firmware; counts and names inside enum tables do not
establish vehicle coverage. See the [README coverage table](README.md#coverage)
for model names, original API names/codenames, and routing versus product-subset scope.

## Source and export inventory

Recounted from the checked-in files on 2026-11-23. Source rows are unique
`(message, signal)` definitions in `data/<firmware>/signals.csv`, not counts
summed across vehicle models or buses. The export columns count the all-message
`dbc/<firmware>/ETH.json` file; its IDs are Ethernet-side IDs, not CAN IDs.

| Firmware | Source messages | Source signal rows | Export messages | Export signals | Dropped source rows |
|---|---:|---:|---:|---:|---:|
| 2026.26.6.5 | 673 | 42,360 | 673 | 42,316 | 44 |
| 2025.20.8 | 609 | 33,447 | 609 | 33,441 | 6 |

The 2026 export drops six rows without a bit layout and 38 overlapping rows.
The 2025 export drops six rows without a bit layout. Each JSON export records
its exclusions in `dropped`; these rows remain in the source CSV. CAN exports
have additional model, routing and frame-length constraints, so their counts
must be read from the README coverage table rather than inferred from these totals.

## Source metadata

These are literal nonempty CSV cells, before metadata enrichment by the
exporter. A row with both a unit and a description counts once in the last
column. These counts are not the exporter’s confidence categories: a missing
unit or description does not itself mean `layout-only`.

| Firmware | With unit | With description | With either |
|---|---:|---:|---:|
| 2026.26.6.5 | 2,387 | 3,360 | 4,539 |
| 2025.20.8 | 1,812 | 2,654 | 3,567 |

The current confidence counts, after `signal-meta.csv` and `validation.csv`
are applied, are generated in the [README coverage table](README.md#coverage).
The former approximate device-prefix totals and enrichment percentages have
been replaced by these directly countable inventories.

## DBC files

- `dbc/<model>/<firmware>/<BUS>.dbc` — CAN DBC files with real on-bus CAN IDs (`VEH`, `CH`, `PARTY`); see README for coverage.
- `dbc/<firmware>/ETH.dbc` — every exported message under its Ethernet-side ID; not for use on a CAN bus.
- Each DBC has a JSON twin with signal confidence and dropped-row details.

## Source data

- [2026.26.6.5 CSV](data/2026.26.6.5/signals.csv) and [JSON](data/2026.26.6.5/signals.json).
- [2025.20.8 CSV](data/2025.20.8/signals.csv) and [JSON](data/2025.20.8/signals.json).

## Research supplements

[Older HW3 car-log unavailability field](research/hw3-carlog-unavailability.md)
documents a field absent from these source tables. It is separate research
provenance, excluded from the generated DBCs and coverage counts, with no
claim of validated current HW4 applicability.
