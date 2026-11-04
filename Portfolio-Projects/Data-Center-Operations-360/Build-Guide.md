# Data Center Operations 360 — Build-Along Guide

**SunnyVerse AI Labs | Independent Power Platform learning project**  
**Fictional organization:** SunnyVerse Renewable Group  
**Published:** Parts 00–07 — Solution Foundation, Department Master, Campus and Data Halls, Employee Directory, Asset and Sensor Registry, Alarm and Incident Management, Operations Command Center, Field Engineer Mobile App

[Project home](./README.md) · [Practice data](./data/README.md)

Welcome to Data Center Operations 360. In this project, you will build a fictional data center operations solution using Microsoft Power Platform. The work is completed in an environment where you have permission to develop, and all practice records are fictional.

Part 00 prepares the solution. Parts 01–04 build reference data, Part 05 adds alarms and incidents, Part 06 creates the desktop command center, and Part 07 adds a phone-oriented field inspection app. Follow the lessons in order in an authorized learning environment.

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

First we'll create **DC Field Inspection**, a small Dataverse table for inspection records. Then we'll create the mobile app and enter two sample inspections through its own form. **No CSV import or new Power Automate flow is needed.** We'll use the same deep-navy, teal, amber and light-neutral colors as the command center.

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

To create **Inspection Status**, select **Data type → Choice → View more → Local choice**, add the three labels exactly as shown, and leave its default empty. Repeat for **Inspection Result**, using its four labels. These are two independent **Local Choices**, not new Global Choices. **Follow-up Required** is a Boolean Yes/No column, not a Choice.

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

### S07.04 — Create DC FieldOps and apply its mobile theme

Return to **Solutions → SunnyVerse Data Center Operations 360 → New → App → Canvas app**. Choose **Phone / Portrait** and enter **DC FieldOps** as the app's name. In the editor open **Data → Add data → Microsoft Dataverse** and connect these existing tables:

| Studio data source | Purpose |
| --- | --- |
| `'DC Incidents'` | Browse and update incident records |
| `'DC Assets'` | Select an asset for inspection |
| `'DC Employee Profiles'` | Select a fictional inspector in the form |
| `'DC Field Inspections'` | Create, browse and edit inspection records |

Select **App → Formulas** and enter the same reusable named colors used by the desktop command center:

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

Create the six blank screens in **Tree view**, using **New screen → Blank** and **… → Rename**:

| Screen | Purpose | Controls to add in its later section |
| --- | --- | --- |
| `scrFieldHome` | Mobile landing page | KPIs, navigation, refresh |
| `scrFieldIncidents` | Incident search | Search, unassigned filter, incident gallery |
| `scrFieldIncidentDetail` | Read selected incident | Display form, Edit and Back buttons |
| `scrFieldIncidentEdit` | Update selected incident | Edit form, Save and Cancel |
| `scrFieldInspections` | Inspection list | Search, inspection gallery, New button |
| `scrFieldInspectionEdit` | Create or update inspection | Edit form including attachments, Save and Cancel |

On **each screen**, set **Fill = `clrCanvas`**. Create a rectangle (**Insert → Shapes → Rectangle**) and a text label for its header. Give the rectangle **X = 0, Y = 0, Width = Parent.Width, Height = 72, Fill = `clrPrimary`, BorderThickness = 0**. Add a thin second rectangle with **X = 0, Y = 72, Width = Parent.Width, Height = 3, Fill = `clrAccent`**. Send both rectangles to the back. Set each title label's **X = 18, Y = 13, Width = Parent.Width - 36, Height = 44, Color = `clrSurface`, Fill = `Color.Transparent`, Size = 20, FontWeight = `FontWeight.Bold`**.

| Screen title label | Text |
| --- | --- |
| `lblFieldHomeTitle` | `"DC FIELDOPS"` |
| `lblFieldIncidentsTitle` | `"FIELD INCIDENTS"` |
| `lblFieldIncidentDetailTitle` | `"INCIDENT DETAILS"` |
| `lblFieldIncidentEditTitle` | `"UPDATE INCIDENT"` |
| `lblFieldInspectionsTitle` | `"EQUIPMENT INSPECTIONS"` |
| `lblFieldInspectionEditTitle` | `If(varNewInspection, "NEW INSPECTION", "EDIT INSPECTION")` |

Use **Classic** Text labels, Buttons, Text inputs, and **Blank vertical** Galleries when available, so the formulas use the classic `Text` property. Add each title to its screen and rename it as above. Set **App → StartScreen = `scrFieldHome`**.

