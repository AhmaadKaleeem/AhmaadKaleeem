<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
    <img alt="Ahmad Kaleem Bhatti" src="assets/banner-dark.svg" width="100%">
  </picture>
</p>

<p align="center">
  <a href="mailto:ahmadkaleeem1@gmail.com">ahmadkaleeem1@gmail.com</a>
  &ensp;·&ensp;
  <a href="https://linkedin.com/in/ahmadkaleembhatti">LinkedIn</a>
  &ensp;·&ensp;
  <a href="https://www.ahmadkaleem.tech">Portfolio</a>
  &ensp;·&ensp;
  <a href="https://github.com/AhmaadKaleeem">GitHub</a>
</p>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="https://raw.githubusercontent.com/AhmaadKaleeem/AhmaadKaleeem/output/snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/AhmaadKaleeem/AhmaadKaleeem/output/snake-light.svg">
  <img alt="Contribution snake" src="https://raw.githubusercontent.com/AhmaadKaleeem/AhmaadKaleeem/output/snake-dark.svg" width="100%">
</picture>

<br>
<img src="assets/divider.svg" width="100%" alt="">
<br>

### What I build

<table width="100%"><tr>
<td width="50%" valign="top">

**Backend systems**<br>
APIs, layered architecture, background daemons, idempotency, rate limiting, RBAC.

`Go` `Python` `FastAPI` `PostgreSQL` `Redis` `Celery`

</td>
<td width="50%" valign="top">

**AI applications**<br>
Retrieval-augmented pipelines, tool calling, multi-provider LLM orchestration, agent authorization.

`LangChain` `RAG` `OpenRouter` `OPA` `ONNX`

</td>
</tr><tr>
<td width="50%" valign="top">

**Security engineering**<br>
RBAC built three ways, JWT with real-time revocation, policy enforcement that defaults to deny.

`JWT` `OPA/Rego` `RLS` `RE2` `Ed25519`

</td>
<td width="50%" valign="top">

**Mobile & offline-first**<br>
Flutter apps that work without internet, queue locally, and sync without duplicating data on reconnect.

`Flutter` `Dart` `SharedPreferences` `Riverpod`

</td>
</tr></table>

<img src="assets/divider.svg" width="100%" alt="">

### Shipped

---

<table width="100%"><tr>
<td valign="top">

**01 &ensp; Kaar-e-Kamal** &ensp; <img src="assets/badge-shipped.svg" alt="SHIPPED" height="16">

A welfare management platform that handles assistance cases across applicants, field workers, operations, and administrators. 

**What I built:** I led the MVP and built the core system. Different roles get different workflows and access to the information they need, from initial submission to final delivery.

**Engineering underneath:** The system uses a Go backend and PostgreSQL database to enforce business rules, with a Flutter mobile app for users. The backend owns authorization, using JWTs, PostgreSQL Row-Level Security, and a synchronized offline queue for field workers operating without internet.

**Evidence:** 92.9% of the 170 commits across the repository are mine.

<details>
<summary>Technical depth</summary>

**Concurrency.** Case eligibility (one Rozgar grant per lifetime; one Rashan or Fees case active at a time per CNIC) is enforced via `pg_advisory_xact_lock(hashtext(cnic || "::" || case_type))` inside each insert transaction. Advisory locks were chosen deliberately over `SELECT FOR UPDATE` because they serialize only on the same CNIC+type without blocking unrelated inserts.

**Idempotency.** Every case creation request carries a SHA-256 fingerprint of `userID + payload`. A Redis `SetNX` lock (24h TTL) ensures a resubmitted request returns `409 IDEMPOTENCY_KEY_REUSED` rather than creating a duplicate. A mid-retry network drop still cannot double-create a case.

**Rate limiting.** Redis `TxPipeline` fixed-window counter with random TTL jitter (55s + 0–6s) prevents thundering-herd cache-stampede on key expiry. In-memory `golang.org/x/time/rate` token-bucket fallback if Redis goes down.

**Scoring engine.** Admin submits a `map[string]bool` scorecard. The server rejects numeric or non-boolean types to block point-injection. It evaluates against dynamic, DB-configurable thresholds (`passing_score`, `manual_review_score`) set by Super Admin sliders — not hardcoded constants. Output: `approved`, `manual_review`, or `rejected`.

**RBAC & RLS.** Middleware re-queries the `profiles` table on every request rather than trusting JWT claims alone. Role revocations take effect immediately. Row-Level Security is `FORCE`d across all 18 tables, and anonymous access is globally revoked.

