# AHMAD KALEEM BHATTI — CAREER CONTEXT (optimized for LLM use)

Evidence store, not a finished resume. Nothing invented; uncertain items are flagged inline with **[UNCONFIRMED]** rather than silently resolved. Source: Ahmad's direct statements + independent codebase audit reports (Demetronics; Kaar-e-Kamal has two — an Aug 2026 audit and a more thorough Sep 16 2026 forensic/git audit that supersedes it where they conflict) + resume drafts + JD-matching sessions. Last compiled: Sep 2026.

---

## 1. Identity & Background

- **Name:** Ahmad Kaleem Bhatti · **Location:** Islamabad, Pakistan
- **Contact:** ahmadkaleeem1@gmail.com · +92-328-0092525 · linkedin.com/in/ahmadkaleembhatti · github.com/ahmaadkaleeem · ahmadkaleem.tech
- **Career stage:** Undergrad (3rd yr, ~5 semesters done). Two founder ventures (Actsurance, Qualix) + AUCIS leadership role. Two internships, both **concluded**: Kaar-e-Kamal (Jul–Aug 2026), Demetronics (Aug–Sep 2026).
- **Target roles:** AI Engineer / AI Agent Developer (evaluated against Agileday, dexter health JDs — see §10). Also general Full-Stack/SWE internships. Distinct positioning niche: **AI agent security/policy enforcement** via Actsurance — not a generalist framing.
- **CGPA/grades:** Never include on any resume — standing instruction.

