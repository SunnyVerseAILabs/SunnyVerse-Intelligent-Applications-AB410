# Data Center Operations 360 — Portfolio Case Study

[Project home](../README.md) · [Complete Build Guide](../Build-Guide.md) · [Architecture](./Architecture.md) · [Demonstration](./Demo-Walkthrough.md) · [Evidence](./Evidence-Matrix.md) · [Presentation Storyboard](./Presentation-Storyboard.md)

**SunnyVerse AI Labs — independent fictional engineering project.** The teaching enterprise is **SunnyVerse Renewable Group**. The project uses Microsoft Power Platform and Power BI Desktop to demonstrate connected data modeling, app development, workflow controls, analytics and evidence-led quality engineering. It is **not a live data center system or an enterprise-production deployment**.

## The engineering problem

Fictional facilities operations span equipment assets, sensor context, alarms, incidents, maintenance work, change/risk decisions, vendor/spare records, shift reviews and rack-capacity planning. Disconnected data makes it difficult to trace an incident to its source or see what work and review followed. The design objective is a coherent set of linked business records with focused user experiences, visible decision boundaries and reproducible synthetic reporting.

## Solution overview

| Layer | Components and value | What must not be inferred |
| --- | --- | --- |
| **Dataverse** | Relational operational and planning registers; Choices, required columns, real Lookups and selected alternate keys | Every business-code column has an enforced key, or the data are live facility records |
| **Three Canvas apps** | DC Operations Command Center, DC FieldOps, DC Capacity Planner | Capacity validation is an atomic conflict-free booking transaction |
| **Three model-driven apps** | DC Asset & Maintenance Manager, DC Change & Risk Manager, DC Supporting Operations Hub | Choice-based mock approval is an authenticated safety sign-off |
| **Power Automate** | Five distinct solution flow records for prior notification/approval examples and a guarded insight demonstration | All flows are On, or two same-name DC08 flows are the same record |
| **Power BI Desktop** | 50,000 synthetic readings, seven loaded tables, six relationships, twenty DAX measures, five report pages | Live Dataverse telemetry ingestion or Power BI Service publication |
| **Engineering evidence** | Checker inspections, UAT, dependencies, private unmanaged source export, public verification templates | Successful target import, complete accessibility remediation or tested least-privilege deployment |

## Fixed reproducible learning scale

| Source | Published initial data or training sample |
| --- | ---: |
| Campuses / Data Halls / Departments | 1 / 2 / 6 |
| Employee Profiles / Assets / Sensors | 20 / 100 / 24 |
| Alarms / Incidents | 120 / 200 |
| Work orders in original CSV | **500** |
| Vendor / Spare Part / Inventory Balance / Shift Handover | 2 / 3 / 3 / 2 |
| Hall Baseline / Rack Plan / Allocation / Capacity Request | 2 / 20 / 3 / 2 |
| Intelligence Rule / Knowledge Article / Operational Insight | 3 / 2 / 3 |
| Synthetic monitoring readings | **50,000** in ten CSV files |

A maker-reported final review observed **501 Work Order rows in the learning environment** because an additional **WO-TRAIN-01** practice row remained. The **500-row published CSV** is unchanged. Keeping that distinction is an example of data-lineage discipline, not a data error that automatically needs deleting.

## End-to-end experiences that were reported as tested

The final maker-reported read-only Play walkthrough verified **all six apps' saved/published versions** at the time of testing. In **Operations Command Center**, Home displayed 200 incidents, 120 alarms and 100 assets, and the search found existing **INC-0001**. **FieldOps** showed the incident list and two inspections. **Capacity Planner** displayed both hall baselines with modeled headroom **443 / 495 kW** and the 20 Rack Plans.

In the model-driven applications, **Active Work Orders** displayed **335 filtered rows** and real Asset Lookups; the Change & Risk app showed a fictional Approved change and Rejected change; the Supporting Operations Hub showed its Shift, Inventory and Intelligence navigation, with Reviewed knowledge separated from Approved knowledge by the view filters.

