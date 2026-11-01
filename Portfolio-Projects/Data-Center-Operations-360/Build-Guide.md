# Data Center Operations 360 — Complete Build Guide

*A practical Microsoft Power Platform learning project using a fictional data center.*

**Project:** SunnyVerse Renewable Group — Data Center Operations 360  
**Scenario:** Pacific Resilience Campus  
**Data:** Entirely fictional  
**Current published chapters:** S00 — Foundation; S01.01–S01.03 — Department Master

[Project home](./README.md) · [Sample data directory](./data/README.md)

---

## Before you begin

This guide takes you through the actual maker interface. Follow each numbered action, save the result, and use the verification checks. Some screens differ across Power Apps releases and tenant configurations; use the equivalent menu label when necessary.

### Prerequisites

1. Sign in to [Power Apps](https://make.powerapps.com) with an account authorized to develop in the selected environment.
2. Confirm the environment permits creating **Solutions** and **Dataverse tables**.
3. Use a dedicated learning environment when possible. Do not alter shared applications or business data.
4. Keep screenshots free of actual account names, email addresses, tenant identifiers, connection IDs, and secrets.

**Important:** GitHub hosts this guide and the sample files. The actual Canvas Apps, model-driven apps, Dataverse tables, and cloud flows are created and run in Microsoft Power Platform.

### If you are restarting an earlier practice exercise

A clean start should only affect **your own disposable practice components**. First review what is in the environment. Removing an unmanaged solution is not necessarily the same as deleting the underlying components and their data. Do not remove a component that another app or flow uses. Export a copy if you might need it later, and follow your organization's deletion policy. This guide does not require deleting or editing other course solutions.

---

## S00 — Foundation

### S00.01 — Select your learning environment

1. Open [make.powerapps.com](https://make.powerapps.com).
2. Sign in using your permitted Microsoft account.
3. In the top-right **Environment** selector, select the environment in which you are authorized to create custom components.
4. In the left navigation, select **Solutions**. If the entry is hidden, open **More** and select **Solutions**.
5. Confirm you can see the list of solutions.

**Verify:** The environment shown in the top-right selector is the intended learning environment. Do not copy its tenant or environment identifier into your public notes.

### S00.02 — Create a solution publisher

A publisher assigns a customization prefix to the components we create. It allows custom tables and columns to be distinguished from Microsoft-managed objects.

1. In **Solutions**, select **New solution**.
2. Locate **Publisher**, then choose **New publisher**. If a publisher with the specified name was created for this same exercise earlier, select it instead of adding a duplicate.
3. Enter the following values:

| Property | Value |
| --- | --- |
| Display name | `SunnyVerse Renewable Learning Publisher` |
| Name | `SunnyVerseRenewableLearningPublisher` |
| Prefix | `svrg` |
| Description | `Publisher for fictional SunnyVerse Renewable Group learning solutions.` |
| Choice value prefix | Keep the automatically generated numeric value |

4. Save the publisher.
5. In the solution form, select **SunnyVerse Renewable Learning Publisher** as the publisher.

**Verify:** The publisher appears in the selector. Inspect the actual prefix saved by the environment; future logical names must use that actual value, not an assumed value.

**Troubleshooting:** If the maker portal prevents publisher creation, use only an existing publisher that you are authorized to use, and note the actual prefix before adding columns. Do not override organization policy.

### S00.03 — Create the solution

1. With the **New solution** form open, enter:

| Property | Value |
| --- | --- |
| Display name | `SunnyVerse Data Center Operations 360` |
| Name / unique name | `SunnyVerseDataCenterOperations360` |
| Publisher | `SunnyVerse Renewable Learning Publisher` |
| Version | `1.0.0.0` |
| Description | `Educational Power Platform solution for fictional data center operations.` |

2. Review the values; the unique name is an important permanent identifier.
3. Select **Create** or **Save**, depending on the interface.
4. Open the newly created solution.

**Verify:** The solution opens and its object list is initially empty. Inspect the publisher, version, and whether the solution is **Unmanaged** where shown.

**Troubleshooting:** If a solution with this exact unique name already exists in the environment, open it rather than creating a duplicate. If the publisher differs from the table design, resolve the discrepancy before adding custom components.

---

## S01 — Organization and reference data

### S01.01 — Create the DC Department table

This table stores shared department names for the fictional campus. It will later support employee and work assignments.

1. Open **Solutions → SunnyVerse Data Center Operations 360**.
2. Select **New → Table**. Open the advanced-properties form if offered.
3. Configure the table:

| Property | Value |
| --- | --- |
| Display name | `DC Department` |
| Plural display name | `DC Departments` |
| Description | `Master list of fictional data center operating departments used for assignments and reporting.` |
| Primary name column | `Department Name` |
| Type | `Standard` |
| Record ownership | `Organization` |

4. Inspect the generated **Schema name / Logical name** and confirm the publisher prefix is the one you selected. Do not manually invent the final schema name.
5. Select **Create**.
6. Reopen the table overview and confirm **Primary column = Department Name** and **Type = Standard**. Inspect the actual ownership setting.

**Why organization ownership?** Departments are shared reference information rather than personal records. Choose ownership before creating the table because it is not freely changeable afterward.

### S01.02 — Add the Department columns

Open **DC Department → Schema → Columns → New column** for each column below. After configuring a column, select **Done** and **Save table** when prompted. Reopen **Columns** to confirm it was saved.

#### Column A — Department Code

| Property | Value |
| --- | --- |
| Display name | `Department Code` |
| Description | `Stable fictional department identifier used for matching sample data.` |
| Data type | `Single line of text` / `Text` |
| Format | `Text` |
| Behavior | `Simple` |
| Required | `Business required` |
| Searchable | `Yes` |
| Maximum character count | `20` |
| Default | None |

Inspect the generated logical name. Example business code: `DC-OPS`. Making a column required does **not** make its values unique; uniqueness can be enforced later with an alternate key after checking the data.

#### Column B — Operational Area

| Property | Value |
| --- | --- |
| Display name | `Operational Area` |
| Description | `Functional group used to organize departments in reports.` |
| Data type | `Single line of text` / `Text` |
| Format | `Text` |
| Behavior | `Simple` |
| Required | `Optional` |
| Searchable | `Yes` |
| Maximum character count | `100` |
| Default | None |

#### Column C — Active

| Property | Value |
| --- | --- |
| Display name | `Active` |
| Description | `Indicates whether this fictional department is available for operational use.` |
| Data type | `Yes/No` |
| Labels | `Yes` / `No` |
| Default value | `Yes` |
| Required | `Optional`, if editable |
| Searchable | `No`, if available |
| Behavior | Simple / default behavior |

This **Active** field is a custom Yes/No column; it is not the Dataverse system Status field. Do **not** create a separate `Routing Enabled` field.

**Verify:** In **Columns**, confirm that Department Code, Operational Area, and Active are present with the correct types. Dataverse also creates system columns automatically, including the record's primary ID (GUID). Do not delete or edit the GUID column.

### S01.03 — Enter six fictional departments

Use **[departments.csv](./data/departments.csv)** as the source of truth.

1. Open **DC Department → columns and data**.
2. Select **Edit** to enter the grid editor, or use **New row**, depending on the interface.
3. Show the columns **Department Name**, **Department Code**, **Operational Area**, and **Active**. If needed, use the column picker.
4. Add the following six rows, entering **Yes** for Active:

| Department Name | Department Code | Operational Area | Active |
| --- | --- | --- | --- |
| Data Center Operations | `DC-OPS` | Campus Operations | Yes |
| Electrical Operations | `DC-ELEC` | Electrical | Yes |
| Mechanical & Cooling | `DC-MECH` | Mechanical | Yes |
| Facilities Maintenance | `DC-FAC` | Facilities | Yes |
| Safety & Compliance | `DC-SAFE` | Safety | Yes |
| IT Infrastructure | `DC-IT` | IT Infrastructure | Yes |

5. Save the rows using the available save control.
6. Leave the data view, reopen it or select **Refresh**.
7. Confirm that all six distinct Department Codes remain, each has the intended name and area, and all are Active = Yes.

**Expected result:** Six stored department records, each with a Dataverse-generated primary GUID.

**If records disappear:** Check for save errors, active filters, the selected environment, and data permissions before recreating rows.

**If a duplicate code is present:** Correct the incorrect record rather than blindly importing another row.

### Chapter completion check

- [ ] Correct solution and publisher are visible.
- [ ] `DC Department` is a Standard table with primary name `Department Name`.
- [ ] Department Code, Operational Area, and Active have the specified types.
- [ ] The six sample rows match [departments.csv](./data/departments.csv).
- [ ] All six rows remain after refresh, with no duplicate Department Codes.

**Stop here at the end of the published lesson.** Subsequent learning steps will continue in this same Build Guide. The [campus](./data/campuses.csv) and [data-hall](./data/data-halls.csv) files are already provided as preview datasets; do not create their tables until their detailed instructions are published.

---

## Reference materials

- [Microsoft Learn — Create and edit tables](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entities-portal)
- [Microsoft Learn — Create and edit columns](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-field-portal)
- [Microsoft Learn — Solutions](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/solutions-overview)

This guide uses fictional data for education. Follow the permissions and licensing requirements of your own environment.