### Development Philosophy
- Backend: standard-library-first, YAGNI, layered architecture (Handler→Service→Repository) — explicit Go engineering guideline.
- Security: fail-closed by default (Actsurance's whole architecture; EMU86 Sandbox was an earlier low-level exploration of the same idea).
- Ships small, real tools proactively without being asked (QEC Auto-Filler, GradePilot) and gets organic adoption.
- Disciplined AI-assisted development: built an internal "Engineering Operating System" (EOS) governing how AI coding agents are allowed to touch the Actsurance codebase — not casual prompting.
- Discloses AI-assisted work openly (e.g., Pakistan Digital Elections frontend built with Claude assistance) — public stance: "AI is a tool, not a replacement."

---

## 2. Standing Rules for AI Use of This File

1. Never invent resume facts, metrics, or skill levels.
2. No CGPA/SGPA/grades on any resume, ever, under any circumstances.
3. Prefer the most recent confirmed status — see Status Ledger (§5) for every known contradiction and its resolution.
4. Preserve historical framing where it matters (e.g., PakLand must stay framed as a completed educational project, not an active startup).
5. Before writing a resume: identify the target job, then select the most relevant evidence from this file.
6. Don't delete technically relevant detail just because it isn't on a current resume.
7. Translate technical work into recruiter-readable language without losing technical accuracy.
8. Don't claim production/deployed status unless confirmed — recent Demetronics work is still built-but-uncommitted/unverified (see §5, §7). Kaar-e-Kamal is the exception: the Sep 2026 forensic audit confirms the hardened backend/DB/offline-sync work is committed and tested (see §5, §7) — don't apply the old "uncommitted/Not Ready" framing to it anymore.
9. Don't claim leadership scope beyond what's confirmed — AUCIS promotion scope is still open (see §5). Kaar-e-Kamal team size/composition is now resolved (3 contributors, 92.9%/6.5%/0.6% commit split — see §5); the *formal title* Ahmad held is still just "Application Developer Intern," so don't upgrade the official title, only the resume-equivalent framing.
10. Don't assume a project is current just because it's in this file — PakLand is closed/completed.
11. Preserve exact numbers and technology names as recorded, including ones flagged unconfirmed.
12. When uncertain, flag it — don't guess.

---

## 3. Writing & Resume Preferences

- **Length:** 1 page by default; 2 pages only if forcing 1 page would hurt readability.
- **Structure:** Reverse-chronological — Contact → Summary → Skills (moved high, "top-third" ATS rule) → Experience → Projects → Leadership → Education → Certifications.
- **Bullets:** Action-verb-led, XYZ/CAR framework, one technology/outcome per bullet where possible.
- **Avoid:** Unsupported buzzwords ("passionate," "results-driven" without evidence in the same sentence), AI-cliché phrasing ("dynamic professional," "leveraged cutting-edge"), em dashes as narrative connectors, narrative (non-structural) colons.
- **Use:** Specific, plain, technically precise language; real numbers only when methodology is known and defensible.
- **Format:** ATS-safe, single-column, no icons, no custom colors. No fabricated metrics ever. No claimed skills without a traceable project/experience behind them.
- **ATS:** Keywords mirrored from job descriptions only where genuinely true, never stuffed.
- Comfortable with LaTeX resume production (incl. debugging real compile/render bugs) and with being told "no/not yet" on unverifiable claims. Consistently prioritizes interview-defensible truth over impressive-sounding claims.

---

## 4. Technical Stack (canonical — project-specific usage noted only where materially different; see §7 for full project architecture)

**Languages:** Python, JavaScript/TypeScript, Go, Dart (Flutter), PHP, C++, x86 Assembly (8086, EMU86 project only), SQL

**Backend:** FastAPI (Python), Go `net/http` (stdlib-first), Node.js/Express, REST API design, Webhooks

**Frontend:** React (+Vite+TS+Tailwind), Next.js, Flutter (GoRouter, GetX, StatefulWidget/AnimationController, `syncfusion_flutter_charts`)

**Databases:** PostgreSQL (+PgBouncer; Supabase w/ heavy RLS), MySQL, Firebase Realtime DB/Firestore, MongoDB, Redis, ChromaDB

**Cloud/DevOps:** Docker, Kubernetes, Firebase, Supabase, Render (planned target, not confirmed live), Railway (confirmed live CI/CD — Kaar-e-Kamal), GitHub Actions. **No confirmed AWS/GCP/Azure experience — real gap, don't claim.**

**AI/ML:** OpenAI, Claude, Gemini, OpenRouter, Nvidia NIM APIs (genuine multi-provider experience); LangChain, ChromaDB, RAG, vector DBs, prompt engineering, tool calling, AI agents; ONNX Runtime (self-hosted/local inference — Actsurance risk model, explicitly avoids external LLM calls); RE2 regex engine (DPI); GPT-4o-Mini

**Security:** RBAC implemented 3 different ways across 3 systems (JWT-based/Kaar-e-Kamal, Firebase Custom Claims/Demetronics, OPA policy-engine/Actsurance — genuine breadth); JWT (`golang-jwt`+`keyfunc`; RS256 vs JWKS + Redis revocation check); OPA/Rego; mTLS; Ed25519 signing + SHA-256 hash chaining; RE2 deep packet inspection; "Sealed Broker" credential-isolation pattern; `jti` reuse detection; Zod validation; Redis-backed idempotency; Bandit (SAST)

**Testing/Quality:** PyTest, `go test`, Ruff/MyPy/Bandit/pip-audit, Playwright, custom validation scripts (`verify_beta_readiness.py` — 18 automated checks; `failure_mode_validation.py` — service-down simulation, **not yet CI-wired**, acknowledged gap)

**Observability:** Jaeger (OTel tracing), Prometheus, Grafana (Actsurance production stack); structured audit logging; PDF export tooling (`jspdf`)

**Dev tools:** Git/GitHub/GitHub Actions; AI coding tools — Copilot, Cursor, Claude Code, Codex, Devin, Antigravity (**familiarity, not deep-expertise claims**); Figma; Linux/Ubuntu/VMware Workstation Pro

**Automation:** n8n; browser extension dev (Manifest V3)

**Data/RAG:** Pandas, NumPy, Matplotlib, Openpyxl; ChromaDB+LangChain retrieval

**No confirmed MCP (Model Context Protocol) experience.** Actsurance is conceptually adjacent (governs/audits AI agent tool calls) but not built on the MCP spec — frame as adjacent problem space, don't claim MCP directly.

---

## 5. Status Ledger (resolved contradictions — always use the "Current" column)

| Topic | Current (use this) | Superseded / historical only |
|---|---|---|
| Actsurance build status | **Built** — pipeline, crypto receipts, risk model all working (ONNX risk model specifically **partial**, not complete) | "100% design/architecture phase, paused for redesign" — old framing, don't use |
| Actsurance policy engine | **OPA (Open Policy Agent) running Rego** — live, confirmed via `docs/CURRENT_ARCHITECTURE.md`, `docs/OPA.md`, `docker-compose.yml` | Cedar — internal abstraction reference only, explicitly "Planned (Phase 2)," not current |
| Actsurance pipeline stages | Precise 10-step flow: Auth → Idempotency/Rate Limiting → L1 RE2 Firewall → OPA Authorization → ONNX Risk Evaluation → Routing → Sealed Broker Execution → Receipt Generation → Persistence | "Seven-stage" was a coarser rounded description — use the 10-step flow when precision matters |
| Atif E-Commerce title | **"Sales & Data Assistant (E-Commerce Automation)"** — hybrid, Ahmad-confirmed | Early drafts: "E-Commerce Automation and Operations Specialist" / "Python Automation Engineer" |
| Demetronics title | **"Full Stack Development Intern"** (offer letter, official) = **"Full Stack Engineer Intern"** (resume-equivalent, OK) | "IoT Backend & Web Developer" — not official, avoid |
| Demetronics audit-log DB | **MongoDB confirmed** — exposed URIs found in `server/.env` across specific commits | Earlier audit described only an unnamed `audit_logs` collection |
| Demetronics pairing workflow | **NOT aligned across clients** — app bypasses API, connects directly to ESP AP (`192.168.4.1/credentials`); portal uses mediated 6-digit-code flow (`POST /devices/pair/request` → `/devices/pair`) | Earlier material described the flow as identical across app and portal — inaccurate |
| Demetronics completion framing | **"Implemented in local codebase, pending commit/deployment/verification"** | Confident past-tense "Built"/"Shipped to production" bullets — overclaim per audit |
| Kaar-e-Kamal completion framing | **Production-hardened per Sep 16 2026 forensic audit** — consolidated DB migration, PG advisory locks, Redis idempotency/rate-limiting, 12-criterion scoring engine, RLS forced on all 18 tables, offline sync, automated Go + Flutter test suite all confirmed present and committed | Aug 2026 audit's "Not Ready — Admin/Super Admin uncommitted, Op Worker missing entirely" — describes an earlier repo state; superseded by the Sep audit, which finds Op Worker (delivery, handoff requests) and Admin scoring both built and committed. Don't use the "Not Ready" framing going forward. |
| Kaar-e-Kamal role scope | Solo-built MVP (~1 week), then **led a team** through MVP→production. Team size and composition **confirmed by git forensics**: 3 total contributors across 170 commits — Ahmad 158 (92.9%), HaniaWaheed 11 (6.5%, initial field/op-worker UI form mockups + data models), sameera-sus 1 (0.6%, initial Go worker-handler stub, later refactored by Ahmad). A later, full-repo audit gives different raw numbers, 172 commits to Ahmad against 11 for the next contributor globally, plus a backend-only split of 72 out of 75 commits to Ahmad, without naming the other contributors, so it can't be reconciled line-for-line with the breakdown above. Ahmad's clear majority ownership holds under both counts; use the 158/170/92.9% figures for now since they come with full attribution, and treat the 172/backend-72-of-75 figures as supporting evidence, not a replacement, until checked. Formal title on record remains "Application Developer Intern" (see §8); "Technical Lead & Primary Full-Stack Engineer" is a resume-defensible equivalent per the audit's role-defensibility analysis (HIGH confidence), not an official title. | Team size/title "[UNCONFIRMED]" — resolved |
| Kaar-e-Kamal scoring engine thresholds | **Dynamic, per-case-type, DB-configurable** thresholds (`passing_score`, `manual_review_score`) set via Super Admin sliders — not fixed constants | Earlier "35/40-pt thresholds" figure — likely a snapshot of one case type's configured values at audit time, not a hardcoded system-wide rule; don't present as fixed |
| AUCIS promotion scope | **Title + date only**: Developer → Senior Lead Developer, Apr 2026. Scope of change never specified despite repeated direct questions | Don't invent team size/projects owned |
| PakLand moderation | **GPT-4o-Mini, text-only.** Google Vision is **NOT used** — remove from every version | Earlier drafts incorrectly included Google Vision image analysis |
| PakLand status | **Completed semester/class project**, not an active startup | Earlier framing described it more like an active venture with a market narrative |

---

## 6. Unconfirmed / Do-Not-Use Claims

- Demetronics: **"500+ IoT devices"**, **"100% reduction in unauthorized writes"** — the source document that proposed these explicitly flagged them as "still not known."
- PakLand: **"8 of 10 (80%)"** self-test scam-detection accuracy — appears in one portfolio doc, absent from the LinkedIn text Ahmad designated as PakLand's source of truth. Likely real but not fully confirmed.
- QB Hostels: **"40% reduction in manual admin workflow time"** — methodology never confirmed.
- Qualix: **"40% faster response / 60% fewer missed leads"** — Ahmad confirmed this was never measured. **Permanently dropped, do not reintroduce.**
- Four "practice project" names — "Rock Paper Scissors," "Data Analyzer," "NumPy Assignment," a broader "data visualization collection" — from an early AI-generated summary table, never corroborated by Ahmad.
- Sports Analyzer: class assignment vs. personal project — never resolved.
- A synthetic test-script line (`audit_language.py` placeholder: "...class project using Node.js and Express...") — was demo test data, never Ahmad's real experience. Flagged here so it's never mistaken for a real project.
- Kaar-e-Kamal: **"Sole developer"** — explicitly not defensible; git history shows 2 named teammates (HaniaWaheed, sameera-sus) alongside Ahmad's 92.9% share (see §5, §7).
- Kaar-e-Kamal: **"Zero-downtime distributed Redis cluster"** — the real implementation is a single Redis instance with an in-memory fallback, not Sentinel/Cluster.
- Kaar-e-Kamal: **comprehensive automated Flutter UI test coverage** — automated tests are targeted (specific models/repositories/screens), not app-wide; broader coverage was manual (e.g., airplane-mode offline testing).
- Kaar-e-Kamal: **local storage encryption claims** — offline queue data sits as plain JSON in `SharedPreferences`, unencrypted on-device.
- Kaar-e-Kamal: **invented beneficiary/user-scale numbers** — no deployment-usage data exists to support a served-users metric.

---

## 7. Projects

### Actsurance (Founder) — flagship, strongest single piece of evidence
- **Type:** AI-agent authorization gateway ("authority firewall"), documented as "Actsurance Architecture v1.1."
- **Problem:** Human-facing systems built rigorous access control over ~15 years; autonomous AI agents acting on customer databases/payments/internal systems have almost no equivalent control layer.
- **Role:** Founder, sole architect/builder. Also built the internal EOS governing the project's own AI-assisted development (below).
- **Architecture (10-step, confirmed via engineering audit):** Agent Request → Gateway Auth (RS256 JWT vs JWKS + Redis-backed revocation check) → Idempotency & Rate Limiting (Redis) → L1 Firewall (RE2 deep packet inspection: SQLi, XSS, path traversal) → Authorization (OPA evaluating Rego policies by Tenant + RBAC) → Risk Evaluation (ONNX Runtime score) → Routing (deterministic ALLOW/DENY/ESCALATE) → **Sealed Broker Execution** (secrets injected locally at the perimeter — agent never sees raw credentials) → Receipt Generation (Ed25519 signing, hash-chained) → Persistence (PostgreSQL system-of-record, Redis cache).
- **"Sealed Broker" pattern:** the single most differentiated, concrete technical claim in the project — agents execute allowed actions without ever being exposed to underlying credentials.
- **Fail-closed:** if OPA, ONNX, Redis, or PostgreSQL become unavailable → DENY. Backed by named ADRs: ADR-0004 (receipt persistence failure → fail closed), ADR-0005 (ONNX risk engine unavailable → fail closed).
- **ESCALATE:** first-class outcome alongside allow/deny, with a real Human-Approval Workflow (SQLite-persisted, managed by an `ApprovalsManager` component).
- **Implementation status:**
  - *Fully implemented:* OPA policy enforcement, sealed secret broker, crypto receipts (Ed25519 + hash chain, Postgres), tamper detection (watchdog file observer), human-approval workflow, L1 RE2 firewall, "Universal Callables" (functions/async as executable targets).
  - *Partial:* ONNX risk-scoring engine — implemented but explicitly marked partial by the audit.
  - *Planned (Phase 2):* Cedar policy backend, AWS Nitro hardware attestation.
  - *In progress:* compliance dashboard, more robust live SaaS sandbox connector validation.
- **SDKs:** first-class Python and Go SDKs.
- **Testing:** `pytest` (gateway), `go test` (Go SDK), `verify_beta_readiness.py` (18 automated checks vs. live Docker stack), `failure_mode_validation.py` (service-down simulation — **not yet CI-wired**, acknowledged gap).
- **Observability:** Jaeger (OTel tracing), Prometheus, Grafana — confirmed via `infra/prometheus/prometheus.yml`.
- **CI/CD:** Makefile-driven (`install`/`dev`/`test`/`lint`/`security-scan`/`docker-up/down`); Ruff, Bandit; Docker Compose.
- **EOS (Engineering Operating System)** — distinctive evidence of disciplined AI-assisted development: `AGENTS.md` routes any AI assistant through a context-bootstrap process before it may act; `mcp/context/decision-memory.md` is a rolling architectural-decision log; `actsurance-eos/specs/kernel/GlobalEngineeringRules.md` is a constitutional rulebook with named principles (`SEC-001` Least Privilege, `SEC-002` Centralized Secrets Mgmt, `REL-004` Graceful Degradation, `AI-001` — AI output never implicitly trusted, must pass deterministic gates); domain-scoped "skills" files give AI agents curated instructions (e.g., MCP engineering, production-security engineering). Strong, concrete answer to "how do you use AI coding agents seriously."
- **Acknowledged gaps:** two `AGENTS.md`-mandated files (`actsurance-eos/constitution/laws.md`, `actsurance-eos/workflows/core-workflows.yaml`) are empty (0 bytes) as of audit — unresolved, self-acknowledged. Frontend (Next.js marketing site, separate `frontend/` dir in a Vercel monorepo) not present in the audited backend repo — details **[UNCONFIRMED]**.
- **External validation:** Selected to pitch at NIC Lahore and NIC Hyderabad (National Incubation Center); missed the in-person pitch due to a university-exam scheduling conflict.
- **Resume angle:** Strongest evidence for AI-agent-security roles (e.g., Agileday's "permission-aware MCP layer" framing maps closely). Sealed Broker + fail-closed ADRs + ESCALATE pipeline are concrete, interview-safe claims. EOS is separately strong evidence of serious (not casual) AI-coding-tool use.

### Qualix (Founder)
- **Type:** Multi-surface agentic AI sales/support platform — lead qualification + customer comms across WhatsApp, Instagram, Telegram.
- **Problem:** Fragmented channels + manual lead qualification → lost sales from delayed/missed replies.
- **Architecture:** Hybrid RAG (LangChain + ChromaDB) for business-context retrieval; tool-calling via FastAPI backend functions (retrieve context, qualify leads, update status, trigger follow-ups); role-gated portals (Agent/Client/Manager/Developer). Stack: FastAPI (Python 3.12) + async SQLAlchemy 2.0 + PostgreSQL 16 (via PgBouncer) + Redis 7 + Celery/Celery Beat; frontend React 19 + Vite + TypeScript + Tailwind; landing site Next.js 16.
- **Integrations:** OpenRouter, OpenAI, Nvidia NIM (multi-provider LLM access).
- **Testing:** PyTest (API behavior, lead-qualification logic, RAG retrieval, tool-calling flows); Ruff/MyPy/Bandit/pip-audit as CI gates.
- **Deployment:** GitHub Actions CI/CD; Kubernetes manifests (staging/prod); Docker Compose (single-VM path).
- **Status:** MVP built and functioning.
- **Metric:** "40% faster response / 60% fewer missed leads" — **not measured, permanently dropped** (see §6).

### PakLand (Founder, semester project) — completed, not active
- **Type:** Flutter real-estate marketplace addressing Pakistan's real-estate trust deficit (commonly cited: ~60% of buyers avoid platforms due to fake/outdated listings).
- **Features:** Automated 30-day ad-expiry requiring active re-verification; AI-moderation pipeline (n8n workflow, GPT-4o-Mini, **text-only** — Google Vision not used, see §5) with human-review routing for high-risk content, all actions logged; 0–100 Trust Score (verification + reviews, affects search ranking; 75+ unlocks "Featured"); geo-location search (Google Maps SDK); dual-mode booking flow.
- **UI:** Designed first in Figma.
- **Stack:** Flutter (single iOS/Android codebase), Firebase (Auth, Firestore), Supabase (image storage/CDN), n8n, GPT-4o-Mini, Google Maps SDK, Figma.
- **Roadmap (not built):** in-app messaging, JazzCash/EasyPaisa payments, AI property recommendations, Urdu support, video property tours.
- **Metric:** "8/10 (80%)" self-test — **[UNCONFIRMED]**, see §6.

### Kaar-e-Kamal Welfare Foundation — Application Developer Intern (Jul–Aug 2026, concluded)
- **Type:** Multi-portal welfare assistance management platform covering four aid categories (Rashan, Medicine, Education Fees, Rozgar/Employment) — 5 portals (Applicant, Field Worker, Operations Worker, Admin, Super Admin) — Go REST backend, PostgreSQL/Supabase database, Flutter mobile/desktop frontend. In UAT with the NGO's operations team per the latest audit, targeting an initial Islamabad launch with a stated long-term goal of nationwide access.
- **Role:** Built MVP solo (~1 week), then led a 3-person team through MVP→production. See Status Ledger (§5) for the git-forensics-confirmed team breakdown (92.9%/6.5%/0.6%). "Technical Lead & Primary Full-Stack Engineer" is the audit's recommended, defensible resume framing — not an official title (official title stays "Application Developer Intern," §8).
- **Architecture (per Sep 16 2026 audit — supersedes the Aug 2026 snapshot, see §5):** Layered Client → Gateway/Middleware → Application Service → Persistence design.
  - *Frontend:* Feature-first Flutter structure (`app/`, `core/` incl. offline services + `SyncWorker` + session manager, `shared/`, then one directory per portal: `client/`, `worker/field/`, `worker/operations/`, `admin/`, `super_admin/`). `GoRouter`-based routing, `flutter_riverpod` for state management (newly confirmed, wasn't in earlier notes). Custom dark theme (Mustard `#F5BF25` / dark-gray `#1E1E1E`); responsive layout — floating pill nav on mobile, fixed 280px nav rail on desktop/tablet. **Open conflict:** a separate, shorter audit describes the same `lib/` folder as split into `data/`, `domain/`, `presentation/` layers instead of the feature-first/portal layout above. The two don't reconcile as written. The feature-first breakdown names exact directories and should be treated as primary until the repo is re-checked directly.
  - *Backend:* Go 1.22+, idiomatic `net/http` `ServeMux` w/ typed path params, zero third-party web framework, strict Handler→Service→Repository. Global middleware chain: CORS → panic recovery → Redis/in-memory rate limiter → request logger → security headers. `pgx/v5`, `go-redis/v9`, `slog`, `sentry-go`.
  - *Database:* PostgreSQL/Supabase, consolidated canonical migration (`20260916000000_consolidated_schema.sql`) replacing 25+ incremental migrations; explicit B-tree indexes on `user_id`/`status`/`area`/`created_at`.
- **Audited directory map (per a later full-repo pass):** `backend/internal/` holds the domain packages (`cases`, `admin`, `auth`, `platform/middleware`); `backend/cmd/api/main.go` is the entry point wiring dependency injection and the middleware stack (Sentry, Redis rate limiting, CORS, auth); `supabase/migrations/` holds schema history and RLS policy definitions; `docs/` was checked against the actual code rather than taken at face value.
- **Role responsibilities (detail not previously captured):** Field Workers submit structured verification reports covering family size, income, and photo evidence. Op Workers handle physical delivery, with built-in workflows for failed-delivery retries and handoffs between workers.
- **Concurrency-safe eligibility enforcement:** CNIC-based limits (Rozgar: 1 lifetime; Rashan/Fees: 1 active + 1 fulfilled per month; Medicine: 4/month) enforced via a PostgreSQL transaction-level advisory lock — `pg_advisory_xact_lock(hashtext(cnic + "::" + case_type))` — inside the case-insert transaction, chosen deliberately over `SELECT FOR UPDATE` (advisory locks don't lock existing rows, so concurrent inserts for *different* CNICs proceed while identical-CNIC submissions serialize). Case numbers generated via a dedicated Postgres sequence (`case_number_seq`, format `KK-YYYY-XXXXXX`) instead of `SELECT COUNT(*)+1`, avoiding lock contention.
- **Idempotency & rate limiting:** SHA-256 fingerprint of `userID + payload`; Redis `SetNX` lock (24h TTL) makes case creation idempotent — reusing a key with an altered payload returns `409 IDEMPOTENCY_KEY_REUSED`, concurrent duplicates return `409 CONFLICT`. Separately, Redis `TxPipeline` fixed-window rate limiting (atomic `INCR`+`EXPIRE`) with random TTL jitter (55s + 0–6s) to avoid thundering-herd cache-stampede on key expiry; client-IP extraction guards against proxy spoofing; in-memory `golang.org/x/time/rate` token-bucket fallback if Redis is down.
- **12-criterion scoring engine:** Admin-submitted `map[string]bool` scorecard; server enforces strict boolean typing (rejects numeric/other types to block point-injection), matches against server-side point definitions, evaluates against **dynamic, per-case-type, DB-configurable thresholds** (`passing_score`, `manual_review_score` — Super-Admin-adjustable, see §5 for why not to quote fixed numbers), branches to `approved`/`manual_review`/`rejected`.
- **RBAC & RLS:** Server-side JWT auth middleware + real-time DB role lookup on every request (`requireFieldWorker`/`requireOpWorker`/`requireAdminOrSuper`/`requireSuperAdmin` re-query `profiles`, not just JWT claims — enables instant role revocation). Row-Level Security `FORCE`d across all 18 tables; anonymous access globally revoked (`REVOKE ALL ... FROM anon`).
- **Background daemons (3, goroutine + `time.Ticker` + context cancellation for graceful shutdown):** `ProcessEscalations` (hourly case auto-escalation, 3-day applicant confirmation timeout), 30-second notification-queue dispatcher (SMTP), `workerScheduler.StartRetryEngine` (5-minute delivery-retry worker). Function names confirmed by a later audit pass.
- **Offline-first field verification:** Field/Op workers queue verifications + evidence locally via `SharedPreferences` when offline (local UUID, local image paths). `SyncWorker` monitors `connectivity_plus` + app lifecycle to run a two-phase flush on reconnect — upload binary evidence to Supabase Storage first, then submit the JSON payload with the original idempotency key preserved (so a mid-retry network drop still can't double-create a case). **Known limitation:** local `SharedPreferences` queue is unencrypted on-device (don't claim disk encryption — see §6).
- **Audit logging:** Actor ID/role, action string, entity type/ID, and arbitrary JSON metadata captured to `audit_logs` for all state-mutating admin actions.
- **Automated test suite confirmed in-repo:** Go — idempotency/fingerprinting tests, an adversarial test specifically targeting non-boolean scorecard-injection attempts, rate-limit header/threshold tests, DB-schema-vs-DTO contract tests, an end-to-end case-lifecycle test (`backend/internal/e2e/lifecycle_test.go`). Flutter — model tests (admin dashboard stats), repository tests (case repository), widget tests (field verification form screen). Manual testing covered offline scenarios (airplane-mode toggling on a physical device mid-submission) and SMTP approval-email delivery. **Don't claim automated UI test coverage across the whole Flutter app** — automated coverage is targeted (specific models/repos/screens), not comprehensive.
- **Case lifecycle:** 11 states — `pending`, `under_review`, `pending_scoring`, `manual_review`, `approved`, `rejected`, `assigned_op_worker`, `in_delivery`, `delivery_failed`, `fulfilled`, `completed`, `escalated`.
- **Don't claim (per audit, Kaar-e-Kamal-specific):** sole developer (2 named teammates in git history); zero-downtime/distributed Redis cluster (it's a single Redis instance + in-memory fallback, not Sentinel/Cluster); custom local disk encryption (offline storage is plain JSON in `SharedPreferences`); invented user-scale numbers (no deployment-data-backed beneficiary counts exist).
- **Resume/interview framing:** Strongest concrete, interview-defensible claims are the advisory-lock eligibility enforcement, the SHA-256/Redis idempotency + jittered rate-limiting pair, the injection-hardened scoring engine, and the offline-first sync engine — all independently verified against source. Be ready to explain *why* each design choice was made (advisory locks vs. row locks, jitter vs. plain TTL, boolean-only scorecard, sequence vs. `COUNT(*)`, DB-backed role checks vs. JWT-claim trust) rather than just naming the technology.
- **Audit-suggested draft language (evidence/raw material only — not vetted against §3 writing rules, not finalized, don't paste verbatim without editing):**
  - *LinkedIn headline options:* "Technical Lead & Backend Engineer | Go, PostgreSQL, Redis, Distributed Systems"; "Full-Stack Mobile Engineer | Go, Flutter, PostgreSQL, System Architecture"; "Software Engineer & Tech Lead | Go, Flutter, System Design, Production Systems."
  - *LinkedIn experience bullets (raw, pre-edit):* led full-stack architecture across the 5 role portals; architected the Go REST backend (layered Handler/Service/Repository, DB-backed RBAC, structured logging); engineered the advisory-lock CNIC eligibility system; implemented the Redis rate-limiting/idempotency pair; designed the 12-criterion scoring engine w/ boolean validation + dynamic thresholds; built the offline-first Flutter sync engine; hardened DB security (consolidated schema, forced RLS across 18 tables, revoked anon access, audit logging).
  - *CV bullet drafts exist in 3 variants* — backend/technical-focused, AI-engineering-focused (frames the scoring engine as a socio-economic decision workflow + emphasizes structured logging/transaction management), and general-SWE-focused (emphasizes the multi-portal product + Flutter UI + notification/escalation daemons). Same underlying facts, different emphasis per target role — re-derive per §3 rules and target JD rather than reusing audit wording as-is.
  - *Interview-prep topic list (12 items) the audit flagged as things to be ready to explain in depth:* advisory locks vs. `SELECT FOR UPDATE`; the Redis idempotency mechanism end-to-end; why rate-limit jitter prevents thundering herd; why boolean-only scorecard input blocks injection; why RBAC middleware re-queries `profiles` instead of trusting JWT claims alone; Go 1.22 `ServeMux` + middleware chaining; the offline `SyncWorker`'s two-phase flush; `case_number_seq` vs. `COUNT(*)+1`; the 11-state case lifecycle; `time.Ticker` + context-cancellation background-job pattern; why RLS was `FORCE`d + anon access revoked; and the team-leadership/integration story (architecture decisions, DTO contracts, reviewing + refactoring teammate UI stubs into production code).

### Demetronics (Private) Limited — Full Stack Development Intern (Aug–Sep 2026, concluded)
- **Type:** Smart Water Management IoT company. Mandate: build a new Admin Portal + backend for centralized IoT fleet control (tank monitoring/motor control), fix mobile-app data issues, remediate security vulnerabilities.
- **Major shift:** decentralized (clients write directly to Firebase RTDB) → centralized "Portal API" model (clients → Express.js backend → Firebase RTDB), a 5-phase migration.
- **Verified implemented (per audit):** Express.js Portal API routes (`device.routes.js`: control/actuation/schedules/pairing/admin), global try/catch wrapper, `audit.js` middleware → `audit_logs` collection (**MongoDB confirmed**, see §5); `database.rules.json` enforces `.write:false` globally under the Device node (local codebase only — live deployment **[UNCONFIRMED]**); Flutter app (`api_client.dart`, `device_service.dart`) routes all commands through the centralized API; offline/local fallback — `DeviceService.updateMotorStatus` pings the ESP's local IP (`http://<wifiIp>/motorOn`) when cloud is unreachable, queues audit events via `sync_service.dart` (SharedPreferences); Portal parity (`Devices.jsx` w/ `PairModal`/`RenameModal`); Admin `Audit.jsx` log viewer; `pdfService.js` (`jspdf`) for fleet/usage PDF reports.
- **Frontend detail:** mobile — Flutter (StatefulWidget, AnimationController, GetX, `syncfusion_flutter_charts`, raw Firebase SDKs incl. `firebase_database`); web portal — React (hooks, `react-router-dom`, CSS-var theming, custom hooks `usePortalDevices`/`usePortalAuth` abstracting Firebase RTDB listeners w/ `useEffect` teardown). Portal is a deliberate UX translation (enterprise grid layout), not a blind copy of the app's dense mobile patterns.
- **Pairing workflow:** NOT aligned across clients (see §5) — app bypasses the API entirely, connects directly to the ESP AP (`192.168.4.1/credentials`); portal expects a mediated 6-digit-code flow.
- **Security work (personal):** audited legacy codebase, found exposed MongoDB URIs + JWT secrets committed to `server/.env` across specific commits; rotated credentials, secured env-var management; separately remediated unauthenticated e-commerce API routes and a CORS origin-reflection flaw.
- **P0 caveat (from audit, must travel with any resume framing):** recent changes across `demetronics-website` (portal+backend) and `demetronicsapp` are **not committed to Git** (untracked on `feature/portal` branch, or entirely untracked for the app).
- **Also unconfirmed per audit:** `database.rules.json` deployment to the live Firebase project; whether offline/local-IP fallback works on a physical device disconnected from the internet; whether PDF generation renders cleanly end-to-end (logo asset untested).
- **Future scope (not yet done):** redesigning the legacy e-commerce website, kept architecturally separate from the IoT platform.

### QEC Auto-Filler (browser extension)
- Auto-fills Air University's mandatory QEC course-evaluation form; configurable default answers/exceptions, autonomous mode loops all subjects, manual override preserved.
- **Evidence:** 1,000+ students adopted within days of release (Ahmad's consistent account); 2 GitHub stars.
- Interview anecdote: campus recognition; briefly (incorrectly) misattributed to "a senior" in a Discrete Structures class.
- **Stack:** JavaScript, HTML, CSS, Chrome Extension APIs (Manifest V3), DOM scraping.

### GradePilot / CGPA Helper (browser extension)
- CGPA/SGPA calculator replicating Air University's exact retake-replacement and non-credit/Pass-Fail rules (which the university's own portal doesn't always apply correctly).
- **Features:** Overview tab (CGPA/SGPA/credits/quality points/graduation progress); Plan tab (target-CGPA solver, per-semester roadmap, retake-opportunity finder); Simulate tab (live what-if scenarios); Portal Error Corrections; Settings (program config, JSON backup, multi-sheet Excel export).
- **Distribution:** WinGet, Inno Setup installer, manual ZIP, versioned user manual.
- **Stack:** Vanilla JS ES6+ (modularized engine/optimizer/parser/ui), vanilla CSS, Manifest V3, SheetJS.
- **No verified usage-count metric** (unlike QEC) — describe by feature completeness/distribution breadth.

### Minor / Practice Projects (not headline material, but real supporting evidence)
- **Pakistan Digital Elections (CLI+Web):** Models 266 National Assembly + 297+ Provincial seats across Punjab/Sindh/KPK/Balochistan/Islamabad. Linked lists/hash maps/queues for voter registration, seat-wise counting, time-windowed voting. SHA-256 hash-chained tamper-evident ledger. CNIC (13-digit) validation, one-vote-per-citizen. Later extended w/ C++ REST API (cpp-httplib) + browser frontend sharing the original core data structures. Built in 1 week. Web frontend built with Claude-AI assistance (disclosed openly); backend/DSA/integration done independently.
- **EMU86 Sandbox:** Educational 8086-assembly project (folder name `Sandbox_Actsurance` — an early low-level POC for Actsurance's later ideas). Interactive REPL simulating a DOS interrupt gateway vs. a fixed policy table; case-insensitive substring filtering; hash-chained in-memory audit log w/ tamper simulation + automatic fail-closed mode. Constraint: strict 16-bit 8086 only (no 32/64-bit regs, no RDTSC); runs via EMU8086/VS Code DOS-emulator ext/TASM+DOSBox.
- **Deforestation Impact on Temperature Trends:** Merged Pakistan tree-loss (2001–2024, Kaggle) + monthly temperature (1901–2016, OpenData PK) datasets; cleaned/filtered to a consistent 2001–2015 range across 6 months/year. Found higher tree-loss periods correspond to greater month-to-month temperature instability. Tools confirmed: Python, Pandas, Matplotlib. Full write-up published w/ linked datasets.
- **Sports Analyzer (C++, OOP):** Multi-sport stats analyzer (football/Euro2020, basketball/NBA2020, cricket/IPL2020), OOP class hierarchies, sorting algorithms for rankings. Context (class assignment vs. personal) — **[UNCONFIRMED]**.
- **Student Record Management System:** Built primarily by a classmate (her Sem-1 project); Ahmad's contribution was the email-notification feature via CURL, at her request. Minor, but legitimate early CURL/API-integration evidence.
- **Practice projects (verified via source/GitHub, not headline material):** Hangman (Python — file-based words + fallback list, 6/8/10 attempt limits by difficulty); Guess the Number (Python — 1–20 range, high/low hinting); Sound Recorder (Python CLI + PyQt GUI — fixed/dynamic recording, playback, normalize, trim, active commit history).
- **QB Hostels (DBMS class project, Semester 2):** 3-role system (Student/Warden/Admin) — registration/payments/complaints, room approval, oversight. Stack: HTML/CSS/JS/PHP/MySQL/XAMPP. Delivered with a full timestamped video walkthrough. Metric "40% admin time reduction" — **[UNCONFIRMED]**, omit.

---

## 8. Work Experience

| Company | Role | Dates | Location | Detail |
|---|---|---|---|---|
| Demetronics (Private) Ltd | Full Stack Development Intern (= "Full Stack Engineer Intern") | Aug–Sep 2026, concluded | Islamabad | See §7 |
| Kaar-e-Kamal Welfare Foundation | Application Developer Intern (resume-equivalent per audit: "Technical Lead & Primary Full-Stack Engineer" — see §5, §7) | Jul–Aug 2026, concluded | Islamabad, Hybrid | See §7 |
| Atif E-Commerce Services | Sales & Data Assistant (E-Commerce Automation) | Feb–May 2026, concluded | Islamabad | See below |
| AUCIS | Senior Lead Developer (promoted from Developer) | Dev: Nov 2024–Apr 2026; Sr Lead: Apr 2026–present | Air University | See §5 for scope caveat |
| Rizq Summer Internship 2026 | Management team member (volunteer/leadership, unpaid) | Summer 2026 | Islamabad | See below |

### Atif E-Commerce Services (full detail — not covered under Projects)
- **Action:** Cut e-commerce operational overhead. **Method:** Python (Pandas, Openpyxl) automation + custom GUI for stock/pricing/order tracking; LLM-based email classifier for support triage; automated SKU/inventory data-validation scripts. **Problem:** manual listing updates, support triage, and data correction were slow/error-prone across multiple client accounts (incl. Blauberg UK, Amazon/eBay).
- **Result:** ~35% reduction in listing-update time, ~45% improvement in support-handling speed, ~50% reduction in manual-correction effort. **Methodology confirmed:** timed manual-vs-automated task comparison (e.g., a ~10-min manual task → ~2 min automated). Consistent across all 3 original resume drafts.
- Also: created AI-generated product images; handled customer support via email.

### Rizq Summer Internship 2026
- Social-impact program, "Three Zero" theme; intern teams built local-problem solutions in fixed 10–12 day sprints.
- **Confirmed responsibilities:** logistics (scheduling, venue, activities); coordinated/mentored specific intern teams.
- **Program context (not personal claims):** led overall by Muhammad Hassam Ul Haq (Youth Engagement & Mobilization Lead), day-to-day by Abdul Wasay. Ahmad was one of 6 named management-team members. 7 guest speakers from WWF-Pakistan, UNICEF, Adam Smith International, Al Khidmat Foundation, Adcom Leo Burnett, Atom Camp, Assistant Commissioner Islamabad's office.

---

## 9. Quantifiable Achievements (quick reference)

~35% / ~45% / ~50% — Atif E-Commerce (listing-update time / support speed / correction effort) · 1,000+ students, 2 GitHub stars — QEC Auto-Filler · 0–100 Trust Score scale, 75+ "Featured" threshold, 30-day ad expiry — PakLand · 92.9% (158/170 commits, see §5 for a later audit's differing raw count) — Ahmad's confirmed git-forensic share of Kaar-e-Kamal codebase · 12 criteria, 18 RLS-forced tables, 24h idempotency TTL, 55s+0–6s rate-limit jitter, 3 background daemons, 11 case-lifecycle states — Kaar-e-Kamal (all per Sep 2026 forensic audit; dynamic per-case-type scoring thresholds, not fixed — see §5) · 10–12 days — Rizq sprint length · 266/297+ seats, 13-digit CNIC, 1-week build — Pakistan Digital Elections · 6/8/10 — Hangman attempt limits · 1–20 — Guess the Number range.

**Superseded:** the old "~80%/90%/85% functional/backend/frontend completion" and "35/40-pt thresholds" figures for Kaar-e-Kamal were self-reported/Aug-2026-audit estimates; the Sep 2026 forensic audit describes a more complete, tested, production-hardened state instead (§5, §7) — don't quote the old percentages.

**Do-not-use metrics:** see §6.

---

## 10. Target Roles & Applications

- **Agileday** (AI Agent Developer, Series A SaaS, Finland HQ, remote-friendly): Strong fit — Actsurance (permission-aware agent architecture), Qualix (agent product experience). Gaps: no MCP-specific experience, no GCP. Application requires 4 Q&A (why this role; proudest agent/architecture; problem solved; how AI/coding agents are used daily) — not yet drafted. **Status: evaluating, not yet applied.**
- **dexter health** (AI Engineer, healthcare AI, remote): Strong fit — Qualix (shipping-focused AI product), PyTest (evaluation/testing), OpenRouter (multi-provider), Actsurance's ONNX model (self-hosted-model reasoning). Gap: no healthcare/regulated-environment experience (nice-to-have). Recommended resume changes: explicit AI-dev-tools skills line (Claude Code/Cursor/Copilot), shipping/evaluation-framed summary, surface the ONNX self-hosted angle. **Status: evaluating, retargeted resume not finalized.**
- **Bahria Town, Rawalpindi** (Software Developer Intern, CRM/business-automation, Rs 25,000/month, 6PM–3AM in-person): fully tailored resume built. **Status/outcome: not recorded.**

---

## 11. Career Goals & Preferences

- **Short-term:** Land an AI engineering / AI-agent-development role (Agileday, dexter health under active evaluation). Both internships and the semester have since concluded.
- **Medium-term:** Continue building Actsurance and Qualix alongside employment.
- **Long-term:** Not stated in the record.
- **Target roles:** AI Engineer, AI Agent Developer, roles at the AI × security/permissions-architecture intersection (Actsurance-driven positioning).
- **Preferred industries:** No strong stated preference — evaluated a professional-services SaaS (Agileday) and healthcare AI (dexter health) without pre-existing bias toward either.
- **Preferred technical areas:** AI agents/agentic systems, RAG, security/authorization architecture for AI systems, full-stack development.
- **Geo/remote:** Islamabad-based. Open to remote (incl. Finland-hours overlap) and on-site work (applied to a local Rawalpindi internship).
- **Career constraints (historical):** was juggling full-time studies + 2 internships + a leadership role — flagged as a bandwidth constraint at the time. Both internships have since concluded; currently full-time student + AUCIS role + 2 founder ventures.

---

## 12. Education

- **Air University, Islamabad** — BS Computer Science, Sep 2024 – Sep 2028 (in progress, 3rd year). No CGPA/grades on resumes, ever. Course list available (Programming Fundamentals, OOP, Data Structures, Database Systems, Information Security, Mobile Computing, Computer Networks, Computer Organization & Assembly Language, Software Engineering, Discrete Structures, Calculus/Statistics, etc.) for an optional "Relevant Coursework" line — not currently used.
- **Pak Garrison College for Boys, Nankana Sahib** — FSc Pre-Medical, Sep 2022 – Sep 2024. Lower priority; master resume only, not targeted one-pagers.

---

## 13. Certifications

Object-Oriented Data Structures in C++ (University of Illinois, Coursera) · Fundamentals of Generative AI (Microsoft Learn) · CS50x: Introduction to Programming with Python (Harvard, edX). No hackathons/competitions recorded — NIC Lahore/Hyderabad (Actsurance) is an incubator pitch selection, not a hackathon.

---

## 14. Research & Technical Judgment

- Evaluated publishing **QEC Auto-Filler** as a CS research paper — concluded **not viable** (fails novelty/rigor criteria per Ahmad's own uploaded methodology doc: no technical innovation, no graduate-level challenge, no theoretical contribution, no rigorous quantitative evaluation). One adjacent angle (a survey-validity/evaluation-gaming study using QEC as the originating observation) would be a distinct, new, multi-month project needing ethics review. **Decision: did not pursue.**
- Evaluated **Actsurance** as a first academic paper — live literature review found the considered angles (TTL/caching security tradeoffs, an agent-firewall benchmark, formalizing an ESCALATE-style human-in-the-loop decision) already covered by real, recent (2025–2026) published work (HBHC, agent-egress-bench/Gauntlet, MI9, AURA, AESP). **Conclusion: no viable "quick" first paper; a real contribution would need months.** A self-imposed 1-week "publish something" deadline was explicitly de-prioritized in favor of an honest technical write-up over a rushed paper.
- LinkedIn posts (raw source material, not independent publications): QEC adoption story, Election Management System build story (incl. honest AI-assisted-frontend disclosure), Actsurance NIC pitch/missed-pitch story.

---

## 15. Portfolio & Open Source

- **GitHub:** github.com/ahmaadkaleeem (capitalization varies across contexts, same account) · **LinkedIn:** linkedin.com/in/ahmadkaleembhatti · **Site:** ahmadkaleem.tech
- **Public repos:** `cgpa_helper_au` (GradePilot), `qec_au` (QEC Auto-Filler), `sandbox_coal` (EMU86 Sandbox), `Programming_Practice` (Sports Analyzer, Hangman, Guess the Number, Sound Recorder, deforestation analysis)

### Open Source Contributions — `mahlernim/google-timeline-visualizer` (external, ~2.6k★, MIT; turns exported Google Timeline JSON into an on-device animated MP4 travel recap — Android app + iPhone web app + legacy Python desktop version, no account/location permissions/analytics)
- **PR #132 (merged)** — "Fix: dismiss video export notification when acknowledging in-app tray." Ahmad's first-ever OSS contribution. Fixed a completed-export notification staying in the Android drawer after in-app "Done." Added `clearNotification` to `VideoExportService`, wired via `VideoExportCoordinator.clear`. Tested on Infinix Hot 60i (Android 15). Merged; shipped in v2.2.13.
- **PR #143 → merged as #146** — "feat: embed MP4 title metadata." Embeds the resolved video title into MP4 metadata via Media3 `Mp4Muxer` (UTF-8), stores the same title in `MediaStore` (Android 10+), preserves existing title UI/logic. Verified via `gradlew test/lint/assemble*` variants, `connectedAndroidTest` on API 35/36, `pytest` (36 passing), manual `ffprobe` check. Owner requested scope-narrowing + verification output, then merged after maintainer cleanup.
- **PR #150 (closed, not merged, superseded by #153)** — "City Visited Recap" feature; closed by Ahmad himself for being "fluff" (his characterization).
- **PR #153 (Closed, not merged — supersedes #150)** — "feat(android): add City Visited Recap to New Video workflow" (resolves #149). Detected meaningful stops (filtering brief stops/GPS drift), resolved city/area via Android Geocoder (country-level fallback), grouped same-city/same-day visits; v2.3.3, versionCode 36; 17 files, +1822/-4 lines, all CI passing. **Maintainer (mahlernim) requested substantial changes before it could be considered for production**, citing: (1) the stop-detection heuristic (30-min gap + always treating the final point as a stop) could produce false visits on sparse/compressed Timeline data; (2) Android Geocoder may send precise coordinates to a network backend, which wasn't disclosed in the app's existing privacy materials (only CARTO tile traffic was disclosed at the time); (3) the 8 added JSON test fixtures weren't wired into any actual unit/instrumentation test, so CI wasn't exercising the new code despite the PR implying regression coverage; (4) new UI text was hardcoded in English despite the app supporting 9 locales; (5) the PR shouldn't carry a production version bump/changelog for experimental work. Maintainer's recommended path: a separately-installable experimental APK (distinct app ID, visible "Preview" label, explicit network-geocoding disclosure, results framed as "candidates requiring verification," real-user testing on false/missing cities, wrong dates, old data, processing time, Geocoder failures) before any production-integration PR. Ahmad closed the PR himself to rework per this guidance, then force-pushed `main` (`2452f74` → `03cd69d`). **Next step (confirmed by Ahmad):** reworking City Visited Recap with modifications addressing the maintainer's feedback before resubmitting.

### Ghost Trail — PR #176 (closed, superseded), adapted into PR #195 (merged), resolves issue #152
- **PR #176 (Closed, not merged — superseded)** — "feat: add experimental Ghost Trail rendering (#152)." Adds a `GhostTrailCache` that incrementally caches older route points in 256-point chunks so long trips (>80km) keep a faded "ghost trail" visible instead of the trail disappearing entirely past the performance-driven cutoff in `drawRouteRange()`. Renders the ghost trail beneath the active trail; new "Ghost Trail (Experimental)" toggle under Advanced Settings; gated behind a new `ghostTrailExperimental` build flavor. Precision detail: each 256-point chunk is shifted to its own local origin to avoid 32-bit float quantization when zoomed into large global paths. Also fixed a text-truncation bug on `screen_new_video.xml`'s timeline setup buttons (converted to vertical layout), then later fixed a bug where the ghost trail setting wasn't serialized for background export. 3 commits; 18 files, +266/-9 lines; all 5 checks passing. Manually tested on a 10,000+ point cross-country sample on an Infinix Hot 60i; Ahmad reported it worked effectively on sample data and moved it to user testing. **Maintainer feedback:** the caching idea was useful, but the app's v3 renderer uses a different route model — the maintainer adapted the approach into a new maintainer-authored PR (#195) rather than merging this one, crediting Ahmad's work; closed as superseded once #195 merged.
- **PR #195 (Merged, maintainer-authored)** — "Keep past routes visible in previews and videos." Adapts Ahmad's #176 approach: off-by-default "Keep past routes visible" switch, incrementally-cached completed route geometry, preserved v3 route gaps/backward seeking, preview/background-export settings kept together. Explicitly credits Ahmad as co-author for the incremental trail-caching approach he prototyped and user-tested in #176. Closes issue #152. Verified via `testGithubDebugUnitTest`; all 5 checks passed.

---

## 16. Archive: Resume Iteration History (low ongoing value, kept for continuity)

- **Master resume** (5-page reference, full detail + internal verification appendix).
- **Targeted 1-pagers:** general, AI/ML-focused, Security-focused (Actsurance-led), SWE-internship-focused, Bahria Town JD-specific.
- **LaTeX version (AI Engineer-targeted):** multiple content iterations (Rizq added, Kaar-e-Kamal bullets expanded, Deforestation project added/removed by page-length tradeoffs); fixed a `hyperref`/`xcolor` load-order color-bleed bug (resolved via `hidelinks`, dropped custom colors); fixed spacing/alignment; removed em dashes/narrative colons (per the standing Resume Orchestrator rule); resolved 1-page-vs-2-page in favor of 2 pages only if needed for readability; added Figma/portfolio links.
- **A separate iteration** (different session/tool): added Demetronics, changed Actsurance framing from "Architecting/Designing" to "Built" (later confirmed accurate), used different LaTeX macros (`\resumeEntry`+`tabularx` vs. `\entry`/`\subline`) — audited for the same issues and corrected.
- **Standing rules throughout:** no CGPA/SGPA/grades ever; no fabricated metrics; ATS-safe single-column, no icons/custom colors; zero em dashes/narrative colons; every claim traceable to confirmed evidence before use.
