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

The CSV headers exactly match the **display names** introduced in the [Build Guide](../Build-Guide.md). The guide identifies the intended **svrg-prefixed schema names** separately. Dataverse may suggest field mapping automatically, but always review Choice and lookup values before completing an import. Import referenced parent records before child records: campus before halls; halls before assets; assets before sensors; alarms after assets and sensors; incidents after alarms. If you have entered the same rows manually, do not also import the CSVs.

Do not import datasets from previous experiments, previous Power Platform solutions, or unrelated AB-410 course modules. Every future dataset will be fictional and checked for consistency with the published schema.

Do not upload personal, institutional, tenant or credential information to a public repository.