**Offline sync.** Field and Op workers queue verifications locally in `SharedPreferences` when offline. `SyncWorker` monitors connectivity and app lifecycle. On reconnect it runs a two-phase flush: upload binary evidence to Supabase Storage first, then submit the JSON payload with the original idempotency key, so a second network drop mid-retry still cannot duplicate the case.

**Background daemons.** Three goroutines using `time.Ticker` + context cancellation: hourly auto-escalation, 30-second notification dispatcher (SMTP), 5-minute delivery-retry engine.

</details>

</td>
</tr></table>

---

<table width="100%"><tr>
<td valign="top">

**02 &ensp; Qualix** &ensp; <img src="assets/badge-shipped.svg" alt="SHIPPED" height="16">

An AI sales and support system that helps businesses handle customer conversations and qualify leads across messaging apps like WhatsApp, Instagram, and Telegram.

**What I built:** I built the retrieval system that connects conversations with business knowledge, and the background systems that allow agents to execute follow-ups.

**Engineering underneath:** The system uses RAG, tool calling, and background task queues. Agents retrieve relevant business information at inference time and use controlled backend APIs to perform actions instead of only generating replies.

<details>
<summary>Technical depth</summary>

**Retrieval.** Hybrid RAG using LangChain and ChromaDB to pull business context at inference time, so agents answer from live business data rather than stale training knowledge.

**Background processing.** Celery workers handle follow-up scheduling. Celery Beat manages periodic tasks. Redis as the broker.

**Multi-provider LLM.** Routes to OpenRouter, OpenAI, and Nvidia NIM depending on task requirements.

**Testing.** PyTest suites covering API behavior, lead-qualification logic, RAG retrieval accuracy, and tool-calling flows. Ruff, MyPy, Bandit, and pip-audit as CI gates.

**Stack.** Python 3.12, FastAPI, async SQLAlchemy 2.0, PostgreSQL 16 with PgBouncer, Redis 7, React 19 + Vite + TypeScript frontend, Next.js landing site.

</details>

</td>
</tr></table>

---

<table width="100%"><tr>
<td valign="top">

**03 &ensp; Demetronics** &ensp; <sub>Full Stack Development Intern, Aug–Sep 2026</sub> &ensp; <img src="assets/badge-shipped.svg" alt="SHIPPED" height="16">

A smart water management IoT system connecting mobile controls, a web portal, and backend services. 

**What I worked on:** My mandate was to move the device fleet from decentralized client-writes directly to a database, toward a centralized control model, and to fix security issues along the way.

**Engineering underneath:** Node.js, Express, MongoDB, and Firebase. Backend-side authorization controls mutations, with global audit logging and offline fallback mechanisms for device operations.

<details>
<summary>Technical depth</summary>

**Architecture shift.** Built an Express.js Portal API that stands between clients and Firebase Realtime DB. All device control, scheduling, and pairing now routes through the API rather than directly from the app.

**Audit logging.** Every state-mutating action is captured to a MongoDB `audit_logs` collection via a global `audit.js` middleware.

**Security work.** Audited the legacy codebase and found MongoDB URIs and JWT secrets committed in plaintext across several commits. Rotated the credentials and secured env-var management. Separately remediated unauthenticated e-commerce API routes and a CORS origin-reflection flaw.

**Offline fallback.** When the cloud is unreachable the Flutter app pings the device's local ESP IP directly. Audit events generated during offline operation are queued via `sync_service.dart` and flushed on reconnect.

**Note.** The recent codebase changes are in a local branch and not yet committed to the upstream Git repository.

</details>

</td>
</tr></table>

---

<table width="100%"><tr>
<td width="65%" valign="top">

**04 &ensp; PakLand** &ensp; <sub>Academic Project</sub> &ensp; <img src="assets/badge-shipped.svg" alt="SHIPPED" height="16">

A real-estate marketplace for Pakistan designed to solve the problem of fake ads, outdated prices, and unverified landlords.

**What I built:** I built the trust infrastructure. This includes a 30-day automatic ad-expiry that forces active re-verification, and an automated text moderation pipeline that routes flagged content to human review. I also engineered a 0–100 Trust Score derived from verification status and reviews that directly affects search ranking.

**Engineering underneath:** Flutter app backed by Firebase and Supabase. The moderation pipeline runs on n8n and GPT-4o-Mini.

</td>
</tr></table>

---

<table width="100%"><tr>
<td width="65%" valign="top">

**05 &ensp; QEC Auto-Filler** &ensp; <img src="assets/badge-shipped.svg" alt="SHIPPED" height="16">

A browser extension that automatically fills and submits mandatory university course evaluation forms, saving students several minutes per subject.

**Evidence:** Adopted by 1,000+ students within days of release.

