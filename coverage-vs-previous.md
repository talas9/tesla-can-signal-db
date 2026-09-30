# Coverage versus previous DBCs

> **Status of this report.** The counts below are from the comparison run
> against revision `44aedf5`, before the per-bus CAN files and before the
> recovered signals were merged. They have not been regenerated since. Merge
> result for 2026.26.6.5: 246 of the recovered firmware-position signals were
> added with Confidence `plausible` and the note "message assignment
> inferred". 38 of those were then left out of the DBC files because they
> overlap an existing signal (listed as dropped in the JSON twins). 82
> recovered signals were already present. 25 are on a controller's private
> bus and were not added. 43 name a message that differs from the one the
> CAN id map assigns to that id, and 7 reference a multiplexer switch that
> does not exist in the message; neither group was added. The old
> `dbc/<fw>/ALL.dbc` is now `dbc/<fw>/ETH.dbc`.


**Goal:** every message id and signal name in a previous DBC is one of three things in this database: present, mapped (renamed or renumbered), or explained (diagnostic, older firmware only, or on a bus this release does not cover yet).

**Compared against:** `dbc/2026.26.6.5/ALL.dbc`, `dbc/2025.20.8/ALL.dbc` and `data/<fw>/signals.csv`, at tesla-can-signal-db main `44aedf5`.

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

Each row of the gap list is counted once. Class x is included because the earlier gap list counted it as missing.

| DBC | kind | gap rows | x | a | b | c | f | d | e | recovered: firmware-proven | recovered: firmware-position | position-only | not recovered (d+e) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| P1 | id | 93 | 0 | 0 | 0 | 84 | 0 | 9 | 0 | 9 | 0 | 0 | 0 |
| P2 | id | 28 | 0 | 0 | 0 | 0 | 6 | 10 | 12 | 2 | 0 | 0 | 20 |
| P3 | id | 0 | - | - | - | - | - | - | - | - | - | - | - |
| P4 | id | 5 | 0 | 0 | 0 | 0 | 1 | 4 | 0 | 1 | 0 | 0 | 3 |
| P1 | signal | 3095 | 2286 | 197 | 15 | 121 | 0 | 305 | 171 | 70 | 147 | 66 | 22 d + 171 e |
| P2 | signal | 1021 | 0 | 235 | 28 | 0 | 0 | 502 | 256 | 7 | 303 | 107 | 85 d + 256 e |
| P3 | signal | 45 | 0 | 2 | 2 | 0 | 0 | 2 | 39 | 0 | 0 | 2 | 0 d + 39 e |
| P4 | signal | 94 | 0 | 3 | 3 | 0 | 0 | 58 | 30 | 4 | 21 | 0 | 33 d + 30 e |

`recovered-signals.csv` holds 396 unique signals: 93 firmware-proven and 303 firmware-position. The firmware-proven rows include every signal of the 12 recovered d messages, not only the signal names that were in the gap list. A further 107 unique signals are position-only.

## Findings

1. **Most of the earlier "missing" count was the 32-character name limit.** In P1, 2,286 of the 3,095 missing signal names are present (class x). An exact-name check against the DBC `SG_` names alone cannot see them.
2. **Renumbering between ETH and vehicle-bus ids explains only 7 ids.** These are 6 in P2 and 1 in P4:
   - 5 are pure renumbering: `UI_status` 0x00C→0x353, `RCM_inertial2` 0x111→0x116, `VCLEFT_doorStatus2` 0x122→0x7DC, `CP_chargeStatus` 0x23D→0x13D, `DAS_status` 0x39B→0x399.
   - 2 are renumbered and renamed.
   - P1 already uses ETH ids. Its 93 id gaps break down as:
     - 84 diagnostic ids (UDS request/response, ISO-TP pipes, functional request).
     - 9 messages that the ETH decoder does not handle:
       - 3 on the right body controller's private bus: 0x111, 0x112, 0x113.
       - `ESP_wheelSpeeds`, `BMS_contactorRequest`, `GTW_carState`, `APP_cameraTemperatures`, `GTW_factoryEcuPresent` and `HVP_hvpFaults`.
     - All 9 were recovered from the firmware network definition.
3. **Renames:** 437 gap rows map to a firmware name at an identical layout, which is 262 unique mappings in `renames.csv`. Of these rows, 416 are proven and 21 are likely.
   - A mapping is likely when the scale differs or the message was matched only by position.
   - Positions reused by an unrelated firmware signal with a dissimilar name are not called renames. They stay in class e, and their evidence notes the reuse.
4. **What remains unexplained (e):** 496 signal rows and 12 P2 ids. The largest groups are:
   - a previous-DBC-only overlap message (31)
   - a steering-wheel button frame (30)
   - an old drive-inverter limits frame (29)
   - road-sign fields (26)
   - drive-unit debug pages (69 rows in total)
   - older-generation EPB and inverter frames

   None of these names appears in the 2026.26.6.5 or 2025.20.8 firmware we hold, or in the other-platform firmware. They are kept as explained-as-unknown. They are not dropped.

## Status against the goal

- **Present, mapped or explained (x, a, b, c, f):**
  - ids: 91 of 126
  - signals: 2,892 of 4,255
- **Explained as another bus (d), and recovered from firmware:**
  - 12 of 23 d ids
  - 552 d signal rows at firmware-proven or firmware-position tier
- **Open:**
  - d not recovered: 11 ids and 140 signal rows. The name is in firmware but no layout is in our sources; 175 further rows have a position but no proven factor.
  - e: 12 ids and 496 signal rows.
