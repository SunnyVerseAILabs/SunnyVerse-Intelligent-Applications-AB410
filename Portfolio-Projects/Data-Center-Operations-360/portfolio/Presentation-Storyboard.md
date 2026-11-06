# DC360 — Final Portfolio Presentation Storyboard

[Case study](./Case-Study.md) · [Architecture](./Architecture.md) · [Demonstration](./Demo-Walkthrough.md) · [Evidence](./Evidence-Matrix.md)

Use this source-first storyboard to build an interview-ready presentation from actual verified artifacts. Slides should be legible without relying on screenshots that have not been captured. **Never invent application screenshots, performance timings, user identities, system integrations or test successes.**

| Slide | Title | Key visual / content | Speaker emphasis |
| --- | --- | --- | --- |
| 01 | Data Center Operations 360 | Fictional-data-center scope and Power Platform technology stack | Independent learning project, not a live facility system |
| 02 | The operations problem | Disconnected records → linked business workflows | Operational traceability and coordination |
| 03 | Scope and baseline | 1 campus; 2 halls; 100 assets; 24 sensors; 200 incidents; 500 starting work orders | Fixed synthetic exercise scale |
| 04 | Reference architecture | Dataverse + 3 Canvas apps + 3 model-driven apps + controlled flows + separate Power BI Import | Explain trust and data boundaries |
| 05 | Dataverse information model | Campus → Hall → Asset → Sensor, incidents and work orders | Lookups, business codes, Choices, referential integrity |
| 06 | Application portfolio | Operations Command Center; FieldOps; Capacity Planner; three model-driven apps | Purposeful app surfaces, not six disconnected demos |
| 07 | Workflow design | Status notifications/approvals and one guarded insight demonstration | Idempotency evidence and connection/identity constraints |
| 08 | Capacity planning | 42U rack plans and separate requests/allocations | Boundaries and unimplemented server-atomic concurrency |
| 09 | Analytics | 50,000 samples; Power BI's 7 tables, 6 relationships, 20 measures, 5 pages | Static synthetic measurements ≠ live telemetry |
| 10 | Quality engineering | Checker findings and UAT categories | 13 Pass/5 Not Run reported; 143 accessibility issues disclosed |
| 11 | ALM and deployment gates | Verified unmanaged export, source-control practices, missing target import | Artifact provenance is not deployment proof |
| 12 | Key outcomes / next steps | Engineering skills, limitations, responsible release boundaries | Interview-ready summary without overstating readiness |

**Visual guidance:** Use navy/teal technical palette, one focal point per slide, short labels and readable contrast. If you later insert images, use only actual redacted captures from published app versions or the authorized Power BI Desktop report. Mark conceptual diagrams as conceptual and include source links in the speaker notes or final reference slide. Any slide deck built before the final live demonstration should be labelled **portfolio presentation draft — verify runtime evidence before external use**.

**Source links:** [Complete build guide](../Build-Guide.md), [synthetic data](../data/README.md), [PBIP source](../powerbi/README.md), [public UAT template](../quality/Part-15-UAT-Matrix.csv), [architecture](./Architecture.md).
