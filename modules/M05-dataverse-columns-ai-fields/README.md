# Dataverse Columns, Prompt Fields & Alternate Keys | AB-410 M05

**SunnyVerse Intelligent Applications · Twinkle & Celestyn — Design & Troubleshooting Lab**  
▶️ **[Watch Module 5 on YouTube](https://youtu.be/_kPVgWgKZ-E)** · **Runtime: 55:29** · **Learning path: Dataverse foundations**

## How to follow this guide

**First complete the Module 5 table setup below, then start the podcast from the beginning.** A **👀 Watch & understand** section explains a concept: keep watching and refer to its short notes. When you see **⏸️ Pause & build**, pause YouTube, perform the steps in your permitted Power Apps learning environment, verify the result, then select the **▶️ Resume** link. **🔎 Optional exploration** means the hosts explain a feature that you can inspect, but it is not a required additional build.

**Module 5 begins with a required setup step:** Create a new Dataverse table named **Battery Inspection** using the instructions below. Learners following this course from Module 1 have not created this table in Modules 1–4. Complete the setup **before starting the Module 5 podcast**. Table creation is a supporting step added to make this guide self-contained; the podcast starts with the table already prepared. Work only in an approved learning environment using fictional data.

**Follow the lesson in order:** The examples before [49:57](https://youtu.be/_kPVgWgKZ-E?t=2997) explain how fields and AI features work. **Do not create Battery Unit Label, Finding Description, or sample records during those explanations.** The guided exercise creates those columns at **50:28** and **50:52**. After finishing the exercise, you can add fictional practice records and revisit the optional AI demonstrations. Prompt columns and row summaries may depend on licensing, feature availability, and credits.

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
| [28:08](https://youtu.be/_kPVgWgKZ-E?t=1688) | Temperature, status, finding examples | 👀 Watch; no build yet |
| [31:37](https://youtu.be/_kPVgWgKZ-E?t=1897) | Prompt column demonstration | 👀 Watch; revisit after 52:44 |
| [32:37](https://youtu.be/_kPVgWgKZ-E?t=1957) | Prompt wording and source fields | 👀 Watch |
| [34:19](https://youtu.be/_kPVgWgKZ-E?t=2059) | Test generated content against a record | 👀 Watch; revisit after 52:44 |
| [35:32](https://youtu.be/_kPVgWgKZ-E?t=2132) | Remove temporary test restriction | 👀 Watch |
| [37:37](https://youtu.be/_kPVgWgKZ-E?t=2257) | Execution filters versus test filters | 👀 Watch |
| [39:21](https://youtu.be/_kPVgWgKZ-E?t=2361) | Row summary demonstration | 👀 Watch; revisit after 52:44 |
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

## 3. Watch the column examples — do not build ahead

**👀 At [28:08](https://youtu.be/_kPVgWgKZ-E?t=1688), continue watching.** Twinkle and Celestyn demonstrate how to choose ordinary field types. You are not yet at the module's guided creation steps.

| Column discussed | Type | What you should understand now |
|---|---|---|
| **Battery Temperature** | Decimal number | Measurement in degrees Celsius; example precision of one decimal place |
| **Inspection Status** | Single-select Choice | Options: `Open`, `Review required`, `Closed` |
| **Finding Description** | Multiple lines of text / Text area | Inspector-entered evidence, not an AI conclusion |

**Do not create these columns or enter practice records at this point.** In particular, **Finding Description** belongs to the guided exercise at [50:52](https://youtu.be/_kPVgWgKZ-E?t=3052). The optional **Battery Temperature** and **Inspection Status** columns can be created **after** the guided exercise, only if you want to test the advanced AI examples.

**▶️ [Continue at 31:37](https://youtu.be/_kPVgWgKZ-E?t=1897).**

## 4. Watch the Prompt column demonstration — practice later

**👀 Watch [31:37](https://youtu.be/_kPVgWgKZ-E?t=1897) through [38:16](https://youtu.be/_kPVgWgKZ-E?t=2296) without creating a field or test record.**

The hosts explain how a Prompt column uses referenced Dataverse fields to generate stored AI text, how the testing controls work, and why generated claims require human verification. **Battery Unit Label** is not created until [50:28](https://youtu.be/_kPVgWgKZ-E?t=3028), so do **not** create it early simply to test the prompt now.

After the guided exercise, the [optional Prompt practice](#9-optional-ai-practice-revisit-the-earlier-demonstrations) provides a complete fictional test record and the configuration steps from this segment.

**▶️ [Continue at 38:16](https://youtu.be/_kPVgWgKZ-E?t=2296).**

## 5. Watch the row-summary explanation — practice later

**👀 Watch [38:16](https://youtu.be/_kPVgWgKZ-E?t=2296) through [42:30](https://youtu.be/_kPVgWgKZ-E?t=2550). No build is needed yet.**

A **row summary** is an AI-generated overview shown within a model-driven app experience; unlike a Prompt column, it is not a separately stored generated field. It needs a meaningful record for testing, which you will enter **after the main guided exercise**.

When you finish creating the columns and enter the sample records, return to the [optional Row Summary practice](#optional-b-row-summary).

**▶️ [Continue at 42:30](https://youtu.be/_kPVgWgKZ-E?t=2550).**

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

1. Add a new column named `Finding Description`. This is its first creation in the guided exercise.
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

6. Save the Autonumber column. **Do not enter sample data yet.** You will verify the generated ticket number after finishing the guided exercise.

**✅ Check:** The **Inspection Ticket Number** column exists with the configured Autonumber format. Verify actual generated values later, when you add the practice records in Section 8. The ticket number is not the underlying GUID.

**▶️ [Resume at 52:12](https://youtu.be/_kPVgWgKZ-E?t=3132).**

### Activity E — Create an alternate key

**⏸️ [52:12 — Inspection Record Name Key](https://youtu.be/_kPVgWgKZ-E?t=3132)**

1. Check that the **Inspection Record Name** column exists and is eligible as an alternate-key column. The new learning table should not have duplicate records yet; practice records are added **after** this guided exercise. If you already have records for another reason, confirm that their names are unique.
2. Open **Battery Inspection → Schema → Keys → New key**.
3. **Display name:** `Inspection Record Name Key`.
4. Select **Inspection Record Name**, the renamed primary-name column, as the **only key column** for this exercise.
5. Select **Save**, then inspect the key's status. The background indexing job may take time.

**✅ Check:** The key reaches **Active**, not merely `Pending` or `In Progress`. If activation is pending, inspect the status again before testing uniqueness. **You will test a duplicate name only after adding the fictional practice records in Section 8.** [Microsoft alternate-key guidance](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/define-alternate-keys-portal).

**▶️ [Resume at 52:44](https://youtu.be/_kPVgWgKZ-E?t=3164)** to review the result with the hosts. Continue through the [53:50 recap](https://youtu.be/_kPVgWgKZ-E?t=3230), then create the practice data in Section 8.

## 8. After the guided exercise — enter practice records

**🛠️ Additional learner practice, after [52:44 — Verification](https://youtu.be/_kPVgWgKZ-E?t=3164).** These two fictional rows and the following optional test steps support the module, but are **not** values dictated by the podcast. **Do not perform them before the 50:28 and 50:52 column-creation steps.**

At this point the module's guided exercise has created **Battery Unit Label**, **Finding Description**, the renamed **Inspection Record Name**, **Inspection Ticket Number**, and **Inspection Record Name Key**. Use the finished table rather than creating any of these again.

### Prepare additional fields for optional AI testing

**Only if you want to test the earlier Prompt and row-summary demonstrations**, add the following **optional** columns now, based on the examples discussed at [28:08](https://youtu.be/_kPVgWgKZ-E?t=1688):

| Additional column | Type | Values or settings |
|---|---|---|
| **Inspection Status** | Choice (one value) | `Open`, `Review required`, `Closed` |
| **Battery Temperature** | Decimal number | Description: `Recorded measurement in degrees Celsius`; one decimal place if suitable |

**✅ Check:** The five guided-exercise components remain in place, and you add only the optional columns that were not already created. **Do not recreate Finding Description or Battery Unit Label.**

### Enter two fictional practice records

In **Battery Inspection → Edit data / Data**, create the following rows **manually**, selecting Choice values from the options you configured. The **Inspection Record Name** field is the renamed primary-name display label. **Do not type a value in Inspection Ticket Number**; Dataverse generates it.

| Field | Practice record A | Practice record B |
|---|---|---|
| **Inspection Record Name** | `BESS-07 Surface Review` | `BESS-08 Connector Review` |
| **Battery Unit Label** | `BESS-07` | `BESS-08` |
| **Finding Description** | `Visual surface mark observed on the battery unit housing. Maintenance review requested. No corrective work has been documented.` | `Connector enclosure showed no visible damage during inspection. Review remains open; no corrective work has been documented.` |
| **Inspection Status** *(if added)* | `Review required` | `Open` |
| **Battery Temperature** *(if added)* | `31.2` | `28.4` |
| **Inspection Ticket Number** | *Leave blank; system-generated* | *Leave blank; system-generated* |

**✅ Verify:** Both rows save with different Inspection Record Name values. New rows should receive generated ticket values according to your configured autonumber format. If the alternate key is still pending, check that it reaches **Active** before testing duplicate names.

**Alternate-key negative test (extra learner practice):** After the key is **Active**, attempt to save another row named `BESS-07 Surface Review` with a different Battery Unit Label such as `BESS-09`. The duplicate should be rejected. **Do not add a duplicate record to the dataset.**

[Download the two sample records as CSV](resources/M05_Battery_Inspection_Practice_Records.csv) for reference or copy/paste. Manual entry is simplest for two records; importing CSV is **not** part of this podcast's guided exercise.

**▶️ Next:** If you want the optional AI experiments, return to [31:37 — Prompt column](https://youtu.be/_kPVgWgKZ-E?t=1897) and use Section 9. Otherwise continue to the final checklist.

## 9. Optional AI practice: revisit the earlier demonstrations

**These practical tests come after the main guided exercise** to preserve the column-creation order. The concepts were discussed earlier at [31:37](https://youtu.be/_kPVgWgKZ-E?t=1897) and [39:21](https://youtu.be/_kPVgWgKZ-E?t=2361). If the features are unavailable, you may complete Module 5 without these optional tests.

### Optional A — Prompt column: stored AI text

**🔁 After finishing the main exercise and Section 8, replay [31:37 — Prompt column](https://youtu.be/_kPVgWgKZ-E?t=1897)** if your environment supports this optional AI feature. The column and sample data now exist, so you can test without building ahead or spending credits unintentionally.

**Prepare:** Use **Practice record A — `BESS-07 Surface Review`**, created in Section 8 **after** the guided exercise. The fields **Finding Description**, **Battery Unit Label**, and optional **Inspection Status** are now present. If you did not create the optional Inspection Status Choice or save a row, complete that preparation before testing a prompt that references those inputs. Copilot/AI Prompts feature enablement, geography, permissions, and credits may apply.

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

**▶️ [Replay the row-summary explanation at 38:16](https://youtu.be/_kPVgWgKZ-E?t=2296)** if continuing the optional AI practice.

### Optional B: Row summary

**🔁 After Section 8, replay [39:21 — Row summary](https://youtu.be/_kPVgWgKZ-E?t=2361)** if the feature is available and you want to follow the optional demonstration using a saved row.

Unlike **Battery Review Brief**, a **row summary** is an AI-generated overview displayed in the model-driven app experience. It is **not** a dedicated stored Prompt column or proof of approval.

If your environment enables row summaries, use **Practice record A — `BESS-07 Surface Review`** from Section 8. It contains a written finding and, if you added the optional Choice field, the value **Review required**. Create that practice row **after** the guided exercise, not before it.

1. In **Tables → Battery Inspection → Customizations**, select **Row summary**. If disabled, hover for the reason; a data row may be required.
2. In the **Prompt** area, select **Add** or type `/` to insert only appropriate column references.
3. For an **additional practice prompt** (not a quote from the episode), use: `Summarize the inspection finding and current review status in two short sentences using only the selected record fields. If no completed corrective work is recorded, say corrective work not documented. Do not claim the battery is safe, repaired or approved.` Do not ask AI to calculate authoritative elapsed days or safety decisions.
4. Select **Test prompt**, review the preview using the available record, then select **Apply to main forms** if appropriate.

**✅ Check:** The output is a reading aid. A release to another environment may also require adding the correct **AI Skill Config** component through **Solution → Add existing → More → Other → AI Skill Config**, followed by a separate destination-environment review. Do not add unrelated system rows. [Microsoft row-summary documentation](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/configure-form-row-summary).

**✅ Check:** The preview is a descriptive reading aid, not a statement that any repair, approval, or safety check is complete.

## 10. Final verification and troubleshooting

**⏸️ At [52:44](https://youtu.be/_kPVgWgKZ-E?t=3164)** check the actual saved state, not just whether you clicked Save.

- [ ] The **Battery Inspection** table was created during Module 5 setup in the intended environment and solution.
- [ ] `Battery Unit Label` exists with **Single line of text**.
- [ ] `Finding Description` exists with an appropriate longer-text configuration.
- [ ] Primary-name **display label** is now `Inspection Record Name`; its schema name was not changed.
- [ ] `Inspection Ticket Number` is **Autonumber** and generates a number for a **new** practice record (such as Practice record B).
- [ ] `Inspection Record Name Key` is **Active** and rejects duplicate names when tested safely.
- [ ] If configured, `Battery Review Brief` remains a clearly labeled **AI-generated** field—not the original inspection evidence.

**If the alternate key is `Failed`** (discussed at [53:18](https://youtu.be/_kPVgWgKZ-E?t=3198)), check duplicate/blank sample values, eligible column type, field security and system job details. A visible key name does **not** prove that uniqueness is enforced. If the Prompt field is empty, inspect actual execution status, credits, input changes, feature permissions and error details.

**▶️ [Review the 53:50 podcast recap](https://youtu.be/_kPVgWgKZ-E?t=3230)** if needed. **Module 6** moves on to Dataverse security roles and teams.

---

### Helpful official references

- [Microsoft Learn — Create and manage columns within a Dataverse table](https://learn.microsoft.com/en-us/training/modules/create-manage-fields-within-entity/)
- [Prompt columns in Microsoft Dataverse](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/prompt-column)
- [Configure a row summary for a model-driven app](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/configure-form-row-summary)
- [Autonumber columns](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/create-auto-number-attributes)
- [Define alternate keys using Power Apps](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/define-alternate-keys-portal)
- [SunnyVerse Intelligent Applications course](https://sunnyverse.odoo.com/intelligent-applications)

*© 2026 SunnyVerse AI Labs. Original independent educational companion. SunnyVerse Renewable Group and all sample values are fictional. Not affiliated with or endorsed by Microsoft. Always validate current feature availability, permissions and licensing in your own environment.*