# Data Center Operations 360 — Build-Along Guide

**SunnyVerse AI Labs | Independent Power Platform learning project**  
**Fictional organization:** SunnyVerse Renewable Group  
**Part 00:** Create the learning environment foundation

[Project home](./README.md) · [Practice data](./data/README.md)

Welcome to Data Center Operations 360. In this project, you will build a fictional data center operations solution using Microsoft Power Platform. The work is completed in an environment where you have permission to develop, and all practice records are fictional.

This first lesson prepares the environment, creates a publisher, and sets up the solution that will hold our Dataverse tables, applications, and flows. You will also check whether the Dataverse table designer is available and, if your account permits it, test Outlook and Teams notifications.

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

## Microsoft Learn references

- [Create a Power Platform solution](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-solution)
- [Create and edit Dataverse tables](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entities-portal)

*All organizations, facilities, staff, and operational scenarios in this learning project are fictional. Do not use this guide to control live data center infrastructure.*