**Known Capacity Planner UI limitation:** Rack 013 was confirmed **Hold both in Dataverse and in the filtered Rack Browse list**, but Hold **was not visible** on the inspected Rack Detail screen. Reserved U and reserved kW were **blank instead of 0** in that screen. The underlying record was not rewritten. The separate overlap-validation path can submit data and was not exercised during the read-only closing test. These are outstanding UI/testing limitations.

## Workflow and analytics evidence

Five distinct Power Automate flows were identified. Two share the display name **DC08 Incident Status Notice**: the older has **four** historical succeeded runs; the later has **zero**. **DC08 Inspection Follow-up Notice** has **two**, **DC10 Change Approval** has **six**, and **DC14_Incident_Insight_Demo** has **two**; **14 historical runs in total**. The second DC14 run succeeded while skipping duplicate Insight insertion. The configured Cancelled Terminate branch was **not** exercised.

The Power BI project is reproduced from [ten monitoring CSVs](../data/monitoring/README.md) plus the six operational/dimension reference CSVs. The local Desktop report was verified during an earlier module, and the [sanitized PBIP source](../powerbi/README.md) is public. **A subsequent Part 16 refresh was attempted and failed** with a **Dim Sensor cyclic-reference** error that blocked six queries. All expected figures remained available from the **previously loaded model**, but the failure means the current refresh test **Fail**, not Pass. The analytical model is **not a real-time sensor pipeline**.

## Quality assessment and constraints

The separate post-export Part 15 review was reported as **13 Pass, 5 Not Run and 0 Fail**. An updated Part 16-specific private audit reported **10 Pass, 1 Fail and 1 Blocked**. Seven read-only Power Apps Play captures were collected and redacted, but the originals and redacted images remain **private**, not published. Power BI's fresh refresh failed, and the presentation/recording remains blocked pending assembly and approval. These reported results are not downloadable private UAT files and should not be copied into the public learner templates.

The prior solution check reported **148 Medium findings**, including **143 Capacity Planner accessibility findings**, with no High or Critical findings. The earlier Dataverse key review found **eight of 24 tables without Active alternate keys**, even though the checked business codes were currently duplicate-free. Role-separated non-admin testing, server-atomic rack reservation prevention, flow-identity cleanup, target-environment solution import and production recovery validation are **not complete**.

The unmanaged development solution package was exported and privately checksum-verified; the original package contains implementation/configuration metadata and is intentionally **not published**. Packaging is **Conditional**, not evidence of a successfully imported or production-ready target solution.

**Readiness:** Suitable for an **educational Power Platform demonstration with disclosed conditions**. Not verified enterprise-production ready.

## Public artifacts and reproducibility

- [Cumulative learner Build Guide, Parts 00–16](../Build-Guide.md)
- [Synthetic practice data and import notes](../data/README.md)
- [Architecture and trust boundaries](./Architecture.md)
- [Evidence matrix with provenance categories](./Evidence-Matrix.md)
- [End-to-end safe demonstration route](./Demo-Walkthrough.md)
- [12-slide presentation storyboard](./Presentation-Storyboard.md)
- [Part 16 twelve-check learner template](../quality/Part-16-Final-Verification.csv)
- [Sanitized Power BI Desktop source](../powerbi/README.md)

Reproduce the build **only in an authorized training environment**, and use synthetic records. The real Power Platform tenant, unpublished app internals, private run results, original source solution ZIP, hash ledger, credential-bearing connections, account identifiers and unredacted images are deliberately outside the public repository.

## Portfolio takeaway

**Built and documented:** relational Dataverse solution design, six complementary application experiences, guarded automation examples, planning/analytics separation and evidence-backed quality engineering. **Not claimed:** current real-time data-center integration, automatic conflict-free capacity booking, production security validation or a completed public video capture.

The project is complete as a **source-first learner portfolio**. Any remaining runtime demonstration and production-hardening work is described separately instead of being silently counted as finished.
