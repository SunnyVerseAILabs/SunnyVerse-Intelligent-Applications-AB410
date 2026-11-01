# SunnyVerse Data Center Operations 360 — Complete Build Guide

**One chronological guide: Stage 00 through S01.05**

Version 4.1 • November 1, 2026 • Independent portfolio prototype • Fictional company: SunnyVerse Renewable Group

**Scope:** Everything from the first university-environment check through creating and saving two DC Data Hall records. Stop at S01.05. Employee and asset stages are intentionally excluded.

**Reading this guide:** Each heading states the action to perform (for example, **Create DC Campus table**). The status immediately below tells you whether you have already completed that action. **Do not create duplicates of completed objects or records.**

## How to use this file

- [ ] Follow the numbered steps in order. Do not recreate existing tables, rows, or choices.

- [ ] A VERIFIED (VISIBLE) item is supported by your screenshot or reported successful test. A PENDING item still needs a save/reopen check.

- [ ] When the UI differs, write down the actual setting; do not silently substitute a different field type or Choice scope.

- [ ] After each step: Save → reopen/refresh → verify → record the actual result and screenshot.

- [ ] Do not insert personal university email addresses, environment IDs, or credentials into a public portfolio file.

## Current progress at a glance

| **Milestone**                       | **Status**             | **Evidence / outstanding item**                                     |
|-------------------------------------|------------------------|---------------------------------------------------------------------|
| Outlook and Teams self-notification | VERIFIED (user report) | Both messages received from readiness test flow.                    |
| Power Apps solution                 | VERIFIED (visible)     | SunnyVerse Data Center Operations 360 exists and opens.             |
| DC Department table                 | VERIFIED (visible)     | Standard table, primary name Department Name.                       |
| Six Department rows                 | VERIFIED (visible)     | All six codes and Active=Yes appear; explicit reload not confirmed. |
| DC Campus table + one row           | VERIFIED (visible)     | DC-PAC-01 appears; explicit reload not confirmed.                   |
| Publisher / schema / ownership      | PENDING                | Values were proposed but not visible in supplied screenshots.       |
| Global Choice + Data Hall + 2 rows  | NOT YET VERIFIED       | Complete the Global Choice, Data Hall table, lookup and hall rows in Part D.                             |

## Fixed project size

| **Campus** | **Halls** | **Assets** | **Employees** | **Incidents** | **Work orders** | **Telemetry** |
|------------|-----------|------------|---------------|---------------|-----------------|---------------|
| 1          | 2         | 100        | 20            | 200           | 500             | 50,000        |

The 100 assets, 20 employee profiles, 200 incidents, 500 work orders and 50,000 readings are future project targets, NOT cloud records that we have already imported. This guide intentionally stops at the two halls.

> **Progress notation:** **Completed** means the action has already been performed in your tenant. **Visible** means the screenshot shows the result. **Pending verification** means a refresh, properties check or run-history inspection is still outstanding. Headings describe the original build action, not an instruction to repeat completed work.

## Part A — Foundation (S00)

### S00.01 — Open the university Power Apps environment

**Status: Maker portal access VERIFIED; environment administrative type and permissions still PENDING.**

1. Open https://make.powerapps.com and sign in with the university Microsoft 365 account you are authorized to use.

2. At the upper-right Environment selector, locate the environment containing SunnyVerse Data Center Operations 360. Use only a development environment approved for your use.

3. From the left navigation select Solutions (or More → Solutions if hidden).

4. For the private log, record the environment alias and whether you can open Solutions. Do not copy school tenant identifiers into the public case study.

Do not assume the environment is a production, sandbox or developer environment solely from its display name; its type/license remains an explicit future check.

### S00.02 — Create and test the Outlook and Teams flow

**Status: Real Outlook email and Teams self-message VERIFIED by your report.**

1. Open https://make.powerautomate.com in the same authorized environment.

2. Under My flows or Create, choose New flow → Instant cloud flow. Name: DC00_Connector_Readiness_Test. Choose Manually trigger a flow and Create.

3. Add Office 365 Outlook → Send an email (V2). Set To = your own authorized school mailbox, Subject = [TEST] Data Center Operations — Outlook Connector, and Body = This is an automated test notification for the fictional SunnyVerse Data Center Operations portfolio project.

