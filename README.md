<div align="center">
  <img src="./terminal.svg?v=6" alt="Identity" />
</div>

<div align="center">
  <a href="https://linkedin.com/in/ahmadkaleembhatti"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://www.ahmadkaleem.tech"><img src="https://img.shields.io/badge/Portfolio-000000?style=flat-square&logo=vercel&logoColor=white" alt="Portfolio" /></a>
</div>

<br/>

<div align="center">
  <img src="./stats.svg?v=6" alt="GitHub Stats" />
</div>

<br/>

<img src="./header-building.svg?v=6" alt="Evidence" />

### [Actsurance](https://actsurance.qualixofficial.com) — Zero-Trust Policy Gateway for AI Agents

**The Problem:**
AI agents are frequently given access to real business tools—email, CRMs, databases. However, most production setups lack a deterministic control layer between the AI and the external tools. An agent tricked by a prompt injection attack can execute a destructive tool call with no structural barrier to stop it.

**The Solution:**
Actsurance is a security infrastructure platform that intercepts every tool request before execution. It acts like an airport security checkpoint: enforcing identity, running structural policy evaluations, and utilizing ML risk models to determine whether a tool call should be allowed, blocked, or escalated to a human supervisor.

<br/>

<div align="center">
  <img src="./actsurance-architecture.svg?v=6" alt="Actsurance Architecture" />
</div>

<br/>

<details>
<summary><b>View Technical Architecture & Implementation</b></summary>
<br/>

Actsurance is a layered security pipeline that intercepts every AI agent tool call (v5.1 Firewall-First).

1. **L1 Firewall (Go sidecar):** Sub-millisecond RE2 regex inspection using OWASP-grade patterns. Detects SQL injection, command injection, PII, and credential leaks. Match = HTTP 403 HARD DENY.
2. **Routing Splitter (OPA + ONNX):** Open Policy Agent enforces static RBAC rules ("Agent X cannot call Tool Y"). ONNX provides a lightweight ML model scoring prompt intent. High-confidence ALLOWs are fast-tracked; ambiguous requests are escalated.
3. **Fast Path (Synchronous):** Evaluates OPA, retrieves secrets via the **Sealed Broker** pattern from Vault/KMS (1h TTL), forwards the external tool sync call, and returns HTTP 200 within a 180ms p99 budget.
4. **Slow Path (Asynchronous):** Staged in PostgreSQL (status: `PENDING_REVIEW`). A **Temporal** workflow starts, returning HTTP 202. The workflow waits for a human Slack signal (Approve/Deny) or a 48h timeout.
5. **Offline Verifier:** An independent open-source worker reads the Postgres audit trail to validate every decision independently without trusting Actsurance runtime state.

</details>

---

### Qualix AI — Agentic Lead Qualification Pipeline

A backend service automating lead qualification across WhatsApp and Instagram using retrieval-augmented generation (RAG) and CRM tool-calling.

**The Engineering Problem:** Lead qualification is a multi-step workflow. An LLM call might succeed while a CRM update fails due to rate limits. A monolithic queue silently drops failed steps, resulting in dropped leads.

<details>
<summary><b>View Technical Implementation</b></summary>
<br/>

- **Architecture:** Developed a **FastAPI** backend with async **SQLAlchemy 2.0**.
- **Decoupled Failures:** Utilized **Celery** and **Redis 7** for independent task retries, separating LLM calls from CRM writes.
- **Agentic Workflow:** Implemented **LangChain** and **ChromaDB** to retrieve business context locally rather than stuffing context windows, routing LLM requests dynamically across OpenRouter, OpenAI, and Nvidia NIM based on cost capability.

</details>

<img src="./header-stack.svg?v=6" alt="Technical Focus" />

### AI Systems & Orchestration
LangChain, RAG, ChromaDB, ONNX, Tool Calling

### Backend & Infrastructure
FastAPI, Python, Go, TypeScript, PostgreSQL, Redis, Celery, Docker, Temporal

### Security & Identity
Open Policy Agent (OPA), Cedar, RBAC, mTLS, JWT, Vault

<img src="./header-background.svg?v=6" alt="Engineering Approach" />

- **Fail-Closed Execution:** Systems must default to `ESCALATE` rather than `ALLOW`. If the ONNX risk model crashes, the fast path stops safely.
- **Decoupled Failures:** External API writes and LLM inferences fail independently and at different rates. They require separate retry queues.
- **Structural Enforcement:** Defending against prompt injection is a structural problem, not a prompt engineering problem. OPA policies evaluating structured JSON tool schemas outrank probabilistic intent.

<br/>
<br/>

<details>
<summary><b>View Additional Projects</b></summary>
<br/>

- **PakLand:** Flutter real estate platform featuring an **n8n moderation pipeline** using Google Vision API and GPT-4o-Mini to automatically expire stale listings and assign Trust Scores to sellers.
- **[GradePilot](https://github.com/AhmaadKaleeem/cgpa_helper_au):** A Manifest V3 Chrome extension built in vanilla JavaScript that parses university DOM structures to simulate CGPA retake rules locally, distributed via WinGet.
</details>

<div align="center">
  <img src="./header-contact.svg?v=6" alt="Contact" />
</div>

- **Portfolio:** [ahmadkaleem.tech](https://www.ahmadkaleem.tech)
- **LinkedIn:** [linkedin.com/in/ahmadkaleembhatti](https://linkedin.com/in/ahmadkaleembhatti)
- **Email:** [ahmadkaleeem1@gmail.com](mailto:ahmadkaleeem1@gmail.com)
- **Location:** Islamabad, Pakistan
