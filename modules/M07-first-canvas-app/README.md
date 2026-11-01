# Build Your First Canvas App from Excel | AB-410 M07

**SunnyVerse Intelligent Applications · Twinkle & Celestyn — Design & Troubleshooting Lab**  
**▶️ [Watch the Module 7 podcast](https://youtu.be/_G8UkxDQGqc)** · Approximately **1:20:12** · Learning path: Power Apps and portals

## How to use this build-along guide

**Play the podcast from the beginning.** When you reach **⏸️ Pause & build**, pause the video and follow the instructions on your own screen. **✅ Verify** your result before selecting **▶️ Resume** to continue the podcast. **👀 Watch & understand** means no action is required. Timestamps jump to the corresponding conversation, so you can also return to a particular stage later.

You will practice **three different ways to get started**, not three steps of one automatically synchronized application:

1. **Excel in OneDrive → generated canvas app:** the app reads and edits the **same workbook**.
2. **Excel in OneDrive → blank canvas app:** a second app you build manually against the **same workbook**.
3. **File upload → new Dataverse table + generated canvas app:** a **different storage location**, with no automatic updates back to OneDrive. The optional conversation-based Dataverse approach is another *alternative*, not something you must run as well.

Use a permitted, non-production Power Apps environment, an authorized work/school account, and **fictional records only**. The Excel-backed exercises need Excel and OneDrive access. The Dataverse/Copilot alternatives depend on the correct environment, features, permissions, region, and licensing. **If a feature is missing, follow the explanation without creating duplicate data or bypassing organizational restrictions.** Do not publish or share the training apps with colleagues as part of this module.

### Start with the actual learner workbook

**📗 [Download M7_Solar_Data.xlsx](downloads/M7_Solar_Data.xlsx)**, and save a working copy on your device. It already includes an Excel worksheet and a **formatted Excel table**, both named `SolarInstallations`. Do **not** replace this workbook with a CSV or assume that unformatted cells count as an Excel table.

| Required column — exact header | Example: first record | What it means |
|---|---|---|
| `Request ID` | `SOL-101` | A unique fictional request identifier |
| `Solar Site` | `Solar Site A` | Fictional proposed installation location |
| `Region` | `West` | Region label |
| `Capacity kW` | `120` | Requested power capacity, numeric |
| `Status` | `Draft` | Review state |
| `Inspection Notes` | `Initial layout submitted` | A text note |
| `Solar Preview [image]` | Encoded illustrative data | Optional visual field; may display as text depending on connector |

The six prepared requests are **SOL-101 through SOL-106**, from **Solar Site A to Solar Site F**. These are installation requests, not commands to operate live solar equipment. A screenshot is not a suitable replacement for this workbook.

## Podcast chapter map

| Time | Topic | What to do |
|---|---|---|
| [00:00](https://youtu.be/_G8UkxDQGqc?t=0) | Canvas apps, controls and data | 👀 Watch |
| [09:59](https://youtu.be/_G8UkxDQGqc?t=599) | Power Apps maker portal | ✅ Check access |
| [14:25](https://youtu.be/_G8UkxDQGqc?t=865) | Solar workbook and fields | ✅ Check workbook |
| [17:25](https://youtu.be/_G8UkxDQGqc?t=1045) | Why an Excel table matters | 👀 Watch |
| [18:17](https://youtu.be/_G8UkxDQGqc?t=1097) | Upload workbook to OneDrive | ⏸️ Pause & build |
| [19:27](https://youtu.be/_G8UkxDQGqc?t=1167) | Generate app from Excel Online | ⏸️ Pause & build |
| [22:14](https://youtu.be/_G8UkxDQGqc?t=1334) | Browse screen and Tree view | ✅ Inspect |
| [23:44](https://youtu.be/_G8UkxDQGqc?t=1424) | `ThisItem` and gallery labels | ⏸️ Pause & build |
| [27:04](https://youtu.be/_G8UkxDQGqc?t=1624) | Optional image field | 👀 Watch / optional |
| [30:29](https://youtu.be/_G8UkxDQGqc?t=1829) | Detail and edit screens | ✅ Inspect |
| [32:33](https://youtu.be/_G8UkxDQGqc?t=1953) | Test Excel write-back: SOL-102 | ⏸️ Pause & verify |
| [36:10](https://youtu.be/_G8UkxDQGqc?t=2170) | Save the generated app | ⏸️ Pause & build |
| [37:26](https://youtu.be/_G8UkxDQGqc?t=2246) | Explore app templates | 👀 Watch / optional |
| [39:04](https://youtu.be/_G8UkxDQGqc?t=2344) | Start a blank tablet app | ⏸️ Pause & build |
| [40:18](https://youtu.be/_G8UkxDQGqc?t=2418) | Insert and connect gallery | ⏸️ Pause & build |
| [42:50](https://youtu.be/_G8UkxDQGqc?t=2570) | Add and configure Edit form | ⏸️ Pause & build |
| [45:08](https://youtu.be/_G8UkxDQGqc?t=2708) | Bind form to selected gallery row | ⏸️ Pause & build |
| [46:32](https://youtu.be/_G8UkxDQGqc?t=2792) | Optional image-card warning | 👀 Watch |
| [48:29](https://youtu.be/_G8UkxDQGqc?t=2909) | Save Changes button | ⏸️ Pause & build |
| [50:05](https://youtu.be/_G8UkxDQGqc?t=3005) | Test manual save: SOL-104 | ⏸️ Pause & verify |
| [51:11](https://youtu.be/_G8UkxDQGqc?t=3071) | Add heading and rectangle | ⏸️ Pause & build |
| [53:30](https://youtu.be/_G8UkxDQGqc?t=3210) | Compare Excel, SharePoint, Dataverse, SQL | 👀 Watch |
| [55:51](https://youtu.be/_G8UkxDQGqc?t=3351) | Delegation and connector limits | 👀 Watch |
| [58:57](https://youtu.be/_G8UkxDQGqc?t=3537) | Excel upload creates new Dataverse data | 👀 Watch |
| [1:00:40](https://youtu.be/_G8UkxDQGqc?t=3640) | Optional Dataverse upload route | ⏸️ Pause & build (if eligible) |
| [1:03:18](https://youtu.be/_G8UkxDQGqc?t=3798) | Correct column types and choices | ⏸️ Pause & check |
| [1:04:22](https://youtu.be/_G8UkxDQGqc?t=3862) | Save table and open Dataverse app | ⏸️ Optional save |
| [1:05:34](https://youtu.be/_G8UkxDQGqc?t=3934) | Conversation-first table alternative | 👀 Watch / optional |
| [1:07:47](https://youtu.be/_G8UkxDQGqc?t=4067) | Verify new Dataverse app | ⏸️ Pause & verify |
| [1:10:24](https://youtu.be/_G8UkxDQGqc?t=4224) | Power Automate's supporting role | 👀 Watch |
| [1:11:36](https://youtu.be/_G8UkxDQGqc?t=4296) | Power BI's supporting role | 👀 Watch |
| [1:13:30](https://youtu.be/_G8UkxDQGqc?t=4410) | Design questions and accessibility | 👀 Watch |
| [1:19:17](https://youtu.be/_G8UkxDQGqc?t=4757) | Recap and Module 8 bridge | 👀 Watch |

## 1. Confirm access and prepare the workbook

**⏸️ At [09:59 — Maker portal](https://youtu.be/_G8UkxDQGqc?t=599)**, open [Power Apps](https://make.powerapps.com/) and sign in with an authorized work/school account. Check the environment at the top of the page. Identify **Home**, **Create** or **Start with data**, **Apps**, and optionally **App templates**. Power Apps Mobile is optional; it does not grant additional permissions to the workbook.

**⏸️ At [14:25 — Solar workbook](https://youtu.be/_G8UkxDQGqc?t=865)**, open the downloaded Excel workbook. Check the **seven headers**, **six records**, and the named `SolarInstallations` table. If preparing a different Excel file manually, select the range with headers → **Insert → Table**, confirm headers, and name the table `SolarInstallations`; the provided file is already prepared.

**✅ Verify:** The table is named exactly `SolarInstallations` and records from `SOL-101` to `SOL-106` are present. Avoid changing header names, table name, or field types while following the episode.

**▶️ Resume at [18:17 — Upload the workbook](https://youtu.be/_G8UkxDQGqc?t=1097).**

## 2. Upload the workbook to OneDrive

**⏸️ Pause at [18:17](https://youtu.be/_G8UkxDQGqc?t=1097).**

1. Open **OneDrive** in your browser with your authorized Microsoft 365 account.
2. Navigate to an appropriate learning folder, select **Add new → Files upload**, and choose your **working copy of `M7_Solar_Data.xlsx`**.
3. After uploading, locate and open the file in Excel for the web.
4. Confirm its `SolarInstallations` table, seven columns and six rows. This confirms the file is in cloud storage; it does not automatically configure app sharing.

**✅ Verify:** The workbook is visible in the intended OneDrive account. Keep this tab available to check saved changes later.

**▶️ Resume at [19:27 — Generate from the live Excel table](https://youtu.be/_G8UkxDQGqc?t=1167).**

## 3. Generate the first Excel-backed canvas app

**⏸️ Pause at [19:27](https://youtu.be/_G8UkxDQGqc?t=1167).**

1. In **Power Apps → Start with data**, choose **Excel Online (Business)**.
2. Authorize the connection if asked. Browse to **the same OneDrive workbook** you uploaded.
3. Select the **`SolarInstallations`** Excel table—not the worksheet alone and not a Dataverse import option.
4. Select **Create app**. In the generated app, inspect the browse, details, and editing experiences. The number and names of generated screens can vary with the interface.
5. In **Tree view**, expand the browse screen and its gallery. Identify the label/control used for each record's primary display text.

**✅ Verify:** The app gallery shows six solar requests, and the connected source is the Excel table in OneDrive. This path does **not** convert your workbook to Dataverse.

**▶️ Resume at [23:44 — Customize gallery labels](https://youtu.be/_G8UkxDQGqc?t=1424).**

## 4. Map the generated gallery's text fields

**⏸️ Pause at [23:44](https://youtu.be/_G8UkxDQGqc?t=1424).** In **Tree view**, select the appropriate gallery label and its **Text** property. For classic labels, use the following exact expressions from the episode:

| Gallery label | Text property — copy exactly |
|---|---|
| Main/title label | `ThisItem.'Solar Site'` |
| Second/subtitle label | `ThisItem.'Request ID'` |
| Third available label | `ThisItem.Status` |

**What `ThisItem` means:** use the current record for *each* gallery row. Power Fx places single quotes around field names containing spaces. If your generated experience has a modern **Fields** picker rather than classic labels, select the corresponding fields in the right pane instead; don't invent a `Title1` control if it does not exist.

**✅ Verify:** Different rows show different sites and request IDs. For instance, `SOL-101` must be paired with `Solar Site A`, while `SOL-102` must be paired with `Solar Site B`.

**▶️ Resume at [27:04 — Optional gallery image](https://youtu.be/_G8UkxDQGqc?t=1624).**

### Optional A — Image preview

**👀 Watch [27:04–30:29](https://youtu.be/_G8UkxDQGqc?t=1624).** The workbook contains an encoded illustrative `Solar Preview [image]` value, not a hosted photograph. If you choose to experiment, insert an **Image** control in the gallery, shift nearby text labels right (the narration uses an illustrative `X = 80`), and set its **Image** property to:

```powerfx
ThisItem.'Solar Preview [image]'
```

The Excel connector **may show raw text instead of a usable image**. A built-in `SampleImage` is a *placeholder*, not evidence that a solar image loaded. Skip the image exercise if your environment cannot render the data; it is not necessary for saving inspection notes.

### Inspect the generated forms

**👀 Watch at [30:29](https://youtu.be/_G8UkxDQGqc?t=1829).** Expand the detail and edit screens. Inspect their forms and the selected-record binding. Use the field or data-card pane to identify `Inspection Notes`. Avoid deleting or unlocking cards without understanding their **Update** property.

## 5. Test the generated app against SOL-102

**⏸️ Pause at [32:33 — Write-back test](https://youtu.be/_G8UkxDQGqc?t=1953).**

1. Preview the app with **Play** or **F5**.
2. Select the record **`SOL-102` — `Solar Site B`** and open the generated edit screen.
3. Replace **Inspection Notes** with this **exact fictional example spoken in the podcast**:

```text
inspected on Tuesday, severe weather delay
```

4. Use the generated save/check control.
5. Close preview. Open or refresh **the same OneDrive workbook**, locate **SOL-102**, and confirm the note is present in its **Inspection Notes** cell. Confirm the **SOL-101** row was not changed.

**✅ Verify:** The correct Excel row was updated. A successful animation or visible text in the app is **not** enough; inspect the physical source row. If unchanged, check connection, permissions, saved action, workbook locking and whether you opened the correct file.

**▶️ Resume at [36:10 — Save the generated app](https://youtu.be/_G8UkxDQGqc?t=2170).**

### Save this first app

**⏸️ At [36:10](https://youtu.be/_G8UkxDQGqc?t=2170)**, close preview and save the app with the narrated example name **`Solar Installation Browse`**. Use **Back** to exit Studio. **Save** stores your maker changes; **Publish** and **Share** are separate actions and are not needed for this activity.

### Optional B — Explore an app template

**👀 Watch [37:26 — App templates](https://youtu.be/_G8UkxDQGqc?t=2246).** In **Create → App templates**, browse a template, review its description and required connections, and use **Use this template** if available. Templates do **not** automatically connect to `SolarInstallations`. You may inspect one without creating or republishing a replacement app.

## 6. Build a separate blank canvas app

**⏸️ Pause at [39:04 — Blank app](https://youtu.be/_G8UkxDQGqc?t=2344).** This is **another canvas app using the same Excel table**, not a new data import.

1. In Power Apps select **Create → Create from blank** (or **Start from blank**, depending on your UI).
2. Select **Tablet** layout and name the app **`Solar Installation Review`**.
3. In Studio, dismiss any welcome panel and **Save** the empty app.
4. At **[40:18 — Gallery](https://youtu.be/_G8UkxDQGqc?t=2418)**, select **Insert → Vertical gallery**.
5. With the gallery selected, use **Data** or the connection picker → **Excel Online (Business)** → the same OneDrive workbook → **`SolarInstallations`** table. Confirm the gallery's **Items/data source** points to `SolarInstallations`.
6. At **[41:41 — Field mapping](https://youtu.be/_G8UkxDQGqc?t=2501)**, map the three labels as before:

```powerfx
ThisItem.'Solar Site'
```

```powerfx
ThisItem.'Request ID'
```

```powerfx
ThisItem.Status
```

7. Resize the gallery to the **left half** of the tablet layout, leaving space for an edit form on the right.

**✅ Verify:** Six requests appear in the gallery and it is connected to the same workbook as `Solar Installation Browse`.

**▶️ Resume at [42:50 — Add an edit form](https://youtu.be/_G8UkxDQGqc?t=2570).**

## 7. Place an Edit form and bind it to the selected record

**⏸️ Pause at [42:50](https://youtu.be/_G8UkxDQGqc?t=2570).**

1. Click a blank area of the screen to deselect the gallery.
2. Select **Insert → Edit form**, position the form on the **right half** of the screen.
3. In the form's Properties choose **Data source: `SolarInstallations`**.
4. Choose **Edit fields → Add field** and select these **six narrated fields**: `Request ID`, `Solar Site`, `Region`, `Capacity kW`, `Status`, `Inspection Notes`. The optional image column need not be included.
5. At **[45:08 — Selected record](https://youtu.be/_G8UkxDQGqc?t=2708)**, select the form's **Item** property and enter:

```powerfx
Gallery1.Selected
```

6. **Important:** Use the actual gallery control name shown in **Tree view**; `Gallery1` is a narrated example, not a guaranteed autogenerated name.

**✅ Verify:** Clicking **Solar Site B** in the left gallery populates the edit form with `SOL-102` on the right. If blank, check the form's **Data source** and **Item**, and the gallery's actual name.

**▶️ Resume at [46:32 — Optional image-card warning](https://youtu.be/_G8UkxDQGqc?t=2792).**

### Optional C — Understand the image card, without breaking submission

**👀 Watch [46:32–48:11](https://youtu.be/_G8UkxDQGqc?t=2792).** A text data card cannot simply be replaced by an Image control without checking the card's **Update** expression. An old formula referring to a deleted text control may cause errors. For this first app, **leave the image card out of the submitted form** unless you have confirmed the connector and field support writing its value. This is an explanation, **not a required replacement step**.

## 8. Create the Save Changes button

**⏸️ Pause at [48:29 — Save button](https://youtu.be/_G8UkxDQGqc?t=2909).**

1. Select the **screen** in Tree view so the button is not nested in the wrong control.
2. Select **Insert → Button**; place it **below the Edit form**.
3. Set the button's **Text** property to the narrated label **`Save Changes`**.
4. Set the button's **OnSelect** property to:

```powerfx
SubmitForm(Form1)
```

5. As with `Gallery1`, replace `Form1` only if your form has a different name in Tree view. `SubmitForm` validates and attempts to write the selected record—it does not guarantee success.

**✅ Verify:** The button targets the actual edit form and there are no formula errors.

**▶️ Resume at [50:05 — Manual save test](https://youtu.be/_G8UkxDQGqc?t=3005).**

## 9. Test the manual Save Changes button with SOL-104

**⏸️ Pause at [50:05](https://youtu.be/_G8UkxDQGqc?t=3005).**

1. Open **Play/F5**, select **`SOL-104` — `Solar Site D`** from the left gallery.
2. Confirm that the form on the right shows the same request.
3. Change its **Inspection Notes** to a **distinct fictional progress comment of your choice**. The podcast does **not** dictate an exact sentence here, so do not confuse a new sample note with a quoted value.
4. Click **Save Changes**.
5. Open/refresh the connected **OneDrive workbook** and confirm **SOL-104**, rather than a different record, contains your new note.

**✅ Verify:** Your edit persisted to `SolarInstallations` in Excel. If not, check **OnSelect**, **Item**, connection access, required fields, errors and file locking before claiming success.

**▶️ Resume at [51:11 — Add a header](https://youtu.be/_G8UkxDQGqc?t=3071).**

## 10. Add a simple header and inspect layout

**⏸️ Pause at [51:11](https://youtu.be/_G8UkxDQGqc?t=3071).**

1. Insert a **Rectangle** across the top of the screen.
2. Use the narrated illustrative **Height = `75`** layout units.
3. Move the gallery and form down to avoid overlap.
4. Insert a **Text label**, set its **Text** to **`Solar Installation Review`**, and center it on the rectangle with readable contrast.
5. Preview the layout using **Play/F5** and check for overlapping controls on narrower screens. A tablet layout with absolute X and Y coordinates is **not automatically responsive**.
6. Save the app. Publishing and sharing are separate later skills.

**✅ Verify:** The header is legible, and the gallery, edit form and button remain usable.

**▶️ Resume at [53:30 — Data sources](https://youtu.be/_G8UkxDQGqc?t=3210).**

## 11. Understand data-source trade-offs

**👀 Watch [53:30–58:57](https://youtu.be/_G8UkxDQGqc?t=3210).** No new connector setup is required here.

| Source | Key consideration |
|---|---|
| **Excel in OneDrive** | Useful for a small demonstration; limited concurrent editing and data operations |
| **SharePoint lists** | Useful for internal list workflows; field types, permissions and delegation need review |
| **Dataverse** | Governed records, relationships and security; environment and licensing matter |
| **SQL** | Suitable for supported database workloads; connector, gateway and access requirements matter |

**Delegation** means that a supported operation runs on the data service rather than over a locally limited subset. Six records may hide incomplete searches that become important when the dataset grows. Adding Power Automate or Power BI does not automatically correct a weak source design.

## 12. Optional alternative — Upload the workbook to create Dataverse data

**👀 Start by watching [58:57 — The storage fork](https://youtu.be/_G8UkxDQGqc?t=3537).** This is **not another connection to the live OneDrive workbook**. Uploading creates a **new Dataverse table** in an eligible environment, so later edits in this new app **do not synchronize back to Excel**.

**⏸️ If your account supports it, pause at [1:00:40 — Upload file](https://youtu.be/_G8UkxDQGqc?t=3640).**

1. Confirm you are in an eligible **Dataverse development environment** with the necessary maker/Copilot access. If not, simply watch and skip the hands-on alternative.
2. Open **Power Apps → Start with data → Upload file**.
3. Choose **Select from device**, select the original `M7_Solar_Data.xlsx` file, and start **Import**.
4. Inspect the proposed table. If you see **Use first row as column headers**, verify it recognizes `Request ID`, `Solar Site`, and the other headings.
5. At **[1:03:18 — Edit column](https://youtu.be/_G8UkxDQGqc?t=3798)**, review the proposed types before accepting:

| Field | Human review |
|---|---|
| `Request ID`, `Solar Site` | Text |
| `Capacity kW` | Numeric, not free-form text |
| `Status`, `Region` | Consider Choice values where appropriate |
| `Inspection Notes` | Text; avoid making optional notes required by accident |
| `Solar Preview [image]` | May require deliberate exclusion or supported image mapping |

6. The podcast's example **Copilot refinement request** is to make `Status` a **Choice** column with **`Draft`**, **`Inspection Pending`**, and **`Approved`**. Check the proposed schema **visually**, not only the chat reply.
7. When the proposal is correct and you intend to create practice objects, select **Save and open app** at **[1:04:22](https://youtu.be/_G8UkxDQGqc?t=3862)**. This persists a new Dataverse table and starts a generated app. Check that Studio's data source is **Dataverse**, not Excel Online.

**✅ Verify:** You can identify the new Dataverse table and its records. No changes are assumed to have occurred in your original OneDrive workbook. Never assume generated table names or publisher prefixes; inspect the created objects.

**▶️ Resume at [1:05:34 — Conversation-based alternative](https://youtu.be/_G8UkxDQGqc?t=3934).**

### Optional D — Create new data by description (alternative, not a required duplicate)

**👀 Watch [1:05:34](https://youtu.be/_G8UkxDQGqc?t=3934).** If available, **Start with data → Create new data** lets you describe the table instead of uploading Excel. Here is the **spoken example**, with capitalization and punctuation formatted for copying:

```text
Create a table for SunnyVerse Solar Operations to track solar installation
requests with the columns Request ID, Solar Site, Region, Capacity kW,
Status, and Inspection Notes.
```

Use Copilot to refine the proposed structure if the feature is available, **inspect each field**, and select the relevant save action only if you **want a second separate practice table**. Running this and the upload route may create **two different Dataverse tables**, not one synchronized table. For most learners, completing **one** of these alternatives is sufficient.

### Verify the Dataverse-backed app

**⏸️ Pause at [1:07:47 — App verification](https://youtu.be/_G8UkxDQGqc?t=4067)** if you created the Dataverse variant.

1. Inspect the app's gallery, form, and search control (if present).
2. Search for `Solar Site B` or `SOL-102` **only if the generated search formula actually searches those columns**.
3. Edit a permitted fictional note and use the form's save control.
4. Inspect the **Dataverse table in the same environment** for the updated record. Do **not** check OneDrive expecting that update to appear automatically.
5. Save your app. Publish or share only if separately authorized and appropriate.

**✅ Verify:** The specific Dataverse row changed and the source connection is Dataverse. If an object is missing, check the selected environment and generated table rather than guessing.

**▶️ Resume at [1:10:24 — Related Power Platform services](https://youtu.be/_G8UkxDQGqc?t=4224).**

## 13. Finish the lesson without building ahead

**👀 Watch from [1:10:24 to the end](https://youtu.be/_G8UkxDQGqc?t=4224).** Power Automate can support notifications and workflows; Power BI supports aggregated reports. **No flow or dashboard is required in Module 7.** The closing discussion covers who uses the app, permissions, phone layouts, readability, accessibility, data volume and when Excel may stop being a suitable backend. Advanced layout, navigation and Power Fx customization come in **Module 8**.

### Completion check

- [ ] I used the provided six-row `SolarInstallations` workbook and confirmed its Excel table name.
- [ ] I built or inspected an Excel-backed generated canvas app and checked a real write-back to `SOL-102` in **OneDrive**.
- [ ] I built a separate blank tablet canvas app with a gallery, edit form, selected-record binding and **Save Changes** button, and verified the update to `SOL-104`.
- [ ] I understand that `ThisItem.'Solar Site'`, `Gallery1.Selected`, and `SubmitForm(Form1)` refer to specific controls and data context.
- [ ] I can explain why uploading a file for Dataverse creation results in a **different data source** from live OneDrive Excel.
- [ ] I did not accidentally create two Dataverse tables or publish the training apps.

### Troubleshooting quick reference

| Symptom | First check |
|---|---|
| Excel file cannot be selected | Workbook uploaded to the correct OneDrive; formatted table named `SolarInstallations`; authorized Excel connection |
| Gallery is empty | Gallery **Items** source; correct connection; six workbook rows |
| Labels show the same value | Use `ThisItem` rather than a hard-coded reference |
| Blank edit form | Form **Data source**, **Item** (`Gallery1.Selected` or actual gallery name), and selected record |
| Red formula error on save | Button **OnSelect** refers to the form's actual name; required fields and connection permissions |
| Excel note did not change | Confirm correct file and record, refresh, connection status, file lock or failed submission |
| Image shows code/text | Encoded image may not be supported in the chosen Excel control; skip optional image card |
| Copilot upload is missing | Dataverse environment, feature availability, licensing, region and maker permissions |
| Dataverse update is absent from OneDrive | Expected: they are **separate data sources** unless independently synchronized |

---

## More resources

- [Watch Module 7 — Twinkle & Celestyn](https://youtu.be/_G8UkxDQGqc)
- [Microsoft Learn — Get started with Power Apps canvas apps](https://learn.microsoft.com/en-us/training/modules/get-started-with-powerapps/)
- [Microsoft Learn — Create a canvas app based on Excel data](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/get-started-create-from-data)
- [SunnyVerse Intelligent Applications course](https://sunnyverse.odoo.com/intelligent-applications)
- [Return to the 17-module course index](../../README.md)

*Original educational material © 2026 SunnyVerse AI Labs. SunnyVerse Renewable Group and its requests are fictional; Microsoft products and services retain their owners' rights. Independent education, not affiliated with or endorsed by Microsoft. Product labels, licensing, and available features may differ by environment.*