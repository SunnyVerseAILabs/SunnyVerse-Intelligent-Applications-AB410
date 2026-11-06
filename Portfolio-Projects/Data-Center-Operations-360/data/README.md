# Practice dataset library

[Back to the Build Guide](../Build-Guide.md)

This directory will contain **original synthetic practice datasets** as the corresponding learner exercises are published. Each dataset will be linked from its relevant Build Guide section with the expected column names, record counts, validation checks, and import method.

**Available practice data:**

- [Part 01 — departments.csv](./departments.csv): six fictional departments.
- [Part 02 — campuses.csv](./campuses.csv): one fictional campus.
- [Part 02 — data-halls.csv](./data-halls.csv): two fictional data halls linked to that campus.
- [Part 03 — employee-profiles.csv](./employee-profiles.csv): 20 fictional employee profiles for initial import. After creating the records, follow [Part 03](../Build-Guide.md#part-03--build-the-employee-directory-and-reporting-hierarchy) to select the existing Department, Campus and Manager lookup records.
- [Part 04 — assets.csv](./assets.csv): 100 fictional infrastructure assets, 50 per data hall; **Data Hall** is an actual lookup and needs lookup-reference mapping.
- [Part 04 — sensors.csv](./sensors.csv): 24 fictional sensor inventory records referring to existing assets; **Asset** is an actual lookup and needs lookup-reference mapping.
- [Part 05 — alarms.csv](./alarms.csv): 120 fictional operating alarms, including 48 sensor-linked records; requires existing DC Asset and DC Sensor records.
- [Part 05 — incidents.csv](./incidents.csv): 200 fictional incidents linked to assets, employee profiles and optionally prior alarm records; import alarms before incidents.

**Part 06 — Operations Command Center** uses the existing Dataverse records from Parts 04–05. No additional dataset or CSV import is required. Follow [Part 06 in the Build Guide](../Build-Guide.md#part-06--build-the-operations-command-center-canvas-app).

**Part 07 — DC FieldOps** uses the existing Asset, Incident and Employee data plus a new **DC Field Inspection** table. Create two fictional inspection records directly through the app in [Part 07](../Build-Guide.md#part-07--build-the-field-engineer-mobile-app). No new CSV import is needed. Supporting evidence is added through the form's attachment field where enabled.

**Part 08 — Incident and Inspection Automation** uses the existing DC Incident and DC Field Inspection records. It creates two solution-aware notification flows and a configurable authorized test recipient; **no new CSV dataset** is needed. Follow [Part 08 in the Build Guide](../Build-Guide.md#part-08--automate-incident-updates-and-inspection-follow-ups).

**Part 09 — [work-orders.csv](./work-orders.csv)** contains **500** deterministic fictional maintenance work orders with **17 display-name headers**. Work orders reference existing Assets, fictional Employee Profiles and optional Incidents; the optional Related Inspection column is blank in the starting data. Complete the [Part 09 lookup-reference mapping and validation](../Build-Guide.md#s0904--import-the-500-fictional-work-orders-and-verify-references) before claiming a successful Dataverse import. Do not create duplicate parent rows or import Work Order lookup names as plain text.

**Part 10 — Change, Risk and Procedure Approvals** creates three linked Dataverse tables and small fictional practice records through model-driven forms. It also creates one controlled approval flow using an authorized test approver. **No new CSV file** is needed. Follow [Part 10](../Build-Guide.md#part-10--build-change-risk-and-maintenance-procedure-approvals). The prior Work Orders CSV remains unchanged.

**Part 11 — Supporting Operations** creates DC Vendor, DC Spare Part, DC Inventory Balance and DC Shift Handover, then builds **DC Supporting Operations Hub** with a small, manually entered fictional practice set. **No new CSV dataset** is required. Follow [Part 11](../Build-Guide.md#part-11--run-supporting-operations-vendors-spares-inventory-and-shift-handover). The existing 500 work orders and other datasets remain unchanged.

**Part 12 — [rack-plans.csv](./rack-plans.csv)** contains **20 fictional rack-capacity planning records** mapped to the existing Server Rack assets and Data Halls. Create the Part 12 planning tables and nine real Lookup relationships before import; map `Asset` to **DC Asset → Asset Name** and `Data Hall` to **DC Data Hall → Hall Name**, and map the local Planning Status Choice by label. Rack 013 and Rack 019 begin on **Hold**. The two hall baselines, three sample allocations and two capacity requests are entered as training records through the guide; no other CSV is required.

**Part 13 — Monitoring & Operational Intelligence:** [monitoring/README.md](./monitoring/README.md) indexes ten [`monitoring-readings-*.csv`](./monitoring/) files (5,000 records each, **50,000 total**) and a deterministic [generator](./monitoring/generate_monitoring.py). They use the existing 24 Sensor Codes and are combined in **Power BI Desktop Import mode**, not uploaded as 50,000 new Dataverse rows. The report also uses the existing 100 Assets, two Data Halls, 120 Alarms, 200 Incidents and 500 Work Orders as separately imported reference/operational tables. Follow [Part 13](../Build-Guide.md#part-13--build-monitoring-and-operational-intelligence-with-power-bi) for type mapping, relationships, DAX measures and reconciliation. Keep only the ten monitoring files in the Folder connector import directory. Nothing in the dataset represents live instrumentation.

**Part 14 — Rules-Based Intelligent Operations** uses small fictional practice records entered through the documented Main forms in the [Part 14 Build Guide](../Build-Guide.md#part-14--build-rules-based-intelligent-operations-and-reviewed-knowledge). It creates three related Dataverse registers (Intelligence Rule, Operational Insight and Operations Knowledge Article), one guarded manual training flow and new review pages inside the existing Supporting Operations Hub. **No new CSV is needed.** Reuse the published Incident, Work Order, Inventory Balance and Department records; do not replace them or pretend that the Power BI readings were imported into Dataverse. Optional AI prompt testing requires separate permissions and approved credits.

**Part 15 — Engineering Validation and Release Readiness** uses existing solution components and the [Part 15 UAT template](../quality/Part-15-UAT-Matrix.csv), which starts with 18 **Not Run** test cases. No new operational CSV, Dataverse table, app or flow is required. Follow [Part 15](../Build-Guide.md#part-15--engineer-test-and-prepare-the-solution-for-release) for safe checker, security, performance, ALM and regression steps. Do not publish private tenant evidence or unreviewed solution exports.

**Part 16 — [Final Portfolio Case Study](../portfolio/Case-Study.md)** connects the existing documented sources to a [public architecture diagram](../portfolio/Architecture.md), [safe demonstration walkthrough](../portfolio/Demo-Walkthrough.md), [evidence matrix](../portfolio/Evidence-Matrix.md) and [presentation storyboard](../portfolio/Presentation-Storyboard.md). The [Part 16 verification template](../quality/Part-16-Final-Verification.csv) starts with twelve Not Run checks. Part 16 **does not require new synthetic data or new Dataverse rows** and does not publish the private solution export or working UAT results.

The CSV headers exactly match the **display names** introduced in the [Build Guide](../Build-Guide.md). The guide identifies the intended **svrg-prefixed schema names** separately. Dataverse may suggest field mapping automatically, but always review Choice and lookup values before completing an import. Import referenced parent records before child records: campus before halls; halls before assets; assets before sensors; alarms after assets and sensors; incidents after alarms. If you have entered the same rows manually, do not also import the CSVs.

Do not import datasets from previous experiments, previous Power Platform solutions, or unrelated AB-410 course modules. Every future dataset will be fictional and checked for consistency with the published schema.

Do not upload personal, institutional, tenant or credential information to a public repository.
