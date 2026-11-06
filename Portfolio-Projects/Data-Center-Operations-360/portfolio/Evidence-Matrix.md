# Data Center Operations 360 — Evidence Matrix

[Project Case Study](./Case-Study.md) · [Architecture](./Architecture.md) · [Demonstration](./Demo-Walkthrough.md) · [Complete Build Guide](../Build-Guide.md)

This public index separates **published teaching material**, **inspected files**, **prior maker-reported tenant observations** and **tests not yet completed**. It is not a public copy of a private test report.

| ID | Portfolio claim | Public support | Evidence category | Accurate wording |
| --- | --- | --- | --- | --- |
| EV-01 | Full learning project | [Parts 00–16](../Build-Guide.md) | Public instructional source | “One cumulative 17-part build-along guide is published” |
| EV-02 | Fixed fictional organization and scale | [Practice data library](../data/README.md) | Published fictional CSVs | “One campus, two halls, 100 Assets, 24 Sensors” |
| EV-03 | Incident/maintenance baseline | [Incidents](../data/incidents.csv), [Work Orders](../data/work-orders.csv) | Published original datasets | “200 source Incidents, 500 starting Work Orders” |
| EV-04 | Monitoring experiment | [Monitoring CSVs](../data/monitoring/README.md) | Published fictional data | “50,000 readings from 24 sensor codes” |
| EV-05 | Power BI model | [Sanitized PBIP source](../powerbi/README.md) | Inspectable public source + earlier reported Desktop test | “7 tables, 6 relationships, 20 measures and 5 pages in the source; no current-session Desktop retest” |
| EV-06 | Three Canvas and three model-driven apps | [Parts 06–12](../Build-Guide.md) and [Part 16](../Build-Guide.md#part-16--present-and-verify-the-complete-data-center-operations-360-project) | Maker-reported published Play walkthrough | “Six app experiences were exercised read-only, with specific limitations disclosed” |
| EV-07 | Corrected capacity-planning explanation | [Part 12](../Build-Guide.md#part-12--plan-data-hall-rack-capacity-and-power-headroom) | Design source + maker-reported Detail screen | “Rack 013 Hold is visible in the filtered rack list and Dataverse, but missing on Detail; reserved-zero fields appear blank” |
| EV-08 | Historical flow diagnostics | [Part 14](../Build-Guide.md#part-14--build-rules-based-intelligent-operations-and-reviewed-knowledge) | Maker-reported historical run inspection | “Five flow records; historical 4 + 0 + 2 + 6 + 2 successful runs; duplicate creation skipped in DC14” |
| EV-09 | Public QA starting point | [Part 15 UAT template](../quality/Part-15-UAT-Matrix.csv) | Unexecuted 18-case learner template | “Each learner starts at Not Run; actual tenant outcomes remain private” |
| EV-10 | Verified development-source export procedure | [Part 15](../Build-Guide.md#part-15--engineer-test-and-prepare-the-solution-for-release) | Documented procedure + private, inspected package | “An unmanaged source export was verified; no target import/restore shown” |
| EV-11 | Architecture diagram | [Architecture](./Architecture.md) | Published technical documentation | “Connectors belong to Power Automate; no unverified Teams ref or live BI pipeline” |
| EV-12 | Final end-to-end walkthrough | [Demo](./Demo-Walkthrough.md), [Part 16](../Build-Guide.md#part-16--present-and-verify-the-complete-data-center-operations-360-project) | Public route + maker-reported app Play | “Seven read-only Play-mode screen captures were reported as privately redacted; no public recording was published” |
| EV-13 | Final verification evidence | [Part 16 verification template](../quality/Part-16-Final-Verification.csv) | Unexecuted public template; private maker report | “Ten Pass, one Fail (Power BI refresh), one Blocked (presentation) were reported; private results were not published” |
| EV-15 | Read-only screen-capture provenance | [Part 16](../Build-Guide.md#part-16--present-and-verify-the-complete-data-center-operations-360-project) | Maker-reported private redacted captures, not public images | “Seven candidate Play-mode images exist privately; a final recording is still pending” |
| EV-14 | Final presentation content | [Storyboard](./Presentation-Storyboard.md) | Published presentation source; private editable draft | “Twelve-slide draft exists; recorded/published demonstration evidence still pending” |

## How to interpret the categories

**Public synthetic source** can be checked without tenant access. **Private artifact inspected** means an existing file's structure/hash or references were examined; it does not prove an external import. **Maker-reported Play result** describes an authorized actual app session, not a fresh independent audit. **Not Run** and **Blocked** remain incomplete even when other tests pass. **Design-only** materials (such as an architecture diagram or storyboard) are never authentic app screenshots.

## Key limitations requiring clear disclosure

The source CSV has **500** maintenance work orders, while the earlier learning-tenant practice contained **501** because of one additional retained training row. The latest reported walkthrough observed **335 Active Work Orders** in a filtered view; these are three different valid contexts.

Two distinct cloud flows share the display name **DC08 Incident Status Notice**; the later flow has **zero history**, not an unreported successful run. The second DC14 run skipped duplicate record insertion, but its Cancelled branch was not exercised and concurrency safety was not demonstrated.

The reported filtered Rack Browse list **did display Hold** for Rack 013, but its Detail screen did **not**, and zero reserved values appeared blank. The source Dataverse row remained Hold. Its overlap precheck can be write-capable, and server-side atomic reservation conflict protection is not implemented.

The earlier engineering review documented **143 accessibility errors** and restricted role-sharing; a target solution import and non-admin role-separated testing remain unverified. Power BI Desktop **was subsequently opened**, but **Refresh failed** with a Dim Sensor cyclic-reference error affecting six queries. The loaded values remained correct; **cached model checks are not a clean source refresh**.

## Rules for adding genuine media evidence

Capture only in an authorized, controlled and privacy-reviewed session. Crop user profiles, account IDs, environment URLs, developer-environment banners, private flow connections and confidential records. Use actual *published* app versions where the caption says published; include date and precise filter context. Do not synthesize or edit a conceptual diagram into a deceptive “screenshot.”

Keep the original unmanaged solution export, private hash, tenant-specific UAT files, internal narration workbooks and production instructions **outside public GitHub**.
