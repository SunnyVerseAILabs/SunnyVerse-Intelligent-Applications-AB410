# Data Center Operations 360 — Step-by-Step Build Guide

**SunnyVerse AI Labs · Independent learner project**  
**Fictional enterprise:** SunnyVerse Renewable Group  
**Published learning part:** Part 00 — Environment and Solution Foundation  
**Updated:** November 1, 2026

[Project home](./README.md) · [Practice data library](./data/README.md)

> **Scope:** Create a fresh learning solution in an authorized Power Platform environment. This part does **not** require Dataverse tables, employee records, real infrastructure data, or bulk imports. Work with fictional information only.

## How to use this guide

Work through the numbered activities in order. Do not assume that a successful Save action is proof that the component works; reopen it and check the actual properties. Screens and menus can differ across Power Apps designer versions.

Each activity follows the same format: **Purpose → Navigation → Exact configuration → Save → Verification → Troubleshooting**. Component and schema names created by Microsoft may include your actual publisher prefix; verify them rather than copying an unconfirmed prefix.

## Part 00 — Prepare the environment and create the solution

### S00.01 — Open the Power Apps maker portal

**Purpose:** Select a workspace where you are allowed to build custom components.

1. In a web browser, open [Power Apps](https://make.powerapps.com).
2. Sign in using a Microsoft account permitted to create Power Platform applications. A school or work account is suitable only when its organization's policy permits the exercise.
3. Find **Environment** near the top of the maker portal and open the environment selector.
4. Choose an approved personal learning/development environment. Do not select a shared institution-wide environment merely because it appears in the list.
5. From the left navigation, select **Solutions**. If you cannot see it, select **More → Solutions**.
6. Confirm that the Solutions list opens and **New solution** is available.

**Verify:** The intended environment is selected and the Solutions page is accessible.

**Troubleshoot:** If you cannot create solutions, check that you are in the intended environment and have maker permissions. Ask the administrator for an authorized development environment if necessary. Do not bypass tenant restrictions.

**Security:** Record environment-specific identifiers privately, not in public screenshots or Markdown files.

### S00.02 — Check for naming conflicts before creation

**Purpose:** Avoid accidentally modifying someone else's components or creating duplicate learning objects.

1. On **Solutions**, search for **SunnyVerse Data Center Operations 360**.
2. If a solution with this name already exists, stop this *fresh-build* exercise until the intended environment is clean or a separate authorized environment is available.
3. If the project solution does not exist, proceed to **S00.03**.
4. Do not delete any unrelated solutions, including the university's managed applications or training modules.

**Verify:** You have a permitted environment where the new solution name is available.

### S00.03 — Create the solution publisher

**Purpose:** Use a consistent customization prefix for tables, columns, choices, apps, and related components.

1. In **Solutions**, select **New solution**.
2. In the solution panel, locate **Publisher**.
3. Select **New publisher** or the equivalent publisher-creation command.
4. Configure these exact values:

| Field | Value |
| --- | --- |
| Display name | SunnyVerse Renewable Learning Publisher |
| Name | SunnyVerseRenewableLearningPublisher |
| Description | Publisher for the fictional SunnyVerse Renewable Group educational solution. |
| Customization prefix | svrg |
| Choice value prefix | Keep the system-generated numeric value |

5. Inspect the full **Name** and customization prefix in the publisher dialog. The interface may derive the unique name automatically.
6. Select **Save**.
7. Return to the solution panel and choose **SunnyVerse Renewable Learning Publisher**.

**Verify:** The publisher is available in the selector. Confirm the actual prefix is `svrg` before creating any custom Dataverse components.

**Troubleshoot:** If your environment prevents publisher creation, do not substitute a random prefix. Obtain permission or use an approved publisher, documenting its actual prefix before proceeding.

### S00.04 — Create the Power Platform solution

**Purpose:** Group the custom application components for maintainable solution development.

1. Stay in the **New solution** panel, or reopen it from **Solutions → New solution**.
2. Enter:

| Field | Value |
| --- | --- |
| Display name | SunnyVerse Data Center Operations 360 |
| Name / unique name | SunnyVerseDataCenterOperations360 |
| Publisher | SunnyVerse Renewable Learning Publisher |
| Version | 1.0.0.0 |
| Description | Fictional data center operations learning solution built with Microsoft Power Platform. |

3. Review all values **before** saving, particularly the unique name and publisher.
4. Select **Create** or **Save**, according to the interface.
5. From the Solutions list, open **SunnyVerse Data Center Operations 360**.
6. Open its **Overview** or **Properties** section, if available.
7. Inspect the actual publisher, solution version, unique name, and managed/unmanaged state.
8. Open **Objects → All**.

**Verify:** The solution opens. Its publisher and version match the configuration above. In a newly created unmanaged solution, no project-specific tables or apps should be present.

**Troubleshoot:** If the project title already exists, do not create a duplicate with a suffix. Verify the selected environment and complete the naming-conflict check in S00.02.

### S00.05 — Check Dataverse table-creation access without adding project data

**Purpose:** Determine whether the learning environment permits custom Dataverse components.

1. Open the new solution and locate **New → Table**.
2. Confirm that the table creation experience can be opened.
3. **Do not create a table yet.** Close the creation panel without saving.
4. Record locally whether the command was available and whether licensing or permission warnings appeared.

**Verify:** The table designer is reachable, or a specific permission/license limitation is documented.

**Troubleshoot:** The maker portal opening does not prove full Dataverse rights or app runtime licensing. Do not begin an import before those rights are understood.

### S00.06 — Optional: Test Outlook and Teams self-notifications

**Purpose:** Check two specific connectors using only your own permitted test accounts. This step is optional and is **not** a multi-user approval test.

1. Open [Power Automate](https://make.powerautomate.com) using the authorized environment.
2. Choose **Create → Instant cloud flow** or **My flows → New flow → Instant cloud flow**, depending on the page.
3. Name the flow **DC00_Connector_Readiness_Test** and choose **Manually trigger a flow**.
4. Add **Office 365 Outlook → Send an email (V2)**.
5. Configure **To** = your own authorized test mailbox; **Subject** = `[TEST] DC360 — Outlook connector`; **Body** = `This is a fictional Power Platform learning project notification test.`
6. Add a parallel branch from the manual trigger, if the designer offers the command.
7. In the other branch, choose **Microsoft Teams → Post a message to myself**.
8. Set **Content type** to Text if requested. Set **Content** = `[TEST] DC360 — Teams connector`.
9. Select **Save → Test → Manually → Run flow**.
10. Open the flow's run history. Check each action independently, then confirm the Outlook message and Teams self-message were received.

**Verify:** Report the two outcomes separately: **Outlook passed/failed/not tested** and **Teams passed/failed/not tested**.

**Troubleshoot:** If parallel branches aren't available in your designer, test the connectors in separate flows. Do not send messages to arbitrary university users or Teams channels. Administrator policies and connector entitlements may differ.

**Important:** A self-message proves only the tested action worked for your identity. It is not evidence of independently authenticated fictional approvers or role-based security.

### S00.07 — Complete the Part 00 checkpoint

Before beginning the next published part, confirm:

- [ ] An authorized development environment is selected.
- [ ] No previous project solution with the same identity conflicts with the fresh exercise.
- [ ] Publisher display name and actual customization prefix are confirmed.
- [ ] The solution is created and can be reopened.
- [ ] Solution version and unique name have been checked.
- [ ] Dataverse table creation is accessible or the limitation is documented.
- [ ] Any optional Outlook and Teams results are recorded accurately.
- [ ] No real user data, secrets, or environment identifiers have been published.

**End of Part 00.** The next lesson will add the first Dataverse reference-data table only after these prerequisites are completed.

## Microsoft Learn references

- [Create a solution](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-solution)
- [Create and edit Dataverse tables](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entities-portal)
- [Power Automate — Turn off or delete a flow](https://learn.microsoft.com/en-us/power-automate/disable-flow)

The learning company and all future project records are fictional. Do not use this project to operate real critical infrastructure.
