# SunnyVerse Data Center Operations 360
## Build Session 04 — S01.06: Employee Directory, Reporting Hierarchy & Campus/Department Lookups

**Version:** 4.2  
**Build date:** 2026-11-01  
**Project:** Independent fictional enterprise portfolio; 1 campus, 2 halls, 20 synthetic employee profiles.  
**Purpose:** Create a reusable employee business master for incidents, work orders, shifts, and demonstration approval routing.  
**Stop after this session:** 20 correctly linked, persisted fictional employee records and tested manager hierarchy. **Do not build assets or approval flows yet.**

> **Status policy:** This file is a *planned procedure*, not proof that any step was completed. Mark each verification PASS only after opening the actual saved objects or after the maker confirms it. Dataverse employees are **fictional business records**, not real Microsoft Entra users or independently authenticated approvers.

---

## A. Where we stand — evidence from the actual screen

- [x] Power Apps solution `SunnyVerse Data Center Operations 360` exists.
- [x] `DC Department` created; six rows displayed in an earlier screenshot.
- [x] `DC Campus` created; `Pacific Resilience Campus` (`DC-PAC-01`) displayed in an earlier screenshot.
- [x] `DC Data Hall` exists with **Data Hall 01**, **Data Hall 02**, both referring to `Pacific Resilience Campus`, both **High**, capacities **2350.00** and **2500.00 kW**, and **Active = Yes**.
- [x] One Choice component is listed in the solution. **The screen alone does not prove its exact name or global binding.**
- [ ] Reopen/refresh the three data tables and confirm rows persist; verify the Choice name and each lookup's related table.
- [ ] Confirm actual publisher customization prefix, ownership, solution type/version; **`svrg` is proposed, not yet evidenced**.
- [ ] S01.06 employee table and data: not created yet.

**Latest screenshot:** Solution navigation shows `Tables (3)`, `Choices (1)`, `Apps (0)`, and `Cloud flows (0)`; populated data grid is `DC Data Hall`.

### S01.06.00 — Final preflight

1. Open https://make.powerapps.com with your university account.
2. Select the authorized environment containing the solution.
3. Select **Solutions → SunnyVerse Data Center Operations 360**.
4. Open **Tables → DC Data Hall**, select **Edit** or view grid, then **Refresh**. Confirm both Hall Codes `DC-PAC-01-H01` and `DC-PAC-01-H02` persist with correct Campus lookups.
5. Open **Choices** and inspect the saved Choice. Our expected global Choice is **DC Infrastructure Criticality**, options **High, Medium, Low**. If it differs, record the actual value; don't create a duplicate choice automatically.
6. Return to the solution objects list. The next object must be **DC Shift Group** (the next shared Choice); search existing Choices before creation.

**Architecture note:** Keep approval permissions, actual authenticated Microsoft 365 identity, and fictional organization-persona records separate. A demonstration persona is not a security identity.

---

## B. S01.06.01 — Create the reusable Global Choice: DC Shift Group

**Why now:** We intend to reuse the same shift-group labels in the fictional employee master and later shift-roster records. **Use GLOBAL, not LOCAL.** These are group identifiers, *not hours or time-zone conversions*.

1. In solution Objects view, select **New → Choice** (or **New → More → Choice** where shown).
2. If an object named `DC Shift Group` already exists, open that object rather than creating a duplicate. This is an initial inspection, not an invitation to make two.
3. On the creation panel, enter:

| Setting | Required value |
|---|---|
| Choice display name | `DC Shift Group` |
| Type/scope | **Global Choice**, intended for reuse |
| Proposed unique/schema name suffix | `DCShiftGroup` |
| Full schema name | Let Power Apps populate from your actual publisher prefix; inspect rather than assume `svrg_DCShiftGroup` |
| Description | `Shared fictional staffing roster group classification for DC employee profiles and shift assignments.` |
| Choice labels, in order | `A`, `B`, `C`, `D` |
| Option numeric values | Keep automatically generated Dataverse values; don't manually invent numeric IDs |
| Colors | Keep defaults |
| Multi-select | **No**; consuming column is single-select |
| Default | **None on employee column**; require explicit selection |

