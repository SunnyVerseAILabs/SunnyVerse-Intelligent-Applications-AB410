# Module 03 | Power Apps Plans — From Business Idea to Solution Design

**SunnyVerse Intelligent Applications · Twinkle & Celestyn — Design & Troubleshooting Lab**  
**Podcast:** [Play Module 3 on YouTube](https://youtu.be/BvRKiWRBNqA) · **Runtime:** 47:18 · **Learning path:** AI-first foundations  
**Guide type:** Timestamped conceptual learning companion with an **optional** Power Apps Plans interface walkthrough

> **How to use this guide:** Listen to the episode and click timestamps below to return to the relevant explanation. The times come from the actual `3T.sbv` generated-podcast subtitles; YouTube playback can differ by a few seconds. **This official-aligned module has no dedicated formal Exercise unit.** The screen-side actions describe what the podcast teaches; you do not need to create or deploy an application to complete Module 3. Where a step could change an environment (especially **Save tables**), proceed only with an approved practice environment and appropriate permissions.

## Jump to the moment you need

| Time | Podcast topic |
|---|---|
| [00:00](https://youtu.be/BvRKiWRBNqA?t=0) | Why business needs must come before generation |
| [02:05](https://youtu.be/BvRKiWRBNqA?t=125) | SunnyVerse Solar Operations scenario |
| [04:14](https://youtu.be/BvRKiWRBNqA?t=254) | Plans versus a finished app; eligibility |
| [05:58](https://youtu.be/BvRKiWRBNqA?t=358) | Plans availability and environment checks |
| [06:33](https://youtu.be/BvRKiWRBNqA?t=393) | Open Power Apps → Start with a plan |
| [07:24](https://youtu.be/BvRKiWRBNqA?t=444) | Three planning agents and their responsibilities |
| [08:15](https://youtu.be/BvRKiWRBNqA?t=495) | Describe the solar-review business problem |
| [10:10](https://youtu.be/BvRKiWRBNqA?t=610) | Generate and inspect proposed requirements |
| [11:28](https://youtu.be/BvRKiWRBNqA?t=688) | Edit roles and correct unsafe suggestions |
| [12:41](https://youtu.be/BvRKiWRBNqA?t=761) | Read and validate the process diagram |
| [15:42](https://youtu.be/BvRKiWRBNqA?t=942) | Data Agent: suggested tables and columns |
| [18:22](https://youtu.be/BvRKiWRBNqA?t=1102) | Security illusion: models are not permissions |
| [20:02](https://youtu.be/BvRKiWRBNqA?t=1202) | Edit data model and inspect relationships |
| [21:07](https://youtu.be/BvRKiWRBNqA?t=1267) | Solution Agent: technology recommendations |
| [23:45](https://youtu.be/BvRKiWRBNqA?t=1425) | Remove an unnecessary contractor portal |
| [25:07](https://youtu.be/BvRKiWRBNqA?t=1507) | Power BI tile: recommendation versus report |
| [26:03](https://youtu.be/BvRKiWRBNqA?t=1563) | Save tables, solution and publisher |
| [28:20](https://youtu.be/BvRKiWRBNqA?t=1700) | Collaborate and share a plan |
| [29:23](https://youtu.be/BvRKiWRBNqA?t=1763) | Export the plan to PDF |
| [29:57](https://youtu.be/BvRKiWRBNqA?t=1797) | Create a component from a technology tile |
| [35:31](https://youtu.be/BvRKiWRBNqA?t=2131) | Reuse an existing app |
| [36:21](https://youtu.be/BvRKiWRBNqA?t=2181) | Objects view and troubleshooting |
| [38:27](https://youtu.be/BvRKiWRBNqA?t=2307) | Reverse planning: create a plan from a solution |
| [43:06](https://youtu.be/BvRKiWRBNqA?t=2586) | Recap, guardrails and what follows |

**Suggested listening rhythm:** Read requirements as you hear [10:10](https://youtu.be/BvRKiWRBNqA?t=610); examine the process map at [12:41](https://youtu.be/BvRKiWRBNqA?t=761); scrutinize the proposed data structure at [15:42](https://youtu.be/BvRKiWRBNqA?t=942); evaluate technology proposals at [21:07](https://youtu.be/BvRKiWRBNqA?t=1267); treat [26:03](https://youtu.be/BvRKiWRBNqA?t=1563) as the save/persistence boundary.

## 1. Before you open Power Apps

**🎧 Listen at [05:58](https://youtu.be/BvRKiWRBNqA?t=358)**

**Your goal is to understand a proposed design, not deploy an app.** The fictional SunnyVerse Solar Operations team needs one controlled review process for proposed solar sites, feasibility observations, internal permit packages and limited external comments. Internal reviewers decide whether the work may advance; an outside partner **must not** automatically see confidential assessments or attachments.

For an optional interface walkthrough, confirm:

- You can sign in to [Power Apps](https://make.powerapps.com/) and select an **approved development** environment, not production.
- That environment has **Dataverse** and the necessary maker privileges; Plans also depends on Copilot feature and regional eligibility. Some actions or technologies may require separate permissions or licensing.
- You will use only fictional content. Do not upload actual permits, private customer records or confidential process diagrams.

**If “Start with a plan” is missing:** first check the selected environment, Dataverse, maker role, region and feature entitlement. Do not assume the menu has merely moved.

## 2. Understand the three Plans agents

**🎧 Listen at [07:24](https://youtu.be/BvRKiWRBNqA?t=444)**

| Agent | Proposal to inspect | Key question |
|---|---|---|
| **Requirement Agent** | Roles, needs and business process | Is each participant accurately described and appropriately limited? |
| **Data Agent** | Suggested Dataverse tables, columns, types and relationships | Do the records and relationships fit the real process? |
| **Solution Agent** | Suggested apps, flows, sites or agents | Is each proposed technology justified by a validated user need? |

The agents propose. **People approve requirements and security boundaries.** A role in a planning diagram is **not** a configured security role; a relationship is **not** an access-control rule.

## 3. Start a plan with an effective solar scenario

**🎧 Listen at [08:15](https://youtu.be/BvRKiWRBNqA?t=495)**

If you have an eligible environment, the described navigation is:

1. Go to **Power Apps** → **Home**.
2. Select **Start with a plan** → **Create a plan**.
3. Enter a focused description in the plan text box; attach only safe, necessary context.
4. Choose **Generate** and inspect what the agents suggest. Generated results can differ from the examples below.

**Copy-ready SunnyVerse scenario — fictional:**

```text
SunnyVerse Solar Operations needs to track proposed solar sites,
gather feasibility observations and internal permit packages,
and coordinate review decisions. Internal Solar Operations
Reviewers decide whether a submission can move to the next stage.
An independent partner may submit comments only for site reviews
explicitly authorized for that partner. Confidential feasibility
findings and permit attachments must stay restricted to approved
internal personnel. Authorized owners must be able to view the
review status and relevant history. Propose the required user
roles, information structure, process and only the technologies
needed for this scope. Do not assume the external partner requires
broad Dataverse access or a public portal.
```

**Expected conceptual result:** a draft of roles and needs, followed by data and technology suggestions **after review**—not a published solution.

## 4. Review requirements before accepting them

**🎧 Listen at [10:10](https://youtu.be/BvRKiWRBNqA?t=610)**

Inspect the **Requirement Agent** output for an internal submitter, **Solar Operations Reviewer**, and limited external commenter *if appropriate*. Confirm that internal review decisions are assigned to authorized internal personnel.

- Select **Edit** to revise a role or need inline, add/delete a role or need, or adjust the order of needs.
- For broader corrections, supply **Copilot feedback**; inspect its proposal using **Review** or accept an appropriate revision using **Keep**, as available.
- Select **Looks good** **only after** the roles, needs and boundaries accurately reflect the intended process.

**Example correction if the AI suggests unrestricted contractor access:**

```text
Limit the external partner role to submitting comments on site
reviews explicitly authorized for that partner. Do not grant that
role access to internal feasibility findings, confidential permit
packages or unrelated site reviews. Keep advancement decisions
with approved Solar Operations Reviewers. Remove any requirement
that automatically shares all documents with external users.
```

**Check:** A suggested role now describes a **business need**, not a security guarantee. Real identity, table permissions and record-level access are separate implementation work in later modules.

## 5. Inspect and validate the process map

**🎧 Listen at [12:41](https://youtu.be/BvRKiWRBNqA?t=761)**

The requirements view may include a process diagram. Read it as a proposed workflow:

1. **Event:** a solar site review is submitted.
2. **Activity:** an internal reviewer checks the supporting information.
3. **Gateway:** are required internal checks complete?
4. **No:** return for missing information. **Yes:** an authorized reviewer considers moving the review forward.

Check that people and systems are assigned the right actions. The editor may allow adding/deleting events, activities or gateways and reconnecting nodes. **Validate changes before retaining them.** A diagram does not authorize a real installation or safety-critical action.

## 6. Inspect proposed Dataverse tables and relationships

**🎧 Listen at [15:42](https://youtu.be/BvRKiWRBNqA?t=942)**

After accepting requirements, the **Data Agent** proposes a model. Choose **Edit** to request changes or **Show details** to inspect its diagram and data workspace; return with **Back**. The source illustration uses:

| Possible table | What it represents | Important check |
|---|---|---|
| **Solar Site Review** | One proposed site and its review stage | Clear owner, review status and dates |
| **Permit Package** | Internal permit-related package linked to a site | Sensitivity and restricted access must be designed separately |
| **Contractor Comment** | Limited external feedback for an authorized site review | Must not imply access to every internal permit |

Look for sensible column types (a **date** for a review date; meaningful **status** values) and the correct record relationships. Do not assume generated names or schemas match any actual tenant. **Select Looks good** when the proposal is suitable. At this stage, a proposed model is not automatically a saved Dataverse table.

> **Scope boundary:** Detailed manual table, column and relationship configuration is taught from **Module 4** onward. Here, learn to judge the proposed model.

## 7. Examine the Solution Agent technology tiles

**🎧 Listen at [21:07](https://youtu.be/BvRKiWRBNqA?t=1267)**

Hover over each technology tile's **information** icon to see the roles and tables it addresses. Use **Edit** and Copilot feedback if a proposed component is unnecessary; **Looks good** accepts a suitable proposal.

| Potential component | Valid role in this example | Do not assume |
|---|---|---|
| **Model-driven app** | Internal review of related site and permit records | Forms, views and permissions are already verified |
| **Canvas app** | A focused task-oriented entry screen | Screens and behavior are production-ready |
| **Power Automate flow** | Notification after an authorized stage change | A draft flow grants business approval |
| **Power Pages** | A future external experience *only if justified* | External access is automatically secure |
| **Copilot Studio agent** | Authorized informational conversation *if needed* | Confidential data is safe to expose by default |
| **Power BI report** | Possible analytics recommendation | The plan instantly creates a complete verified report |

For a first iteration, an internal review app and a narrowly scoped notification may be sufficient. The presence of an external stakeholder does **not** require a portal.

## 8. Save tables only when authorized

**🎧 Listen at [26:03](https://youtu.be/BvRKiWRBNqA?t=1563)**

Saving is consequential: it moves from proposals toward objects in an environment. If you have reviewed the plan and are authorized to save it:

1. Select **Save tables**.
2. Enter a permitted solution name, for example `Solar_Feasibility_Review` (letters, numbers and underscores).
3. Choose the intended publisher **or** a suitable existing solution; verify the environment and selection.
4. Select **Save**, then inspect the plan's **Objects** view to identify what actually exists.

**Publisher naming:** `SunnyVerse Renewable Learning Publisher` and prefix `svrg` are **proposed educational configuration values only**. They apply only if that publisher is actually configured and selected. Do not assume schema names or modify an existing tenant's publisher settings to match an illustration. A Power Platform publisher is not the podcast publisher.

**Reality check:** Saving the plan/tables is **not** the same as creating, validating, sharing or publishing the proposed apps, flows, agent or website.

## 9. Share or export a reviewed plan

**🎧 Listen at [28:20](https://youtu.be/BvRKiWRBNqA?t=1700)**

**Collaboration:** use **Share** and choose **Viewer** (view only) or **Co-Owner** (use/edit/share within allowed boundaries). Underlying privileges still apply. Copresence can show multiple participants, but only **one editor at a time**; the documented cap is **up to 100** participants in the same plan experience.

**Stakeholder reading copy:** **Share → Export as a PDF** provides the document-side content, not every interactive diagram. It does not grant access to the underlying app or data.

## 10. Understand what each Create action starts

**🎧 Listen at [29:57](https://youtu.be/BvRKiWRBNqA?t=1797)**

After saving, a supported tile may offer **Create**. Know its starting point; do not treat it as a finished build:

- **Canvas app:** opens Power Apps Studio with a suggested starter; inspect data connections, controls and responsive behavior, then separately save/test/publish.
- **Model-driven app:** opens a designer with candidate tables; verify navigation, forms, views and privileges before publishing.
- **Power Automate:** opens a flow-creation experience using plan context; check triggers, conditions, connections and evidence of successful runs.
- **Copilot Studio agent:** opens an agent proposal; review instructions, knowledge access, identity and publication boundary.
- **Power Pages:** opens the site designer; additional administrative and Entra permissions may be required, and real website/table permissions must be configured independently.

These are **feature orientations**, not instructions to build five finished components in Module 3. Detailed implementation comes in later lessons.

## 11. Reuse applications and inspect Objects view

**🎧 Listen at [35:31](https://youtu.be/BvRKiWRBNqA?t=2131)**

**Reuse:** **Replace** can substitute an existing app for a proposed app. **Add technology** can include an existing app in the plan. This does **not** guarantee the app is moved into the new solution—check existing ownership and dependencies.

**Objects view:** review associated solution tabs and their components. **Only show objects in this plan** filters the view to plan-linked objects; turning it off can show additional solution contents. If an expected object is absent, save/refresh the view and verify it in its actual solution before concluding it was deleted.

## 12. Reverse the process: create a plan from a solution

**🎧 Listen at [38:27](https://youtu.be/BvRKiWRBNqA?t=2307)**

This is for **understanding** an existing app, not proof its current design is correct:

1. In **Power Apps**, open **Solutions**.
2. Choose **Create plan from a solution** (or select a solution → **Commands → Create a plan**).
3. Choose **Select solution**, select the intended solution, then **Create plan**.
4. Review the inferred requirements, data model and technologies; save only when appropriate.

The selected solution needs **at least one app and an associated table**. Avoid generating a reverse plan from a broad default solution. With an **unmanaged** solution, the plan may be saved in that solution; with a **managed** solution, it defaults to a **new unmanaged** solution. An inferred business rule needs owner confirmation.

## 13. Troubleshooting and completion checks

**🎧 Listen at [43:06](https://youtu.be/BvRKiWRBNqA?t=2586)**

| Situation | What to check first |
|---|---|
| Plans is unavailable | Environment, Dataverse, regional/Copilot eligibility, maker privileges |
| Generated contractor role has excessive access | Correct the *requirement*; later enforce actual security separately |
| Table relationships look plausible but expose sensitive records | Relationships are not permissions; redesign the access boundary |
| Too many technology tiles | Remove/defer unnecessary site or agent; require a clear use case |
| Objects appear missing | Save, refresh, check the correct solution and object filters |
| Sharing works for a plan but a user cannot see data | Separate plan-level share from underlying app/table authorization |

**You have understood Module 3 when you can explain** the three-agent sequence, review a proposed solar plan without accepting unsafe assumptions, distinguish draft versus saved objects, identify the purpose of **Create** and **Objects**, and describe the reverse-plan workflow. You have **not** been asked to deploy an app or implement security controls yet.

**Next in the course:** Module 4 — actual Dataverse tables and relationships.

---

### References and learner use

- [Twinkle & Celestyn — Module 3 video](https://youtu.be/BvRKiWRBNqA)
- [Microsoft Learn — Turn business ideas into solutions with Plans](https://learn.microsoft.com/en-us/training/modules/turn-business-ideas-power-platform-solutions-plans/)
- [Power Apps documentation — Create a plan](https://learn.microsoft.com/en-us/power-apps/maker/plan-designer/create-plan)
- [Power Apps documentation — Manage objects in a plan](https://learn.microsoft.com/en-us/power-apps/maker/plan-designer/manage-solution)
- [Power Apps documentation — Create a plan from an existing solution](https://learn.microsoft.com/en-us/power-apps/maker/plan-designer/create-plan-from-solution)
- [SunnyVerse Intelligent Applications course](https://sunnyverse.odoo.com/intelligent-applications)

*Original educational material by SunnyVerse AI Labs (independent educational YouTube/podcast brand). SunnyVerse Renewable Group and its sample records are fictional. Not affiliated with or endorsed by Microsoft. © 2026 SunnyVerse AI Labs. All rights reserved. This guide is not a substitute for verifying live product permissions and current documentation.*