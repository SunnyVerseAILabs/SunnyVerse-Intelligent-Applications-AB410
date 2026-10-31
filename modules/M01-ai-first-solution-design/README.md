# Module 01 | AI-first Solution Design
### Twinkle & Celestyn — Design & Troubleshooting Lab

**Listen:** [YouTube podcast](https://youtu.be/ejxXypKOmpk) · **Runtime:** 59:24 · **Guide type:** Timestamped listening companion

> **No hands-on lab in this module.** This episode explains how to *choose* Power Platform components; it does not narrate a Power Apps build or claim to configure a live solution. Use this page beside the audio. Actual guided builds arrive in later modules.

## 1. Jump to the part you are hearing

| Podcast time | What you will hear |
|---|---|
| [00:00](https://youtu.be/ejxXypKOmpk) | Welcome & the design challenge |
| [01:21](https://youtu.be/ejxXypKOmpk?t=81) | The scattered cooling-suggestion scenario |
| [04:21](https://youtu.be/ejxXypKOmpk?t=261) | AI-first means designing for the need |
| [09:08](https://youtu.be/ejxXypKOmpk?t=548) | Six Power Platform components |
| [12:42](https://youtu.be/ejxXypKOmpk?t=762) | Dataverse and governed records |
| [17:04](https://youtu.be/ejxXypKOmpk?t=1024) | AI for makers: Plans, flows, agents, prompts |
| [24:05](https://youtu.be/ejxXypKOmpk?t=1445) | AI for users; trustworthy summaries |
| [25:59](https://youtu.be/ejxXypKOmpk?t=1559) | Canvas versus model-driven apps |
| [30:34](https://youtu.be/ejxXypKOmpk?t=1834) | Five component-selection questions |
| [31:55](https://youtu.be/ejxXypKOmpk?t=1915) | Apply the questions to cooling proposals |
| [36:52](https://youtu.be/ejxXypKOmpk?t=2212) | Battery-storage inspection scenario |
| [38:44](https://youtu.be/ejxXypKOmpk?t=2324) | Wind partner: external access |
| [39:58](https://youtu.be/ejxXypKOmpk?t=2398) | Hydropower shift handoff |
| [41:40](https://youtu.be/ejxXypKOmpk?t=2500) | Solar document intake and simple checklists |
| [43:04](https://youtu.be/ejxXypKOmpk?t=2584) | Human-assisted, agent-assisted, autonomous |
| [47:34](https://youtu.be/ejxXypKOmpk?t=2854) | Built-in capabilities before custom agents |
| [51:04](https://youtu.be/ejxXypKOmpk?t=3064) | Connectors, APIs, plug-ins, custom UI/models |
| [57:15](https://youtu.be/ejxXypKOmpk?t=3435) | Recap and the next topic |

## 2. Quick component reference

Twinkle and Celestyn introduce these roles at [09:08](https://youtu.be/ejxXypKOmpk?t=548) and the data foundation at [12:42](https://youtu.be/ejxXypKOmpk?t=762).

| Component | When it fits |
|---|---|
| **Power Apps** | Screens for people to submit, review, or update work; canvas is layout-led, model-driven is data-led. |
| **Power Automate** | Event-triggered or scheduled routing, notifications, and other background processes. |
| **Power Pages** | A controlled external website for partners and other authorized outside users. |
| **Copilot Studio** | Agents that answer questions, collect details, or use permitted actions within limits. |
| **AI Builder** | AI-assisted extraction and classification when a genuine information-processing need exists. |
| **Power BI** | Reporting and trends from existing data; not the transactional approval system. |
| **Dataverse (foundation)** | Structured business records, relationships, permissions, and governance; accurate design still matters. |

**Maker AI vs user AI** ([17:04](https://youtu.be/ejxXypKOmpk?t=1024), [24:05](https://youtu.be/ejxXypKOmpk?t=1445)): A maker might use Plans to explore requirements, flow Copilot to propose automation, Copilot Studio to configure an agent, or prompt-building tools to draft text. A user might receive a suggested field value, a grounded record summary or a permitted conversational answer. None of these automatically makes a proposal accurate, approved or deployable.

## 3. How the cooling-suggestion design is reasoned through

At [30:34](https://youtu.be/ejxXypKOmpk?t=1834), the hosts introduce five questions; at [31:55](https://youtu.be/ejxXypKOmpk?t=1915), they apply them to **SunnyVerse Renewable Group** and its fictional data-center sustainability team.

| Design question | What the teaching scenario establishes |
|---|---|
| **1. Who uses it?** | Internal engineers and the sustainability manager; consider separate identities for outside partners. |
| **2. What data?** | An initiative record with description, owner, review status, relevant evidence and any justified estimate. |
| **3. Screen or background?** | Human-facing submission/review screens plus background notification and routing. |
| **4. Is language interpretation needed?** | Possibly to summarize lengthy technical notes; simple status routing may need no AI. |
| **5. What evidence and authority?** | Restrict access, preserve submitted evidence, and retain a designated human reviewer. |

**Illustrative architecture (not a configured solution):**

```text
Engineer submits suggestion in an app
          ↓
Governed initiative record in Dataverse
          ↓
Power Automate routes/alerts the reviewer
          ↓
Optional AI/agent drafts a summary or requests missing details
          ↓
Authorized human evaluates evidence and decides
```

An email-only inbox cannot reliably serve as the tracked approval record; an agent-only conversation is not the source of truth. Power BI can report review trends, but it is not the approval interface. The podcast uses these contrasts to explain component responsibility—not to require every component in every project.

## 4. Four short examples: the same questions, different answers

Follow the changing requirements from [36:52](https://youtu.be/ejxXypKOmpk?t=2212) to [42:59](https://youtu.be/ejxXypKOmpk?t=2579).

| Fictional team | Why the choice changes |
|---|---|
| **Battery storage** | Mobile, task-focused inspection → canvas app; governed history → Dataverse; possible image assistance → AI Builder, with technician verification. |
| **Wind operations** | External Rotor Services partner needing only its permitted appointments → consider Power Pages and carefully scoped access. |
| **Hydropower** | Shift handoff and notifications → Power Automate; an AI summary can assist but cannot replace the original safety-relevant notes. |
| **Solar operations** | Incoming supplier documents → possible extraction plus human review; a short routine checklist may need only a simple app, not AI. |

## 5. Who makes the decision?

At [43:04](https://youtu.be/ejxXypKOmpk?t=2584), the episode distinguishes three patterns:

- **Human-assisted:** AI drafts or summarizes; a person checks and decides.
- **Agent-assisted:** An agent gathers missing details, handles routine questions and escalates; the handoff retains evidence and context.
- **Bounded autonomous:** Low-impact administrative actions may run without each manual click; not unsupervised physical cooling changes or major approvals.

The takeaway is an **authority boundary**: software can move information or draft recommendations; the responsible people retain control of safety-relevant actions and consequential approvals.

## 6. Built-in first; extend only for a real gap

At [47:34](https://youtu.be/ejxXypKOmpk?t=2854), built-in assistance and managed agents are discussed. At [51:04](https://youtu.be/ejxXypKOmpk?t=3064), the conversation shifts to extension options.

| When the requirement exceeds built-in capability | Possible extension (introduced here, *not* built) |
|---|---|
| **Standard / custom connector** | Communicate with supported services or wrap a documented REST API for a specialized monitoring service. |
| **Agent tool / MCP** | Give an agent a narrowly authorized external operation; compare scope and reuse with connectors. |
| **Dataverse plug-in / custom API** | Enforce shared business logic or expose a defined operation across authorized entry points. |
| **PCF, client scripting, Power Pages extensions** | Extend app controls and site experiences when built-in UX is insufficient; developer/security review is needed. |
| **Specialized models / developer SDK** | Consider only when justified by requirements, data handling, licensing, region and evaluation. |

### Three accuracy reminders

- Dataverse **enables** governing records; correct roles, data quality and review processes still need deliberate design.
- AI output may be missing context or wrong. Distinguish a draft suggestion from verified evidence and authorization.
- Avoid outdated tutorials instructing you to add the **legacy Copilot control** to a new canvas app. Microsoft stopped allowing new additions on **February 2, 2026**. [Microsoft documentation](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/add-ai-copilot). Newer Copilot experiences depend on feature availability and licensing.

## 7. Where the actual build work starts

This module establishes **what belongs in the solution**. **Module 02** introduces effective prompting (still concept-focused); **Module 03** covers Power Apps Plans; **Modules 04–06** develop Dataverse modeling and access; **Modules 07–08** introduce canvas-app building and customization; later modules cover model-driven apps, portals and automation. Each future guide will contain click-by-click steps **only where the source and audio actually teach a practical procedure**.

---

**Official topic reference:** [Microsoft Learn — Design AI-powered business solutions with Microsoft Power Platform](https://learn.microsoft.com/en-us/training/modules/design-ai-powered-solutions-power-platform/)  
**Full podcast:** [https://youtu.be/ejxXypKOmpk](https://youtu.be/ejxXypKOmpk)  
**Created by:** SunnyVerse AI Labs · Independent educational companion · Sample organization and scenarios are fictional.