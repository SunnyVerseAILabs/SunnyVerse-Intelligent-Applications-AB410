# Data Center Operations 360 — Build-Along Guide

**SunnyVerse AI Labs | Independent Power Platform learning project**  
**Fictional organization:** SunnyVerse Renewable Group  
**Published:** Parts 00–03 — Solution Foundation, Department Master, Campus and Data Halls, Employee Directory

[Project home](./README.md) · [Practice data](./data/README.md)

Welcome to Data Center Operations 360. In this project, you will build a fictional data center operations solution using Microsoft Power Platform. The work is completed in an environment where you have permission to develop, and all practice records are fictional.

Part 00 prepares the solution. Part 01 creates departments, Part 02 adds a campus and two related data halls, and Part 03 builds a fictional employee directory with reporting managers. Follow the lessons in order in an authorized learning environment.

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

Our fictional facility, **Pacific Resilience Campus**, contains two data halls. In this lesson, you'll create a campus register, a shared criticality classification, and a data hall register. Each hall will point to its campus through a real Dataverse lookup, so the campus details are kept in one place.

The practice files are [campuses.csv](./data/campuses.csv) and [data-halls.csv](./data/data-halls.csv). Their **first-row headers exactly match the Dataverse column display names** in this lesson. The corresponding technical names use the confirmed `svrg` publisher prefix. These are two different naming conventions: for example, the display name `Campus Code` is the CSV header, while `svrg_CampusCode` is its Dataverse schema name. Matching headers helps the importer map columns, but choices and lookups still require value mapping.

### S02.01 — Create the campus table

