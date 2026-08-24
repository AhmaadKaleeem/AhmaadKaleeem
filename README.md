<div align="center">
  <a href="https://www.ahmadkaleem.tech">
    <img src="./name.svg?v=15" alt="Ahmad Kaleem Bhatti" />
  </a>
</div>

<div align="center">
  <img src="./terminal.svg?v=13" alt="Identity" />
</div>

<br/>

<div align="center">
  <img src="./stats.svg?v=10" alt="GitHub Stats" height="195" />
  <img src="./streak.svg" alt="GitHub Streak" height="195" />
</div>

<br/>

<div align="center">
  <img src="./radar.svg?v=1" alt="Skill Radar" height="300" />
</div>

<br/>

<div align="center">
  <img src="https://raw.githubusercontent.com/AhmaadKaleeem/AhmaadKaleeem/main/profile-3d-contrib/profile-night-rainbow.svg" alt="3D Contributions Graph" />
</div>

<br/>

<img src="./header-building.svg?v=8" alt="Evidence" />

### [Actsurance](https://www.ahmadkaleem.tech/case/actsurance) | Zero-Trust Policy Gateway for AI Agents

**The Problem**
AI agents frequently interact with production systems without deterministic access control. A prompt injection attack that tricks an agent can result in destructive tool calls with no structural barrier to prevent data mutation. 

**The Solution**
Actsurance is a fail-closed security gateway that sits between AI agents and external APIs. It acts as a strict policy enforcer, evaluating structural rules and utilizing ONNX-based risk models to determine if a tool call should be allowed, denied, or escalated to a human reviewer.

<br/>

<div align="center">
  <img src="./actsurance-architecture.svg?v=8" alt="Actsurance Architecture" />
</div>

<br/>

<details>
<summary><b>View Architecture & Implementation</b></summary>
<br/>

- **L1 Firewall**: Uses the RE2 regex engine to inspect payloads for SQL injection and XSS patterns, returning a 403 instantly on a match.
- **Deterministic Policy Enforcement**: Evaluates requests using Open Policy Agent (OPA) against strict RBAC rules.
- **The Sealed Broker Pattern**: Retrieves secrets from a local cache and injects them into outbound requests, ensuring the AI agent never sees raw credentials.
- **Cryptographic Receipts**: Every allowed action generates an Ed25519-signed, hash-chained audit trail persisted in PostgreSQL.
- **Fail-Closed Design**: If the ONNX risk engine or any core component fails, the gateway defaults to DENY or ESCALATE.

</details>

<br/>

### [Qualix](https://www.ahmadkaleem.tech/case/qualix) | Agentic Lead Qualification Pipeline

An automated lead qualification backend for WhatsApp, Instagram, and Telegram using Retrieval-Augmented Generation (RAG) and CRM tool-calling.

**The Problem**
Sales teams lose deals due to slow response times, and manual follow-up doesn't scale. Additionally, monolithic systems often drop leads entirely if a single step (like a CRM update) fails.

<details>
<summary><b>View Architecture & Implementation</b></summary>
<br/>

- **Architecture**: Developed a backend in FastAPI with async SQLAlchemy and PostgreSQL 16.
- **Decoupled Workflows**: LLM inferences and CRM writes fail independently. Utilized Redis 7 and Celery to separate these steps into reliable, independently retriable queues.
- **RAG Implementation**: Integrated LangChain and ChromaDB to retrieve necessary business context locally rather than stuffing context windows, reducing cost and latency. 
- **Dynamic Routing**: LLM requests route across OpenRouter, OpenAI, and Nvidia NIM based on cost and capability.

</details>

<img src="./header-experience.svg?v=1" alt="Experience" />

### Demetronics (Private) Limited | Full Stack Engineer Intern
*Aug 2026 – Sep 2026 | Islamabad, Pakistan*
- Architected and executed a system-wide migration from direct client-to-database writes to a centralized Express.js REST API.
- Implemented role-based access control (RBAC), Zod parameter validation, and an immutable audit logging system to secure IoT device actuations.
- Audited the legacy codebase, remediating exposed production secrets and securing the CI/CD pipeline.

### Kaar-e-Kamal Welfare Foundation | Application Developer Intern
*Jul 2026 – Aug 2026 | Islamabad, Pakistan*
- Developed the MVP for a unified welfare-services platform serving multiple NGO roles (Admin, Field Worker, Beneficiary).
- Built a modular Go backend (`net/http`) connected to Supabase PostgreSQL, featuring Redis rate-limiting and strict server-side role validation.
- Engineered offline-first capabilities in Flutter, enabling field workers to cache case data locally and sync automatically upon network reconnection.

<img src="./header-stack.svg?v=8" alt="Technical Focus" />

### Systems & Orchestration
LangChain, RAG, ChromaDB, ONNX, Tool Calling

### Backend & Infrastructure
FastAPI, Python, Go, TypeScript, PostgreSQL, Redis, Celery, Docker

### Security & Identity
Open Policy Agent (OPA), RBAC, mTLS, JWT, Vault

<img src="./header-background.svg?v=8" alt="Engineering Approach" />

- **Fail-Closed Execution**: Security systems must default to `ESCALATE` or `DENY`. If a risk model crashes, the fast path stops safely.
- **Decoupled Failures**: External API writes and model inferences fail at different rates and require separate retry queues.
- **Structural Enforcement**: Defending against prompt injections is a structural problem, not a prompt engineering problem. OPA policies evaluating structured JSON outrank probabilistic intent.

<br/>

<details>
<summary><b>View Additional Projects</b></summary>
<br/>

- **[PakLand](https://www.ahmadkaleem.tech/case/pakland)**: A Flutter real estate platform featuring a GPT-4o-Mini moderation pipeline that automatically expires stale listings and assigns Trust Scores to sellers, directly affecting their search ranking.
- **[GradePilot](https://www.ahmadkaleem.tech/case/gradepilot)**: A Manifest V3 Chrome extension built in vanilla JavaScript that parses university DOM structures to simulate CGPA retake rules locally, distributed via WinGet.

</details>

<div align="center">
  <img src="./header-contact.svg?v=11" alt="Contact" />
</div>

<div align="center">
  <a href="mailto:ahmadkaleeem1@gmail.com">
    <img src="https://img.shields.io/badge/ahmadkaleeem1@gmail.com-DF6513?style=flat-square&logo=gmail&logoColor=white" alt="Email" />
  </a>
  <a href="https://github.com/AhmaadKaleeem">
    <img src="https://img.shields.io/badge/AhmaadKaleeem-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub" />
  </a>
  <a href="https://linkedin.com/in/ahmadkaleembhatti">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://www.ahmadkaleem.tech">
    <img src="https://img.shields.io/badge/Portfolio-000000?style=flat-square&logo=vercel&logoColor=white" alt="Portfolio" />
  </a>
  <img src="https://img.shields.io/badge/Islamabad_Pakistan-059D00?style=flat-square&logo=googlemaps&logoColor=white" alt="Location" />
</div>
