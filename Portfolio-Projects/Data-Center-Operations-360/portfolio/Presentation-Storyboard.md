# Data Center Operations 360 — Final Portfolio Presentation Storyboard

[Case Study](./Case-Study.md) · [Architecture](./Architecture.md) · [Evidence](./Evidence-Matrix.md) · [Demonstration Route](./Demo-Walkthrough.md) · [Full Build Guide](../Build-Guide.md)

This is the **source-backed content plan for a twelve-slide educational portfolio presentation**. It is not an actual recording, a source of live Power Platform access or evidence that a final screenshot has been captured. A private **editable presentation draft** can be created from these instructions, but it must be reviewed before external publication.

| Slide | Title | Central diagram or displayed facts | Accurate narration emphasis |
| --- | --- | --- | --- |
| 01 | **Data Center Operations 360** | Fictional scope; Power Apps + Dataverse + Power Automate + Power BI Desktop | Independent educational implementation, not a live facility |
| 02 | **The operational challenge** | Siloed assets, incidents, work orders, changes and shift/stock decisions becoming linked records | Traceability, cross-app context and controlled review |
| 03 | **Fixed fictional scale** | 1 campus, 2 halls, 100 assets, 24 sensors, 200 incidents, 500 starting Work Orders, 50,000 readings | A separate practice row can make tenant Work Orders 501 |
| 04 | **Architecture and trust boundaries** | Three Canvas and three model-driven apps → Dataverse; flows → Dataverse and their own connection references; CSV → Power BI | **No Teams connection reference identified** and no live Dataverse-to-Power-BI telemetry |
| 05 | **Relational data model** | Hall→Asset→Sensor; Incident/Work Order; planning, inventory, knowledge relationships | Real many-to-one Lookups, not text substitutes |
| 06 | **Six application experiences** | Command Center, FieldOps, Capacity Planner, Asset & Maintenance Manager, Change & Risk Manager, Supporting Operations Hub | Published Play state previously verified; do not invent app screenshots |
| 07 | **Automation with bounded behavior** | Five distinct flows; history **4 + 0 + 2 + 6 + 2**; DC14 skipped second insert | Same-name DC08 records differ; no Cancelled branch or race-safe concurrency proof |
| 08 | **Capacity as planning, not load** | Twenty 42U Rack Plans, held rack, 443/495 kW planning headroom, separate proposals | **Rack 013 Hold not visible** in the observed Canvas Detail, and reserved zeros may be blank |
| 09 | **Power BI synthetic analytics** | Fifty thousand samples; 290 High / 193 Low / 49,517 Normal; seven loaded tables, six relationships, twenty measures, five pages | Not real-time; a **fresh Part 16 Desktop check was Not Run** |
| 10 | **Quality engineering** | Earlier 13 Pass/5 Not Run UAT; separate final 9 Pass/2 Not Run/1 Blocked; 143 accessibility findings | Do not collapse two test cycles or count unfinished cases as Pass |
| 11 | **ALM and deployment boundary** | Private unmanaged source export verified; target import, role testing and recovery unverified | A matching export hash does not prove deployment |
| 12 | **Portfolio outcomes and next checks** | Source-first documentation, six apps, linked data, guarded workflows, analytics and disclosed gaps | Learning-demo ready with conditions—not enterprise deployment ready |

## Visual production requirements

Use a restrained navy/teal engineering palette, high contrast, descriptive slide titles, 16:9 layout and enough white space for an interview presentation. Prefer **diagrammatic illustrations built from shapes** to low-resolution screenshots. Conceptual graphics must be labelled conceptual. When authentic application captures are available, use the **published Play version**, crop identities/tenant URLs and any developer-environment banner, retain evidence of errors/warnings where relevant and cite the relevant screen.

Do not include the private unmanaged ZIP, SHA-256 checksum, UAT CSV, accounts, connection IDs, environment GUID, local user paths or behind-the-scenes production notes on a slide. Do not invent or simulate a Power Apps interface and then label it as a real capture. A **draft deck** may exist before the final privacy-reviewed recording; label the draft explicitly.

## Speaker-notes evidence rules

Every slide should answer three questions: **what is the demonstrable learning outcome**, **what public source supports it**, and **what was not tested or was limited**. Use [Evidence Matrix](./Evidence-Matrix.md) for each statement. For Slides 08–10, explain the Rack Detail UI defect, no fresh Desktop verification in the last session, and unresolved accessibility findings. Do not imply five successfully running flows simply because five records exist.

## Completion and external-sharing gate

The deck becomes externally releasable **only after** its text, diagrams, screenshot provenance, privacy and approval are reviewed. The previously reported Part 16 check **F16-11 was Blocked** because a publishable redacted capture/recording had not been produced. A static editable deck can be a valuable private preparation artifact, but it does not clear the recording gate.

**Public resources:** [Build Guide](../Build-Guide.md), [Synthetic data](../data/README.md), [Architecture](./Architecture.md), [Evidence Matrix](./Evidence-Matrix.md), [Demonstration route](./Demo-Walkthrough.md) and [Part 16 final learner template](../quality/Part-16-Final-Verification.csv).
