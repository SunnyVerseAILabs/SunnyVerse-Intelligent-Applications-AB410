# Data Center Operations 360 — Step-by-Step Build Guide

**An independent Microsoft Power Platform learning project by SunnyVerse AI Labs**  
**Fictional organization:** SunnyVerse Renewable Group  
**Fictional location:** Pacific Resilience Campus  
**Published lesson:** Part 01 — Foundation and Department Master  
**Last updated:** November 1, 2026

[Project home](./README.md) · [Department dataset](./data/departments.csv) · [Dataset instructions](./data/README.md) · [Episode companions](./episode-companions/README.md)

> **Learning use only.** Every company, department, employee, asset and operational record in this project is fictional. This guide does not control or operate real data center equipment. Use an environment and connectors you are authorized to develop in.

## How to follow the project

Complete the numbered actions in order. Each step includes the purpose, exact configuration, a saved-data check and troubleshooting. Do not proceed to the next published part until the completion checks pass. When the Power Apps interface differs, identify the equivalent action and confirm the actual schema name instead of inventing one. Do not publish screenshots containing real user accounts, tenant IDs, environment IDs, connection details or tokens.

**What you will build in this part:** one unmanaged solution and one Dataverse table holding six fictional operating departments. No campus, employee, data-hall, asset, or incident records are required for Part 01.

---

## S00 — Set up the learning environment

### S00.01 — Open the Power Apps maker portal

**Why:** An environment is the workspace in which Power Apps, Dataverse tables and flows are created.

1. In a browser, open https://make.powerapps.com.
2. Sign in with a Microsoft work or school account that is allowed to develop Power Platform components.
3. Find **Environment** near the upper-right corner and select your authorized development environment. Do not use a shared organizational environment without permission.
4. From the left menu, select **Solutions**. If Solutions is hidden, select **More → Solutions**.
5. Confirm that the Solutions list opens.

**Verify:** The selected environment is the one intended for this exercise and the **New solution** command is available.

**Troubleshoot:** If Solutions is missing, verify that the correct account and environment are selected. An administrator may restrict maker permissions. Do not attempt to bypass access restrictions.

### S00.02 — Create a custom solution publisher

**Why:** A publisher assigns the customization prefix used by components created in the solution. The exact logical names matter later in Power Fx, relationships and integrations.

1. In **Solutions**, select **New solution**.
2. Find **Publisher** and select **New publisher**.
3. Enter the values below. Keep automatically generated numeric option values rather than guessing them.

| Property | Enter |
| --- | --- |
| Display name | SunnyVerse Renewable Learning Publisher |
| Name | SunnyVerseRenewableLearningPublisher |
| Description | Publisher for fictional SunnyVerse Renewable Group learning solutions. |
| Prefix | svrg |
| Choice value prefix | Keep the automatically generated value |

4. Select **Save**.
5. Back in the New solution panel, select **SunnyVerse Renewable Learning Publisher**.
6. Confirm that the publisher is selected before continuing.

**Verify:** The saved publisher is present, and its actual customization prefix is **svrg**. Record any different actual prefix and use that value consistently. Do not create a second publisher with a similar name.

**Troubleshoot:** If publisher creation is restricted, use only an existing publisher you have permission to use, and record its actual prefix before creating tables.

### S00.03 — Create the Power Platform solution

**Why:** A solution groups the components of an application so their changes can be managed and exported.

Continue in the **New solution** panel:

| Property | Enter |
| --- | --- |
| Display name | SunnyVerse Data Center Operations 360 |
| Name | SunnyVerseDataCenterOperations360 |
| Publisher | SunnyVerse Renewable Learning Publisher |
| Version | 1.0.0.0 |
| Description | Educational Power Platform solution for fictional data center operations. |

1. Inspect the display name and unique name carefully before saving.
2. Select **Create** or **Save**.
3. Open **SunnyVerse Data Center Operations 360** from the Solutions list.
4. In the solution overview or settings, inspect the publisher and version. Confirm the solution is **Unmanaged** if that information is shown.
5. Open **Objects → All**. A new solution starts without custom objects.

