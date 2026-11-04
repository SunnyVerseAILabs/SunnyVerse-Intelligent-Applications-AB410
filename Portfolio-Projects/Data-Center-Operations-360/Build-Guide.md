# Data Center Operations 360 — Build-Along Guide

**SunnyVerse AI Labs | Independent Power Platform learning project**  
**Fictional organization:** SunnyVerse Renewable Group  
**Published:** Parts 00–06 — Solution Foundation, Department Master, Campus and Data Halls, Employee Directory, Asset and Sensor Registry, Alarm and Incident Management, Operations Command Center

[Project home](./README.md) · [Practice data](./data/README.md)

Welcome to Data Center Operations 360. In this project, you will build a fictional data center operations solution using Microsoft Power Platform. The work is completed in an environment where you have permission to develop, and all practice records are fictional.

Part 00 prepares the solution. Parts 01–04 build the reference data, Part 05 adds alarms and incidents, and Part 06 creates a connected Canvas App. Follow the lessons in order in an authorized learning environment.

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

Our Dataverse tables now contain fictional assets, alarms and incidents. In this lesson, we'll turn those records into a working **tablet-style Canvas App** for reviewing operational activity, finding incidents, opening related records and updating incident assignments. The app reads and writes the existing Dataverse tables directly; it does not require a new table, CSV import or Power Automate flow.

We'll build one app named **DC Operations Command Center** with five screens: Home, Incidents, Incident Details, Incident Editor and Alarms. This is a learning application using fictional data, not a real facility-control console. It does not implement live sensor monitoring or authenticated role-based approvals.

**Formula convention:** The examples use English-language Power Fx, commas as argument separators, and the exact **column display names** from Parts 04–05. In Power Apps Studio, the existing Dataverse tables generally appear under their **plural** names (`'DC Incidents'`, `'DC Alarms'` and `'DC Assets'`). Select the actual source shown by Studio autocomplete if the label differs in your environment. The existing technical schema names retain the `svrg` publisher prefix; Canvas control names below are local app identifiers, not additional Dataverse columns.

### S06.01 — Create the Canvas App and connect Dataverse