Buttons will use consistent mobile styling: **Fill = `clrSecondary`**, **Color = `clrSurface`**, **Height = 48**, **Size = 16**, **BorderThickness = 0**. Set **HoverFill = `ColorValue("#07515B")`** and **PressedFill = `ColorValue("#06444C")`** for Classic buttons. For **Back** and **Cancel** buttons use **Fill = `clrSurface`**, **Color = `clrPrimary`**, **BorderColor = `clrBorder`**, **BorderThickness = 1**. Use a 12–16 pixel margin between touch controls.

### S07.05 — Build the FieldOps Home screen

Open `scrFieldHome`. Add two large labels for the KPIs and three buttons below them. Rename the controls exactly and set their properties:

| Control | Property | Formula / value |
| --- | --- | --- |
| `lblFieldIncidentCount` | Text | `"INCIDENTS" & Char(10) & Text(CountIf('DC Incidents', true), "0")` |
| `lblFieldInspectionCount` | Text | `"INSPECTIONS" & Char(10) & Text(CountIf('DC Field Inspections', true), "0")` |
| Both KPI labels | Fill / Color / BorderColor / BorderThickness | `clrSurface` / `clrText` / `clrBorder` / `1` |
| Both KPI labels | X / Width / Height / Align | `18` / `Parent.Width - 36` / `90` / `Align.Center` |
| `lblFieldIncidentCount` | Y | `104` |
| `lblFieldInspectionCount` | Y | `212` |
| `btnFieldOpenIncidents` | Text / OnSelect | `"Browse incidents"` / `Navigate(scrFieldIncidents, ScreenTransition.Fade)` |
| `btnFieldOpenInspections` | Text / OnSelect | `"Record inspection"` / `Navigate(scrFieldInspections, ScreenTransition.Fade)` |
| `btnFieldRefresh` | Text / OnSelect | `"Refresh"` / `Refresh('DC Incidents'); Refresh('DC Field Inspections'); Notify("Records refreshed.", NotificationType.Information)` |

Set each button's **X = 18**, **Width = Parent.Width - 36**, and use **Y = 330, 398, and 466**, respectively. The first two buttons use teal; make Refresh white with navy text and a cool-gray border.

With the original practice data, Incidents should initially show approximately **200**, and Inspections should initially show **0**. Dataverse counts can be cached or delegation-limited; the `CountIf` formula is intended to request an exact count in supported Dataverse environments with enhanced delegation enabled. If a count contradicts the table's records, inspect the formula warning rather than replacing the number with a fixed literal.

**Checkpoint 3 — Mobile Home.** The portrait screen shows two readable white KPI cards, three large touch buttons, and a navy header with a thin amber divider. Both Browse incidents and Record inspection navigate to their respective screens.

### S07.06 — Browse and open existing incidents

On `scrFieldIncidents` insert **Classic Text input** `txtFieldIncidentSearch`, **Button** `btnFieldOnlyUnassigned`, **Blank vertical Gallery** `galFieldIncidents` and **Button** `btnFieldIncidentsHome`. Place the search field at the top, the filter button beneath it, and the list below. Keep the Home action visible at the bottom.