**Verify:** The solution opens and its publisher, version and unique name match the intended configuration.

**Troubleshoot:** If a solution with this name already exists in the same environment, inspect it rather than create a duplicate. The name may be permanently assigned. You may need an authorized new environment for a truly fresh exercise.

### S00.04 — Optional Outlook and Teams connector readiness exercise

**Purpose:** Confirm whether your environment allows an email to your own account and a Teams self-message. These are **not** required to complete the Department Master.

1. Open https://make.powerautomate.com, select the same permitted environment, and choose **Create → Instant cloud flow** (or **My flows → New flow → Instant cloud flow**).
2. Set **Flow name** to **DC00_Connector_Readiness_Test** and select **Manually trigger a flow**.
3. Select **Create**.
4. Add **Office 365 Outlook → Send an email (V2)**. Set **To** to your *own authorized mailbox*, **Subject** to **[TEST] Data Center Operations — Outlook Connector**, and **Body** to **This is a fictional-project connector test.**
5. From the plus (+) immediately below the trigger, choose **Add a parallel branch** if available. In the second branch add **Microsoft Teams → Post a message to myself**.
6. Set **Content type** to **Text** if offered and **Content** to **[TEST] Data Center Operations — Teams connector check.**
7. Select **Save → Test → Manually → Run flow**.
8. Check the run history for each action and confirm delivery in your own Outlook mailbox and Teams Notes/self chat.

**Verify:** Each action succeeds and the corresponding message is received. If either action is blocked, record the outcome and continue with the Department Master; connector availability varies by licensing and administrator policy.

**Important:** A self-notification test does not establish that multi-user approvals or posting to arbitrary Teams channels is authorized.

---

## S01 — Create the organizational master data

### S01.01 — Create the DC Department table

**Why:** An operating department will eventually be referenced by staff profiles, maintenance assignments and workflow-routing rules. Use a proper Dataverse table rather than repeating department names in every transaction.

1. Return to https://make.powerapps.com.
2. Select **Solutions → SunnyVerse Data Center Operations 360**.
3. Select **New → Table**, and open advanced properties if the designer requires it.
4. Configure the table exactly as shown:

| Property | Enter |
| --- | --- |
| Display name | DC Department |
| Plural display name | DC Departments |
| Description | Master list of fictional data center operating departments used for assignments and reporting. |
| Primary name column | Department Name |
| Type | Standard |
| Record ownership | Organization |
| Schema name | Inspect the generated value; it must use your actual publisher prefix |

5. Confirm that the primary column is **Department Name**, not the automatically generated record ID.
6. Review **Record ownership** **before creating the table**. Organization ownership is appropriate for this shared reference table; ownership cannot be changed after the table is created.
7. Select **Create**.
8. Open the new table's **Properties** and confirm its name, primary name, type, ownership and generated schema/logical name.

**Verify:** DC Department appears in the solution under **Tables**. Dataverse creates its own system GUID/primary-key column. Do not delete or edit that column.

### S01.02 — Create the Department Code column

1. Open **DC Department → Schema → Columns → New column**.
2. Enter the following values:

| Property | Enter |
| --- | --- |
| Display name | Department Code |
| Description | Stable fictional identifier for a data center operating department. |
| Data type | Single line of text / Text |
| Format | Text |
| Behavior | Simple, if offered |
| Required | Business required |
| Searchable | Yes |
| Maximum character count | 20 |
| Default value | None |
| Schema name | Use the generated publisher-prefixed name |

3. Select **Done** and then **Save table** if prompted.
4. Return to **Columns** and confirm Department Code appears as a text column.

**Note:** Business required does not guarantee a unique value. A unique alternate key may be introduced in a later lesson after the sample data is checked.

### S01.03 — Create the Operational Area column

1. Open **DC Department → Schema → Columns → New column**.
2. Enter:

| Property | Enter |
| --- | --- |
| Display name | Operational Area |
| Description | Functional grouping of the fictional operating department. |
| Data type | Single line of text / Text |
| Format | Text |
| Behavior | Simple, if offered |
| Required | Optional |
| Searchable | Yes |
| Maximum character count | 100 |
| Default value | None |
| Schema name | Use the generated publisher-prefixed name |