Open [Power Apps](https://make.powerapps.com), select your authorized learning environment, then navigate to **Solutions → SunnyVerse Data Center Operations 360 → New → App → Canvas app**. Select **Tablet** (landscape) when asked for the format. If the current designer instead starts with a blank-app dialog, choose **Tablet size**. Set the app's display name to **DC Operations Command Center** when the name field is offered, or use **Settings → General → App name** after Studio opens.

In Studio, open **Data** from the left rail and select **Add data → Microsoft Dataverse**. Add the following three tables from the *same environment*:

| Data source in Studio | Existing Dataverse table | Used for |
| --- | --- | --- |
| `'DC Incidents'` | DC Incident (`svrg_DCIncident`) | Incident queues, forms and edits |
| `'DC Alarms'` | DC Alarm (`svrg_DCAlarm`) | Alarm search and details |
| `'DC Assets'` | DC Asset (`svrg_DCAsset`) | Summary inventory count |

Select the **App** node in the tree view and set **StartScreen** to `scrHome` *after* creating that screen in the next step. Do not create another connection to an unrelated environment.

### S06.02 — Create the screens, add controls and connect navigation

We will first create the five screens and give each control a consistent name. **Only add the controls listed for this step**; the Incident forms and Alarm browser controls will be inserted in their respective later activities. This avoids adding the same control twice.

**1. Create and rename the screens.** In Power Apps Studio, select **Tree view** on the left. Find the first screen (often named `Screen1`), select its **…** menu (or right-click), choose **Rename**, type `scrHome` and press **Enter**. Then choose **New screen → Blank**, rename the new screen `scrIncidents`, and repeat **New screen → Blank** three more times to create `scrIncidentDetail`, `scrIncidentEdit` and `scrAlarms`. The Tree view should now show **exactly these five screens**.

| Order | Screen name | Purpose |
| --- | --- | --- |
| 1 | `scrHome` | Summary counts and recent incidents |
| 2 | `scrIncidents` | Search the incident queue |
| 3 | `scrIncidentDetail` | View a selected incident |
| 4 | `scrIncidentEdit` | Create or edit an incident |
| 5 | `scrAlarms` | Browse and inspect alarms |

**2. Learn the add-and-rename action once.** Select the target **screen name in Tree view**, then choose **Insert**. For a title or count choose **Text label / Label**; for a navigation action choose **Button**; for search choose **Text input**; and for a list choose **Gallery → Vertical** (choose a title/subtitle layout if offered). Find the newly inserted control *under that screen* in Tree view, select **… → Rename**, enter the exact name below and press **Enter**. Repeat for the remaining controls. Prefer **Classic** Label, Button, Text input and Gallery variants when available so the formulas in this lesson use the `Text` property. A Modern Text input may use `Value` instead; if you choose Modern, replace references to `txtIncidentSearch.Text` with `txtIncidentSearch.Value` consistently.

**3. Add the controls screen by screen.** Work down the table; each comma-separated name represents **one separate control**. Do not type these names into the canvas as visible text—enter them using **Rename** in Tree view.

| Select screen | Add **now** (control type → exact names) | Add **later** |
| --- | --- | --- |
| `scrHome` | **Labels:** `lblHomeTitle`, `lblCountIncidents`, `lblCountAlarms`, `lblCountAssets`; **Vertical gallery:** `galRecentIncidents`; **Buttons:** `btnHomeIncidents`, `btnHomeAlarms`, `btnRefreshHome` | Populate KPI/gallery formulas in **S06.03** |
| `scrIncidents` | **Label:** `lblIncidentsTitle`; **Text input:** `txtIncidentSearch`; **Vertical gallery:** `galIncidents`; **Buttons:** `btnOnlyUnassigned`, `btnNewIncident`, `btnIncidentsHome` | Configure search and filtering in **S06.04** |
| `scrIncidentDetail` | **Label:** `lblIncidentTitle`; **Buttons:** `btnEditIncident`, `btnDetailBack` | Insert **Display form** `frmIncidentView` in **S06.05** |
| `scrIncidentEdit` | **Label:** `lblEditTitle`; **Buttons:** `btnSaveIncident`, `btnCancelIncident` | Insert **Edit form** `frmIncidentEdit` in **S06.06** |
| `scrAlarms` | **Label:** `lblAlarmsTitle`; **Button:** `btnAlarmsHome` | Insert **Text input** `txtAlarmSearch`, **Vertical gallery** `galAlarms` and **Display form** `frmAlarmView` in **S06.07** |

**4. Arrange the controls.** Select each title label and place it at the top of its screen. Set **Font size = 24** and **Font weight = Bold** where offered. On `scrHome`, arrange the three count labels across the upper area, followed by the recent-incidents gallery and the navigation/refresh buttons. On `scrIncidents`, place the search input above the incident gallery, with the filter and New Incident buttons nearby. On the detail and edit screens, keep the title at the top and their action buttons below or beside the space reserved for the forms. On `scrAlarms`, reserve the left side for the gallery and the right side for the read-only form added in S06.07. Leave approximately 16 pixels between adjacent controls; you can resize and refine the layout after the data is connected.

**5. Set the screen titles and navigation buttons.** To change a property, select a control in **Tree view**, choose the property (for example **Text** or **OnSelect**) using the property drop-down above the formula bar, paste the expression and press **Enter**. **Text** controls what a label or button displays; **OnSelect** is what happens when a button is clicked.

| Control | Property | Formula / value |
| --- | --- | --- |
| `lblHomeTitle` | Text | `"Data Center Operations 360 — Command Center"` |
| `lblIncidentsTitle` | Text | `"Incident Management"` |
| `lblIncidentTitle` | Text | `"Incident Details"` |
| `lblEditTitle` | Text | `"Incident Editor"` |
| `lblAlarmsTitle` | Text | `"Alarm Monitoring"` |
| `btnHomeIncidents` | Text | `"Open incidents"` |
| `btnHomeIncidents` | OnSelect | `Navigate(scrIncidents, ScreenTransition.Fade)` |
| `btnHomeAlarms` | Text | `"Open alarms"` |
| `btnHomeAlarms` | OnSelect | `Navigate(scrAlarms, ScreenTransition.Fade)` |
| `btnIncidentsHome` | Text | `"Home"` |
| `btnIncidentsHome` | OnSelect | `Navigate(scrHome, ScreenTransition.None)` |
| `btnAlarmsHome` | Text | `"Home"` |
| `btnAlarmsHome` | OnSelect | `Navigate(scrHome, ScreenTransition.None)` |
| `btnDetailBack` | Text | `"Back to incidents"` |
| `btnDetailBack` | OnSelect | `Navigate(scrIncidents, ScreenTransition.None)` |

The other buttons, galleries, forms and search properties are deliberately configured in **S06.03–S06.07**. You do not need to assign temporary formulas to them now.

**6. Choose the starting screen.** Select **App** at the top of Tree view (not the `scrHome` screen). In the property drop-down select **StartScreen**, enter `scrHome` without quotes, and press **Enter**. The app should launch on Home.

Finally choose **Preview (Play/F5)** and test **Open incidents → Home** and **Open alarms → Home**. Use **Back to incidents** from `scrIncidentDetail` if you preview that screen directly. A blank gallery or unconfigured form at this stage is expected; the next activities connect them to Dataverse.

### S06.03 — Add live-count KPIs and a recent-incident list

Set the following properties on `scrHome`. A label should have its **Text** property set to a *formula*, not a hard-coded number.

| Control | Property | Formula / value |
| --- | --- | --- |
| `lblHomeTitle` | Text | `"Data Center Operations 360 — Command Center"` |
| `lblCountIncidents` | Text | `"Incidents: " & CountRows('DC Incidents')` |
| `lblCountAlarms` | Text | `"Alarms: " & CountRows('DC Alarms')` |
| `lblCountAssets` | Text | `"Assets: " & CountRows('DC Assets')` |
| `galRecentIncidents` | Items | `Sort('DC Incidents', 'Reported At', SortOrder.Descending)` |
| `galRecentIncidents` | OnSelect | `Set(varSelectedIncident, ThisItem); Navigate(scrIncidentDetail, ScreenTransition.None)` |
| `btnRefreshHome` | Text | `"Refresh"` |
| `btnRefreshHome` | OnSelect | `Refresh('DC Incidents'); Refresh('DC Alarms'); Refresh('DC Assets'); Notify("Data refreshed.", NotificationType.Information)` |

Inside `galRecentIncidents`, use a Title and Subtitle layout or insert two labels into the gallery template. Configure their **Text** properties as follows:

| Gallery template label | Text formula |
| --- | --- |
| Title | `ThisItem.'Incident Name'` |
| Subtitle | `ThisItem.'Incident Code' & "  |  " & Text(ThisItem.Priority) & "  |  " & Text(ThisItem.'Incident Status')` |

If the gallery contains a chevron icon or labels that intercept clicks, set those controls' **OnSelect** property to `Select(Parent)`. Keep the gallery connected directly to Dataverse; do not copy its records into a static collection.

The count labels show the currently visible Dataverse totals. Microsoft notes that unfiltered `CountRows` on Dataverse can use cached counts, so use the source tables rather than those numbers as proof of exact import completeness. The seeded dataset contains 200 incidents, 120 alarms and 100 assets before any additional edits or records are created.

### S06.04 — Build the searchable Incident queue

On `scrIncidents`, enter the following properties:

| Control / screen | Property | Formula / value |
| --- | --- | --- |
| `lblIncidentsTitle` | Text | `"Incident Management"` |
| `txtIncidentSearch` | HintText (Classic) | `"Search incident code or name"` |
| `scrIncidents` | OnVisible | `Set(varOnlyUnassigned, false)` |
| `btnOnlyUnassigned` | Text | `If(varOnlyUnassigned, "Show all", "Unassigned only")` |
| `btnOnlyUnassigned` | OnSelect | `Set(varOnlyUnassigned, !varOnlyUnassigned)` |
| `galIncidents` | OnSelect | `Set(varSelectedIncident, ThisItem); Navigate(scrIncidentDetail, ScreenTransition.None)` |
| `btnNewIncident` | Text | `"New incident"` |
| `btnNewIncident` | OnSelect | `Set(varIsNewIncident, true); NewForm(frmIncidentEdit); Navigate(scrIncidentEdit, ScreenTransition.None)` |

Set `galIncidents.Items` to:

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

This searches the two text fields by prefix and optionally shows records without an Assigned Engineer. Selecting **Unassigned only** changes the gallery without modifying any incident. If the editor displays a blue delegation warning, inspect the flagged expression and the actual Dataverse column type before relying on the filter in a larger environment; do not raise the data row limit merely to hide the warning.

For the gallery's visible fields, set:

| Template label | Text formula |
| --- | --- |
| Title | `ThisItem.'Incident Name'` |
| Subtitle | `ThisItem.'Incident Code' & "  |  " & Text(ThisItem.Priority)` |
| Status | `Text(ThisItem.'Incident Status')` |
| Assignment | `If(IsBlank(ThisItem.'Assigned Engineer'), "Unassigned", ThisItem.'Assigned Engineer'.'Employee Name')` |

For the Assignment label, use the actual related-record **Employee Name** property suggested by Studio autocomplete. The selection is a Dataverse employee lookup, not the signed-in Microsoft user. Set the labels' **OnSelect** to `Select(Parent)` if needed.

### S06.05 — Show complete Incident details

On `scrIncidentDetail`, insert a **Display form** using **Insert → Forms → Display** (or the equivalent form command). Rename it `frmIncidentView`.

| Control | Property | Formula / value |
| --- | --- | --- |
| `lblIncidentTitle` | Text | `"Incident Details"` |
| `frmIncidentView` | DataSource | `'DC Incidents'` |
| `frmIncidentView` | Item | `varSelectedIncident` |
| `btnEditIncident` | Text | `"Edit incident"` |
| `btnEditIncident` | OnSelect | `Set(varIsNewIncident, false); EditForm(frmIncidentEdit); Navigate(scrIncidentEdit, ScreenTransition.None)` |

Select the form and choose **Edit fields → Add field**. Include these existing columns: **Incident Name**, **Incident Code**, **Incident Category**, **Priority**, **Incident Status**, **Reported At**, **Incident Description**, **Safety Related**, **Resolution Notes**, **Source Asset**, **Reported By**, **Assigned Engineer**, and **Related Alarm**.

Change the form's **Columns** setting to **2** if it improves readability on your tablet canvas. Preview from the Incident queue and open an existing incident, for example **INC-0002**. The form should display its existing field values and related records, without letting you edit them directly on this screen.

### S06.06 — Add the Incident create/edit form and save behavior

On `scrIncidentEdit`, insert **Insert → Forms → Edit form** and rename it `frmIncidentEdit`. In the **Data** pane, choose **DC Incidents**. Add the same 13 fields from S06.05. Use the default controls that Power Apps generates for **Choice**, **Yes/No**, date/time and **Lookup** columns: do not replace the lookup cards with free-text inputs, and leave their generated **Update** properties intact unless a specific correction is required.

| Control | Property | Formula / value |
| --- | --- | --- |
| `lblEditTitle` | Text | `If(varIsNewIncident, "New Incident", "Edit Incident")` |
| `frmIncidentEdit` | DataSource | `'DC Incidents'` |
| `frmIncidentEdit` | Item | `varSelectedIncident` |
| `btnSaveIncident` | Text | `"Save incident"` |
| `btnSaveIncident` | OnSelect | `SubmitForm(frmIncidentEdit)` |
| `btnCancelIncident` | Text | `"Cancel"` |
| `btnCancelIncident` | OnSelect | `ResetForm(frmIncidentEdit); If(varIsNewIncident, Navigate(scrIncidents, ScreenTransition.None), Navigate(scrIncidentDetail, ScreenTransition.None))` |

Set `frmIncidentEdit.OnSuccess` to:

```powerfx
Set(varSelectedIncident, frmIncidentEdit.LastSubmit);
Set(varIsNewIncident, false);
Refresh('DC Incidents');
Notify("Incident saved.", NotificationType.Success);
Navigate(scrIncidentDetail, ScreenTransition.None)
```

Set `frmIncidentEdit.OnFailure` to:

```powerfx
Notify(
    Coalesce(frmIncidentEdit.Error, "Incident was not saved."),
    NotificationType.Error
)
```

The same form handles two modes. **Edit incident** uses `EditForm` to update the existing record; **New incident** uses `NewForm` so the learner can enter a new record. When creating an incident, complete all required columns, including **Incident Name**, **Incident Code**, **Incident Category**, **Priority**, **Incident Status**, **Reported At**, **Incident Description**, **Source Asset** and **Reported By**. Select existing Lookup records using the generated lookup pickers. **Assigned Engineer** and **Related Alarm** may remain blank. Use a new, unique business code (for example `INC-MAN-0001`) and do not assume the Text field's Business required setting enforces uniqueness; record-key enforcement is a separate topic.

Select **Save incident** once and observe the success notification. If the save fails, the form stays on the edit screen and displays a validation or Dataverse error. **Cancel** resets unsaved field changes. This screen updates only the incident record and does not send Teams notifications, initiate approvals or automatically update an associated alarm; those are separate automation features.

### S06.07 — Add the Alarm browser

Open `scrAlarms` and use **Insert → Text input** for `txtAlarmSearch`, **Insert → Gallery → Vertical** for `galAlarms`, and **Insert → Forms → Display** for `frmAlarmView`. Place the gallery to the left and the form to the right.

| Control | Property | Formula / value |
| --- | --- | --- |
| `lblAlarmsTitle` | Text | `"Alarm Monitoring"` |
| `txtAlarmSearch` | HintText (Classic) | `"Search alarm code or name"` |
| `galAlarms` | Items | `Sort(Search('DC Alarms', txtAlarmSearch.Text, 'Alarm Code', 'Alarm Name'), 'Detected At', SortOrder.Descending)` |
| `galAlarms` | OnSelect | `Set(varSelectedAlarm, ThisItem)` |
| `frmAlarmView` | DataSource | `'DC Alarms'` |
| `frmAlarmView` | Item | `varSelectedAlarm` |

For the gallery template, show **Alarm Name** as the title, **Alarm Code** as the subtitle, and **Alarm Severity** and **Alarm Status** as additional labels using `Text(ThisItem.'Alarm Severity')` and `Text(ThisItem.'Alarm Status')`. Set nested template labels to `Select(Parent)` where necessary.

In `frmAlarmView → Edit fields → Add field`, include **Alarm Name**, **Alarm Code**, **Alarm Type**, **Alarm Severity**, **Alarm Status**, **Detection Source**, **Detected At**, **Alarm Details**, **Source Asset**, and **Source Sensor**. Before a selection, the form may be blank; select an alarm in the gallery to populate it.

This Alarm screen is intentionally **read-only**. Alarm acknowledgment, escalation, automated routing and real-time updates will be introduced when those behaviors have been designed and tested.

### S06.08 — Test, save and publish the Canvas App

Use **Preview (Play/F5)** in Power Apps Studio and perform these activities on the seeded fictional data:

| Test | Action | Expected result |
| --- | --- | --- |
| T01 | Open Home | Incident, Alarm and Asset summary labels show counts sourced from the matching Dataverse tables |
| T02 | Select **Open incidents**, search `INC-0002` | The matching Incident appears in the queue |
| T03 | Select the incident | Incident Details opens with its existing Priority, Status and linked records |
| T04 | Select **Edit incident**, change `Incident Status` from **Assigned** to **In Progress**, then save | The app displays a success message; reopen the record and confirm the saved status |
| T05 | Edit the same record again to restore **Assigned** | The training data returns to its original status |
| T06 | Select **Unassigned only** | The incident list shows records with no Assigned Engineer; toggle again to show all |
| T07 | Open Alarms, search `ALM-0001` and select it | The Alarm form shows its existing detail and linked Asset/Sensor |
| T08 | Open **New incident**, confirm the required fields and lookup pickers work; select **Cancel** without submitting | No extra Incident record is created |
| T09 | Run **App checker** (stethoscope icon, where available) | Resolve formula errors, unexpected warnings and control accessibility issues before publishing |

For T04–T05, use the **existing** Incident record rather than creating duplicate seed rows. After testing, select **File → Save** or the current Studio **Save** command, and then **Publish → Publish this version** where available. Return to **Solutions → SunnyVerse Data Center Operations 360 → Apps** (or **Objects**) and confirm **DC Operations Command Center** is listed. Reopen it to verify the saved version displays the five screens.

If the app reports a missing data source or permission error, confirm its Dataverse connections and the signed-in user's actual privileges before proceeding. **Visibility of a screen or button is not Dataverse security.** Sharing the app with another person requires authorization, appropriate licensing and access to the underlying Dataverse tables. Do not share the fictional operational dashboard with arbitrary institution users.

### Finish Part 06

You should now have **one working Canvas App** inside the existing solution, containing **five screens** for summary KPIs, Incident browsing, Incident details, Incident creation/editing and Alarm browsing. The incident save form should persist changes to Dataverse; searches, lookups, navigation, cancellation and refresh should work. The original Alarm, Incident and Asset tables remain the data sources, with no duplicate tables or new CSV files.

The command center is ready for later notification, assignment and escalation automations. It remains a fictional educational interface and does not control physical equipment.

## Microsoft Learn references

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

*All organizations, facilities, staff, and operational scenarios in this learning project are fictional. Do not use this guide to control live data center infrastructure.*
