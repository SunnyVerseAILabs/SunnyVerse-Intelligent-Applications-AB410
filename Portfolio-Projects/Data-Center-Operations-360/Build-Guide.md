# Data Center Operations 360 — Build-Along Guide

**SunnyVerse AI Labs | Independent Power Platform learning project**  
**Fictional organization:** SunnyVerse Renewable Group  
**Published:** Parts 00–01 — Solution Foundation and Department Master

[Project home](./README.md) · [Practice data](./data/README.md)

Welcome to Data Center Operations 360. In this project, you will build a fictional data center operations solution using Microsoft Power Platform. The work is completed in an environment where you have permission to develop, and all practice records are fictional.

Part 00 prepares the solution that holds the project components. Part 01 creates a Dataverse department table and adds six fictional operating departments. You can complete the lessons using your own authorized learning environment.

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

## Microsoft Learn references

- [Create a Power Platform solution](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-solution)
- [Create and edit Dataverse tables](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entities-portal)
- [Create and edit Dataverse columns](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-field-portal)
- [Dataverse table types and ownership](https://learn.microsoft.com/en-us/powerapps/maker/data-platform/types-of-entities)

*All organizations, facilities, staff, and operational scenarios in this learning project are fictional. Do not use this guide to control live data center infrastructure.*
