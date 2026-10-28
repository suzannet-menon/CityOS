# CiVix — Documentation Index

## Product scope

CiVix is a pedestrian navigation system that routes citizens through
streets scored for **safety**. Road-segment safety scores are precomputed
by the `logic/` pipeline into PostGIS, and verified community incident
reports adjust scores live at scoring time.

The active implementation scope is Phases 1–6:

1. **Phase 1 — Walking-module structure**
2. **Phase 2 — Reporting** (`report_type`, categories)
3. **Phase 3 — Waste reporting**
4. **Phase 4 — Authority dashboard**
5. **Phase 5 — Deployment and configuration**
6. **Phase 6 — Multi-city support**

## Document index

| Document | Status | Contents |
|----------|--------|----------|
| `BASELINE.md` | Current reference | Verified tables, endpoints, cache behaviour, and test inventory |
| `step_1` … `step_6` | Historical | Origin of the module, reporting, config, and deployment structure |
| `CityOS_Engineering_Handbook_Volume_I.md` | Legacy | Original platform vision |
| `CityOS_ADR_System_Spec.md` | Legacy | Original architecture decisions |
| `cityos_plan.xml` | Legacy | Original module plan |

Legacy documents carry a superseded banner. Where a legacy document conflicts
with the current code, the code takes precedence.

## Phase status

| Phase | Title | Status |
|-------|-------|--------|
| 1 | Walking-module structure | Implemented |
| 2 | Reporting (`report_type`, categories) | Implemented |
| 3 | Waste reporting | Implemented |
| 4 | Authority dashboard | Implemented |
| 5 | Deployment and configuration | Implemented |
| 6 | Multi-city support | Implemented |

## Engineering conventions

1. **Additive changes only.** New signals are added as new response keys. The
   existing `safety_score` value and all existing keys must remain unchanged.
2. **I/O isolation.** Database access and Valhalla are injected into
   services, not called from pure logic. Unit tests run without a database or
   network.
3. **Characterisation before modification.** Freeze the current `/route-safe`
   response in a test before refactoring the scorer.
4. **Layer ownership.** Data flows through a fixed path:
   `logic/` ingest → PostGIS → `SafetyDatasetCache` → service → router →
   Flutter model → controller → screen. Changes belong in the layer that owns
   the data.
5. **Versioned schema.** Every database change is an Alembic migration with a
   working `downgrade()`.

## External services

| Service | Purpose | Credentials |
|---------|---------|-------------|
| Valhalla | Pedestrian routing | Self-hosted; `VALHALLA_BASE_URL` |
| Supabase / PostGIS | Road, zone, and report storage | `DATABASE_URL`, Supabase keys |
| Maptiler | Map tiles (mobile) | `MAPTILER_API_KEY` via `--dart-define` |

## Commands

```bash
# Backend tests (no database or network required)
cd backend && python -m pytest tests/ -v

# Mobile analysis and tests
cd mobile && flutter analyze lib/ && flutter test

# Backend development server
cd backend && python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

See the repository `README.md` for local setup, Valhalla, and APK packaging.
