# Coverage versus previous DBCs

**Goal:** every message id and signal name in a previous DBC is one of three things in this database: present, mapped (renamed or renumbered), or explained (diagnostic, older firmware only, or on a bus this release does not cover yet).

**Compared against:** the current `data/<fw>/signals.csv` (both firmwares, full signal names including `SystemSignalLongSymbol`), `data/can-only-signals.csv` and `data/renames.csv`. Messages and signals are matched by name (case-insensitive); ids are matched through the message name. Counts are regenerated against the database as committed with this report.

We compared four previous DBCs:

| label | what it is |
|---|---|
| P1 | an earlier merged Model 3/Y DBC for 2026.26.6.5 |
| P2 | a large previous community Model 3 DBC (vehicle bus) |
| P3 | a small previous community Model 3 DBC (vehicle bus) |
| P4 | a small previous community Model 3 DBC (chassis / party bus) |

## Classes

| class | meaning |
|---|---|
| x | **Present.** The DBC format limits names to 32 characters, so the exported `SG_` name is shortened. The full name is kept in `SystemSignalLongSymbol` and in `signals.csv`. This is not a gap. |
| a | **Renamed.** The same message has a signal at the identical start, length and byte order (and the same mux page) under the firmware name. See `dbc/renames.csv`. |
| b | **Older firmware only.** The name exists in 2025.20.8 or older firmware data, but not in 2026.26.6.5. |
| c | **Diagnostic.** A UDS / ISO-TP request, response or pipe, or a signal inside one. This is not a broadcast signal. It is planned for a later diagnostics release. |
| f | **Present under a different id.** The previous DBC used the vehicle-bus id. At the time of this comparison the database used the Ethernet-side id; the per-bus files now use the on-bus CAN id, and `dbc/renames.csv` gives both. See `dbc/renames.csv`. |
| d | **Other bus or outside the decoder scope.** The message or signal is real firmware content, but it is not handled by the ETH decoder this release is built from. Examples are private buses, chassis/party-bus frames the gateway does not forward, and variant tables. |
| e | **Unexplained.** No firmware source we hold names this signal or message. |

Recovery tiers for d and e, in `recovered-signals.csv`:

- **firmware-proven:** message, id and full layout all come from a firmware network definition.
- **firmware-position:** start, length, byte order and min/max come from a firmware signal table. The previous DBC's factor and offset reproduce that firmware min/max exactly. Message membership comes from the previous DBC.
- **position-only:** firmware confirms the position, but the factor is not proven. These rows are not in `recovered-signals.csv`.

## Counts

Each row of the gap list is counted once. Class x is included because the earlier gap list counted it as missing. Column a includes 10 P2 signal rows that were class d in the first comparison and now have an entry in `renames.csv`.

| DBC | kind | gap rows | x | a | b | c | f | R (present after recovery) | d (still open) | e (still open) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| P1 | id | 93 | 0 | 0 | 0 | 84 | 0 | 6 | 3 | 0 |
| P2 | id | 28 | 0 | 0 | 0 | 0 | 6 | 2 | 8 | 12 |
| P3 | id | 0 | - | - | - | - | - | - | - | - |
| P4 | id | 5 | 0 | 0 | 0 | 0 | 1 | 1 | 3 | 0 |
| P1 | signal | 3095 | 2286 | 197 | 15 | 121 | 0 | 208 | 97 | 171 |
| P2 | signal | 1021 | 0 | 245 | 28 | 0 | 0 | 260 | 232 | 256 |
| P3 | signal | 45 | 0 | 2 | 2 | 0 | 0 | 0 | 2 | 39 |
| P4 | signal | 94 | 0 | 3 | 3 | 0 | 0 | 4 | 54 | 30 |
| all | id | 126 | 0 | 0 | 0 | 84 | 7 | 9 | 14 | 12 |
| all | signal | 4255 | 2286 | 447 | 48 | 121 | 0 | 472 | 385 | 496 |

Class b rows (48 signals) name signals that exist only in firmware older than the two we hold, so they are not in the database by design.

## Findings

1. **Most of the earlier "missing" count was the 32-character name limit.** In P1, 2,286 of the 3,095 missing signal names are present (class x). An exact-name check against the DBC `SG_` names alone cannot see them.
2. **Renumbering between ETH and vehicle-bus ids explains only 7 ids.** These are 6 in P2 and 1 in P4, all listed in `renames.csv` with the vehicle-bus id.
   - 5 are pure renumbering: `UI_status` 0x00C→0x353, `RCM_inertial2` 0x111→0x116, `VCLEFT_doorStatus2` 0x122→0x7DC, `CP_chargeStatus` 0x23D→0x13D, `DAS_status` 0x39B→0x399.
   - 2 are renumbered and renamed.
   - P1 already uses ETH ids. Of its 93 id gaps, 84 are diagnostic ids (UDS request/response, ISO-TP pipes, functional request) and 9 were messages the ETH decoder does not handle. 6 of those 9 are now in the database; the other 3 are on a body controller's private bus and are not added.
3. **Renames:** 447 gap rows map to a firmware name at an identical layout; `renames.csv` holds 262 unique mappings, 247 proven and 15 likely.
   - A mapping is likely when the scale differs or the message was matched only by position.
   - Positions reused by an unrelated firmware signal with a dissimilar name are not called renames. They stay in class e, and their evidence notes the reuse.
4. **Recovery:** 472 signal rows and 9 ids that were class d or e in the first comparison are now present. The rest of the recovered firmware signals were not merged: some sit on a controller's private bus, some name a message that differs from the one the CAN id map assigns to that id, and some reference a multiplexer switch that does not exist in the message.
5. **What remains unexplained (e):** 496 signal rows and 12 P2 ids. The largest groups are:
   - a previous-DBC-only overlap message (31)
   - a steering-wheel button frame (30)
   - an old drive-inverter limits frame (29)
   - road-sign fields (26)
   - drive-unit debug pages (69 rows in total)
   - older-generation EPB and inverter frames

   None of these names appears in the 2026.26.6.5 or 2025.20.8 firmware we hold, or in the other-platform firmware. They are kept as explained-as-unknown. They are not dropped.

## Status against the goal

- **Present, mapped or explained (x, a, b, c, f, R):**
  - ids: 100 of 126 (9 present after recovery, 7 mapped, 84 diagnostic)
  - signals: 3,374 of 4,255 (2,758 present, 447 mapped, 169 older-firmware or diagnostic)
- **Still missing:**
  - d (real firmware content on another bus, not in the database): 14 ids and 385 signal rows
  - e (unexplained): 12 ids and 496 signal rows
