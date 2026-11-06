# Data Center Operations 360 — Build-Along Guide

**SunnyVerse AI Labs | Independent Power Platform learning project**  
**Fictional organization:** SunnyVerse Renewable Group  
**Published:** Parts 00–15 — Solution Foundation, Department Master, Campus and Data Halls, Employee Directory, Asset and Sensor Registry, Alarm and Incident Management, Operations Command Center, Field Engineer Mobile App, Incident and Inspection Automation, Asset and Maintenance Manager, Change Risk and Procedure Approvals, Supporting Operations, Capacity Management and Rack Planning, Monitoring and Operational Intelligence, Intelligent Operations and Knowledge Review, Engineering Validation and Release Readiness

[Project home](./README.md) · [Practice data](./data/README.md)

Welcome to Data Center Operations 360. In this project, you will build a fictional data center operations solution using Microsoft Power Platform. The work is completed in an environment where you have permission to develop, and all practice records are fictional.

Part 00 prepares the solution. Parts 01–04 build reference data, Part 05 adds alarms and incidents, Part 06 creates the command center, Part 07 adds FieldOps, Part 08 configures notification flows, Part 09 adds maintenance operations, Part 10 adds change and risk reviews, and Part 11 introduces vendors, spares, inventory and shift handovers, and Part 12 builds a fictional rack and power capacity planning experience. Follow the lessons in order in an authorized learning environment.

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

You will create one **DC Employee Profile** table, populate **20 fictional employees**, and establish their reporting hierarchy. Download [employee-profiles.csv](./data/employee-profiles.csv). Its six headers match the text, Choice and Yes/No column display names used for initial import; related Department, Campus and Manager records are then selected using Dataverse lookups. The technical schema names use the `svrg` prefix. These are *fictional business profiles*, not real Microsoft Entra accounts, Microsoft 365 recipients, or authenticated approvers.

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

Download [employee-profiles.csv](./data/employee-profiles.csv). Its six CSV headers use the exact display names of the Dataverse columns configured in S03.02:

```csv
Employee Name,Employee Code,Job Title,Shift Group,Active,Is Synthetic
```

Open **DC Employee Profile → Import from CSV** (or **Import data**, depending on the portal). Upload the file and select **Review Mapping**. Match all six headers to their corresponding columns. **Employee Code** is a fictional business code, not the system-generated Dataverse GUID. For **Shift Group**, match A, B, C and D to the existing Global Choice options. For **Active** and **Is Synthetic**, confirm that Yes is interpreted as the Boolean **Yes** value.

Complete the import and reopen **DC Employee Profile → Columns and data**. Confirm the 20 fictional employee profiles exist with distinct codes (`EMP-000001` through `EMP-000020`). Use the table's column picker if one of these columns is hidden. If the import experience requires lookups before saving records, create the rows in the editable table instead, selecting the existing lookup records as described below.

Next, populate the **Department** and **Campus** lookups in the editable grid. For **Campus**, select the existing **Pacific Resilience Campus** record for **every employee**. For **Department**, select the related **DC Department** record according to the table below. These are actual Dataverse lookup selections, not ordinary text labels or copied GUIDs.

| Department lookup | Employee profiles |
| --- | --- |
| Data Center Operations | Sophia Carter, Emma Park, David Patel, Iris Chen, Priya Allen, Liam Santos |
| Electrical Operations | Anika Shah, Noah Morales |
| Mechanical & Cooling | Marcus Johnson, Sana Kim, Jordan Wilson, Theo Singh |
| Facilities Maintenance | Elena Stone, Daniel Lee, Ava Brooks, Mina Reed, Ethan Baker, Maya Iyer |
| Safety & Compliance | Arjun Davis |
| IT Infrastructure | Olivia Nair |

Save the lookup changes and reopen the table. Each profile should resolve to the intended existing Department and Campus record. Continue with the Manager hierarchy in S03.05. The file is intended for one initial import; don't import it again if those employee rows already exist.

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


---

## Part 04 — Build the Asset and Sensor Registry

Our fictional campus now has departments, halls and employees. In this lesson, we'll register the physical equipment that operates inside those halls and connect a smaller set of monitoring sensors to selected assets. **DC Asset** is the parent table for **DC Sensor**; each asset belongs to a data hall, and each sensor belongs to an asset.

We will create **100 assets** and **24 sensors**. Download [assets.csv](./data/assets.csv) and [sensors.csv](./data/sensors.csv). The headers are the exact **Dataverse display names** in the tables below. Technical schema names use the confirmed publisher prefix `svrg`. The two lookup fields, **Data Hall** and **Asset**, require explicit relationship mapping; matching a header alone does not establish a lookup.

### S04.01 — Create the DC Asset table

Open [Power Apps](https://make.powerapps.com), select the same environment as the earlier lessons and navigate to **Solutions → SunnyVerse Data Center Operations 360 → New → Table**. Open advanced table properties if needed.

| Table property | Enter |
| --- | --- |
| Display name / plural | `DC Asset` / `DC Assets` |
| Description | `Fictional data center equipment inventory across the two operating data halls.` |
| Primary name column | `Asset Name` |
| Primary-column description | `Display name of this fictional infrastructure asset.` |
| Table type / ownership | Standard / **Organization** |
| Table schema name (target) | `svrg_DCAsset` |
| Primary-name schema (target) | `svrg_AssetName` |

Confirm the primary name and **Organization** ownership before selecting **Create**. Leave the Dataverse-generated primary-key GUID unchanged.

### S04.02 — Configure the Asset columns and Choices

In **DC Asset → Schema → Columns → New column**, add each field in the table. **Asset Name** is already the primary name column—do not create it twice. Select **Done** after each new column and **Save table** when prompted.

| Exact display name / CSV header | Schema name (target) | Description | Type and required level | Other properties |
| --- | --- | --- | --- | --- |
| `Asset Name` | `svrg_AssetName` | `Display name of this fictional infrastructure asset.` | Primary Text; Business required | Created with table; no default |
| `Asset Code` | `svrg_AssetCode` | `Unique fictional equipment inventory code.` | Single-line Text; Business required | Format Text; max 24; Searchable Yes; Simple; no default |
| `Asset Category` | `svrg_AssetCategory` | `Shared classification of infrastructure equipment.` | **Single-select Choice; Business required** | **New Global Choice** `DC Equipment Category` (target `svrg_DCEquipmentCategory`); description `Reusable fictional infrastructure equipment categories.`; options **UPS, Generator, Cooling Unit, Switchgear, Power Distribution Unit, Server Rack**; keep generated numeric values; Searchable Yes; no default |
| `Criticality` | `svrg_Criticality` | `Operational importance classification of the asset.` | **Single-select Choice; Business required** | Reuse existing **Global Choice** `DC Infrastructure Criticality` (`svrg_DCInfrastructureCriticality`); High / Medium / Low; Searchable Yes; no default |
| `Manufacturer` | `svrg_Manufacturer` | `Fictional manufacturer label for the training equipment.` | Single-line Text; Optional | Format Text; max 80; Searchable Yes; Simple; no default |
| `Model Number` | `svrg_ModelNumber` | `Fictional equipment model reference.` | Single-line Text; Optional | Format Text; max 80; Simple; no default |
| `Serial Number` | `svrg_SerialNumber` | `Fictional equipment serial reference; never a real serial number.` | Single-line Text; Optional | Format Text; max 40; Searchable Yes; Simple; no default |
| `Rated Power kW` | `svrg_RatedPowerkW` | `Illustrative equipment nameplate power in kilowatts; not live measured consumption.` | Decimal number; Optional | 2 decimal places; minimum 0; Simple; no default |
| `Install Date` | `svrg_InstallDate` | `Fictional installation date for equipment lifecycle exercises.` | Date Only; Optional | Use Date only, not Date and Time; no default |
| `Operational Status` | `svrg_OperationalStatus` | `Current fictional equipment lifecycle state.` | **Single-select Choice; Business required** | **Local Choice** with **In Service, Standby, Under Maintenance, Retired**; keep generated numeric option values; Searchable Yes; no default |

For **Asset Category**, choose **Choice** rather than multi-select. Select the existing **DC Equipment Category** Global Choice if it is already correctly configured; otherwise, use **New choice** in the column editor. Configure its global name, description and six labels as shown in the row. Do not create a local duplicate. For **Criticality**, choose the existing **DC Infrastructure Criticality** Global Choice from Part 02; do not recreate its High/Medium/Low options.

For **Operational Status**, choose **Choice → View more → Local choice** (or the equivalent explicit local option) because this status list belongs only to the Asset column. Enter the four labels from the row. Keep the generated numeric values and no default so each imported record supplies its status. <https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-field-portal>

### S04.03 — Connect each asset to its Data Hall

Open **DC Asset → Schema → Relationships → New relationship → Many-to-one**. Set the **Related table** to the existing **DC Data Hall**, so multiple assets can belong to one hall.

| Exact lookup display name / CSV header | Schema name (target) | Description | Related table | Other properties |
| --- | --- | --- | --- | --- |
| `Data Hall` | `svrg_DataHall` | `The existing data hall containing this equipment asset.` | **DC Data Hall** | Business required; Searchable Yes; Referential — Restrict Delete if offered |

Select **Done → Save table** and confirm that **DC Asset → Schema → Columns** contains one **Data Hall** lookup pointing to **DC Data Hall**. If a lookup was created by the relationship editor, do not create a second lookup or a text column with the same name.

### S04.04 — Import the 100 fictional assets

Open **DC Asset → Import from CSV** in a supported Dataverse import experience and choose [assets.csv](./data/assets.csv). The CSV has these exact headers:

```csv
Asset Name,Asset Code,Asset Category,Criticality,Manufacturer,Model Number,Serial Number,Rated Power kW,Install Date,Operational Status,Data Hall
```

Select **Review Mapping**. Confirm the simple Text, Decimal and Date headers match their respective columns, and match the **Asset Category**, **Criticality** and **Operational Status** source labels to the *existing* Choice options rather than adding new ones. Ensure Yes/No, currency or other unintended destinations were **not** selected.

**For the Data Hall lookup**, open **Lookup Reference** in the import mapping for the **Data Hall** field. Choose the related **DC Data Hall** table and its primary name **Hall Name** as the search/match column. The source values are **Data Hall 01** and **Data Hall 02**, which already exist in Part 02. Do **not** map them as Dataverse GUIDs or match against the **Hall Code** field. Complete the import only once the wizard shows a valid reference mapping. If your import interface cannot specify lookup reference matching, **do not force the import**; use a supported import experience with lookup mapping or enter records via the Dataverse editable grid and select their real Data Hall records.

Import the file once, then open **Track Progress** or the run results and reopen **DC Asset → Columns and data**. The sample contains exactly **100 assets**: 12 UPS, 8 generators, 20 cooling units, 16 switchgear assets, 24 power distribution units and 20 server racks. **50 assets belong to Data Hall 01 and 50 to Data Hall 02.** Asset codes start with `DC-`; every code and serial number is fictional.

The **Rated Power kW** figures are illustrative equipment nameplate values and must not be summed as though every device represents independent IT capacity. No real equipment controls, telemetry, or work orders are created here.

### S04.05 — Create the DC Sensor table and its columns

Sensors will provide the equipment-linked metadata needed for later monitoring examples. They are **sensor inventory records, not live measurement rows**.

From the same solution choose **New → Table** and enter:

| Table property | Enter |
| --- | --- |
| Display name / plural | `DC Sensor` / `DC Sensors` |
| Description | `Fictional sensor registry linked to data center equipment for later monitoring exercises.` |
| Primary name column | `Sensor Name` |
| Primary-column description | `Display name of a fictional monitoring sensor.` |
| Table type / ownership | Standard / **Organization** |
| Table schema name (target) | `svrg_DCSensor` |
| Primary-name schema (target) | `svrg_SensorName` |

Select **Create**. Then open **DC Sensor → Schema → Columns → New column** and configure the fields below. The primary name is already created. Select **Done** after each and **Save table** when prompted.

| Exact display name / CSV header | Schema name (target) | Description | Type and required level | Other properties |
| --- | --- | --- | --- | --- |
| `Sensor Name` | `svrg_SensorName` | `Display name of a fictional monitoring sensor.` | Primary Text; Business required | Created with table; no default |
| `Sensor Code` | `svrg_SensorCode` | `Unique fictional sensor inventory identifier.` | Single-line Text; Business required | Format Text; max 24; Searchable Yes; Simple; no default |
| `Metric Type` | `svrg_MetricType` | `Type of measurement this sensor would produce.` | **Single-select Choice; Business required** | **Local Choice**: **Output Power, Temperature, Supply Air Temperature, Voltage, Electrical Power, Inlet Temperature**; retain generated numeric values; Searchable Yes; no default |
| `Unit` | `svrg_Unit` | `Unit in which the fictional sensor reports its measurement.` | Single-line Text; Business required | Format Text; max 16; Simple; no default |
| `Minimum Acceptable` | `svrg_MinimumAcceptable` | `Illustrative lower acceptable threshold for a sensor measurement.` | Decimal number; Business required | 2 decimal places; Simple; no default |
| `Maximum Acceptable` | `svrg_MaximumAcceptable` | `Illustrative upper acceptable threshold for a sensor measurement.` | Decimal number; Business required | 2 decimal places; Simple; no default |
| `Sample Interval Seconds` | `svrg_SampleIntervalSeconds` | `Illustrative sensor collection interval measured in seconds.` | Whole number; Business required | Minimum 1; maximum 3600 if available; Simple; no default |
| `Enabled` | `svrg_Enabled` | `Whether this fictional sensor is enabled for future simulation.` | Yes/No Boolean; Optional | Labels Yes / No; default Yes; Searchable No if offered |

For **Metric Type**, choose **Choice → View more → Local choice** and enter the six options shown in the table. There is no need to create a separate Global Choice used by no other table. The unit `degC` means degrees Celsius in our synthetic data; `kW` and `V` indicate kilowatts and volts. Set both decimal threshold fields to **2 decimal places** and retain the exact display names for CSV mapping.

### S04.06 — Link sensors to their assets

Open **DC Sensor → Schema → Relationships → New relationship → Many-to-one**, and select **Related table = DC Asset**. A sensor belongs to one asset, while an asset may have many sensors.

| Exact lookup display name / CSV header | Schema name (target) | Description | Related table | Other properties |
| --- | --- | --- | --- | --- |
| `Asset` | `svrg_Asset` | `Existing equipment asset monitored by this sensor.` | **DC Asset** | Business required; Searchable Yes; Referential — Restrict Delete if offered |

Select **Done → Save table**, then confirm the **Asset** lookup appears once in **DC Sensor → Schema → Columns**. Do not create a free-text Asset column.

### S04.07 — Import the 24 sensor records

After the 100 asset records exist, open **DC Sensor → Import from CSV** and select [sensors.csv](./data/sensors.csv). Its headers match the Sensor table's column display names:

```csv
Sensor Name,Sensor Code,Metric Type,Unit,Minimum Acceptable,Maximum Acceptable,Sample Interval Seconds,Enabled,Asset
```

In **Review Mapping**, match Text, Decimal, Whole Number and Yes/No columns with their correct types. Map each source **Metric Type** label to the matching existing **Local Choice** option. Confirm **Enabled = Yes** resolves to the Boolean Yes value.

For the **Asset** lookup, choose **Lookup Reference → DC Asset → Asset Name**, not the primary-key GUID. The source values, such as `UPS 001` and `Cooling Unit 002`, are existing Asset **primary names** from the earlier import. Do not map them to **Asset Code** or a GUID. Finish only after this lookup reference is correctly configured. If the wizard lacks lookup reference mapping, use a supported import path or enter the sensor rows in the editable grid using the **Asset** record picker.

Review the import progress and reopen the sensor table. You should see **24** sensors, each associated with one of the 100 existing assets. For every sensor record, **Minimum Acceptable** must be less than **Maximum Acceptable**, and **Sample Interval Seconds** should be **60**. These are metadata thresholds, not imported time-series readings.

### Finish Part 04

Reopen **DC Asset** and **DC Sensor**. Confirm **100 distinct Asset Codes**, **50 assets per Data Hall**, and **24 distinct Sensor Codes** whose **Asset** lookups resolve to real DC Asset records. The Asset categories match the six specified options; Criticality uses the existing shared Choice, while Operational Status and Metric Type use their local Choice lists. The earlier Campus, Data Hall, Department and Employee data remain unchanged.

You now have a relational infrastructure registry ready for incident and monitoring exercises. **No live sensor data or external hardware connection is required.**


---

## Part 05 — Build the Alarm and Incident Management Registers

The asset and sensor registry now identifies the equipment operating across our fictional data center. This lesson adds **DC Alarm** to describe detected operating conditions and **DC Incident** to track issues requiring investigation. Some incidents originate from alarms; others are reported directly by fictional employees. This gives us connected records to use in later application and automation exercises.

We'll create **120 alarm records** and **200 incident records** using [alarms.csv](./data/alarms.csv) and [incidents.csv](./data/incidents.csv). As in earlier lessons, CSV headers match the exact Dataverse **column display names**, while target schema names use our `svrg` prefix. Configure the tables first, then create the parent alarms before the incident records that reference them.

### S05.01 — Create DC Alarm

Open [Power Apps](https://make.powerapps.com), select your learning environment, then open **Solutions → SunnyVerse Data Center Operations 360 → New → Table**. Select advanced table properties when needed.

| Table property | Enter |
| --- | --- |
| Display name / plural | `DC Alarm` / `DC Alarms` |
| Description | `Fictional operating alerts reported by data center equipment and monitoring systems.` |
| Primary name column | `Alarm Name` |
| Primary-column description | `Readable description of a fictional operating alarm.` |
| Table type / ownership | Standard / **Organization** |
| Table schema name (target) | `svrg_DCAlarm` |
| Primary-name schema (target) | `svrg_AlarmName` |

Select **Organization** ownership before creating the table. Confirm the primary name and schema values, choose **Create**, and leave the Dataverse-generated primary-key GUID unchanged.

### S05.02 — Configure the Alarm columns and Choices

In **DC Alarm → Schema → Columns → New column**, add the following fields. **Alarm Name** is the primary column created with the table, so do not add it again. Complete each new column with **Done**, then select **Save table** where prompted.

| Exact display name / CSV header | Schema name (target) | Description | Data type and required level | Other properties |
| --- | --- | --- | --- | --- |
| `Alarm Name` | `svrg_AlarmName` | `Readable description of a fictional operating alarm.` | Primary Text; Business required | Created with table; no default |
| `Alarm Code` | `svrg_AlarmCode` | `Stable fictional identifier for the operating alarm.` | Single-line Text; Business required | Format Text; max **24**; Searchable Yes; Simple; no default |
| `Alarm Type` | `svrg_AlarmType` | `Type of condition represented by this alarm.` | Single-select Choice; Business required | **Local Choice:** High Temperature, Low Voltage, Power Deviation, Cooling Degradation, Equipment Fault, Communication Loss; Searchable Yes; no default |
| `Alarm Severity` | `svrg_AlarmSeverity` | `Reported seriousness of the operating condition.` | Single-select Choice; Business required | **Local Choice:** Critical, High, Medium, Low; Searchable Yes; no default |
| `Alarm Status` | `svrg_AlarmStatus` | `Acknowledgment and lifecycle state of the alarm.` | Single-select Choice; Business required | **Local Choice:** New, Acknowledged, Cleared, Suppressed; Searchable Yes; no default |
| `Detection Source` | `svrg_DetectionSource` | `Origin of the fictional alarm event.` | Single-select Choice; Business required | **Local Choice:** Sensor, System, Manual; Searchable Yes; no default |
| `Detected At` | `svrg_DetectedAt` | `Date and time when the fictional alarm was detected.` | Date and Time; Business required | Format **Date and time**; Behavior **User local**; no default |
| `Alarm Details` | `svrg_AlarmDetails` | `Description of the detected condition for investigation.` | Multiple lines of text; Optional | Maximum **2000** characters if configurable; Simple; no default |

Create each of the four Choice columns **directly in its column editor**. Choose **Choice → View more → Local choice**, not a separately named Global Choice, and enter the option labels in the order shown. Keep Dataverse-generated numeric option values. These Choices are specific to the Alarm table. There is no need to repeat the Asset Criticality Choice here; equipment criticality and alert severity describe different things.

For **Detected At**, choose the Date and Time type and **User local** behavior. The sample CSV timestamps use ISO 8601 **UTC** values ending in `Z`. A model-driven app may display the same instant converted into the viewer's local time zone.

### S05.03 — Link and load the Alarm records

Every alarm references an existing equipment asset. A sensor may also be associated with the alarm, but a sensor link is optional.

Open **DC Alarm → Schema → Relationships → New relationship → Many-to-one** for each row below. The current table must be **DC Alarm**; the related table is the destination to which the lookup points.

| Exact lookup display name / CSV header | Schema name (target) | Description | Related table | Requirement / other settings |
| --- | --- | --- | --- | --- |
| `Source Asset` | `svrg_SourceAsset` | `Existing data center equipment asset affected by this alarm.` | **DC Asset** | Business required; Searchable Yes; Referential — Restrict Delete when available |
| `Source Sensor` | `svrg_SourceSensor` | `Existing sensor associated with the alarm when the source is sensor-based.` | **DC Sensor** | Optional; Searchable Yes; Referential — Restrict Delete when available |

Choose **Done → Save table** and confirm the two lookup fields appear once under **Schema → Columns**. They must be Lookup types, not text columns. A sensor selected in **Source Sensor** must belong to the same asset identified by **Source Asset**.

Download [alarms.csv](./data/alarms.csv) and open the table's supported **Import from CSV** or **Import data** command. Its exact headers are:

```csv
Alarm Name,Alarm Code,Alarm Type,Alarm Severity,Alarm Status,Detection Source,Detected At,Alarm Details,Source Asset,Source Sensor
```

Review the mapping before importing: match each Choice label to the existing option, parse **Detected At** as a UTC Date and Time value, and resolve **Source Asset → DC Asset → Asset Name** and **Source Sensor → DC Sensor → Sensor Name** through your chosen import tool's supported lookup-reference mechanism. A blank **Source Sensor** is legitimate for System and Manual alerts. If a mapping cannot be configured, use an import method that supports it rather than loading unresolved references.

Complete the import once. Open the import result and return to **DC Alarm → Columns and data**. There should be **120 distinct Alarm Codes**, starting with `ALM-0001`. **48 alarms** refer to existing sensors; the other **72** do not. All 120 alarms must reference existing assets. These are fictional historical events, not live telemetry or actual facility alerts.

### S05.04 — Create DC Incident

Return to the same solution and choose **New → Table**.

| Table property | Enter |
| --- | --- |
| Display name / plural | `DC Incident` / `DC Incidents` |
| Description | `Fictional operational incidents linked to equipment, alarms and staff profiles.` |
| Primary name column | `Incident Name` |
| Primary-column description | `Readable title of a fictional operational incident.` |
| Table type / ownership | Standard / **Organization** |
| Table schema name (target) | `svrg_DCIncident` |
| Primary-name schema (target) | `svrg_IncidentName` |

Confirm **Organization** ownership, the primary-name column, and the intended schema names, then select **Create**.

### S05.05 — Configure the Incident columns and Choices

Open **DC Incident → Schema → Columns → New column**. Add each custom field as shown below. The primary-name column already exists.

| Exact display name / CSV header | Schema name (target) | Description | Data type and required level | Other properties |
| --- | --- | --- | --- | --- |
| `Incident Name` | `svrg_IncidentName` | `Readable title of a fictional operational incident.` | Primary Text; Business required | Created with table; no default |
| `Incident Code` | `svrg_IncidentCode` | `Stable fictional incident identifier for tracking.` | Single-line Text; Business required | Format Text; max **24**; Searchable Yes; Simple; no default |
| `Incident Category` | `svrg_IncidentCategory` | `Business area associated with the incident.` | Single-select Choice; Business required | **Local Choice:** Electrical, Mechanical & Cooling, IT Infrastructure, Facilities, Safety, Other; Searchable Yes; no default |
| `Priority` | `svrg_Priority` | `Response priority assigned to the incident.` | Single-select Choice; Business required | **Local Choice:** P1 Critical, P2 High, P3 Medium, P4 Low; Searchable Yes; no default |
| `Incident Status` | `svrg_IncidentStatus` | `Current work state of this operational incident.` | Single-select Choice; Business required | **Local Choice:** New, Assigned, In Progress, Resolved, Closed; Searchable Yes; no default |
| `Reported At` | `svrg_ReportedAt` | `Date and time when the incident was reported.` | Date and Time; Business required | Format **Date and time**; Behavior **User local**; no default |
| `Incident Description` | `svrg_IncidentDescription` | `What was observed or requires investigation.` | Multiple lines of text; Business required | Maximum **2000** characters if configurable; Simple; no default |
| `Safety Related` | `svrg_SafetyRelated` | `Whether the fictional incident has a safety classification.` | Yes/No Boolean; Optional | Labels Yes / No; default **No**; Searchable No if available |
| `Resolution Notes` | `svrg_ResolutionNotes` | `Recorded outcome for a resolved or closed practice incident.` | Multiple lines of text; Optional | Maximum **2000** characters if configurable; Simple; no default |

Create **Incident Category**, **Priority**, and **Incident Status** as **Local Choice** columns in their respective column editors, using precisely the displayed labels. Leave the defaults blank; the CSV supplies a value for each row. **Safety Related** is a Boolean, not a separate Choice. Save the table when prompted.

### S05.06 — Connect the Incident relationships and import records

Each incident refers to an existing asset and a fictional reporting employee. An assigned engineer and an originating alarm are optional.

Open **DC Incident → Schema → Relationships → New relationship → Many-to-one** for each lookup in this table, then select **Done → Save table**.

| Exact lookup display name / CSV header | Schema name (target) | Description | Related table | Requirement / other settings |
| --- | --- | --- | --- | --- |
| `Source Asset` | `svrg_SourceAsset` | `Existing equipment affected by the incident.` | **DC Asset** | Business required; Searchable Yes; Referential — Restrict Delete when available |
| `Reported By` | `svrg_ReportedBy` | `Fictional employee profile that reported the issue.` | **DC Employee Profile** | Business required; Searchable Yes; Referential — Restrict Delete when available |
| `Assigned Engineer` | `svrg_AssignedEngineer` | `Fictional employee profile assigned to investigate the issue.` | **DC Employee Profile** | Optional; Searchable Yes; Referential — Restrict Delete when available |
| `Related Alarm` | `svrg_RelatedAlarm` | `Existing alarm associated with this incident when one exists.` | **DC Alarm** | Optional; Searchable Yes; Referential — Restrict Delete when available |

Verify all four fields under **Schema → Columns**. **Reported By** and **Assigned Engineer** both point to **DC Employee Profile** but are different lookups. Neither grants Microsoft 365 permissions or sends real notifications; these are fictional staff references.

Download [incidents.csv](./data/incidents.csv) and import it into **DC Incident** using your supported import experience. Its display-name headers are:

```csv
Incident Name,Incident Code,Incident Category,Priority,Incident Status,Reported At,Incident Description,Safety Related,Resolution Notes,Source Asset,Reported By,Assigned Engineer,Related Alarm
```

In the field mapping, confirm the local Choice labels, **Safety Related** Yes/No values and **Reported At** UTC timestamps. Resolve lookup references to **Source Asset → DC Asset → Asset Name**, **Reported By / Assigned Engineer → DC Employee Profile → Employee Name**, and **Related Alarm → DC Alarm → Alarm Name**. The referenced Asset, Employee and Alarm records must already exist. Leave blank optional lookup values blank; do not create placeholder records.

After import, confirm there are **200 distinct Incident Codes**, beginning with `INC-0001`. The sample includes **120 incidents** associated with an existing alarm and **80 directly reported incidents** without an alarm; **160** have an assigned fictional engineer and **40** have the assignment blank. All 200 have an Asset and Reported By reference. For incidents linked to alarms, the Source Asset matches the related alarm's Source Asset.

### Finish Part 05

Reopen both tables and inspect a few records. **DC Alarm** should have **120** unique codes and valid equipment references, including **48** sensor-linked alerts. **DC Incident** should have **200** unique codes; the **120 Related Alarm** lookups, **200 Source Asset** lookups and **200 Reported By** lookups should resolve to existing fictional rows. Confirm the Choice values and timestamps remain populated, with the expected optional blank fields.

This is now a linked alarm-and-incident data model ready for later app screens, automated routing, acknowledgments and incident-management workflows. No app, flow, real alarm connector or live facility integration is required in this lesson.


---

## Part 06 — Build the Operations Command Center Canvas App

The data center's equipment, alarms and incident records are now connected in Dataverse. Next, we'll build **DC Operations Command Center**, a tablet Canvas App where an operator can monitor the fictional facility, browse incident and alarm records, review a selected incident and create or edit a record.

We'll build the screens in the order a user would use them. **The visual design is part of each step**: a deep-navy header, teal actions, a restrained amber accent, clear dark text, and comfortable light surfaces. No new Dataverse tables, datasets or flows are needed in this lesson.

| Screen | What the learner will do |
| --- | --- |
| `scrHome` | View incident, alarm and asset counts; open recent incidents |
| `scrIncidents` | Search and filter incidents, then open or create one |
| `scrIncidentDetail` | Read all the selected incident's business fields |
| `scrIncidentEdit` | Create/edit records using Dataverse form controls |
| `scrAlarms` | Search alarms and inspect their related records |

### S06.01 — Create the Canvas App and establish the design palette

Open [Power Apps](https://make.powerapps.com), select your authorized learning environment, and choose **Solutions → SunnyVerse Data Center Operations 360 → New → App → Canvas app**. Select **Tablet / Landscape** and name the app `DC Operations Command Center`.

In the editor select **Data → Add data → Microsoft Dataverse**. Add these existing tables, which will usually appear in Power Fx using their plural names:

| Data source | Existing Dataverse schema | Purpose |
| --- | --- | --- |
| `'DC Incidents'` | `svrg_DCIncident` | Browse and edit incidents |
| `'DC Alarms'` | `svrg_DCAlarm` | Browse alarms |
| `'DC Assets'` | `svrg_DCAsset` | Asset count |

Now select **App** at the top of Tree view and choose its **Formulas** property from the property selector above the formula bar. Paste the following reusable named formulas. They let every screen share a consistent palette without adding a hidden theme screen or repeating hexadecimal values.

```powerfx
clrPrimary = ColorValue("#16364F");
clrSecondary = ColorValue("#086B78");
clrAccent = ColorValue("#F3B547");
clrCanvas = ColorValue("#F3F7FA");
clrSurface = ColorValue("#FFFFFF");
clrText = ColorValue("#192F42");
clrMuted = ColorValue("#536A7B");
clrBorder = ColorValue("#D9E4EB");
clrSelected = ColorValue("#E1F2F3");
clrDanger = ColorValue("#B83D51");
clrSuccess = ColorValue("#20715B");
```

| Color role | Color | Use |
| --- | --- | --- |
| Primary navy | **#16364F** | Screen headers and product identity |
| Secondary teal | **#086B78** | Primary buttons, focus and selection |
| Signal amber | **#F3B547** | Thin dividers and KPI emphasis |
| Arctic Mist | **#F3F7FA** | Every screen's background |
| Surface white | **#FFFFFF** | KPIs, lists, forms and inputs |
| Ink slate | **#192F42** | Main text |
| Blue-gray | **#536A7B** | Descriptions and metadata |
| Cool line | **#D9E4EB** | Borders |
| Pale teal | **#E1F2F3** | Selected gallery rows |
| Red / green | **#B83D51 / #20715B** | Errors and success feedback, with text |

For the steps below use **Classic** labels, buttons and text inputs when offered. A Classic Text input uses `.Text`; a Modern Text input can use `.Value` instead. To change a property, select the control in **Tree view**, choose **Fill**, **Text**, **OnSelect** or another property above the formula bar, paste the expression and press **Enter**. In English Power Fx, commas separate function arguments and semicolons separate actions.

**Checkpoint 1.** All three Dataverse tables are present under Data, and entering `clrPrimary` into a control's **Fill** property is recognized without an error.

### S06.02 — Create five screens with consistent headers and navigation

In **Tree view**, select the first blank screen, choose **… → Rename** and enter `scrHome`. Choose **New screen → Blank** four times, renaming the new screens `scrIncidents`, `scrIncidentDetail`, `scrIncidentEdit` and `scrAlarms` in that order.

On **scrHome**, create a header using **Insert → Shapes → Rectangle** twice, plus a **Text label**. Set their properties as follows. Build the same header on each of the other four screens; copy the two rectangles and title label and paste them onto the destination screen if you prefer. Power Apps will give copied controls unique names.

| Control on Home | Property | Formula/value |
| --- | --- | --- |
| Rectangle `recHeaderHome` | X, Y, Width, Height | `0`, `0`, `Parent.Width`, `88` |
| `recHeaderHome` | Fill, BorderThickness | `clrPrimary`, `0` |
| Rectangle `recAccentHome` | X, Y, Width, Height | `0`, `88`, `Parent.Width`, `4` |
| `recAccentHome` | Fill, BorderThickness | `clrAccent`, `0` |
| Label `lblHomeTitle` | X, Y, Width, Height | `32`, `18`, `Parent.Width - 64`, `52` |
| `lblHomeTitle` | Text | `"DATA CENTER OPERATIONS 360  |  COMMAND CENTER"` |
| `lblHomeTitle` | Color, Fill, Size, FontWeight | `clrSurface`, `Color.Transparent`, `25`, `FontWeight.Bold` |

For **every screen**, set the screen's **Fill = `clrCanvas`** and use the same navy header / amber divider / white title. Set the title label text and its name using this table:

| Screen | Title label | Text |
| --- | --- | --- |
| `scrHome` | `lblHomeTitle` | `"DATA CENTER OPERATIONS 360  |  COMMAND CENTER"` |
| `scrIncidents` | `lblIncidentsTitle` | `"INCIDENT MANAGEMENT"` |
| `scrIncidentDetail` | `lblIncidentTitle` | `"INCIDENT DETAILS"` |
| `scrIncidentEdit` | `lblEditTitle` | `If(varIsNewIncident, "NEW INCIDENT", "EDIT INCIDENT")` |
| `scrAlarms` | `lblAlarmsTitle` | `"ALARM MONITORING"` |

Use **Arrange → Send to back** for both rectangles so they never cover the title or clickable controls. Keep the header across the full width of the tablet. The additional content starts below **Y = 92**.

Now add buttons using **Insert → Button**, select each new button in Tree view, and use **… → Rename**. Set these basic navigation actions; the Save, Edit and New actions will be configured with their forms.

| Screen | Button name | Text property | OnSelect property |
| --- | --- | --- | --- |
| `scrHome` | `btnHomeIncidents` | `"Open incidents"` | `Navigate(scrIncidents, ScreenTransition.Fade)` |
| `scrHome` | `btnHomeAlarms` | `"Open alarms"` | `Navigate(scrAlarms, ScreenTransition.Fade)` |
| `scrHome` | `btnRefreshHome` | `"Refresh data"` | `Refresh('DC Incidents'); Refresh('DC Alarms'); Refresh('DC Assets'); Notify("Data refreshed.", NotificationType.Information)` |
| `scrIncidents` | `btnIncidentsHome` | `"Home"` | `Navigate(scrHome, ScreenTransition.None)` |
| `scrIncidentDetail` | `btnDetailBack` | `"Back to incidents"` | `Navigate(scrIncidents, ScreenTransition.None)` |
| `scrIncidentDetail` | `btnEditIncident` | `"Edit incident"` | Configured in S06.05 |
| `scrIncidentEdit` | `btnSaveIncident` | `"Save incident"` | Configured in S06.06 |
| `scrIncidentEdit` | `btnCancelIncident` | `"Cancel"` | Configured in S06.06 |
| `scrAlarms` | `btnAlarmsHome` | `"Home"` | `Navigate(scrHome, ScreenTransition.None)` |

Apply these **button appearance settings now**, so new controls do not remain default blue:

| Button style | Property | Value |
| --- | --- | --- |
| Primary buttons (Open, Edit, New, Save, Refresh) | Fill / Color / BorderThickness | `clrSecondary` / `clrSurface` / `0` |
| Primary buttons | HoverFill / PressedFill | `ColorValue("#07515B")` / `ColorValue("#06444C")` |
| Back / Cancel / Home | Fill / Color / BorderColor / BorderThickness | `clrSurface` / `clrPrimary` / `clrBorder` / `1` |
| All buttons | Height / Size | `44` / `15` |
| Classic buttons, where available | RadiusTopLeft, RadiusTopRight, RadiusBottomLeft, RadiusBottomRight | `8` for each |

Set **App → StartScreen = `scrHome`** without quotation marks. Place navigation buttons in an action row with at least 16 pixels between them; do not cover the header.

**Checkpoint 2.** Five screens exist, all with a navy header, amber separator and pale background. Preview **Open incidents → Home** and **Open alarms → Home**. Button labels are intentional, not the default `Button`.

### S06.03 — Build the Home KPIs and recent-incident list

On `scrHome` insert three **Text labels** for the KPI cards and rename them `lblCountIncidents`, `lblCountAlarms` and `lblCountAssets`. Place them horizontally below the header. Apply their formulas:

| Label | Text property |
| --- | --- |
| `lblCountIncidents` | `"INCIDENTS" & Char(10) & Text(CountIf('DC Incidents', true), "0")` |
| `lblCountAlarms` | `"ALARMS" & Char(10) & Text(CountIf('DC Alarms', true), "0")` |
| `lblCountAssets` | `"ASSETS" & Char(10) & Text(CountIf('DC Assets', true), "0")` |

| Card property | Formula/value |
| --- | --- |
| Fill / Color | `clrSurface` / `clrText` |
| BorderColor / BorderThickness | `clrBorder` / `1` |
| Size / Align / Height | `20` / `Align.Center` / `102` |
| All card Y positions | `124` |
| `lblCountIncidents` X / Width | `32` / `(Parent.Width - 96) / 3` |
| `lblCountAlarms` X / Width | `lblCountIncidents.X + lblCountIncidents.Width + 16` / `lblCountIncidents.Width` |
| `lblCountAssets` X / Width | `lblCountAlarms.X + lblCountAlarms.Width + 16` / `lblCountIncidents.Width` |
| `lblCountAlarms` BorderColor | `clrAccent` (one restrained highlight) |

A plain Dataverse `CountRows` may return a cached count; `CountIf(table, true)` can return an exact count within the supported delegation limit. If necessary, enable **Settings → Upcoming features → Preview → Enhanced delegation for Microsoft Dataverse** when that setting is available. If a count reads zero while records appear in the gallery, open **App checker** and inspect the delegation warning, data source and permissions. Do not replace the formula with a fixed number.

Under the cards insert a label `lblRecentHeading` with **Text = `"RECENT INCIDENTS"`**, **Color = `clrPrimary`**, **Size = `17`**, **FontWeight = `FontWeight.Bold`**, **X = `32`**, **Y = `247`**.

Next choose **Insert → Gallery → Blank vertical**, rename it `galRecentIncidents`, and set:

| Gallery property | Formula/value |
| --- | --- |
| Items | `Sort('DC Incidents', 'Reported At', SortOrder.Descending)` |
| OnSelect | `Set(varSelectedIncident, ThisItem); Navigate(scrIncidentDetail, ScreenTransition.Fade)` |
| X / Y | `32` / `292` |
| Width / Height | `Parent.Width - 64` / `Parent.Height - 390` |
| TemplateSize / TemplatePadding | `72` / `4` |
| Fill / TemplateFill | `clrSurface` / `If(ThisItem.IsSelected, clrSelected, clrSurface)` |

Select **Edit gallery** (pencil in first row), then insert **two Text labels inside its template**, not on the surrounding screen. Rename them `lblRecentName` and `lblRecentMeta`. A blank gallery has no image placeholder; if you chose another gallery layout, remove the **Image** template control only.

| Inner gallery label | Text | Color / size / position |
| --- | --- | --- |
| `lblRecentName` | `ThisItem.'Incident Name'` | `clrText` / `16`; X `16`, Y `7`, Width `Parent.TemplateWidth - 32` |
| `lblRecentMeta` | `ThisItem.'Incident Code' & "  ·  " & Text(ThisItem.'Incident Status')` | `clrMuted` / `13`; X `16`, Y `36`, Width `Parent.TemplateWidth - 32` |

For both nested labels set **Fill = `Color.Transparent`** and **OnSelect = `Select(Parent)`**. Place `btnHomeIncidents`, `btnHomeAlarms` and `btnRefreshHome` below the gallery in one row and keep them clear of the gallery's scroll area.

**Checkpoint 3.** The three KPI cards report the actual Dataverse records (initial dataset: 200 incidents, 120 alarms, 100 assets). Recent incidents appear as compact text rows without gray image icons. Buttons are teal and the gallery has a pale-teal selected row.

### S06.04 — Build the Incident Management queue

On `scrIncidents`, insert **Classic Text input** `txtIncidentSearch`, **buttons** `btnOnlyUnassigned` and `btnNewIncident`, then a **Blank vertical gallery** `galIncidents`. The Home button already exists. Arrange the search and three buttons across the top of the content area (under the navy header); place the gallery below.

| Control | Property | Value |
| --- | --- | --- |
| `txtIncidentSearch` | HintText / Default | `"Search incident code or name"` / `""` |
| `txtIncidentSearch` | X / Y / Width / Height | `32` / `124` / `Parent.Width * 0.43` / `44` |
| `txtIncidentSearch` | Fill / Color / BorderColor / FocusedBorderColor | `clrSurface` / `clrText` / `clrBorder` / `clrSecondary` |
| `scrIncidents` | OnVisible | `Set(varOnlyUnassigned, false)` |
| `btnOnlyUnassigned` | Text | `If(varOnlyUnassigned, "Show all", "Unassigned only")` |
| `btnOnlyUnassigned` | OnSelect | `Set(varOnlyUnassigned, !varOnlyUnassigned)` |
| `btnNewIncident` | Text | `"New incident"` |
| `btnNewIncident` | OnSelect | Configured in S06.06 |
| `galIncidents` | X / Y / Width / Height | `32` / `193` / `Parent.Width - 64` / `Parent.Height - 220` |
| `galIncidents` | TemplateSize / TemplatePadding | `78` / `4` |
| `galIncidents` | Fill / TemplateFill | `clrSurface` / `If(ThisItem.IsSelected, clrSelected, clrSurface)` |
| `galIncidents` | OnSelect | `Set(varSelectedIncident, ThisItem); Navigate(scrIncidentDetail, ScreenTransition.Fade)` |

Paste into **galIncidents.Items**:

```powerfx
Sort(
    Filter(
        'DC Incidents',
        IsBlank(txtIncidentSearch.Text) ||
            StartsWith('Incident Code', txtIncidentSearch.Text) ||
            StartsWith('Incident Name', txtIncidentSearch.Text),
        !varOnlyUnassigned || IsBlank('Assigned Engineer')
    ),
    'Reported At',
    SortOrder.Descending
)
```

Inside the first gallery template add two labels, `lblIncidentRowName` and `lblIncidentRowMeta`. Remove any default Image control rather than leaving generic image icons. Set both labels to **Fill = `Color.Transparent`**, **OnSelect = `Select(Parent)`**, **X = `16`** and **Width = `Parent.TemplateWidth - 32`**.

| Template label | Text formula | Style |
| --- | --- | --- |
| `lblIncidentRowName` | `ThisItem.'Incident Name'` | Color `clrText`; Size `16`; FontWeight `FontWeight.Bold`; Y `7` |
| `lblIncidentRowMeta` | `ThisItem.'Incident Code' & "  ·  " & Text(ThisItem.'Incident Status') & "  ·  " & If(IsBlank(ThisItem.'Assigned Engineer'), "Unassigned", ThisItem.'Assigned Engineer'.'Employee Name')` | Color `clrMuted`; Size `13`; Y `39` |

Choose the actual related `'Employee Name'` from Power Apps autocomplete if needed; the assignment is a Dataverse lookup. On narrower screens, put **Home** on a second action row rather than squeezing the search and buttons together.

**Checkpoint 4.** Searching `INC-0200` finds the matching incident. Clearing the search and selecting **Unassigned only** shows records without an assigned engineer; **Show all** restores the list. Rows are readable and image-free.

### S06.05 — Create the complete Incident Details view

Open `scrIncidentDetail`. Select **Insert → Forms → Display form**, rename it `frmIncidentView`, and configure:

| Control | Property | Value |
| --- | --- | --- |
| `frmIncidentView` | DataSource / Item | `'DC Incidents'` / `varSelectedIncident` |
| `frmIncidentView` | X / Y / Width / Height | `32` / `116` / `Parent.Width - 64` / `Parent.Height - 214` |
| `frmIncidentView` | Columns / Fill | `2` / `clrSurface` |
| `frmIncidentView` | BorderColor / BorderThickness | `clrBorder` / `1` |
| `btnEditIncident` | Text | `"Edit incident"` |
| `btnEditIncident` | OnSelect | `Set(varIsNewIncident, false); EditForm(frmIncidentEdit); Navigate(scrIncidentEdit, ScreenTransition.Fade)` |
| `btnDetailBack` | Text | `"Back to incidents"` |

Select **frmIncidentView → Edit fields → Add field** and include exactly the following **13 business fields**, in this order:

| Row | Left | Right |
| --- | --- | --- |
| 1 | Incident Name | Incident Code |
| 2 | Incident Category | Priority |
| 3 | Incident Status | Reported At |
| 4 | Incident Description | Safety Related |
| 5 | Source Asset | Reported By |
| 6 | Assigned Engineer | Related Alarm |
| 7 | Resolution Notes | — |

If the form automatically displays system **Status** or **Status Reason**, remove **those cards from the form**, not the Dataverse columns. **Incident Status** is the custom operational field and must remain.

Expand the form's generated cards in Tree view. For each card set the **caption/field label** (often `DataCardKey…`) to **Color = `clrMuted`**, **Size = `12`** and **FontWeight = `FontWeight.Bold`**. Set the displayed value control to **Color = `clrText`**, **Size = `15`** where available. Leave the generated field bindings alone. Place **Edit incident** (teal) and **Back to incidents** (white outlined) in a button row outside the form. If text is cut off, increase the form's available height or switch its Columns property to `1`.

**Checkpoint 5.** Navigate from the Incident queue and select `INC-0002`. Its complete details, including Source Asset and reporting/assigned employees, appear in the white form instead of an empty page.

### S06.06 — Create the Incident Editor with themed forms and Save/Cancel

Open `scrIncidentEdit`, choose **Insert → Forms → Edit form** and rename it `frmIncidentEdit`. The editor creates Dataverse-aware cards for each selected field.

| Control | Property | Value |
| --- | --- | --- |
| `frmIncidentEdit` | DataSource / Item | `'DC Incidents'` / `varSelectedIncident` |
| `frmIncidentEdit` | X / Y / Width / Height | `32` / `116` / `Parent.Width - 64` / `Parent.Height - 214` |
| `frmIncidentEdit` | Columns / Fill | `2` / `clrSurface` |
| `frmIncidentEdit` | BorderColor / BorderThickness | `clrBorder` / `1` |
| `lblEditTitle` | Text | `If(varIsNewIncident, "NEW INCIDENT", "EDIT INCIDENT")` |
| `btnNewIncident` (on `scrIncidents`) | OnSelect | `Set(varIsNewIncident, true); NewForm(frmIncidentEdit); Navigate(scrIncidentEdit, ScreenTransition.Fade)` |
| `btnSaveIncident` | Text | `"Save incident"` |
| `btnSaveIncident` | OnSelect | `SubmitForm(frmIncidentEdit)` |
| `btnCancelIncident` | Text | `"Cancel"` |

In **Edit fields → Add field**, choose the same 13 business columns and order as the Details form in S06.05. Include **Source Asset** and **Reported By** (required lookups), **Assigned Engineer** and **Related Alarm** (optional lookups). Keep the custom **Incident Status**; remove autogenerated system Status/Status Reason cards if present.

Style each generated card *without changing its logic*:

| Form element | Property | Value |
| --- | --- | --- |
| DataCardKey (field caption) | Color / Size / FontWeight | `clrMuted` / `12` / `FontWeight.Bold` |
| Input, Combo box, or Date picker | Fill / Color / BorderColor | `clrSurface` / `clrText` / `clrBorder` |
| Classic editable input (where offered) | FocusedBorderColor | `clrSecondary` |
| ErrorMessage label | Color | `clrDanger` |
| Required-star label | Color | `clrDanger` |

Keep each DataCard's **DataField, Default, Update and Required** properties and the generated lookup pickers unchanged. Changing these can prevent valid Dataverse values from being submitted. Place **Save incident** (teal) and **Cancel** (outlined white) outside the form and below the last visible card.

Set **btnCancelIncident.OnSelect**:

```powerfx
ResetForm(frmIncidentEdit);
If(
    varIsNewIncident,
    Navigate(scrIncidents, ScreenTransition.None),
    Navigate(scrIncidentDetail, ScreenTransition.None)
)
```

Set **frmIncidentEdit.OnSuccess**:

```powerfx
Set(varSelectedIncident, frmIncidentEdit.LastSubmit);
Set(varIsNewIncident, false);
Refresh('DC Incidents');
Notify("Incident saved.", NotificationType.Success);
Navigate(scrIncidentDetail, ScreenTransition.Fade)
```

Set **frmIncidentEdit.OnFailure**:

```powerfx
Notify(
    Coalesce(frmIncidentEdit.Error, "Incident was not saved. Review required fields."),
    NotificationType.Error
)
```

**Edit:** select an incident, then choose **Edit incident**. **New:** from the queue choose **New incident**, which opens a blank form. Required fields include Incident Name, Incident Code, Incident Category, Priority, Incident Status, Reported At, Incident Description, Source Asset and Reported By. Select existing records from lookup pickers. Assigning a fictional employee in the form does not change real Microsoft 365 permissions.

**Checkpoint 6.** Open `INC-0002`, change **Incident Status** from **Assigned** to **In Progress**, save and reopen; then change it back to **Assigned** and save. Open New incident and press **Cancel** without submitting. Both buttons display the correct text, no records are unintentionally added, and the form is readable.

### S06.07 — Build the themed Alarm Monitoring screen

Select `scrAlarms`. Insert a **Classic Text input** `txtAlarmSearch`, a **Blank vertical Gallery** `galAlarms` and a **Display form** `frmAlarmView`. Place the search field over the gallery on the **left** and the form on the **right**. The Home button already has its formula and outlined appearance.

| Control | Property | Formula/value |
| --- | --- | --- |
| `txtAlarmSearch` | HintText / Default | `"Search alarm code or name"` / `""` |
| `txtAlarmSearch` | X / Y / Width / Height | `32` / `120` / `Parent.Width * 0.38` / `44` |
| `txtAlarmSearch` | Fill / Color / BorderColor | `clrSurface` / `clrText` / `clrBorder` |
| `galAlarms` | X / Y / Width / Height | `32` / `181` / `Parent.Width * 0.4` / `Parent.Height - 209` |
| `galAlarms` | TemplateSize / TemplatePadding | `78` / `4` |
| `galAlarms` | Fill / TemplateFill | `clrSurface` / `If(ThisItem.IsSelected, clrSelected, clrSurface)` |
| `galAlarms` | OnSelect | `Set(varSelectedAlarm, ThisItem)` |
| `frmAlarmView` | DataSource / Item | `'DC Alarms'` / `varSelectedAlarm` |
| `frmAlarmView` | X / Y | `galAlarms.X + galAlarms.Width + 24` / `181` |
| `frmAlarmView` | Width / Height | `Parent.Width - galAlarms.Width - 88` / `Parent.Height - 209` |
| `frmAlarmView` | Columns / Fill / BorderColor | `1` / `clrSurface` / `clrBorder` |

Set **galAlarms.Items**:

```powerfx
Sort(
    Filter(
        'DC Alarms',
        IsBlank(txtAlarmSearch.Text) ||
            StartsWith('Alarm Code', txtAlarmSearch.Text) ||
            StartsWith('Alarm Name', txtAlarmSearch.Text)
    ),
    'Detected At',
    SortOrder.Descending
)
```

Insert two labels **inside the gallery template** and name them `lblAlarmRowName` and `lblAlarmRowMeta`. Remove any Image placeholder. Set their **Fill = `Color.Transparent`**, **OnSelect = `Select(Parent)`**, **X = `16`** and **Width = `Parent.TemplateWidth - 32`**.

| Label | Text | Style |
| --- | --- | --- |
| `lblAlarmRowName` | `ThisItem.'Alarm Name'` | `clrText`; Size `16`; Y `7`; FontWeight `FontWeight.Bold` |
| `lblAlarmRowMeta` | `ThisItem.'Alarm Code' & "  ·  " & Text(ThisItem.'Alarm Severity') & "  ·  " & Text(ThisItem.'Alarm Status')` | `clrMuted`; Size `13`; Y `39` |

On **frmAlarmView → Edit fields → Add field**, add: Alarm Name, Alarm Code, Alarm Type, Alarm Severity, Alarm Status, Detection Source, Detected At, Alarm Details, Source Asset and Source Sensor. Apply **clrMuted** to the card captions and **clrText** to their values; the form itself has a white background. A blank form before selecting a gallery row is expected.

**Checkpoint 7.** Search `ALM-0001`, select it and verify its type, severity, time, Source Asset and Source Sensor in the right-hand form. The gallery and details are readable and use the same palette as the incident screens.

### S06.08 — Complete the functional tests, save and publish

Select **Preview / Play (F5)** and carry out the checks below in the working app.

| Test | Action | Expected result |
| --- | --- | --- |
| T01 — Dashboard | Open Home, choose Refresh data | Dataverse totals appear; no unexplained zeros |
| T02 — Theme | Visit all five screens | Navy headers, amber accents, Arctic Mist backgrounds, white forms/cards, teal primary buttons, readable labels |
| T03 — Navigation | Open Incidents → Home → Alarms → Home | Navigation works |
| T04 — Search | Enter `INC-0200` and `ALM-0001` | Correct record appears in the matching gallery |
| T05 — Incident queue | Toggle Unassigned only / Show all | Correct queue filtering |
| T06 — Details | Open `INC-0002` | Full custom business details and lookups appear |
| T07 — Edit | Change custom Incident Status, save, reopen, restore | Persisted changes and success feedback |
| T08 — New/Cancel | Open New incident; choose Cancel | No new record created |
| T09 — Alarm details | Select `ALM-0001` | Read-only form shows alarm and related asset/sensor |
| T10 — App checker | Open **App checker** in Studio | Resolve blocking formula errors and accessibility warnings |

If a KPI shows zero while a gallery contains records, inspect its delegation warning and Dataverse table access. If a form is blank, inspect **DataSource**, **Item**, selection variables and field list. If any control still displays `Button` or a gray image placeholder, finish configuring or remove that default template element.

Select **Save**, then **Publish → Publish this version**. Return to **Solutions → SunnyVerse Data Center Operations 360** and confirm **DC Operations Command Center** appears as the single Canvas App created in this part.

### Finish Part 06

You have a **five-screen Operations Command Center** with consistent navy, teal, amber and neutral colors, live Dataverse KPI formulas, searchable image-free incident and alarm lists, readable details, and a working incident New/Edit form. The app uses the existing fictional records and does not operate real equipment or send real notifications.


---

## Part 07 — Build the Field Engineer Mobile App

Our Operations Command Center provides a desktop view of alarms and incidents. Next, we'll create **DC FieldOps**, a portrait Canvas App for a fictional field engineer carrying a phone. The app will show existing incidents, allow an update to an incident's operational status, and record equipment inspections with notes and supporting evidence. It uses the existing Assets, Incidents and Employee Profiles from earlier lessons.

First we'll create **DC Field Inspection**, a small Dataverse table for inspection records. Then we'll create the mobile app and enter two sample inspections through its own form. **No CSV import or new Power Automate flow is needed.** We'll use a distinct **Night Shift Neon** visual design: a fully black screen, deep slate panels, vivid cyan actions, violet dividers and warm-gold highlights. Wherever the selected Canvas control exposes a **Font** property, set it to **Comic Sans MS** with a fallback for devices that don't have that font. The theme is applied during each build activity, not in a separate styling exercise.

### S07.01 — Create the DC Field Inspection table

Open [Power Apps](https://make.powerapps.com), select the same authorized environment, then navigate to **Solutions → SunnyVerse Data Center Operations 360 → New → Table**. Open the advanced table properties so that the primary name, ownership and attachment settings are visible.

| Table property | Enter |
| --- | --- |
| Display name / plural | `DC Field Inspection` / `DC Field Inspections` |
| Description | `Fictional mobile equipment inspections with findings, follow-up decisions and supporting evidence.` |
| Primary name column | `Inspection Name` |
| Primary-column description | `Readable title of the fictional equipment inspection.` |
| Type / record ownership | Standard / **Organization** |
| Table schema name (target) | `svrg_DCFieldInspection` |
| Primary-name schema name (target) | `svrg_InspectionName` |
| Enable attachments / Notes | **Yes** — enable notes and attachments for this table |

Choose **Organization** ownership because these training inspection records form a shared reference history. Set **Enable attachments** (sometimes labeled **Notes and attachments**) to **On** when the table's properties expose it. This permits supported form-based evidence uploads; it is **not** a separate text or image column.

Select **Create** and reopen the table's properties to confirm that the primary name reads **Inspection Name** and that attachments are enabled. Leave the generated Dataverse GUID column unchanged. If the notes/attachments setting was not available during creation, locate it under **Table properties → Advanced options** and enable it before making the app.

### S07.02 — Add the inspection columns

Open **DC Field Inspection → Schema → Columns → New column**. Enter the display names, descriptions, types and options from the table. The first row is the primary name column created in S07.01; **do not create it again**. Use **Done** after each new column and **Save table** when prompted. Set **Behavior = Simple** for applicable fields, and retain the generated numeric Choice values.

| Exact display name | Schema name (target) | Description | Type / Required | Other properties |
| --- | --- | --- | --- | --- |
| `Inspection Name` | `svrg_InspectionName` | `Readable title of the fictional equipment inspection.` | Primary Text; Business required | Created with table; no default |
| `Inspection Code` | `svrg_InspectionCode` | `Stable fictional inspection identifier for later reporting.` | Single-line Text; Business required | Format Text; max 24; Searchable Yes; no default |
| `Inspection Date` | `svrg_InspectionDate` | `Date on which the fictional equipment inspection was performed.` | Date Only; Business required | Date-only behavior; no default |
| `Inspection Status` | `svrg_InspectionStatus` | `Progress of the inspection through its work lifecycle.` | Single-select Choice; Business required | **Local Choice:** Planned, In Progress, Completed; Searchable Yes; no default |
| `Inspection Result` | `svrg_InspectionResult` | `Outcome recorded after examining the asset.` | Single-select Choice; Optional | **Local Choice:** Pass, Attention, Fail, Not Assessed; Searchable Yes; no default |
| `Finding Description` | `svrg_FindingDescription` | `Observed condition or issue identified during the inspection.` | Multiline Text; Optional | Max 2000 characters if available; no default |
| `Action Taken` | `svrg_ActionTaken` | `Action completed during the inspection or recommended next step.` | Multiline Text; Optional | Max 2000 characters if available; no default |
| `Follow-up Required` | `svrg_FollowUpRequired` | `Whether another action is needed after the inspection.` | Yes/No Boolean; Optional | Labels Yes / No; default No; Searchable No if available |
| `Duration Minutes` | `svrg_DurationMinutes` | `Illustrative number of minutes spent on the inspection.` | Whole Number; Optional | Format None; minimum 0, maximum 1440 if offered; no default |

To create **Inspection Status**, select **Data type → Choice**, keep the choice **local to this column** (for a designer showing **Sync with global choice**, set it to **No**), add the three labels exactly as shown, and leave the default empty. Repeat for **Inspection Result**, using its four labels. If the designer instead offers **Local choice** directly, select it. These are two independent local Choice columns; do not create global duplicates. **Follow-up Required** is a Boolean Yes/No column, not a Choice.

**Checkpoint 1 — Table definition.** Reopen **Schema → Columns**. Confirm the primary name and all eight additional business columns, with the intended `svrg` schema prefix and the exact Local Choice labels. No Asset or Employee fields should have been created as plain text.

### S07.03 — Add the inspection relationships

Each inspection concerns an existing equipment asset and identifies a fictional employee profile who performed it. An inspection may also reference an earlier incident, but that is optional.

Open **DC Field Inspection → Schema → Relationships → New relationship → Many-to-one** for each row below. Keep **DC Field Inspection** as the current table, choose the indicated **Related table**, enter the exact lookup display name, and save the relationship. The lookup column is created with the relationship; **do not add it again** from Columns.

| Lookup display name | Schema name (target) | Description | Related table | Requirement / other settings |
| --- | --- | --- | --- | --- |
| `Asset` | `svrg_Asset` | `Existing equipment asset examined during this inspection.` | **DC Asset** | Business required; Searchable Yes; Referential / Restrict Delete where available |
| `Inspected By` | `svrg_InspectedBy` | `Fictional employee profile who completed the inspection.` | **DC Employee Profile** | Business required; Searchable Yes; Referential / Restrict Delete where available |
| `Related Incident` | `svrg_RelatedIncident` | `Existing incident associated with the finding when applicable.` | **DC Incident** | Optional; Searchable Yes; Referential / Restrict Delete where available |

In **Schema → Columns**, verify that **Asset**, **Inspected By** and **Related Incident** each have type **Lookup**, and that their related tables match the table above. The employee profile is fictional reference data; it does not represent the signed-in user's Microsoft identity or grant access permissions.

**Checkpoint 2 — Relationships.** The DC Field Inspection table has **three** lookups: two required and one optional. The related Asset, Employee Profile and Incident tables already contain the practice records created earlier.

### S07.04 — Create DC FieldOps with a black canvas, neon palette and Comic Sans MS typography

Return to **Solutions → SunnyVerse Data Center Operations 360 → New → App → Canvas app**. Choose **Phone / Portrait** and enter **DC FieldOps** as the app's name. In the editor open **Data → Add data → Microsoft Dataverse** and connect these existing tables:

| Studio data source | Purpose |
| --- | --- |
| `'DC Incidents'` | Browse and update incident records |
| `'DC Assets'` | Select an asset for inspection |
| `'DC Employee Profiles'` | Select a fictional inspector in the form |
| `'DC Field Inspections'` | Create, browse and edit inspection records |

Select **App** in Tree view and choose the **Formulas** property above the formula bar. Enter these named formulas. Using one palette means the header, screens, forms, galleries and buttons remain visually consistent. The screen itself is **pure black**; elevated cards use dark slate so their edges and contents remain clear.

```powerfx
clrPrimary = ColorValue("#000000");
clrCanvas = ColorValue("#000000");
clrSurface = ColorValue("#141C2A");
clrSecondary = ColorValue("#27D7E7");
clrAccent = ColorValue("#AC91FF");
clrSignal = ColorValue("#FFC86A");
clrText = ColorValue("#F6F9FF");
clrMuted = ColorValue("#BECDDD");
clrBorder = ColorValue("#38475D");
clrSelected = ColorValue("#203F52");
clrDanger = ColorValue("#FF879A");
clrSuccess = ColorValue("#76E8BB");
fontField = "Comic Sans MS";
```

| Role | Color / font token | Purpose |
| --- | --- | --- |
| Header and entire canvas | `clrPrimary` / `clrCanvas` — **#000000** | Pure black, focused night-shift environment |
| Primary interaction | `clrSecondary` — **#27D7E7** | Cyan navigation, buttons and focus |
| Secondary accent | `clrAccent` — **#AC91FF** | Violet header underline and selected visual emphasis |
| Signal highlight | `clrSignal` — **#FFC86A** | Warm-gold marker for important figures |
| Cards, forms and inputs | `clrSurface` — **#141C2A** | Dark slate surfaces distinct from black |
| Primary text | `clrText` — **#F6F9FF** | High-contrast near-white labels |
| Supporting text | `clrMuted` — **#BECDDD** | Metadata, captions and descriptions |
| Borders | `clrBorder` — **#38475D** | Subtle separation of controls |
| Selected records | `clrSelected` — **#203F52** | Dark cyan-blue gallery selection |
| Error and success | `clrDanger` / `clrSuccess` | State indicators with written messages |
| Typography | `fontField` — **Comic Sans MS** | Preferred text family in supported controls; device default font if unavailable |

In Power Apps, the **Font** property accepts a font-family name. Apply **Font = `fontField`** to all Classic labels, buttons, text inputs, gallery labels, and supported form card captions/values. This named formula resolves to **Comic Sans MS**, not a comma-separated CSS font list. If Comic Sans MS is unavailable on the device, Power Apps can render a platform fallback; test on an actual phone rather than assuming the lettering will look identical everywhere. Combo boxes, date pickers, attachment controls and Modern controls can expose different typography properties: set **Font** where supported, but leave their generated data bindings intact. No external font file is required.

Apply this reusable control-format reference while adding controls in the steps below. It keeps the entire app consistent rather than styling only the title.

| Control type | Properties to configure during insertion | Formula/value |
| --- | --- | --- |
| Every screen | Fill | `clrCanvas` |
| Header rectangles | Fill / BorderThickness | `clrPrimary` / `0` |
| Screen title labels | Font / Color / FontWeight | `fontField` / `clrSecondary` / `FontWeight.Bold` |
| Body and gallery title labels | Font / Color | `fontField` / `clrText` |
| Secondary labels and form card captions | Font / Color | `fontField` / `clrMuted` |
| Classic input controls | Font / Fill / Color / BorderColor | `fontField` / `clrSurface` / `clrText` / `clrBorder` |
| Primary buttons | Font / Fill / Color | `fontField` / `clrSecondary` / `clrPrimary` |
| Back, Cancel, Refresh buttons | Font / Fill / Color / BorderColor | `fontField` / `clrSurface` / `clrText` / `clrBorder` |
| Gallery containers | Fill / TemplateFill | `clrSurface` / `If(ThisItem.IsSelected, clrSelected, clrSurface)` |
| Display/Edit forms | Fill / BorderColor | `clrSurface` / `clrBorder` |
| Form input validation label | Font / Color | `fontField` / `clrDanger` |

**Why these colors?** Cyan-on-black buttons are easy to locate, dark-slate cards establish grouping without losing the black-screen effect, violet adds identity without overwhelming the work area, and warm gold highlights operational information. Always pair an alert color with readable text. Avoid white text on a bright cyan button; the **black text** is intentional for contrast.

Create the six blank screens in **Tree view**, using **New screen → Blank** and **… → Rename**:

| Screen | Purpose | Controls to add in its later section |
| --- | --- | --- |
| `scrFieldHome` | Mobile landing page | KPIs, navigation, refresh |
| `scrFieldIncidents` | Incident search | Search, unassigned filter, incident gallery |
| `scrFieldIncidentDetail` | Read selected incident | Display form, Edit and Back buttons |
| `scrFieldIncidentEdit` | Update selected incident | Edit form, Save and Cancel |
| `scrFieldInspections` | Inspection list | Search, inspection gallery, New button |
| `scrFieldInspectionEdit` | Create or update inspection | Edit form including attachments, Save and Cancel |

On **each screen**, set **Fill = `clrCanvas`** for the complete black canvas. Create a rectangle (**Insert → Shapes → Rectangle**) and a text label for its header. Give the rectangle **X = 0, Y = 0, Width = Parent.Width, Height = 72, Fill = `clrPrimary`, BorderThickness = 0**. Add a thin violet divider rectangle with **X = 0, Y = 72, Width = Parent.Width, Height = 3, Fill = `clrAccent`**. Send both shapes to the back. Set each title label's **X = 18, Y = 13, Width = Parent.Width - 36, Height = 44, Font = `fontField`, Color = `clrSecondary`, Fill = `Color.Transparent`, Size = 20, FontWeight = `FontWeight.Bold`**. This gives every screen a black top area with a vivid cyan Comic Sans heading and a fine violet accent.

| Screen title label | Text |
| --- | --- |
| `lblFieldHomeTitle` | `"DC FIELDOPS"` |
| `lblFieldIncidentsTitle` | `"FIELD INCIDENTS"` |
| `lblFieldIncidentDetailTitle` | `"INCIDENT DETAILS"` |
| `lblFieldIncidentEditTitle` | `"UPDATE INCIDENT"` |
| `lblFieldInspectionsTitle` | `"EQUIPMENT INSPECTIONS"` |
| `lblFieldInspectionEditTitle` | `If(varNewInspection, "NEW INSPECTION", "EDIT INSPECTION")` |

Use **Classic** Text labels, Buttons, Text inputs, and **Blank vertical** Galleries when available, so the formulas use the classic `Text` property. Add each title to its screen and rename it as above. Set **App → StartScreen = `scrFieldHome`**.

Buttons will use consistent mobile styling: **Font = `fontField`**, **Fill = `clrSecondary`**, **Color = `clrPrimary`** (black text), **Height = 48**, **Size = 16**, **BorderThickness = 0**. Set **HoverFill = `ColorValue("#54E6F1")`** and **PressedFill = `ColorValue("#1EB0C0")`** for Classic buttons. For **Back**, **Cancel** and **Refresh**, use **Fill = `clrSurface`**, **Color = `clrText`**, **BorderColor = `clrBorder`**, **BorderThickness = 1**. Use a 12–16 pixel margin between touch controls. When available, set Classic button corner radii to `8` for all four corners.

### S07.05 — Build the FieldOps Home screen

Open `scrFieldHome`. Add two large labels for the KPIs and three buttons below them. Rename the controls exactly and set their properties:

| Control | Property | Formula / value |
| --- | --- | --- |
| `lblFieldIncidentCount` | Text | `"INCIDENTS" & Char(10) & Text(CountIf('DC Incidents', true), "0")` |
| `lblFieldInspectionCount` | Text | `"INSPECTIONS" & Char(10) & Text(CountIf('DC Field Inspections', true), "0")` |
| Both KPI labels | Fill / Color / BorderColor / BorderThickness / Font | `clrSurface` / `clrText` / `clrBorder` / `1` / `fontField` |
| Both KPI labels | X / Width / Height / Align | `18` / `Parent.Width - 36` / `90` / `Align.Center` |
| `lblFieldIncidentCount` | Y | `104` |
| `lblFieldInspectionCount` | Y | `212` |
| `btnFieldOpenIncidents` | Text / OnSelect | `"Browse incidents"` / `Navigate(scrFieldIncidents, ScreenTransition.Fade)` |
| `btnFieldOpenInspections` | Text / OnSelect | `"Record inspection"` / `Navigate(scrFieldInspections, ScreenTransition.Fade)` |
| `btnFieldRefresh` | Text / OnSelect | `"Refresh"` / `Refresh('DC Incidents'); Refresh('DC Field Inspections'); Notify("Records refreshed.", NotificationType.Information)` |

Set each button's **X = 18**, **Width = Parent.Width - 36**, and use **Y = 330, 398, and 466**, respectively. The first two buttons use **cyan Fill, black Text and Comic Sans MS**; Refresh uses a dark-slate Fill, light Text and a muted border. Set **lblFieldIncidentCount.BorderColor = `clrSignal`** so the warm-gold edge marks an important KPI without filling the card with bright color.

With the original practice data, Incidents should initially show approximately **200**, and Inspections should initially show **0**. Dataverse counts can be cached or delegation-limited; the `CountIf` formula is intended to request an exact count in supported Dataverse environments with enhanced delegation enabled. If a count contradicts the table's records, inspect the formula warning rather than replacing the number with a fixed literal.

**Checkpoint 3 — Mobile Home.** The portrait screen is fully black with two readable dark-slate KPI cards, large cyan touch buttons, a black header, a thin violet divider and Comic Sans MS wherever supported. Both Browse incidents and Record inspection navigate to their respective screens.

### S07.06 — Browse and open existing incidents

On `scrFieldIncidents` insert **Classic Text input** `txtFieldIncidentSearch`, **Button** `btnFieldOnlyUnassigned`, **Blank vertical Gallery** `galFieldIncidents` and **Button** `btnFieldIncidentsHome`. Place the search field at the top, the filter button beneath it, and the list below. Keep the Home action visible at the bottom.

| Control or screen | Property | Formula / value |
| --- | --- | --- |
| `txtFieldIncidentSearch` | HintText / Default | `"Search incident code or name"` / `""` |
| `txtFieldIncidentSearch` | X / Y / Width / Height | `18` / `94` / `Parent.Width - 36` / `48` |
| `txtFieldIncidentSearch` | Font / Fill / Color / BorderColor / FocusedBorderColor | `fontField` / `clrSurface` / `clrText` / `clrBorder` / `clrSecondary` |
| `scrFieldIncidents` | OnVisible | `Set(varFieldOnlyUnassigned, false)` |
| `btnFieldOnlyUnassigned` | Text | `If(varFieldOnlyUnassigned, "Show all incidents", "Unassigned only")` |
| `btnFieldOnlyUnassigned` | OnSelect | `Set(varFieldOnlyUnassigned, !varFieldOnlyUnassigned)` |
| `btnFieldOnlyUnassigned` | X / Y / Width | `18` / `158` / `Parent.Width - 36` |
| `galFieldIncidents` | X / Y / Width / Height | `18` / `222` / `Parent.Width - 36` / `Parent.Height - 315` |
| `galFieldIncidents` | Fill / TemplateFill | `clrSurface` / `If(ThisItem.IsSelected, clrSelected, clrSurface)` |
| `galFieldIncidents` | TemplateSize / TemplatePadding | `82` / `4` |
| `galFieldIncidents` | OnSelect | `Set(varFieldIncident, ThisItem); Navigate(scrFieldIncidentDetail, ScreenTransition.Fade)` |
| `btnFieldIncidentsHome` | Text / OnSelect | `"Home"` / `Navigate(scrFieldHome, ScreenTransition.None)` |

Set **galFieldIncidents.Items**:

```powerfx
Sort(
    Filter(
        'DC Incidents',
        IsBlank(txtFieldIncidentSearch.Text) ||
            StartsWith('Incident Code', txtFieldIncidentSearch.Text) ||
            StartsWith('Incident Name', txtFieldIncidentSearch.Text),
        !varFieldOnlyUnassigned || 'Assigned Engineer' = Blank()
    ),
    'Reported At',
    SortOrder.Descending
)
```

The unassigned condition uses a **blank lookup comparison** (`'Assigned Engineer' = Blank()`) rather than applying `IsBlank` directly to a related record. In the connected Dataverse environment, review the gallery's delegation indicators; a lookup predicate can still produce warnings depending on connector version and combined filters. **Do not assume the gallery is complete for datasets exceeding the app's nondelegation record limit unless the warning is resolved and tested.** For a larger deployment, validate a delegable server-side view/filter or a precomputed assignment-state field. Do not increase the data row limit as a substitute for fixing delegation.

Inside the gallery template insert **two labels**, `lblFieldIncidentRowName` and `lblFieldIncidentRowMeta`. Do not use a photo gallery. Give the first **Text = `ThisItem.'Incident Name'`**, **Color = `clrText`**, **Font = `fontField`**, **Size = 15**; the second **Text = `ThisItem.'Incident Code' & "  ·  " & Text(ThisItem.'Incident Status')`**, **Color = `clrMuted`**, **Font = `fontField`**, **Size = 12**. Set both **OnSelect = `Select(Parent)`**, **Fill = `Color.Transparent`**, **X = 12** and **Width = Parent.TemplateWidth - 24**. Use **Y = 9** for the first and **Y = 42** for the second. Remove any placeholder image control from the template.

On `scrFieldIncidentDetail` choose **Insert → Forms → Display form** and rename it `frmFieldIncidentView`. Add two buttons, `btnFieldOpenEdit` and `btnFieldDetailBack`. Configure:

| Control | Property | Formula / value |
| --- | --- | --- |
| `frmFieldIncidentView` | DataSource / Item | `'DC Incidents'` / `varFieldIncident` |
| `frmFieldIncidentView` | X / Y / Width / Height | `18` / `96` / `Parent.Width - 36` / `Parent.Height - 194` |
| `frmFieldIncidentView` | Columns / Fill | `1` / `clrSurface` |
| `btnFieldOpenEdit` | Text / OnSelect | `"Update incident"` / `Navigate(scrFieldIncidentEdit, ScreenTransition.Fade)` |
| `btnFieldDetailBack` | Text / OnSelect | `"Back to incidents"` / `Navigate(scrFieldIncidents, ScreenTransition.None)` |

Under **frmFieldIncidentView → Edit fields → Add field**, include **Incident Name**, **Incident Code**, **Priority**, **Incident Status**, **Reported At**, **Incident Description**, **Source Asset**, **Reported By**, **Assigned Engineer**, **Related Alarm** and **Resolution Notes**. Remove any automatically included *system* Status or Status Reason cards from the form; keep the custom **Incident Status**. Set each card caption's **Font = `fontField`**, **Color = `clrMuted`**; set the displayed value control's **Font = `fontField`** where offered and **Color = `clrText`**. Give the form **Fill = `clrSurface`** and **BorderColor = `clrBorder`**. Use one column for readable phone layouts. For a read-only lookup whose generated value label is blank, select **the value label inside its display card** (not the card itself) and set its **Text** to the related record's primary name using the table below; retain the underlying **DataField** and **Item** properties.

| Read-only field | Value label Text formula | Meaning |
| --- | --- | --- |
| Source Asset | `Coalesce(varFieldIncident.'Source Asset'.'Asset Name', "—")` | Show the name of the existing asset |
| Reported By | `Coalesce(varFieldIncident.'Reported By'.'Employee Name', "—")` | Show the fictional reporting employee |
| Assigned Engineer | `Coalesce(varFieldIncident.'Assigned Engineer'.'Employee Name', "Unassigned")` | Show the selected fictional engineer or an unassigned label |
| Related Alarm | `Coalesce(varFieldIncident.'Related Alarm'.'Alarm Name', "None")` | Show the linked alarm name when present |

These formulas are for **display-only labels**, not editable lookup cards; the edit forms keep the generated lookup pickers. Keep the label **Font = `fontField`** (where available), **Color = `clrText`**, and an accessible label identifying the field.

**Checkpoint 4 — Incident navigation.** Search `INC-0002`, select it, and verify the Incident Details form displays the selected existing record. The Back button returns to the incident gallery without creating anything.

### S07.07 — Update an existing incident from the phone

Open `scrFieldIncidentEdit`, choose **Insert → Forms → Edit form**, and rename it `frmFieldIncidentEdit`. This is a **limited update form**, not a new-incident wizard. It changes the operational fields needed for practice without changing the record's originating Asset or reporting employee.

| Control | Property | Formula / value |
| --- | --- | --- |
| `frmFieldIncidentEdit` | DataSource / Item | `'DC Incidents'` / `varFieldIncident` |
| `frmFieldIncidentEdit` | X / Y / Width / Height | `18` / `96` / `Parent.Width - 36` / `Parent.Height - 194` |
| `frmFieldIncidentEdit` | Columns / Fill | `1` / `clrSurface` |
| `scrFieldIncidentEdit` | OnVisible | `EditForm(frmFieldIncidentEdit)` |
| `btnFieldSaveIncident` | Text / OnSelect | `"Save update"` / `SubmitForm(frmFieldIncidentEdit)` |
| `btnFieldCancelIncident` | Text / OnSelect | `"Cancel"` / `ResetForm(frmFieldIncidentEdit); Navigate(scrFieldIncidentDetail, ScreenTransition.None)` |

Under **Edit fields → Add field**, choose only **Incident Status**, **Assigned Engineer**, **Resolution Notes** and **Incident Description**, in that order. Keep their generated Choice/Lookup/Multiline controls and **Update** bindings. The remaining Incident fields retain their previously saved values because they are not being modified by these cards.

Set `frmFieldIncidentEdit.OnSuccess`:

```powerfx
Set(varFieldIncident, frmFieldIncidentEdit.LastSubmit);
Refresh('DC Incidents');
Notify("Incident updated.", NotificationType.Success);
Navigate(scrFieldIncidentDetail, ScreenTransition.Fade)
```

Set `frmFieldIncidentEdit.OnFailure`:

```powerfx
Notify(
    Coalesce(frmFieldIncidentEdit.Error, "Update not saved."),
    NotificationType.Error
)
```

Position Save update and Cancel beneath the form; use **cyan Fill with black Comic Sans text** for Save, and a dark-slate Fill with light Comic Sans text and a thin border for Cancel. For each form-card caption set **Font = `fontField`**, **Color = `clrMuted`**. For editable controls use **Font = `fontField`** (where offered), **Fill = `clrSurface`**, **Color = `clrText`**, **BorderColor = `clrBorder`** and **FocusedBorderColor = `clrSecondary`** (where available). Error labels use **Font = `fontField`** and **Color = `clrDanger`**. Leave the generated Combo box's lookup source and any card **DataField / Default / Update** settings unchanged.

**Checkpoint 5 — Update.** Open `INC-0002`, update its **Incident Status** from Assigned to In Progress, save and confirm the status is shown in the read-only details. Change it back to Assigned so the fictional seed data stays consistent. Canceling the form must not save a change. Using the destination screen's **OnVisible** property to enter edit mode avoids directly referencing a form control from another screen.

### S07.08 — Create the inspection list and mobile inspection form

On `scrFieldInspections` insert **Classic Text input** `txtFieldInspectionSearch`, **Blank vertical Gallery** `galFieldInspections`, **Button** `btnFieldNewInspection` and **Button** `btnFieldInspectionsHome`. Use the existing title and theme header.

| Control | Property | Formula / value |
| --- | --- | --- |
| `txtFieldInspectionSearch` | HintText / Default | `"Search inspection code or name"` / `""` |
| `txtFieldInspectionSearch` | Font / Fill / Color / BorderColor | `fontField` / `clrSurface` / `clrText` / `clrBorder` |
| `txtFieldInspectionSearch` | X / Y / Width / Height | `18` / `96` / `Parent.Width - 36` / `48` |
| `galFieldInspections` | Items | See formula below |
| `galFieldInspections` | X / Y / Width / Height | `18` / `211` / `Parent.Width - 36` / `Parent.Height - 304` |
| `galFieldInspections` | Fill / TemplateFill | `clrSurface` / `If(ThisItem.IsSelected, clrSelected, clrSurface)` |
| `galFieldInspections` | TemplateSize | `80` |
| `galFieldInspections` | OnSelect | `Set(varFieldSelectedInspection, ThisItem); Set(varNewInspection, false); Navigate(scrFieldInspectionEdit, ScreenTransition.Fade)` |
| `btnFieldNewInspection` | Text / OnSelect | `"New inspection"` / `Set(varNewInspection, true); Navigate(scrFieldInspectionEdit, ScreenTransition.Fade)` |
| `btnFieldInspectionsHome` | Text / OnSelect | `"Home"` / `Navigate(scrFieldHome, ScreenTransition.None)` |

Set **galFieldInspections.Items**:

```powerfx
Sort(
    Filter(
        'DC Field Inspections',
        IsBlank(txtFieldInspectionSearch.Text) ||
            StartsWith('Inspection Code', txtFieldInspectionSearch.Text) ||
            StartsWith('Inspection Name', txtFieldInspectionSearch.Text)
    ),
    'Inspection Date',
    SortOrder.Descending
)
```

Inside the gallery template add **two labels**: `lblFieldInspectionRowName` (**Text = `ThisItem.'Inspection Name'`**, **Font = `fontField`**, Color `clrText`, Size 15), and `lblFieldInspectionRowMeta` (**Text = `ThisItem.'Inspection Code' & "  ·  " & Text(ThisItem.'Inspection Status')`**, **Font = `fontField`**, Color `clrMuted`, Size 12). Set **OnSelect = `Select(Parent)`**, **Fill = `Color.Transparent`**, **X = 12** and **Width = Parent.TemplateWidth - 24** for both. Put New inspection above the gallery and Home below it.

Next open `scrFieldInspectionEdit`, insert **Forms → Edit form**, rename it `frmFieldInspectionEdit`, then add the **Save inspection** and **Cancel** buttons below the form.

| Control | Property | Formula / value |
| --- | --- | --- |
| `frmFieldInspectionEdit` | DataSource | `'DC Field Inspections'` |
| `frmFieldInspectionEdit` | Item | `varFieldSelectedInspection` |
| `frmFieldInspectionEdit` | X / Y / Width / Height | `18` / `94` / `Parent.Width - 36` / `Parent.Height - 198` |
| `frmFieldInspectionEdit` | Columns / Fill | `1` / `clrSurface` |
| `scrFieldInspectionEdit` | OnVisible | `If(varNewInspection, NewForm(frmFieldInspectionEdit), EditForm(frmFieldInspectionEdit))` |
| `btnFieldSaveInspection` | Text / OnSelect | `"Save inspection"` / `SubmitForm(frmFieldInspectionEdit)` |
| `btnFieldSaveInspection` | DisplayMode | `If(frmFieldInspectionEdit.Valid, DisplayMode.Edit, DisplayMode.Disabled)` |
| `btnFieldCancelInspection` | Text / OnSelect | `"Cancel"` / `ResetForm(frmFieldInspectionEdit); Navigate(scrFieldInspections, ScreenTransition.None)` |

Under **frmFieldInspectionEdit → Edit fields → Add field**, select these fields in this order. Each should remain a **Dataverse-generated data card** so its Choice, Date, Yes/No and Lookup values save correctly.

| Form order | Field | Learner action |
| --- | --- | --- |
| 1 | **Inspection Name** | Enter a readable inspection title |
| 2 | **Inspection Code** | Enter a fictional unique business code |
| 3 | **Inspection Date** | Select the inspection date |
| 4 | **Asset** | Choose an existing **DC Asset** through its lookup picker |
| 5 | **Inspected By** | Choose an existing **DC Employee Profile** |
| 6 | **Inspection Status** | Select Planned, In Progress or Completed |
| 7 | **Inspection Result** | Select Pass, Attention, Fail or Not Assessed |
| 8 | **Finding Description** | Explain the observation |
| 9 | **Action Taken** | Describe the action or recommendation |
| 10 | **Follow-up Required** | Choose Yes or No |
| 11 | **Duration Minutes** | Enter the training duration |
| 12 | **Related Incident** | Optionally select an existing related incident |
| 13 | **Attachments** | Add a staged photo or supporting file where the tenant permits |

**Evidence upload:** When **Enable attachments** is selected on the Dataverse table, an Edit form can offer the **Attachments** field; the availability of this field still depends on your environment and form configuration. Choose **Edit fields → Add field → Attachments**, if shown. Keep the generated attachment card and its data binding unchanged. The file is not stored just because it was selected; **SubmitForm** saves the record and the staged file together. On Power Apps Mobile, the classic Attachments control accepts files one at a time. Use a **fictional/staged image or non-sensitive sample file**—never a real facility photo. If Attachments isn't available, verify table attachment enablement and refresh the Dataverse connection; do not substitute an unbound Add picture control and assume it saved to Dataverse. The attachment feature may depend on the tenant configuration and permissions.

For the form's existing card captions set **Font = `fontField`** and **Color = `clrMuted`** where supported. For **Classic inputs**, set **Font = `fontField`**, **Fill = `clrSurface`**, **Color = `clrText`**, **BorderColor = `clrBorder`** and **FocusedBorderColor = `clrSecondary`** when available. **Modern input and Combo box property names vary with the control version**: use the exposed text-color property (**FontColor** or **Color**) and the available palette/appearance properties, then confirm the dropdown's selected and unselected text is readable. A modern **Number Input** may not expose the same Font, Fill or text-color properties; style only the settings present in your designer (such as Size, BasePaletteColor, Appearance, border properties or AccessibleLabel) and retain its numeric binding. Do not replace a generated Number Input solely to force Comic Sans MS. For **Duration Minutes**, enter the number, press **Tab** or move focus away to commit it, then save and reopen the record to verify that 15 or 20 persists. Use the error-message color `clrDanger`. Set **AccessibleLabel** on inputs and attachment controls where available, and leave static shapes/labels without unnecessary behavior events. Keep **DataField**, **Update**, **Default**, **Required** and attachment control bindings as generated. The one-column form is taller than a phone's display; keep it scrollable and place Save/Cancel outside the scrollable cards.

Set `frmFieldInspectionEdit.OnSuccess`:

```powerfx
Set(varFieldSelectedInspection, frmFieldInspectionEdit.LastSubmit);
Set(varNewInspection, false);
Refresh('DC Field Inspections');
Notify("Inspection saved.", NotificationType.Success);
Navigate(scrFieldInspections, ScreenTransition.Fade)
```

Set `frmFieldInspectionEdit.OnFailure`:

```powerfx
Notify(
    Coalesce(frmFieldInspectionEdit.Error, "Inspection was not saved. Check required fields and evidence."),
    NotificationType.Error
)
```

**Create two fictional practice records** from the app. Select **New inspection**, complete the form, choose the actual Asset and Inspected By lookup records, and save. Do not import additional CSVs.

| Field | Practice inspection A | Practice inspection B |
| --- | --- | --- |
| Inspection Name | `UPS 001 Surface Review` | `Cooling Unit 002 Visual Check` |
| Inspection Code | `INSP-0001` | `INSP-0002` |
| Inspection Date | Today's date in the app | Today's date in the app |
| Asset | UPS 001 | Cooling Unit 002 |
| Inspected By | Noah Morales | Sana Kim |
| Inspection Status | Completed | Completed |
| Inspection Result | Pass | Attention |
| Finding Description | `No visible damage observed in the fictional inspection.` | `Synthetic inspection notes describe a cooling performance concern.` |
| Action Taken | `Recorded completed visual review.` | `Recommended follow-up review of cooling performance.` |
| Follow-up Required | No | Yes |
| Duration Minutes | 15 | 20 |
| Related Incident | Leave blank | Leave blank |
| Attachments | Optional staged sample image/file | Optional staged sample image/file |

After saving, select one inspection from `galFieldInspections` to reopen the edit form. Verify its Asset, inspector, status, result, notes and any attachment remain associated with the saved record. The attachment should be retrievable from the record if the tenant supports it.

**Checkpoint 6 — Inspection workflow.** The inspection gallery shows **two** records with distinct codes; opening one shows its saved fields, lookups and evidence where enabled. Text fields, buttons and record cards use the same black/slate/cyan/violet visual system and Comic Sans MS where available. The form can create and edit inspection records without duplicating the underlying Assets or Employees.

### S07.09 — Test, save and publish DC FieldOps

Use **Preview (Play/F5)** in Power Apps Studio, then test on an authorized phone with **Power Apps Mobile** where available. Browser preview is useful for formulas, but a mobile device is more representative for touch controls and its file picker.

| Test | Action | Expected result |
| --- | --- | --- |
| T01 | Open DC FieldOps | Portrait layout, pure-black canvas/header, violet divider, cyan buttons with black lettering, slate cards and readable Comic Sans MS text when available |
| T02 | Tap Browse incidents; search `INC-0002` | Existing incident appears |
| T03 | Open its details | Priority, status, asset and reporting employee are visible |
| T04 | Update Incident Status; save; restore original value | The change persists and the form reports success |
| T05 | Open Record inspection | Inspection list opens |
| T06 | Create `INSP-0001` and `INSP-0002` | Both records save, with valid Asset and Inspected By lookups |
| T07 | Add a staged attachment using the inspection form, where available | The saved record retains the attachment |
| T08 | Reopen and edit an inspection, then Cancel | Changes that weren't submitted are discarded |
| T09 | Check **App checker** | No blocking formula errors; examine delegation, form, accessibility and permission warnings |

Review **App checker → Accessibility** after configuring the forms: remove unused **OnSelect** formulas from static decorative shapes and labels, and set meaningful **AccessibleLabel** values for interactive inputs and the Attachments control. Performance notices involving cross-screen controls should also be reviewed; this lesson keeps form-mode changes on the destination screen's **OnVisible** event. Do not mistake a fictional **Inspected By** lookup for real user authentication. App visibility and button rules do not replace Dataverse security roles; access to the app and its Dataverse tables must be authorized for each real user.

Select **Save**, then **Publish → Publish this version**. Return to the solution and confirm **DC FieldOps** appears as a second Canvas App alongside **DC Operations Command Center**.

### Finish Part 07

Your solution now contains a **phone-oriented FieldOps Canvas App** using a fully black, cyan/violet/gold mobile theme and Comic Sans MS text where supported, plus a **DC Field Inspection** Dataverse table with three lookup relationships. The app can browse and update existing fictional incidents, create and edit inspections, record observations and follow-up decisions, and save supporting evidence through a supported Dataverse attachment form. Confirm the two sample inspection records persist after reopening the table and that the previous incident, asset and employee data remain intact.


---

## Part 08 — Automate Incident Updates and Inspection Follow-ups

The Operations Command Center and DC FieldOps apps now save real changes to fictional Dataverse records. Let's connect those changes to **two automated cloud flows**: an incident-status notification and a conditional inspection follow-up. Both flows belong to **SunnyVerse Data Center Operations 360** and send training messages only to a verified mailbox you control. They do not contact fictional employees or operate live infrastructure.

| Solution component | Role |
| --- | --- |
| `DC Automation Test Recipient` | Text environment variable containing the authorized test mailbox |
| `DC08 Incident Status Notice` | Email when the custom incident status is included in an update |
| `DC08 Inspection Follow-up Notice` | Email only when an updated inspection has Follow-up Required = true |
| Dataverse and Office 365 Outlook connection references | Link the solution flows to authorized connections |

### S08.01 — Create the test-recipient environment variable

Open [Power Automate](https://make.powerautomate.com), choose the same authorized environment, and select **Solutions → SunnyVerse Data Center Operations 360 → New → More → Environment variable**.

| Setting | Enter | Reason |
| --- | --- | --- |
| Display name | `DC Automation Test Recipient` | Readable shared configuration |
| Name / target schema | `svrg_DCAutomationTestRecipient` | Unambiguous reference in expressions |
| Data type | **Text** | An email address is a string |
| Description | `Authorized inbox for fictional DC360 training notifications.` | Documents appropriate use |
| Default value | Leave empty | Prevents accidental delivery after moving the solution |
| Current value | Choose **+ New value**, then enter **your verified authorized testing email** | Keeps the recipient specific to this environment |

If a help tip obscures the form, dismiss it before choosing **+ New value**. The current-value editor may not appear until you select that button. Save, reopen the variable and verify its current value. Do **not** commit a real email address or environment-specific values to GitHub.

Next check **Solutions → SunnyVerse Data Center Operations 360 → Objects** for **Connection references**. The upcoming flows need **Microsoft Dataverse** and **Office 365 Outlook**. When a trigger or action offers **Sign in**, complete the authorized connector sign-in prompt; the designer can create a new solution connection reference even if a connection already exists elsewhere in the environment. If a sign-in dialog seems to hang on **Creating…**, finish or close its authentication popup and reopen the flow. Select the successfully connected reference. Leave unrelated or unused references untouched; do not delete one without checking dependencies.

**Checkpoint 1 — Destination and connections.** The environment variable has the correct current value, and you can authorize Dataverse and Outlook in this solution. No test email has been sent yet.

### S08.02 — Build the Incident Status Notice flow

In the same solution choose **New → Automation → Cloud flow → Automated**. Name the flow **DC08 Incident Status Notice** and select **Microsoft Dataverse — When a row is added, modified or deleted**. The flow may open in either the **classic designer** (vertical action cards) or the new designer (property pane); configure the same trigger in either.

| Trigger setting | Value | Why |
| --- | --- | --- |
| Change type | **Modified** | Listen only to saved updates |
| Table name | **DC Incidents** | Existing incident records |
| Scope | **Organization** | Monitor permitted rows within this environment |
| Select columns | `svrg_incidentstatus` | Custom Incident Status logical column |
| Filter rows | Empty | Keep every incident eligible for this lesson |

**Check the logical column name:** Go to **Power Apps → DC Incident → Columns → Incident Status** and inspect its advanced properties. Use the actual lowercase logical name in **Select columns** (the classic designer uses this exact label). Do not use the display label, the custom column's formatted Choice label, or the Dataverse system `statuscode`. **Select columns** monitors whether the field occurs in the update request: it does not compare the old and new values. A repeated save with the same status may still start a run.

Select **+ New step → Office 365 Outlook → Send an email (V2)**. Complete the fields below:

| Outlook action property | Enter |
| --- | --- |
| To | The **DC Automation Test Recipient** solution environment-variable value |
| Subject | `[DC360 TRAINING] Incident status: ` followed by **Incident Code** dynamic content |
| Body line 1 | `Fictional incident notification — training only.` |
| Body line 2 | `Incident: ` + **Incident Name** dynamic content |
| Body line 3 | `Code: ` + **Incident Code** dynamic content |
| Body line 4 | `Current incident status: ` + the label expression shown below |
| Body line 5 | `Review this record using its incident code in DC Operations Command Center.` |
| Importance | **Normal** |

To reference the environment variable, choose it from **Dynamic content → Environment variables** if offered. The underlying expression is typically:

```text
parameters('DC Automation Test Recipient (svrg_DCAutomationTestRecipient)')
```

When pasted into a text/expression-enabled field, the designer may display the serialized inline form `@parameters('DC Automation Test Recipient (svrg_DCAutomationTestRecipient)')`. Use the designer's **Expression / fx** editor where appropriate rather than typing an address into an autocomplete **person chip**. Resolve a chip only if you intentionally want that literal email recipient; the environment-variable reference is preferred. Verify the resolved To value in the first controlled run.

For the **readable custom Choice label**, use this expression in the body's dynamic expression editor:

```text
triggerOutputs()?['body/_svrg_incidentstatus_label']
```

This trigger-specific label token was verified for the fictional Incident Status field in this lesson. It is different from the common OData formatted-value annotation, which may be empty in this trigger. Inspect the actual trigger output during testing if your connector version exposes a different token. The Choice numeric value and its human-readable label are not interchangeable.

In the **classic designer**, use the HTML/rich-text editor or **code view** for the email body if typing in the visual Body region does not persist. Ensure that the text or expressions are present after switching back. Choose **Save**, then return to the solution's **Cloud flows** list and reopen **DC08 Incident Status Notice** to prove it actually saved. A long **Saving…** indicator alone is not confirmation. If saving fails, inspect the flow checker, connection references, or try the other supported designer; do not assume the flow exists or create duplicates. Advanced authorized deployment methods are separate from this UI exercise.

**Checkpoint 2 — Saved flow.** The incident flow exists in the same solution, has a Dataverse Modified trigger, a single Outlook action, the correct custom logical column, and verified connection references.

### S08.03 — Test the incident notice and restore the record

To test an automated trigger, the flow must be **turned on**. Open its details, choose **Turn on** if it is off, and verify its status before editing a record. Only enable it for the controlled test window.

From DC Operations Command Center or DC Incident data, open `INC-0002` (initial **Incident Status = Assigned**), change the custom status to **In Progress**, and save. Reopen **Power Automate → DC08 Incident Status Notice → 28-day Run history** (the portal's run history, not the Dataverse `flowruns` table), inspect the latest run, and check the authorized test inbox. The message should contain the code and the readable **In Progress** label.

Now restore the same incident's status to **Assigned**, save, and verify the second run and email. In the sample Dataverse Choice used here, the numeric option values were verified as **In Progress = 479120002** and **Assigned = 479120001**. In the app, select the displayed label. Use numeric values **only** when an authorized interface explicitly requires the underlying Choice value, and check the actual Choice metadata rather than assuming these numbers apply to a different environment.

| What to check | Expected outcome |
| --- | --- |
| Run history | A completed run for each intentional status update |
| Email To | Only the approved test inbox |
| Email content | `INC-0002` and a nonblank readable status label |
| Dataverse record | Restored to **Assigned** |
| Flow status after testing | **Off**, until ongoing operation is expressly approved |

**Checkpoint 3 — Incident test.** The run history and inbox confirm successful messages, `INC-0002` is restored, and the flow is switched **Off** after testing.

### S08.04 — Build the conditional Inspection Follow-up Notice

Create another solution-aware automated cloud flow named **DC08 Inspection Follow-up Notice** with the same Dataverse trigger.

| Trigger setting | Value |
| --- | --- |
| Change type | **Modified** |
| Table name | **DC Field Inspections** |
| Scope | **Organization** |
| Select columns | `svrg_followuprequired` (verify its column logical name) |
| Filter rows | Leave blank |

Choose **+ New step → Control → Condition**. The decision is based on a **Boolean**, not the visible words Yes/No.

| Condition | Configure |
| --- | --- |
| Left operand | **Follow-up Required** from Dataverse trigger |
| Operator | **is equal to** |
| Right operand | Boolean **true** from the **Expression / fx** selector |
| If yes | **Office 365 Outlook → Send an email (V2)** |
| If no | No action; end silently |

Equivalent Condition expression:

```text
equals(triggerBody()?['svrg_followuprequired'], true)
```

Inside **If yes**, set Outlook **To** to the same **DC Automation Test Recipient** environment variable. Set the subject to `[DC360 TRAINING] Inspection follow-up: ` plus **Inspection Code**. In the body include a training-only heading, **Inspection Name**, **Inspection Code**, **Finding Description**, **Action Taken**, and a line saying **Follow-up Required: Yes**. Use dynamic content from the triggering row, not typed placeholder names.

For a readable **Inspection Status** Choice label, use the environment-verified token:

```text
triggerOutputs()?['body/_svrg_inspectionstatus_label']
```

Insert this token with the Expression editor. Do not rely on an empty generic OData formatted-value annotation. Leave **If no** empty. Save, reopen the actual saved flow, and verify the Outlook connection reference belongs to the solution. If your designer prompts for **Sign in** rather than selecting an existing connection, complete the authorized sign-in and check the resulting solution reference.

**Checkpoint 4 — Inspection flow.** The saved flow has one Modified trigger, one Boolean Condition, one Outlook action inside **If yes**, no action in **If no**, and the approved recipient configured.

### S08.05 — Test the inspection's No and Yes branches

Turn **DC08 Inspection Follow-up Notice** **On** only for this controlled test. Open `INSP-0002` in DC FieldOps. Its original **Follow-up Required** value is **Yes**.

| Test step | Expected result |
| --- | --- |
| Set **Follow-up Required = No**, save | Trigger runs; the **If no** branch sends no email |
| Set **Follow-up Required = Yes**, save | Trigger runs; the **If yes** branch sends one email |
| Check the portal's **28-day Run history** | Both run records and the actual branch results are visible |
| Check mailbox and Body labels | Test message identifies `INSP-0002` and has nonblank Choice text if a status label is included |
| Reopen the inspection | Follow-up remains **Yes**, restoring the practice record |
| Finish | Turn the inspection flow **Off** |

The trigger may run for either update request because the selected field is included. The Condition determines whether email is sent. Use the actual Boolean expression `true` rather than the string `"Yes"`.

**Checkpoint 5 — Both branches.** No email for the No case, one email for the Yes case, original inspection state restored, and the second flow is **Off** after testing.

### S08.06 — Inspect the solution components and run history

Go to **Solutions → SunnyVerse Data Center Operations 360 → Objects**. Confirm that the environment variable, both cloud flows, and the **Dataverse** and **Office 365 Outlook connection references actually used by the flows** belong to the solution. A new connector sign-in can create a reference in another solution; add the used references to this solution when absent. Do not delete a leftover unused connection reference without reviewing its dependencies.

| Review | Where to check | Why it matters |
| --- | --- | --- |
| Flow presence | Solution → Cloud flows | A designer canvas alone doesn't prove Save succeeded |
| Trigger | Edit flow → Dataverse card | Correct table, Modified, Scope and selected scalar column |
| Outlook action | Edit flow → Send an email (V2) | Approved recipient and full message body |
| Choice text | Portal run history → trigger output and email | `_svrg_incidentstatus_label` / `_svrg_inspectionstatus_label` contain readable values |
| Condition | Inspection run → Condition inputs/outputs | Boolean true/false, not a text label |
| Connection references | Solution → Objects / Connection references | References are included with the flows for solution portability |
| Mail delivery | Authorized test inbox | No unintended recipients |
| Enabled state | Flow details | Both flows remain **Off** outside approved test windows |

Use the **Power Automate portal's flow details → 28-day Run history** for these tests. A separate Dataverse `flowruns` table may not contain records immediately and is not the primary confirmation route here. A success result refers to that flow run; it is not evidence of permanent exactly-once behavior. Changing a row to the value it already has may still generate a new Modified trigger run.

If a flow fails, open the failed step in portal run history and inspect its action error, connector authentication, input recipient and dynamic expressions. If the Body is blank in a classic designer, verify it in code view and re-save. For large data imports or repetitive test edits, keep both notification flows **Off**.

### S08.07 — Finish Part 08

In the solution, confirm **one** test-recipient environment variable, **two** correctly configured automated cloud flows and their **used** connection references. Confirm successful incident and inspection runs in the portal and recipient inbox, then verify `INC-0002` is back to **Assigned** and `INSP-0002` is back to **Follow-up Required = Yes**. Leave both flows **Off** until a deliberate decision to enable recurring notifications.

You have connected the two existing apps and Dataverse records to controlled, auditable training notifications without creating new tables or flows that write back to incident or inspection data.


---

## Part 09 — Build the Asset and Maintenance Manager

The fictional data center already has 100 assets, 200 incidents, employee profiles and inspection records. Now we'll add a work-order register and use a **model-driven app** to manage preventive work, corrective repairs, assignments, planned dates and completion evidence. Model-driven apps build forms, views and table navigation directly from Dataverse metadata, so this lesson doesn't require a new Canvas App or hand-written Power Fx.

The target is **DC Asset & Maintenance Manager**, a maintenance workspace backed by a new **DC Work Order** table. We'll use the [500-row work-order practice dataset](./data/work-orders.csv), whose Asset, Assigned Engineer and Related Incident values refer to existing fictional records. We'll also configure a focused read-only Asset Context form so that opening an Asset lookup reveals meaningful equipment information.

| Component | Result |
| --- | --- |
| `DC Work Order` Dataverse table | Work-order identity, scheduling, lifecycle and relationships |
| 500 fictional work-order records | Repeatable synthetic maintenance data with lookup references |
| Maintenance Main form and Asset Context form | Work-order fields in logical sections and readable equipment context |
| Work-order system views | All, Active, Overdue and Unassigned queues |
| `DC Asset & Maintenance Manager` model-driven app | Navigation across Work Orders, Assets, Incidents and Inspections |

### S09.01 — Create the DC Work Order table

Open [Power Apps](https://make.powerapps.com) in the authorized environment, then **Solutions → SunnyVerse Data Center Operations 360 → New → Table**. Configure the advanced properties before creating the table.

| Table property | Enter |
| --- | --- |
| Display / plural names | `DC Work Order` / `DC Work Orders` |
| Description | `Synthetic data center maintenance work orders for planning and completion tracking.` |
| Table type | **Standard** |
| Record ownership | **Organization** |
| Primary name column | `Work Order Name` |
| Primary column description | `Readable name of a fictional maintenance task.` |
| Primary name format / maximum | Single-line Text / 200 characters |
| Table schema target | `svrg_DCWorkOrder` |
| Primary name schema target | `svrg_WorkOrderName` |
| Notes and attachments | **On**, if available, for optional supporting evidence; verify after creation |
| Activity / routing flags | Leave off unless an authorized tenant requirement calls for them |

Create the table, then **reopen its Properties / Advanced options** to confirm **Notes** is really **On**. If the setting did not persist during creation, turn it on in the saved table's settings and save again. Reopen **Schema → Columns → Work Order Name** and verify **Requirement = Business required**; if it displays **Optional**, change it to Business required and save the existing primary column. Do not make a second primary-name column. Leave the generated Dataverse GUID intact.

**Checkpoint 1 — Table shell.** The solution contains one **DC Work Order** table with the correct primary name and publisher prefix. Confirm *after reopening* that Notes is On and Work Order Name is Business required.

### S09.02 — Add exact work-order business columns and Choices

Open **DC Work Order → Schema → Columns → New column** for each row below, saving one at a time. **Work Order Name** is already present. Use the exact display names shown because [work-orders.csv](./data/work-orders.csv) uses those headers. Schema names below are target names; verify what your environment actually saves.

| Display name / target schema | Description | Data type | Required | Additional properties |
| --- | --- | --- | --- | --- |
| **Work Order Name** / `svrg_WorkOrderName` | Human-readable task title | Primary Text | Business required | Created with table; max 200; not duplicated |
| **Work Order Code** / `svrg_WorkOrderCode` | Stable fictional work-order identifier | Text single line | Business required | Format Text; max 24; Searchable Yes; no default |
| **Work Order Type** / `svrg_WorkOrderType` | Category of maintenance activity | **Local Choice** single select | Business required | Preventive Maintenance, Corrective Repair, Inspection Follow-up, Emergency Response; no default; Searchable Yes |
| **Work Order Priority** / `svrg_WorkOrderPriority` | Relative urgency of maintenance | **Local Choice** single select | Business required | Critical, High, Medium, Low; no default; Searchable Yes |
| **Work Order Status** / `svrg_WorkOrderStatus` | Lifecycle stage | **Local Choice** single select | Business required | Planned, Assigned, In Progress, On Hold, Completed, Cancelled; no default; Searchable Yes |
| **Work Description** / `svrg_WorkDescription` | Work instructions written for this synthetic exercise | Multiline Text | Business required | Plain text; up to 2,000 characters; no default |
| **Requested On** / `svrg_RequestedOn` | Time the maintenance task was requested | Date and Time | Business required | User local behavior; date and time; no default |
| **Due On** / `svrg_DueOn` | Planned completion deadline | Date and Time | Optional | User local; no default |
| **Estimated Minutes** / `svrg_EstimatedMinutes` | Planned labor duration | Whole Number | Optional | 0–1,440; Format None; no default |
| **Safety Review Required** / `svrg_SafetyReviewRequired` | Marks work needing an additional human safety review | Yes/No | Optional | Labels Yes/No; default No |
| **Completed On** / `svrg_CompletedOn` | When work was recorded complete | Date and Time | Optional | User local; no default |
| **Actual Minutes** / `svrg_ActualMinutes` | Actual time logged in training | Whole Number | Optional | 0–1,440; Format None; no default |
| **Completion Notes** / `svrg_CompletionNotes` | Synthetic completion commentary | Multiline Text | Optional | Plain text; up to 2,000 characters; no default |

For each **Local Choice**, open **Data type → Choice** and keep it local to the current column. Where the designer shows **Sync with global choice**, switch it **Off**, then enter the labels in exactly the listed order. These are three independent local Choices. Their **numeric values are separate per column**, even if the numbers overlap. In this project's verified environment, the first option in each local Choice is **479120000**, then each successive option increments by one. This gives **Work Order Type** 479120000–479120003, **Work Order Priority** 479120000–479120003 and **Work Order Status** 479120000–479120005 in their respective label orders. **Always inspect the actual saved Choice metadata before an API import**; publisher settings and prior customization can yield different values in another solution or environment. No custom numbers need to be invented for a designer-based import.

For **Work Order Code**, open **Schema → Keys → New key** after saving the column, name it `DC Work Order Code Key`, and select **Work Order Code**. Choose Save. The key may initially show **Pending**, because Dataverse builds the index asynchronously. Refresh the Keys list until the key reaches **Active** before importing; do not treat Pending as a failed key or run an upsert while it is not ready. An alternate key enforces unique codes and supports idempotent upsert workflows.

**Checkpoint 2 — Column definitions.** Verify **one primary-name column plus 12 actual nonlookup business columns**. Dataverse may also display generated virtual **…name** columns for Choice or Yes/No labels; those are metadata companions, not extra fields to recreate. Check every Choice's labels and numeric values, the Business required setting on the primary name, and the Work Order Code alternate key's **Active** state.

### S09.03 — Add Asset, employee, Incident and Inspection relationships

Go to **DC Work Order → Schema → Relationships → New relationship → Many-to-one**. For each row, the current table is **DC Work Order**, and the related table is the pre-existing target. Creating the relationship creates a Lookup column; do not add a duplicate text or Lookup column afterward.

| Lookup display name / target schema | Related table | Description | Requirement / settings |
| --- | --- | --- | --- |
| **Asset** / `svrg_Asset` | **DC Asset** | Equipment receiving the maintenance work | **Business required**, Searchable Yes |
| **Assigned Engineer** / `svrg_AssignedEngineer` | **DC Employee Profile** | Fictional employee responsible for the task | Optional, Searchable Yes |
| **Related Incident** / `svrg_RelatedIncident` | **DC Incident** | Existing incident from which the task originated | Optional, Searchable Yes |
| **Related Inspection** / `svrg_RelatedInspection` | **DC Field Inspection** | Inspection that may have requested maintenance | Optional, Searchable Yes |

For each relationship, set **Delete = Restrict** and **Assign, Share, Unshare, Reparent and Merge = No cascade**, where the operation is exposed and supported. If the designer offers a **Referential** preset, inspect its individual settings before saving; use the **Configure cascading** options when needed. The goal is to prevent accidental parent deletion and unrelated updates to child work orders. Confirm the actual **Lookup** type and target table under Columns. Existing Asset Name, Employee Name, Incident Name and Inspection Name values are human-readable references, not GUIDs.

**Checkpoint 3 — Relationships.** Exactly four new Lookups exist on DC Work Order. Asset is required; other references are optional. Existing tables haven't been recreated or changed.

### S09.04 — Import the 500 fictional work orders and verify references

Download [**work-orders.csv**](./data/work-orders.csv) from this repository. It has **500 work-order rows** (codes `WO-0001` through `WO-0500`), **17 exact display-name headers**, and fictional references to the 100 assets and existing employee/incident records. This is sample data only.

| Import group | CSV columns | Treatment |
| --- | --- | --- |
| Text / Choice / date / numbers | Work Order Name, Work Order Code, Work Order Type, Work Order Priority, Work Order Status, Work Description, Requested On, Due On, Estimated Minutes, Safety Review Required, Completed On, Actual Minutes, Completion Notes | Map to their matching display-name columns; map each local Choice label to an existing option |
| Required lookup | **Asset** | Resolve against **DC Asset → Asset Name** |
| Optional lookup | **Assigned Engineer** | Resolve against **DC Employee Profile → Employee Name**; leave blank source cells blank |
| Optional lookup | **Related Incident** | Resolve against **DC Incident → Incident Name**; leave blank source cells blank |
| Optional lookup | **Related Inspection** | Resolve against **DC Field Inspection → Inspection Name**; empty in this starting dataset |

**Resolve the relationships before committing imports.** Open **DC Work Order → Data → Import** and choose an authorized CSV import surface that supports reference mapping, or use an approved Dataverse import/API process that resolves existing row identifiers first. For every CSV nonblank **Asset**, **Assigned Engineer** and **Related Incident** cell, match the displayed name to **exactly one** existing Dataverse row and use its GUID as the lookup target. Keep **Related Inspection** blank for this dataset. Do not pass plain names into GUID-typed lookup fields; some simplified designers cannot perform reference resolution even when the CSV headers match. A supported alternate-key **upsert** keyed on **Work Order Code** is useful when the interface supports it. It must update the five trial rows rather than inserting them again. **Do not** weaken the Asset relationship or replace lookups with text to force a file through. If API tools are used, use only the authorized connection and verify the correct entity-set names and `@odata.bind` syntax from actual Dataverse metadata.

The CSV uses ISO 8601 **UTC timestamps** (for example `2026-07-01T12:00:00Z`). Dataverse should store the UTC instant as supplied, while a user-local form may display another clock hour; the test environment's form can display **12:00 PM** when its user time-zone setting is UTC. Compare the actual stored instant and the user's configured time zone rather than assuming a Pacific display time. Map durations as numbers and Choice labels to their saved option values, not arbitrary integers.

**Before running the complete file**, validate lookup mapping and data types with a **five-row test in a nonduplicating preview or controlled import**. If the wizard inserts the five test rows, the full import must **skip or update those five by Work Order Code**, never create them again. Review the selected import mode and existing records before proceeding. In the finished table, filter by work-order code and confirm exactly one `WO-0001` and one `WO-0500`. Check `WO-0001` points to **UPS 001**, and inspect a record with a related Incident.

| Post-import validation | Expected result |
| --- | --- |
| Record count | **500** unique work-order codes after a successful full import |
| Asset references | All 500 Work Orders resolve to an existing DC Asset |
| Employees | Nonblank Assigned Engineer lookups resolve to fictional employee profiles |
| Incident links | Nonblank Related Incident lookups resolve to existing DC Incidents |
| Choice fields | All labels mapped to existing Work Order Type / Priority / Status options |
| Completed work | Completed On, Actual Minutes and Completion Notes appear on Completed rows |
| Invalid relationships | No unresolved lookup names and no duplicate records |

If imports are blocked by licensing, permissions or lookup mapping, finish the app design with a small manually created set of **uniquely named training records** while leaving the unresolved bulk import unclaimed. Avoid importing the same rows twice.

**Checkpoint 4 — Work-order data.** The table contains 500 valid linked records if the import succeeded. Otherwise, record the exact import limitation and use only validated manual test records; do not report 500 as loaded without checking.

### S09.05 — Create a maintenance Main form with sections

Open **DC Work Order → Forms → New form → Main form**, and name it **DC Work Order — Maintenance Main**. Use the modern model-driven form designer to create readable sections. You will configure **Dataverse columns**, not add Canvas control names or Power Fx formulas.

| Form area | Columns to place | Reason |
| --- | --- | --- |
| **Identity & Priority** (two columns) | Work Order Name, Work Order Code, Work Order Type, Work Order Priority, Work Order Status | Find, classify and prioritize work quickly |
| **Asset & Assignment** (two columns) | Asset, Assigned Engineer, Requested On, Due On, Estimated Minutes | Establish equipment context, owner and schedule |
| **Execution & Safety** (two columns) | Safety Review Required, Completed On, Actual Minutes | Track execution and safety review markers |
| **Work Description & Completion Notes** (one column) | Work Description, Completion Notes | Allow multiline instructions and outcomes to use the full width |
| **Related Context** (two columns) | Related Incident, Related Inspection | Connect maintenance work to initiating records |

In the **Form designer → Sections / Components**, create four sections with the column widths specified in the revised layout table: two-column sections for short fields and a separate **one-column** section for **Work Description** and **Completion Notes**. Drag each field into its section only once. Keep Work Order Code, the required Asset lookup and the custom Work Order Status visible without excessive scrolling. Do not mistake system `Status` / `Status Reason` for the custom Work Order Status. The default generated **Information** form may remain in the table; choose **Maintenance Main only** as the work-order form exposed through this app.

Use the built-in model-driven controls for Choices, Lookups, numbers and date/time values. These inherit the model-driven app's supported Fluent/theme settings and do not expose the same `Fill`, `Font` or `OnSelect` properties as Canvas controls. **Do not attempt to force Comic Sans MS or custom per-field colors into the model-driven designer.** Give the form concise labels, clear sections and readable column widths instead.

Choose **Save and publish** for the form, then return to **DC Work Order → Forms** and confirm the new main form is present.

**Add an Asset Context form for meaningful lookup navigation.** Open the existing **DC Asset → Forms → New form → Main form**, name it **DC Asset — Maintenance Context**, and add existing columns **Asset Name, Asset Code, Asset Category, Criticality, Operational Status, Data Hall, Manufacturer, Model Number, Serial Number, Rated Power kW, Install Date**. Use two columns for short identifiers and one column for longer descriptions if needed. **Do not alter or delete the original Asset Information form**. Save and publish the new context form. Later, select it for the **DC Assets** page of this maintenance app so that a clicked Asset lookup shows meaningful information. This is a context view; it does not create new asset records.

**Checkpoint 5 — Maintenance forms.** The work-order form displays all the fields in their proper sections and the separate Asset Context form shows asset identity and properties; no pre-existing forms were deleted.

### S09.06 — Create operational system views

Open **DC Work Order → Views → New view**. Add the four public/system views below. For each view choose the listed fields under **Edit columns / Add view column**, arrange them in the stated order, add filters, then **Save and publish**. These are Dataverse views usable by multiple app users, not a Canvas gallery.

| View | Columns in display order | Filter |
| --- | --- | --- |
| **DC All Work Orders** | Work Order Code, Work Order Name, Work Order Priority, Work Order Status, Asset, Assigned Engineer, Due On | None; sort Due On ascending where sensible |
| **DC Active Work Orders** | Work Order Code, Work Order Name, Work Order Status, Work Order Priority, Asset, Due On | Work Order Status is not **Completed** AND not **Cancelled** |
| **DC Overdue Work Orders** | Work Order Code, Work Order Name, Due On, Work Order Status, Asset, Assigned Engineer | Due On **older than 1 minute**, Due On **contains data**, Status not Completed AND not Cancelled |
| **DC Unassigned Work Orders** | Work Order Code, Work Order Name, Work Order Priority, Asset, Due On | Assigned Engineer **does not contain data** |

Some view designers do not expose a continually updating **before Today** operator for Date and Time. In that case choose the **relative** date condition **Older Than 1 Minute** with **Due On contains data** and exclude Completed/Cancelled records. This identifies work due more than one minute ago, a practical approximation of passed deadlines. It differs slightly from 'before today' and may exclude items due in the last minute. Confirm filters are combined with **AND**. Sort **Due On ascending in all four views** for consistent queue ordering. Since the fields use **User local** behavior, displayed times may differ across users.

If the form/view editor offers a **model-driven Power Apps grid control**, keep its built-in accessibility and editing behavior; do not depend on legacy deprecated grid controls. A view lists records but does not override Dataverse security roles.

**Checkpoint 6 — Queues.** All four views are saved and published. The All view shows records; the Active, Overdue and Unassigned views filter appropriately against the data actually loaded.

### S09.07 — Assemble the model-driven maintenance app

Inside the same solution choose **New → App → Model-driven app** and enter:

| App property | Value |
| --- | --- |
| Name | **DC Asset & Maintenance Manager** |
| Description | `Manage fictional equipment work orders and maintenance context in Dataverse.` |
| Publisher/solution | Existing **SunnyVerse Data Center Operations 360** solution |
| App type | Model-driven, standard modern designer |

In the app designer choose **Add page → Dataverse table** (or the current **Table-based view and form** option) and add these **existing** tables. Do not create another copy of them.

| Navigation group | Page / table | Purpose |
| --- | --- | --- |
| **Maintenance** | **DC Work Orders** | Open work-order views and the Maintenance Main form |
| **Maintenance** | **DC Field Inspections** | See field findings that may motivate work |
| **Equipment & Context** | **DC Assets** | Inspect asset registry and existing relationships |
| **Equipment & Context** | **DC Incidents** | See originating incident context |

Set the navigation labels and ordering using the current **Pages / Navigation** editor. For **DC Work Orders**, explicitly select **DC Work Order — Maintenance Main** and the four published work-order views **In this app**; keep the default generated **Information** form out of this app's Work Orders page. For **DC Assets**, select **DC Asset — Maintenance Context** to display the asset properties when a linked record opens. Existing forms and views of other tables remain available unless your app requires a specific selection. An app-designer warning that a table has no explicitly selected forms/views means all eligible components might be exposed; review the page component selections before accepting that warning. This setup does not require deleting default forms. Save, **Publish**, and **Play** the app.

This is a **model-driven** application: it uses the environment's supported user interface theme, lookups, views and form metadata. Unlike the Canvas apps, it is not appropriate to apply arbitrary `ColorValue` formulas or raw CSS to its navigation. You can use supported app icon/description settings if offered without modifying the environment-wide theme.

**Checkpoint 7 — Navigation.** The new app opens with Work Orders, Inspections, Assets and Incidents in the intended groups. Work Orders opens the published main form and operational views. The two Canvas Apps remain separate and unchanged.

### S09.08 — Walk through a real maintenance workflow

In **DC Asset & Maintenance Manager → DC Work Orders → DC All Work Orders**, open `WO-0001` if the 500-row import completed. Confirm its **Asset = UPS 001**, its **Work Order Type = Preventive Maintenance**, and its original **Work Order Status = Planned**. This record is part of the fictional practice data.

| Exercise | Expected result |
| --- | --- |
| Open `WO-0001` | Work Order Code, Type, Priority, Asset and Requested/Due dates are visible |
| Select the Asset Lookup | Opens the existing **DC Asset — Maintenance Context** form with asset identifiers; no new asset is created |
| Change Work Order Status from Planned to **Assigned**, save | The form persists the custom Choice value; if a mouse click doesn't commit a Choice dropdown selection, use keyboard navigation, Tab or Enter and confirm the displayed value before saving |
| Reopen the record | Status is **Assigned**, and the work order appears in an appropriate active queue |
| Change status back to **Planned**, save | Practice record is restored |
| Open **DC Unassigned Work Orders** | Rows with no Assigned Engineer are visible if present |
| Open **DC Overdue Work Orders** | Results reflect due dates and the current local date; no fixed count expected |

To practice creating a row, choose **New** and enter a new code outside the published `WO-0001`–`WO-0500` range (for example, `WO-TRAIN-01`), choose an existing Asset, enter required classifications and description, then Save. Reopen it, confirm the relationships, and either retain it as an explicitly labeled test record or remove **only that authorized test row** if your environment permits deletion and you intend to keep the original 500-row count. The 500-row baseline should not be claimed after adding extra tests unless you filter them out.

Model-driven form-level input is not automatic approval. The **Safety Review Required** field is a tracking flag, not a safety permit. Closing a fictional work order does not change actual equipment state or dispatch a technician. If the published app displays **Some components of this app require you to sign in**, verify that the current user can access Work Orders, Assets, Incidents and Inspections and check relevant connection authorization rather than treating a banner as proof of failure or dismissing a blocked component.

**Checkpoint 8 — Maintenance workflow.** Work-order edit, lookup navigation, custom Status, view filtering and data persistence work using the original Dataverse tables. No real equipment actions or unintended notifications occur.

### S09.09 — Final validation, publication and handoff

| Check | Validation |
| --- | --- |
| Data model | One DC Work Order table, three Local Choices, four actual Lookups and unique Work Order Code key |
| Dataset | [work-orders.csv](./data/work-orders.csv) has 500 synthetic rows; verify actual imported count separately |
| Forms | Maintenance Main form shows all work-order fields and Asset Context form shows meaningful asset details |
| Views | All, Active, Overdue and Unassigned work-order views function |
| App | One published **DC Asset & Maintenance Manager** model-driven app in the existing solution |
| Records | Existing Assets, Incidents, Inspections and Employees still resolve correctly |
| Validation | Required Asset/Code/Status values and unique code behavior are enforced |
| Security | Actual app and Dataverse table access requires the appropriate tenant roles |
| Operations | Other solution flows remain in their intended enabled/disabled states; check for unintended extra enabled flows before exercising related data |

Open **App designer → Save**, **Publish**, then **Play** after confirming the form/view changes were also published. Check for unresolved component warnings. Verify that model-driven users are not granted access merely because they can see the public GitHub instructions.

### Finish Part 09

You now have a **Dataverse Work Order register** and **DC Asset & Maintenance Manager** model-driven app for fictional maintenance planning and execution. Its linked work orders, operational system views and published forms reuse the Asset, Incident, Employee and Inspection tables already built. The supplied [work-orders.csv](./data/work-orders.csv) provides 500 deterministic synthetic practice rows; their successful import and lookup resolution must be verified in the learner's own authorized environment.



---

## Part 10 — Build Change, Risk and Maintenance Procedure Approvals

A maintenance work order describes *what* needs to be done. A planned operational change also needs a clear impact assessment, a method of procedure (MOP), a rollback strategy and an explicit review decision. In this lesson, we'll create three related Dataverse tables, assemble **DC Change & Risk Manager** as a model-driven app, and test one approval flow with original fictional records.

The approval is **training-only**. An Approved status records a fictional administrative decision, not a work permit or permission to operate physical infrastructure. Every event and approval must be checked: triggers can be delayed or missed and a flow waiting for a response can queue subsequent runs. Use only an authorized environment and a real test approver you control.

| New component | What it records |
| --- | --- |
| `DC Change Request` | Change identity, timing, scope, work-order context, MOP readiness and approval state |
| `DC Risk Register` | Likelihood, impact, mitigation, risk owner and related change |
| `DC MOP Step` | Ordered procedure steps and expected verification |
| `DC Change & Risk Manager` | Model-driven app with forms, views and linked records |
| `DC10 Change Approval` | One controlled approval flow, with an authorized real test approver |

All references to Assets, Work Orders and Employee Profiles use existing records. There is **no CSV import** in this lesson; the small sample set is entered and checked through the forms.

### S10.01 — Create the DC Change Request table

Open [Power Apps](https://make.powerapps.com), choose the authorized environment, then **Solutions → SunnyVerse Data Center Operations 360 → New → Table**. Use the current table designer's advanced properties to enter:

| Table property | Value |
| --- | --- |
| Display / plural | **DC Change Request** / **DC Change Requests** |
| Description | `Fictional operational changes with review, rollback and approval fields.` |
| Type / ownership | Standard / **Organization** |
| Primary name | **Change Name** |
| Primary-name description | `Readable training change title.` |
| Table target schema | `svrg_DCChangeRequest` |
| Primary-name target schema | `svrg_ChangeName` |
| Notes and attachments | **On** if supported, for optional staged evidence |
| Activity / routing | Keep default Off unless required by the authorized environment |

After creating and saving the table, **reopen Properties → Notes** and verify **On**. If the original creation setting was not retained, switch Notes on in the saved table, save and verify again. Then reopen **Columns → Change Name → Required** and verify **Business required**. Correct it on the existing primary column if Optional appears. Never create a second primary name or alter the generated GUID.

Add the following columns through **Schema → Columns → New column**. For each Choice, use **Choice, single select, local to this column**. If you see **Sync with global choice**, switch it **Off**. Enter the labels in the stated order and inspect the saved option values before using them in a flow.

| Display name / target schema | Description | Data type / required | Format, options and other properties |
| --- | --- | --- | --- |
| Change Name / `svrg_ChangeName` | Readable change title | Primary Text / Business required | Created with table; max 200 |
| Change Code / `svrg_ChangeCode` | Unique training change identifier | Text / Business required | Max 24, Searchable Yes, no default |
| Change Type / `svrg_ChangeType` | Class of change | Local Choice / Business required | Maintenance, Standard, Emergency; no default |
| Change Status / `svrg_ChangeStatus` | Review and execution lifecycle | Local Choice / Business required | Draft, Submitted, Under Review, Approved, Rejected, Scheduled, Implemented, Cancelled; no default |
| Business Impact / `svrg_BusinessImpact` | Anticipated effect of the fictional change | Local Choice / Business required | Low, Moderate, High, Critical; no default |
| Reason for Change / `svrg_ReasonForChange` | Why the change is proposed | Multiline Text / Business required | Max 2,000 characters |
| Planned Start / `svrg_PlannedStart` | Proposed start of fictional window | Date and Time / Business required | User local behavior |
| Planned End / `svrg_PlannedEnd` | Proposed end of fictional window | Date and Time / Business required | User local behavior |
| MOP Summary / `svrg_MOPSummary` | Overview of documented procedure | Multiline Text / Business required | Max 2,000 |
| Backout Plan / `svrg_BackoutPlan` | How the team would reverse the fictional change | Multiline Text / Business required | Max 2,000 |
| Verification Plan / `svrg_VerificationPlan` | How to establish success during the simulation | Multiline Text / Business required | Max 2,000 |
| Safety Review Required / `svrg_SafetyReviewRequired` | Flags need for separate human safety review | Yes/No / Optional | Default No |
| MOP Reviewed / `svrg_MOPReviewed` | Human confirms documentation is ready for approval | Yes/No / Optional | Default No |
| Approval Requested / `svrg_ApprovalRequested` | One-time submission gate for the training flow | Yes/No / Optional | Default No |
| Approval Decision Note / `svrg_ApprovalDecisionNote` | Text from the decision process or summary | Multiline Text / Optional | Max 2,000; no default |
| Decision On / `svrg_DecisionOn` | Date and time decision recorded | Date and Time / Optional | User local; no default |

After **Change Code** is saved, open **Schema → Keys → New key**, choose just **Change Code** and name the key **DC Change Code Key**. Refresh the Keys list until the alternate key becomes **Active**; it may remain **Pending** for several minutes. Do not create a duplicate key or insert potentially duplicate sample codes while its index is building.

**Checkpoint 1 — Change schema.** There is one DC Change Request table, one required primary name, 15 additional business columns, three local Choices, and an Active Change Code alternate key. Generated hidden Choice-label metadata columns are not extra fields to recreate.

### S10.02 — Create the DC Risk Register table

In the same solution create a second Standard / Organization-owned table:

| Table property | Value |
| --- | --- |
| Display / plural | **DC Risk Register** / **DC Risk Registers** |
| Primary name | **Risk Name**, Business required |
| Primary description | `Readable title of a fictional operational risk.` |
| Table schema target | `svrg_DCRiskRegister` |
| Primary schema target | `svrg_RiskName` |
| Table description | `Fictional operational risk assessments linked to assets and change records.` |
| Notes | Optional; not needed for this lesson |

After creation, reopen **Risk Name** and verify **Business required**; correct Optional to Business required if necessary. Reopen table Properties to check the saved description and Notes settings. Then add the following columns:

| Display name / target schema | Description | Type / required | Properties |
| --- | --- | --- | --- |
| Risk Name / `svrg_RiskName` | Readable risk description | Primary Text / Business required | Created with table |
| Risk Code / `svrg_RiskCode` | Unique risk identifier | Text / Business required | Max 24; Searchable Yes |
| Risk Category / `svrg_RiskCategory` | Domain at risk | Local Choice / Business required | Electrical, Mechanical & Cooling, IT Infrastructure, Facilities, Safety, Other |
| Likelihood / `svrg_Likelihood` | Qualitative frequency of a simulated event | Local Choice / Business required | Rare, Unlikely, Possible, Likely, Almost Certain |
| Impact / `svrg_Impact` | Potential fictional consequence | Local Choice / Business required | Minor, Moderate, Major, Critical |
| Risk Score / `svrg_RiskScore` | Numerical likelihood × impact for training | Whole Number / Business required | Minimum 1; maximum 20; no default |
| Risk Response / `svrg_RiskResponse` | How this risk is to be handled | Local Choice / Business required | Mitigate, Avoid, Accept, Transfer |
| Risk Status / `svrg_RiskStatus` | Current risk tracking state | Local Choice / Business required | Open, Mitigating, Closed |
| Risk Description / `svrg_RiskDescription` | What might occur | Multiline Text / Business required | Max 2,000 |
| Mitigation Plan / `svrg_MitigationPlan` | Proposed action to reduce the fictional risk | Multiline Text / Business required | Max 2,000 |
| Review Date / `svrg_ReviewDate` | Next review date | Date Only / Optional | Date-only behavior |
| Safety Related / `svrg_SafetyRelated` | Marks risk requiring human safety attention | Yes/No / Optional | Default No |

Use independent **Local Choices**, not new Global Choices. Verify saved option numbers in each column's metadata when a process requires numeric values. In this publisher setup, Risk Status can use Open = **479120000**, Mitigating = **479120001**, Closed = **479120002**; another configuration may differ. For the training Risk Score, assign Likelihood ranks 1–5 and Impact ranks 1–4 in listed order, then multiply manually: Unlikely (2) × Major (3) = **6**. The form does not calculate or validate this automatically. Create **DC Risk Code Key** on Risk Code, refresh and wait until it becomes **Active**; Pending is not Active.

**Checkpoint 2 — Risk schema.** One DC Risk Register table has the stated fields, choices and Active Risk Code key. The score is clearly labeled as a training assessment, not a real safety rating.

### S10.03 — Create the DC MOP Step table

Create a third Standard / Organization-owned table, **DC MOP Step** (plural **DC MOP Steps**), with primary name **Step Name**, Business required, primary-column description `Readable label for a fictional maintenance procedure step.`, **table description** `Ordered fictional methods-of-procedure steps and their expected review evidence.`, and target schema `svrg_DCMOPStep`. After saving, reopen the table properties and primary column to confirm the description, Notes setting and **Business required** level were retained; correct any saved Optional setting.

| Display name / target schema | Description | Type / required | Properties |
| --- | --- | --- | --- |
| Step Name / `svrg_StepName` | Readable instruction label | Primary Text / Business required | Created with table |
| Step Number / `svrg_StepNumber` | Order within the parent MOP | Whole Number / Business required | 1–1,000; no default |
| Step Instruction / `svrg_StepInstruction` | Fictional action or review step | Multiline Text / Business required | Max 2,000 |
| Expected Verification / `svrg_ExpectedVerification` | What indicates a successful simulation | Multiline Text / Business required | Max 2,000 |
| Step Status / `svrg_StepStatus` | Tracking state of the procedure step | Local Choice / Business required | Not Started, Passed, Failed, Skipped; default Not Started |
| Execution Notes / `svrg_ExecutionNotes` | Notes about the simulated step | Multiline Text / Optional | Max 2,000 |
| Performed On / `svrg_PerformedOn` | When a simulated result was recorded | Date and Time / Optional | User local |

Do not enter real switching instructions or credentials. MOP Reviewed means the written procedure was checked, not executed.

**Dataverse service-limit checkpoint:** Save and verify metadata changes in measured batches. Rapid API writes may receive **HTTP 429 Too Many Requests** or stall. Follow a returned **Retry-After**, slow the next attempt, reopen the table and check whether the intended field/relationship already exists before retrying. Do not treat an unresponsive designer as proof of failure or submit an identical create repeatedly.

### S10.04 — Connect the Change, Risk and MOP relationships

On each source table use **Schema → Relationships → New relationship → Many-to-one**. Save the relationship and then inspect the resulting Lookup field under Columns. Lookups point to previously created tables; do not recreate those parent tables or use text in place of a relationship.

| Current table | Lookup / target schema | Related table | Required |
| --- | --- | --- | --- |
| DC Change Request | **Asset** / `svrg_Asset` | DC Asset | Business required |
| DC Change Request | **Related Work Order** / `svrg_RelatedWorkOrder` | DC Work Order | Optional |
| DC Change Request | **Requested By** / `svrg_RequestedBy` | DC Employee Profile | Optional |
| DC Risk Register | **Related Change** / `svrg_RelatedChange` | DC Change Request | Optional |
| DC Risk Register | **Asset** / `svrg_Asset` | DC Asset | Optional |
| DC Risk Register | **Risk Owner** / `svrg_RiskOwner` | DC Employee Profile | Optional |
| DC MOP Step | **Related Change** / `svrg_RelatedChange` | DC Change Request | Business required |

For each relationship choose **Delete = Restrict** and **Assign / Share / Unshare / Reparent / Merge = No cascade** where those actions can be configured. If an operation is unavailable in your table's relationship type, retain the supported default and document it in your own implementation notes. Always confirm Lookup target, required level and deletion behavior **after saving**.

**Checkpoint 3 — Relationships.** DC Change Request has three lookups, DC Risk Register has three, and DC MOP Step has one required parent-change lookup. Existing Assets, Work Orders and Employee Profiles remain unchanged.

### S10.05 — Create complete forms and filtered views

Open each new table's **Forms → New form → Main form** and give the form the exact name below. For long instructions use a **one-column** section; keep short choices, dates and lookups in **two-column** sections. Every **Business required** field must be visible when a user creates a row.

| Published form | Exact sections and fields |
| --- | --- |
| **DC Change Request — Review Main** | **Identity (2 columns):** Change Name, Change Code, Change Type, Change Status, Business Impact. **Context & Timing (2):** Asset, Related Work Order, Requested By, Planned Start, Planned End. **Procedure Text (1):** Reason for Change, MOP Summary, Backout Plan, Verification Plan. **Readiness Flags (2):** Safety Review Required, MOP Reviewed, Approval Requested. **Decision Record (2 with full-width notes):** Decision On, Approval Decision Note |
| **DC Risk Register — Assessment Main** | **Risk Identity (2):** Risk Name, Risk Code, Risk Category, Risk Status, **Risk Response**. **Assessment (2):** Likelihood, Impact, Risk Score, Safety Related. **Mitigation Text (1):** Risk Description, Mitigation Plan. **Risk Context (2):** Review Date, Related Change, Asset, Risk Owner |
| **DC MOP Step — Procedure Main** | **Step Identity (2):** Step Name, Step Number, Related Change, Step Status. **Instructions (1):** Step Instruction, Expected Verification. **Evidence (2 and full-width notes):** Performed On, Execution Notes |

**Risk Response is required.** Do not omit it from the Risk form, even if all other fields are already present: a record creation can fail when a Business required field is absent. Use existing Dataverse field controls; do not replace lookup cards with free-text controls. Save and publish each form. The generated Information forms can remain in the table; choose the named forms for the app later.

Create these **six public/system views** through **Views → New view**, with the indicated columns, filters, and **Save and publish**:

| Table | View | Columns | Exact filter |
| --- | --- | --- | --- |
| DC Change Request | **DC All Changes** | Change Code, Change Name, Change Status, Change Type, Business Impact, Asset, Planned Start | No filter |
| DC Change Request | **DC Changes Awaiting Review** | Change Code, Change Name, Change Status, MOP Reviewed, Asset, Planned Start | Change Status = Submitted **OR** Under Review |
| DC Change Request | **DC Approved Changes** | Change Code, Change Name, Change Status, Asset, Planned Start | Change Status = Approved **OR** Scheduled |
| DC Risk Register | **DC Open Risks** | Risk Code, Risk Name, Risk Category, Risk Score, Risk Status, Risk Response, Related Change | Risk Status **is not** Closed |
| DC Risk Register | **DC All Risks** | Risk Code, Risk Name, Likelihood, Impact, Risk Score, Risk Response, Risk Status | No filter |
| DC MOP Step | **DC Procedure Steps** | Related Change, Step Number, Step Name, Step Status | No filter; sort by Related Change and Step Number ascending when possible |

For each OR condition, use a dedicated group in the filter builder; combining two distinct statuses with AND returns no records. In the saved Risk Status Choice, Closed may have underlying numeric option **479120002**, but view filters should use the visible label. Validate the six saved views in Preview before publishing the app.

**Checkpoint 4 — Forms and views.** All three published Main forms show every required field (including Risk Response), long text does not overflow, and the six filtered views return the expected available records.

### S10.06 — Assemble DC Change & Risk Manager and working Asset context

In **Solutions → SunnyVerse Data Center Operations 360 → New → App → Model-driven app**, enter **DC Change & Risk Manager**. Description: `Review fictional changes, assess risks and track method-of-procedure steps.` Use **Add page → Dataverse table** to add these existing tables:

| Group | Page | Select in this app |
| --- | --- | --- |
| **Change Control** | DC Change Requests | **DC Change Request — Review Main**; All Changes, Changes Awaiting Review, Approved Changes |
| **Change Control** | DC MOP Steps | **DC MOP Step — Procedure Main**; Procedure Steps |
| **Risk & Context** | DC Risk Registers | **DC Risk Register — Assessment Main**; Open Risks and All Risks |
| **Risk & Context** | DC Work Orders | **DC Work Order — Maintenance Main**; **DC All Work Orders**, **DC Active Work Orders**, **DC Overdue Work Orders**, **DC Unassigned Work Orders** |
| **Risk & Context** | DC Assets | **DC Asset — Maintenance Context** form and an existing asset view |

**Verify the Asset form rather than assuming one already exists.** Open **DC Asset → Forms** and preview its available main forms. If no useful form exists, choose **New form → Main form**, name it **DC Asset — Maintenance Context**, and add these **existing** columns: Asset Name, Asset Code, Asset Category, Criticality, Operational Status, Data Hall, Manufacturer, Model Number, Serial Number, Rated Power kW, Install Date. Use two columns for short values and one for longer detail, then **Save and publish**. Select this form for the Assets page. Do not delete or overwrite the existing Information form or recreate the table.

Explicitly select intended forms/views for each page; otherwise the app designer may warn that an entity can show all eligible components. Those warnings are different from broken forms: verify actual table navigation and field content rather than dismissing them unread. Model-driven apps use supported theme/form layout controls, not Canvas ColorValue formulas.

Select **Save → Publish → Play**, and open Changes, Risks, MOP Steps, Work Orders and Assets. Navigate into an Asset lookup and verify it shows equipment details instead of an empty form.

**Checkpoint 5 — Model-driven navigation.** One published DC Change & Risk Manager uses the specified page groups, Work Order four views and meaningful Asset context without deleting earlier forms.

### S10.07 — Enter two fictional changes, one risk and five MOP steps

In **DC Change & Risk Manager → DC Change Requests → New**, create the following *fictional, paper-only* records. Use existing Lookup pickers for Asset, Related Work Order and Requested By. Enter a future, permitted training date/time window in your local date-time picker; **do not schedule any actual facility work**.

| Field | Change A | Change B |
| --- | --- | --- |
| Change Name | `UPS 001 Maintenance Simulation` | `UPS 002 Backout Review Simulation` |
| Change Code | `CHG-0001` | `CHG-0002` |
| Change Type | Maintenance | Standard |
| Change Status | Draft | Draft |
| Business Impact | Low | Moderate |
| Asset | UPS 001 | UPS 002 |
| Related Work Order | WO-0001 | WO-0002 |
| Requested By | Select an existing fictional employee | Select an existing fictional employee |
| Planned Start / End | Future training window / later end | Different future training window / later end |
| Reason for Change | `Verify a fictional maintenance procedure against simulated equipment context.` | `Practice review of an alternative rollback scenario.` |
| MOP Summary | `Review numbered paper-simulation steps before approval.` | `Review the written verification and rollback sequence.` |
| Backout Plan | `Stop the simulation and restore the recorded baseline state.` | `Return the training record to its initial fictional state.` |
| Verification Plan | `Compare pre- and post-simulation values in training notes.` | `Confirm the simulated rollback checklist is complete.` |
| MOP Reviewed | No (until steps are reviewed) | No (until steps are reviewed) |
| Approval Requested | No | No |
| Safety Review Required | No | No |

In **DC MOP Steps**, create these records with actual **Related Change** Lookup values:

| Related Change | Step Number | Step Name | Step Instruction | Expected Verification |
| --- | ---: | --- | --- | --- |
| CHG-0001 | 10 | Review synthetic asset context | Open the fictional UPS 001 training record | Correct Asset and Work Order displayed |
| CHG-0001 | 20 | Record simulated baseline | Note fictional prechange values in a training note | Baseline note saved |
| CHG-0001 | 30 | Review written rollback | Confirm the paper backout procedure is documented | Backout text present |
| CHG-0001 | 40 | Confirm readiness | Review all prior written steps | Review notes complete |
| CHG-0002 | 10 | Review alternate change | Compare the second change's simulated rollback plan | Supporting text is complete |

Leave all Step Status values **Not Started**; pre-approval review does **not** mean simulated execution has occurred.

Create one risk using **DC Risk Registers → New**:

| Field | Enter |
| --- | --- |
| Risk Name / Code | `Simulated UPS Maintenance Interruption` / `RSK-0001` |
| Risk Category | Electrical |
| Likelihood / Impact | Unlikely (2) / Major (3) |
| Risk Score | **6** (= 2 × 3) |
| Risk Response / Status | Mitigate / Open |
| Risk Description | `Fictional interruption could affect training continuity if the simulation is mishandled.` |
| Mitigation Plan | `Require written verification and rollback review before training approval.` |
| Related Change / Asset | CHG-0001 / UPS 001 |
| Risk Owner | An existing fictional employee |
| Safety Related | No |

Reopen each record and validate its actual Lookups. Once the written MOP steps and the procedure/backout/verification text have been reviewed for each change, set **MOP Reviewed = Yes** on CHG-0001 and CHG-0002. This confirms **document readiness only**. Do not change Change Status to Submitted until the approval flow has been configured and approved for testing.

**Checkpoint 6 — Practice data.** Two Changes, five MOP Steps and one Risk exist with valid related records, the two Changes remain **Draft**, and their MOP Reviewed flags are **Yes** after documented review.

### S10.08 — Build and save a guarded Change Approval flow

Open [Power Automate](https://make.powerautomate.com) → **Solutions → SunnyVerse Data Center Operations 360**. Verify **DC Automation Test Recipient** still holds a real email address controlled by the authorized test approver. Fictional employee lookups are not email accounts.

Choose **New → Automation → Cloud flow → Automated**, name the flow **DC10 Change Approval**, and use **Microsoft Dataverse — When a row is added, modified or deleted**:

| Trigger property | Configure |
| --- | --- |
| Change type | **Modified** |
| Table name | **DC Change Requests** |
| Scope | **Organization** |
| Select columns | `svrg_changestatus` — verify the logical name under the Change Status column |
| Filter rows | Leave empty |

For **Change Status** verify the saved Choice metadata. In the documented publisher setup **Submitted = 479120001**, but do not hardcode this value for another environment without checking.

**Read the current row first.** Choose **+ → Dataverse → Get a row by ID**, select **DC Change Requests** and set **Row ID** from the trigger. Rename the action exactly **Get_change_fresh**. This reads the saved state when the action executes, reducing the risk of basing approval dispatch on an old, queued trigger snapshot.

Add **Control → Condition** with **all three AND tests** on *Get_change_fresh* outputs: Change Status = Submitted, MOP Reviewed = Boolean true, Approval Requested = Boolean false. In the Expression editor this is:

```text
and(
  equals(outputs('Get_change_fresh')?['body/svrg_changestatus'], 479120001),
  equals(outputs('Get_change_fresh')?['body/svrg_mopreviewed'], true),
  equals(outputs('Get_change_fresh')?['body/svrg_approvalrequested'], false)
)
```

Replace the numeric Submitted value if the saved Choice differs. If your designer exposes current-row fields directly, use them in the Condition builder instead. **Reading the current row is not a transactional lock**—parallel requests can still race—so this lesson must not be treated as a production exactly-once system.

In **If yes**, create these actions **in this order**:

1. **Dataverse → Update a row** on the same Change Request GUID: set **Approval Requested = Yes**, **Change Status = Under Review**. Leave unrelated fields untouched.
2. **Standard approvals → Start and wait for an approval** (choose the nondeprecated action). If authorization is required, sign in through the authorized connector flow. Add or confirm its **Standard approvals** solution connection reference (for example `svrg_DC10StandardApprovals`). **Inspect the actual Connector field and saved connector ID**: a search selector can choose an unrelated connector even if the reference was given a familiar display name.
3. Set **Approval type = Approve/Reject — First to respond**. **Assigned to = DC Automation Test Recipient** environment-variable current value. **Title:** `[DC360 TRAINING] Review change ` plus Change Code dynamic content. **Details:** Change Name, MOP Summary, Backout Plan, Verification Plan and readable Business Impact. If available in the trigger output, the Business Impact label expression is `triggerOutputs()?['body/_svrg_businessimpact_label']`. A Lookup typically exposes only a GUID: to show an Asset name, add a separate Dataverse **Get a row by ID** on DC Assets, or omit the name. Do not mistake the GUID for a user-readable asset name.
4. Add a **Condition** comparing the Standard approvals **Outcome** to the exact text **Approve**. In **If yes**, **Dataverse → Update a row** sets **Change Status = Approved**, **Approval Decision Note = "Approved during fictional training review"**, **Decision On = utcNow()**. In **If no**, update **Change Status = Rejected**, **Approval Decision Note = "Rejected during fictional training review"**, **Decision On = utcNow()**.
5. Leave the *first readiness guard's* **If no** branch empty.

In trigger **Settings**, enable **Concurrency Control** and set **Degree of Parallelism = 1** if your designer supports it. This reduces overlapping runs for the training test, but **the long-running Start and wait action occupies the one run slot until a human responds**. Additional Dataverse Modified events can queue for minutes. A delayed run should check the *fresh* row and exit when Approval Requested is already Yes. Neither concurrency 1 nor a Boolean flag guarantees delivery, deduplication or atomic idempotency. A production design needs a durable, unique dispatch claim and explicit reconciliation.

Save, reopen the actual **DC10 Change Approval** flow to verify trigger, guard, connection references, approval action and two decision branches. Do not rely on a designer still displaying "Saving…". Leave the flow **Off** until a deliberate test is authorized.

**Checkpoint 7 — Approval configured.** One verified, saved DC10 Change Approval flow has the **Get_change_fresh** action, correct **Standard approvals** connector and solution reference, readiness guard, approval action, two decision branches, and verified test approver. It remains Off.

### S10.09 — Test Approved and Rejected decisions, then switch Off

Confirm **CHG-0001** and **CHG-0002** remain in **Draft** with **MOP Reviewed = Yes**, **Approval Requested = No**, full MOP and Backout plans, and valid lookups. Request approval to start the controlled test, turn **DC10 Change Approval On**, and perform:

| Action | Expected verification |
| --- | --- |
| Set **CHG-0001** Change Status = Submitted and Save | Confirm a new run under **Flow details → 28-day Run history**; current Change becomes Under Review |
| Open **Power Automate → Approvals → Received** | One pending training approval exists even if no email is visible |
| Approve CHG-0001 through **Received** | Flow completes; saved Change Status = Approved with Decision On and Decision Note |
| Set **CHG-0002** Change Status = Submitted and Save | A separate run and a second approval are recorded |
| Reject CHG-0002 through **Received** | Flow completes; saved Change Status = Rejected with Decision On and Decision Note |
| Inspect extra Modified runs | Runs caused by Under Review/Approved/Rejected updates exit through the readiness guard without creating additional approvals |
| End test | Switch **DC10 Change Approval Off**, verify actual enabled status and check earlier flows were not changed |

**Do not depend solely on an approval email.** A request may appear under **Approvals → Received** without appearing in the inbox. The portal's run history and approval center are the authoritative places to verify state. A run waiting for response is neither a completed success nor automatically a failure.

**If a Submitted save produces no run:** check the flow's enabled status, Scope, selected logical column and permissions; check the Approvals center and pending runs before retrying. Only when the row is still Submitted, Approval Requested is **No**, and there is **no pending approval**, consider a single deliberate repeat save in the authorized learning environment. **Do not keep toggling fields or resubmitting blindly**; missed or delayed events are a known limitation requiring monitoring and recovery design.

Because Concurrency = 1, retrigger runs can wait behind a pending human approval and appear to take several minutes. This alone does not prove a flow is broken. Conversely, a completed test does **not** prove all events will arrive in the future. Compare records, Received approvals and flow runs; for this controlled test confirm exactly **two intended approvals**, one approved and one rejected.

**Checkpoint 8 — Approval verification.** Both decisions are stored, no unexpected approval was dispatched, the MOP and Risk records remain unchanged, and the cloud flow is **Off**. If any of these cannot be confirmed, mark the test incomplete rather than assuming success.

### S10.10 — Verify the solution and finish Part 10

Open **Solutions → SunnyVerse Data Center Operations 360** and inspect the components:

| Component | Check |
| --- | --- |
| Dataverse | One DC Change Request table, one DC Risk Register table, one DC MOP Step table |
| Lookup relationships | Change → Asset / Work Order / Employee; Risk → Change / Asset / Employee; MOP Step → Change |
| Uniqueness | Change Code and Risk Code alternate keys **Active** |
| Forms | Three published main forms with readable multiline fields and correct lookups |
| Views | Change approval queues, Risk views, Procedure Step view |
| Model-driven app | One published **DC Change & Risk Manager** |
| Sample records | Two Changes, one Risk, five MOP Steps, no invented parent records |
| Approvals | One solution flow, the correct **Standard approvals** connector identity and reference, verified test recipient, Received-center decisions and observed runs |
| Safe status | Approval flow **Off** after tests; existing notification flow states unchanged; inspect unexpected extra enabled flows before related tests |
| Access | Authorized Power Platform roles, not the fictional requested/assigned employee references |

Check that model-driven app navigation opens Change and Risk forms, Risk Response is present in the required-field form, Asset context is meaningful and MOP Steps show their correct parent Change. **Approved** means a fictional administrative decision was recorded, not that MOP steps executed. The sample change records may remain Approved/Rejected as evidence of the training workflow; do not reset them unless your own testing requires it.

### Finish Part 10

You have a linked **Change Request**, **Risk Register** and **MOP Step** model, plus **DC Change & Risk Manager** and one controlled approval process. This provides a reproducible training workflow for documenting change impact, procedure readiness, rollback, risk response and an explicit human decision while keeping operational control and real infrastructure entirely outside the application.


---

## Part 11 — Run Supporting Operations: Vendors, Spares, Inventory and Shift Handover

Part 10 linked maintenance work to change reviews, risks and approval decisions. The next operational responsibility is continuity between shifts: teams must know **which fictional suppliers support a part**, **what spare quantities are recorded in each data hall**, and **which open work must carry into the next shift**. Here you will build the Supporting Operations registers in the existing solution and make them usable through a model-driven app. Reuse the assets, halls, employees, incidents, work orders and changes you have already created.

We will create four tables—**DC Vendor**, **DC Spare Part**, **DC Inventory Balance**, and **DC Shift Handover**—then configure their Lookup relationships, forms and views. The practice records are entered through the app. **No CSV import, new cloud flow, live inventory feed, or message to a real supplier** is required.

| New table | Business purpose |
| --- | --- |
| `DC Vendor` | Store fictional external-partner contacts and service categories |
| `DC Spare Part` | Catalog replacement-part identities, units, supplier and reorder thresholds |
| `DC Inventory Balance` | Record how much of a part is on hand or reserved in each hall |
| `DC Shift Handover` | Document fictional outgoing-to-incoming shift notes and open work |
| `DC Supporting Operations Hub` | Model-driven app for browsing the four registers and existing operational context |

The quantity and handover fields in this lesson are **training records**. Entering a new inventory number is **not an automatic stock transaction**, and an Acknowledged handover status is **not a verified electronic signature**. Do not use these training records to direct physical work.

### S11.01 — Confirm the existing reference data

Open [Power Apps](https://make.powerapps.com), choose the authorized environment and select **Solutions → SunnyVerse Data Center Operations 360**. Review, but do not recreate, the existing parent records.

| Existing table | Check in its Data view | Used later for |
| --- | --- | --- |
| DC Data Hall | `Data Hall 01` and `Data Hall 02` | Inventory location and shift coverage; the existing primary-name display column is **Hall Name** (in the validated practice environment, schema `svrg_hallname`, not `datahallname`) |
| DC Asset | `UPS 001` and `Cooling Unit 002` | Spare compatibility and equipment context |
| DC Employee Profile | Fictional engineers such as `Noah Morales` and `Sana Kim` | Outgoing/incoming handover references |
| DC Work Order | Valid `WO-0001` and `WO-0002` | Open-work context |
| DC Incident | Valid `INC-0001` and `INC-0002` | Shift handover context |
| DC Change Request | Valid `CHG-0001` and `CHG-0002` | Change-control context |

When a parent lookup displays only an identifier or an empty main form, inspect the existing table's published Main form and selected app components rather than creating duplicate parent tables. Use the real Dataverse lookup picker when linking records.

For each of the four new tables, select **Standard** and **Organization ownership** at creation. Enter the stated primary-name label; **after the table is created, reopen Schema → Columns → the primary-name column and explicitly set Required = Business required, then save and reopen it again to verify persistence**. In the practice build, this setting reverted for all four primary names when initially created, so do not treat the creation dialog as proof. Confirm the `svrg` publisher prefix in saved metadata. Create the code alternate key only after its column is fully saved, and wait for the key status **Active** before adding records. A just-created key can fail temporarily; inspect and retry only after confirming the column and key are not already present.

**Checkpoint 1 — Existing data.** Both data halls, sample Assets and the existing Employee, Incident, Work Order and Change records can be opened. No new table has been created just to replace an existing reference.

### S11.02 — Create the DC Vendor register

In the solution choose **New → Table** and use advanced settings:

| Table property | Value |
| --- | --- |
| Display name / plural | **DC Vendor** / **DC Vendors** |
| Description | `Fictional third-party service and parts partners for data center operations training.` |
| Type / ownership | Standard / Organization |
| Primary name / schema target | **Vendor Name** / `svrg_VendorName` |
| Primary name description / required | `Readable name of a fictional external supplier.` / Business required |
| Table schema target | `svrg_DCVendor` |
| Notes | Off by default; no attachment workflow in this lesson |

Create the table. Reopen **Vendor Name** and confirm **Business required**; update if the designer saved Optional. Add these columns under **Schema → Columns → New column**, entering the description and other properties:

| Display / target schema | Description | Type / Required | Configuration |
| --- | --- | --- | --- |
| Vendor Name / `svrg_VendorName` | External fictional partner name | Primary Text / Business required | Created with table, max 200 |
| Vendor Code / `svrg_VendorCode` | Unique supplier reference | Single-line Text / Business required | Text format, max 24, Searchable Yes |
| Service Category / `svrg_ServiceCategory` | Primary training supplier specialty | **Local single Choice** / Business required | **Cooling Systems**, **Electrical Services**, **Spare Parts Supply**, **Other**; no default |
| Vendor Status / `svrg_VendorStatus` | Whether the vendor is eligible in the exercise | Local single Choice / Business required | **Approved**, **Under Review**, **Inactive**; no default |
| Contact Role / `svrg_ContactRole` | Generic responsible office, not a personal name | Text / Optional | Max 100, Searchable Yes |
| Contact Email / `svrg_ContactEmail` | Fictional supplier contact reference | Text (email format when offered) / Optional | Max 150; do **not** use real addresses |
| Support Window / `svrg_SupportWindow` | Illustrative response coverage | Text / Optional | Max 100 |
| Vendor Notes / `svrg_VendorNotes` | Training-only support limitations | Multiline Text / Optional | Max 2,000 |
| Active / `svrg_Active` | Whether record can be selected for new practice work | Yes/No / Optional | Default **Yes** |

For Choice columns use **Data type → Choice** and turn off **Sync with global choice** if shown, so the options remain local. Save each column, inspect its actual schema name, and do not create duplicates if a previous save appeared to hang.

After confirming **Vendor Code** was saved, open **Schema → Keys → New key**, name it **DC Vendor Code Key**, select only **Vendor Code**, then save. If the editor returns **HTTP 400** immediately after column creation, refresh the table and inspect both Columns and Keys; verify Vendor Code exists and a key was not already created, then retry once the column metadata is available. In the validated practice run the retry succeeded and the key took several minutes to become **Active**. Check the actual key status before entering supplier records. For the local Choice columns, use their labels in forms; if using an API, read the numeric option values from saved metadata rather than guessing them.

**Checkpoint 2 — Vendors.** DC Vendor has one primary name, eight additional business columns, two local Choices and an Active Vendor Code key.

### S11.03 — Create the DC Spare Part catalog

Create another Standard, Organization-owned table:

| Table property | Value |
| --- | --- |
| Display / plural | **DC Spare Part** / **DC Spare Parts** |
| Description | `Fictional catalog of replacement parts compatible with data center assets.` |
| Primary name / schema target | **Spare Part Name** / `svrg_SparePartName` |
| Primary name required | **Business required**, verified after saving |
| Table schema target | `svrg_DCSparePart` |
| Notes | Off unless you intentionally need notes in your training environment |

Add these columns. **Preferred Vendor** and **Compatible Asset** are created later as actual Lookup relationships, not text.

| Display / target schema | Description | Type / Required | Configuration |
| --- | --- | --- | --- |
| Spare Part Name / `svrg_SparePartName` | Readable replacement-part description | Primary Text / Business required | Created with table |
| Spare Part Code / `svrg_SparePartCode` | Unique catalog identifier | Text / Business required | Max 24; Searchable Yes |
| Part Category / `svrg_PartCategory` | Replacement-part classification | Local single Choice / Business required | **UPS & Electrical**, **Mechanical & Cooling**, **IT & Network**, **Other** |
| Unit of Measure / `svrg_UnitOfMeasure` | Unit used for stock counting | Local single Choice / Business required | **Each**, **Kit**, **Box** |
| Manufacturer Part Code / `svrg_ManufacturerPartCode` | Fictional manufacturer reference | Text / Optional | Max 100 |
| Reorder Point / `svrg_ReorderPoint` | Threshold at or below which stock needs review | Whole Number / Business required | Minimum 0; maximum 100,000 |
| Critical Spare / `svrg_CriticalSpare` | Flags a part requiring special stock attention | Yes/No / Optional | Default No |
| Storage Guidance / `svrg_StorageGuidance` | General fictional storage description | Multiline Text / Optional | Max 2,000 |
| Active / `svrg_Active` | Stock item remains in the practice catalog | Yes/No / Optional | Default Yes |

Create a **DC Spare Part Code Key** based on **Spare Part Code** and wait for **Active**. Reopen Local Choice settings to confirm labels and display order. This catalog does **not** have a Quantity On Hand field: quantities vary by hall and belong on **DC Inventory Balance**.

**Checkpoint 3 — Parts catalog.** DC Spare Part has the eight additional nonlookup columns, its primary name, two local Choices, and an Active code key. No free-text Vendor or Asset column has been created.

### S11.04 — Create the DC Inventory Balance table

A single spare may have different quantities in Data Hall 01 and Data Hall 02. Create **DC Inventory Balance** (plural **DC Inventory Balances**), Standard / Organization ownership, primary name **Balance Name** (Business required), table schema target `svrg_DCInventoryBalance`, primary schema target `svrg_BalanceName`, and description `Fictional per-hall on-hand and reserved spare-part balances for training.`

| Display / target schema | Description | Type / Required | Configuration |
| --- | --- | --- | --- |
| Balance Name / `svrg_BalanceName` | Human-readable part and hall label | Primary Text / Business required | Created with table |
| Balance Code / `svrg_BalanceCode` | Unique location-specific inventory record | Text / Business required | Max 24; Searchable Yes |
| Quantity On Hand / `svrg_QuantityOnHand` | Physical quantity represented in synthetic data | Whole Number / Business required | Min 0; max 100,000 |
| Quantity Reserved / `svrg_QuantityReserved` | Quantity committed to open fictional work | Whole Number / Business required | Min 0; max 100,000; **no column default in the verified designer; enter 0 explicitly when nothing is reserved** |
| Reorder Required / `svrg_ReorderRequired` | Manual flag for a low-availability balance | Yes/No / Optional | Default No |
| Last Counted On / `svrg_LastCountedOn` | When the simulated stock count was recorded | Date and Time / Optional | User local behavior |
| Count Notes / `svrg_CountNotes` | Fictional discrepancy or follow-up explanation | Multiline Text / Optional | Max 2,000 |

Create **DC Balance Code Key** on Balance Code, wait for Active, and verify **Balance Name** is Business required. **Spare Part** and **Data Hall** are added as required Lookups in S11.06.

For every balance, manually calculate **Available = Quantity On Hand − Quantity Reserved**. Compare Available with the related Spare Part's **Reorder Point** and enter **Reorder Required = Yes** when Available is at or below that threshold; otherwise choose No. Enter **Quantity Reserved = 0** explicitly where applicable. Before saving, manually check **0 ≤ Quantity Reserved ≤ Quantity On Hand**. This is a **human validation checkpoint**, not an enforced Dataverse cross-field rule: the numeric column minimums cannot compare two fields, and neither the available amount nor the reorder flag recalculates automatically. Reopen each balance and repeat the check if someone edits the quantities.

**Checkpoint 4 — Balance design.** The Inventory Balance table exists with a working unique code, numeric nonnegative fields and the manual low-stock flag. No quantities are stored on the part catalog itself.

### S11.05 — Create the DC Shift Handover table

Create **DC Shift Handover** (plural **DC Shift Handovers**), Standard / Organization ownership, table schema target `svrg_DCShiftHandover`, primary name **Handover Name** with target `svrg_HandoverName`, Business required, and description `Synthetic shift-transition notes linking open operational records.`

| Display / target schema | Description | Type / Required | Configuration |
| --- | --- | --- | --- |
| Handover Name / `svrg_HandoverName` | Readable shift transition summary title | Primary Text / Business required | Created with table |
| Handover Code / `svrg_HandoverCode` | Unique handover reference | Text / Business required | Max 24, Searchable Yes |
| Handover At / `svrg_HandoverAt` | Time of recorded fictional shift transition | Date and Time / Business required | User local behavior; no default |
| Shift Group / `svrg_ShiftGroup` | Fictional shift rotation | Local single Choice / Business required | A, B, C, D; no default |
| Handover Status / `svrg_HandoverStatus` | Documentation state | Local single Choice / Business required | Draft, Ready for Review, Acknowledged |
| Shift Summary / `svrg_ShiftSummary` | High-level outgoing shift record | Multiline Text / Business required | Max 2,000 |
| Open Items / `svrg_OpenItems` | Outstanding synthetic operational concerns | Multiline Text / Business required | Max 2,000 |
| Next Actions / `svrg_NextActions` | Planned fictional next-shift follow-ups | Multiline Text / Business required | Max 2,000 |
| Safety Notes / `svrg_SafetyNotes` | Non-sensitive training safety reminders | Multiline Text / Optional | Max 2,000 |
| Training Acknowledged / `svrg_TrainingAcknowledged` | Human-entered confirmation of review | Yes/No / Optional | Default No |
| Acknowledged On / `svrg_AcknowledgedOn` | When acknowledgement was documented | Date and Time / Optional | User local; no default |

Create **DC Handover Code Key** on Handover Code and wait until it reaches Active. Reopen Handover Name and any Notes setting to confirm the saved property values. Actual Employee, Hall, Incident, Work Order and Change links come from relationships in S11.06; do not represent them with text or assume that selecting a fictional employee verifies a user's real identity.

**Checkpoint 5 — Handover design.** The handover table has one primary name and ten additional nonlookup columns, with all Business required fields present and the unique code key Active.

### S11.06 — Add the relationships to existing tables

On each new table open **Schema → Relationships → New relationship → Many-to-one**. The **Current table** is the first column below, and the **Related table** must be selected exactly. A Many-to-one relationship automatically creates the Lookup column; never add it again as ordinary Text.

| Current table | Lookup name / target schema | Related table | Required |
| --- | --- | --- | --- |
| DC Spare Part | **Preferred Vendor** / `svrg_PreferredVendor` | DC Vendor | Optional |
| DC Spare Part | **Compatible Asset** / `svrg_CompatibleAsset` | DC Asset | Optional |
| DC Inventory Balance | **Spare Part** / `svrg_SparePart` | DC Spare Part | **Business required** |
| DC Inventory Balance | **Data Hall** / `svrg_DataHall` | DC Data Hall | **Business required** |
| DC Shift Handover | **Data Hall** / `svrg_DataHall` | DC Data Hall | **Business required** |
| DC Shift Handover | **Outgoing Employee** / `svrg_OutgoingEmployee` | DC Employee Profile | **Business required** |
| DC Shift Handover | **Incoming Employee** / `svrg_IncomingEmployee` | DC Employee Profile | Optional |
| DC Shift Handover | **Related Incident** / `svrg_RelatedIncident` | DC Incident | Optional |
| DC Shift Handover | **Related Work Order** / `svrg_RelatedWorkOrder` | DC Work Order | Optional |
| DC Shift Handover | **Related Change** / `svrg_RelatedChange` | DC Change Request | Optional |

For every relationship set **Delete = Restrict**, with **Assign / Share / Unshare / Reparent / Merge = No cascade** where the designer allows it. These behaviors help prevent unintended child-row changes when a fictional parent is edited or removed. Save the relationship and verify the generated **Lookup** column's target, required setting, and actual `svrg` schema name. The platform may hide cascade options that do not apply to a particular ownership type.

**Checkpoint 6 — Ten Lookups.** Spare Part has two Lookups, Inventory Balance has two, and Shift Handover has six. All resolve to the correct existing parent tables; no duplicate Asset, Data Hall or Employee table exists.

### S11.07 — Create the Main forms and operational system views

Before building the Supporting Operations forms, inspect **DC Asset → Forms** for a published form named **DC Asset — Maintenance Context**. If none is present, use **Forms → New form → Main form**, name it exactly, and include the existing **Asset Name, Asset Code, Asset Category, Criticality, Operational Status, Data Hall, Manufacturer, Model Number, Serial Number, Rated Power kW and Install Date** fields. Save and publish; do not create a second Asset table or recreate any of its columns. Likewise inspect **DC Data Hall → Forms**. If the only usable form shows Hall Name alone, create and publish **DC Data Hall — Identity Main** with the existing **Hall Name, Hall Code, Campus, Criticality, Design IT Capacity kW and Active** fields. Confirm its primary name uses the **Hall Name** column; select it by display name even where the saved schema shows `svrg_hallname`.

Next create one named **Main form** on each of the four new tables with **Forms → New form → Main form**, then save and publish. Use one-column sections for multiline notes and two-column sections for short identifiers, statuses and lookups. All **Business required** fields, including lookup fields, must appear. These are model-driven forms using built-in field controls, not Canvas Text/Fill/OnSelect formulas.

| New Main form | Sections and exact fields |
| --- | --- |
| **DC Vendor — Support Main** | **Identity (2):** Vendor Name, Vendor Code, Service Category, Vendor Status, Active. **Contact (2):** Contact Role, Contact Email, Support Window. **Notes (1):** Vendor Notes |
| **DC Spare Part — Catalog Main** | **Part Identity (2):** Spare Part Name, Spare Part Code, Part Category, Unit of Measure, Manufacturer Part Code, Active. **Stock Policy & Fit (2):** Critical Spare, Reorder Point, Preferred Vendor, Compatible Asset. **Guidance (1):** Storage Guidance |
| **DC Inventory Balance — Stock Main** | **Stock Identity (2):** Balance Name, Balance Code, Spare Part, Data Hall. **Counts (2):** Quantity On Hand, Quantity Reserved, Reorder Required, Last Counted On. **Notes (1):** Count Notes |
| **DC Shift Handover — Main** | **Shift Identity (2):** Handover Name, Handover Code, Handover At, Shift Group, Handover Status, Data Hall, Outgoing Employee, Incoming Employee. **Operational Links (2):** Related Incident, Related Work Order, Related Change. **Shift Narrative (1):** Shift Summary, Open Items, Next Actions, Safety Notes. **Training Review (2):** Training Acknowledged, Acknowledged On |

Verify that every Business required field, including required Lookup fields, is on its form. Leave generated Information forms untouched, but later choose these named forms in the new app.

Create these **eight views** under **Views → New view**, choose the listed columns and conditions, and **Save and publish**:

| Table | View | Important columns | Filter |
| --- | --- | --- | --- |
| DC Vendor | **DC Active Vendors** | Vendor Code, Vendor Name, Service Category, Vendor Status, Active | Active = Yes AND Vendor Status = Approved |
| DC Vendor | **DC All Vendors** | Vendor Code, Vendor Name, Vendor Status, Service Category | None |
| DC Spare Part | **DC Spare Catalog** | Spare Part Code, Spare Part Name, Part Category, Unit of Measure, Reorder Point, Preferred Vendor | None |
| DC Spare Part | **DC Critical Spares** | Spare Part Code, Spare Part Name, Part Category, Reorder Point, Preferred Vendor | Critical Spare = Yes |
| DC Inventory Balance | **DC Inventory by Hall** | Balance Code, Spare Part, Data Hall, Quantity On Hand, Quantity Reserved, Reorder Required | None; sort by Data Hall, then Balance Code when supported |
| DC Inventory Balance | **DC Reorder Review** | Balance Code, Spare Part, Data Hall, Quantity On Hand, Quantity Reserved, Reorder Required | Reorder Required = Yes |
| DC Shift Handover | **DC Shift Handovers** | Handover Code, Handover Name, Handover At, Shift Group, Handover Status, Data Hall | None; sort Handover At descending |
| DC Shift Handover | **DC Handover Pending Review** | Handover Code, Handover At, Handover Status, Data Hall, Incoming Employee | Handover Status = Draft OR Ready for Review |

For **DC Inventory by Hall**, sort by the **Data Hall** Lookup's **display value**, then Balance Code where the designer permits a secondary sort; this is a display-name sort, not a GUID sort. For **DC Active Vendors**, set two conditions joined with **AND**: Active = Yes and Vendor Status = Approved. Use the **Approved** label in the view designer; stored Choice numeric values are metadata-dependent and should only be read from that environment for API operations. For **DC Handover Pending Review**, put Draft and Ready for Review in one **OR** group, not AND.

The **DC Reorder Review** view filters a **manually saved Boolean**, not a calculated comparison between Quantity On Hand and a related Spare Part's threshold. Recalculate and check the manual value after quantity edits. The view itself does not guarantee inventory correctness.

**Checkpoint 7 — Forms and views.** All four new named Main forms show required fields, the Asset and Data Hall context forms are readable, and eight published views show the intended queues. Verify the two-context-form names and use their actual saved components rather than blank auto-generated forms.

### S11.08 — Assemble DC Supporting Operations Hub

Inside **Solutions → SunnyVerse Data Center Operations 360**, choose **New → App → Model-driven app**. Enter:

| App property | Value |
| --- | --- |
| Name | **DC Supporting Operations Hub** |
| Description | `Review fictional shift handovers, supplier contacts, spare parts and inventory balances.` |
| App type | Model-driven |
| Solution | Existing SunnyVerse Data Center Operations 360 |

Under **Add page → Dataverse table**, add the **existing** tables and arrange navigation groups:

| Navigation group | Table page | Use in this app |
| --- | --- | --- |
| **Shift Operations** | DC Shift Handovers | DC Shift Handover — Main; both handover views |
| **Shift Operations** | DC Incidents | Select a published existing Incident Main form and an existing Incident view explicitly under **In this app**; do not leave both unselected |
| **Shift Operations** | DC Work Orders | DC Work Order — Maintenance Main; four work-order views |
| **Shift Operations** | DC Change Requests | DC Change Request — Review Main; existing change views |
| **Inventory & Partners** | DC Inventory Balances | DC Inventory Balance — Stock Main; both inventory views |
| **Inventory & Partners** | DC Spare Parts | DC Spare Part — Catalog Main; both spare views |
| **Inventory & Partners** | DC Vendors | DC Vendor — Support Main; both vendor views |
| **Inventory & Partners** | DC Assets | Published **DC Asset — Maintenance Context** form; existing Asset view |
| **Inventory & Partners** | DC Data Halls | Published **DC Data Hall — Identity Main** form; existing Data Hall view |

Under each table page, inspect **Forms → In this app** and **Views → In this app**, using **Add** to select its published forms and views as shown. In particular, explicitly select an existing Incident form and view: when Incidents was added without a selected form or view, app validation showed **“Entity doesn't reference a form or view”**. That warning can allow access to broader defaults, so correct the app selection rather than describing the warning as a successful validation. If no appropriate Incident form or view exists, inspect its published components and add a focused existing-entity form or view; do not recreate the Incident table. Check and publish the Asset Maintenance Context and Data Hall Identity forms created in S11.07. Model-driven apps inherit supported theme settings; unlike the Canvas apps, these pages do not use `ColorValue` formulas.

Choose **Save → Publish → Play**. Open Vendor, Spare, Balance and Handover pages and confirm each shows its expected form.

**Checkpoint 8 — Supporting Operations Hub.** One published model-driven app presents the two navigation groups and linked operational pages. The existing Canvas Apps and approval flows are unchanged.

### S11.09 — Create and verify a small connected practice set

Use the model-driven app's **New** command on each table, following the parent-first sequence below. Start by creating **VEN-0001** through **DC Vendor — Support Main** to verify that the complete form saves. For bulk entry in an authorized development environment, advanced learners may use a supported Dataverse Web API client, but must bind **real Lookup references**, not text or invented GUID values; then reopen and read back **every saved row in the model-driven app**. The learner path remains the app form. Do not import unrelated CSV files or create duplicate sample records. All named partners are fictional external suppliers, not SunnyVerse Renewable Group subsidiaries.

**A. Vendor records**

| Vendor Code | Vendor Name | Category | Status | Active |
| --- | --- | --- | --- | --- |
| `VEN-0001` | Data Center Partner A — Cooling Systems Support | Cooling Systems | Approved | Yes |
| `VEN-0002` | Wind Partner B — Electrical Services | Electrical Services | Approved | Yes |

Set Contact Role to **Service Desk**, Support Window to **Training business hours**, and use only a **nonworking address under example.com** if you populate Contact Email (for example `support@example.com`). **VEN-0002 retains the fictional name Wind Partner B — Electrical Services** so it matches the established exercise records; in this example the partner supplies a cross-sector electrical service. Do not treat the partner as an internal SunnyVerse team or send it real email.

**B. Spare catalog records**

| Spare Part Code | Name | Category | Unit | Reorder Point | Critical Spare | Preferred Vendor | Compatible Asset |
| --- | --- | --- | --- | ---: | --- | --- | --- |
| `SPR-0001` | UPS Battery Cartridge | UPS & Electrical | Each | 2 | Yes | VEN-0002 | UPS 001 |
| `SPR-0002` | Cooling Fan Module | Mechanical & Cooling | Each | 3 | Yes | VEN-0001 | Cooling Unit 002 |
| `SPR-0003` | Network Patch Kit | IT & Network | Kit | 5 | No | Leave blank | Leave blank |

**C. Inventory balances**

| Balance Code | Balance Name | Spare Part | Data Hall | On Hand | Reserved | Available | Reorder Required |
| --- | --- | --- | --- | ---: | ---: | ---: | --- |
| `BAL-0001` | UPS Cartridge — Hall 01 | SPR-0001 | Data Hall 01 | 4 | 1 | 3 | No |
| `BAL-0002` | Cooling Fan — Hall 02 | SPR-0002 | Data Hall 02 | 2 | 0 | 2 | Yes |
| `BAL-0003` | Patch Kits — Hall 01 | SPR-0003 | Data Hall 01 | 8 | 2 | 6 | No |

**Explain the result:** BAL-0002 has Available = 2 and the Cooling Fan Module's Reorder Point = 3, so its manually selected **Reorder Required = Yes** is correct. The other two Available values exceed their thresholds. The Status does not automatically change if someone edits counts.

**D. Shift handovers**

| Field | Handover A | Handover B |
| --- | --- | --- |
| Handover Name / Code | `Hall 01 Morning Review` / `HAN-0001` | `Hall 02 Evening Review` / `HAN-0002` |
| Data Hall | Data Hall 01 | Data Hall 02 |
| Handover At | Current fictional exercise date/time | Current fictional exercise date/time |
| Shift Group | A | B |
| Handover Status | Ready for Review | Draft |
| Outgoing Employee | Noah Morales | Sana Kim |
| Incoming Employee | Sana Kim | Olivia Nair |
| Related Incident | INC-0001 | INC-0002 |
| Related Work Order | WO-0001 | WO-0002 |
| Related Change | CHG-0001 | CHG-0002 |
| Shift Summary | `Fictional shift review of UPS 001 records.` | `Fictional review of UPS 002 and related records.` |
| Open Items | `Review linked incident and work order.` | `Review linked work order and change status.` |
| Next Actions | `Confirm upcoming training inspection notes.` | `Check unresolved simulated follow-up items.` |
| Training Acknowledged | No | No |
| Acknowledged On | Blank | Blank |

If the chosen employee lookup is not present, choose another existing fictional employee rather than adding a duplicate person row. Enter only data-neutral fictional notes—no real facility conditions, credentials, phone numbers or dispatch instructions.

**E. Test one handover and one inventory correction.** Open **HAN-0001**, set **Handover Status = Acknowledged**, **Training Acknowledged = Yes**, and **Acknowledged On = current training time**, then save and reopen to verify. Afterwards restore it to **Ready for Review**, **Training Acknowledged = No**, and clear Acknowledged On, so the baseline remains consistent. This is an illustrative record edit, **not** actual user authentication or a shift sign-off.

On **BAL-0002**, temporarily change **Quantity On Hand** to 5, leave Reserved 0, and manually change **Reorder Required** to No because Available = 5 is above Reorder Point = 3. Save and inspect **DC Reorder Review**. Restore Quantity On Hand = 2 and Reorder Required = Yes, and verify BAL-0002 returns to the view. **No automatic inventory transaction occurred.**

**Checkpoint 9 — Linked sample records.** Two Vendors, three Spare Parts, three Balances and two Handovers exist with valid lookups. The Reorder Review view displays BAL-0002 at baseline, and the Handover Pending Review view includes HAN-0001 / HAN-0002. Sample edits have been restored.

### S11.10 — Validate and publish Part 11

| Validation | Expected result |
| --- | --- |
| Tables | Exactly one new Vendor, Spare Part, Inventory Balance and Shift Handover table |
| Schema | Intended `svrg` prefixes, required primary names and code keys Active |
| Relationships | 2 Spare Part + 2 Inventory Balance + 6 Handover = **10** new Lookup columns |
| Forms | Four complete named new Main forms, plus the published **DC Asset — Maintenance Context** and **DC Data Hall — Identity Main** context forms where previously absent |
| Views | Eight published operational views and correct filter grouping |
| App | One published **DC Supporting Operations Hub** with explicitly selected forms/views, including Incidents, and no unresolved form/view selection warning |
| Data | 2 fictional vendors, 3 spare parts, 3 balances, 2 handovers |
| Inventory | Reorder flags match the manually verified available quantities and part thresholds |
| Handovers | Incoming/outgoing personnel and related work context resolve; no real identity verification implied |
| Existing components | Earlier apps, approval flows, 500 work orders and parent records unchanged |
| Safe operation | No real supplier email, automated stock movement, electrical work or live facility integration |

Review the published model-driven app through **Play** and verify forms, views, lookup navigation, selected records and user permissions. Save and publish again if any form/view change was made after the first app publication.

### Finish Part 11

You now have a connected **Supporting Operations Hub** for fictional vendor coordination, spare catalog management, per-hall stock visibility and shift handover notes. The four new Dataverse tables reuse the existing Assets, Data Halls, Employees, Incidents, Work Orders and Changes. The training data demonstrates what the next shift needs to know and which spare parts need review—without pretending that manual counts or handover flags are authenticated operational controls.



---

## Part 12 — Plan Data Hall Rack Capacity and Power Headroom

Part 11 connected shift operations to suppliers, spares and work orders. Now we continue in **the same solution** with capacity planning: the fictional **Pacific Resilience Campus** contains **Data Hall 01** and **Data Hall 02**, 100 assets and 20 existing Server Rack assets. You will build the four planning registers and the **DC Capacity Planner** desktop Canvas App, linking rack positions, planned power, reservations and requests without duplicating the equipment register.

Use only an authorized learning environment and fictitious records. Verify saved metadata, field types, row relationships and the **published app version** before completing the chapter. The calculations represent a training planning model, never real facility telemetry or an authenticated capacity reservation.

We will create four small planning tables, reusing the existing Data Hall, Asset and Employee references:

| New table | Why it exists |
| --- | --- |
| `DC Hall Planning Baseline` | One explicit fictional planning load snapshot and reserve margin per hall |
| `DC Rack Plan` | One planning record linked to each existing Server Rack asset; total U and allowable planning power |
| `DC Rack Allocation` | Proposed or reserved U-ranges and planning power for a particular rack |
| `DC Capacity Request` | Requests for prospective space/power; not real purchase orders or approvals |

By the end, a learner should be able to inspect the existing 20 racks, compare free rack units and reserved kW, propose a nonoverlapping allocation, recognize a deliberate conflict, and create a separate capacity request. **A request is not an allocation; a saved allocation is not a live device load; a Data Hall design rating is not its real spare capacity.**

### S12.01 — Confirm prerequisite records and define the planning model

Open [make.powerapps.com](https://make.powerapps.com), choose your authorized development environment, and open **Solutions → SunnyVerse Data Center Operations 360**. Confirm the existing records before creating anything:

| Reference | Existing target | What to inspect |
| --- | --- | --- |
| DC Campus | Pacific Resilience Campus | Existing campus record; no duplicate |
| DC Data Hall | Data Hall 01; Data Hall 02 | Hall 01 Design IT Capacity = **2,350.00 kW**; Hall 02 = **2,500.00 kW** |
| DC Asset | 20 Server Rack records | `Server Rack 001` through `Server Rack 020`, category Server Rack, codes `DC-RACK-001` through `DC-RACK-020` |
| DC Asset | Rack status | Rack 013 is **Standby** and Rack 019 is **Under Maintenance**; do not silently treat these as available |
| DC Employee Profile | Existing 20 fictional people | Optional request originator Lookup only; no user authentication assumption |

The existing `assets.csv` assigns odd-numbered racks to Data Hall 01 and even-numbered racks to Data Hall 02. Its `Rated Power kW = 30.00` values are **illustrative equipment nameplate data**, not live rack consumption or available planning capacity. In this lesson we select a separate conservative fictional **Rack Power Budget kW = 20.00** for each rack. Do not combine or sum rated values as facility telemetry.

A **rack unit (U)** is a space height measure; a 42U rack has 42 integer U positions. **Reserved U** is a planned space commitment, not a measured percentage of occupied hardware. A **hall planning baseline** is a manually selected, fixed illustrative load; the design capacity only enters a *planning arithmetic model* after a baseline and buffer are explicitly supplied. These three concepts are not interchangeable.

The project is educational and uses only fake inputs. If the previously published tables are missing from the actual environment, first resolve the earlier lesson without creating substitute parent records.

### S12.02 — Create DC Hall Planning Baseline and its columns

Inside the solution choose **New → Table**, using the advanced table settings where necessary:

| Table property | Enter |
| --- | --- |
| Display / plural | `DC Hall Planning Baseline` / `DC Hall Planning Baselines` |
| Description | `Fictional dated load and reserve assumptions used only for capacity planning exercises.` |
| Type / ownership | Standard / **Organization** |
| Primary name | `Baseline Name` (Business required; reopen after saving) |
| Table schema target | `svrg_DCHallPlanningBaseline` |
| Primary-name schema target | `svrg_BaselineName` |

Add the business columns. Set their saved description, required level, data type, limits, behavior, defaults and actual schema as shown. Use `Done` for each and **Save table** if offered. After the table is created, reopen **Baseline Name → Edit column** and explicitly set **Business required** if the creation dialog saved Optional. Verify that setting again after saving; repeat this primary-name verification on the other three new tables.

| Exact display name / CSV header | Target schema | Type / Required | Other properties and meaning |
| --- | --- | --- | --- |
| Baseline Name | `svrg_BaselineName` | Primary Text / Business required | Human-readable fictional snapshot; created with the table |
| Baseline Code | `svrg_BaselineCode` | Text / Business required | Max 24; Searchable Yes; unique business reference |
| Baseline IT Load kW | `svrg_BaselineITLoadkW` | Decimal / Business required | Precision 2; minimum 0; fictional existing hall load *before* Part 12's new reservations |
| Planning Reserve kW | `svrg_PlanningReservekW` | Decimal / Business required | Precision 2; minimum 0; explicit protected planning margin |
| Baseline As Of | `svrg_BaselineAsOf` | Date Only / Business required | Date only; no automatic time conversion |
| Basis Notes | `svrg_BasisNotes` | Multiline Text / Optional | Max 2,000; record assumptions, never source-of-truth telemetry |
| Active | `svrg_Active` | Yes/No / Optional | Default Yes; marks the active exercise baseline |

Plan one **Many-to-one** relationship from **DC Hall Planning Baseline** to existing **DC Data Hall**, giving it a Business required **Data Hall** Lookup (`svrg_DataHall`). Create that relationship **once in S12.06**, after all four tables exist, using Restrict Delete and No cascade where supported. Do not also create a Text hall field. Create an alternate key **DC Baseline Code Key** based only on `Baseline Code`; wait for **Active**. Because a hall may have multiple *dated* baselines, the key is the Baseline Code, not the Hall Lookup alone. For this lesson, choose one active baseline per hall; the application does not automatically enforce that policy across all possible future rows.

After completing the Data Hall Lookup in S12.06, enter the two fictional baseline records directly in the table editor or a form:

| Baseline Code | Baseline Name | Data Hall | Baseline IT Load kW | Planning Reserve kW | Baseline As Of | Active |
| --- | --- | --- | ---: | ---: | --- | --- |
| `HBL-0001` | Hall 01 Training Baseline | Data Hall 01 | 1800.00 | 100.00 | 2026-11-05 | Yes |
| `HBL-0002` | Hall 02 Training Baseline | Data Hall 02 | 1850.00 | 150.00 | 2026-11-05 | Yes |

The initial modeled headroom **before new reserved allocations** is **450.00 kW** for Hall 01 and **500.00 kW** for Hall 02: 2350−1800−100 and 2500−1850−150. These are illustrative model outputs, not measured facility headroom. Save, leave the grid, and reopen both rows.

### S12.03 — Create DC Rack Plan and its planning fields

Create one Standard, Organization-owned table with:

| Table property | Enter |
| --- | --- |
| Display / plural | `DC Rack Plan` / `DC Rack Plans` |
| Description | `Fictional rack-unit and planning-power budgets linked to existing server rack assets.` |
| Primary name | `Rack Plan Name`, Business required |
| Table schema target | `svrg_DCRackPlan` |
| Primary schema target | `svrg_RackPlanName` |

Add the following. The last two columns are Lookups, created *after* the regular columns via S12.06:

| Exact display / header | Target schema | Type / Required | Configuration |
| --- | --- | --- | --- |
| Rack Plan Name | `svrg_RackPlanName` | Primary Text / Business required | Existing primary name; no duplicate |
| Rack Plan Code | `svrg_RackPlanCode` | Text / Business required | Max 24; Searchable Yes; match rack asset code in this training set |
| Total Rack Units | `svrg_TotalRackUnits` | Whole number / Business required | Minimum 1; maximum 52; **no column default—enter 42 explicitly per Rack Plan record/import row** |
| Rack Power Budget kW | `svrg_RackPowerBudgetkW` | Decimal / Business required | Precision 2; minimum 0; training budget 20.00 |
| Planning Status | `svrg_PlanningStatus` | **Local single Choice** / Business required | `Available`, `Hold`, `Retired`; no default |
| Active | `svrg_Active` | Yes/No / Optional | Default Yes |
| Planning Notes | `svrg_PlanningNotes` | Multiline Text / Optional | Max 2,000; note constraints and training assumptions |
| Asset | `svrg_Asset` | **Lookup to DC Asset** / Business required | Reuse an existing Server Rack row; verified relationship |
| Data Hall | `svrg_DataHall` | **Lookup to DC Data Hall** / Business required | Must agree with that Asset's Data Hall |

Create the **DC Rack Plan Code Key** on Rack Plan Code; wait for Active. In the verified authoring pattern, Whole Number fields do not provide an editable column default; keep the saved column without a default and enter **42** in every training row. Do not confuse the record value with a Dataverse column default. Do **not** create a second asset register and do not rely on a plain text Asset Code in place of the relationship. The single-select status is a **local Choice**, not a shared global option set. Save its labels in the given order and retain the generated numeric values.

For this lesson, 20 Rack Plans correspond to the 20 existing Server Rack assets. The linked practice CSV has the same **display-name headers** as the new table, with Asset and Data Hall represented by existing primary names for lookup mapping. Rack 013 (Standby) and Rack 019 (Under Maintenance) start on **Hold**. The other 18 start on **Available**. This holds training reservations away from assets not in service.

### S12.04 — Create DC Rack Allocation to reserve an exact U-range

Create a Standard, Organization-owned table with display **DC Rack Allocation**, plural **DC Rack Allocations**, primary name **Allocation Name** (Business required), table schema target `svrg_DCRackAllocation`, primary schema target `svrg_AllocationName`, and description `Fictional rack-space and power planning allocations with an explicit reserved flag.`

| Exact display / header | Target schema | Type / Required | Configuration |
| --- | --- | --- | --- |
| Allocation Name | `svrg_AllocationName` | Primary Text / Business required | Readable workload label |
| Allocation Code | `svrg_AllocationCode` | Text / Business required | Max 24; Searchable Yes |
| Start U | `svrg_StartU` | Whole number / Business required | Minimum 1; maximum 52; first rack-unit position |
| Units Reserved | `svrg_UnitsReserved` | Whole number / Business required | Minimum 1; maximum 52; contiguous U-space length |
| Power Reserved kW | `svrg_PowerReservedkW` | Decimal / Business required | Precision 2; minimum 0; planned kW |
| Allocation Status | `svrg_AllocationStatus` | Local single Choice / Business required | `Draft`, `Reserved`, `Released`, `Cancelled`; no default |
| Capacity Reserved | `svrg_CapacityReserved` | Yes/No / Optional | Default No; **must be Yes exactly when reservation should consume capacity** |
| Requested On | `svrg_RequestedOn` | Date Only / Optional | Date only; fictional request date |
| Allocation Notes | `svrg_AllocationNotes` | Multiline Text / Optional | Max 2,000 |
| Rack Plan | `svrg_RackPlan` | Lookup to DC Rack Plan / Business required | Existing saved Rack Plan |
| Data Hall | `svrg_DataHall` | Lookup to DC Data Hall / Business required | Must match that Rack Plan's hall; aids hall-level filters |
| Related Request | `svrg_RelatedRequest` | Lookup to DC Capacity Request / Optional | Added after request table exists; optional linkage |

Create **DC Allocation Code Key** on Allocation Code and wait for Active. The Date Only field is not a live activation timestamp. `Capacity Reserved` is an explicit, manually maintained educational projection flag. A `Reserved` Choice without `Capacity Reserved = Yes`, or `Released` with Yes, would make the calculations misleading. We will test and inspect both fields on every sample row; Part 12 does not provide a server-side rule guaranteeing consistency across integrations.

Important validations before a new row is saved: `Start U ≥ 1`; `Units Reserved ≥ 1`; `Start U + Units Reserved − 1 ≤ Total Rack Units`; planned kW is nonnegative; no overlap with a previously reserved U-range for the same rack; and planned total rack power must stay within its budget. The app demonstrates these checks, but client-side validation alone does not prevent a simultaneous competing user, an import or an external API call from bypassing the rule. **Do not claim transaction-safe capacity booking.**

### S12.05 — Create DC Capacity Request for prospective demand

Create **DC Capacity Request** / **DC Capacity Requests**, Standard / Organization ownership; primary name **Request Name** (Business required), target schema `svrg_DCCapacityRequest`, target primary name `svrg_RequestName`, description `Fictional requests for future rack units and planning power, independent of allocations.`

| Exact display / header | Target schema | Type / Required | Configuration |
| --- | --- | --- | --- |
| Request Name | `svrg_RequestName` | Primary Text / Business required | Readable request title |
| Request Code | `svrg_RequestCode` | Text / Business required | Max 24; Searchable Yes |
| Requested Units | `svrg_RequestedUnits` | Whole number / Business required | Minimum 1; maximum 52 |
| Requested Power kW | `svrg_RequestedPowerkW` | Decimal / Business required | Precision 2; minimum 0 |
| Request Status | `svrg_RequestStatus` | Local single Choice / Business required | `Draft`, `Ready for Review`, `Planned`, `Withdrawn`; no default |
| Needed By | `svrg_NeededBy` | Date Only / Optional | Projected date; no promise of delivery |
| Business Justification | `svrg_BusinessJustification` | Multiline Text / Business required | Max 2,000; fictional explanation |
| Review Notes | `svrg_ReviewNotes` | Multiline Text / Optional | Max 2,000 |
| Data Hall | `svrg_DataHall` | Lookup to DC Data Hall / Business required | Destination hall |
| Preferred Rack Plan | `svrg_PreferredRackPlan` | Lookup to DC Rack Plan / Optional | Candidate rack, not an actual reservation |
| Requested By Employee | `svrg_RequestedByEmployee` | Lookup to DC Employee Profile / Optional | Fictional directory context only |

Create the **DC Capacity Request Code Key** on Request Code and inspect **Keys** until its status is **Active**. It may show **Pending** during the background index operation; do not insert duplicate-prone records or create another key while that operation runs. A `Planned` state is a manual exercise label, not an enterprise approval. A request does **not** subtract space or power: only allocations with `Capacity Reserved = Yes` do so. Do not create a new cloud flow or send an approval message in Part 12.

### S12.06 — Create and verify the nine real Lookup relationships

Open each **current table → Schema → Relationships → New relationship → Many-to-one**. Select the **related table** exactly as shown. Set **Restrict Delete** and No cascade for Assign/Share/Unshare/Reparent/Merge when available; inspect the actual saved settings. A relationship auto-creates the Lookup column—do not add that same name again as Text.

| Current table | Lookup display name / target schema | Related table | Required |
| --- | --- | --- | --- |
| DC Hall Planning Baseline | Data Hall / `svrg_DataHall` | DC Data Hall | Business required |
| DC Rack Plan | Asset / `svrg_Asset` | DC Asset | Business required |
| DC Rack Plan | Data Hall / `svrg_DataHall` | DC Data Hall | Business required |
| DC Rack Allocation | Rack Plan / `svrg_RackPlan` | DC Rack Plan | Business required |
| DC Rack Allocation | Data Hall / `svrg_DataHall` | DC Data Hall | Business required |
| DC Rack Allocation | Related Request / `svrg_RelatedRequest` | DC Capacity Request | Optional |
| DC Capacity Request | Data Hall / `svrg_DataHall` | DC Data Hall | Business required |
| DC Capacity Request | Preferred Rack Plan / `svrg_PreferredRackPlan` | DC Rack Plan | Optional |
| DC Capacity Request | Requested By Employee / `svrg_RequestedByEmployee` | DC Employee Profile | Optional |

This design adds **nine** new Lookups. Verify all nine by reopening each relationship and a sample referenced record. Match existing parent records by their saved primary names, or resolve their real record IDs before a supported API upsert; **a plain business code in a CSV is not itself an automatically resolved Dataverse Lookup**. The three links associated with Allocation are created only after both Rack Plan and Capacity Request exist; this is why the table creation order precedes the relationships. Likewise, the Baseline Data Hall link is created **here once**, not earlier in S12.02. When a builder has already created a correct Lookup, inspect and reuse it rather than duplicating it.

**Cross-reference rule:** The Hall on a Rack Plan must match the Hall on its linked Asset; the Hall on an Allocation must match its Rack Plan's Hall; the Hall on a Request must match its preferred Rack if one is selected. Required Lookups alone do not enforce these equality rules; verify them in the form and sample tests, and treat server-side validation as a future enterprise hardening task.

### S12.07 — Populate the rack planning reference, without duplicating Assets

Download the new practice file [`rack-plans.csv`](./data/rack-plans.csv) before importing. Its first line is:

```csv
Rack Plan Name,Rack Plan Code,Total Rack Units,Rack Power Budget kW,Planning Status,Active,Planning Notes,Asset,Data Hall
```

This 20-row original synthetic dataset corresponds to the existing Server Rack assets. Its headers use Dataverse display names, but the two Lookup columns still require explicit reference mapping. Download the linked CSV before importing.

Open **DC Rack Plan → Import from CSV** in a Dataverse import experience that supports Lookup Reference mapping, select `rack-plans.csv`, and use **Review Mapping**. If the designer cannot reliably resolve Lookup references from a business code, **stop before importing**. Resolve the existing Asset and Hall records to their actual Dataverse IDs using an authorized supported data tool and load the same rows by the Active Rack Plan Code alternate key with proper Lookup bindings, or use the standard record form and actual Lookup picker. After importing, reread every row and its referenced parents; do not assume that a successful import status proves correct relationships. Match Text, Whole Number, Decimal and Boolean columns by their exact display names. Map Planning Status labels to the existing local Choice options. For the **Asset** Lookup, choose `DC Asset → Asset Name`; source values are `Server Rack 001` … `Server Rack 020`. For **Data Hall**, choose `DC Data Hall → Hall Name`; source values are Data Hall 01/02. Do not point either lookup at a GUID field or free-text column. If the wizard cannot set Lookup References, do not force the import—use a supported import route or enter the 20 records through the editor with real pickers.

Use one creation method only, and verify count before rerunning. Inspect the 20 rows after a completed import and select three references from the grid: Rack 001 → Server Rack 001 → Hall 01, Rack 002 → Server Rack 002 → Hall 02, and Rack 019 → Server Rack 019 → Hall 01 with **Planning Status = Hold**. Check Rack 013 is also on Hold. Every Total Rack Units value is 42 and every **planning** budget is 20.00 kW.

Create these two **DC Hall Planning Baseline** rows from S12.02 first if they have not yet been saved. Reopen them before proceeding. Do not import a second copy if the records already exist.

### S12.08 — Add the three starting allocations and two capacity requests

Use the table's New form or the editable data grid. Choose real Lookup records using the record picker and enter the following exact fictional examples:

| Allocation Code | Allocation Name | Rack Plan / Hall | Start U | Units Reserved | End U (calculated) | Power Reserved kW | Status | Capacity Reserved |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| `ALC-0001` | UPS Analytics Pilot | DC-RACK-001 / Hall 01 | 1 | 8 | 8 | 4.00 | Reserved | Yes |
| `ALC-0002` | Telemetry Collector Trial | DC-RACK-001 / Hall 01 | 12 | 6 | 17 | 3.00 | Reserved | Yes |
| `ALC-0003` | Cooling Diagnostic Simulation | DC-RACK-002 / Hall 02 | 1 | 10 | 10 | 5.00 | Reserved | Yes |

`End U` is explained and calculated as `Start U + Units Reserved − 1`, **not** created as a new Dataverse column. For Rack 001, the reserved positions are 1–8 and 12–17, leaving **28** U by total count. There are 3 unreserved U positions in the gap at 9–11, illustrating why total free units alone is not enough to guarantee a contiguous placement. Rack 001 has 7.00 kW reserved and **13.00 kW** of its 20.00 kW budget unreserved. Rack 002 has 10U reserved and 5.00 kW reserved, leaving 32U and 15.00 kW in the simplified plan.

Add these two requests *separately*—a request does not change reservation totals:

| Request Code | Request Name | Data Hall | Preferred Rack Plan | Requested Units | Requested Power kW | Request Status | Business Justification |
| --- | --- | --- | --- | ---: | ---: | --- | --- |
| `REQ-0001` | Monitoring Dashboard Pilot | Data Hall 01 | DC-RACK-001 | 5 | 3.00 | Draft | Fictional analytics workload planning exercise. |
| `REQ-0002` | Lab Workload Expansion | Data Hall 02 | DC-RACK-002 | 10 | 12.00 | Ready for Review | Fictional expansion capacity review. |

REQ-0002 represents 12.00 kW of prospective demand. Rack 002 currently has 5.00 kW reserved, so a later accepted 12.00 kW allocation would total 17.00 kW, within its 20.00 kW budget; however, a request alone does not consume capacity. Later examples should evaluate both power and U position constraints.

**Hall planning arithmetic:** Because the baseline inputs deliberately exclude the **new reserved allocations**, the simplified model computes:

`Modeled Hall Headroom = Hall Design IT Capacity − Baseline IT Load − Planning Reserve − Sum(New Part 12 Allocations with Capacity Reserved = Yes)`.

At the starting state: Hall 01 = **2,350 − 1,800 − 100 − (4 + 3) = 443 kW**. Hall 02 = **2,500 − 1,850 − 150 − 5 = 495 kW**. These are not live DCIM measurements. If someone changes or replaces the baseline, re-evaluate the model; do not count an allocation in both the baseline and the new sum.

### S12.09 — Build the DC Capacity Planner desktop Canvas App

Inside **Solutions → SunnyVerse Data Center Operations 360**, choose **New → App → Canvas app** (or New app within the solution). Name it exactly **DC Capacity Planner** and select **Tablet / landscape**. In **Data**, connect these existing Dataverse tables: `DC Hall Planning Baselines`, `DC Rack Plans`, `DC Rack Allocations`, `DC Capacity Requests`, `DC Data Halls`, and `DC Assets`. Also connect `DC Employee Profiles` only if the optional request-originator field is shown in an app form. Insert the documented Classic Label, Button, Text input, Gallery and Form controls; the authoring studio may already choose Classic controls by default. **Classic text inputs use `.Text`**, whereas Modern inputs may use `.Value`. If an Insert operation does not create the control, verify the Tree view before retrying. Supported paste-as-code can add compatible **controls inside an existing blank screen**; it does not paste a complete `Screen` object. Avoid unescaped colon-space sequences in inline YAML text and place longer formulas in multiline blocks when pasting. For Classic forms, leave unsupported pasted properties such as `Columns` at their saved defaults rather than forcing them.

Use the same restrained navy / teal visual language as the previously published Command Center. Functional formulas come first. In **App → OnStart**, set:

```powerfx
Set(varCapacityNavy, ColorValue("#123A56"));
Set(varCapacityTeal, ColorValue("#147D86"));
Set(varCapacityBg, ColorValue("#F3F7FA"));
Set(varRack, First('DC Rack Plans'));
Set(varRack, Blank());
Set(varHall, First('DC Data Halls'));
Set(varHall, Blank());
Set(varRequest, First('DC Capacity Requests'));
Set(varRequest, Blank());
Set(varAllocationValid, false)
```

Assign each record variable from a **typed Dataverse table** before clearing it to Blank. This establishes a record type that later formulas can use; a blank-only assignment can leave Power Fx without enough type information. These first-row assignments do not create or edit any record. Run **App → Run OnStart** once after adding the formula, if the editor offers that command. Do not count on OnStart rerunning on every screen navigation. Set each screen **Fill = varCapacityBg**. Use a meaningful text label for every status, not color alone.

Create and rename six blank screens in Tree view:

| Screen | Purpose | Named controls to add |
| --- | --- | --- |
| `scrCapacityHome` | Model boundaries, hall planning snapshot and navigation | `lblCapacityTitle`, `galHallBaselines`, `lblScopeNotice`, `btnBrowseRacks`, `btnBrowseRequests`, `btnRefreshCapacity` |
| `scrRackBrowse` | Browse 20 racks and select a plan | `lblRackBrowseTitle`, `txtRackSearch`, `galRackPlans`, `btnRackBrowseHome`, `btnRackBrowseRefresh` |
| `scrRackDetail` | Selected rack's U/power budget and existing allocations | `lblRackTitle`, `lblRackTotalU`, `lblRackReservedU`, `lblRackFreeU`, `lblRackBudgetKW`, `lblRackReservedKW`, `lblRackFreeKW`, `galRackAllocations`, `btnProposeAllocation`, `btnRackDetailBack` |
| `scrAllocationEdit` | Create a draft or reserved allocation with explicit validation | `lblAllocationTitle`, `frmAllocation`, `btnValidateAllocation`, `btnSaveAllocation`, `btnCancelAllocation`, `lblAllocationCheck`, `txtAllocStartU`, `txtAllocUnits`, `txtAllocPowerKw` (rename the three inner form inputs) |
| `scrRequestBrowse` | Browse existing planning requests | `lblRequestBrowseTitle`, `galCapacityRequests`, `btnNewRequest`, `btnRequestBrowseHome`, `btnRequestRefresh` |
| `scrRequestEdit` | Create or edit an educational capacity request | `lblRequestEditTitle`, `frmCapacityRequest`, `btnSaveRequest`, `btnCancelRequest`, `lblRequestError` |

For each inserted Label or Button, set its **Text** to its intended readable caption. For galleries choose a vertical layout; keep a visible text name and one useful secondary field. Use screen-specific rectangles only as optional visuals; never cover form controls. Keep total App instances one: updating an app is not the same as creating it again.

### S12.10 — Set the exact navigation and read-only calculation formulas

The formulas below use the suggested English display names and the Dataverse table names described above. **Power Apps may expose option sets or relationships under slightly different identifiers.** Use IntelliSense to confirm the generated names after adding each real data source. Do not paste code blindly when your saved schema differs. Formulas are intended for a small 20-rack educational dataset; test all delegation warnings, especially aggregates over child records.

**Home navigation:**

| Control/property | Formula |
| --- | --- |
| `btnBrowseRacks.Text` | `"Browse rack capacity"` |
| `btnBrowseRacks.OnSelect` | `Navigate(scrRackBrowse, ScreenTransition.Fade)` |
| `btnBrowseRequests.Text` | `"Capacity requests"` |
| `btnBrowseRequests.OnSelect` | `Navigate(scrRequestBrowse, ScreenTransition.Fade)` |
| `btnRefreshCapacity.OnSelect` | `Refresh('DC Hall Planning Baselines'); Refresh('DC Rack Plans'); Refresh('DC Rack Allocations'); Refresh('DC Capacity Requests')` |
| `lblScopeNotice.Text` | `"SIMULATED capacity planning — not live power or reserved physical infrastructure"` |
| `galHallBaselines.Items` | `Filter('DC Hall Planning Baselines', Active = true)` |
| `galRackPlans.Items` | `Sort(Filter('DC Rack Plans', IsBlank(txtRackSearch.Text) || StartsWith('Rack Plan Code', txtRackSearch.Text)), 'Rack Plan Code', SortOrder.Ascending)` |
| `galRackPlans.OnSelect` or an inner row button | `Set(varRack, ThisItem); Navigate(scrRackDetail, ScreenTransition.Fade)` |
| `btnRackBrowseHome.OnSelect` | `Navigate(scrCapacityHome, ScreenTransition.Fade)` |
| `btnRackBrowseRefresh.OnSelect` | `Refresh('DC Rack Plans')` |
| `galCapacityRequests.Items` | `Sort('DC Capacity Requests', 'Request Code', SortOrder.Ascending)` |
| `btnRequestBrowseHome.OnSelect` | `Navigate(scrCapacityHome, ScreenTransition.Fade)` |

Choose `scrRackDetail` in Tree view and set **OnVisible** to:

```powerfx
Refresh('DC Rack Allocations');
ClearCollect(
    colRackReservations,
    Filter('DC Rack Allocations', 'Rack Plan'.'DC Rack Plan' = varRack.'DC Rack Plan' && 'Capacity Reserved' = 'Capacity Reserved (DC Rack Allocations)'.Yes)
)
```

This code is a **small-data client collection**. It is appropriate for validating only the published training scale after confirming no delegation warning affects the filtered results. `ClearCollect` is not a server-side lock or full-dataset query. Compare the Lookup **primary key** (`'Rack Plan'.'DC Rack Plan'`) to the selected Rack Plan ID rather than comparing entire records; this avoids nondeterministic record equality and supports the intended delegable filter. In this form, the Yes/No **Capacity Reserved** value is exposed as a typed Choice, so use `'Capacity Reserved (DC Rack Allocations)'.Yes` in formulas rather than an untyped Boolean. If more racks or allocations are introduced later, replace this pattern with a validated delegable/server-side calculation.

For the selected Rack display labels, set **Text** to the formulas:

| Label | Formula |
| --- | --- |
| `lblRackTitle` | `varRack.'Rack Plan Name'` |
| `lblRackTotalU` | `"Total U: " & Text(varRack.'Total Rack Units')` |
| `lblRackReservedU` | `"Reserved U: " & Text(Sum(colRackReservations, 'Units Reserved'))` |
| `lblRackFreeU` | `"Unreserved U: " & Text(varRack.'Total Rack Units' - Sum(colRackReservations, 'Units Reserved'))` |
| `lblRackBudgetKW` | `"Budget kW: " & Text(varRack.'Rack Power Budget kW', "0.00")` |
| `lblRackReservedKW` | `"Reserved kW: " & Text(Sum(colRackReservations, 'Power Reserved kW'), "0.00")` |
| `lblRackFreeKW` | `"Unreserved kW: " & Text(varRack.'Rack Power Budget kW' - Sum(colRackReservations, 'Power Reserved kW'), "0.00")` |
| `galRackAllocations.Items` | `Filter('DC Rack Allocations', 'Rack Plan'.'DC Rack Plan' = varRack.'DC Rack Plan')` |
| `btnRackDetailBack.OnSelect` | `Navigate(scrRackBrowse, ScreenTransition.Fade)` |

`Sum(colRackReservations, ...)` totals only saved allocations explicitly marked `Capacity Reserved = Yes`. A request record does not appear here. **Free U count does not promise a contiguous block**: racks can have holes between placements. A separate interval-overlap check follows.

For the Home hall snapshot, use a label in `galHallBaselines` to display the baseline only:

```powerfx
"Baseline modeled headroom before new allocations: " &
Text(
    ThisItem.'Data Hall'.'Design IT Capacity kW' -
    ThisItem.'Baseline IT Load kW' -
    ThisItem.'Planning Reserve kW',
    "0.00"
) & " kW"
```

Inspect the actual related Data Hall field in IntelliSense. If the lookup expansion is not available in your editor, retrieve the existing Hall row using LookUp on `DC Data Halls` and the selected Hall primary name, instead of replacing the reference with Text. This Home label intentionally shows **baseline headroom before allocations**, not the 443/495 kW totals. Show those totals separately only after verifying the child allocation aggregation for the actual Hall. Never label either number as measured energy consumption.

### S12.11 — Configure the allocation form and the conflict-check action

Open `scrAllocationEdit` and insert **Edit form**, rename it `frmAllocation`, set **DataSource = 'DC Rack Allocations'** and **Item = Defaults('DC Rack Allocations')** for new-only exercises. Add cards for Allocation Name, Allocation Code, Start U, Units Reserved, Power Reserved kW, Allocation Status, Capacity Reserved, Requested On, Allocation Notes, Rack Plan, Data Hall and Related Request. Select each numeric card's inner **Classic Text input** and rename it `txtAllocStartU`, `txtAllocUnits` or `txtAllocPowerKw`. Keep its parent DataCard's `Update` property as the appropriately typed `Value(txtAlloc...Text)`; do not accidentally submit numeric strings. Keep the Lookup cards as typed Dataverse record pickers and the Choice card as an Option Set—not a text box. For this Dataverse form, set the **Capacity Reserved** card's typed `Default` and `Update` using the saved option set (for this project, `'Capacity Reserved (DC Rack Allocations)'.Yes` for consuming reservations), not literal `true`; verify whether a newly generated card uses the same option-set identifier.

For this **new-only Reserved allocation** exercise, bind the typed Lookup cards to the rack chosen on `scrRackDetail`. Unlock the **Rack Plan** data card and set its **Update** to `varRack`; unlock **Data Hall** and set its **Update** to `varRack.'Data Hall'`. Keep a read-only label showing each selected record, and prevent the user from choosing a different rack or hall on this screen. Verify that the cards submit Dataverse records, not text. Keep the **Allocation Status** and **Capacity Reserved** cards in the form: set their **Update** to the typed **Reserved** local Choice (choose the actual enum member using IntelliSense) and Boolean `true`, respectively. Do not use the text string `"Reserved"` for a Choice field. Test all four typed updates by saving and reopening one valid sample row before adding more. For later changes from Reserved to Released or Cancelled, use the standard Dataverse form after applying the appropriate manual Capacity Reserved flag.

```powerfx
Set(varAllocationValid, false);
NewForm(frmAllocation);
Navigate(scrAllocationEdit, ScreenTransition.Fade)
```

Set `btnValidateAllocation.OnSelect` to the following deliberately explicit client-side check:

```powerfx
Set(varStartU, IfError(Value(txtAllocStartU.Text), Blank()));
Set(varUnits, IfError(Value(txtAllocUnits.Text), Blank()));
Set(varNewPowerKW, IfError(Value(txtAllocPowerKw.Text), Blank()));
Set(varEndU, varStartU + varUnits - 1);
Refresh('DC Rack Allocations');
ClearCollect(
    colRackReservations,
    Filter('DC Rack Allocations', 'Rack Plan' = varRack && 'Capacity Reserved' = true)
);
Set(
    varAllocationValid,
    !IsBlank(varStartU) && !IsBlank(varUnits) && !IsBlank(varNewPowerKW) &&
    varStartU >= 1 && varUnits >= 1 && varNewPowerKW >= 0 &&
    varStartU = RoundDown(varStartU, 0) &&
    varUnits = RoundDown(varUnits, 0) &&
    varEndU <= varRack.'Total Rack Units' &&
    varRack.Active = true &&
    varRack.'Planning Status' = 'Planning Status (DC Rack Plans)'.Available &&
    CountRows(
        Filter(
            colRackReservations,
            'Start U' <= varEndU &&
            ('Start U' + 'Units Reserved' - 1) >= varStartU
        )
    ) = 0 &&
    Sum(colRackReservations, 'Power Reserved kW') + varNewPowerKW <=
        varRack.'Rack Power Budget kW'
);
If(
    varAllocationValid,
    Notify("The rack-space and power checks pass for this demo.", NotificationType.Success),
    Notify("Allocation is invalid, overlaps a reserved U-range, is on hold, or exceeds the planned budget.", NotificationType.Error)
)
```

Use `lblAllocationCheck.Text = If(varAllocationValid, "Demo validation passed — review fields before saving", "Validate the allocation first")`. The check reads the selected `varRack` and currently saved reservations. The two Lookup DataCards must remain bound to that rack and its hall; verify the first submitted row by reopening it in Dataverse. These client-side checks are not a substitute for transaction-safe server validation.

**Choice type check:** Power Fx compares Dataverse Choices against a typed enum member, not a displayed or translated text label. The example `'Planning Status (DC Rack Plans)'.Available` illustrates the intended local Choice reference. IntelliSense might present a different generated option-set name in your saved environment; choose the **Available** member of the actual local Choice and re-test. Do not replace a Choice with a Text column just to silence an error.

Set `varAllocationValid` to **false** before every new form session. In the **OnChange** of each of the three numeric text inputs, the Rack Plan Lookup picker, the Data Hall Lookup picker, and the `Capacity Reserved` or Allocation Status selection controls, set:

```powerfx
Set(varAllocationValid, false)
```

The Rack Plan and Data Hall form cards must submit the selected `varRack` and its related hall as typed Lookup records. In some editor/view configurations, a locked Lookup card may show blank display text even though the saved reference is valid; show the selected Rack/Hall in a separate read-only title and confirm the actual Lookup bindings by reopening the saved Dataverse record. A blank display label is not proof of a blank stored relationship. If these field values or the Choice update cannot be verified after the first save, disable Save and keep this screen read-only; enter valid sample rows with a supported Dataverse form until the bindings are corrected.

Set `btnSaveAllocation.DisplayMode` to `If(varAllocationValid, DisplayMode.Edit, DisplayMode.Disabled)` and `btnSaveAllocation.OnSelect` to:

```powerfx
If(
    varAllocationValid,
    Set(varAllocationValid, false);
    SubmitForm(frmAllocation),
    Notify("Validate the selected rack, hall, space and power first.", NotificationType.Error)
)
```

Set `frmAllocation.OnSuccess` to:

```powerfx
Notify("Training allocation saved", NotificationType.Success);
Refresh('DC Rack Allocations');
Set(varAllocationValid, false);
Navigate(scrRackDetail, ScreenTransition.Fade)
```

Set `frmAllocation.OnFailure` to `Notify(frmAllocation.Error, NotificationType.Error)`, `btnCancelAllocation.OnSelect` to `ResetForm(frmAllocation); Set(varAllocationValid, false); Navigate(scrRackDetail, ScreenTransition.Fade)`, and `frmAllocation.Item` to `Defaults('DC Rack Allocations')` if keeping this as a new-only form. Invalidate the validation flag whenever a reservation-related input changes and re-run validation before using Save. The Save button requires the latest successful check but does not prevent concurrent or external writes; do not present it as a transaction-safe booking operation.

A Canvas App query and form submission are **not an atomic booking transaction**. Include that limitation in the success message and learner demonstration, and keep client-side validation distinct from server-side enforcement. Concurrent makers can pass the same pre-check and still save overlapping reservations. This must be stated in the lesson and in its portfolio evidence. For a real solution, use a server-side enforcement design, concurrency rules and tests before calling a slot reserved.

### S12.12 — Capacity requests, negative tests and publish

On `scrRequestBrowse`, set `btnNewRequest.OnSelect`:

```powerfx
Set(varRequest, Blank());
NewForm(frmCapacityRequest);
Navigate(scrRequestEdit, ScreenTransition.Fade)
```

In `scrRequestEdit`, insert an **Edit form** `frmCapacityRequest`, set **DataSource = 'DC Capacity Requests'**, Item `Defaults('DC Capacity Requests')` for new requests, and include cards for Request Name, Request Code, Requested Units, Requested Power kW, Request Status, Needed By, Business Justification, Review Notes, Data Hall, Preferred Rack Plan and optionally Requested By Employee. Use the form's typed lookup pickers, not text copies. Set `btnSaveRequest.OnSelect = SubmitForm(frmCapacityRequest)`. Set `frmCapacityRequest.OnSuccess` to `Notify("Training request saved", NotificationType.Success); Refresh('DC Capacity Requests'); Navigate(scrRequestBrowse, ScreenTransition.Fade)` and `frmCapacityRequest.OnFailure` to `Notify(frmCapacityRequest.Error, NotificationType.Error)`. Set `btnCancelRequest.OnSelect = ResetForm(frmCapacityRequest); Navigate(scrRequestBrowse, ScreenTransition.Fade)` and `lblRequestError.Text = frmCapacityRequest.Error`. A saved request **does not** create or consume an Allocation.

Perform these deterministic checks using the records from S12.08. **Do not write invalid rows just to prove they are invalid.**

| Test | Input or action | Expected learner evidence |
| --- | --- | --- |
| Baseline arithmetic | Hall 01 and 02 snapshots | 450 and 500 kW before new allocations |
| Rack 001 space | ALC-0001 and ALC-0002 | 14 reserved U total; 28 unreserved U; 7 of 20 kW reserved |
| Rack 002 space | ALC-0003 | 10 reserved U, 32 unreserved U, 5 of 20 kW reserved |
| Contiguous overlap | Rack 001, Start U 6, Units 4 | Overlaps existing 1–8, so validation rejects |
| Boundary conflict | Rack 001, Start U 40, Units 4 | End U 43 exceeds 42, so reject |
| Power budget | Rack 001, Start U 20, Units 4, Power 14 kW | Existing 7 + 14 = 21, above budget 20: reject |
| Rack availability | Rack 019, a new reservation | Status Hold due to source asset Under Maintenance; reject |
| Request separation | REQ-0001 remains Draft | Counts unchanged until a distinct Allocation exists |
| Hall planning totals | Reserved allocations by correct Hall | Hall 01 443 kW; Hall 02 495 kW (illustrative) |
| Choice consistency | Each reserved Allocation | Status Reserved AND Capacity Reserved Yes; matching Hall Lookup |
| Date and identity | Capacity Requests | No real Entra approval/sign-off inferred from fictional employee |
| Idempotency | Rerun demo after save | No duplicate Rack Plan/Allocation Codes; alternate keys Active |

**Publish sequence:** Use **App checker** to inspect **Formulas**, **Accessibility**, **Performance**, and **Data source** categories separately. Zero formula errors alone does not mean the app is free of accessibility, performance or data-source findings. Resolve or explicitly document each remaining category before claiming a production-quality implementation.  Reopen the saved tables and confirm Lookup targets, local Choices and Active alternate keys. In the Canvas editor select **Save**, wait for saved confirmation, then **Publish** the app, and **Play** the published version. Navigate through all six screens, inspect gallery selections, open real related records, save one valid controlled request, and review whether new allocations appear after Refresh. If the browser warns of unsaved changes despite publishing, inspect the app's saved version status, whether any pending edits remain, and the last app publish history; do not assume the warning alone proves a loss of Dataverse data.

**Safe ending:** Restore any temporary allocation or request changes to the initial sample if they were only for test; the three baseline allocations remain as originally entered. No real equipment action, procurement request, data center power measurement or automated reservation was produced. Preserve the output as a fictional portfolio learning exercise. If a code formula or permission fails, fix and re-test that operation before declaring Part 12 complete.

### Finish Part 12

After completing and verifying the exercises, you have a **DC Capacity Planner** grounded in the existing two data halls and 20 Server Rack assets. It separates facility *design rating*, manually declared *planning baseline*, rack *unit space*, rack *planning power budget*, committed *allocation* and uncommitted *request*. The four Dataverse planning tables and one Canvas App show how these concerns fit together without pretending they are live monitoring or transaction-safe DCIM reservations.

Before marking Part 12 complete, verify all four primary names are Business required, all four alternate keys are Active, and all nine Lookup targets are correct. Confirm 20 rack plans, two baselines, three starting allocations and two capacity requests after removing temporary test rows; then inspect all App checker categories, delegation warnings and the exact saved/published app version. If the authoring environment reports 0 formula errors but leaves accessibility, performance or data-source findings, record them as outstanding rather than silently calling the application fully validated. A blank visual label on an allocation form must be cross-checked against its saved Lookup fields. Client-side overlap checks cannot eliminate simultaneous conflicting writes. This learner chapter describes reproducible steps; it does not certify that a particular Power Platform environment has completed them.

**Microsoft Learn references:**

- [Dataverse relationships](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-1n-relationships-portal)
- [Alternate keys](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/define-alternate-keys-reference-records)
- [Canvas app forms](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/working-with-forms)
- [Power Fx Filter, Search and LookUp](https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-filter-lookup)
- [Delegation in Canvas Apps](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/delegation-overview)
- [Power Fx error handling](https://learn.microsoft.com/en-us/power-apps/guidance/coding-guidelines/error-handling)

*All facilities, personnel, system loads, power budgets and requests are fictional; no live operational action is authorized.*


## Part 13 — Build Monitoring and Operational Intelligence with Power BI

Part 12 delivered a fictional rack-capacity planning layer. We now add a separate **Power BI Desktop operational-intelligence report**, connecting measurements to known equipment without confusing planning assumptions with observed values. This is a reporting layer, not a new Power App, an automated facility monitoring system, or an approval workflow. You will combine **50,000 synthetic readings** with the existing **24 DC Sensor records**, 100 Assets, two Data Halls and the previously published Alarm, Incident and Work Order files.

The work uses **Power BI Desktop Import mode** and the published CSV files. You can complete it through the Folder/Text-CSV interface or by editing a transparent Power BI Project (PBIP) whose Power Query M steps and TMDL model you inspect before opening in Desktop. Power BI Desktop remains responsible for refresh, query execution, visual evaluation and save verification. This route does not require creating 50,000 Dataverse rows, configuring a premium SQL connection or obtaining an on-premises gateway. Optional publication to Power BI Service depends on the permissions and licenses in your own environment. No new Dataverse table, cloud flow, physical-device connection or automatic data refresh is required here.

| Dataset / source | Expected rows | What it represents |
| --- | ---: | --- |
| `data/monitoring/monitoring-readings-01.csv` through `-10.csv` | **50,000 total** | Fictional sampled measurement fact; ten nonoverlapping batches |
| `data/sensors.csv` | **24** | Existing sensor inventory with metric, unit, acceptable range and Asset primary name |
| `data/assets.csv` | **100** | Existing equipment identity, category, status and Data Hall primary name |
| `data/data-halls.csv` | **2** | Existing Hall names and design IT capacities |
| `data/alarms.csv` | **120** | Alarm events and their own original statuses |
| `data/incidents.csv` | **200** | Historical incidents, priorities and lifecycle states |
| `data/work-orders.csv` | **500** | Maintenance backlog and completion states |

**Important distinction:** Threshold flags are generated examples, not genuine equipment alarms. A Reading row is not automatically an Alarm, an Incident or a Work Order. Samples for different metric types and units must not be averaged or summed together as though they measure the same quantity. The Part 12 capacity baseline is a separate manual planning model; these readings do not update or validate it.

### S13.01 — Verify the existing operations data and Power BI Desktop

Open the existing **SunnyVerse Data Center Operations 360** solution in your authorized Power Apps environment and inspect, without changing, these parent records: the Pacific Resilience Campus; Data Hall 01 and 02; the 100 DC Assets; 24 DC Sensors; 120 DC Alarms; 200 DC Incidents; and 500 DC Work Orders. The reference data can already be studied through the published CSVs even if a learner's tenant does not contain every earlier record. Confirm the four Part 12 planning tables remain intact; **do not recreate them**.

On your own development computer, open **Power BI Desktop**. Create a blank report using **Home → New**, when offered, and save it as `DC360-Operations-Intelligence.pbix` in a local training folder. Desktop is sufficient for this lesson. If Power BI Desktop is not installed or your computer is managed, use the institution-approved install/access route; do not bypass device or tenant policy. Never place private account identifiers or institutional data in the public repository.

Before import, create a local folder such as `DC360-Learning/monitoring` and place **only the ten published `monitoring-readings-*.csv` files** there. If using the source-controlled PBIP files, update the example local `C:\DC360-Learning` Power Query paths to the folder on your computer **before refresh**; the path is an illustrative placeholder and is not a shared network location. Keep the other six dimension and operation CSVs in a separate `DC360-Learning/reference` folder. Do not put the entire GitHub repository into the monitoring folder, because the Folder connector would otherwise combine unrelated CSV schemas.

**Checkpoint 1 — Prepared:** One existing solution, a locally saved blank PBIX, and ten monitoring batches in a dedicated folder. Do not claim that Power BI Service sharing or refresh is available yet.

### S13.02 — Understand the 50,000-row synthetic measurement contract

Download the ten files from the [monitoring folder](./data/monitoring/) or regenerate the identical practice dataset using [the generator](./data/monitoring/generate_monitoring.py) and the existing `sensors.csv`. **Do one or the other**, not both in the same import directory. Each file has exactly 5,000 data rows plus one header and exactly the same five headers:

```csv
Reading ID,Recorded At UTC,Sensor Code,Reading Value,Threshold State
```

| Exact header | Power Query type | Meaning / validation |
| --- | --- | --- |
| Reading ID | Text | Unique `RDG-000001` through `RDG-050000`; no duplicates |
| Recorded At UTC | Date/Time | Explicit UTC-labelled fictional instant, `2026-10-01 00:00:00` through `2026-10-22 16:45:00` |
| Sensor Code | Text | References one of the **existing 24** `DC-SEN-001`–`DC-SEN-024` business sensor codes |
| Reading Value | Decimal number | Numeric synthetic reading, interpreted only with the related Sensor's Metric Type and Unit |
| Threshold State | Text | `Normal`, `High` or `Low`, derived from the Sensor's acceptable minimum/maximum |

The generator emits **15-minute educational snapshots**, even though the sensor inventory's `Sample Interval Seconds` column is 60. The monitoring files are a *downsampled illustration*, not proof that live 60-second sampling occurred. Each recorded instant contains at most 24 sensor values. Sensor 001–008 have 2,084 examples each and the remaining sensors have 2,083; there are **2,084 distinct timestamps**. The earliest reading, `RDG-000001`, is a deliberately high example for Sensor 001. No asset name, tenant GUID or user identity is embedded in a fact row.

The fixed complete dataset contains **49,517 Normal**, **290 High** and **193 Low** flags, a total of **483 out-of-range samples**. These are expected totals for the unfiltered example, not operational alarm counts. The generator uses the saved `Minimum Acceptable` and `Maximum Acceptable` thresholds from `sensors.csv`. Do not turn the 483 readings into 483 Dataverse Alarm rows.

**Checkpoint 2 — Dataset contract:** Ten identical headers, no blank Sensor Codes, and total row count 50,000 before any report filtering.

### S13.03 — Import and combine the ten readings files

In Power BI Desktop choose **Home → Get data → More → File → Folder → Connect** (or **Get data → Folder**). Choose the local `DC360-Learning/monitoring` folder containing only ten reading CSVs. Select **Combine & Transform Data**, inspect the sample file preview, and choose the CSV data table. The Folder connector builds sample-file helper queries and combines files with matching columns. Those helper queries do **not** count as extra loaded model tables. Alternatively, in an authorized PBIP project, define one M query using `Folder.Files`, filter to the ten reading CSVs, parse each CSV with `Csv.Document`, promote its headers and expand all rows. Power BI Desktop must still execute and refresh the resulting query. Open **Transform data** if the preview is already open.

In **Power Query Editor**, rename the final combined table/query **Fact Monitoring Readings**. Ensure that *Use First Row as Headers* is applied once, not once again after already promoted headers. Keep the `Source.Name` column in the final **Fact Monitoring Readings** query so you can audit which files contributed rows, detect a duplicated batch, and distinguish a data-source problem from a semantic-model problem. Remove unused technical columns such as `Extension` only when unnecessary. The ten source filenames must be present in `Source.Name` with 5,000 rows each. Do not accidentally remove Reading ID, Sensor Code or Threshold State.

Select each column and confirm its icon/type: `Reading ID` Text, `Recorded At UTC` Date/Time, `Sensor Code` Text, `Reading Value` Decimal Number, and `Threshold State` Text. Change **Using Locale** only if your computer interprets the unambiguous `yyyy-MM-dd HH:mm:ss` dates incorrectly. These values represent UTC as written; if you later combine them with local timestamps, perform an explicit, documented time-zone conversion rather than silently changing their meaning.

Select **Transform → Count Rows** on a *duplicated reference/query* or use the bottom row count preview carefully, then discard the temporary count query after recording the result. The final Fact query must remain a table of all readings. Select **Close & Apply** and wait for model load.

| Check | Correct result |
| --- | --- |
| Combined files / `Source.Name` | Ten `monitoring-readings-01.csv` through `-10.csv`, **5,000 rows from each** |
| Data rows | **50,000** |
| Unique Reading ID | **50,000** |
| Distinct Sensor Code | **24** |
| High / Low / Normal | **290 / 193 / 49,517** |
| First / last Reading ID | `RDG-000001` / `RDG-050000` |
| Date range | 2026-10-01 to 2026-10-22, UTC-labelled |

If you get **5,000 rows**, inspect the Combine Files step and its directory source instead of reimporting more copies. If a query reports a missing `Column1` field after promoting headers, inspect and remove/rebuild the stale automatically generated Changed Type step, then set the exact types again. If duplicates appear, check for duplicate downloaded batches or repeated import queries; do not quietly deduplicate and call the source correct.

**Checkpoint 3 — Readings fact:** The data model loads 50,000 unique readings. No Dataverse or SQL table was modified.

### S13.04 — Load the operational reference dimensions

Choose **Home → Get data → Text/CSV** three times to import the separately downloaded `sensors.csv`, `assets.csv` and `data-halls.csv`. The combined readings query already exists from S13.03; **do not reimport it**. Use **Transform Data** for each dimension and rename the first three queries exactly:

| Power BI query | Source | Primary business key | Type checks |
| --- | --- | --- | --- |
| **Dim Sensor** | `sensors.csv` | `Sensor Code` (24 distinct) | Sensor Code and Asset Text; `Minimum Acceptable` / `Maximum Acceptable` Decimal; `Sample Interval Seconds` Whole Number; `Enabled` explicit Boolean or consistent Text |
| **Dim Asset** | `assets.csv` | `Asset Name` (100 distinct) | Asset Name, Asset Code, Asset Category, Operational Status, Data Hall Text; `Rated Power kW` Decimal; `Install Date` Date |
| **Dim Data Hall** | `data-halls.csv` | `Hall Name` (2 distinct) | Hall Name, Hall Code, Campus, Criticality Text; `Design IT Capacity kW` Decimal; `Active` Boolean or consistent Text |

When setting the `Enabled` and `Active` Yes/No values, make sure every source value resolves correctly, or keep them as Text until an explicit Yes/No conversion is validated. For Choice columns imported as CSV labels, retain the readable labels; Power BI data models do not need Dataverse's generated Choice integer values.

**Use the exact fields from the already published files.** For example, `Dim Sensor[Asset]` contains an **Asset Name** such as `UPS 001`, not the `Asset Code`. Similarly, `Dim Asset[Data Hall]` contains `Data Hall 01`, not the Hall GUID or Hall Code. A relationship built on different naming conventions without mapping will create blank/unmatched records.

Inspect the three source-table keys for duplicates and missing values. Do not duplicate `DC Sensor` or `DC Asset` in Dataverse; these are analytical copies of published fictional data.

### S13.05 — Import Alarm, Incident and Work Order history separately

Choose **Get data → Text/CSV** for the existing `alarms.csv`, `incidents.csv` and `work-orders.csv`. Rename the queries exactly **Fact Alarm**, **Fact Incident**, and **Fact Work Order**. Keep the business primary names and codes, and convert status/priority/type fields to Text.

| Fact | Date columns (Date/Time) | Asset reference | Expected rows / original status labels |
| --- | --- | --- | --- |
| **Fact Alarm** | `Detected At` | `Source Asset` | 120; New, Acknowledged, Cleared, Suppressed |
| **Fact Incident** | `Reported At` | `Source Asset` | 200; New, Assigned, In Progress, Resolved, Closed |
| **Fact Work Order** | `Requested On`, `Due On`, optional `Completed On` | `Asset` | 500; Planned, Assigned, In Progress, On Hold, Completed, Cancelled |

Before date conversion, replace blank CSV strings `""` with **null**, for example with a Power Query `Table.ReplaceValue` step across the relevant columns. A conversion of an empty string to Date/Time can fail; null stays null. For timestamp text that ends with **`Z`**, parse it as `DateTimeZone`, explicitly change to **UTC** using `DateTimeZone.SwitchZone(..., 0)`, then remove the zone with `DateTimeZone.RemoveZone` only if the report needs a UTC-clock-time `datetime` column. Example: `DateTimeZone.RemoveZone(DateTimeZone.SwitchZone(DateTimeZone.FromText("2026-09-01T08:00:00Z"), 0))`. A naive local Date/Time conversion can silently shift a UTC clock. Inspect any optional `Related Alarm`, `Related Incident`, `Related Inspection` or engineer names but **do not** pretend they are authenticated user identities or a verified causal join. Relationship creation is a separate step; importing a Text column never creates a Dataverse Lookup.

Check representative records against the existing CSV file values: `ALM-0001`, `INC-0001` and `WO-0001`. The files are synthetic historical snapshots, not a continuous live stream and not automatically refreshed from the Power Apps tenant.

**Checkpoint 5 — All seven **loaded model tables** (Power Query may also contain un-loaded helper queries):** 50,000 readings + 24 sensors + 100 assets + 2 halls + 120 alarms + 200 incidents + 500 work orders, without duplicate load queries.

### S13.06 — Build an unambiguous star-like relationship model

Open **Model view**, confirm all seven imported tables are present, and use **Manage relationships → New** (or drag the business keys on the model canvas). Create these relationships with **One-to-many (1:*)** from the dimension side and **Single** cross-filter direction:

| One side (unique) | Many side (repeats) | Expected filter path |
| --- | --- | --- |
| `Dim Data Hall[Hall Name]` | `Dim Asset[Data Hall]` | Hall filters Assets |
| `Dim Asset[Asset Name]` | `Dim Sensor[Asset]` | Asset filters Sensors |
| `Dim Sensor[Sensor Code]` | `Fact Monitoring Readings[Sensor Code]` | Sensor filters Readings |
| `Dim Asset[Asset Name]` | `Fact Alarm[Source Asset]` | Asset filters Alarms |
| `Dim Asset[Asset Name]` | `Fact Incident[Source Asset]` | Asset filters Incidents |
| `Dim Asset[Asset Name]` | `Fact Work Order[Asset]` | Asset filters Work Orders |

Set the relationship to **Active** where it does not introduce an ambiguous path. Do **not** also create a direct Hall-to-Readings relationship, or a Sensor-to-Alarm relationship that creates a second active route through Asset. Do not relate two fact tables directly by their row numbers. A cross-filter that appears to connect tables is not evidence of a real event-causation relationship.

In **Data view** inspect Dim Sensor's 24 distinct Sensor Codes, Dim Asset's 100 Asset Names and Dim Data Hall's two Hall Names. In **Model view** confirm each is on the unique **1** side of its relationship. If Power BI offers a many-to-many relationship because a key is duplicated, investigate the duplicate in the source rather than accepting many-to-many to silence the warning. Do not enable Both-direction filters as a general workaround.

**Checkpoint 6 — Semantic model:** Six intended active, single-direction relationships and no ambiguous loops. Filtering one hall should restrict its Assets, Sensors and Reading rows. The fixed practice dataset yields **12 sensors, 25,000 readings, 60 alarms, 100 incidents and 250 work orders for Hall 01**; Hall 02 also contains 25,000 readings. These are fictional reporting checks, not live telemetry.

### S13.07 — Create explicit Power BI DAX measures and validate units

In **Report view**, select the **Fact Monitoring Readings** table, then choose **Modeling → New measure**. Create each measure individually. The formula editor may use commas or semicolons as argument separators depending on your locale; do not change the underlying measure semantics. Use these exact measure names and formulas in the report:

```dax
Monitoring Rows = COUNTROWS('Fact Monitoring Readings')

Monitored Sensors = DISTINCTCOUNT('Fact Monitoring Readings'[Sensor Code])

Normal Rows =
CALCULATE([Monitoring Rows], 'Fact Monitoring Readings'[Threshold State] = "Normal")

High Rows =
CALCULATE([Monitoring Rows], 'Fact Monitoring Readings'[Threshold State] = "High")

Low Rows =
CALCULATE([Monitoring Rows], 'Fact Monitoring Readings'[Threshold State] = "Low")

Out of Range Rows = [High Rows] + [Low Rows]

Out of Range Rate =
DIVIDE([Out of Range Rows], [Monitoring Rows], 0)

Sensor Key Mismatches =
COUNTROWS(
    EXCEPT(
        VALUES('Fact Monitoring Readings'[Sensor Code]),
        VALUES('Dim Sensor'[Sensor Code])
    )
) + 0

Average Reading (Selected Metric) =
IF(
    HASONEVALUE('Dim Sensor'[Metric Type]) &&
    HASONEVALUE('Dim Sensor'[Unit]),
    AVERAGE('Fact Monitoring Readings'[Reading Value]),
    BLANK()
)

Peak Reading (Selected Metric) =
IF(
    HASONEVALUE('Dim Sensor'[Metric Type]) &&
    HASONEVALUE('Dim Sensor'[Unit]),
    MAX('Fact Monitoring Readings'[Reading Value]),
    BLANK()
)
```

Set **Out of Range Rate** format to **Percentage**, two decimals. The `+ 0` in Sensor Key Mismatches ensures that `COUNTROWS` over an empty `EXCEPT` table shows numeric **0** rather than **BLANK**. Without it, a report can display blank even though there are no unmatched Sensor Codes. Put the Average and Peak measures on pages with **Metric Type and Unit filters**. A blended average across kW, degrees Celsius and volts is dimensionally meaningless, so these measures deliberately show Blank unless one metric type and unit are selected. Even among matching units, average only when metric meaning agrees—Output Power and Electrical Power are not automatically the same operational KPI.

Create one explicit source-to-flag quality measure. The related Sensor thresholds apply to each reading through the active Sensor relationship:

```dax
Threshold Flag Mismatches =
SUMX(
    'Fact Monitoring Readings',
    VAR v = 'Fact Monitoring Readings'[Reading Value]
    VAR lowLimit = RELATED('Dim Sensor'[Minimum Acceptable])
    VAR highLimit = RELATED('Dim Sensor'[Maximum Acceptable])
    VAR expectedState =
        SWITCH(
            TRUE(),
            v < lowLimit, "Low",
            v > highLimit, "High",
            "Normal"
        )
    RETURN IF(expectedState <> 'Fact Monitoring Readings'[Threshold State], 1, 0)
)
```

For the operational snapshots, create measures on their respective fact tables:

```dax
Alarm Rows = COUNTROWS('Fact Alarm')

Actionable Alarms =
CALCULATE(
    [Alarm Rows],
    'Fact Alarm'[Alarm Status] IN {"New", "Acknowledged"}
)

Critical Alarms =
CALCULATE(
    [Alarm Rows],
    'Fact Alarm'[Alarm Severity] = "Critical"
)

Incident Rows = COUNTROWS('Fact Incident')

Active Incidents =
CALCULATE(
    [Incident Rows],
    'Fact Incident'[Incident Status] IN {"New", "Assigned", "In Progress"}
)

P1 Incidents =
CALCULATE(
    [Incident Rows],
    'Fact Incident'[Priority] = "P1 Critical"
)

Work Order Rows = COUNTROWS('Fact Work Order')

Open Work Orders =
CALCULATE(
    [Work Order Rows],
    'Fact Work Order'[Work Order Status] IN
        {"Planned", "Assigned", "In Progress", "On Hold"}
)

Completed Work Orders =
CALCULATE(
    [Work Order Rows],
    'Fact Work Order'[Work Order Status] = "Completed"
)
```

Expected unfiltered checks: Monitoring Rows **50,000**, Monitored Sensors **24**, High **290**, Low **193**, Normal **49,517**, Out of Range **483**, Sensor Key Mismatches **0**, Threshold Flag Mismatches **0**, Alarm Rows **120**, Actionable Alarms **60**, Critical Alarms **30**, Incident Rows **200**, Active Incidents **120**, P1 Incidents **50**, Work Order Rows **500**, Open Work Orders **334**, Completed Work Orders **83**. Measures react to filter context, so verify these totals with **all slicers cleared**.

**Checkpoint 7 — DAX:** All 20 source measures save without syntax errors. If selecting Unit = `kW` alone still spans both **Output Power** and **Electrical Power**, the guarded Average and Peak measures should show BLANK rather than mixing distinct metrics. Out-of-range readings and formal alarm counts remain distinct.

### S13.08 — Create the Executive Operations Overview report page

In **Report view**, rename the first blank page **Executive Overview**. Use a restrained navy/teal theme with neutral backgrounds; use amber/red only for attention. Keep text labels readable without relying on color.

Create these visuals through **Visualizations**, add the exact fields/measures and format them:

| Visual type | Title / field mapping | Expected unfiltered interpretation |
| --- | --- | --- |
| Card | **Monitoring Samples** → `[Monitoring Rows]` | 50,000 fictional readings |
| Card | **Monitored Sensors** → `[Monitored Sensors]` | 24 sensor codes represented |
| Card | **Out-of-Range Samples** → `[Out of Range Rows]` | 483 flagged readings, not 483 alarms |
| Card | **Out-of-Range Rate** → `[Out of Range Rate]` | Approximately 0.97% of samples |
| Card | **Actionable Alarms** → `[Actionable Alarms]` | 60 historical alarms with New/Acknowledged status |
| Card | **Active Incidents** → `[Active Incidents]` | 120 historical incidents with New/Assigned/In Progress status |
| Card | **Open Work Orders** → `[Open Work Orders]` | 334 planned/assigned/in-progress/on-hold work orders |
| Clustered column chart | Axis `Dim Sensor[Metric Type]`, values `[Out of Range Rows]` | Compare *counts*, not average mixed-unit values |
| Slicer | `Dim Data Hall[Hall Name]` | Restrict all connected fact tables by Hall through the Asset dimension |
| Slicer | `Dim Sensor[Unit]` | Make the measurement domain visible |

Use an explanatory Text box such as: **“Synthetic historical snapshots; threshold exceptions do not create Dataverse alarms, and planned headroom is not measured usage.”** Do not imply the report tracks currently running equipment. Clear all slicers **and chart selections/cross-highlighting** for the initial evidence screenshot. Selecting a chart segment can silently filter other cards and change a peak even when a slicer appears unchanged. Click the same segment again or clear selections before comparing baseline numbers.

### S13.09 — Add the Monitoring and Environmental Trends page

Add a new page using the **+** control or **Insert → New page** and rename it **Monitoring & Trends**. Build the following:

| Visual | Field / configuration | Important validation |
| --- | --- | --- |
| Slicer | `Dim Sensor[Metric Type]` and `Dim Sensor[Unit]` | Select exactly one meaningful metric/unit context before reading averages |
| Slicer | `Dim Sensor[Sensor Name]` | One sensor makes trend interpretation straightforward |
| Line chart | X `Fact Monitoring Readings[Recorded At UTC]`, Y `[Average Reading (Selected Metric)]` | Use continuous timestamp or a suitable aggregation; remove unhelpful auto date hierarchy if needed |
| Card | `[Peak Reading (Selected Metric)]` | Must use a selected metric and unit |
| Stacked column chart | Axis `Dim Sensor[Sensor Code]`, Legend `Fact Monitoring Readings[Threshold State]`, Y `[Monitoring Rows]` | Shows high/normal/low counts, not severity of alarms |
| Table | Reading ID, timestamp, Sensor Code, Reading Value, Threshold State plus related Metric Type/Unit | Filter to High or Low for an inspectable anomaly list |

Add **`Dim Sensor[Minimum Acceptable]` and `Dim Sensor[Maximum Acceptable]` columns to the exceptions table**, where each reading is shown alongside its sensor's own limits. This works even when the line chart cannot bind an individual dynamic threshold to each sensor. Do not insert an arbitrary fixed constant line across multiple sensors. For a single selected sensor, add a dynamic reference line only when its current visual supports that data binding and you have tested the actual scalar. **Clear chart cross-highlighting** before validating the peak, average or exception example.

Drill into **DC-SEN-001** and confirm `RDG-000001` is a High example with value **560.00 kW** against a fictional maximum of 500.00 kW. A high sample is synthetic data, not a power-safety event. Verify that selecting Data Hall 01/02 changes the filtered sensor/readings population appropriately.

### S13.10 — Create the Alarm, Incident and Maintenance Operations pages

Add three report pages named **Alarm Operations**, **Incident Operations** and **Maintenance Operations**.

**Alarm Operations:** Add cards for `[Alarm Rows]`, `[Actionable Alarms]` and `[Critical Alarms]`. Add a stacked bar by `Fact Alarm[Alarm Severity]` and `Fact Alarm[Alarm Status]`. Include a table with Alarm Code, Detected At, Source Asset, Alarm Severity, Alarm Status, and Alarm Details. Filter by Hall using the Dim Data Hall hierarchy through Asset. The fixed dataset has 30 each of Critical/High/Medium/Low severities and 30 each of New/Acknowledged/Cleared/Suppressed statuses; these are illustrative distributions.

**Incident Operations:** Add cards for `[Incident Rows]`, `[Active Incidents]` and `[P1 Incidents]`. Add a clustered bar for Incident Status and a table of Incident Code, Priority, Incident Category, Source Asset, Reported At and Assigned Engineer. Do not claim the fictional Assigned Engineer label is a genuine Entra identity. `Related Alarm` is a source text reference, not an automatically verified process transition.

**Maintenance Operations:** Add cards for `[Work Order Rows]`, `[Open Work Orders]` and `[Completed Work Orders]`. Add a bar by Work Order Status and a table with Work Order Code, Work Order Type, Asset, Due On, Work Order Status and Assigned Engineer. Use the `Due On` source date field only after verifying its converted type. A work order marked Completed in a teaching file is not a physical equipment maintenance certificate.

For every page, select an Asset or Hall filter and compare counts with the actual matching source rows. Use only source-supported categories and definitions. If a visual displays a blank category, check its relationship and key values rather than discarding records.

### S13.11 — Perform data-quality, reconciliation and negative tests

Perform the following checks in the final loaded model before publishing or capturing portfolio screenshots:

| Test | Procedure | Expected |
| --- | --- | --- |
| Complete ingestion | Reset all slicers; use Monitoring Rows card | **50,000** |
| Unique readings | Group by Reading ID or use Power Query Remove Duplicates on a temporary reference | **50,000 distinct IDs** |
| Sensor matches | Sensor Key Mismatches measure | **0** |
| Value-to-threshold flags | Threshold Flag Mismatches measure | **0** |
| Outcome categories | High, Low, Normal card values | 290, 193, 49,517 |
| Reading dates | Earliest and latest Recorded At UTC | 2026-10-01 00:00:00 and 2026-10-22 16:45:00 |
| Hall hierarchy | Filter Hall 01, then Hall 02 | Sensor and fact rows change through the valid Asset links |
| Mixed units | Clear Metric Type and Unit slicers | Average Reading measure shows **Blank**, not a meaningless cross-unit value |
| Source counts | Clear slicers; inspect Alarm, Incident, Work Order cards | 120, 200, 500 |
| Operational subsets | Clear slicers; inspect Active Incidents / Open Work Orders | 120 / 334 |
| Duplicate batch | Temporarily add a second copy of batch 01 in a **test folder** | Detect 55,000 rows; restore original folder; never publish test result |
| Missing sensor | In a **temporary copied** file, replace one Sensor Code with `BAD-SENSOR` | Sensor Key Mismatches > 0; restore original source |
| Threshold inconsistency | In a **temporary copied** row, change Normal to High without changing the value | Threshold Flag Mismatches > 0; restore original source |

**Do not modify the checked-in source CSVs** for negative tests. Use separate local test copies. One safe method is to add a **temporary test table/query to an unsaved Power BI Desktop session**, run the duplicate/missing-sensor/flag checks, and **close without saving**. Alternatively use a copy of the PBIX/PBIP and restore the original files afterward. Reopen the baseline PBIX and verify exactly 50,000 rows after each test. Never carry a temporary test folder or test query into the published learning model. Do not delete or recreate existing Dataverse rows to simulate telemetry failures. If a model visual contradicts a known row count, inspect file folder scope, Power Query Applied Steps, type conversions, relationship direction and filter context before saying the report is complete.

### S13.12 — Save, verify, and optionally publish the Power BI report

Save the completed report as **`DC360-Operations-Intelligence.pbix`** in the authorized local working folder. Reopen it to verify that the seven queries, six relationships, DAX measures and five report pages survived. Select **Refresh** in Desktop and confirm row counts and measures match the unfiltered baseline. Document any performance warnings, invalid transforms, disabled relationships or source-path dependencies as actual findings. If using a PBIP project, check the `.pbip`, report definitions, semantic-model `.tmdl` files and saved `.pbix` separately. A saved script alone does not prove that Desktop visuals rendered and refreshed.

Power BI Desktop can build and save this report **without publishing**. For source control, publish only a **reviewed, path-sanitized PBIP source project**: exclude `.pbi/localSettings.json`, `.pbi/cache.abf`, temporary negative-test CSVs, private user paths and credential-bearing files. A sanitized project uses illustrative paths such as `C:\DC360-Learning` which the learner must replace before refresh. Do not upload an unreviewed PBIX or raw machine snapshot to a public repository. If your institution permits publication, check the signed-in Power BI account, workspace and actual sharing license first. Publishing to a personal workspace does **not** automatically authorize organization-wide distribution, embedding, anonymous public sharing or scheduled refresh. If publishing is blocked, keep the validated local PBIX and explain the limitation rather than fabricating an online report. Do not publish reports containing tenant-specific secrets, real facility telemetry, private university data or credentials.

| Final verification | Expected |
| --- | --- |
| Data model | Seven **loaded model tables** (plus optional helper queries), six active single-direction relationships |
| Measurements | 50,000 unique readings from 24 existing sensors |
| Additional facts | 120 alarms, 200 incidents, 500 work orders |
| DAX | All 20 measures evaluate; Sensor Key Mismatches explicitly returns 0 rather than BLANK |
| Report pages | Executive Overview; Monitoring & Trends; Alarm Operations; Incident Operations; Maintenance Operations |
| Source provenance | CSV Import mode; no live device connection or unsupported premium Dataverse/SQL dependency |
| Security | No real identities, tenant URLs, credentials or physical operations data in the public report |
| Persistence | Saved PBIX reopens, refreshes and retains visual interactions |
| Publication | Optional and separately verified; Service sign-in/workspace selection is separate from local PBIX save or GitHub source publication |

### Finish Part 13

You now have a reproducible **Monitoring & Operational Intelligence** Power BI Desktop model with an auditable 50,000-row synthetic measurement source, meaningful Sensor-to-Asset-to-Hall relationships, and separate operational views for alarms, incidents and work orders. The report does not claim real-time observability, automated alarm generation, or live capacity measurement. If your Power BI Service access is restricted, the local PBIX remains a complete learning deliverable once its queries and visuals pass validation.

**Microsoft Learn references:**

- [Combine files (binaries) in Power BI Desktop](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-combine-binaries)
- [Combine CSV files in Power Query](https://learn.microsoft.com/en-us/power-query/combine-files-csv)
- [Model relationships in Power BI Desktop](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-relationships-understand)
- [Use Report view in Power BI Desktop](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-report-view)
- [Power BI licensing and sharing](https://learn.microsoft.com/en-us/power-bi/fundamentals/end-user-license)

*This chapter contains fictional data only. Nothing in it authorizes real facility operation, monitoring, dispatch or electrical work.*



## Part 14 — Build Rules-Based Intelligent Operations and Reviewed Knowledge

Part 13 supplied fictional monitoring and operations reporting. Reporting does not itself document why an individual record needs attention or who reviewed an explanation. Continue in **the same SunnyVerse Data Center Operations 360 solution** with three rules-first registers, real source Lookups, six published views, the existing Supporting Operations Hub and one guarded manual insight flow. The existing Incidents, Work Orders and Inventory records remain the evidence; do not duplicate or overwrite their source data.

The core exercise does **not** need AI Builder, Copilot Studio, a new Power App, a Power BI Service workspace, SQL, real telemetry or a new license beyond what is already required for your authorized Dataverse/Power Automate learning environment. An optional, permission-gated AI-summary test comes last. Rule outcomes, fictional knowledge, and human review remain explicit even if AI features are unavailable.

| New component | Use in this chapter | Boundary |
| --- | --- | --- |
| **DC Intelligence Rule** (Dataverse) | Document three visible business-condition rules | A rule row documents criteria; it is not automatically executed as arbitrary code |
| **DC Operational Insight** (Dataverse) | Record flagged fictional work, source record and review outcome | A generated insight is not an actual alarm or authenticated approval |
| **DC Operations Knowledge Article** (Dataverse) | Store short fictional reviewed guidance with lifecycle state | A knowledge note is not a safe work procedure or executable MOP |
| Existing **DC Supporting Operations Hub** | Add three pages, three forms and six operational views | Reuse the existing model-driven app; do not create a duplicate app |
| **DC14_Incident_Insight_Demo** (instant cloud flow) | Demonstrate one guarded, idempotent incident rule | No sending messages, no automatic physical action, no edits to earlier flows |

Your source records are already in the solution. We will use **INC-0001** (the source CSV marks it P1 Critical and New), **WO-0004** (On Hold in the sample sequence) and **BAL-0002** (manual Reorder Required = Yes from Supporting Operations). If your tenant data was deliberately modified after earlier exercises, inspect the saved rows and correct the exercise prerequisites **only with appropriate authorization**; do not silently change live-looking records just to make a demonstration pass.

### S14.01 — Verify prerequisites and establish safe rule boundaries

Open [Power Apps](https://make.powerapps.com), select the authorized environment, then navigate to **Solutions → SunnyVerse Data Center Operations 360**. Confirm these existing table records using their saved main forms or editable data views:

| Existing source | Record to read, not recreate | Fields to verify |
| --- | --- | --- |
| DC Incident | `INC-0001` | Incident Name, Incident Code, Priority **P1 Critical**, Incident Status **New**, Source Asset, and primary-key GUID |
| DC Incident | `INC-0002` | A different incident available for the negative/nonmatching exercise |
| DC Work Order | `WO-0004` | Work Order Code, Work Order Status **On Hold**, related Asset |
| DC Inventory Balance | `BAL-0002` | Balance Code, Reorder Required **Yes**, Spare Part and Data Hall Lookups |
| DC Department | `DC-OPS` | Existing Department Name and Department Code |
| Existing app | **DC Supporting Operations Hub** | It opens and displays the previous shift/vendor/spare pages |

The monitoring data in Part 13 is a **CSV-based Power BI model**. Do not assume 50,000 reading records exist in Dataverse. This chapter uses the existing *operational* Dataverse records only. Never create a new incident or spare part solely to hide a broken Lookup.

**Rules-first operating model:** The training flow will check a fixed, documented condition against one incident. It will create a reviewable Insight **only if that rule matches** and if an Insight with the same business code does not already exist. The human reviewer can later mark the Insight Reviewed or Dismissed. Neither status automatically closes an incident, reserves stock, notifies a technician or executes maintenance.

**Checkpoint 1 — References:** Existing Incident, Work Order, Inventory Balance, Department and Supporting Operations Hub objects open. Nothing from Parts 00–13 has been deleted or renamed.

### S14.02 — Create DC Intelligence Rule with exact properties

From the existing solution choose **New → Table**, open advanced properties if needed, and enter:

| Table property | Value |
| --- | --- |
| Display name / plural | **DC Intelligence Rule** / **DC Intelligence Rules** |
| Description | `Fictional, human-readable detection rules for safe operational insight demonstrations.` |
| Table type | **Standard** |
| Record ownership | **Organization** |
| Primary name / target schema | **Rule Name** / `svrg_RuleName` |
| Table schema target | `svrg_DCIntelligenceRule` |
| Primary name required level | **Business required** (verify again after creation) |

Create the table, then reopen **Rule Name** under **Schema → Columns** and confirm **Required = Business required**. Some table-creation paths, including API-based creation, save a primary name as **Optional** despite the requested setting. Correct and verify it *after creation*; repeat for **Article Title** and **Insight Name** in S14.03–S14.04. Only then add the remaining columns, saving each and checking whether it exists before retrying a slow insert.

| Exact display name / target schema | Description | Type / required | Format, options and other properties |
| --- | --- | --- | --- |
| Rule Name / `svrg_RuleName` | Readable identifier of the documented rule | Primary Text / Business required | Created with table; no duplicate primary column |
| Rule Code / `svrg_RuleCode` | Stable unique fictional rule identifier | Text / Business required | Text format; max 24; Searchable Yes; no default |
| Source Area / `svrg_SourceArea` | Operating record family evaluated | **Local single Choice** / Business required | **Incident**, **Work Order**, **Inventory**; retain generated option integers; no default |
| Rule Type / `svrg_RuleType` | Kind of comparison the scenario illustrates | **Local single Choice** / Business required | **Priority Check**, **Status Check**, **Boolean Flag**; no default |
| Match Value / `svrg_MatchValue` | Documented expected visible source value | Text / Business required | Max 100; Searchable Yes; Simple; no default |
| Default Severity / `svrg_DefaultSeverity` | Illustrative priority of rule outcome | **Local single Choice** / Business required | **Critical**, **Warning**, **Information**; no default |
| Rule Explanation / `svrg_RuleExplanation` | Plain-English rationale and safe response boundary | Multiline Text / Optional | Max 2,000; no default |
| Enabled / `svrg_Enabled` | Whether rule may be chosen for a future exercise | Yes/No / Optional | Labels Yes/No; default **Yes** |
| Active / `svrg_Active` | Whether the catalog record is current | Yes/No / Optional | Labels Yes/No; default **Yes** |

Use **Local Choice**, not multi-select, for all three Choices; switch off synchronization with an existing Global Choice where offered. The option labels, not manually invented numeric IDs, are the learner's mapping source.

Under **Schema → Keys → New key**, name the key **DC Rule Code Key**, select only **Rule Code**, save and inspect its status until **Active**. If **HTTP 400 / database error** appears immediately after creating Rule Code, refresh **Schema → Columns** and **Keys**. Confirm the column is saved and no matching key already exists before retrying; do not create a duplicate. A successful key can remain **Pending** for several minutes while indexing completes—inspect until **Active**. Repeat this Active-state verification on the Article Code and Insight Code keys before importing potentially duplicate codes.

**Checkpoint 2 — Rule catalog:** One Organization-owned table, one primary name, eight additional business columns, three local Choices, and an Active alternate key.

### S14.03 — Create DC Operations Knowledge Article

Create another Standard, Organization-owned table:

| Table property | Value |
| --- | --- |
| Display name / plural | **DC Operations Knowledge Article** / **DC Operations Knowledge Articles** |
| Description | `Reviewed fictional guidance entries for safe operational learning and knowledge provenance.` |
| Primary name | **Article Title**; Business required after save |
| Table schema target | `svrg_DCOperationsKnowledgeArticle` |
| Primary schema target | `svrg_ArticleTitle` |

Configure all of its business columns:

| Exact display name / target schema | Description | Type / required | Other properties |
| --- | --- | --- | --- |
| Article Title / `svrg_ArticleTitle` | Human-readable knowledge entry title | Primary Text / Business required | Created once with table |
| Article Code / `svrg_ArticleCode` | Unique fictional knowledge reference | Text / Business required | Max 24; Searchable Yes |
| Topic / `svrg_Topic` | Primary operational use of the entry | **Local single Choice** / Business required | **Incident Triage**, **Work Order Review**, **Inventory Review**, **General**; no default |
| Audience / `svrg_Audience` | Team intended to review the entry | **Local single Choice** / Business required | **Operations**, **Engineering**, **Governance**; no default |
| Review Status / `svrg_ReviewStatus` | Editorial state of the knowledge entry | **Local single Choice** / Business required | **Draft**, **Reviewed**, **Approved**, **Retired**; no default |
| Guidance Summary / `svrg_GuidanceSummary` | Fictional review steps and decision context | Multiline Text / Business required | Max 2,000; not physical work instructions |
| Safety Boundary / `svrg_SafetyBoundary` | Non-operational-use disclaimer | Multiline Text / Business required | Max 1,000 |
| Last Reviewed On / `svrg_LastReviewedOn` | Editorial review date for the exercise | Date Only / Optional | No default |
| Active / `svrg_Active` | Whether article is current | Yes/No / Optional | Default Yes |
| Owner Department / `svrg_OwnerDepartment` | Optional responsibility grouping | Lookup / Optional | **Existing DC Department**; create once in S14.05 |

Reopen **Article Title** and confirm **Business required** after the table exists; correct Optional if necessary. Create **DC Knowledge Article Code Key** on Article Code and inspect until **Active** without creating another key while it is Pending. The optional Owner Department column must be a real Dataverse Lookup from S14.05, not a department-name Text duplicate. **Approved** is a fictional editorial Choice, not an Entra-authenticated electronic signature.

**Checkpoint 3 — Knowledge table:** One primary name, eight other regular business columns, a future Department Lookup and an Active code key. Guidance contains no real operational instructions.

### S14.04 — Create DC Operational Insight for traceable outcomes

Create **DC Operational Insight** / **DC Operational Insights**, Standard / **Organization** ownership, description `Fictional, evidence-linked operational findings that require explicit review.`, primary name **Insight Name** (verify Business required after saving), table schema target `svrg_DCOperationalInsight` and primary schema target `svrg_InsightName`.

| Exact display name / target schema | Description | Type / required | Other properties |
| --- | --- | --- | --- |
| Insight Name / `svrg_InsightName` | Readable finding title | Primary Text / Business required | Created with table |
| Insight Code / `svrg_InsightCode` | Unique deterministic finding identifier | Text / Business required | Max 30; Searchable Yes |
| Source Area / `svrg_SourceArea` | Which operational register supplied evidence | **Local single Choice** / Business required | **Incident**, **Work Order**, **Inventory** |
| Source Record Code / `svrg_SourceRecordCode` | Source business-code audit label | Text / Business required | Max 30; Searchable Yes; does **not** replace required actual Lookup |
| Insight Severity / `svrg_InsightSeverity` | Fictional attention level | **Local single Choice** / Business required | **Critical**, **Warning**, **Information** |
| Review Status / `svrg_ReviewStatus` | Human review workflow state | **Local single Choice** / Business required | **New**, **Under Review**, **Reviewed**, **Dismissed** |
| Evidence Summary / `svrg_EvidenceSummary` | Verifiable source fields justifying the finding | Multiline Text / Business required | Max 2,000; fictional facts only |
| Suggested Review / `svrg_SuggestedReview` | Non-executable next-review suggestion | Multiline Text / Optional | Max 2,000; human review only |
| Review Notes / `svrg_ReviewNotes` | Fictional reviewer explanation | Multiline Text / Optional | Max 2,000 |
| Flagged At / `svrg_FlaggedAt` | When the finding was generated in training | Date and Time / Business required | User local behavior; enter a value explicitly or set in the flow |
| Reviewed At / `svrg_ReviewedAt` | When a reviewer recorded a decision | Date and Time / Optional | Blank until actually reviewed in the exercise |
| Active / `svrg_Active` | Whether finding remains in the exercise | Yes/No / Optional | Default Yes |
| Rule / `svrg_Rule` | Catalog rule that justified the insight | Lookup / Business required | Existing **DC Intelligence Rule**; create in S14.05 |
| Related Incident / `svrg_RelatedIncident` | Parent evidence link | Lookup / Optional | Existing **DC Incident**; create in S14.05 |
| Related Work Order / `svrg_RelatedWorkOrder` | Parent evidence link | Lookup / Optional | Existing **DC Work Order**; create in S14.05 |
| Related Inventory Balance / `svrg_RelatedInventoryBalance` | Parent evidence link | Lookup / Optional | Existing **DC Inventory Balance**; create in S14.05 |
| Related Article / `svrg_RelatedArticle` | Optional reviewed knowledge reference | Lookup / Optional | Existing **DC Operations Knowledge Article**; create in S14.05 |

Reopen **Insight Name** and verify **Business required**. Add **DC Insight Code Key** using only **Insight Code** and wait until **Active**, inspecting the saved key and its actual metadata rather than assuming a submitted request finished. A rule may flag multiple records, but each Insight Code is unique to an intended source + rule combination. The app alone does not enforce cross-field consistency between Source Area, Source Record Code and optional source Lookups; validate them before saving.

**Checkpoint 4 — Insight table:** One primary name, 11 regular business fields, five planned Lookups, three local Choices, one Active code key.

### S14.05 — Add the six real Dataverse Lookup relationships

Create the three new tables first. Then go to **current table → Schema → Relationships → New relationship → Many-to-one**. Each relationship generates its Lookup column; never separately add that name as Text.

| Current table | Lookup display name / target schema | Related table | Required |
| --- | --- | --- | --- |
| DC Operations Knowledge Article | **Owner Department** / `svrg_OwnerDepartment` | DC Department | Optional |
| DC Operational Insight | **Rule** / `svrg_Rule` | DC Intelligence Rule | **Business required** |
| DC Operational Insight | **Related Incident** / `svrg_RelatedIncident` | DC Incident | Optional |
| DC Operational Insight | **Related Work Order** / `svrg_RelatedWorkOrder` | DC Work Order | Optional |
| DC Operational Insight | **Related Inventory Balance** / `svrg_RelatedInventoryBalance` | DC Inventory Balance | Optional |
| DC Operational Insight | **Related Article** / `svrg_RelatedArticle` | DC Operations Knowledge Article | Optional |

Use **Delete = Restrict** for all six new relationships, and **No cascade** for other available relationship behaviors. Reopen each saved relationship to inspect the real target table and cascade settings; inapplicable controls may be hidden by organization ownership. Organization-owned parent tables may hide certain cascade settings; inspect the actual saved relationship metadata instead of guessing. Verify the Lookup appears once under **Columns**, has the correct related table and required level, and opens an existing parent record from the picker.

**Checkpoint 5 — Six real Lookups:** One Knowledge Article→Department relationship and five Insight relationships. Nothing from earlier lessons is duplicated.

### S14.06 — Create three complete Main forms and six filtered system views

For each new table open **Forms → New form → Main form**. Add one two-column section for short identifiers, one single-column section for long summaries, and a final review section where needed. Save and publish each form.

| Table / named Main form | Sections and exact fields |
| --- | --- |
| **DC Intelligence Rule — Rule Main** | **Identity (2):** Rule Name, Rule Code, Source Area, Rule Type, Match Value, Default Severity, Enabled, Active. **Explanation (1):** Rule Explanation |
| **DC Operations Knowledge Article — Knowledge Main** | **Identity (2):** Article Title, Article Code, Topic, Audience, Review Status, Owner Department, Active, Last Reviewed On. **Content (1):** Guidance Summary, Safety Boundary |
| **DC Operational Insight — Insight Main** | **Finding (2):** Insight Name, Insight Code, Source Area, Source Record Code, Insight Severity, Review Status, Flagged At, Active, Rule. **Evidence Links (2):** Related Incident, Related Work Order, Related Inventory Balance, Related Article. **Narrative (1):** Evidence Summary, Suggested Review, Review Notes. **Review (2):** Reviewed At |

Check that every Business required field appears. Required Lookups cannot be hidden from the only form needed for creating records. Save and **Publish** all three.

Create these six public/system views using **Views → New view → Save → Publish**. Adding a table to a model-driven app may also bring in generated **default views**. This is not missing data or an error: keep them when useful, but deliberately choose the named views to show learners the appropriate filters. Confirm the exact six business views below are saved and published:

| Table | View name | Columns | Filter / sort |
| --- | --- | --- | --- |
| DC Intelligence Rule | **DC Enabled Intelligence Rules** | Rule Code, Rule Name, Source Area, Rule Type, Default Severity, Enabled, Active | Enabled = Yes AND Active = Yes |
| DC Intelligence Rule | **DC All Intelligence Rules** | Rule Code, Rule Name, Source Area, Match Value, Enabled | None |
| DC Operations Knowledge Article | **DC Approved Knowledge** | Article Code, Article Title, Topic, Owner Department, Review Status, Last Reviewed On | Review Status = Approved AND Active = Yes |
| DC Operations Knowledge Article | **DC Knowledge Review Queue** | Article Code, Article Title, Topic, Review Status, Owner Department | Review Status = Draft OR Reviewed, grouped with **OR** |
| DC Operational Insight | **DC Open Operational Insights** | Insight Code, Insight Name, Insight Severity, Review Status, Source Record Code, Flagged At, Rule | Review Status = New OR Under Review |
| DC Operational Insight | **DC All Operational Insights** | Insight Code, Insight Name, Source Area, Review Status, Related Incident, Related Work Order, Related Inventory Balance | None; Flagged At descending when available |

An Approved knowledge label does not confer access rights or automatically authorize an AI agent to act. Use proper OR filter grouping; do not combine mutually exclusive statuses with AND.

**Checkpoint 6 — Forms/views:** Three published complete Main forms, six views, all required fields visible and filters behaving as intended.

### S14.07 — Add intelligence review pages to the existing Supporting Operations Hub

Open **Solutions → SunnyVerse Data Center Operations 360 → DC Supporting Operations Hub → Edit**. Inspect the existing Shift Operations and Inventory & Partners navigation sections; keep their pages and their configured forms/views.

Use **Add page → Dataverse table** to add the three existing new tables. Group them under a new navigation group named **Intelligence & Knowledge**, or the equivalent site-map grouping interface:

| Navigation group | Existing/new table page | Forms and views included |
| --- | --- | --- |
| **Intelligence & Knowledge** | DC Operational Insights | DC Operational Insight — Insight Main; Open/All Insights views |
| **Intelligence & Knowledge** | DC Intelligence Rules | DC Intelligence Rule — Rule Main; Enabled/All Rules views |
| **Intelligence & Knowledge** | DC Operations Knowledge Articles | DC Operations Knowledge Article — Knowledge Main; Approved/Review views |

Under **In this app**, select the intended forms and six named views; inspect additional defaults and leave them only if useful. Confirm the original **Shift Operations** and **Inventory & Partners** groups still work, then **Save**. Obtain authorization before **Publish**. After publishing, inspect the *published version* and open it through **Play**, not just the designer preview. If a published timestamp advanced but the live version is uncertain, inspect version history rather than declaring success prematurely. **DC Approved Knowledge** legitimately shows only KNO-0001; KNO-0002 has status **Reviewed** and appears in its applicable review view. Open both **DC All Operational Insights** (three New rows after S14.11) and **DC All Intelligence Rules** (three enabled rules). Do not create another standalone Power App.

**Checkpoint 7 — Reused app:** One existing Supporting Operations Hub now exposes the new intelligence and knowledge pages; no earlier form, Canvas app or flow was replaced.

### S14.08 — Enter three fictional rules and two reviewed-source knowledge records

Create the three Rules before Insights so the source Rule Lookups are valid. The normal learner route is the published **Main forms**. In an authorized development environment, you may alternatively use a supported **Dataverse Web API** client, resolving real saved Choice values and binding existing Lookup GUIDs; then **reopen and inspect every saved row in the app**. Do not confuse a successful API response with verified application forms or duplicate the sample records. All values are fictional.

| Rule Code | Rule Name | Source Area | Rule Type | Match Value | Default Severity | Enabled |
| --- | --- | --- | --- | --- | --- | --- |
| `RUL-0001` | Critical New Incident | Incident | Priority Check | `P1 Critical + New` | Critical | Yes |
| `RUL-0002` | Work Order On Hold | Work Order | Status Check | `On Hold` | Warning | Yes |
| `RUL-0003` | Low Stock Review Flag | Inventory | Boolean Flag | `Reorder Required = Yes` | Warning | Yes |

In the **Rule Explanation** field, enter human-readable criteria: RUL-0001 requires both Priority = P1 Critical and Incident Status = New; RUL-0002 checks only the Work Order Status = On Hold; RUL-0003 checks the saved **manual** Inventory Balance Reorder Required flag. Leave all rules Active = Yes. **The Match Value field is documentation**; it is not a string expression that Power Automate automatically interprets. The initial flow demonstrates only RUL-0001.

Create the two knowledge articles:

| Article Code | Title | Topic | Audience | Review Status | Owner Department |
| --- | --- | --- | --- | --- | --- |
| `KNO-0001` | Incident Record Review Basics | Incident Triage | Operations | Approved | Data Center Operations |
| `KNO-0002` | Spare Balance Verification | Inventory Review | Engineering | Reviewed | Facilities Maintenance |

For KNO-0001, set Guidance Summary to `Verify the fictional incident code, saved priority, status and related asset. Escalate questions to an authorized reviewer; this note performs no dispatch or device action.` For KNO-0002, use `Compare Quantity On Hand, Quantity Reserved and the related part's Reorder Point. Correct only the training record after human review.` For both, set Safety Boundary = `Training-only knowledge; never follow as a live facility procedure or safety authorization.` Enter a fictional Last Reviewed On exercise date only if a review was actually simulated; it may remain blank otherwise. Save and reopen both.

**Checkpoint 8 — Source rules and knowledge:** Three rules, two knowledge articles, correct Choices, active code keys and valid Department Lookups.

### S14.09 — Create two manual Insights and verify their source links

Before building automation, enter two insights using **DC Operational Insight — Insight Main**, selecting actual Lookups from pickers. These belong to the Work Order and Inventory sources, not the Incident flow.

| Insight Code / Name | Source Area / Source Record Code | Rule | Related Lookup | Severity / Review Status |
| --- | --- | --- | --- | --- |
| `INS-WO-0004-HOLD` / Work Order Hold Review | Work Order / `WO-0004` | RUL-0002 | **Related Work Order** = existing WO-0004 | Warning / New |
| `INS-BAL-0002-REORDER` / Spare Reorder Review | Inventory / `BAL-0002` | RUL-0003 | **Related Inventory Balance** = existing BAL-0002 | Warning / New |

For each record, set Evidence Summary from saved source fields, such as `WO-0004 has Work Order Status = On Hold` or `BAL-0002 has Reorder Required = Yes in the manually maintained inventory register`. Set Suggested Review to `Review the linked fictional record and document the decision; no automated action is authorized.` Set Flagged At to the exercise's current time in the form and Active to Yes. You may connect KNO-0002 to the Inventory insight using the optional **Related Article** Lookup. Do not enter or copy Dataverse GUIDs as visible narrative text.

Open both Insights after saving and select the related Work Order/Balance to prove the relationships are real. Check that Source Area and Source Record Code are consistent with the selected parent. No email, Teams notification, stock transaction or work-order status change should occur.

**Checkpoint 9 — Manual Insights:** Exactly two source-linked Insight rows exist before the incident demonstration. No incident Insight exists yet for the deterministic code `INS-INC-0001-P1`.

### S14.10 — Build the guarded DC14 incident Insight demonstration flow

In [Power Automate](https://make.powerautomate.com), choose the **same authorized environment and existing solution**. Before creating anything, search solution cloud flows for `DC14_Incident_Insight_Demo`; open and reuse it if it already exists. Otherwise choose **New → Automation → Cloud flow** (or **New → Cloud flow → Instant**) and name it **DC14_Incident_Insight_Demo**. Select **Manually trigger a flow**. Do not add Outlook, Teams or Approvals actions.

Create the following Dataverse actions, naming each action distinctly in the designer. Use the generated **logical** field names actually saved in the tenant (lowercase may differ from the target schemas in the guide). Configure the OData filter text based on those inspected names, not a guessed schema:

| Order | Action | Table and inputs | Required behavior |
| --- | --- | --- | --- |
| 1 | **List rows — Incident** | DC Incidents, Filter rows = `svrg_incidentcode eq 'INC-0001'` **only after confirming the actual Incident Code logical name**; Top Count = 1 | Read one saved incident, no change |
| 2 | **Condition — Found** | Test `length(body('List_rows_Incident')?['value']) > 0` (adapt the expression to the action's actual internal name) | If missing, terminate **without** writing |
| 3 | **Condition — Critical & New** | Compare saved **Priority = P1 Critical** AND **Incident Status = New** using actual Choice values or their formatted labels | If not matched, terminate without an Insight |
| 4 | **List rows — Rule** | DC Intelligence Rules, filter Rule Code `RUL-0001`; Top Count 1 | Verify saved rule exists, Enabled = Yes, Active = Yes |
| 5 | **List rows — Existing Insight** | DC Operational Insights, filter Insight Code `INS-INC-0001-P1`; Top Count 1 | If a matching record exists, no-op instead of creating a duplicate |
| 6 | **Add a new row — Operational Insight** | Set name `Critical New Incident INC-0001`, Insight Code `INS-INC-0001-P1`, Source Area Incident, Source Record Code `INC-0001`, Severity Critical, Review Status New, safe Evidence Summary, Flagged At `utcNow()`, Active Yes | **Bind Rule and Related Incident to their real Dataverse row IDs**; no text substitutes |
| 7 | **Result / Run history** | Inspect action status and result row | Do not send outward notifications |

**Designer guidance:** A Dataverse Choice field may expose a numeric option value or a formatted-value label. Inspect the actual metadata/Run history before comparing. Do not insert a guessed option integer. For a Dataverse Lookup action input, use the supported related-row reference or the proper **OData bind** syntax selected by the maker UI; the value must reference a real Rule or Incident row GUID. The flow's actions should remain in **the existing solution**, with its existing Dataverse connection.

The **Rule** row documents the criteria, but the flow's Condition explicitly evaluates the two source fields. Do not use `Match Value` as a run-time interpreter or assume the text automatically drives arbitrary decisions. The alternate key on Insight Code is a second uniqueness control, while the List rows check makes repeated runs idempotent in this **single-user demonstration**. Parallel writers can still race unless a server-side uniqueness/upsert design is implemented.

**Connection-reference check:** Open the solution flow's Dataverse connection reference. A reference without a currently authenticated user/connection can prevent enabling the flow even when the action definitions are correct. Inspect existing authorized Dataverse references, choose a **signed-in working reference** permitted for this solution, save, and test without editing DC08 or DC10. Do not store credentials or create an unapproved service principal.

**Choice comparison:** For this training flow, comparisons using formatted Choice labels such as **P1 Critical** and **New** are readable, but they depend on those labels remaining unchanged and may be sensitive to localization. Verify source metadata before running. For a hardened future implementation, use the saved numeric Choice values after inspecting metadata, not guessed integers. Keep the actual flow condition and catalog text consistent.

**Terminate behavior:** When adding a **Terminate** action to an expected no-match or already-exists branch, choose a status deliberately. **Cancelled** is acceptable for a deliberately aborted training path but may make the run appear Cancelled rather than Succeeded. For a clean expected no-op that should be reported as success, use **Succeeded** and document the branch as skipped; use **Failed** only for an actual error. Verify the run's final status in history, not just the absence of a new Insight.

**Save** the flow and inspect any connector or licensing error. Do not enable unattended recurrence or an automatic trigger for this lesson. Ask for the required approval before activating any automation beyond the documented manual test.

### S14.11 — Test idempotency, human review and restoration

Run **DC14_Incident_Insight_Demo** manually once. Open its Run history and verify that the Incident and Rule rows were found, both Choice conditions matched, Existing Insight returned zero rows and **Add a new row** succeeded. Open DC Operational Insight → All Insights and confirm exactly one new incident-based record with Insight Code `INS-INC-0001-P1`. Reopen it and verify its **Rule** and **Related Incident** Lookups.

Run the exact flow a second time without changing INC-0001. Inspect the **Terminate** status or successful no-op branch, and record both the flow run status and the absence of a second Insight. An expected skipped creation can be represented by **Cancelled** or **Succeeded** depending on the documented branch, but do not label a Cancelled run Succeeded.  Verify that **Existing Insight** now finds the same code and **Add a new row is skipped**. There should still be only one Incident Insight and **three total** Insights. Inspect the Active alternate key for duplicate prevention. Do **not** delete the baseline insight to force another creation test.

**Human review test:** Open `INS-INC-0001-P1`, set Review Status = Under Review, save/reopen; then set Review Status = Reviewed and set Reviewed At to the simulated exercise time, save/reopen. Restore Review Status = **New**, clear Reviewed At and Review Notes that were only entered for this test. The restoration should return **DC Open Operational Insights** to the original three New records. This is a training review flag—not a real approver identity or security audit.

**Negative tests:** Open RUL-0001 and confirm its Rule Code and Enabled/Active status; do not disable it if other training processes depend on the rule. To demonstrate that a non-P1/non-New incident does not qualify, inspect INC-0002 source fields against the rule and explain why **the condition would fail**; do not change the production source row or make a second flow that writes an incorrect Insight. For repeat-run safety, inspect the condition's skipped branches in Run history.

| Evidence | Expected baseline after restoring test changes |
| --- | --- |
| Rules | Three enabled and active records |
| Knowledge | KNO-0001 and KNO-0002; original editorial statuses |
| Operational Insights | Exactly **three**: two manual source examples, one incident-derived |
| Insight Code uniqueness | One `INS-INC-0001-P1` row after two manual flow runs |
| Lookup links | Incident insight links to INC-0001 and RUL-0001; others link to their sources |
| Review state | New on all three Insights; no leftover test review timestamp |
| Earlier solution components | Prior apps, Dataverse data and flows unchanged |
| External behavior | No emails, Teams posts, approvals or live infrastructure calls |

### S14.12 — Optional AI-summary exercise, governance and final validation

**The core Part 14 is complete without generative AI.** If the environment makes AI Builder prompts available and you have explicit permission and adequate credits, you may optionally test an **isolated prompt** in the approved AI Hub/Prompt builder. Do not quietly add a Prompt column or turn on recurring generation in a university or shared environment.

**Permission/licensing gate:** Check the current environment's Copilot/AI Prompts features, your maker permissions, regional availability and AI Builder/Copilot Credits before running even a small experiment. Drafting or testing a prompt may have different credit behavior from running it through an app/flow. If access or credit approval is uncertain, record **Not attempted — optional feature unavailable/unapproved** and finish with the deterministic rule workflow.

**Optional prompt, synthetic inputs only:** In the approved prompt builder, create an isolated training prompt named **DC14 Fictional Insight Summary Test**, with the following instruction and *manually supplied* text from INS-INC-0001-P1: `Summarize only the provided fictional Incident Code, Priority, Incident Status and related evidence. Return a two-sentence review brief and a final sentence stating that a human must verify the underlying Dataverse record. Do not invent failure causes, claim live telemetry, provide switching instructions, or make autonomous decisions. If an input is missing, say it is unavailable.` Review the output against INC-0001. Discard the test if it invents anything. Do not automatically write it to an Incident, Work Order or Knowledge Article.

If the optional feature is unavailable, a **manual evidence-based summary** in the Insight form is the fully supported baseline. Do not deploy a Copilot Studio agent, connect enterprise knowledge or enable an autonomous workflow just to complete this exercise. Those are distinct architectural choices requiring permissions and governance.

**Final validations:** In the published Hub, verify that **DC Approved Knowledge** shows **only KNO-0001** and that Reviewed **KNO-0002** appears in the appropriate review view. Confirm **DC All Operational Insights** shows all three New records, the Rules view shows all three enabled rules, and earlier Shift Handover and Inventory Balance pages still open with HAN-0001/HAN-0002 and BAL-0002's manual reorder flag. Open every new form/view; inspect all three new tables and their schema prefixes, primary Required levels, three Active alternate keys and six real Lookups. Confirm the Supporting Operations Hub still opens its earlier pages, the manual flow's two executions are visible and the second run created no duplicate. Check the records, their related evidence, and that no temporary review changes remained. Publish the three Main forms and six views; publish the updated model-driven app only with authorization. Do not treat a Save button or flow Run succeeded notification as sufficient proof: reopen the target rows.

### Finish Part 14

You now have a **rules-first Intelligent Operations and Knowledge Review layer** on the existing fictional data center solution: a catalog of transparent conditions, source-linked operational findings, human-review states, safe knowledge entries, and one guarded instant cloud-flow demonstration. The exercise intentionally stops short of self-governing AI, live telemetry ingestion, autonomous dispatch or unverified safety recommendations.

**Microsoft Learn references:**

- [Create and edit Dataverse tables](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entities-portal)
- [Create and edit Dataverse columns](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-field-portal)
- [Create relationships in Dataverse](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-1n-relationships-portal)
- [Define Dataverse alternate keys](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/define-alternate-keys-reference-records)
- [Dataverse row-triggered and query flows](https://learn.microsoft.com/en-us/power-automate/dataverse/create-update-delete-trigger)
- [Prompt columns in Dataverse](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/prompt-column)
- [AI Builder licensing and credits](https://learn.microsoft.com/en-us/ai-builder/administer-licensing)

*All operating records, rules and knowledge are fictional. Do not use the guidance to issue live data center instructions or substitute for qualified engineering review.*


## Part 15 — Engineer, Test and Prepare the Solution for Release

The previous chapter connected transparent intelligence rules, knowledge articles and reviewable operational insights. Before a learning solution can be presented as a coherent engineering portfolio, the maker must test its dependencies, security assumptions, performance, failure behavior, accessibility and release boundaries. This lesson turns the existing **SunnyVerse Data Center Operations 360** into a documented **release candidate** without creating another application, changing existing business records, or claiming that an educational environment is production-ready.

**Scope of this chapter:** inventory existing components; inspect security and connection references; run permitted solution/app/flow checkers; perform non-destructive functional and negative tests; review performance, observability and ALM exports; and record a repeatable release decision. The starting environment might not have privileges for solution checker, security-role administration, managed-environment pipelines or a second test environment. **Record those limitations rather than bypassing them.** No new Dataverse table, flow, app, live integration or premium service is mandatory.

| Work product | Why it matters | Safe storage |
| --- | --- | --- |
| Component and dependency inventory | Establishes what is actually present, saved and published | Local engineering evidence; public summary without tenant identifiers |
| Solution/App/Flow checker results | Identifies functional, performance and maintainability concerns | Redacted evidence; never expose user or connection data |
| Security and connection-reference review | Distinguishes Dataverse authorization from fictional employee records | Private permission findings; public design principles |
| [Part 15 UAT Matrix](./quality/Part-15-UAT-Matrix.csv) | Repeatable tests, expected results and honest execution status | Public **template**, all rows initially Not Run |
| Local solution export, if permitted | Validates source portability and component completeness | **Private local backup**, not a public GitHub ZIP by default |
| Release-readiness decision | Records unresolved blockers and next engineering action | Only a sanitized conclusion may be published |

**Safety boundary:** use fictional records only. Do not change real university users or organization security policies, enable previously disabled flows, send emails/Teams posts, publish an app, import a managed solution, or run a deployment pipeline without authorization. A valid Dataverse write from a Canvas App is not evidence of race-free server validation. The Power BI monitoring dataset is still a local CSV Import model; the 50,000 readings do **not** belong in Dataverse.

### S15.01 — Open the existing solution and record the actual release baseline

Open [Power Apps](https://make.powerapps.com) and choose the already authorized environment. Select **Solutions → SunnyVerse Data Center Operations 360 → Overview**. Verify the existing publisher, the saved prefix **`svrg`**, and the actual solution version. Do not create another solution. In the solution component list use **Object type** filters to inspect apps, Dataverse tables, cloud flows, choices, forms, views, connection references and environment variables.

Check these known products from the earlier build, then record the **observed** status in a private evidence log:

| Component group | Specific existing object(s) | Evidence to capture |
| --- | --- | --- |
| Canvas apps | DC Operations Command Center; DC FieldOps; DC Capacity Planner | Saved version, published version, App checker and Play result |
| Model-driven apps | DC Asset & Maintenance Manager; DC Change & Risk Manager; DC Supporting Operations Hub | Saved/published app status and main navigation sections |
| Operational core | Department, Campus, Data Hall, Employee Profile, Asset, Sensor, Alarm, Incident | Actual tables, key status and representative Lookup rows |
| Maintenance and governance | Work Order, Field Inspection, Change Request, Risk Register, MOP Step | Existing forms, statuses and relationships |
| Supporting operations | Vendor, Spare Part, Inventory Balance, Shift Handover | Active keys and linked examples |
| Capacity planning | Hall Planning Baseline, Rack Plan, Rack Allocation, Capacity Request | Existing 2 baselines, 20 rack plans, 3 allocations and 2 requests, if unchanged |
| Intelligent operations | Intelligence Rule, Operations Knowledge Article, Operational Insight | Existing 3 rules, 2 articles and 3 insights, if unchanged |
| Existing flows | DC08 notification flows, DC10 Change Approval, DC14_Incident_Insight_Demo | Connection-reference health, actual On/Off state, last observed run status |
| Analytics | Locally saved DC360-Operations-Intelligence PBIX/PBIP | Local report verification, not a Power BI Service deployment |

**Verify the Supporting Operations Hub version carefully.** It may have a newer published timestamp while an edited version is still unsaved or unpublished. Open the **published** version through **Play**, inspect the Intelligence & Knowledge, Shift Operations and Inventory & Partners groups, and compare its actual version/time with the designer. Record **Published**, **Saved but not published**, or **Unverified** from direct evidence. Do not change the app's publication state merely to simplify the record.

**Checkpoint 1 — Baseline:** A single solution and its actual component statuses are recorded. No unsupported assertion about a published app or a passed test is made.

### S15.02 — Assemble the existing component and dependency inventory

In the solution use **See all → Objects** (or the available component list) and inspect each major group. If the maker exposes **Show dependencies / See dependencies**, open that view for a representative Canvas App, model-driven app and cloud flow. Record both the component type and whether it is already in this solution. If a dependency belongs to another managed/system solution, do **not** try to copy or delete it just to make the inventory look complete.

| Dependency chain | What must resolve | What to do if missing |
| --- | --- | --- |
| Campus → Data Hall → Asset → Sensor | Real parent Lookups and primary names | Return to the relevant earlier lesson; inspect existing relationships before creating anything |
| Department → Employee Profile → assignment | Existing fictional directory Lookup; not Entra identity | Check table metadata and selected lookup row, never invent a user |
| Alarm → Incident → Work Order | Source record links and published forms | Inspect parent records and form selection, not free-text substitutions |
| Spare Part → Inventory Balance → Hall | Manually checked reorder flag | Verify the arithmetic with source values; no automatic stock update implied |
| Rack Plan → Allocation → Request | Correct Asset/Hall references and reserve flags | Check distinct request vs reservation semantics; app validation is not atomic |
| Rule → Insight → Incident/Work Order/Balance | Documented rule and evidence references | Inspect six Part 14 Lookups, not only visible code labels |
| Solution-aware flow → connection reference | Working connection with an authenticated permitted owner | Identify missing connection; do not silently switch user credentials |

Create a private **component inventory** with columns: `Object Type`, `Display Name`, `Actual Schema/Logical Name`, `Solution Membership`, `Published/Enabled Status`, `Dependency`, `Finding`, `Evidence`. Record only the **necessary type and business name** in public materials. A private inventory may include opaque object IDs temporarily, but never upload them to GitHub.

**Checkpoint 2 — Dependency coverage:** Every app and flow used in the sample demonstrations has its critical prerequisites identified. Unavailable dependency views are documented, not guessed.

### S15.03 — Run the permitted solution and application checkers

In **Solutions**, locate the **unmanaged** SunnyVerse solution. If **... → Solution checker → Run** (or the currently available Check action) is enabled, run it on that solution and read the resulting status. Microsoft solution checker may report **Running**, **Results as of [date/time]**, or a failure state; it does not guarantee deployment success. Review findings by component, severity, category and rule. Save a **sanitized local finding summary** without usernames, URLs, connection identifiers or raw environment metadata.

Separately open each of the three Canvas Apps in Edit/Studio and inspect **App checker → Formulas, Accessibility, Performance, Data source**. Where modern editors use different headings, record the actual categories shown. A **0 Formula Errors** status does not cancel accessibility or performance findings. Review Power Fx delegation warnings and check for any new errors after earlier lessons.

For the three model-driven apps, inspect the app designer's validation result and reopen a representative Main form/view. For each solution-aware flow, open its checker, read any errors or warnings and inspect saved status and references. **Do not turn on, retest or publish** an app or flow merely because a checker prompts you to.

| Checker evidence | Required distinction |
| --- | --- |
| Solution checker result | Static inspection, not successful import or production suitability |
| Canvas Formulas | 0 errors is desirable; track other categories independently |
| Canvas Accessibility | Record remaining issues and priority; do not claim zero if not checked |
| Canvas Performance / Data source | Capture delegation, repeated calls, connection or rule findings |
| Model-driven designer validation | Navigation/forms/views must still work in published Play |
| Flow checker | No syntax errors does not prove connection health or runtime execution |

**Checkpoint 3 — Findings register:** Document the actual result and unresolved blocker for each available checker. If unavailable for licensing or permission reasons, record **Not Run — permission/tool unavailable**; never invent a pass.

### S15.04 — Review Dataverse security and identity boundaries without changing roles

Under the Power Platform admin center or the authorized environment's **Settings → Users + permissions → Security roles** (UI varies), inspect only the role configuration you are permitted to see. Do not edit roles or add users during this baseline review. Dataverse **organization-owned** tables—used for many DC360 masters and supporting registers—do not automatically gain record-owner row isolation: for their ordinary privileges the role generally allows the operation organization-wide or denies it. A fictional **DC Employee Profile** row is not a signed-in Microsoft Entra user. A fictional **Acknowledged** or **Approved** field is not authentication.

Use this **proposed role matrix** to discuss least privilege without claiming the tenant implements it. Actual table permissions must be checked per role before this can be called enforced security:

| Fictional job function | Needed business outcome | Proposed table permissions | Not implied |
| --- | --- | --- | --- |
| Operations viewer | See active incidents, alarms, work orders and Insights | Read only, scoped as ownership model permits | Create/Edit/Delete rights |
| Field engineer | Update authorized inspection and assigned work forms | Read and limited Write/Create on relevant tables after design review | Privilege based on fictional name in Employee Profile |
| Shift coordinator | Review handovers and balances | Read registers, controlled Write where approved | Digital-signature authentication |
| Maintenance planner | Review asset and work-order records | Read and validated Write in the right workstreams | Unrestricted access to every table |
| Governance reviewer | Review change and knowledge records | Read and controlled review fields | Ability to approve real safety work |
| Solution administrator | Configure components and permissions | Separate privileged role assigned by tenant administrator | Permission for everyone using an app |

For each row, distinguish **Read, Create, Write, Delete, Append, Append To** (and Assign/Share when relevant). A model-driven app's page being visible does not prove that the underlying Dataverse data is accessible. If a second **authorized** test account is available, have the owner run read-only access tests; otherwise record access separation **Not Tested**. Do not use a colleague's credentials, make dummy real users, weaken an institution's security roles or enable auditing without approval.

**Checkpoint 4 — Security review:** Record the current permission visibility and proposed matrix; state whether actual role-separated tests were performed. The organization-owned table limitation remains a documented architectural decision.

### S15.05 — Inspect connection references, environment variables and connector health

Within the solution open **Connection references** and **Environment variables** if they exist. Match existing references to the flows/apps that consume them; do not assume a reference is usable simply because it is listed. Examine the existing DC08 notification flows, DC10 Change Approval and DC14 instant Insight flow. Record for each the **connector family** (Dataverse, Outlook, Teams, Approvals if present), authorized connection health, environment-variable dependency and current On/Off state.

A reference with **no signed-in user or connection** may prevent a flow from being enabled. A different valid Dataverse reference can solve that problem *when permitted*, but do not silently change it during a read-only ALM assessment. Record the reference type and observed health privately; **do not publish a connection ID, owner email, URL, tenant ID or token**.

If the solution has an environment variable representing a notification test recipient, inspect **schema name, type, default/current value presence and where consumed** without exposing its value. Do not change the recipient or trigger a notification. If no variable exists, write **Not present**—do not create a placeholder just to satisfy a template. Some deployment settings are populated at import time and are never safe to hard-code for a public learner repo.

**Checkpoint 5 — Connector inventory:** The dependencies, health and existing flow states are recorded. No email, Teams or approval run has been triggered.

### S15.06 — Inspect Canvas performance, delegation and user experience

Open the **published** DC Operations Command Center, DC FieldOps and DC Capacity Planner in a controlled training session. Use ordinary navigation, search and **read-only** form operations first. Where the editor provides **Live monitor/Monitor**, launch a session only if authorized and inspect the calls for the tested screen. Do not copy personally identifying request headers or environment details into the portfolio.

| Diagnostic | What to observe | Engineering interpretation |
| --- | --- | --- |
| Home and gallery loading | Whether meaningful content appears and refresh works | A loaded page is not evidence of fast performance for every dataset size |
| Dataverse calls | getRows/read operations, errors and durations | Detect repeated calls and unexpected 4xx/5xx/429 responses |
| Delegation | Source query behavior versus client-side limits | The 50,000 monitoring CSV rows are **not** in Dataverse; no Canvas delegation proof for them |
| Search and filter | Existing Incident/Asset/Work Order collections and views | Verify correctness of visible search results before optimizing |
| Capacity validation | Reservation conflict and 42U/budget checks | Client-side pre-check still cannot prevent concurrent writers |
| Forms | Saved vs published display and typed Lookup cards | A blank display label may differ from correctly persisted Lookup metadata |
| Accessibility | Contrast, labels, keyboard focus and screen-reader naming where available | Record all outstanding issues rather than declaring readiness from Formula count |

Use the environment's existing fictional records and **avoid writes** during a performance-only check. If you must run a single safe form submit, agree the target training row, record its baseline values and restore them immediately. Do not enable load testing against shared Dataverse tables or generate thousands of network calls. Capture only redacted timings and counts; do not invent measured response times.

**Checkpoint 6 — Performance:** Actual inspected warnings and reproducible slow/error paths are documented, with explicit **Not Tested** for unavailable devices, accessibility tooling or load conditions.

### S15.07 — Verify data quality, relationship integrity and sample baselines

Use saved Dataverse views or supported read-only Dataverse queries and the already verified Power BI source files. Compare the following **expected training dataset** to actual current counts, recognizing that a learner may have intentionally created extra records during prior exercises:

| Source family | Intended baseline | Verification method |
| --- | --- | --- |
| Campus / Data Hall / Department | 1 / 2 / 6 | Records persist after refresh; real parent Lookups |
| Employee Profile / Asset / Sensor | 20 / 100 / 24 | Unique codes, no orphaned Asset or Hall references |
| Alarm / Incident / Work Order | 120 / 200 / 500 | Unique record codes; selected parent and status fields |
| Supporting Operations | 2 Vendors, 3 Spare Parts, 3 Balances, 2 Handovers | Open records, Low-stock Boolean manually reconciled |
| Capacity | 2 Hall Baselines, 20 Rack Plans, 3 Allocations, 2 Requests | Hold Rack 013/019, capacity arithmetic and real Lookups |
| Intelligence | 3 Rules, 2 Knowledge Articles, 3 Insights | Required Rule Lookup, source links, Active alternate keys |
| Monitoring report | 50,000 imported CSV readings (24 sensors) | Local Power BI Desktop model refresh or sanitized source verification |

Inspect several actual **alternate-key statuses** under table **Schema → Keys**. Reopen sample Lookup links, including **INS-INC-0001-P1 → INC-0001 / RUL-0001** and **INS-BAL-0002-REORDER → BAL-0002 / RUL-0003**, where each arrow represents an Insight Lookup pointing to its existing source or Rule. Count unique business codes rather than using a visual's row count as proof. Do not automatically repair mismatches by deleting records. For Capacity, note that the baseline Hall planning figures and simulated monitoring samples are distinct models; no measured rack power is reconciled to design headroom.

**Checkpoint 7 — Data integrity:** Record exact present counts, unique keys and sampled Lookup outcomes. Any extra/missing records are investigated without overwriting prior practice data.

### S15.08 — Execute a non-destructive UAT regression matrix

Open the [Part 15 UAT Matrix](./quality/Part-15-UAT-Matrix.csv). It is a **template**, not a report of tests already executed. All 18 tests begin **Not Run**. Save a **private working copy** to record actual execution status, evidence and blockers; never overwrite the public template with tenant-specific observations. Execute permitted tests in the listed order and write **Pass**, **Fail**, **Blocked**, or **Not Run** with a concise evidence note.

| Test cluster | Examples | Safe rule |
| --- | --- | --- |
| Foundation/data | Uniqueness, Lookup navigation, key status | Read-only checks; no duplicate imports |
| Canvas | Home KPI, search, field inspection, capacity precheck | Avoid unsafe writes and restore test record changes |
| Model-driven | Forms/views, knowledge filter, handover and inventory records | Choose published app version where possible |
| Automation | Prior saved DC08/DC10 evidence and DC14 idempotency | Prefer inspecting historical run history; no re-trigger without permission |
| Analytics | Seven Power BI tables, six relationships, 20 measures, five pages | Desktop-local testing, no Power BI Service publication |
| Security/ALM | Role boundary review, solution checker, export readiness | No user-role edits or import/deploy without approval |

**Negative tests:** For a record with a required field, inspect the form's validation UI without submitting invalid data. For lookup mismatch, inspect that the saved parent opens. For reservation overlap, use the already documented non-writing capacity precheck. For the DC14 duplicate flow, prefer **existing two run histories** unless explicitly approved to trigger it again. For error-path tests, use a copied local Power BI test session or a safe approved demo dataset, not a live user or actual notification recipient.

**Checkpoint 8 — Regression evidence:** An honest 18-row UAT result with no blank status values. **Not Run/Blocked** tests remain outstanding; they cannot be counted as Pass.

### S15.09 — Review flow resilience, diagnostics and review auditability

In [Power Automate](https://make.powerautomate.com) select the same environment and existing solution. Open the **details** and **Run history** of the current solution cloud flows. Do not change their On/Off state or send a test notification. For any accessible historical run inspect action status, duration, retry/error indication and the branch taken. The DC14 flow must still demonstrate **one Insight after two controlled runs**, not duplicated records.

| Failure/recovery concern | What to look for | Evidence boundary |
| --- | --- | --- |
| Trigger and inputs | Manual versus automatic trigger, source code and guard | An instant demo should not run on an unattended schedule |
| Lookup and Choice types | Logical names, formatted labels versus stored option values | Renaming a displayed label can break a text comparison |
| Retry and duplicate prevention | Existing code-key uniqueness and duplicate query | A List rows guard alone is not an atomic race-free lock |
| Expected early termination | **Cancelled** versus **Succeeded** action configuration | Do not describe a Cancelled run as Succeeded; capture actual run status |
| Connection references | Signed-in owner and authorized Dataverse access | Never publish connection/account IDs or tokens |
| Historical action failure | 400/403/429, required field, connector throttle | Record actual error category, not guessed cause |
| Review trail | Insight Review Status, Reviewed At and restored baseline | Fictional review is not an authenticated electronic signature |

If you lack permissions to view history, record **Not visible**. Do not create new monitoring flows or modify DC08, DC10 or DC14 in this chapter. **Checkpoint 9 — Resilience review:** Evidence and real limitations are logged without changing the operating system of record.

### S15.10 — Review ALM packaging and export an authorized local solution backup

Return to **Solutions → SunnyVerse Data Center Operations 360 → Overview**. Check solution components, object dependencies, publish readiness and the version. If you have permission and **the owner authorizes a local export**, select **Export** and follow the solution export wizard. For a development source backup, an **Unmanaged** export may be appropriate; a **Managed** package is a deployment artifact for an authorized target—not something to import back into the original development environment as a casual test. **Do not import anything, install a managed layer, or create a deployment pipeline here.**

| Release artifact/step | Recommended action in this lesson | Important limit |
| --- | --- | --- |
| Unmanaged solution export | Download only to an authorized private local folder | May include configuration and connection-reference metadata; privacy-review before sharing |
| Managed export | Optional if licensing/policy and intended target allow | Do not import to source environment or claim production deployment |
| Component dependency report | Inspect before export | Solution checker success does not prove target import succeeds |
| Connection-reference settings | Document types and whether a target connection is needed | Never commit real connection IDs, recipient addresses or tenant values publicly |
| Environment-variable settings | Record schema/type and target value requirement | No secrets or hard-coded environment URLs in GitHub |
| Version and package hash | Record release candidate version and optional SHA-256 privately | A saved ZIP is not a deployed release |

Power Platform ALM uses **unmanaged customizations as development source** and **managed packages for controlled deployment to downstream environments**. Deployment also requires target-environment permissions, suitable connection references, solution dependencies and sometimes managed-environment licensing. Where a second authorized test environment is unavailable, mark an import-test **Not Performed**; do not create a new environment or use an institutional production environment without permission.

**Checkpoint 10 — ALM:** Record whether an export actually completed, its local destination and a sanitized hash if produced. No unauthorized GitHub upload, solution import or deployment occurs.

### S15.11 — Decide release readiness and document rollback boundaries

Create a private release-candidate review using the actual evidence. Apply the following gates in this order:

| Gate | Required evidence | Outcome rule |
| --- | --- | --- |
| Solution integrity | Dependency inventory and relevant checker report | Major unresolved required component = Blocked |
| Functional UAT | Test matrix with actual Pass/Fail/Blocked statuses | A Fail cannot be relabelled Pass by commentary |
| Security | Role/connection boundary understood, no unexpected access | Untested segregation is a known limitation, not verified least privilege |
| Reliability | Flow run outcomes and retry/idempotency observations | No unverified notification/approval/external calls |
| Accessibility and performance | App checker categories reviewed | Outstanding findings documented with severity |
| Analytics | Source import, DAX and report evidence from Desktop | PBIX validated locally is not published to Power BI Service |
| Packaging | Export/deployment readiness actually observed | An exported ZIP does not prove a test-environment import |
| Privacy | No tenant/user identifiers in public material | Do not release unsanitized screenshots, URLs or packages |

Classify each gate **Pass**, **Conditional**, **Blocked**, or **Not Tested** and record an owner-independent rationale. An overall **Learning demonstration ready** decision may be different from **Enterprise deployment ready**. With untested server-side rack concurrency, unknown tenant security-role separation and no authorized target environment, do not claim production readiness.

For a failure after an authorized future deployment, the response is **stop further changes, capture the error, review versioned artifacts and obtain an approved recovery plan**. A “rollback” is not automatically achieved by deleting a managed solution; that may remove components or data. Do not attempt unapproved removal/import/restore. **Checkpoint 11 — Decision:** A written evidence-based release classification and bounded recovery procedure, not an invented deployment success.

### S15.12 — Package safe portfolio evidence and complete the engineering review

In an authorized private folder, consolidate the **test results, sanitized issue summary, component inventory, relevant screen evidence and export details if an export was permitted**. Keep source code, synthetic datasets and the cumulative learner guide in their existing GitHub location. Do **not** publish environment IDs, signed-in names, user profile paths, secrets, exact connection references, real addresses, private tenant reports, or original solution exports without an explicit security review and authorization.

Create a concise learner-readable completion record from the actually performed checks. This may report totals, generic component types, observed troubleshooting lessons and any honest outstanding limitations—but must not include a private implementation transcript or unperformed future scope. Preserve the Part 15 public UAT matrix with **Not Run** statuses so readers can perform their own tests independently. If you capture screenshots, crop/redact the browser chrome and user/tenant details.

**Final verification:** Verify the original three Canvas apps, three model-driven apps, established Dataverse tables and current flows are **unchanged unless you deliberately and separately authorized a correction**. The Power BI Desktop source still opens locally. Review the Hub published version before concluding that Part 14 navigation is live. Confirm the solution has not been imported into any new environment and that no unauthorized messages, permissions changes, deletion or AI execution occurred.

**Checkpoint 12 — Completion:** A traceable engineering/UAT evidence set and release decision. If anything remains unavailable, label it explicitly and preserve the working previous application state.

### Finish Part 15

You have learned how to evaluate an existing Power Platform solution as an engineering release candidate: inventory and dependencies, static checkers, access control, connector health, accessibility and performance, data integrity, regression tests, observed run history, ALM export boundaries, release gates and safe evidence handling. The exercise documents **actual evidence and remaining risk**, not a claim that a fictional educational environment has become an enterprise production system.

**Microsoft Learn references:**

- [Solution checker in Power Apps](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/use-powerapps-checker)
- [Dataverse security roles and privileges](https://learn.microsoft.com/en-us/power-platform/admin/security-roles-privileges)
- [Security concepts for organization-owned tables](https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds)
- [Live monitor and Trace in Canvas apps](https://learn.microsoft.com/en-us/troubleshoot/power-platform/power-apps/create-and-use-apps/monitor-debugging-canvas-apps)
- [Export a Power Apps solution](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/export-solutions)
- [Managed and unmanaged solutions](https://learn.microsoft.com/en-us/power-platform/alm/solution-concepts-alm)
- [Connection references and environment variables](https://learn.microsoft.com/en-us/power-platform/alm/conn-ref-env-variables-build-tools)
- [Solution layers](https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm)

*The exercise uses fictitious data. It does not authorize changes to live data centers, real users, security administration, institutional policies or external deployments.*

## Microsoft Learn references
- [Define alternate keys in Dataverse](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/define-alternate-keys-reference-records)
- [Create a model-driven app](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-model-driven-app)
- [Add and remove forms and views in an app](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-add-remove-forms-views-dashboards)
- [Dataverse cascading relationship behavior](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/configure-entity-relationship-cascading-behavior)

- [Create and test Power Automate approvals](https://learn.microsoft.com/en-us/power-automate/modern-approvals)
- [Dataverse relationship cascading behavior](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/configure-entity-relationship-cascading-behavior)
- [Manage model-driven app forms and views](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-add-remove-forms-views-dashboards)


- [Build model-driven apps in Power Apps](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/app-building-steps)
- [Create or configure model-driven app forms](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-and-edit-forms)
- [Create and edit public views](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-edit-views)
- [Import CSV files with lookup-reference mapping](https://learn.microsoft.com/en-us/power-apps/user/import-data)

- [Create a Power Platform solution](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-solution)
- [Create and edit Dataverse tables](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entities-portal)
- [Create and edit Dataverse columns](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-field-portal)
- [Dataverse table types and ownership](https://learn.microsoft.com/en-us/powerapps/maker/data-platform/types-of-entities)
- [Create global choices](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/custom-picklists)
- [Create and edit one-to-many / many-to-one relationships](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-1n-relationships-portal)
- [Import data and map choices/lookups](https://learn.microsoft.com/en-us/power-apps/user/import-data)
- [Create a relationship by adding a lookup](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-entity-lookup)
- [Date and Time column behavior](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/behavior-format-date-time-field)
- [Create a Canvas App inside a solution](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/add-app-solution)
- [Browse, display and edit records with forms](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/working-with-forms)
- [Power Fx: Search, Filter and LookUp](https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-filter-lookup)
- [Power Fx: SubmitForm and EditForm](https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-form)
- [Understand Canvas App delegation](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/delegation-overview)
- [Enable attachments on a Dataverse table](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/create-edit-tables)
- [Attachments control in canvas apps](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-attachments)
- [Build phone-sized Canvas Apps](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/app-from-image)
- [Dataverse: trigger cloud flows on added/modified/deleted rows](https://learn.microsoft.com/en-us/power-automate/dataverse/create-update-delete-trigger)
- [Use environment variables in solution cloud flows](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/environmentvariables-power-automate)
- [Create a cloud flow in Power Automate](https://learn.microsoft.com/en-us/power-automate/get-started-logic-flow)

*All organizations, facilities, staff, and operational scenarios in this learning project are fictional. Do not use this guide to control live data center infrastructure.*