4. Replace any sample option labels if present and add all four named options **A**, **B**, **C**, **D** using **+ New choice** as shown in your interface.
5. Select **Save**. Go back to solution **Choices**, reopen **DC Shift Group**, and verify four labels and actual generated unique name.
6. Capture the Choice settings screen (crop out university identity/tenant details).

**Check:** 4 labels, a single global component, actual name recorded. We will later reference this existing global choice, not create a local employee-specific choice.

---

## C. S01.06.02 — Create the DC Employee Profile table

1. Return to **Solutions → SunnyVerse Data Center Operations 360**.
2. Select **New → Table**. Use **Table (advanced properties)** or **Set advanced properties** where provided.
3. Enter the complete table properties before selecting Create:

| Property | Exact value / action |
|---|---|
| Display name | `DC Employee Profile` |
| Plural display name | `DC Employee Profiles` |
| Description | `Synthetic employee directory for fictional data center reporting lines, shift groups, operational assignments and simulated approval routing.` |
| Primary name column | `Employee Name` |
| Primary name type | Text, single line; maximum 150 if configurable |
| Type | Standard |
| Record ownership | **Organization** (shared fictional reference master) |
| Publisher | Existing publisher of DC360 solution |
| Schema/logical name | Inspect automatically generated prefix and full name; record actual value |

4. Confirm table type/ownership before saving: **record ownership cannot be casually changed after creation**.
5. Select **Create**. When the table overview loads, inspect **Table properties → Properties** and note the name, description, primary column, ownership and actual schema name.
6. The automatically generated `DC Employee Profile` GUID primary key is **system-managed**; never type your `EMP-000001` business ID into that GUID field.

**Check:** Solution Tables count becomes 4 if there are no unrelated additions. `DC Employee Profile` should display `Employee Name` as the primary name column.

---

## D. S01.06.03 — Create every employee business column (full settings)

For **each column** below:

1. Open **DC Employee Profile → Schema → Columns**.
2. Select **+ New column**.
3. Enter Display name and Description, select Data type and Format, inspect **Advanced options** if provided, set Behavior, Required, Searchable, limits or default.
4. Inspect the **actual generated schema name**; record it in your engineering log.
5. Select **Done** and then **Save table** where the designer requires it.
6. Reopen **Columns** and inspect the saved field's properties before continuing to the next column.

### D1 — Text business columns

| Property | Employee Code | Job Title |
|---|---|---|
| Display name | `Employee Code` | `Job Title` |
| Description | `Unique fictional business employee identifier in EMP-000001 format; not a Dataverse GUID.` | `Fictional employee's organizational job title used for display and reporting.` |
| Data type | Single line of text / Text | Single line of text / Text |
| Format | Text | Text |
| Behavior | Simple | Simple |
| Required | **Business required** | **Business required** |
| Searchable | Yes | Yes |
| Maximum characters | **20** | **100** |
| Default | Blank | Blank |
| Schema name | Confirm generated suffix `EmployeeCode` | Confirm generated suffix `JobTitle` |
| Form fill assistance | Off if offered | Off if offered |

**Do not create an Email or Microsoft 365 Person column** for these 20 fictional profiles. Real notifications will be directed to your own authorized test mailbox through private configuration, not to imaginary directory accounts.

### D2 — Shift Group (single-select Global Choice)

| Property | Exact setting |
|---|---|
| Column display name | `Shift Group` |
| Description | `Fictional staffing roster group; synchronized with the reusable DC Shift Group global Choice.` |
| Data type | **Choice** (single-select; NOT multi-select) |
| Choice type | **GLOBAL** — synchronize to saved `DC Shift Group` |
| Global Choice display name | `DC Shift Group` |
| Choice name | Use actual saved unique name (proposed suffix `DCShiftGroup`) |
| Choices | `A`, `B`, `C`, `D` |
| Required | **Business required** |
| Default | **None** |
| Searchable | Yes, if offered |
| Behavior | Simple if offered |
| Column schema name | Verify separate generated employee-column name, proposed suffix `ShiftGroup` |
| Form fill assistance | Off if offered |