**Engineering underneath:** Built with JavaScript and Chrome Manifest V3. Features configurable default answers and an autonomous mode that loops through all subjects via DOM scraping.

</td>
</tr></table>

---

<table width="100%"><tr>
<td width="65%" valign="top">

**06 &ensp; GradePilot** &ensp; <img src="assets/badge-shipped.svg" alt="SHIPPED" height="16">

A CGPA simulator that correctly applies the university's retake-replacement and non-credit rules, which the official student portal miscalculates.

**What I built:** A browser extension featuring a target-CGPA solver, per-semester roadmap, retake-opportunity finder, and live what-if scenarios. 

**Engineering underneath:** Vanilla ES6+ JavaScript modularized engine and SheetJS. Distributed via WinGet and an Inno Setup installer.

</td>
</tr></table>

<img src="assets/divider.svg" width="100%" alt="">

### Open source

Two merged PRs to [`mahlernim/google-timeline-visualizer`](https://github.com/mahlernim/google-timeline-visualizer) (~2.6k★):

**PR #132** — Fixed a completed-export notification staying in the Android notification drawer after the user acknowledged it in-app. Added `clearNotification` to `VideoExportService`, wired via `VideoExportCoordinator`. Shipped in v2.2.13.

**PR #176 → adapted as #195** — Prototyped an incremental ghost-trail cache that kept older route points visible on long trips (>80km) instead of cutting off at the performance-driven render limit. The maintainer adapted the approach into their own PR (#195), crediting the incremental trail-caching idea, and merged it.

<img src="assets/divider.svg" width="100%" alt="">

### On the workbench

<table width="100%"><tr>
<td valign="top">

**Actsurance** &ensp; <img src="assets/badge-building.svg" alt="BUILDING" height="16">

An authorization gateway that sits between autonomous AI agents and target systems. AI agents acting on real systems—databases, payments, internal APIs—have almost no access control compared to what human-facing systems use.

**What I'm building:** A system where the agent requests an action instead of holding credentials directly. A 10-step pipeline checks a firewall, evaluates policies, scores risk, and only executes if the request passes.

**Engineering underneath:** Python, Go, and OPA/Rego. The system defaults to deny. If the policy engine, risk scorer, Redis, or PostgreSQL go offline, the request is denied. Credentials are injected locally at the perimeter so the agent never sees them.

<details>
<summary>Technical depth</summary>

**Pipeline Flow:**
```text
Agent Request
  → JWT Auth (RS256 + JWKS, Redis revocation)
  → Idempotency & Rate Limiting (Redis)
  → L1 Firewall (RE2 deep packet inspection: SQLi, XSS, path traversal)
  → Authorization (OPA evaluating Rego policies, per-tenant RBAC)
  → Risk Evaluation (ONNX Runtime, local inference — no external LLM call)
  → Routing: ALLOW / DENY / ESCALATE
  → Sealed Broker Execution (credentials injected at perimeter; agent never sees them)
  → Receipt Generation (Ed25519 signed, SHA-256 hash-chained)
  → Persistence (PostgreSQL, Redis cache)
```

**Fail-closed.** If OPA, ONNX, Redis, or PostgreSQL become unavailable, the answer is DENY. This is enforced in named ADRs, not just convention.

**ESCALATE** is a first-class outcome with a real human-approval workflow, not just a fallback label.

**Current implementation state:**
- Fully implemented: OPA enforcement, sealed broker, Ed25519 crypto receipts, tamper-detection watchdog, human-approval workflow, L1 RE2 firewall, Python and Go SDKs.
- Partial: ONNX risk-scoring engine (implemented, marked partial in audit).
- Planned (Phase 2): Cedar policy backend, AWS Nitro hardware attestation.
- Observability: Jaeger (OTel), Prometheus, Grafana.

**Engineering Operating System (EOS):** The project includes an internal rule system. `AGENTS.md` forces any AI coding assistant through a context-bootstrap before it can touch the codebase. `GlobalEngineeringRules.md` is a constitutional rulebook with named principles (SEC-001 Least Privilege, REL-004 Graceful Degradation, AI-001 AI output must pass deterministic gates before deployment). 

</details>

</td>
</tr></table>

<img src="assets/divider.svg" width="100%" alt="">

<sub>
  <a href="mailto:ahmadkaleeem1@gmail.com">Email</a>
  &ensp;·&ensp;
  <a href="https://linkedin.com/in/ahmadkaleembhatti">LinkedIn</a>
  &ensp;·&ensp;
  <a href="https://www.ahmadkaleem.tech">ahmadkaleem.tech</a>
</sub>