4. From the + between the manual trigger and email action, add a parallel branch. In its second branch choose Microsoft Teams → Post a message to myself; set Content type = Text if offered; Content = [TEST] SunnyVerse Data Center Operations — Teams connector successfully executed.

5. Save → Test → Manually → Run flow. Check the two actions in run history. Confirm the email was received and the Teams message appeared in your Notes/self-chat.

6. Retain this readiness flow separately. Do not treat it as the future business approval engine.

Observed result: You confirmed receipt on both Outlook and Teams. This proves these particular actions work for your account, not multi-user approvals or organization-wide Teams channel posting.

#### Narration evidence to retain

Twinkle & Celestyn (technical): Show how the instant flow was triggered, where the two independent actions live, and how delivery was verified.

Arka & Veda (architecture): Explain connector boundaries, tenant policy, and why self-notification is not proof of genuine multi-user segregation of duties.

### S00.03 — Create the solution publisher

**Status:** A solution was created, but the actual saved publisher and customization prefix have not yet been confirmed from the screenshots.

1. In [Power Apps](https://make.powerapps.com), select **Solutions → New solution**.
2. In the **Publisher** field, select **New publisher**. Fill in the values below, then select **Save**.

| Field | Value specified for the build |
|---|---|
| Publisher display name | `SunnyVerse Renewable Learning Publisher` |
| Publisher name | `SunnyVerseRenewableLearningPublisher` |
| Customization prefix | `svrg` (proposed; inspect the actual saved value) |
| Description | `Publisher for independent SunnyVerse Renewable Group learning and portfolio solutions.` |
| Choice value prefix | Leave the generated numerical value |

3. **Current checkpoint:** Because the DC360 solution is already created, **do not create a second publisher**. Instead open the existing solution's **Overview / Properties / Settings** and inspect which publisher it actually uses.
4. Record the actual **publisher display name**, **unique name**, and **customization prefix**. If the prefix is not `svrg`, document that difference rather than renaming existing components blindly.

**Why:** The publisher prefix affects generated Dataverse names for tables, columns and choices. It must be documented for future formulas and deployment.

### S00.04 — Create the Power Platform solution

**Status:** **Completed — visible in screenshot.** Solution publisher, version and managed status still require a metadata check.

1. Go to **Power Apps → Solutions → New solution**.
2. Enter the following values and select **Create / Save**:

| Property | Intended configuration |
|---|---|
| Display name | `SunnyVerse Data Center Operations 360` |
| Unique name | `SunnyVerseDataCenterOperations360` |
| Publisher | `SunnyVerse Renewable Learning Publisher` (verify actual) |
| Version | `1.0.0.0` (verify actual) |
| Description | `Independent educational portfolio prototype for fictional data center operations, asset maintenance, incident management, enterprise automation and operational intelligence.` |

3. **Current checkpoint:** The solution is already visible. Open **Solutions → SunnyVerse Data Center Operations 360**; do not create another one.
4. On **Overview / Properties**, record the actual publisher, version and managed/unmanaged status if visible. In **Objects → All**, confirm the existing DC Department and DC Campus components.

**Recorded observation:** The green *Module6 imported successfully* banner in an earlier screenshot referred to a separate import, not a DC360 solution error.

## Part B — Department master (S01.01–S01.03)

### S01.01 — Create the DC Department table

**Status:** **Completed — visible in screenshot.** Primary name and standard table type confirmed; ownership and actual schema still need inspection.

1. From the DC360 solution, select **+ New → Table** and open the **advanced table properties** option if the editor offers it.
2. Configure the table properties below and select **Create**.

| Table property | Value |
|---|---|
| Display name | `DC Department` |
| Plural display name | `DC Departments` |
| Description | `Master list of fictional data center operational departments used for organizational structure, assignment, approvals, and reporting.` |
| Primary name column | `Department Name` |
| Table type | Standard |
| Record ownership | Organization (intended; actual must be checked) |
| Schema name | Generated using actual publisher prefix; record it |

3. **Current checkpoint:** This table already exists. Open **DC360 solution → Tables → DC Department → Properties**. Confirm the table type, primary column, actual ownership and generated schema name; **do not create another table**.
4. The automatically generated **DC Department** GUID is the primary key. Never delete or manually enter that ID. `Department Code` is a separate human-readable business identifier.

### S01.02 — Create the DC Department columns

**Status:** **Completed as far as visible fields; exact underlying settings remain to be inspected.**

1. Open **DC360 solution → Tables → DC Department → Schema → Columns**.
2. Select **+ New column**. Configure **Department Code** and select **Done → Save table**.
3. Repeat **+ New column → Done → Save table** for **Operational Area** and **Active** using this table:

| Column | Data type | Required | Searchable | Other properties |
|---|---|---|---|---|
| Department Name | Text, primary name | Primary name | As created | Created with table |
| Department Code | Single line of text, Text | Business required | Yes | Max 20; Behavior Simple; description `Unique fictional department identifier, such as DC-OPS.` |
| Operational Area | Single line of text, Text | Business recommended | Yes | Max 100; Behavior Simple; description `Operational grouping used for department reporting and filtering.` |
| Active | Yes/No | Actual required level to inspect | No, where offered | Option labels `Yes` and `No`; default `Yes`; custom boolean, not Dataverse built-in Status |

4. **Current checkpoint:** These columns already appear in your screenshot. Open each column's properties and record the *actual* required, format, searchability, length, default, behavior and schema name; **do not create duplicate columns**.
5. Keep **Active**. **Do not create `Routing Enabled`**, which appeared in an earlier roadmap draft. Routing decisions will use dedicated rules later.
6. Save, reopen **Columns**, and confirm the fields are still present.

### S01.03 — Create the six department records

**Status:** **Six rows visible in screenshot.** Persistence after a fresh reload is not yet independently confirmed.

1. Select **DC Department → DC Department columns and data → Edit** (or **New row** where available).
2. Enter these six records, one per row. Leave the Dataverse-generated GUID blank:

| Department Name | Department Code | Operational Area | Active |
|---|---|---|---|
| Data Center Operations | `DC-OPS` | Campus Operations | Yes |
| Electrical Operations | `DC-ELEC` | Electrical | Yes |
| Mechanical & Cooling | `DC-MECH` | Mechanical | Yes |
| Facilities Maintenance | `DC-FAC` | Facilities | Yes |
| Safety & Compliance | `DC-SAFE` | Safety | Yes |
| IT Infrastructure | `DC-IT` | IT Infrastructure | Yes |

3. Select **Save**, or complete the grid's save mechanism.
4. **Current checkpoint:** All six rows are already visible. Select **Refresh** or leave/reopen the table. Confirm exactly six distinct Department Codes remain and all `Active` values are `Yes`. **Do not enter the same records again.**
5. Capture a post-refresh screenshot and record **PASS / FAIL**.

#### Narration evidence to retain

Twinkle & Celestyn (technical): Explain creation or inspection of columns, primary ID versus business code, and post-refresh verification.

Arka & Veda (architecture): Explain master-data reuse and why department codes are stable business identifiers but do not replace Dataverse relationship GUIDs.

## Part C — Campus master (S01.04)

### S01.04.01 — Create the DC Campus table

**Status:** **Table and one record visible in screenshot.** Ownership, schema and refresh persistence still require inspection.

1. From **Solutions → SunnyVerse Data Center Operations 360**, select **+ New → Table**, then the advanced table properties option when offered.
2. Enter the following values, inspect ownership and schema, and select **Create**:

| Table property | Value |
|---|---|
| Display name | `DC Campus` |
| Plural display name | `DC Campuses` |
| Primary name column | `Campus Name` |
| Description | `Fictional data center campus master used for facility assets, personnel, operational monitoring and reporting.` |
| Type | Standard |
| Record ownership | Organization (intended; verify actual) |
| Schema name | Record generated name and prefix |

3. **Current checkpoint:** This table already exists. Open **DC Campus → Properties** and inspect the values. Do not create a duplicate.

### S01.04.02 — Create the DC Campus columns

**Status:** Columns are visible in the campus record screenshot; underlying schema/settings not yet fully checked.

1. Open **DC Campus → Schema → Columns → + New column**.
2. Create the following columns one at a time using **Done → Save table**:

| Column | Data type | Required | Searchable | Other properties |
|---|---|---|---|---|
| Campus Name | Text, primary name | Primary name | As created | Created with table |
| Campus Code | Single line of text, Text | Business required | Yes | Max 20; Simple; stable fictional campus code |
| Region | Single line of text, Text | Business recommended | Yes | Max 100; Simple |
| Time Zone | Single line of text, Text | Business recommended | Yes | Max 100; Simple; IANA time-zone identifier |
| Active | Yes/No | Verify actual | No, where offered | Labels `Yes` / `No`; default `Yes` |

3. **Current checkpoint:** The fields already appear in your screenshot. Reopen each column's properties to capture its actual type, length, required setting, default, schema and searchability. Do not add duplicates.
4. Save/reopen the Columns view to confirm persistence.

### S01.04.03 — Create the campus record

**Status:** **One completed row visible.** Refresh persistence remains to be checked.

1. Open **DC Campus → DC Campus columns and data → Edit**.
2. Create this record:

| Campus Name | Campus Code | Region | Time Zone | Active |
|---|---|---|---|---|
| Pacific Resilience Campus | `DC-PAC-01` | Pacific | `America/Los_Angeles` | Yes |

3. Leave the system-generated **DC Campus** GUID untouched. Save the record.
4. **Current checkpoint:** This row is already visible. Refresh or reopen the table and confirm exactly one `DC-PAC-01` record remains. Do not add a second campus.
5. Capture the post-refresh evidence.

#### Narration evidence to retain

Twinkle & Celestyn (technical): Walk through table properties, text/IANA time zone and Active fields, then record validation after reload.

Arka & Veda (architecture): Explain campus as one parent for the two halls, why campus code is human-readable and lookup must reference Dataverse key.

## Part D — Data hall and Global Choice (S01.05)

Complete this entire part, verify both hall records, then STOP. Do not create DC Employee Profile or assets until we review this checkpoint.

### S01.05.01 — Create the Global Choice: DC Infrastructure Criticality

**Status: Not yet verified as created.** Follow the creation steps below; check the solution component list first to avoid duplicates.

Architecture decision: Use one GLOBAL Choice so the same infrastructure-criticality classification can be used later by DC Asset. Not to be confused with incident severity or change risk.

| **Property**          | **Exact value**                                                                                                                                         |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Component             | Global Choice (solution component), NOT local                                                                                                           |
| Display name          | DC Infrastructure Criticality                                                                                                                           |
| Name / unique schema  | Prefer suffix DCInfrastructureCriticality; actual generated full name and publisher prefix must be inspected                                            |
| Description           | Shared infrastructure criticality classification for fictional data halls and physical equipment assets. Not an incident severity or change-risk scale. |
| Option labels (order) | High → Medium → Low                                                                                                                                     |
| Option numeric values | Leave Dataverse-generated; record actual values if needed                                                                                               |
| Multi-select?         | No; field using this choice must be single-select                                                                                                       |
| Default               | None at column; explicit user choice required                                                                                                           |

1. Return to SunnyVerse Data Center Operations 360 solution objects list using breadcrumb.

2. In the solution, check **Choices** for `DC Infrastructure Criticality`. If it already exists, check its three options rather than creating a duplicate.

3. To create the choice, select **+ New → Choice**. Enter display name `DC Infrastructure Criticality` and the description above.

4. Expand Advanced options. Inspect generated Name and actual publisher prefix. If editable, prefer suffix DCInfrastructureCriticality; do not invent or force an unverified svrg prefix.

5. Edit the first option label to High; use + New choice to add Medium and then Low. Leave numeric option values automatically generated. Verify order High / Medium / Low. Keep default colors unless deliberately designing them.

6. Select Save. Return to solution → Choices; reopen DC Infrastructure Criticality and inspect labels, unique name and numeric values.

If New → Choice is unavailable, record screenshot and error rather than silently falling back to local Choice or free-text.

### S01.05.02 — Create the DC Data Hall table

**Status: Not yet verified as created.** Create it if absent; if already present, inspect its properties rather than duplicating it.

1. In the DC360 solution, select **+ New → Table → advanced properties** when offered. If `DC Data Hall` already exists in the Tables list, open its Properties instead of creating a duplicate.

| **Property**        | **Exact target**                                                                                             |
|---------------------|--------------------------------------------------------------------------------------------------------------|
| Display name        | DC Data Hall                                                                                                 |
| Plural display name | DC Data Halls                                                                                                |
| Primary name        | Hall Name                                                                                                    |
| Description         | Master register of fictional data halls, their campus ownership, criticality and designed IT power capacity. |
| Type                | Standard                                                                                                     |
| Ownership           | Organization (verify actual before creating)                                                                 |
| Schema/logical name | Inspect actual generated prefix and name                                                                     |

2. Select **Create**. Open **Table properties** and record the actual values before adding fields. Skip creation if the same table already exists.

### S01.05.03 — Create the DC Data Hall columns

Navigation repeated for each field: DC Data Hall → Schema → Columns → + New column → configure every property → Done → Save table → reopen Columns to verify. If the field exists, inspect it instead of adding a second one.

| **Column**            | **Type and choice scope**       | **All required configuration**                                                                                                                                    |
|-----------------------|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Hall Name             | Primary name / Text             | Existing; generated with table.                                                                                                                                   |
| Hall Code             | Text / Single line              | Max 30; Business required; Searchable Yes; Simple; description: Unique fictional data hall business code used for imports and integrations.                       |
| Criticality           | Choice / SINGLE select / GLOBAL | Source: DC Infrastructure Criticality (existing global choice); Required Business required; Searchable Yes; Simple if offered; Default None; High / Medium / Low. |
| Design IT Capacity kW | Decimal number                  | 2 decimal places; min 0; proposed max 100000 if designer permits; Business required; Searchable Yes; Simple; no default; units kW.                                |
| Active                | Yes/No Boolean                  | Labels Yes/No; default Yes; Optional target; Searchable No if offered; Simple if relevant.                                                                        |
| Campus                | Lookup → DC Campus              | N:1 from DC Data Hall to DC Campus; Business required; Searchable Yes; relationship behavior Prefer Referential / Restrict Delete if permitted.                   |

Criticality: detailed binding sequence: Columns → New column → Display name Criticality → Data type Choice (NOT Multi Select Choice) → existing Global Choice DC Infrastructure Criticality (select Sync with global choice = Yes if shown) → verify High / Medium / Low → Required Business required → default left empty → Done → Save table. The COLUMN schema name and GLOBAL CHOICE name are distinct; record both.

Design IT Capacity kW: Decimal number measures DESIGN capacity, not measured power. Enter minimum 0 and max 100000 only where supported; select 2 decimal places; do not use currency or floating text.

Active: Built-in Dataverse Status is not the same as our custom Active. Use a Yes/No Boolean with default Yes, not a local or global three-option Choice.

### S01.05.04 — Create the Campus lookup relationship

**Status:** Not yet verified as created. Use the relationship designer path below; create the lookup only once.

1. Within DC Data Hall select Schema → Relationships → New relationship → Many-to-one.

2. Confirm CURRENT table = DC Data Hall and RELATED table = DC Campus. This is correct direction: many halls refer to one campus.

3. Where offered, rename the lookup display name to Campus, set description Parent campus for this data hall, Required = Business required and Searchable = Yes.

4. If Advanced relationship behavior exists, prefer Referential → Restrict Delete (prevent deletion of campus when child halls exist). If not available, record actual behavior; do not claim it is configured.

5. Select Done → Save table; reopen Schema → Columns and verify EXACTLY ONE Campus lookup with related table DC Campus.

6. Reopen Relationships; record actual generated relationship name and delete behavior. Do not create an additional Lookup column if the relationship already generated one.

Alternate single approach if relationship designer is unavailable: Columns → + New column → type Lookup → target DC Campus → display name Campus → Business required → Done → Save table; return to Relationships and verify N:1. Choose ONE path, not both.

### S01.05.05 — Create the two Data Hall records

**Status:** Not yet verified as entered.

1. Open DC Data Hall columns and data → Edit (or New row). Ensure Hall Name, Hall Code, Campus, Criticality, Design IT Capacity kW, Active are visible. Use the grid’s +more/column picker if hidden.

2. For Campus, choose Pacific Resilience Campus from the lookup picker. Do not paste the GUID.

3. For Criticality choose High from the global option set. Both rows are intentionally assigned High; the field has NO default for new records.

4. Enter these exact two records, then Save:

| **Hall Name** | **Hall Code** | **Campus**                | **Criticality** | **Capacity kW** | **Active** |
|---------------|---------------|---------------------------|-----------------|-----------------|------------|
| Data Hall 01  | DC-PAC-01-H01 | Pacific Resilience Campus | High            | 2350.00         | Yes        |
| Data Hall 02  | DC-PAC-01-H02 | Pacific Resilience Campus | High            | 2500.00         | Yes        |

5. Leave and reopen/refresh data grid. Verify exactly two rows, each distinct Hall Code, both Campus lookups resolve to the SAME existing Pacific Resilience Campus, both Criticality = High, both values persist and Active = Yes.

6. Record each Dataverse GUID as system-generated only if useful for private troubleshooting. Never type it manually or publish it.

### S01.05.06 — Test the Data Hall configuration and sign off

**Status:** Pending until both Data Hall records survive a refresh and the Global Choice / Campus lookup are confirmed.

| **Issue**                                   | **Check before retrying**                                                                                               |
|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Choice missing from picker                  | Confirm saved GLOBAL choice in the same solution; inspect actual choice name; refresh; do not create duplicates.        |
| Criticality options appear locally editable | Inspect global synchronization; if you already made a local column, STOP and record its properties before changing it.  |
| Campus lookup is empty                      | Confirm DC-PAC-01 saved after refresh, correct lookup target and lookup view; do not type GUID.                         |
| Hall Code required error                    | Check required entry and exact column; verify length ≤30.                                                             |
| Capacity rejects 2350 / 2500                | Check Decimal number type and min/max, not Whole Number/invalid max.                                                    |
| Row disappears on refresh                   | Verify Save, environment, active filters, security, and whether record really persisted; do not blindly recreate.       |
| Restrict Delete unavailable                 | Capture actual relationship behavior; note as a future governance configuration.                                        |
| Schema prefix not svrg                      | Inspect solution publisher; record actual generated names; do not guess or rename existing components without analysis. |

- [ ] Solution exists, all custom objects in correct solution; publisher and actual prefix recorded or explicitly marked unresolved.

- [ ] Six department records remain after refresh; no duplicates; Active=Yes.

- [ ] One campus record remains after refresh: DC-PAC-01.

- [ ] Global Choice DC Infrastructure Criticality saved: High / Medium / Low; actual name confirmed.

- [ ] DC Data Hall exists, correct primary name and ownership checked.

- [ ] Criticality column uses single-select GLOBAL Choice, required, no default.

- [ ] Campus is one real Lookup to DC Campus, required; relationship behavior documented.

- [ ] Two Data Hall records survive refresh, correct campus, choice, capacities, Active.

- [ ] Capture post-refresh grid, Choice settings, relationship settings, errors/retests, if any.

- [ ] STOP after S01.05. Do not start employee or assets yet.

#### Narration evidence to retain

Twinkle & Celestyn (technical): Twinkle: exact portals, menu selections, global Choice creation, columns and lookup. Celestyn: distinguish PASS after refresh from save toast; investigate choice sync, lookup and numeric validation.

Arka & Veda (architecture): Arka and Veda: global reuse vs local choice, normalized campus-to-hall reference, referential integrity, deliberate design capacity vs measured load, how university tenant restricts cloud scale.

## Part E — Save your work and stop at S01.05

### Copyable progress record

Fill this in after saving and reopening the relevant records. Keep tenant identifiers private.

| Verification item | Recorded result |
|---|---|
| Date / environment alias (private) | Pending |
| Publisher display name / actual prefix | Pending |
| DC Department six-row refresh | PASS / FAIL / NOT TESTED |
| DC Campus one-row refresh | PASS / FAIL / NOT TESTED |
| Global choice full unique name | Pending |
| Global choice numeric option values (optional) | Pending |
| DC Data Hall logical name / ownership | Pending |
| Criticality column logical name / global synchronization | Pending |
| Campus lookup logical name / relationship behavior | Pending |
| Data Hall 01 saved and reopened | PASS / FAIL / NOT TESTED |
| Data Hall 02 saved and reopened | PASS / FAIL / NOT TESTED |
| Evidence screenshots | Pending |
| Error, corrective action and retest | None recorded yet |

### Expected result at the end of this guide

In one authorized university Power Platform solution: one department master with six active rows, one campus master with Pacific Resilience Campus, one reusable global infrastructure-criticality choice, and one DC Data Hall table containing two correctly linked and validated hall records. No employee, asset, incident, work-order or telemetry rows are required for this checkpoint.

### Official Microsoft references used for UI and semantics

https://learn.microsoft.com/en-us/power-apps/maker/data-platform/custom-picklists

https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-field-portal

https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-1n-relationships-portal

https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-entity-lookup

Evidence note: prior screenshots and messages support visible department/campus rows and notification success. They do NOT yet prove all underlying field configuration, refresh persistence or that Data Hall/global Choice are complete. Future videos will use verified implementation outcomes only.