**Click sequence:** Columns → New column → Display name **Shift Group** → Data type **Choice** → select **Sync with global choice = Yes** (if offered) → choose **DC Shift Group** → confirm A/B/C/D → Required **Business required** → no Default → Done → Save table.

### D3 — Yes/No columns

| Property | Active | Is Synthetic |
|---|---|---|
| Display name | `Active` | `Is Synthetic` |
| Description | `Fictional personnel record is currently eligible for operational assignment.` | `Indicates the record is entirely fictional and created for independent portfolio demonstrations.` |
| Data type | Yes/No (Boolean) | Yes/No (Boolean) |
| Options | Yes, No | Yes, No |
| Default | **Yes** | **Yes** |
| Required | Optional if offered | Optional if offered |
| Searchable | No if offered | No if offered |
| Schema suffix | `Active` (actual generated name rules apply) | `IsSynthetic` (actual generated name rules apply) |
| Is this a 3-value Choice? | **No** | **No** |

**Reminder:** A custom `Active` Boolean is different from Dataverse's built-in row Status/Status Reason.

**Result:** Employee Name (primary), Employee Code, Job Title, Shift Group, Active and Is Synthetic are visible in Columns. Lookup columns are created in the next section.

---

## E. S01.06.04 — Create Department lookup (many employees → one department)

**We will use REAL LOOKUPS, not free-text department names or manually pasted GUIDs.**

1. On **DC Employee Profile** table overview, select **Schema → Relationships**.
2. Select **New relationship → Many-to-one**.
3. Confirm **Current table = DC Employee Profile**.
4. For **Related table**, select **DC Department**.
5. If a lookup display name can be configured, set `Department`.
6. Configure these properties where displayed:

| Setting | Value |
|---|---|
| Lookup display name | `Department` |
| Lookup description | `Department to which this fictional employee is assigned.` |
| Related table | `DC Department` |
| Relationship direction | **N:1 from DC Employee Profile to DC Department** |
| Required | Business required |
| Searchable | Yes if offered |
| Relationship behavior | Prefer **Referential — Restrict Delete** if supported |
| Schema name | Record actual generated relationship and lookup names; don't guess prefix |

7. Select **Done** / **Save** as prompted, and **Save table** if shown.
8. Open **Schema → Columns**. Verify **one** `Department` lookup, with target `DC Department`.
9. Open **Relationships** again and verify the N:1 relationship appears.

**Alternative only if the relationship designer doesn't expose the option:** Columns → New column → **Lookup** → Related table **DC Department** → Display name **Department** → Required Business required → Save → verify N:1 under Relationships. **Never use both paths**, as that would create duplicate lookups.

---

## F. S01.06.05 — Create Campus lookup (many employees → one campus)

Repeat the exact relationship workflow:

1. **DC Employee Profile → Schema → Relationships → New relationship → Many-to-one**.
2. **Current table = DC Employee Profile**; **Related table = DC Campus**.
3. Configure:

| Setting | Value |
|---|---|
| Lookup display name | `Campus` |
| Description | `Fictional employee's assigned data center campus.` |
| Required | Business required |
| Searchable | Yes if offered |
| Behavior | Prefer Referential — Restrict Delete if available |
| Actual generated names | Record from your environment |

4. Select Done/Save; inspect the **Campus** lookup under Columns.
5. Use the lookup picker to check the existing parent record **Pacific Resilience Campus** appears. Do not enter `DC-PAC-01` into the Campus Lookup field; the business code is for matching source rows, while the Dataverse lookup references the existing Campus record.
6. Verify **only one** Campus lookup has been created.

---

## G. S01.06.06 — Create Manager self-lookup (employee → employee)

**Why self-reference:** One fictional manager can supervise many employee profiles; each subordinate may have zero or one manager. The top-level director must have a blank manager.

1. Open **DC Employee Profile → Schema → Relationships → New relationship → Many-to-one**.
2. Set **Current table = DC Employee Profile** and **Related table = DC Employee Profile** (the same table).
3. Where editable, rename the lookup display label to `Manager`.
4. Configure:

| Setting | Value |
|---|---|
| Lookup display name | `Manager` |
| Related table | `DC Employee Profile` (self-referencing) |
| Type | Many-to-one / N:1 |
| Required | **Optional** (Director has no manager) |
| Searchable | Yes if offered |
| Delete behavior | Prefer Referential/Restrict Delete where supported; capture actual behavior, because self-relationships may have constraints |
| Relationship and lookup schema | Record actual generated names |