3. Select **Done**, save table changes if prompted, then reopen **Columns** to verify.

### S01.04 — Create the Active column

1. Open **DC Department → Schema → Columns → New column**.
2. Enter:

| Property | Enter |
| --- | --- |
| Display name | Active |
| Description | Indicates whether the fictional department is available for operational assignments. |
| Data type | Yes/No |
| Choice scope | Not applicable — this is a Yes/No column, not a three-option Choice |
| Labels | Yes / No |
| Default value | Yes |
| Required | Optional, if editable |
| Searchable | No, if offered |
| Behavior | Default / Simple if applicable |
| Schema name | Use the generated publisher-prefixed name |

3. Select **Done** and save table changes if prompted.
4. Reopen **Columns** and confirm all three new columns: **Department Code**, **Operational Area**, and **Active**.

**Important:** This Active column is a custom Yes/No business flag. It is not the Dataverse system Status field. Do not add a separate Routing Enabled column.

### S01.05 — Add the six sample departments

Use the linked **[departments.csv](./data/departments.csv)** as the authoritative practice dataset for this lesson. The CSV is supplied in the same GitHub project folder, so you do not need to reconstruct it from screenshots.

1. In the solution, open **Tables → DC Department**.
2. Locate the **DC Department columns and data** section.
3. Select **Edit**, or open the editable data grid using the available action.
4. Ensure the **Department Name**, **Department Code**, **Operational Area** and **Active** columns are visible. Use the columns picker if necessary.
5. Enter the following six fictional rows; leave the system GUID/primary-key column untouched.

| Department Name | Department Code | Operational Area | Active |
| --- | --- | --- | --- |
| Data Center Operations | DC-OPS | Campus Operations | Yes |
| Electrical Operations | DC-ELEC | Electrical | Yes |
| Mechanical & Cooling | DC-MECH | Mechanical | Yes |
| Facilities Maintenance | DC-FAC | Facilities | Yes |
| Safety & Compliance | DC-SAFE | Safety | Yes |
| IT Infrastructure | DC-IT | IT Infrastructure | Yes |

6. Save the changes using the grid's save mechanism, if shown.
7. Close the data grid or navigate back to the table overview. Select **Refresh**, or leave and reopen the table.
8. Confirm that all six distinct Department Code values still exist and each Active value remains **Yes**.

**Verify:** Exactly six records, no duplicate department codes, and the six values match the downloadable CSV.

**Troubleshoot:**
- **Row missing after refresh:** Check save status, grid filters, permissions and selected environment before adding another row.
- **Required error:** Check Department Code, including empty or whitespace-only values.
- **Unexpected extra GUID column:** Keep it; Dataverse uses it for record identity and relationships.
- **Publisher prefix differs:** Record the actual schema name. Do not guess logical names or change existing components casually.

### Part 01 completion checklist

- [ ] Power Apps opens in an authorized learning environment.
- [ ] SunnyVerse Renewable Learning Publisher is saved, or an authorized alternative is documented.
- [ ] SunnyVerse Data Center Operations 360 solution is available and its metadata is checked.
- [ ] DC Department is a Standard, Organization-owned table.
- [ ] Its primary name is Department Name and its system record ID remains untouched.
- [ ] Department Code, Operational Area and Active have the intended types and properties.
- [ ] All six fictional department records match [departments.csv](./data/departments.csv).
- [ ] Save/reopen/refresh confirms six rows remain.
- [ ] Any connector test performed is clearly recorded as passed, failed or not attempted.

**Stop here.** This is the end of Part 01. The next part will be added to this same guide only after its steps and sample data are reviewed and finalized.

---

## Reference documentation

- [Microsoft Learn — Create a solution](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-solution)
- [Microsoft Learn — Create and edit Dataverse tables](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entities-portal)
- [Microsoft Learn — Manage custom columns](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-manage-fields)
- [Microsoft Learn — Table types and ownership](https://learn.microsoft.com/en-us/powerapps/maker/data-platform/types-of-entities)

**All project data is fictional.** Use this material for learning and demonstration, not for controlling real critical infrastructure.
