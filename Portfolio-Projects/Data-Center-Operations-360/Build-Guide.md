# Data Center Operations 360 — Build-Along Guide

**SunnyVerse AI Labs | Independent Power Platform learning project**  
**Fictional organization:** SunnyVerse Renewable Group  
**Published:** Parts 00–02 — Solution Foundation, Department Master, Campus and Data Halls

[Project home](./README.md) · [Practice data](./data/README.md)

Welcome to Data Center Operations 360. In this project, you will build a fictional data center operations solution using Microsoft Power Platform. The work is completed in an environment where you have permission to develop, and all practice records are fictional.

Part 00 prepares the solution. Part 01 creates operating departments, and Part 02 adds a fictional campus with two related data halls. Work through the published lessons in order using your own authorized learning environment.

Follow the activities in order. The menu labels in your environment may differ slightly; choose the equivalent command and inspect the actual settings before saving.

## S00.01 — Open Power Apps and select a learning environment

Open [make.powerapps.com](https://make.powerapps.com) and sign in using a Microsoft work or school account that you are allowed to use for development.

At the top of the maker portal, open **Environment**. Select an environment approved for your learning work. If you only see an institution-wide environment or you are not sure whether you can create objects there, confirm permission before continuing.

From the left navigation, choose **Solutions**. If it is not visible, open **More → Solutions**. The Solutions page should display the **New solution** command.

Before creating anything, search for `SunnyVerse Data Center Operations 360`. If a solution with that exact name already exists in the selected environment, inspect it and resolve the conflict in an authorized way; do not delete unrelated objects or create a similarly named duplicate.

## S00.02 — Create the custom publisher

A publisher supplies the customization prefix that becomes part of the technical names of Dataverse components. Creating it first helps keep the solution consistent.

From **Solutions**, select **New solution**. Find the **Publisher** field and choose **New publisher**. Enter these values:

| Publisher property | Value |
| --- | --- |
| Display name | `SunnyVerse Renewable Learning Publisher` |
| Name | `SunnyVerseRenewableLearningPublisher` |
| Description | Publisher for the fictional SunnyVerse Renewable Group educational solution. |
| Customization prefix | `svrg` |
| Choice value prefix | Keep the system-generated numeric value |

Inspect the publisher **Name** and customization prefix. If the portal generates the unique name automatically, use the displayed value only after confirming it. Select **Save**, return to the New solution form, and select **SunnyVerse Renewable Learning Publisher** from the publisher picker.

You should now see the saved publisher selected in the solution form. If your environment does not permit publisher creation, use only a publisher approved for that environment and note its **actual** customization prefix. Do not assume that the prefix will always be `svrg`.

## S00.03 — Create the solution

The publisher is selected; next, fill in the remaining fields of **New solution**.

| Solution property | Value |
| --- | --- |
| Display name | `SunnyVerse Data Center Operations 360` |
| Unique name | `SunnyVerseDataCenterOperations360` |
| Publisher | `SunnyVerse Renewable Learning Publisher` |
| Version | `1.0.0.0` |
| Description | Fictional data center operations learning solution built with Microsoft Power Platform. |

Review the unique name and publisher before saving. Select **Create** or **Save**, depending on the command shown.

Return to **Solutions** and open **SunnyVerse Data Center Operations 360**. Use **Overview** or **Properties**, when available, to inspect the solution's publisher, unique name, version, and managed/unmanaged status. Then open **Objects → All**.

A newly created solution should not yet contain our custom project tables or apps. If unexpected components appear, confirm that you opened the intended solution and environment rather than deleting anything.

## S00.04 — Check access to the Dataverse table designer

Now that the solution is open, locate **New → Table**. Open the table creation experience, but **do not create a table in this lesson**. Close the panel without saving.

This simple test tells you whether the table creation interface is available. It does not establish full Dataverse storage permissions or all app licensing rights. If you see an access or licensing error, record its wording privately and continue only with features your environment allows.

## S00.05 — Test Outlook and Teams notifications (optional)

If your environment permits the required connectors, you can run a small notification test using only your own authorized mailbox and Teams account. This is a connector exercise, not an approval workflow.

Open [make.powerautomate.com](https://make.powerautomate.com) and select the same authorized environment. From **Create**, choose **Instant cloud flow** (or **My flows → New flow → Instant cloud flow**). Name the flow `DC00_Connector_Readiness_Test`, choose **Manually trigger a flow**, and select **Create**.

Below the manual trigger, add **Office 365 Outlook → Send an email (V2)**. Configure the action:

| Email field | Value |
| --- | --- |
| To | Your own authorized test mailbox |
| Subject | `[TEST] DC360 — Outlook connector` |
| Body | `This is a fictional Power Platform learning project notification test.` |

To test Teams independently, select the **+** below the manual trigger and choose **Add a parallel branch**, if offered by your designer. In the new branch, choose **Microsoft Teams → Post a message to myself**. Set **Content type** to **Text** if the field appears, and enter this content:

```text
[TEST] DC360 — Teams connector
```

Select **Save → Test → Manually → Run flow**. Open the run history and inspect the Outlook and Teams actions separately. Then check your email inbox and your Teams Notes/self-chat to confirm delivery. If the designer does not offer parallel branches, use two small, separately triggered test flows.

A successful self-notification means that particular action worked for your signed-in account. It does not prove that you can send to other users, post to organization channels, or enforce separate approver identities. If an action fails, read the connection or policy error rather than attempting to bypass restrictions.

## Finish Part 00

Return to the Power Apps solution. Make sure it opens with the expected publisher, unique name, and version. You should also know whether the Dataverse table designer opened successfully and, if you ran the optional test, whether the Outlook and Teams messages arrived.

**You are ready for the next lesson when the solution is saved and can be reopened.** No Dataverse business tables or sample records are needed yet.

Keep institution-specific account details, environment IDs, connection strings, credentials, and screenshots containing private information out of public repositories.

---

## Part 01 — Create the Department Master in Dataverse

In Part 00, you prepared a solution to hold the application's components. Now we'll create its first table. In our fictional data center, engineering and operations staff belong to departments. Those departments need consistent names and codes so that future applications can reference them reliably.

By the end of this lesson, your solution will contain a **DC Department** table and six fictional department records. Keep the [department practice dataset](./data/departments.csv) open as you work; it is the source of the values used in this lesson.

### S01.01 — Create the DC Department table

Open [Power Apps](https://make.powerapps.com), select the environment you used in Part 00, and go to **Solutions → SunnyVerse Data Center Operations 360**. On the solution's **Objects** page, select **New → Table**. If the table designer opens a quick-create experience, choose **Set advanced properties**, **Table (advanced properties)**, or the corresponding option that exposes the primary name and ownership settings.

Enter these properties before you create the table:

| Table property | Value |
| --- | --- |
| Display name | `DC Department` |
| Plural display name | `DC Departments` |
| Description | `Fictional data center operating departments used for staff assignments and reporting.` |
| Primary name column | `Department Name` |
| Type | `Standard` |
| Record ownership | `Organization` |
| Schema / logical name | Check the automatically generated name and the actual publisher prefix |

**Choose Organization ownership before saving.** Departments are common reference records rather than tasks assigned to individual users; Dataverse does not let you change the table's ownership type later. Confirm that the primary name column reads **Department Name** rather than a default label.

Select **Create**. Open the newly created table and look at its **Table properties** card. You should see **DC Department**, **Department Name**, and **Standard**. Open **Properties** to inspect the ownership and generated technical name.

You may also see a system-generated `DC Department` identifier containing a GUID. This is the table's primary key. Leave it in place; it is not an extra column you need to fill manually.

### S01.02 — Add the three department columns

In the **DC Department** table, select **Schema → Columns → New column**. We will add **Department Code**, **Operational Area**, and **Active**, one at a time.

For each column, enter the following settings in the column properties panel. Select **Done** after finishing a column. Once all three are configured, select **Save table** if the designer displays that command; **Done** alone may not save the changes to Dataverse.

| Property | Department Code | Operational Area | Active |
| --- | --- | --- | --- |
| Display name | `Department Code` | `Operational Area` | `Active` |
| Description | `Stable fictional department identifier, such as DC-OPS.` | `Operational reporting group for this department.` | `Whether this department is available for assignments.` |
| Data type | Text / Single line of text | Text / Single line of text | Yes/No |
| Format | Text | Text | Yes/No labels: `Yes` and `No` |
| Behavior | Simple, if shown | Simple, if shown | Default / Simple, if shown |
| Required | Business required | Optional | Optional |
| Searchable | Yes | Yes | No, if offered |
| Maximum length | 20 characters | 100 characters | Not applicable |
| Default value | None | None | Yes |
| Choice scope | Not applicable | Not applicable | Yes/No Boolean; **not** a new local or global Choice |
| Schema name | Keep the actual publisher-generated name | Keep the actual publisher-generated name | Keep the actual publisher-generated name |

To create **Department Code**, choose **Text**, confirm the format is **Text**, set **Required** to **Business required**, turn **Searchable** on, and set the maximum character count to **20**. Enter its description, check the generated technical name, and select **Done**.

Repeat for **Operational Area**, using Text with maximum length **100**, **Required = Optional**, and **Searchable = Yes**. Leave the default blank.

For **Active**, choose **Yes/No**, use **Yes** and **No** as the labels, and set the default to **Yes**. Select **Required = Optional** and **Searchable = No** when these settings are available. This is a Boolean field; you do **not** need to create a separate reusable Choice component.

Save the table changes. Open **Schema → Columns** again and confirm that all three custom columns are present. The actual technical names may differ if your publisher uses a prefix other than `svrg`, so use the names shown in your environment.

**A design note:** Making Department Code business required helps prevent blank values in standard app forms, but does not automatically prevent duplicates. We will address enforced business-code uniqueness when the project introduces keys.

### S01.03 — Enter six fictional departments

Return to the **DC Department** overview. Find **DC Department columns and data** and select **Edit** to open the editable grid. If the columns you need are hidden, open the column picker (for example, **+ more**) and show **Department Name**, **Department Code**, **Operational Area**, and **Active**.

Enter the six records from [departments.csv](./data/departments.csv):

| Department Name | Department Code | Operational Area | Active |
| --- | --- | --- | --- |
| Data Center Operations | `DC-OPS` | Campus Operations | Yes |
| Electrical Operations | `DC-ELEC` | Electrical | Yes |
| Mechanical & Cooling | `DC-MECH` | Mechanical | Yes |
| Facilities Maintenance | `DC-FAC` | Facilities | Yes |
| Safety & Compliance | `DC-SAFE` | Safety | Yes |
| IT Infrastructure | `DC-IT` | IT Infrastructure | Yes |

Select a blank row and enter the first department. For **Active**, leave the Yes/No control set to **Yes**. Complete the other five rows using the same method. **Do not enter anything in the system-generated GUID/primary-key column.**

Save changes using the command available in your table editor. Leave the grid, reopen **DC Department**, and select **Refresh** if necessary. The table should display all six saved records with their distinct codes and Active = Yes.

If a row is missing, check whether the grid was saved and whether a filter hides it before creating another copy. If you see a required-field error, inspect **Department Code** for a blank value. If the column names don't match, check that you're editing the correct table inside the correct solution.

### Finish Part 01

Your **DC Department** table should now contain six records, each with a department name, a distinct business code, an operational area, and an Active flag. Confirm that the six rows remain visible after reopening the table. Keep the automatically generated record IDs unchanged.

You have completed the first reference-data table. **No other tables are required for this lesson.**


---

## Part 02 — Build the Campus and Data Hall registers

In Part 01 you created the operating departments. Next, you'll add the location structure for our fictional data center. **Pacific Resilience Campus** contains two data halls, and each hall belongs to exactly one campus. We'll model that connection with a Dataverse lookup rather than typing the campus name into an ordinary text column.

This lesson creates two tables, one reusable Choice and three practice records. You can type the records directly or use the matching [campus CSV](./data/campuses.csv) and [data hall CSV](./data/data-halls.csv). The tables must exist before you import their data.

Our publisher customization prefix is **`svrg`**. The technical names shown below are the intended *schema names*, while CSV headers use the exact *display names* shown in the table designer. Dataverse import attempts to match display-name headers automatically; you still need to review Choice and lookup mapping. If your designer generates a different name, verify and correct it **before** creating the component, where editable. Do not rename an already saved component just to match a sample.

### S02.01 — Create the DC Campus table

Open [Power Apps](https://make.powerapps.com), choose the environment used in Part 01 and go to **Solutions → SunnyVerse Data Center Operations 360 → New → Table**. Select advanced table properties if the designer offers that option.

| Table property | Enter |
| --- | --- |
| Display name | `DC Campus` |
| Plural display name | `DC Campuses` |
| Description | `Fictional campus register for data center locations and reporting.` |
| Primary name column | `Campus Name` |
| Type | Standard |
| Record ownership | **Organization** |
| Intended table schema name | `svrg_DCCampus` |
| Intended primary-name schema | `svrg_CampusName` |

Keep **Organization** ownership because the campus is shared reference data. Ownership is difficult to change after creation. Inspect the generated schema names and select **Create**. The table should appear inside the same solution.

Now open **DC Campus → Schema → Columns → New column** and add the four business columns, one at a time. Enter each description, type, format and required setting. When available, inspect **Advanced options → Name** for the exact `svrg_`-prefixed schema name.

| Column (CSV header) | Intended schema name | Data type / format | Other settings |
| --- | --- | --- | --- |
| `Campus Code` | `svrg_CampusCode` | Text / single line; format Text | Business required; maximum 20 characters; Searchable Yes; no default |
| `Region` | `svrg_Region` | Text / single line; format Text | Optional; maximum 100 characters; Searchable Yes; no default |
| `Time Zone` | `svrg_TimeZone` | Text / single line; format Text | Optional; maximum 100 characters; Searchable Yes; no default |
| `Active` | `svrg_Active` | Yes/No | Labels Yes / No; default **Yes**; Optional; Searchable No if available |

Use these column descriptions, respectively: `Stable fictional campus identifier.`; `Geographical operating region.`; `IANA time zone used for campus reporting.`; and `Indicates whether the campus is available for operational use.`

`Active` is a **Yes/No** field, *not* a local or global Choice. Set column Behavior to **Simple** where the property applies. Select **Done** for each column and **Save table** if required. Reopen **Columns** to confirm the names, data types and generated schema names.

### S02.02 — Add Pacific Resilience Campus

Open **DC Campus columns and data → Edit** (or the table's editable data grid). Show the five columns used in [campuses.csv](./data/campuses.csv), and enter this row:

| Campus Name | Campus Code | Region | Time Zone | Active |
| --- | --- | --- | --- | --- |
| Pacific Resilience Campus | `DC-PAC-01` | Pacific | `America/Los_Angeles` | Yes |

Save the row, leave the grid, and reopen it. Confirm that one campus record appears. Leave the automatically generated Dataverse record ID untouched.

If you prefer an import, the CSV has **exactly the five display-name column headers** above. On a supported table data-import screen, choose the CSV file, review its field mappings and import it. **Choose either direct entry or CSV import—not both**, or you may create duplicate records. We'll use this saved campus as the parent for the halls.

### S02.03 — Create the reusable infrastructure Criticality Choice

A data hall can have one of three criticality classifications. Because other infrastructure records may use the same classification, we'll define the options **once** in a Global Choice.

Return to the solution's object list and select **New → Choice**.

| Choice property | Enter |
| --- | --- |
| Display name | `DC Infrastructure Criticality` |
| Intended unique name | `svrg_DCInfrastructureCriticality` |
| Scope | **Global Choice** (solution component) |
| Description | `Shared fictional infrastructure criticality classification for data halls and assets.` |
| Choice option 1 | High |
| Choice option 2 | Medium |
| Choice option 3 | Low |
| Numeric option values | Keep Dataverse-generated numbers |
| Column selection style | Single-select, configured when we create the Criticality column |
| Column default | No default; the learner selects a value |

If an initial option already appears, replace its label with **High**. Use **New choice** to add **Medium** and **Low** in that order. Open **Advanced options** and check the actual `svrg_`-prefixed **Name**. Save the Choice.

The Global Choice holds the shared option list. It is not itself the field in a data hall row; we'll connect a **Criticality** column to it in the next steps.

### S02.04 — Create the DC Data Hall table

Inside the same solution, select **New → Table** and enter:

| Table property | Enter |
| --- | --- |
| Display name | `DC Data Hall` |
| Plural display name | `DC Data Halls` |
| Description | `Fictional data halls belonging to a campus, with designed IT power capacity.` |
| Primary name column | `Hall Name` |
| Type | Standard |
| Record ownership | **Organization** |
| Intended table schema name | `svrg_DCDataHall` |
| Intended primary-name schema | `svrg_HallName` |

Review the primary-name column, ownership and generated names before selecting **Create**.

### S02.05 — Configure the Data Hall columns

Open **DC Data Hall → Schema → Columns → New column**. Configure each column using this table and select **Done** after each. Save the table when prompted.

| Column (CSV header) | Intended schema name | Data type / format | Other settings |
| --- | --- | --- | --- |
| `Hall Code` | `svrg_HallCode` | Text / single line; format Text | Business required; maximum 30 characters; Searchable Yes; no default |
| `Criticality` | `svrg_Criticality` | **Choice (single-select)**, synced with existing **Global Choice** `DC Infrastructure Criticality` | Required **Business required**; Searchable Yes; options High / Medium / Low; **no default** |
| `Design IT Capacity kW` | `svrg_DesignITCapacitykW` | Decimal number; **2 decimal places** | Business required; minimum **0**; maximum **100000** if the editor permits; no default |
| `Active` | `svrg_Active` | Yes/No | Labels Yes / No; default **Yes**; Optional; Searchable No if available |

Use these descriptions, respectively: `Stable fictional identifier for this data hall.`; `Shared classification of the data hall's infrastructure criticality.`; `Designed IT power capacity in kilowatts, not live power consumption.`; and `Whether this data hall is available for operational use.`

For **Criticality**, choose data type **Choice**, not **Choices / Multi Select Choice**. Where the editor displays **Sync with global choice?**, choose **Yes**, then select **DC Infrastructure Criticality**. Verify all three labels and leave the column default blank. This is a *table column backed by a Global Choice*, not an independently edited Local Choice.

For **Design IT Capacity kW**, use **Decimal number**, set **2 decimal places**, and choose minimum **0**. If the maximum entry is available, use **100000**. Use Behavior **Simple**, rather than calculated or rollup, wherever applicable.

Save the table after adding the columns.

### S02.06 — Create the Campus lookup relationship

Each data hall needs to point to an existing campus record. We'll add the lookup by creating one **many-to-one relationship**.

Open **DC Data Hall → Schema → Relationships → New relationship → Many-to-one**.

Choose **Related table = DC Campus**. The **current table must be DC Data Hall**, because the lookup belongs on each hall record.

| Relationship property | Enter |
| --- | --- |
| Relationship | **Many DC Data Hall records → one DC Campus record (N:1)** |
| Lookup column display name | `Campus` |
| Intended lookup column name | `svrg_Campus` |
| Description | `Parent campus for this data hall.` |
| Lookup requirement | **Business required** |
| Searchable | Yes |
| Intended relationship name, if editable | `svrg_DCDataHall_DCCampus` |
| Delete behavior, if configurable | **Restrict** deletion of a campus that has halls |

Select **Done** and **Save table**. Then open **DC Data Hall → Schema → Columns** and confirm that exactly **one** column named **Campus** has type **Lookup** and points to **DC Campus**.

Do **not** create another Lookup column or a free-text Campus column. Dataverse already created the lookup as part of this relationship. The selected campus row is stored through its Dataverse identifier; do not enter or copy a GUID yourself.

### S02.07 — Add the two data halls

Open **DC Data Hall columns and data → Edit**. Display **Hall Name**, **Hall Code**, **Campus**, **Criticality**, **Design IT Capacity kW** and **Active**.

Use the **Campus** lookup picker to select the existing **Pacific Resilience Campus** record for *both* data halls. For **Criticality**, select **High**.

| Hall Name | Hall Code | Campus | Criticality | Design IT Capacity kW | Active |
| --- | --- | --- | --- | ---: | --- |
| Data Hall 01 | `DC-PAC-01-H01` | Pacific Resilience Campus | High | 2350.00 | Yes |
| Data Hall 02 | `DC-PAC-01-H02` | Pacific Resilience Campus | High | 2500.00 | Yes |

Save the two rows. Leave and reopen the data grid. Both hall records should still show **High**, their respective designed capacities, and the **same existing campus** in the lookup field. The campus table should still have one record.

#### Optional CSV import

The companion [data-halls.csv](./data/data-halls.csv) uses the **exact six display-name headers** shown above. If you prefer importing it instead of entering the two rows manually, import **campuses.csv first**, so the referenced campus already exists.

In a supported Dataverse import experience, choose the appropriate table, upload the CSV, select **Review Mapping**, and confirm all six headers map to their intended columns. For **Criticality**, confirm that source label **High** maps to the existing **High** option; do not create a new option. For **Campus**, open the **Lookup Reference** mapping and select the **DC Campus** table, matching **Campus Name** to `Pacific Resilience Campus`. Complete the import only after those mappings are valid. Check the import results and reopen the two hall records.

Matching CSV column headers to display names helps the importer find fields, but **does not by itself guarantee Choice or lookup values resolve**. Do not import a file after entering the same records manually.

### Finish Part 02

You should now have one **DC Campus** record, two **DC Data Hall** records, and one shared **DC Infrastructure Criticality** Choice. Both halls must resolve through the **Campus** lookup to Pacific Resilience Campus. Reopen the tables and check that all three records are saved with the expected values.

The design now represents a genuine parent/child relationship without duplicating campus details in each hall. No employee, asset or monitoring records are needed for this lesson.

## Microsoft Learn references

- [Create a Power Platform solution](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-solution)
- [Create and edit Dataverse tables](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entities-portal)
- [Create and edit Dataverse columns](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-field-portal)
- [Dataverse table types and ownership](https://learn.microsoft.com/en-us/powerapps/maker/data-platform/types-of-entities)
- [Create global choices](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/custom-picklists)
- [Create and edit one-to-many / many-to-one relationships](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-1n-relationships-portal)
- [Import data and map choices/lookups](https://learn.microsoft.com/en-us/power-apps/user/import-data)

*All organizations, facilities, staff, and operational scenarios in this learning project are fictional. Do not use this guide to control live data center infrastructure.*
