# Dataverse Tables, Relationships & Data Imports | AB-410 M04

**SunnyVerse Intelligent Applications · Twinkle & Celestyn — Design & Troubleshooting Lab**  
**▶️ [Watch the Module 4 podcast](https://youtu.be/eAd0rOf68Ms)** · Approximate runtime: **1:07:38** · Learning path: **Dataverse foundations**

## How to follow the podcast

1. Start the video from the beginning. The chapter links below take you to relevant moments.
2. When you reach **⏸️ Pause & build**, pause YouTube and perform the listed steps in your own permitted Power Apps learning environment.
3. Complete the **✅ Check** before continuing. If your interface or permissions differ, read the troubleshooting note rather than guessing.
4. Use **▶️ Resume** to return to the next part of the video. **👀 Watch & understand** requires no action.

**Practice boundary:** Work with invented SunnyVerse data in a development environment with Dataverse. Do not change a production tenant, security settings, SharePoint site, or auditing configuration without authorization. Some examples depend on an existing approved solution, licensed features, SharePoint permissions, or an administrator. A narrated example is not proof of what exists in your environment.

**What you will build:** A Wind Supplier table and sample record; a governed Service Category choice; a supplier view and main form; a supplier import; a Wind Service Appointment table with Assigned Supplier and Backup Supplier lookups; and a Wind Service Proposal table with a formula, business rule and data import. Auditing is an optional administrator-approved configuration.

## Podcast chapter map

| Time | Podcast topic | Follow-along type |
|---|---|---|
| [00:00](https://youtu.be/eAd0rOf68Ms?t=0) | Why fragmented supplier spreadsheets cause problems | 👀 Watch |
| [04:00](https://youtu.be/eAd0rOf68Ms?t=240) | Tables, rows, columns, GUIDs and table characteristics | 👀 Watch |
| [11:14](https://youtu.be/eAd0rOf68Ms?t=674) | Table type and ownership decisions | 👀 Watch |
| [14:28](https://youtu.be/eAd0rOf68Ms?t=868) | Solution publisher and prefix | ✅ Check prerequisite |
| [17:04](https://youtu.be/eAd0rOf68Ms?t=1024) | Dual-write versus virtual tables | 👀 Watch |
| [20:26](https://youtu.be/eAd0rOf68Ms?t=1226) | Environment and solution selection | ⏸️ Pause & check |
| [22:19](https://youtu.be/eAd0rOf68Ms?t=1339) | Create Wind Supplier | ⏸️ Pause & build |
| [24:17](https://youtu.be/eAd0rOf68Ms?t=1457) | Create Service Category global choice | ⏸️ Pause & build |
| [26:49](https://youtu.be/eAd0rOf68Ms?t=1609) | Add Service Region and Last Service Date | ⏸️ Pause & build |
| [27:42](https://youtu.be/eAd0rOf68Ms?t=1662) | Configure view and main form | ⏸️ Pause & build |
| [29:28](https://youtu.be/eAd0rOf68Ms?t=1768) | Enter a manual Wind Partner A record | ⏸️ Pause & build |
| [30:30](https://youtu.be/eAd0rOf68Ms?t=1830) | Understand the SharePoint import source | ✅ Check prerequisite |
| [32:02](https://youtu.be/eAd0rOf68Ms?t=1922) | Avoid duplicate supplier records | ⏸️ Pause & check |
| [33:02](https://youtu.be/eAd0rOf68Ms?t=1982) | Connect SharePoint list in Power Query | ⏸️ Pause & build |
| [34:07](https://youtu.be/eAd0rOf68Ms?t=2047) | Choose source columns | ⏸️ Pause & check |
| [34:54](https://youtu.be/eAd0rOf68Ms?t=2094) | Load to existing table and map columns | ⏸️ Pause & build |
| [36:44](https://youtu.be/eAd0rOf68Ms?t=2204) | Troubleshoot rejected import rows | ✅ Verify |
| [39:17](https://youtu.be/eAd0rOf68Ms?t=2357) | Understand lookups and one-to-many | 👀 Watch |
| [41:20](https://youtu.be/eAd0rOf68Ms?t=2480) | Create Wind Service Appointment | ⏸️ Pause & build |
| [42:21](https://youtu.be/eAd0rOf68Ms?t=2541) | Add Assigned Supplier lookup | ⏸️ Pause & build |
| [45:15](https://youtu.be/eAd0rOf68Ms?t=2715) | Add Backup Supplier relationship | ⏸️ Pause & build |
| [49:40](https://youtu.be/eAd0rOf68Ms?t=2980) | Wind Service Proposal scenario | 👀 Watch |
| [50:08](https://youtu.be/eAd0rOf68Ms?t=3008) | Create proposal table, stage and input columns | ⏸️ Pause & build |
| [52:13](https://youtu.be/eAd0rOf68Ms?t=3133) | Add Weighted Proposal Value formula | ⏸️ Pause & build |
| [54:13](https://youtu.be/eAd0rOf68Ms?t=3253) | Configure and activate business rule | ⏸️ Pause & build |
| [56:08](https://youtu.be/eAd0rOf68Ms?t=3368) | Prepare two Excel proposal rows | ⏸️ Pause & prepare |
| [57:10](https://youtu.be/eAd0rOf68Ms?t=3430) | Import proposals with Power Query | ⏸️ Pause & build |
| [59:33](https://youtu.be/eAd0rOf68Ms?t=3573) | Understand auditing | 👀 Watch |
| [60:32](https://youtu.be/eAd0rOf68Ms?t=3632) | Environment → table → column audit settings | Optional admin-approved steps |
| [64:12](https://youtu.be/eAd0rOf68Ms?t=3852) | Final system recap | 👀 Watch |

## 1. Prepare the environment and publisher

**⏸️ Pause at [20:26 — Begin the maker workflow](https://youtu.be/eAd0rOf68Ms?t=1226).**

1. Open [Power Apps](https://make.powerapps.com/) and sign in.
2. Confirm you selected your permitted **development environment** with a Dataverse database.
3. Confirm you have permission to create or modify tables.
4. If you have an approved SunnyVerse learning **solution**, open it before creating the tables and inspect its publisher. Otherwise use the solution or table-creation approach approved for your environment.

**Publisher values discussed in the episode:**

| Property | Value |
|---|---|
| Publisher display name | `SunnyVerse Renewable Learning Publisher` |
| Publisher unique name | `SunnyVerseRenewableLearningPublisher` |
| Customization prefix | `svrg` |
| Example resulting table schema name | `svrg_WindSupplier` |

**✅ Check:** The `svrg` prefix applies **only if that publisher is actually configured and selected**. Do not force a prefix manually, claim it already exists, or assume the current tenant has the same solution. If your publisher differs, keep the real generated schema name.

**▶️ [Resume at 22:19](https://youtu.be/eAd0rOf68Ms?t=1339).**

## 2. Create the Wind Supplier table

**⏸️ Pause at [22:19 — Wind Supplier table](https://youtu.be/eAd0rOf68Ms?t=1339).**

1. Inside the selected solution, use **New → Table**; or open **Tables** (use **More** if necessary), then **New table**. Choose **Set advanced properties** or the detailed configuration route available in your environment.
2. Fill in the table properties exactly as discussed:

| Setting | Enter or verify |
|---|---|
| Display name | `Wind Supplier` |
| Plural | `Wind Suppliers` |
| Primary column display name | `Supplier Name` |
| Table type | `Standard` |
| Ownership | `User or team` |
| Schema name | Inspect the *automatically generated* name; `svrg_WindSupplier` only with the configured `svrg` publisher |

3. Save the table and reopen its design page.

**✅ Check:** The custom table exists, and its primary column reads **Supplier Name**. Do not confuse this display name with the system-generated GUID or the schema name.

**▶️ [Resume at 24:17](https://youtu.be/eAd0rOf68Ms?t=1457).**

## 3. Add Service Category as a reusable Choice

**⏸️ Pause at [24:17 — Service Category](https://youtu.be/eAd0rOf68Ms?t=1457).**

1. Open **Wind Supplier → Columns** (under **Schema**, or **New → Column** depending on your designer).
2. Create **Service Category** with data type **Choice**.
3. Under **Sync this choice with**, choose **New choice** if that control is available.
4. Enter the choice-set name **Wind Service Category** and add these **exact labels**:

```text
Rotor Services
Electrical Services
```

5. Save the reusable choice, select it for **Service Category**, and save the column.

**✅ Check:** Your choice column offers these two labels. Text labels and stored numeric option values are different; imports must map to valid choices. If your current designer supports a different creation route, verify the outcome instead of inventing menu names.

**▶️ [Resume at 26:49](https://youtu.be/eAd0rOf68Ms?t=1609).**

## 4. Add two more supplier columns

**⏸️ Pause at [26:49 — Supplier details](https://youtu.be/eAd0rOf68Ms?t=1609).**

Create each column in **Wind Supplier → Columns**:

| Display name | Data type | Format / example |
|---|---|---|
| `Service Region` | Single line of text | Short text, such as `West` |
| `Last Service Date` | Date and time | Choose a **date-only** format for calendar dates |

Save each column.

**✅ Check:** The three added columns are **Service Category**, **Service Region** and **Last Service Date**. A column does not automatically appear on an app's form or view.

**▶️ [Resume at 27:42](https://youtu.be/eAd0rOf68Ms?t=1662).**

## 5. Add the fields to a view and a form

**⏸️ Pause at [27:42 — Views](https://youtu.be/eAd0rOf68Ms?t=1662).**

1. In Wind Supplier, open **Data experiences → Views** (or **Views** in the current interface).
2. Edit the active-record view, usually **Active Wind Suppliers**.
3. Add the three new columns and arrange them: **Supplier Name → Service Category → Service Region → Last Service Date**.
4. Remove an unneeded default column such as **Created On** only if your designer allows and the view still makes sense.
5. **Save and publish** the view.

When the video reaches **[28:35 — Forms](https://youtu.be/eAd0rOf68Ms?t=1715)**:

6. Open **Data experiences → Forms**, select the **Main** form and edit it.
7. Add **Service Category**, **Service Region** and **Last Service Date** to its general section.
8. **Save and publish** the form.

**✅ Check:** The fields are visible in the intended view and form. **Hiding a field on a form does not secure its data.**

**▶️ [Resume at 29:28](https://youtu.be/eAd0rOf68Ms?t=1768).**

## 6. Create one manual supplier record

**⏸️ Pause at [29:28 — Test row](https://youtu.be/eAd0rOf68Ms?t=1768).**

In **Wind Supplier → Data**, create a new row using the values spoken in the episode:

| Field | Value |
|---|---|
| Supplier Name | `Wind Partner A — Rotor Services` |
| Service Category | `Rotor Services` |
| Service Region | `West` |
| Last Service Date | Leave blank |

Save the record. **✅ Check:** It appears with a generated Dataverse row identifier. The category is selected from a list, not entered as arbitrary text.

**Important before importing:** The next SharePoint example also includes **Wind Partner A — Rotor Services**. To avoid a duplicate, either remove this *practice-only* row before importing or use a clearly nonoverlapping practice dataset. Delete only your own test record.

**▶️ [Resume at 30:30](https://youtu.be/eAd0rOf68Ms?t=1830).**

## 7. Check the SharePoint import prerequisite

**👀 Watch [30:30 — SharePoint data source](https://youtu.be/eAd0rOf68Ms?t=1830).**

The lesson describes an existing SharePoint list named **Wind Supplier Intake**. It does **not** provide a guided list-creation exercise. To perform the following import, you need a permitted SharePoint site and a list with these columns:

| SharePoint source column | Data type | Destination in Wind Supplier |
|---|---|---|
| `Title` | Built-in text | `Supplier Name` |
| `ServiceCategory` | Text | `Service Category` (Choice) |
| `ServiceRegion` | Text | `Service Region` |
| `LastServiceDate` | Date | `Last Service Date` |

**Named records in the episode:** `Wind Partner A — Rotor Services` and `Wind Partner B — Electrical Services`. Category and region values such as **Rotor Services / West** and **Electrical Services / Central** are suitable fictional preparation values, but the podcast does not dictate a complete, field-by-field SharePoint dataset. Do not treat these suggested preparation values as a verbatim spoken table.

If you do not have access to such a list, **skip the import**, keep watching, and continue with the Dataverse relationship exercise using your practice supplier record. An [optional source-list CSV template](resources/M04_Wind_Supplier_Intake_Optional_Template.csv) is provided as a preparation reference, not a substitute for a real SharePoint list connection.

**▶️ [Resume at 32:02](https://youtu.be/eAd0rOf68Ms?t=1922).**

## 8. Import supplier rows from SharePoint with Power Query

**⏸️ Pause at [32:02 — Duplicate check](https://youtu.be/eAd0rOf68Ms?t=1922).** Make sure your manual practice row will not be duplicated.

**⏸️ At [33:02 — Import data](https://youtu.be/eAd0rOf68Ms?t=1982):**

1. From your SharePoint site, copy the **site URL**, stopping at the site name. Do not paste a `/Lists/...` page URL or a filtered-view query string.
2. Open **Power Apps → Tables → Wind Supplier → Import → Import data**.
3. Select the **SharePoint list** connector, enter your permitted site URL, authenticate and choose **Wind Supplier Intake**.
4. At **[34:07 — Choose columns](https://youtu.be/eAd0rOf68Ms?t=2047)**, keep only **Title**, **ServiceCategory**, **ServiceRegion** and **LastServiceDate**. Use the **Applied steps** pane to correct any accidental transformation.
5. At **[34:54 — Map columns](https://youtu.be/eAd0rOf68Ms?t=2094)**, select **Load to existing table** → **Wind Supplier**. Verify all four destination mappings:

| Source | Destination |
|---|---|
| `Title` | `Supplier Name` |
| `ServiceCategory` | `Service Category` |
| `ServiceRegion` | `Service Region` |
| `LastServiceDate` | `Last Service Date` |

6. Check the Choice mapping and Power Query warnings. Choice labels must resolve to the accepted Dataverse options or their correct underlying values; don't assume free-text conversion succeeds automatically.
7. When the destination mapping is sound, choose **Refresh manually → Publish** through the supported flow. Inspect the import outcome and refresh the Wind Supplier table.

**✅ Check:** Expected rows appear without duplicates, and no important input field is unmapped. An import failure is not success: at **[36:44 — Troubleshooting](https://youtu.be/eAd0rOf68Ms?t=2204)** check site URL, list selection, credentials, query filters, missing Title values and invalid choice values. Correct the source/transformation; don't weaken security or requirements to make an import pass.

**▶️ [Resume at 39:17](https://youtu.be/eAd0rOf68Ms?t=2357).**

## 9. Create Wind Service Appointment and its first supplier lookup

**👀 Watch [39:17 — Why lookups matter](https://youtu.be/eAd0rOf68Ms?t=2357).** One supplier can have multiple appointments; from the appointment's perspective many appointments may refer to one supplier.

**⏸️ Pause at [41:20 — Create appointment table](https://youtu.be/eAd0rOf68Ms?t=2480).**

1. In the same approved environment/solution, create a new **Standard** table with:

| Setting | Value |
|---|---|
| Display name | `Wind Service Appointment` |
| Plural | `Wind Service Appointments` |
| Primary column | `Appointment Name` |
| Description (illustrative) | `Scheduled wind-service visits` |

2. Review ownership and save.
3. Add **Appointment Priority** as **Choice**. Create or select a choice set for these exact labels: `Routine`, `Scheduled`, `Urgent`. Save.

**⏸️ At [42:21 — Assigned Supplier lookup](https://youtu.be/eAd0rOf68Ms?t=2541):**

4. Create a new column **Assigned Supplier** with data type **Lookup**.
5. Set **Related table** to **Wind Supplier**, then save.
6. Inspect the resulting **Many-to-one** relationship on Appointment and **One-to-many** relationship on Supplier.

**✅ Check:** The lookup points to the actual Wind Supplier table, and its selector can find **Wind Partner A — Rotor Services** if the record exists and your user has access. If missing, check the imported record, permission and related table—not name spelling alone.

**▶️ [Resume at 44:37](https://youtu.be/eAd0rOf68Ms?t=2677).**

## 10. Add a distinct Backup Supplier relationship

**⏸️ Pause at [45:15 — Backup Supplier](https://youtu.be/eAd0rOf68Ms?t=2715).**

1. Open **Wind Supplier → Schema → Relationships**.
2. Choose **New relationship → One-to-many**.
3. For the related many-side table, choose **Wind Service Appointment**.
4. Name the generated lookup **Backup Supplier**, where the editor offers the lookup display-name setting.
5. Save and return to Wind Service Appointment to inspect its columns and relationships.

**✅ Check:** Both **Assigned Supplier** and **Backup Supplier** exist as **separate lookups**, each referencing Wind Supplier. Do not create a redundant Backup Supplier table, and do not overwrite the first lookup. You are not being asked to build a many-to-many relationship here.

**▶️ [Resume at 47:00](https://youtu.be/eAd0rOf68Ms?t=2820)** for the transition to Dataverse business logic.

## 11. Create Wind Service Proposal and its input columns

**👀 Watch [49:40 — Proposal scenario](https://youtu.be/eAd0rOf68Ms?t=2980).** These amounts are fictional learning numbers, not quotes or authorizations.

**⏸️ Pause at [50:08 — Proposal table](https://youtu.be/eAd0rOf68Ms?t=3008).**

1. Create a Standard table named **Wind Service Proposal** (plural **Wind Service Proposals**) and a primary text column **Proposal Name**. Review ownership and save.
2. Add **Proposal Stage** as **Choice**, with requirement **Business required**.
3. Create reusable choice set **Wind Proposal Stage**, with exact labels:

```text
Received
Under Review
Accepted
Declined
```

4. If supported, set **Received** as the default value. Save the choice and Proposal Stage column.
5. Add **Proposed Cost** as **Currency**.
6. Add **Approval Likelihood** as **Number → Whole number**. It represents a percentage from **0 to 100**, where `60` means 60 percent; check or configure range properties where available. Do not assume that the bounds are enforced until configured.

**✅ Check:** The three inputs are **Proposal Stage**, **Proposed Cost** and **Approval Likelihood** with the correct types. Proposal Stage is a label, not an approval workflow.

**▶️ [Resume at 52:13](https://youtu.be/eAd0rOf68Ms?t=3133).**

## 12. Add the exact Weighted Proposal Value formula

**⏸️ Pause at [52:13 — Formula column](https://youtu.be/eAd0rOf68Ms?t=3133).**

1. In Wind Service Proposal, create a column **Weighted Proposal Value** with data type **Formula**.
2. Enter the Power Fx expression dictated by Celestyn, with mathematical symbols formatted for pasting:

```powerfx
Decimal('Proposed Cost') * ('Approval Likelihood' / 100)
```

3. Confirm that your editor recognizes both existing columns; review the resulting numeric type and save.

**✅ Check:** With Proposed Cost **10000** and Approval Likelihood **60**, the result is **6000**. This is a calculated numeric illustration, not an approved monetary value. **Do not import or manually enter the formula's output**—only its input values.

**▶️ [Resume at 54:13](https://youtu.be/eAd0rOf68Ms?t=3253).**

## 13. Require Approval Likelihood only when cost exists

**⏸️ Pause at [54:13 — Business rule](https://youtu.be/eAd0rOf68Ms?t=3253).**

1. In Wind Service Proposal, open **Customizations → Business rules → New business rule**.
2. Select the condition and set **Field:** `Proposed Cost`; **Operator:** `Contains data`. Apply.
3. From **Components**, drag **Set Business Required** onto the **true** branch.
4. Set **Field:** `Approval Likelihood`; **Status:** `Business Required`. Apply.
5. Name the rule **Require Likelihood When Cost Exists**, then **Save**.
6. **Activate** the saved rule and confirm it is active.

**✅ Check:** When a cost is populated, the likelihood should be required in applicable client contexts. The false branch is not the same. **Save is not Activate**; the rule's effectiveness also depends on scope and client behavior. Do not claim platform-wide enforcement without testing the intended app.

**▶️ [Resume at 56:08](https://youtu.be/eAd0rOf68Ms?t=3368).**

## 14. Prepare the two Excel proposal records spoken in the podcast

**⏸️ Pause at [56:08 — Excel source data](https://youtu.be/eAd0rOf68Ms?t=3368).**

Create an Excel table with **these four headings**, using precisely the two records stated in the narration:

| Proposal Name | Proposal Stage | Proposed Cost | Approval Likelihood |
|---|---|---:|---:|
| Rotor Inspection Quote | Received | 10000 | 60 |
| Electrical Diagnostic Review | Under Review | 4500 | 40 |

Save the workbook with a descriptive name such as **Wind Service Proposals.xlsx**. A ready-to-use Excel workbook is included with the downloadable companion package. For GitHub, [download the two-row CSV](resources/M04_Wind_Service_Proposals.csv), open it in Excel, and save it as `.xlsx` if required by your importer.

**✅ Check:** There is **no** `Weighted Proposal Value` column in the source file. The podcast states these two rows; it does not dictate a third proposal record. All amounts are imaginary.

**▶️ [Resume at 57:10](https://youtu.be/eAd0rOf68Ms?t=3430).**

## 15. Import the Excel proposals into Dataverse

**⏸️ Pause at [57:10 — Import proposal data](https://youtu.be/eAd0rOf68Ms?t=3430).**

1. In **Power Apps → Tables → Wind Service Proposal**, choose **Import → Import data**.
2. Connect to your local Excel workbook using a connector available to your environment; select the appropriate sheet/table and review the four source columns.
3. In Power Query, check the input data types, especially Currency-compatible **Proposed Cost** and Whole number **Approval Likelihood**.
4. Under destination/load settings choose **Load to existing table → Wind Service Proposal** (not a new table).
5. Map **Proposal Name** to the table's primary text column, **Proposal Stage** to its Choice, and the two numbers to their corresponding columns.
6. Continue with **Next → Refresh manually → Publish** as supported by the current importer.
7. Refresh the table and verify the source rows are present. Review any refresh errors and adjust failed mappings.

**✅ Check:** Two proposal rows exist. The computed values should be **6000** for Rotor Inspection Quote and **1800** for Electrical Diagnostic Review if the formula and inputs work as defined. The second number is a calculation from the spoken inputs, not a separately spoken result. Running the same append import twice can create duplicate records; check before rerunning.

**▶️ [Resume at 59:33](https://youtu.be/eAd0rOf68Ms?t=3573).**

## 16. Understand and optionally configure auditing

**👀 Watch [59:33 — Auditing](https://youtu.be/eAd0rOf68Ms?t=3573).** This is not another required project. Auditing records supported data changes; it does **not** mean every record view or every user login is captured in the same history.

**⏸️ Only if your administrator authorizes an audit-settings walkthrough, pause at [60:32 — Three audit levels](https://youtu.be/eAd0rOf68Ms?t=3632):**

1. **Environment:** An authorized administrator enables Dataverse auditing in the **Power Platform admin center** for the selected environment. Verify the current menu location in Microsoft's documentation.
2. **Table:** In Power Apps open **Tables → Wind Supplier → Properties → Advanced options**, locate **Audit changes to its data**, enable and **Save**.
3. **Column:** In **Wind Supplier → Schema → Columns → Service Region → Advanced options**, enable auditing for that column and **Save**, if the current interface and your role permit it.

**✅ Check:** All required higher-level switches must be active for the selected audit settings to take effect. Audit history in an eligible model-driven form is different from other enterprise activity logging; availability, storage and privileges matter. If you lack permissions, **do not attempt to bypass them**—continue watching.

**▶️ [Resume at 64:12](https://youtu.be/eAd0rOf68Ms?t=3852)** for the module recap.

## Troubleshooting quick reference

| If this happens | Check before retrying |
|---|---|
| Schema prefix isn't `svrg` | Confirm selected solution/publisher. Use your **actual** generated prefix; do not type a misleading one. |
| Tables or controls unavailable | Environment, Dataverse availability, maker role, license, current maker UI. |
| Choice labels don't import | Verify `Rotor Services` / `Electrical Services` and mapping to the correct choice values. |
| Import produces no rows | Site URL, source table, permissions, query steps, required fields, conversion errors, destination mapping. |
| Duplicate Wind Partner A | Remove your own manual test record before importing the same example; check existing rows before reruns. |
| Supplier missing in lookup | Confirm row exists, visibility privileges, and Lookup's Related table is Wind Supplier. |
| Backup Supplier overwrites first relationship | Confirm two distinct lookups and both relationships on the appointment table. |
| Formula errors | Verify column display names, quote syntax, type conversion, and Decimal support in your editor. |
| Business rule not working | Check true branch, field, action, Save **and** Activate, scope and form context. |
| Auditing appears inactive | Environment auditing, table/column settings, appropriate permissions, and processing delay. |

**Module completion check:** You can explain why Dataverse has table metadata, why a GUID/lookup is safer than repeated supplier-name text, how Power Query maps outside columns to an existing table, how the formula and conditional rule use stored inputs, and how audit settings depend on the environment.

**Next:** Module 5 covers columns and specialized field behaviors in greater depth.

## References

- [▶️ Module 4 podcast](https://youtu.be/eAd0rOf68Ms)
- [Microsoft Learn — Create tables in Dataverse](https://learn.microsoft.com/en-us/training/modules/get-started-with-powerapps-common-data-service/)
- [Microsoft Learn — Work with formula columns](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/formula-columns)
- [Microsoft Learn — SharePoint list connector](https://learn.microsoft.com/en-us/power-query/connectors/sharepoint-list)
- [Microsoft Learn — Import data with Power Query](https://learn.microsoft.com/en-us/power-query/dataflows/add-data-power-query)
- [SunnyVerse Intelligent Applications course](https://sunnyverse.odoo.com/intelligent-applications)

*© 2026 SunnyVerse AI Labs. Independent learner material; not affiliated with or endorsed by Microsoft. SunnyVerse Renewable Group, its suppliers and all examples are fictional. Product interfaces, permissions and feature availability may change.*