5. Select Done/Save and reopen Columns. Confirm `Manager` appears as a **Lookup** referencing **DC Employee Profile**, not a text field.
6. Do not create both a Manager text field and a Manager lookup. Do not choose `System User` as the related table: those are real Microsoft identity records, not our fictional employee profiles.
7. If the self-lookup creation fails, capture the full error/screenshot. Do not replace it with free text without reviewing the design.

**Architecture safeguard:** Manager cycles (A manages B and B manages A) are not automatically prevented merely because the field is a Lookup. We'll validate hierarchy acyclicity in the seed/test process and add an application/flow guard later.

---

## H. S01.06.07 — Reconciled, canonical 20-person employee dataset

**Important correction:** The older v3.0 autogenerated sample incorrectly assigned certain role titles to unrelated departments. This v3.1 **reconciled roster** is the new canonical employee mapping. It retains the same `EmployeeID`, fictional names and shift-group values, so references in planned incident, work-order and monitoring datasets remain stable. **Do not import the older uncorrected employee CSV.**

The fictional employees below are **not** Microsoft 365 user accounts. `Manager Code` is a business ID used here to identify which *existing saved employee* to choose in the `Manager` lookup picker.

| Employee Code | Employee Name | Job Title | Department Code → lookup | Manager Code → lookup | Shift Group |
|---|---|---|---|---|---|
| EMP-000001 | Sophia Carter | Director | DC-OPS | *(blank)* | A |
| EMP-000002 | Emma Park | Operations Manager | DC-OPS | EMP-000001 | B |
| EMP-000003 | Anika Shah | Electrical Manager | DC-ELEC | EMP-000001 | C |
| EMP-000004 | Marcus Johnson | Mechanical Manager | DC-MECH | EMP-000001 | D |
| EMP-000005 | Arjun Davis | Safety Manager | DC-SAFE | EMP-000001 | A |
| EMP-000006 | David Patel | Shift Supervisor | DC-OPS | EMP-000002 | B |
| EMP-000007 | Noah Morales | Electrical Engineer | DC-ELEC | EMP-000003 | C |
| EMP-000008 | Sana Kim | Mechanical Engineer | DC-MECH | EMP-000004 | D |
| EMP-000009 | Elena Stone | Maintenance Technician | DC-FAC | EMP-000006 | A |
| EMP-000010 | Olivia Nair | IT Engineer | DC-IT | EMP-000002 | B |
| EMP-000011 | Iris Chen | Operations Analyst | DC-OPS | EMP-000002 | C |
| EMP-000012 | Jordan Wilson | Mechanical Engineer | DC-MECH | EMP-000004 | D |
| EMP-000013 | Daniel Lee | Maintenance Technician | DC-FAC | EMP-000006 | A |
| EMP-000014 | Theo Singh | Mechanical Engineer | DC-MECH | EMP-000004 | B |
| EMP-000015 | Ava Brooks | Maintenance Technician | DC-FAC | EMP-000006 | C |
| EMP-000016 | Priya Allen | Operations Analyst | DC-OPS | EMP-000002 | D |
| EMP-000017 | Mina Reed | Maintenance Technician | DC-FAC | EMP-000006 | A |
| EMP-000018 | Ethan Baker | Maintenance Technician | DC-FAC | EMP-000006 | B |
| EMP-000019 | Liam Santos | Operations Analyst | DC-OPS | EMP-000002 | C |
| EMP-000020 | Maya Iyer | Maintenance Technician | DC-FAC | EMP-000006 | D |

**For ALL 20 rows:** Campus lookup = **Pacific Resilience Campus**; Active = **Yes**; Is Synthetic = **Yes**. All names, work history, titles, shifts and reporting relationships are fictional. All 20 profiles are associated with the one fictional campus even though they have different departments.

### Why the roles and departments are aligned

