# Data Center Operations 360 — Portfolio Case Study

[Project home](../README.md) · [Build Guide](../Build-Guide.md) · [Architecture](./Architecture.md) · [Demonstration](./Demo-Walkthrough.md) · [Evidence index](./Evidence-Matrix.md)

**SunnyVerse AI Labs — independent educational build.** This project models a fictional data center operated by **SunnyVerse Renewable Group**. It is an original Power Platform learning environment, not a deployed facility-control system, and is not affiliated with or endorsed by Microsoft.

## The problem

A fictional operations team needs consistent registers for equipment, alarms, incidents, maintenance, changes, shift handovers, spare parts and capacity requests. Records must be connected so staff can trace an operational question to its source and review it without relying on disconnected spreadsheets. The learning objective is to demonstrate *cross-application solution engineering*, not to claim real-time instrumentation, automated electrical operations or production deployment.

## What the project demonstrates

| Capability | Implemented design / learning evidence | Important qualification |
| --- | --- | --- |
| Data architecture | Dataverse campus, halls, departments, employees, assets, sensors, incidents, work orders, changes, suppliers, capacity, rules and reviews | Sample records are fictional; some tables have no alternate key |
| Canvas experiences | **DC Operations Command Center**, **DC FieldOps**, **DC Capacity Planner** | Capacity checks are client-side, not transaction-safe reservations |
| Model-driven experiences | **DC Asset & Maintenance Manager**, **DC Change & Risk Manager**, **DC Supporting Operations Hub** | The Hub also exposes intelligence/knowledge views; access depends on roles |
| Workflow examples | Solution-aware Power Automate notification/approval and rules-first insight actions | Flow states must be verified. Two distinct flow records share the DC08 notice display name |
| Analytics | Power BI Desktop report from 50,000 synthetic readings and existing source CSVs | The report uses Import mode, not live telemetry or 50,000 Dataverse monitoring rows |
| Engineering | Solution and App checker inspection, UAT matrix, dependency review, unmanaged solution export | Development export is not a successful target import or enterprise deployment |

## Data and scale

The published synthetic data includes **1 campus**, **2 data halls**, **6 departments**, **20 fictional employees**, **100 assets**, **24 sensor-register entries**, **120 alarms**, **200 incidents**, **500 starting maintenance work-order rows**, and **50,000 monitoring readings** packaged as ten CSV batches. A subsequent practice record can make a learner's actual Dataverse work-order count **501**; that does not alter the starting CSV.

Part 12 adds **20 rack plans** and a distinct planning model for rack units, power budgets and capacity requests. Part 14 adds three human-reviewable rules, two knowledge entries and three insight examples. The portfolio evidence separates **source data**, **previously reported app tests**, and **freshly collected demonstration evidence**; these should never be represented as the same kind of proof.

## Architecture and decisions

The solution intentionally separates **transactional Dataverse records** from **high-volume synthetic monitoring data in CSV/Power BI Desktop**. Dataverse Lookups link operational entities. Canvas apps support focused task-oriented experiences; model-driven apps expose relational registers, views and main forms. Flow examples are solution-aware, with connection references and a documented approval boundary. A rules-first insight example links findings to original source records and requires human review rather than triggering physical or unsupervised actions.

See the [architecture and trust-boundary diagram](./Architecture.md) for exact data flow and what is *not* integrated.

## Validation and limitations

The implementation handoff reported a saved/published solution with **three Canvas apps**, **three model-driven apps**, **24 organization-owned Dataverse tables**, and **five solution flows** (with duplicate DC08 display names). These are **maker-supplied implementation observations**, not a fresh, independent tenant audit performed for this case study.

The Part 15 private engineering review reported **13 Pass, 5 Not Run, 0 Fail** across 18 UAT cases. The five remaining cases concern Play-mode navigation, a potentially writing capacity-overlap test, and a repeat Power BI Desktop check. Solution checker reported **148 Medium issues**, including **143 Canvas accessibility findings** in the Capacity Planner; no High or Critical findings were reported. Least-privilege role-separated testing, live Monitor timings, atomic reservation conflict handling and target-environment solution import remain unverified or incomplete. The project is therefore suitable as a **bounded learning/portfolio demonstration**, **not an enterprise production-ready deployment**.

This case study purposely omits tenant identifiers, connection details, original solution ZIP files, private UAT reports, screenshots containing user information and non-sanitized local paths.

## Review the artifacts

- [Single cumulative Build Guide — Parts 00–16](../Build-Guide.md)
- [Synthetic data library](../data/README.md)
- [Power BI path-sanitized project source](../powerbi/README.md)
- [Architecture decisions](./Architecture.md)
- [End-to-end demonstration walkthrough](./Demo-Walkthrough.md)
- [Evidence status matrix](./Evidence-Matrix.md)
- [Final presentation storyboard](./Presentation-Storyboard.md)
- [Public Part 15 UAT *template*](../quality/Part-15-UAT-Matrix.csv)

## Reproduce responsibly

Use your own authorized Power Platform learning environment; follow Part 00 onward and create the parent records before child Lookups. Import only synthetic files using validated mappings. Do not copy account-specific connection references, export archives or private maker evidence into a public repository. If a feature is disabled by licensing or permissions, document the limitation and retain the supported core.

**Portfolio statement:** This project demonstrates multi-app Power Platform solution modeling, traceable fictional operational data, controlled workflow design, analytical reporting and evidence-based quality engineering. It does not claim production-grade resilience, real-world safety authorization or autonomous facility operation.