| Control or screen | Property | Formula / value |
| --- | --- | --- |
| `txtFieldIncidentSearch` | HintText / Default | `"Search incident code or name"` / `""` |
| `txtFieldIncidentSearch` | X / Y / Width / Height | `18` / `94` / `Parent.Width - 36` / `48` |
| `txtFieldIncidentSearch` | Fill / Color / BorderColor / FocusedBorderColor | `clrSurface` / `clrText` / `clrBorder` / `clrSecondary` |
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
        !varFieldOnlyUnassigned || IsBlank('Assigned Engineer')
    ),
    'Reported At',
    SortOrder.Descending
)
```

Inside the gallery template insert **two labels**, `lblFieldIncidentRowName` and `lblFieldIncidentRowMeta`. Do not use a photo gallery. Give the first **Text = `ThisItem.'Incident Name'`**, **Color = `clrText`**, **Size = 15**; the second **Text = `ThisItem.'Incident Code' & "  ·  " & Text(ThisItem.'Incident Status')`**, **Color = `clrMuted`**, **Size = 12**. Set both **OnSelect = `Select(Parent)`**, **Fill = `Color.Transparent`**, **X = 12** and **Width = Parent.TemplateWidth - 24**. Use **Y = 9** for the first and **Y = 42** for the second. Remove any placeholder image control from the template.

On `scrFieldIncidentDetail` choose **Insert → Forms → Display form** and rename it `frmFieldIncidentView`. Add two buttons, `btnFieldOpenEdit` and `btnFieldDetailBack`. Configure:

| Control | Property | Formula / value |
| --- | --- | --- |
| `frmFieldIncidentView` | DataSource / Item | `'DC Incidents'` / `varFieldIncident` |
| `frmFieldIncidentView` | X / Y / Width / Height | `18` / `96` / `Parent.Width - 36` / `Parent.Height - 194` |
| `frmFieldIncidentView` | Columns / Fill | `1` / `clrSurface` |
| `btnFieldOpenEdit` | Text / OnSelect | `"Update incident"` / `EditForm(frmFieldIncidentEdit); Navigate(scrFieldIncidentEdit, ScreenTransition.Fade)` |
| `btnFieldDetailBack` | Text / OnSelect | `"Back to incidents"` / `Navigate(scrFieldIncidents, ScreenTransition.None)` |

Under **frmFieldIncidentView → Edit fields → Add field**, include **Incident Name**, **Incident Code**, **Priority**, **Incident Status**, **Reported At**, **Incident Description**, **Source Asset**, **Reported By**, **Assigned Engineer**, **Related Alarm** and **Resolution Notes**. Remove any automatically included *system* Status or Status Reason cards from the form; keep the custom **Incident Status**. Set card caption colors to `clrMuted` and displayed values to `clrText`. Use a one-column form so field labels and lookup names remain readable on a phone.

**Checkpoint 4 — Incident navigation.** Search `INC-0002`, select it, and verify the Incident Details form displays the selected existing record. The Back button returns to the incident gallery without creating anything.

### S07.07 — Update an existing incident from the phone

Open `scrFieldIncidentEdit`, choose **Insert → Forms → Edit form**, and rename it `frmFieldIncidentEdit`. This is a **limited update form**, not a new-incident wizard. It changes the operational fields needed for practice without changing the record's originating Asset or reporting employee.

| Control | Property | Formula / value |
| --- | --- | --- |
| `frmFieldIncidentEdit` | DataSource / Item | `'DC Incidents'` / `varFieldIncident` |
| `frmFieldIncidentEdit` | X / Y / Width / Height | `18` / `96` / `Parent.Width - 36` / `Parent.Height - 194` |
| `frmFieldIncidentEdit` | Columns / Fill | `1` / `clrSurface` |
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

Position Save update and Cancel beneath the form; use teal for Save and outlined white for Cancel. For each form-card caption choose **Color = `clrMuted`**. For editable controls use **Fill = `clrSurface`**, **Color = `clrText`** and **BorderColor = `clrBorder`**, where supported. Error labels use `clrDanger`. Leave the generated Combo box's lookup source and any card **DataField / Default / Update** settings unchanged.

**Checkpoint 5 — Update.** Open `INC-0002`, update its **Incident Status** from Assigned to In Progress, save and confirm the status is shown in the read-only details. Change it back to Assigned so the fictional seed data stays consistent. Canceling the form must not save a change.

### S07.08 — Create the inspection list and mobile inspection form

On `scrFieldInspections` insert **Classic Text input** `txtFieldInspectionSearch`, **Blank vertical Gallery** `galFieldInspections`, **Button** `btnFieldNewInspection` and **Button** `btnFieldInspectionsHome`. Use the existing title and theme header.

| Control | Property | Formula / value |
| --- | --- | --- |
| `txtFieldInspectionSearch` | HintText / Default | `"Search inspection code or name"` / `""` |
| `txtFieldInspectionSearch` | X / Y / Width / Height | `18` / `96` / `Parent.Width - 36` / `48` |
| `galFieldInspections` | Items | See formula below |
| `galFieldInspections` | X / Y / Width / Height | `18` / `211` / `Parent.Width - 36` / `Parent.Height - 304` |
| `galFieldInspections` | Fill / TemplateFill | `clrSurface` / `If(ThisItem.IsSelected, clrSelected, clrSurface)` |
| `galFieldInspections` | TemplateSize | `80` |
| `galFieldInspections` | OnSelect | `Set(varFieldSelectedInspection, ThisItem); Set(varNewInspection, false); EditForm(frmFieldInspectionEdit); Navigate(scrFieldInspectionEdit, ScreenTransition.Fade)` |
| `btnFieldNewInspection` | Text / OnSelect | `"New inspection"` / `Set(varNewInspection, true); NewForm(frmFieldInspectionEdit); Navigate(scrFieldInspectionEdit, ScreenTransition.Fade)` |
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

Inside the gallery template add **two labels**: `lblFieldInspectionRowName` (**Text = `ThisItem.'Inspection Name'`**, Color `clrText`, Size 15), and `lblFieldInspectionRowMeta` (**Text = `ThisItem.'Inspection Code' & "  ·  " & Text(ThisItem.'Inspection Status')`**, Color `clrMuted`, Size 12). Set **OnSelect = `Select(Parent)`**, **Fill = `Color.Transparent`**, **X = 12** and **Width = Parent.TemplateWidth - 24** for both. Put New inspection above the gallery and Home below it.

Next open `scrFieldInspectionEdit`, insert **Forms → Edit form**, rename it `frmFieldInspectionEdit`, then add the **Save inspection** and **Cancel** buttons below the form.

| Control | Property | Formula / value |
| --- | --- | --- |
| `frmFieldInspectionEdit` | DataSource | `'DC Field Inspections'` |
| `frmFieldInspectionEdit` | Item | `varFieldSelectedInspection` |
| `frmFieldInspectionEdit` | X / Y / Width / Height | `18` / `94` / `Parent.Width - 36` / `Parent.Height - 198` |
| `frmFieldInspectionEdit` | Columns / Fill | `1` / `clrSurface` |
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

**Evidence upload:** The table's **Enable attachments** setting allows a Dataverse form to offer an **Attachments** field. Choose **Edit fields → Add field → Attachments**, if shown. Keep the generated attachment card and its data binding unchanged. The file is not stored just because it was selected; **SubmitForm** saves the record and the staged file together. On Power Apps Mobile, files are normally selected one at a time. Use a **fictional/staged image or non-sensitive sample file**—never a real facility photo. If Attachments isn't available, verify table attachment enablement and refresh the Dataverse connection; do not substitute an unbound Add picture control and assume it saved to Dataverse. The attachment feature may depend on the tenant configuration and permissions.

For the form's existing card captions use **clrMuted** and for supported inputs use **Fill = clrSurface**, **Color = clrText**, **BorderColor = clrBorder**; use **clrDanger** for error labels. Keep **DataField**, **Update**, **Default**, **Required** and attachment control bindings as generated. The single-column form is taller than a phone's display; keep the form scrollable and its Save/Cancel buttons outside its scrollable cards.

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

**Checkpoint 6 — Inspection workflow.** The inspection gallery shows **two** records with distinct codes; opening one shows its saved fields, lookups and evidence where enabled. The form can create and edit inspection records without duplicating the underlying Assets or Employees.

### S07.09 — Test, save and publish DC FieldOps

Use **Preview (Play/F5)** in Power Apps Studio, then test on an authorized phone with **Power Apps Mobile** where available. Browser preview is useful for formulas, but a mobile device is more representative for touch controls and its file picker.

| Test | Action | Expected result |
| --- | --- | --- |
| T01 | Open DC FieldOps | Portrait layout, navy header, amber divider, teal buttons and readable controls |
| T02 | Tap Browse incidents; search `INC-0002` | Existing incident appears |
| T03 | Open its details | Priority, status, asset and reporting employee are visible |
| T04 | Update Incident Status; save; restore original value | The change persists and the form reports success |
| T05 | Open Record inspection | Inspection list opens |
| T06 | Create `INSP-0001` and `INSP-0002` | Both records save, with valid Asset and Inspected By lookups |
| T07 | Add a staged attachment using the inspection form, where available | The saved record retains the attachment |
| T08 | Reopen and edit an inspection, then Cancel | Changes that weren't submitted are discarded |
| T09 | Check **App checker** | No blocking formula errors; examine delegation, form, accessibility and permission warnings |

Do not mistake a fictional **Inspected By** lookup for real user authentication. App visibility and button rules do not replace Dataverse security roles; access to the app and its Dataverse tables must be authorized for each real user.

Select **Save**, then **Publish → Publish this version**. Return to the solution and confirm **DC FieldOps** appears as a second Canvas App alongside **DC Operations Command Center**.

### Finish Part 07

Your solution now contains a **phone-oriented FieldOps Canvas App** and a **DC Field Inspection** Dataverse table with three lookup relationships. The app can browse and update existing fictional incidents, create and edit inspections, record observations and follow-up decisions, and save supporting evidence through a supported Dataverse attachment form. Confirm the two sample inspection records persist after reopening the table and that the previous incident, asset and employee data remain intact.


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
- [Enable attachments on a Dataverse table](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/create-edit-tables)
- [Attachments control in canvas apps](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-attachments)
- [Build phone-sized Canvas Apps](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/app-from-image)

*All organizations, facilities, staff, and operational scenarios in this learning project are fictional. Do not use this guide to control live data center infrastructure.*
