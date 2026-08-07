<div align="center">
  <h1><a href="https://www.ahmadkaleem.tech">Ahmad Kaleem Bhatti</a></h1>
  <a href="https://linkedin.com/in/ahmadkaleembhatti"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <br/><br/>
  <b>Building security infrastructure for autonomous AI systems.</b>
<div align="center">
  <img src="./terminal.svg?v=3" alt="Terminal Intro" />
</div>

---

<div align="center">
  <img src="./stats.svg?v=3" alt="GitHub Stats" />
</div>

---

<img src="./header-about.svg?v=3" alt="About" />

Actsurance is a **deterministic AI security infrastructure platform** that sits between autonomous agents and their external toolset. It enforces access policies before execution, blocks malicious actions, protects API credentials, and generates tamper-evident audit logs.

Previously built **Qualix AI**, an agentic lead qualification and sales automation platform for WhatsApp and Instagram.

Open to **AI Engineering**, **Backend Architecture**, and **Agentic AI** opportunities.

---

<img src="./header-building.svg?v=3" alt="What I'm Building" />

## [Actsurance](https://actsurance.qualixofficial.com)

Most production AI systems lack a deterministic control layer between AI agents and the external tools they invoke. Agents can execute tool calls autonomously without consistent policy enforcement, credential protection, or verifiable audit trails.

Actsurance addresses this by intercepting every tool request before execution, evaluating deterministic authorization policies, protecting sensitive credentials, and producing cryptographically verifiable audit receipts.

### Core Components

- **Request Normalizer** converts incoming tool calls into a canonical `PolicyRequest`, with `ESCALATE` treated as a first-class authorization outcome.
- **Cedar Policy Engine** provides deterministic, auditable policy-as-code authorization.
- **Tiered Identity Validator** supports JWKS caching with a five-minute TTL, last-known-key fallback, and automated mTLS certificate rotation through cert-manager.
- **SDK Bypass Detection** identifies suspicious JWT ID (`jti`) reuse patterns.
- **Receipt Engine** provides asynchronous, queue-backed, tamper-evident audit logging.

Related research includes **[EMU86 Sandbox](https://github.com/AhmaadKaleeem/sandbox_coal/tree/master/Code)**, an educational 8086 assembly project exploring policy enforcement, fail-closed execution, and hash-chained audit logging before applying those concepts to the production architecture.

---

## Qualix AI

Agentic lead qualification platform supporting WhatsApp and Instagram automation.

### Features

- RAG-based context retrieval using LangChain and ChromaDB
- Tool-calling workflows for live CRM updates
- FastAPI backend with PostgreSQL, Redis, and Celery
- OpenAI integration for intent detection and response generation

---

<img src="./header-stack.svg?v=3" alt="Stack" />

### Languages
`Python` `TypeScript` `JavaScript` `Go` `C++` `Dart`

### AI
`OpenAI API` `Anthropic Claude API` `AI Agents` `Tool Calling` `LangChain` `RAG` `ChromaDB` `Prompt Engineering`

### Backend
`FastAPI` `PostgreSQL` `Redis` `Celery` `REST APIs` `Docker` `Kubernetes` `Webhooks`

### Security
`RBAC` `JWT` `mTLS` `Policy-as-Code (Cedar)` `Audit Logging`

### Frontend
`React` `Next.js` `Flutter` `Vite` `Tailwind CSS`

### Data
`SQL` `NoSQL` `Pandas` `OpenPyXL` `Supabase` `Firebase` `n8n` `PyTest`

---

<img src="./header-projects.svg?v=3" alt="Projects" />

## [Actsurance](https://actsurance.qualixofficial.com)
AI security infrastructure for autonomous agent systems with deterministic policy enforcement, credential protection, tool authorization, and tamper-evident audit logging.

## Qualix AI
Agentic lead qualification platform featuring RAG pipelines, LangChain orchestration, tool-calling workflows, and multi-channel sales automation.

## [GradePilot](https://github.com/AhmaadKaleeem/cgpa_helper_au)
Chrome extension that calculates CGPA and SGPA according to Air University's official retake and exclusion rules. Includes scenario simulation, Excel export, WinGet distribution, and complete user documentation.

## [QEC Auto-Filler](https://github.com/AhmaadKaleeem/qec_au)
Chrome extension that automated completion of Air University's mandatory course evaluation forms. Adopted by more than **1,000 students** within days of release.

## [EMU86 Sandbox](https://github.com/AhmaadKaleeem/sandbox_coal/tree/master/Code)
Educational 8086 assembly sandbox implementing policy enforcement concepts including fail-closed execution, tamper detection, and hash-chained audit logging.

## Pak Land Property Marketplace
Mobile-first Flutter application featuring geo-based booking, trust scoring, and automated listing moderation using n8n workflows. Developed as an academic project.

## Pakistan Digital Elections
C++ election processing platform with CNIC validation, role-based access control, hash-based vote verification, and a real-time JavaScript dashboard.

---

<img src="./header-background.svg?v=3" alt="Background" />

**Bachelor of Computer Science**  
Air University Islamabad  
2024-2028

**Senior Lead Developer**  
Air University Computing and Innovation Society (AUCIS)  
Nov 2024-Present

**Application Developer Intern**  
Kaar-e-Kamal Welfare Foundation  
Jul 2026-Present

**Sales and Data Assistant**  
Atif E-Commerce Services  
Feb 2026-May 2026

---

<img src="./header-certifications.svg?v=3" alt="Certifications" />

- Object-Oriented Data Structures in C++, University of Illinois (Coursera)
- CS50's Introduction to Programming with Python, Harvard University (edX)
- Fundamentals of Generative AI, Microsoft Learn

---

<img src="./header-contact.svg?v=3" alt="Contact" />

- **LinkedIn:** https://linkedin.com/in/ahmadkaleembhatti
- **GitHub:** https://github.com/AhmaadKaleeem
- **Email:** ahmadkaleeem1@gmail.com
- **Location:** Islamabad, Pakistan
