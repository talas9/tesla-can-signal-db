# Older HW3 car-log unavailability field

Status: binary-derived research, separate from the 2025.20.8 and 2026.26.6.5
source tables. Last reviewed 2026-11-23.

## Coverage and missing field

Both source tables define `DAS_carLogMultiplexer` at little-endian bits 0–3.
Their `signal-meta.csv` files name selector value 0 `FEATURE_STATE`, but neither
`signals.csv` contains a mux-0 payload signal for
`DAS_autosteerUnavailableReason`. The generated DBCs therefore do not currently
decode that reason. This is a coverage gap, not evidence that the field is
absent from a vehicle.

The evidence below comes from the **HW3 FSD 12.5.4 September 2024 APE image**,
not from either source-table firmware and not from an HW4 native executable.
It belongs beside, rather than inside, the canonical tables. It contributes
zero signals to this repository's generated coverage totals.

## Binary-derived layout and provenance

The inspected `cantx` emitter registers message ID `0x5D9`, DLC 8. Its mux-0
branch clears payload bits 0–3 and writes the translated unavailable reason
into bits 4–10: unsigned, little-endian, width 7. Physical bus routing for
this emitter was not independently established by this analysis.

| Evidence in the inspected image | Finding |
|---|---|
| `cantx` constructors `0x007244a0` / `0x00728210`, vtable `0x00857748` | `DasCarlogMessageEmitter` registration, ID `0x5D9`, DLC 8 |
| `cantx` update `0x00736430` | Reads the unavailable-reason snapshot at offset `0x80`; translates and packs it into mux 0, bits 4–10 |
| `cantx` translator `0x007c3350`, table `0x006593d4` | Translates internal values 1–94 by table index `value - 1`; out-of-range input returns 0 |
| Native `AutosteerUnavailableReason` names plus the translation-table read | Internal values and serialized values occupy different enum namespaces |

Addresses above use the analysis project's rebased address space: ELF virtual
address plus `0x100000`. They are anchors for this inspected image, not stable
addresses across releases. The underlying decompiler exports and table reads
are retained privately; original binaries and private captures are not
redistributed here. Public context is in the
[APE rejection-evidence summary](https://github.com/talas9/tesla-ape-research/blob/main/LLM.md#november-13-eligibility-and-rejection-evidence).

## Internal values are not wire values

The inspected translator establishes the following subset. This is not a
complete enum definition and must not be extrapolated to the other entries.

| Internal value | Internal name | Wire value |
|---:|---|---:|
| 90 | `USER_SETTINGS_NOT_SUPPORTED` | 91 |
| 91 | `CRUISE_UNAVAILABLE` | 92 |
| 92 | `CRUISE_REQUEST_TIMEOUT` | 93 |
| 93 | `CRUISE_STACK_MISMATCH` | 94 |
| 94 | `UNKNOWN` | 127 |

In particular, wire **91** does not mean internal `CRUISE_UNAVAILABLE` 91.
The shift exists inside the same old binary; it is not solely a difference
between firmware versions. Do not apply this subset to the ACC reason field
at mux 2, bits 46–52, which has its own translator and enum.

For a read-only bit-layout check, the synthetic eight-byte payload
`b0 05 00 00 00 00 00 00` has mux 0 and reason 91:
`(int.from_bytes(payload, "little") >> 4) & 0x7f == 91`.
This is a constructed decoding fixture, not a vehicle capture or a message
to transmit.

## Interpretation limits

- A reason is diagnostic output, not an engagement command or acknowledgement.
- In the inspected old path, multiple ACC internal reasons project to the
  same AS internal 90 / wire 91 result. The AS reason alone does not identify
  which upstream condition failed; correlated AS and ACC reasons are not
  necessarily independent checks.
- Applying this layout to current HW4 traffic remains a candidate decode.
  A matching number or Service Mode label does not establish binary parity,
  the physical producer, or the cause of `APP_w462_selfDrivingUnavailable`.
- No current HW4 refusal predicate is proven by this supplement. Promotion
  into a firmware-specific canonical definition requires matching native
  layout/provenance and independently attributed receive evidence.
- The [older HW2.5 supplement](https://github.com/talas9/tesla_can_signals/tree/main)
  is a different source profile and must not be merged into this HW3 profile
  merely because some IDs or names match.
