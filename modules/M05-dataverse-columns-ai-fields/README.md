# Dataverse Columns, Prompt Fields & Alternate Keys | AB-410 M05

**SunnyVerse Intelligent Applications · Twinkle & Celestyn — Design & Troubleshooting Lab**  
▶️ **[Watch Module 5 on YouTube](https://youtu.be/_kPVgWgKZ-E)** · **Runtime: 55:29** · **Learning path: Dataverse foundations**

## How to follow this guide

**First complete the Module 5 table setup below, then start the podcast from the beginning.** A **👀 Watch & understand** section explains a concept: keep watching and refer to its short notes. When you see **⏸️ Pause & build**, pause YouTube, perform the steps in your permitted Power Apps learning environment, verify the result, then select the **▶️ Resume** link. **🔎 Optional exploration** means the hosts explain a feature that you can inspect, but it is not a required additional build.

**Module 5 begins with a required setup step:** Create a new Dataverse table named **Battery Inspection** using the instructions below. Learners following this course from Module 1 have not created this table in Modules 1–4. Complete the setup **before starting the Module 5 podcast**. Table creation is a supporting step added to make this guide self-contained; the podcast starts with the table already prepared. Work only in an approved learning environment using fictional data.

**Important:** The early column-type examples explain how fields are configured. The **main guided exercise begins at [49:57](https://youtu.be/_kPVgWgKZ-E?t=2997)**. If you have already created a field while following an earlier example, **verify and reuse it**; do not create a duplicate with the same name. Prompt columns and row summaries may be unavailable depending on environment, licensing and rollout.

## Module 5 setup: Create the Battery Inspection table

**Complete this setup before playing the Module 5 podcast.** This course introduces **Battery Inspection** here for the first time. You will create the empty table now, then follow the podcast to configure its columns and key. It is not carried over from Module 4.

**Why this setup comes first:** Twinkle and Celestyn use an already-prepared table when explaining column settings. The steps below apply the table-creation skills from [Module 4](../M04-dataverse-tables-relationships/README.md) and are **additional learner preparation**, not words or actions attributed to the podcast.

1. Open [Power Apps](https://make.powerapps.com/) and choose your approved **development/learning environment**. Confirm it has Dataverse and you can create custom tables.
2. Open the learning **solution** you used for the Dataverse exercises. Choose **New → Table → Table (advanced properties)**, or the corresponding **New table / Standard table** option in your Power Apps interface, to create a new table in that solution.
3. Use these starter settings:

   | Setting | Enter / select |
   |---|---|
   | **Display name** | `Battery Inspection` |
   | **Plural display name** | `Battery Inspections` |
   | **Table type** | `Standard` |
   | **Primary name column** | Keep the initial `Name` display label for now |
   | **Ownership** | `User or team`, if offered and appropriate for your learning environment |

4. Select **Save / Create**. Open **Battery Inspection → Columns** and confirm the table exists with its original primary-name column.
5. **Stop here.** Do **not** create `Battery Unit Label`, `Finding Description`, `Inspection Ticket Number`, or `Inspection Record Name Key` during setup. You will add or configure those in the podcast's main guided exercise, starting at **[49:57](https://youtu.be/_kPVgWgKZ-E?t=2997)**. Do not rename the primary-name label yet; the video covers that at **[51:21](https://youtu.be/_kPVgWgKZ-E?t=3081)**.

**✅ Verify before starting the video:** The new **Battery Inspection** table appears in your selected development environment and learning solution. Its primary-name display label is still **Name**, and you have not added the columns or alternate key taught later. **▶️ [Start the Module 5 podcast at 00:00](https://youtu.be/_kPVgWgKZ-E?t=0)**. At **[22:18](https://youtu.be/_kPVgWgKZ-E?t=1338)**, return to this table when the hosts discuss the column designer.

**Optional AI examples:** Prompt-column and row-summary demonstrations later in the episode may require additional fields, a fictional inspection record, or feature entitlements. Those are separate from the minimal table setup above; do not invent columns or records as if they had been created in an earlier module.

## Find your place in the podcast

| Video time | Topic | Follow-along mode |
|---|---|---|
| [00:00](https://youtu.be/_kPVgWgKZ-E?t=0) | Why structured inspection fields matter | 👀 Watch |
| [05:40](https://youtu.be/_kPVgWgKZ-E?t=340) | Single-line and longer text fields | 👀 Watch |
| [09:00](https://youtu.be/_kPVgWgKZ-E?t=540) | Decimal, float, whole numbers and currency | 👀 Watch |
| [11:35](https://youtu.be/_kPVgWgKZ-E?t=695) | Dates and time-zone behavior | 👀 Watch |
| [14:10](https://youtu.be/_kPVgWgKZ-E?t=850) | Choice, Choices and Yes/No | 👀 Watch |
| [17:45](https://youtu.be/_kPVgWgKZ-E?t=1065) | Lookup and related Battery Asset records | 👀 Watch |
| [20:00](https://youtu.be/_kPVgWgKZ-E?t=1200) | Formula, Autonumber and Prompt columns | 👀 Watch |
| [22:18](https://youtu.be/_kPVgWgKZ-E?t=1338) | Open correct environment, solution and table | ⏸️ Check |
| [23:49](https://youtu.be/_kPVgWgKZ-E?t=1429) | Column properties | ⏸️ Inspect |
| [24:48](https://youtu.be/_kPVgWgKZ-E?t=1488) | Required levels | 👀 Watch |
| [27:25](https://youtu.be/_kPVgWgKZ-E?t=1645) | Form fill assistance versus Prompt | 👀 Watch |
| [28:08](https://youtu.be/_kPVgWgKZ-E?t=1688) | Temperature, status, finding examples | 🔎 Optional |
| [31:37](https://youtu.be/_kPVgWgKZ-E?t=1897) | Create a Prompt column | 🔎 Optional |
| [32:37](https://youtu.be/_kPVgWgKZ-E?t=1957) | Prompt wording and source fields | 🔎 Optional |
| [34:19](https://youtu.be/_kPVgWgKZ-E?t=2059) | Test generated content against a record | 🔎 Optional |
| [35:32](https://youtu.be/_kPVgWgKZ-E?t=2132) | Remove temporary test restriction | 🔎 Optional |
| [37:37](https://youtu.be/_kPVgWgKZ-E?t=2257) | Execution filters versus test filters | 👀 Watch |
| [39:21](https://youtu.be/_kPVgWgKZ-E?t=2361) | Configure row summary | 🔎 Optional |
| [41:29](https://youtu.be/_kPVgWgKZ-E?t=2489) | Solution-aware row-summary configuration | 👀 Watch |
| [42:30](https://youtu.be/_kPVgWgKZ-E?t=2550) | Primary name versus GUID | 👀 Watch |
| [46:34](https://youtu.be/_kPVgWgKZ-E?t=2794) | Autonumber patterns | 👀 Watch |
| [48:08](https://youtu.be/_kPVgWgKZ-E?t=2888) | Alternate keys and activation | 👀 Watch |
| [49:57](https://youtu.be/_kPVgWgKZ-E?t=2997) | **Guided Dataverse column exercise** | ⏸️ Build |
| [50:28](https://youtu.be/_kPVgWgKZ-E?t=3028) | Add Battery Unit Label | ⏸️ Build |
| [50:52](https://youtu.be/_kPVgWgKZ-E?t=3052) | Add Finding Description | ⏸️ Build |
| [51:21](https://youtu.be/_kPVgWgKZ-E?t=3081) | Rename primary-name label | ⏸️ Build |
| [51:43](https://youtu.be/_kPVgWgKZ-E?t=3103) | Create Inspection Ticket Number | ⏸️ Build |
| [52:12](https://youtu.be/_kPVgWgKZ-E?t=3132) | Create alternate key | ⏸️ Build |
| [52:44](https://youtu.be/_kPVgWgKZ-E?t=3164) | Verify fields and key status | ✅ Check |
| [53:18](https://youtu.be/_kPVgWgKZ-E?t=3198) | Troubleshoot a failed key | ✅ Check |
| [53:50](https://youtu.be/_kPVgWgKZ-E?t=3230) | Recap and next module | ▶️ Watch |

## 1. Understand which column type fits the business fact

**👀 Watch from [05:40](https://youtu.be/_kPVgWgKZ-E?t=340) through [22:18](https://youtu.be/_kPVgWgKZ-E?t=1338).** No need to build yet.

| Business fact | Suitable field | Why |
|---|---|---|
| Short battery-unit label | **Single line of text** | A compact human-readable identifier |
| Inspector observation | **Text area / Multiple lines of text** | A narrative that may need more room |
| Recorded temperature such as `31.2` °C | **Decimal** | A numeric measurement that supports calculation/filtering |
| Count of findings | **Whole number** | An integer, rather than a fractional measurement |
| Approximate scientific quantity | **Float** | Floating-point approximation, with calculation limitations |
| Replacement cost | **Currency** | Amount and currency context |
| Inspection date or timestamp | **Date and time** | Choose appropriate date/time behavior and zone interpretation |
| `Open`, `Review required`, `Closed` | **Choice** | Exactly one approved category |
| Several simultaneous categories | **Choices** (multiple-select) | Multiple values, with downstream feature restrictions |
| A genuine two-state fact | **Yes/No** | Only where a third 'Unknown' value is not required |
| Inspection linked to a separate asset | **Lookup** | A reference to an existing Battery Asset row |
| Deterministic calculation | **Formula** | Read-only expression-driven result |
| Readable generated ticket | **Autonumber** | Formatted sequence, not the system key |
| Stored AI-generated briefing | **Prompt** | AI text requiring human review, not source evidence |

**Remember:** The friendly primary name is not the hidden Dataverse **GUID primary key**. A stable small status list normally belongs in Choice; individual physical assets belong in a related table with Lookup. A human inspection finding is an observation, not proof of repair, approval, or safety.

## 2. Check the environment and column-properties panel

**⏸️ Pause at [22:18](https://youtu.be/_kPVgWgKZ-E?t=1338).**

1. Sign in to [Power Apps](https://make.powerapps.com/) and select the correct **development** environment.
2. Open **Battery Inspection → Columns** from the learning solution where you created the table in [Module 5 setup](#module-5-setup-create-the-battery-inspection-table).
3. Confirm the solution's actual **publisher and prefix** before adding custom components. `SunnyVerse Renewable Learning Publisher` and `svrg` are *conditional educational examples*, not guaranteed values in your tenant.
4. Open **Columns → New column**, or use the table's **+ Add column** route if your designer presents it. Inspect the pane without saving an unnecessary field.

**⏸️ Inspect at [23:49](https://youtu.be/_kPVgWgKZ-E?t=1429):**

| Property | What to check |
|---|---|
| **Display name** | Field label visible to makers and users |
| **Description** | What the stored business value actually means |
| **Data type** | Text, number, Choice, Prompt, etc. |
| **Format / Behavior** | Only where the selected type supports these settings |
| **Required** | Optional; Business recommended; Business required |
| **Searchable** | Availability in applicable search/view experiences—not access control |
| **Maximum character count / Minimum & Maximum** | Limits appropriate to text or numeric type |
| **Allow form fill assistance** | A separate AI form aid, not a Prompt column |

**✅ Check:** You can find the exact table and understand the pane. **Business recommended** does not necessarily block saving. **Business required** should be verified for the actual data-entry route, including integrations; do not mistake an app-level prompt for universal database enforcement.

**▶️ [Resume at 28:08](https://youtu.be/_kPVgWgKZ-E?t=1688).**

## 3. Three ordinary-field examples (optional early practice)

**🔎 At [28:08](https://youtu.be/_kPVgWgKZ-E?t=1688)** the hosts describe three field configurations. If you follow now, use **Battery Inspection** and save each column; otherwise note the settings and continue to the later guided exercise.

| Column | Data type | Specific details spoken in the episode |
|---|---|---|
| **Battery Temperature** | **Decimal number** | Description: `Recorded measurement in degrees Celsius`; one decimal place is an example of suitable precision |
| **Inspection Status** | **Choice** (one selection) | Options: `Open`, `Review required`, `Closed` |
| **Finding Description** | **Multiple lines of text**, or appropriate text-area format | Description should convey that this is authoritative, human-entered evidence of equipment condition |

1. Use **New column**, enter each name and select the specified type.
2. Add the description and any supported constraints. Ensure `Closed` is never decided by an AI summary.
3. **Save** and verify the definition appears in **Columns**. A form or view may require separate changes before end users can see it.

**✅ Check:** If you created **Finding Description** here, reuse it at [50:52](https://youtu.be/_kPVgWgKZ-E?t=3052); **do not add a duplicate**.


### Practice record for the optional AI demonstrations

**Extra learner practice data (not spoken in the episode):** To follow the **Prompt column test at [34:19](https://youtu.be/_kPVgWgKZ-E?t=2059)** and the **row-summary preview at [39:21](https://youtu.be/_kPVgWgKZ-E?t=2361)** in real time, you need at least one saved fictional Battery Inspection row.

1. Complete the three optional column examples above: **Battery Temperature**, **Inspection Status**, and **Finding Description**. For this *optional early exploration only*, also create **Battery Unit Label** as **Single line of text**. This extra preparation is not an additional podcast exercise; the guided practice teaches Battery Unit Label at **[50:28](https://youtu.be/_kPVgWgKZ-E?t=3028)**. When you reach that moment, **verify and reuse** the existing column instead of creating it twice.
2. Open **Battery Inspection → Edit data / Data** (the label varies by maker experience), then choose **New row**. The table's primary-name field is still called **Name** at this point.
3. Enter **Practice record A** using the values below, then **Save**. Choose the existing **Inspection Status** value from its Choice list rather than typing a new choice.

| Field | Practice record A — enter before Prompt testing |
|---|---|
| **Name** (later **Inspection Record Name**) | `BESS-07 Surface Review` |
| **Battery Unit Label** | `BESS-07` |
| **Finding Description** | `Visual surface mark observed on the battery unit housing. Maintenance review requested. No corrective work has been documented.` |
| **Inspection Status** | `Review required` |
| **Battery Temperature** (optional Decimal) | `31.2` |

**✅ Check:** The saved row appears under **Battery Inspection**. Its original observation is stored in **Finding Description**; no repair, safety approval or completion is implied.

If you prefer to follow the main guided column exercise **before** adding any early fields or rows, that's fine: skip this preparation now, complete **[49:57](https://youtu.be/_kPVgWgKZ-E?t=2997)**, add **Inspection Status** (and optionally **Battery Temperature**), enter the practice records, and then return to the AI demonstrations. **Do not duplicate columns.**

You can also [download the optional sample-record CSV](resources/M05_Battery_Inspection_Practice_Records.csv) for copy/paste reference. **Manual entry is recommended** for two records; the CSV is not a claim that the podcast teaches a data import.

**▶️ [Resume at 29:56](https://youtu.be/_kPVgWgKZ-E?t=1796).**

## 4. Prompt column: stored AI text (optional advanced walkthrough)

**🔎 Pause at [31:37](https://youtu.be/_kPVgWgKZ-E?t=1897) only if you have an eligible environment.** This is a feature walkthrough, not a requirement to spend credits or create a new app.

**Prepare:** For a live Prompt test, use **Practice record A — `BESS-07 Surface Review`** from the [sample-record setup](#practice-record-for-the-optional-ai-demonstrations) above. It supplies the mapped inputs **Finding Description**, **Inspection Status** and **Battery Unit Label**. Without those fields and a saved row, the preview has no example data. If you skipped early practice, first complete the guided column exercise at [49:57](https://youtu.be/_kPVgWgKZ-E?t=2997), add the optional Inspection Status Choice, save the record, then return here. Copilot/AI Prompts feature enablement, geography, permissions and credits may apply.

1. Open **Battery Inspection → New → Column**.
2. Set **Display name:** `Battery Review Brief`.
3. Set **Description:** `AI-generated summary requiring human review`.
4. Set **Data type:** **Prompt**. Clear **Allow form fill assistance** if shown.
5. Select **Add new prompt** (if available). The episode describes a maximum of **five Prompt columns per table**.
6. Compose the following instructions, combining the sentences the hosts actually prescribe at [32:37](https://youtu.be/_kPVgWgKZ-E?t=1957) and [32:54](https://youtu.be/_kPVgWgKZ-E?t=1974):

```text
Describe the inspection finding and review status in no more than three plain-English sentences. Use only the selected Battery Inspection input fields. If no corrective work is explicitly recorded, say Corrective work not documented. Never say the inspection is approved or safe unless that exact status is present in the source fields.
```

7. Choose **Add content**, select the table, and insert the **Finding Description**, **Inspection Status** and **Battery Unit Label** columns as supported input references. Do not map confidential fields just because the picker shows them. Formula, File, Image and Prompt columns are not supported effective prompt inputs.
8. For **Test**, select **Practice record A** (`BESS-07 Surface Review`) as the example record where your editor permits. In the older **Filter knowledge → Filter attribute** experience described by the episode, choose the identifying **Name** field (or **Inspection Record Name** after renaming) and enter `BESS-07 Surface Review`. If your editor instead uses a required record-ID variable, choose the saved practice row through that interface; do not substitute its display name where a GUID is required. Select **Test** and compare the response with the record's **Finding Description** and **Inspection Status**. Review **Knowledge used** where offered. If the response claims a repair is complete, the unit is safe, or the inspection is approved, that is unsupported; revise the instruction and retest.
9. The podcast describes **Filter knowledge → Filter attribute** to target an inspection by name, followed by **No filter** after testing. **Current Microsoft documentation may instead require the default `PromptColumnRecordId` text variable, filtered to a primary identifier, to be retained for saving.** Follow the controls and validation shown in your actual editor: do not delete a required record variable or save a test-only restriction as a production rule. [Current Prompt column documentation](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/prompt-column).
10. Save the **prompt**, then save the **column**. The generated value can appear **asynchronously**, not necessarily at row-save time.

**✅ Check:** The AI field is clearly distinguishable from the inspector's original observation. If a value is blank, inspect the column's actual **PromptColumnStatus / PromptColumnDetails** companion fields, available credits, referenced inputs, and access—not merely whether the row exists.

**Do not confuse filters:** The temporary test-record selection is different from a configured **Apply filter → Add filter → OK / Save** condition that controls when a prompt should execute (discussed at [37:37](https://youtu.be/_kPVgWgKZ-E?t=2257)).

**▶️ [Resume at 38:16](https://youtu.be/_kPVgWgKZ-E?t=2296).**

## 5. Row summary: read-time assistance, not a stored column

**🔎 Watch at [38:16](https://youtu.be/_kPVgWgKZ-E?t=2296); optionally inspect the maker interface at [39:21](https://youtu.be/_kPVgWgKZ-E?t=2361).**

Unlike **Battery Review Brief**, a **row summary** is an AI-generated overview displayed in the model-driven app experience. It is **not** a dedicated stored Prompt column or proof of approval.

If your environment enables row summaries, use **Practice record A — `BESS-07 Surface Review`** for the preview. It contains a written finding and the Choice value **Review required**. If you did not enter this row yet, follow the [sample-record preparation](#practice-record-for-the-optional-ai-demonstrations) before testing.

1. In **Tables → Battery Inspection → Customizations**, select **Row summary**. If disabled, hover for the reason; a data row may be required.
2. In the **Prompt** area, select **Add** or type `/` to insert only appropriate column references.
3. For an **additional practice prompt** (not a quote from the episode), use: `Summarize the inspection finding and current review status in two short sentences using only the selected record fields. If no completed corrective work is recorded, say corrective work not documented. Do not claim the battery is safe, repaired or approved.` Do not ask AI to calculate authoritative elapsed days or safety decisions.
4. Select **Test prompt**, review the preview using the available record, then select **Apply to main forms** if appropriate.

**✅ Check:** The output is a reading aid. A release to another environment may also require adding the correct **AI Skill Config** component through **Solution → Add existing → More → Other → AI Skill Config**, followed by a separate destination-environment review. Do not add unrelated system rows. [Microsoft row-summary documentation](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/configure-form-row-summary).

**▶️ [Resume at 42:30](https://youtu.be/_kPVgWgKZ-E?t=2550).**

## 6. Before the main exercise: primary name, GUID, number and key

**👀 Watch [42:30](https://youtu.be/_kPVgWgKZ-E?t=2550)–[49:57](https://youtu.be/_kPVgWgKZ-E?t=2997).**

- **Primary-name column:** a friendly record title shown to people; its **display name** can be changed, but that does **not** rename the stable schema name.
- **GUID:** the hidden system-generated row identifier and underlying primary key. It is not the human-readable ticket number.
- **Autonumber:** a formatted identifier such as a `BAT-` prefix plus four-digit sequence. It does not replace the GUID.
- **Alternate key:** a uniqueness constraint based on existing business fields. Its background index job can be `Pending`, `In Progress`, `Active` or `Failed`; enforce uniqueness **only after it is Active**.
- **Choice versus Lookup:** use a stable status list for Choice and a related asset table for a large changing inventory. The episode also mentions limits on rollups and multiple-select Choices.

**▶️ [Continue at 49:57](https://youtu.be/_kPVgWgKZ-E?t=2997)** for the actual guided Dataverse exercise.

## 7. Main guided exercise — configure Battery Inspection

**⏸️ Pause at [49:57 — Guided maker practice](https://youtu.be/_kPVgWgKZ-E?t=2997).** Return to the **Battery Inspection** table created during the [Module 5 setup](#module-5-setup-create-the-battery-inspection-table) in your approved development environment. Confirm the actual solution publisher rather than assuming `svrg`.

### Activity A — Battery Unit Label

**⏸️ [50:28 — Add Battery Unit Label](https://youtu.be/_kPVgWgKZ-E?t=3028)**

1. Open **Battery Inspection → Columns**; select **+ Add column** or **New column**.
2. **Display name:** `Battery Unit Label`.
3. **Data type:** **Single line of text**.
4. **Searchable:** keep enabled if users will need to find this label in supported searches.
5. **Save**.

**✅ Check:** `Battery Unit Label` appears once in the table's column list.

**▶️ [Resume at 50:52](https://youtu.be/_kPVgWgKZ-E?t=3052).**

### Activity B — Finding Description

**⏸️ [50:52 — Add Finding Description](https://youtu.be/_kPVgWgKZ-E?t=3052)**

1. Add a column named `Finding Description` **if it does not already exist**.
2. Select the text format that offers a **Text area**, or **Multiple lines of text** for longer, multi-paragraph observations.
3. If you choose a character limit, document why that limit meets the actual observation requirement.
4. Save and verify that the column appears once.

**✅ Check:** The field can hold a genuine observation, not just a short code. It is **human-entered evidence**, not an AI-generated conclusion.

**▶️ [Resume at 51:21](https://youtu.be/_kPVgWgKZ-E?t=3081).**

### Activity C — Rename the primary-name display label

**⏸️ [51:21 — Rename primary name](https://youtu.be/_kPVgWgKZ-E?t=3081)**

1. Locate the table's existing primary-name column, commonly displayed as `Name`.
2. Select **Edit column**.
3. Change **Display name** to `Inspection Record Name`.
4. **Save**. **Do not change its existing schema name.**

**✅ Check:** The user-friendly name is `Inspection Record Name`, while the Dataverse GUID still serves as the primary key.

**▶️ [Resume at 51:43](https://youtu.be/_kPVgWgKZ-E?t=3103).**

### Activity D — Add the generated ticket number

**⏸️ [51:43 — Inspection Ticket Number](https://youtu.be/_kPVgWgKZ-E?t=3103)**

1. Select **New column**.
2. **Display name:** `Inspection Ticket Number`.
3. **Data type:** **Autonumber**.
4. Select **Custom** format, if available, with a **four-digit sequential segment** and starting seed `1000` where configurable.
5. The episode says you may optionally prepend `BAT-`. A documented syntax example for that pattern is:

```text
BAT-{SEQNUM:4}
```

6. Save the Autonumber column. **Check existing-row behavior rather than assuming retroactive backfill.**
7. **Extra verification record (not narrated):** Now open **Battery Inspection → Edit data / Data → New row**, and create **Practice record B** with **Inspection Record Name** `BESS-08 Connector Review`, **Battery Unit Label** `BESS-08`, and **Finding Description** `Connector enclosure showed no visible damage during inspection. Review remains open; no corrective work has been documented.`. If you created **Inspection Status**, select `Open`; if you created **Battery Temperature**, enter `28.4`. Save. **Leave Inspection Ticket Number system-generated**—do not type a ticket manually.

**✅ Check:** The **new Practice record B** receives a system-generated **Inspection Ticket Number** according to your configured format. Older Practice record A may behave differently; inspect it rather than assuming it was backfilled. The ticket number is not the underlying GUID.

**▶️ [Resume at 52:12](https://youtu.be/_kPVgWgKZ-E?t=3132).**

### Activity E — Create an alternate key

**⏸️ [52:12 — Inspection Record Name Key](https://youtu.be/_kPVgWgKZ-E?t=3132)**

1. Before creating the key, confirm the two saved practice rows have **different Inspection Record Name** values: `BESS-07 Surface Review` and `BESS-08 Connector Review`. If you skipped optional row setup, enter at least **one** uniquely named practice row now. Duplicate names can prevent key activation.
2. Open **Battery Inspection → Schema → Keys → New key**.
3. **Display name:** `Inspection Record Name Key`.
4. Select **Inspection Record Name**, the renamed primary-name column, as the **only key column** for this exercise.
5. Select **Save**, then inspect the key's status. The background indexing job may take time.

**✅ Check:** The key reaches **Active**, not merely `Pending` or `In Progress`. **Negative test:** try to save another practice row with the already-used **Inspection Record Name** `BESS-07 Surface Review` and a different Battery Unit Label, for example `BESS-09`. **Expected outcome:** the save is rejected as a duplicate key. This is an attempted test only—**do not add that duplicate row to your dataset**. If the duplicate is accepted, confirm the key is actually **Active** and that you selected the right column. [Microsoft alternate-key guidance](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/define-alternate-keys-portal).

**▶️ [Resume at 52:44](https://youtu.be/_kPVgWgKZ-E?t=3164)** to compare expected results.

## 8. Final verification and troubleshooting

**⏸️ At [52:44](https://youtu.be/_kPVgWgKZ-E?t=3164)** check the actual saved state, not just whether you clicked Save.

- [ ] The original **Battery Inspection** table is in the intended environment and solution.
- [ ] `Battery Unit Label` exists with **Single line of text**.
- [ ] `Finding Description` exists with an appropriate longer-text configuration.
- [ ] Primary-name **display label** is now `Inspection Record Name`; its schema name was not changed.
- [ ] `Inspection Ticket Number` is **Autonumber** and generates a number for a **new** practice record (such as Practice record B).
- [ ] `Inspection Record Name Key` is **Active** and rejects duplicate names when tested safely.
- [ ] If configured, `Battery Review Brief` remains a clearly labeled **AI-generated** field—not the original inspection evidence.

**If the alternate key is `Failed`** (discussed at [53:18](https://youtu.be/_kPVgWgKZ-E?t=3198)), check duplicate/blank sample values, eligible column type, field security and system job details. A visible key name does **not** prove that uniqueness is enforced. If the Prompt field is empty, inspect actual execution status, credits, input changes, feature permissions and error details.

**▶️ [Resume at 53:50](https://youtu.be/_kPVgWgKZ-E?t=3230)** for the recap. **Module 6** moves on to Dataverse security roles and teams.

---

### Helpful official references

- [Microsoft Learn — Create and manage columns within a Dataverse table](https://learn.microsoft.com/en-us/training/modules/create-manage-fields-within-entity/)
- [Prompt columns in Microsoft Dataverse](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/prompt-column)
- [Configure a row summary for a model-driven app](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/configure-form-row-summary)
- [Autonumber columns](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/create-auto-number-attributes)
- [Define alternate keys using Power Apps](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/define-alternate-keys-portal)
- [SunnyVerse Intelligent Applications course](https://sunnyverse.odoo.com/intelligent-applications)

*© 2026 SunnyVerse AI Labs. Original independent educational companion. SunnyVerse Renewable Group and all sample values are fictional. Not affiliated with or endorsed by Microsoft. Always validate current feature availability, permissions and licensing in your own environment.*