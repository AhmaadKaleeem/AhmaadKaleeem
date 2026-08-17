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
  <img src="https://streak-stats.demolab.com/?user=AhmaadKaleeem&theme=dark&background=000000&ring=DF6513&fire=DF6513&currStreakNum=059D00&currStreakLabel=DF6513&sideNums=FFFFFF&sideLabels=FFFFFF&dates=FFFFFF&hide_border=true" alt="GitHub Streak" height="195" />
</div>

<br/>

<img src="./header-building.svg?v=8" alt="Evidence" />

### [Actsurance](https://actsurance.qualixofficial.com) | Zero-Trust Policy Gateway for Software Agents

**The Engineering Problem**
Automated agents are frequently given access to real business tools like email and databases. Most production setups lack a deterministic control layer between the language model and the external tools. A system tricked by a prompt injection attack can execute a destructive tool call with no structural barrier to stop it.

**The Solution**
Actsurance is a security infrastructure platform that intercepts every tool request before execution. It acts like an airport security checkpoint enforcing identity, running structural policy evaluations, and utilizing machine learning risk models to determine whether a tool call should be allowed, blocked, or escalated to a human supervisor.

<br/>

<div align="center">
  <img src="./actsurance-architecture.svg?v=8" alt="Actsurance Architecture" />
</div>

<br/>

<details>
<summary><b>View Technical Architecture and Implementation</b></summary>
<br/>

Actsurance is a layered security pipeline that intercepts every tool call. It acts as a deterministic policy enforcement layer, evaluating structural rules and routing requests asynchronously for human review when necessary. The core logic focuses on isolating AI agent inferences from critical external system writes, preventing prompt injection attacks from mutating data.

</details>

<br/>

### Qualix | Automated Lead Qualification Pipeline

A backend service automating lead qualification across WhatsApp and Instagram using retrieval-augmented generation and CRM tool-calling.

**The Engineering Problem** Lead qualification is a multi-step workflow. A language model call might succeed while a CRM update fails due to rate limits. A monolithic queue silently drops failed steps, resulting in dropped leads.

<details>
<summary><b>View Technical Implementation</b></summary>
<br/>

- **Architecture** Developed a **FastAPI** backend with async **SQLAlchemy 2.0**.
- **Decoupled Failures** Utilized **Celery** and **Redis 7** for independent task retries, separating LLM calls from CRM writes.
- **Workflow Orchestration** Implemented **LangChain** and **ChromaDB** to retrieve business context locally rather than stuffing context windows, routing LLM requests dynamically across OpenRouter, OpenAI, and Nvidia NIM based on cost capability.

</details>

<img src="./header-stack.svg?v=8" alt="Technical Focus" />

### Systems and Orchestration
LangChain, Retrieval-Augmented Generation, ChromaDB, ONNX, Tool Calling

### Backend and Infrastructure
FastAPI, Python, Go, TypeScript, PostgreSQL, Redis, Celery, Docker, Temporal

### Security and Identity
Open Policy Agent (OPA), Cedar, RBAC, mTLS, JWT, Vault

<img src="./header-background.svg?v=8" alt="Engineering Approach" />

- **Fail-Closed Execution** Systems must default to `ESCALATE` rather than `ALLOW`. If the ONNX risk model crashes, the fast path stops safely.
- **Decoupled Failures** External API writes and inferences fail independently and at different rates. They require separate retry queues.
- **Structural Enforcement** Defending against prompt injection is a structural problem, not a prompt engineering problem. OPA policies evaluating structured JSON tool schemas outrank probabilistic intent.

<br/>

<details>
<summary><b>View Additional Projects</b></summary>
<br/>

- **PakLand** Flutter real estate platform featuring an **n8n moderation pipeline** using Google Vision API and GPT-4o-Mini to automatically expire stale listings and assign Trust Scores to sellers.
- **[GradePilot](https://github.com/AhmaadKaleeem/cgpa_helper_au)** A Manifest V3 Chrome extension built in vanilla JavaScript that parses university DOM structures to simulate CGPA retake rules locally, distributed via WinGet.
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