Open [Power Apps](https://make.powerapps.com), select your learning environment, then open **Solutions → SunnyVerse Data Center Operations 360**. Choose **New → Table**, opening advanced table properties when needed. Enter:

| Property | Value |
| --- | --- |
| Display name / plural | `DC Campus` / `DC Campuses` |
| Description | `Fictional campus register for data center operations.` |
| Primary name column | `Campus Name` |
| Primary column description | `Name of the fictional data center campus.` |
| Type / record ownership | Standard / **Organization** |
| Table schema name (target) | `svrg_DCCampus` |
| Primary name schema (target) | `svrg_CampusName` |

Choose **Organization** ownership before creating the table, since campus records are shared reference data. Confirm the primary name field is **Campus Name**, review generated schema names using **Advanced** or **Properties**, and select **Create**.

Open **DC Campus → Schema → Columns → New column** and create the four additional columns using the settings below. **Campus Name** is the primary column created with the table; do not add it again. Choose **Done** after each new column and **Save table** if prompted.

| Exact display name / CSV header | Schema name (target) | Description | Type and required level | Other properties |
| --- | --- | --- | --- | --- |
| `Campus Name` | `svrg_CampusName` | `Name of the fictional data center campus.` | Primary name, Text; Business required | Created with table; retain its generated settings; no default |
| `Campus Code` | `svrg_CampusCode` | `Stable fictional campus business code.` | Single-line Text; Business required | Format Text; max 20; Searchable Yes; Simple; no default |
| `Region` | `svrg_Region` | `Geographical region for campus reporting.` | Single-line Text; Optional | Format Text; max 100; Searchable Yes; Simple; no default |
| `Time Zone` | `svrg_TimeZone` | `IANA time zone identifier for campus reporting.` | Single-line Text; Optional | Format Text; max 100; Searchable Yes; Simple; no default |
| `Active` | `svrg_Active` | `Whether the campus is available for operational use.` | Yes/No Boolean; Optional | Labels Yes / No; default Yes; Searchable No if offered; not a separate global/local Choice |

Review each generated schema name before saving, where editable. Dataverse also creates a primary-key GUID; leave that system column unchanged.

### S02.02 — Enter the campus record

Open **DC Campus → Columns and data → Edit**. Show the columns `Campus Name`, `Campus Code`, `Region`, `Time Zone`, and `Active`, then enter:

| Campus Name | Campus Code | Region | Time Zone | Active |
| --- | --- | --- | --- | --- |
| Pacific Resilience Campus | `DC-PAC-01` | Pacific | `America/Los_Angeles` | Yes |

Save and reopen the table to confirm that the single campus row persists. You can instead import [campuses.csv](./data/campuses.csv) using **Import from CSV**, where available; inspect the field mappings and ensure the Yes/No value is accepted. **Use one method only**—manual entry *or* import—to avoid duplicate rows. The CSV header names match the table's column display names, not the `svrg_` technical names.

### S02.03 — Create the Data Hall table

Inside the same solution, choose **New → Table**, open advanced properties, and configure:

| Property | Value |
| --- | --- |
| Display name / plural | `DC Data Hall` / `DC Data Halls` |
| Description | `Fictional data halls and their designed IT power capacity.` |
| Primary name column | `Hall Name` |
| Primary column description | `Name of the fictional data hall within its campus.` |
| Type / record ownership | Standard / **Organization** |
| Table schema name (target) | `svrg_DCDataHall` |
| Primary name schema (target) | `svrg_HallName` |

Review the actual generated technical names and select **Create**. Organization ownership must be selected before creation.

### S02.04 — Add the Data Hall columns

Open **DC Data Hall → Schema → Columns → New column** and create the four additional columns using the settings below. **Hall Name** is already the table's primary column. The **Criticality** Global Choice is created as part of configuring that column; no earlier Choice-creation step is necessary. Choose **Done** after each new column and **Save table** if prompted.

| Exact display name / CSV header | Schema name (target) | Description | Type and required level | Other properties |
| --- | --- | --- | --- | --- |
| `Hall Name` | `svrg_HallName` | `Name of the fictional data hall within its campus.` | Primary name, Text; Business required | Created with table; retain its generated settings; no default |
| `Hall Code` | `svrg_HallCode` | `Stable fictional hall business code.` | Single-line Text; Business required | Format Text; max 30; Searchable Yes; Simple; no default |
| `Criticality` | `svrg_Criticality` | `Shared infrastructure criticality for the hall.` | **Single-select Choice; Business required** | **New Global Choice:** `DC Infrastructure Criticality` (`svrg_DCInfrastructureCriticality`); description: `Common criticality classification for fictional infrastructure assets and facilities.`; options **High, Medium, Low** (in this order); keep generated numeric values; Searchable Yes; no default |
| `Design IT Capacity kW` | `svrg_DesignITCapacitykW` | `Designed IT capacity in kilowatts, not measured live power.` | Decimal number; Business required | 2 decimal places; min 0; max 100000 if offered; Simple; no default |
| `Active` | `svrg_Active` | `Whether the hall is available for operational use.` | Yes/No Boolean; Optional | Labels Yes / No; default Yes; Searchable No if offered; not a separate global/local Choice |

For the **Criticality** column, select **Data type → Choice** (not multi-select). If **DC Infrastructure Criticality** is already available in the Choice picker, select it instead of creating a duplicate. Otherwise, choose **New choice**. In the modern designer, this creates a **Global Choice** by default. Enter the global Choice display name, description, unique name and three labels **exactly as shown in the row above**, retaining generated numeric values. Save/Done the Choice, then ensure the column is linked to **DC Infrastructure Criticality**. If the designer instead shows **Sync with global choice**, choose **Yes** and select that Global Choice. Do not select **Local choice** or create a separate option list. Set **Business required**, **Searchable Yes** and leave **Default choice** blank. The column (`svrg_Criticality`) and its Global Choice (`svrg_DCInfrastructureCriticality`) are separate technical components. If your designer does not offer **New choice** in the column panel, use **solution → New → Choice** to create the global list with the same properties, then return to this column and select it.

### S02.05 — Create the Campus lookup

Every hall must reference the existing campus record. In **DC Data Hall**, open **Schema → Relationships → New relationship → Many-to-one** and set **Related table = DC Campus**. Confirm that **DC Data Hall** is the current table: many hall records will link to one campus.

| Lookup / relationship property | Value |
| --- | --- |
| Lookup display name / CSV header | `Campus` |
| Lookup column schema name (target) | `svrg_Campus` |
| Lookup column description | `Parent campus for this data hall.` |
| Related table | `DC Campus` |
| Requirement / searchable | Business required / Yes |
| Relationship name (target, if editable) | `svrg_DCDataHall_DCCampus` |
| Relationship behavior, if configurable | **Referential — Restrict Delete** |

Select **Done**, then **Save table**. Return to **Schema → Columns** and confirm a **single** `Campus` Lookup column exists, pointing to `DC Campus`. The relationship wizard creates the lookup; **do not** add a second `Campus` text or Lookup column. The field stores a reference to the related Dataverse row; do not type a system GUID into the data grid.

### S02.06 — Add the two Data Hall records

Open **DC Data Hall → Columns and data → Edit**. Make the six columns visible, including the `Campus` lookup. In the lookup picker, select the existing **Pacific Resilience Campus** for both rows. Choose **High** from the `Criticality` options.

| Hall Name | Hall Code | Campus | Criticality | Design IT Capacity kW | Active |
| --- | --- | --- | --- | ---: | --- |
| Data Hall 01 | `DC-PAC-01-H01` | Pacific Resilience Campus | High | 2350.00 | Yes |
| Data Hall 02 | `DC-PAC-01-H02` | Pacific Resilience Campus | High | 2500.00 | Yes |

Save the data. Reopen the hall table and confirm the two rows both point to **the same saved campus record**, with the expected Choice and capacity values.

Alternatively, download [data-halls.csv](./data/data-halls.csv) and use the Dataverse **Import from CSV** experience. **Import the campus first**; then review the Data Hall import's **column mapping**. The file's six headers match the six table **display names** exactly, so simple fields will normally be mapped automatically. But you must also inspect **Criticality** for the correct existing **High** option, **Active** for a valid Yes/No value, and **Campus** through **Lookup Reference** (select `DC Campus` and match against its primary name, `Campus Name`). A header match does not by itself establish a valid Choice value or relationship. Use the file only if you have not entered the same rows manually. Follow the import result/progress report and correct any mapping errors before retrying.

### Finish Part 02

The campus table should show **one** Pacific Resilience Campus row. The data hall table should show **two** halls with unique codes, **High** criticality and designed capacities of **2350.00 kW** and **2500.00 kW**. Both Campus lookups should resolve to the existing campus when you reopen the table. The shared `DC Infrastructure Criticality` Global Choice contains High, Medium and Low.

You now have a genuine one-to-many campus-to-hall structure, ready for other fictional operational records to reference. No employee or asset records are needed in this lesson.


---

## Part 03 — Build the Employee Directory and Reporting Hierarchy

The campus and data halls now give our fictional facility a location structure. Next, we'll create an employee directory so that later incident and maintenance records can refer to consistent staff profiles and departments. We'll also connect each profile to a campus and, when applicable, to a manager.

You will create one **DC Employee Profile** table, populate **20 fictional employees**, and establish their reporting hierarchy. Download [employee-profiles.csv](./data/employee-profiles.csv). Its **nine headers exactly match the column display names** defined below; the underlying technical schema names use our `svrg` prefix. These are *fictional business profiles*, not real Microsoft Entra accounts, Microsoft 365 recipients, or authenticated approvers.

### S03.01 — Create the DC Employee Profile table

Open [Power Apps](https://make.powerapps.com) and go to **Solutions → SunnyVerse Data Center Operations 360 → New → Table**. Open advanced properties if you need to set the primary name and ownership.

| Table property | Enter |
| --- | --- |
| Display name / plural | `DC Employee Profile` / `DC Employee Profiles` |
| Description | `Fictional staff profiles for department assignment, shift grouping and reporting relationships.` |
| Primary name column | `Employee Name` |
| Primary-column description | `Display name of the fictional employee profile.` |
| Table type / ownership | Standard / **Organization** |
| Table schema name (target) | `svrg_DCEmployeeProfile` |
| Primary name schema (target) | `svrg_EmployeeName` |

Organization-owned records fit this shared *fictional staff reference directory*. They do not provide individual Dataverse permissions: genuine access control depends on signed-in identities and security roles. Review the primary name, ownership and generated technical names, then select **Create**. Do not alter the Dataverse-created GUID identifier.

### S03.02 — Add the employee business columns

Open **DC Employee Profile → Schema → Columns → New column**. Add the following fields in order, selecting **Done** for each and **Save table** when prompted. **Employee Name** already exists as the primary name column; it appears here so that its description and CSV mapping are explicit.

| Exact display name / CSV header | Schema name (target) | Description | Type and required level | Other properties |
| --- | --- | --- | --- | --- |
| `Employee Name` | `svrg_EmployeeName` | `Display name of the fictional employee profile.` | Primary name, Text; Business required | Created with table; retain generated primary-column settings; no default |
| `Employee Code` | `svrg_EmployeeCode` | `Stable fictional employee identifier used for data matching.` | Single-line Text; Business required | Format Text; max **20**; Searchable Yes; Simple; no default |
| `Job Title` | `svrg_JobTitle` | `Role title used to describe the fictional employee's responsibilities.` | Single-line Text; Business required | Format Text; max **100**; Searchable Yes; Simple; no default |
| `Shift Group` | `svrg_ShiftGroup` | `Fictional roster group assigned to this employee.` | **Single-select Choice; Business required** | Create/use **Global Choice** `DC Shift Group` (target `svrg_DCShiftGroup`); description `Shared fictional employee shift group classification.`; options **A, B, C, D** in that order; generated numeric values; Searchable Yes; **no default** |
| `Active` | `svrg_Active` | `Whether this fictional employee profile can be assigned new work.` | Yes/No Boolean; Optional | Labels Yes / No; default **Yes**; Searchable No if offered |
| `Is Synthetic` | `svrg_IsSynthetic` | `Indicates the profile contains fictional training data.` | Yes/No Boolean; Optional | Labels Yes / No; default **Yes**; Searchable No if offered |

For **Shift Group**, choose **Data type → Choice** (not Multi-select Choices). If **DC Shift Group** exists, select that Global Choice. Otherwise use **New choice** in the column editor; specify the exact Global Choice properties and A/B/C/D labels from the table, and save it. **New choice** creates a Global Choice in the modern designer; if the designer instead requires **Sync with global choice = Yes**, use that and select the newly created Global Choice. Do not create an unrelated Local Choice. Leave the default blank so you select each employee's actual group.

For both Yes/No fields, use the Boolean type—neither needs a separate Global Choice. Confirm the column names and types after saving.

### S03.03 — Create the Department, Campus and Manager lookups

Next, create three **many-to-one (N:1)** relationships on **DC Employee Profile**. The first two connect to existing tables; the third is a self-lookup because an employee's manager is another employee profile.

Open **DC Employee Profile → Schema → Relationships → New relationship → Many-to-one**. For each new relationship, choose the **Related table** shown below. Set the generated lookup's display name and properties as indicated.

| Exact lookup display name / CSV header | Schema name (target) | Description | Related table | Requirement and behavior |
| --- | --- | --- | --- | --- |
| `Department` | `svrg_Department` | `Operating department to which this fictional employee belongs.` | **DC Department** | Business required; Searchable Yes; Referential — Restrict Delete if available |
| `Campus` | `svrg_Campus` | `Data center campus where this fictional employee is assigned.` | **DC Campus** | Business required; Searchable Yes; Referential — Restrict Delete if available |
| `Manager` | `svrg_Manager` | `Fictional employee profile acting as this employee's direct manager.` | **DC Employee Profile** (same table) | **Optional**, since the top-level director has no manager; Searchable Yes; Referential — Restrict Delete if available |

Configure **Department** first, save the relationship/table, then **Campus**, then **Manager**. Confirm **Current table = DC Employee Profile** each time. If a relationship designer labels the lookup with the related table name by default, rename the lookup display name to the exact name in the first column **before saving**, where supported. Record the actual generated relationship name if the interface exposes it.

In **Schema → Columns**, check that precisely one lookup each named **Department**, **Campus**, and **Manager** exists, with the related tables shown above. Do not add a second column through **New column → Lookup** after the relationship already created it; those are alternative ways to define the same relationship.

**Manager is a self-reference**, not a User/Person field. The 20 profiles are fictional data, so selecting a manager here does not grant real access privileges or trigger approval messages to a Microsoft 365 account.

### S03.04 — Add the 20 employee profiles

Use the linked [employee-profiles.csv](./data/employee-profiles.csv) for the practice data. The file has these display-name headers, in this order:

```csv
Employee Name,Employee Code,Job Title,Department,Campus,Shift Group,Active,Is Synthetic,Manager
```

Its **Manager** values are initially blank. This is intentional: we first create all 20 employees so the self-lookup has existing records to reference. We'll assign the managers in the next section.

To import, open **DC Employee Profile → Import from CSV** or the available table **Import data** command. Select the file, then **Review Mapping**. Confirm each of the nine columns maps to the corresponding display name. The employee codes are values in **Employee Code**, **not** the Dataverse system ID.

Inspect the important value mappings before starting:

| CSV column | Dataverse field | How to validate the import |
| --- | --- | --- |
| `Employee Name`, `Employee Code`, `Job Title` | Text / primary name | Header matches field; codes follow `EMP-000001` through `EMP-000020` |
| `Department` | Lookup → DC Department | Resolve to existing records by the primary column **Department Name**; all six department names already exist |
| `Campus` | Lookup → DC Campus | Resolve the existing **Pacific Resilience Campus** record by its primary **Campus Name** |
| `Shift Group` | Global Choice-backed column | Check that **A, B, C, D** map to existing options; do not create new option labels |
| `Active`, `Is Synthetic` | Yes/No Boolean | Check `Yes` is accepted as a true/Yes value |
| `Manager` | Optional self-lookup | Blank for the initial import; skip/ignore the empty source mapping if required |

**Header matching alone doesn't resolve lookup or Choice values.** If an import experience cannot reliably map Department and Campus from their existing primary names, cancel that import and use the editable data grid to create the records from the same CSV; select the actual lookup records using the picker rather than entering text or GUIDs blindly. Choose **one** creation method, not both.

After the import or manual entry, open **DC Employee Profile → Columns and data**. You should see exactly **20** unique Employee Code values, all linked to an existing department and the same existing campus, with a Shift Group selected. Do not start a second import to fix a view filter or an unresolved lookup.

### S03.05 — Connect the reporting managers

All 20 fictional employee records should exist before you assign the **Manager** lookup. Open **DC Employee Profile → Columns and data → Edit** (or open each employee record). Locate the **Manager** field and use its lookup picker to select the proper existing employee profile.

The director **Sophia Carter** keeps Manager **blank**. For everyone else, use the following hierarchy. Each person in the right column has the Manager lookup set to the name in the left column.

| Manager (existing employee profile) | Employees who report to this manager |
| --- | --- |
| **Sophia Carter** | Emma Park, Anika Shah, Marcus Johnson, Arjun Davis |
| **Emma Park** | David Patel, Olivia Nair, Iris Chen, Priya Allen, Liam Santos |
| **Anika Shah** | Noah Morales |
| **Marcus Johnson** | Sana Kim, Jordan Wilson, Theo Singh |
| **David Patel** | Elena Stone, Daniel Lee, Ava Brooks, Mina Reed, Ethan Baker, Maya Iyer |

For example, open **Noah Morales** and set **Manager = Anika Shah**; open **Sana Kim** and select **Marcus Johnson**. Use the lookup picker, not a manually entered employee GUID. Save the updated records. This completes 19 manager links and one top-level employee without a manager.

Dataverse may allow you to select an inappropriate employee as the Manager. Check that nobody manages themselves, that the hierarchy does not contain a cycle, and that the names resolve to the intended records.

### Finish Part 03

Reopen **DC Employee Profile** and confirm there are **20** unique employee codes, each with the correct department, campus and shift group, **19 Manager lookups** that resolve to existing fictional profiles, and **one blank Manager** for Sophia Carter. Both Yes/No fields should show **Yes**. The Department and Campus records from earlier lessons remain unchanged.

This directory is now available for later app screens and work assignments; it is still **fictional directory data**, not user authentication, enterprise security roles or actual approval authority.

## Microsoft Learn references

- [Create a Power Platform solution](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-solution)
- [Create and edit Dataverse tables](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entities-portal)
- [Create and edit Dataverse columns](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-field-portal)
- [Dataverse table types and ownership](https://learn.microsoft.com/en-us/powerapps/maker/data-platform/types-of-entities)
- [Create global choices](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/custom-picklists)
- [Create and edit one-to-many / many-to-one relationships](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-1n-relationships-portal)
- [Import data and map choices/lookups](https://learn.microsoft.com/en-us/power-apps/user/import-data)

*All organizations, facilities, staff, and operational scenarios in this learning project are fictional. Do not use this guide to control live data center infrastructure.*