- Director, Operations Manager, Shift Supervisor and Operations Analysts → **Data Center Operations**.
- Electrical Manager and Electrical Engineer → **Electrical Operations**.
- Mechanical Manager and Mechanical Engineers → **Mechanical & Cooling**.
- Safety Manager → **Safety & Compliance**.
- IT Engineer → **IT Infrastructure**.
- Maintenance Technicians → **Facilities Maintenance**.

This is a defensible *sample* reporting hierarchy; actual organization models can have matrix reporting and multiple approval authorities. The later approval matrix will be a separate configurable object, not inferred solely from one Manager lookup.

---

## I. S01.06.08 — First two rows: click by click

1. On **DC Employee Profile** table overview, find the **DC Employee Profile columns and data** section.
2. Select the purple **Edit** button (or the table's data grid editing action).
3. If some business fields aren't visible, use **+ more** / Add column picker to show: `Employee Name`, `Employee Code`, `Job Title`, `Department`, `Campus`, `Manager`, `Shift Group`, `Active`, `Is Synthetic`.
4. Start the first row:

| Field | Enter/select for first row |
|---|---|
| Employee Name | `Sophia Carter` |
| Employee Code | `EMP-000001` |
| Job Title | `Director` |
| Department | Select lookup **Data Center Operations** (not DC-OPS typed as text) |
| Campus | Select lookup **Pacific Resilience Campus** |
| Manager | Leave **blank** |
| Shift Group | Select Choice **A** |
| Active | Yes |
| Is Synthetic | Yes |

5. Save, leave/reopen or refresh. Verify `Sophia Carter` survives with the correct Department/Campus lookups and has a Dataverse-generated GUID.
6. Start the second row:

| Field | Enter/select for second row |
|---|---|
| Employee Name | `Emma Park` |
| Employee Code | `EMP-000002` |
| Job Title | `Operations Manager` |
| Department | Data Center Operations |
| Campus | Pacific Resilience Campus |
| Manager | Select saved profile **Sophia Carter** (if lookup readily available; otherwise defer to second pass below) |
| Shift Group | B |
| Active | Yes |
| Is Synthetic | Yes |

7. Save and refresh again. Confirm **two distinct Employee Codes** and their related lookup names.
8. If a lookup search returns no results, first confirm that the parent row was saved; then search by its **primary name**, not its Employee Code.

### S01.06.09 — Enter remaining 18 rows, two-pass approach

**Pass 1:** Using the roster in Section H, create rows EMP-000003 through EMP-000020 with **Employee Name, Code, Job Title, Department lookup, Campus lookup, Shift Group, Active, Is Synthetic**. Leave `Manager` empty temporarily because the field was deliberately defined Optional. Save and refresh. Confirm 20 unique Employee Codes exist.

**Pass 2:** Open each subordinate row and set `Manager` by selecting the **fictional manager's Employee Name** corresponding to the Manager Code in the roster. For example:

| Employee | Manager lookup should resolve to |
|---|---|
| Emma Park | Sophia Carter |
| Noah Morales | Anika Shah |
| Sana Kim | Marcus Johnson |
| Elena Stone | David Patel |
| David Patel | Emma Park |
| Sophia Carter | **Blank** |

**Save each update or save the grid in supported batches, then refresh.** Manager is a lookup; never type `EMP-000001` directly into a GUID column.

---

## J. S01.06.10 — Verification and completion gate

- [ ] Solution has one `DC Employee Profile` table, with primary name **Employee Name**.
- [ ] Actual schema name, publisher prefix and ownership recorded (or explicitly unresolved).
- [ ] Exactly one global `DC Shift Group` with **A/B/C/D** saved.
- [ ] `Shift Group` column is a single-select GLOBAL Choice, not local; No default.
- [ ] `Employee Code` text, max 20, business required; `Job Title` text, max 100, business required.
- [ ] `Active` / `Is Synthetic` are Yes/No Booleans with Yes defaults.
- [ ] `Department` lookup targets `DC Department`, and `Campus` lookup targets `DC Campus`.
- [ ] `Manager` lookup targets **DC Employee Profile** (itself) and is Optional.
- [ ] Exactly **20 unique Employee Codes** after refresh; each has a matching department and campus.
- [ ] Sophia Carter has blank Manager; every other employee has the intended Manager.
- [ ] No self-management and no manager cycles; no orphan or duplicate department/campus lookup.
- [ ] Do not claim this creates actual Entra users, approvals, or row-level permission boundaries.
- [ ] Screenshots collected: Choice settings, table columns, all three lookup definitions, employee grid, manager example and post-refresh result.

**Minimal negative tests (one at a time):**

1. Try a new profile without Employee Code; confirm validation, then cancel/discard it.
2. Try setting Manager of a profile to itself; if platform permits it, cancel/discard and record that an application-level validation rule is required later.
3. Confirm real university staff do **not** appear in the fictional Employee lookup; if they do, check the selected related table.
4. Confirm a Department lookup selection displays the friendly department primary name and not a pasted GUID.

## K. Troubleshooting table

| Symptom | What to inspect | Safe resolution |
|---|---|---|
| Global `DC Shift Group` absent from picker | Global Choice saved in solution? correct environment/publisher? | Reopen global choice and refresh picker; do not create a second local choice |
| Relationship created duplicate `Department` columns | Was a relationship AND separate lookup field created? | Stop; inspect both relationships before deleting anything |
| Manager relationship refuses to save | Related table selected as self? cascade restrictions? | Screenshot error; choose supported referential behavior if available; do not replace with plain text |
| `Pacific Resilience Campus` not found | Campus row persisted? target table `DC Campus`? | Verify saved campus record and lookup view |
| `Sophia Carter` not visible for manager | Director row saved? lookup targets employee table? | Reopen saved director record, refresh picker |
| Employee Code required error | Field has Business required; code blank or invalid | Enter exact `EMP-000001` format; verify max length |
| Row not visible after save | Wrong environment, unsaved grid, view filter, or permission | Reopen table, refresh, inspect errors before creating duplicates |
| Name in roster mismatches older CSV | Older autogenerated employee assignments were corrected | Use this v4.2 guide and canonical corrected CSV; not the prior uncorrected employee CSV |

---

## L. Narration capture — two final master videos

**Twinkle (build, click by click):** “Open the DC360 solution, select New → Choice, and create DC Shift Group as a global single-select taxonomy. Enter A, B, C, and D. Save it before creating the employee Shift Group column. Then create the DC Employee Profile table, configure its Employee Name primary field, and add Employee Code and Job Title with explicit lengths and required settings. We are not using Microsoft 365 Person fields because these are fictional personas rather than authenticated school users.”

**Celestyn (verification and troubleshooting):** “Reopen the Choice and the Columns page; confirm the saved employee Choice references the shared global Choice. Inspect Department and Campus lookup targets, then create the Manager self-reference. Save the director with no manager. Confirm the row persists after refresh; create the rest of the employee records and test the actual lookup resolution. Our acceptance condition is not merely that the editor displayed 20 names, but that all 20 records remain and their relationships resolve after reload.”

**Arka & Veda (architecture):** “The employee directory is an organization-owned business master, separate from Microsoft Entra users and separate from Dataverse security-role assignments. N:1 lookups enforce references to department and campus records; a self-reference supports managerial hierarchy. Approval authority will be controlled independently by an approval matrix, so a person's line manager is not automatically entitled to approve every category of data center work. Global shift labels avoid drift between employees and roster data, while actual shift schedules, on-call responsibilities and identity-based authorization remain separate.”

### Progress record to fill after completion

| Evidence | Result |
|---|---|
| Actual publisher prefix and employee table schema | ______ |
| Global DC Shift Group unique name / option count | ______ |
| Department lookup logical name / relationship name | ______ |
| Campus lookup logical name / relationship name | ______ |
| Manager self-lookup logical name / behavior | ______ |
| 20 employees persisted after refresh | PASS / FAIL / NOT TESTED |
| Manager chain check | PASS / FAIL / NOT TESTED |
| Screenshots stored privately (with school identifiers hidden) | ______ |
| Errors and fixes, including actual text | ______ |

**STOP HERE.** Next build session will be **S01.07 — DC Asset**, after employee directory relationships and the canonical 20-person roster pass verification.

### Official reference docs (for current portal behavior)
- https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entities-portal
- https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-field-portal
- https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-1n-relationships-portal
- https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-entity-lookup
