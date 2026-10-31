# Power Apps Plans: Turn Ideas into App Designs | AB-410 M03

**SunnyVerse Intelligent Applications — Twinkle & Celestyn · Design & Troubleshooting Lab**

▶️ **[Watch the Module 3 podcast on YouTube](https://youtu.be/BvRKiWRBNqA)** · Duration: approximately 47:18

## How to follow along

This guide works alongside the podcast. **Start the video from the beginning.** When you reach a section marked **⏸️ Pause & try**, pause YouTube and follow the steps in Power Apps. Check the result, then **▶️ resume the video** from the timestamp linked at the end of that section. If you are returning later, click any chapter timestamp to jump directly to the corresponding part.

Some sections say **👀 Watch & understand**. Those explain how the feature works; you do not need to pause or create anything for them.

Use only a development or learning environment where you have permission. The solar review data below is fictional. **Save tables** and other creation actions can change your environment; take those steps only if you intend to save practice objects. You can still learn the planning flow by watching if Plans is unavailable in your account.

> **What you will achieve:** Follow a SunnyVerse Solar Operations example from an initial business request through reviewed requirements, a proposed data model, technology choices, and possible saved objects. A plan is not automatically a tested, secure, or published application.

## Jump to a podcast moment

| Podcast time | What happens | Guide |
|---|---|---|
| [00:00](https://youtu.be/BvRKiWRBNqA?t=0) | Why business needs come first | Watch |
| [02:05](https://youtu.be/BvRKiWRBNqA?t=125) | Solar Operations scenario | Watch |
| [04:14](https://youtu.be/BvRKiWRBNqA?t=254) | A plan is not a finished app | Watch |
| [05:58](https://youtu.be/BvRKiWRBNqA?t=358) | Check prerequisites and environment | Pause & check |
| [06:33](https://youtu.be/BvRKiWRBNqA?t=393) | Open Power Apps and start a plan | Pause & try |
| [07:24](https://youtu.be/BvRKiWRBNqA?t=444) | Three planning agents | Watch |
| [08:15](https://youtu.be/BvRKiWRBNqA?t=495) | Describe the solar-review problem | Pause & try |
| [10:10](https://youtu.be/BvRKiWRBNqA?t=610) | Review generated requirements | Pause & check |
| [11:28](https://youtu.be/BvRKiWRBNqA?t=688) | Correct inaccurate or unsafe roles | Pause & try |
| [12:41](https://youtu.be/BvRKiWRBNqA?t=761) | Inspect the process map | Pause & check |
| [15:42](https://youtu.be/BvRKiWRBNqA?t=942) | Inspect proposed tables and columns | Pause & check |
| [18:22](https://youtu.be/BvRKiWRBNqA?t=1102) | Why relationships are not permissions | Watch |
| [20:02](https://youtu.be/BvRKiWRBNqA?t=1202) | Review and revise relationships | Pause & check |
| [21:07](https://youtu.be/BvRKiWRBNqA?t=1267) | Review technology recommendations | Pause & check |
| [23:45](https://youtu.be/BvRKiWRBNqA?t=1425) | Remove an unnecessary external portal | Pause & try |
| [25:07](https://youtu.be/BvRKiWRBNqA?t=1507) | Power BI recommendation versus built report | Watch |
| [26:03](https://youtu.be/BvRKiWRBNqA?t=1563) | Save tables and choose a solution | Optional save |
| [28:20](https://youtu.be/BvRKiWRBNqA?t=1700) | Share a plan | Watch / optional |
| [29:23](https://youtu.be/BvRKiWRBNqA?t=1763) | Export a plan to PDF | Watch / optional |
| [29:57](https://youtu.be/BvRKiWRBNqA?t=1797) | What each Create action starts | Watch |
| [35:31](https://youtu.be/BvRKiWRBNqA?t=2131) | Reuse an existing app | Watch / optional |
| [36:21](https://youtu.be/BvRKiWRBNqA?t=2181) | Inspect Objects view | Pause & check |
| [38:27](https://youtu.be/BvRKiWRBNqA?t=2307) | Create a plan from an existing solution | Watch / optional |
| [43:06](https://youtu.be/BvRKiWRBNqA?t=2586) | Review and troubleshooting | Watch |

## 1. Check your Power Apps environment

**⏸️ Pause the video when you reach [05:58 — Environment checks](https://youtu.be/BvRKiWRBNqA?t=358).**

Before opening Power Apps, check the following:

1. You can sign in to [Power Apps](https://make.powerapps.com/).
2. You have an **approved development environment**, rather than a production environment.
3. The environment has **Dataverse** and suitable maker permissions. Plans also depends on regional and Copilot feature eligibility; other technology choices can require further licensing and permissions.
4. You will enter only fictional learning data—no real permits, customer information, or confidential diagrams.

**Check your result:** You have identified an appropriate environment. If **Start with a plan** is unavailable, check environment selection, Dataverse, maker rights, region, and eligibility. You can continue watching without performing the optional steps.

**▶️ [Resume the podcast at 06:33](https://youtu.be/BvRKiWRBNqA?t=393).**

## 2. Open Power Apps and begin a plan

**⏸️ Pause when you reach [06:33 — Start with a plan](https://youtu.be/BvRKiWRBNqA?t=393).**

If Plans is available to you:

1. Open [Power Apps](https://make.powerapps.com/) and confirm your development environment.
2. From **Home**, select **Start with a plan**.
3. Choose **Create a plan**.
4. Find the box where you can describe your business process. You will enter the example at the next practice point.

**Check your result:** You have reached the plan description area. You have not yet generated or saved an app.

**▶️ [Resume at 07:24](https://youtu.be/BvRKiWRBNqA?t=444)** to understand the agents before entering your request.

## 3. Understand the three planning agents

**👀 Continue watching at [07:24 — Planning agents](https://youtu.be/BvRKiWRBNqA?t=444). No pause needed.**

| Agent | What it proposes | What you need to inspect |
|---|---|---|
| **Requirement Agent** | User roles, needs, and business process | Does each person have the appropriate responsibility and boundaries? |
| **Data Agent** | Dataverse tables, columns, types, and relationships | Does the proposed model represent the work accurately? |
| **Solution Agent** | Suggested apps, flows, websites, or agents | Is each component justified by a real need? |

An AI-proposed role is not an actual security role, and a table relationship does not enforce authorization.

## 4. Describe the SunnyVerse Solar Operations problem

**⏸️ Pause at [08:15 — Describe the business problem](https://youtu.be/BvRKiWRBNqA?t=495).**

In your open plan description box, enter the fictional example below:

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

Then select **Generate** if you are following along in an eligible environment.

**Check your result:** The plan should propose requirements and user needs for review. Exact wording and suggestions may vary. Do not assume the proposal is accurate or secure.

**▶️ [Resume at 10:10](https://youtu.be/BvRKiWRBNqA?t=610)** to review the suggestions with Twinkle and Celestyn.

## 5. Review requirements and correct unsafe suggestions

**⏸️ Pause at [10:10 — Requirements review](https://youtu.be/BvRKiWRBNqA?t=610).**

Inspect the proposed roles and needs. A reasonable result could include an internal submitter, a **Solar Operations Reviewer**, and a limited outside commenter. Reviewers—not a proposed AI agent—must retain responsibility for business approval.

When the video reaches **[11:28 — Editing roles](https://youtu.be/BvRKiWRBNqA?t=688)**, try the correction controls if needed:

1. Choose **Edit** to revise roles or needs inline, including adding or deleting them.
2. For a broader correction, use **Copilot feedback** to describe the desired change.
3. Review proposed changes through **Review** or **Keep**, as applicable.
4. Select **Looks good** only after the requirements accurately describe the business process and access boundaries.

If the proposal suggests unrestricted contractor access, this fictional correction is ready to copy:

```text
Limit the external partner role to submitting comments on site
reviews explicitly authorized for that partner. Do not grant that
role access to internal feasibility findings, confidential permit
packages or unrelated site reviews. Keep advancement decisions
with approved Solar Operations Reviewers. Remove any requirement
that automatically shares all documents with external users.
```

**Check your result:** No suggested business requirement grants outside participants broad access to confidential information. These requirements do not themselves configure security; actual permissions must be designed and tested separately.

**▶️ [Resume at 12:41](https://youtu.be/BvRKiWRBNqA?t=761)** to examine the process diagram.

## 6. Examine the proposed process diagram

**⏸️ At [12:41 — Process map](https://youtu.be/BvRKiWRBNqA?t=761), pause if you want to compare the diagram with the guide.**

The planning diagram may represent the solar review as:

1. **Event:** someone submits a site review.
2. **Activity:** an internal reviewer checks supporting information.
3. **Gateway:** are required checks complete?
4. **No:** request missing information. **Yes:** an authorized reviewer considers advancing the review.

Check each step's owner and direction. The editor may let you add or remove events, activities, and gateways and reconnect nodes. Validate any changes before retaining them. A process diagram cannot approve a real solar installation or an operational safety decision.

**Check your result:** The proposed process contains an explicit human review decision and does not treat an external comment as authorization.

**▶️ [Resume at 15:42](https://youtu.be/BvRKiWRBNqA?t=942)** for the proposed data model.

## 7. Review the suggested Dataverse data model

**⏸️ Pause at [15:42 — Data Agent](https://youtu.be/BvRKiWRBNqA?t=942).**

After accepting requirements, the **Data Agent** can suggest tables, columns, data types and relationships. Use **Show details** to examine the diagram or **Edit** to revise the proposal. The example might contain:

| Proposed table | Purpose | Verify |
|---|---|---|
| **Solar Site Review** | One proposed site and its review state | Status, owner, relevant dates |
| **Permit Package** | An internal package associated with a site | Restricted handling and correct link |
| **Contractor Comment** | Feedback for a specifically authorized review | No broad permit access implied |

Check that dates use appropriate types, statuses reflect meaningful stages, and relationships point to the correct records. At **[20:02 — Revising relationships](https://youtu.be/BvRKiWRBNqA?t=1202)**, review possible structural corrections before choosing **Looks good**.

**Check your result:** The data model fits the work, but is still a **proposal** until the appropriate save action creates actual Dataverse objects. Relationships are not security permissions. You will learn detailed table construction in Module 4.

**▶️ [Resume at 21:07](https://youtu.be/BvRKiWRBNqA?t=1267)** for technology choices.

## 8. Review the suggested Power Platform technologies

**⏸️ Pause at [21:07 — Solution Agent recommendations](https://youtu.be/BvRKiWRBNqA?t=1267).**

Inspect each technology tile and its information icon to understand which roles and tables it supports. Consider the business need—not how many products can be added.

| Proposed component | Possible role | Important distinction |
|---|---|---|
| **Model-driven app** | Internal review of related site, permit, and comment records | Not yet tested or published |
| **Canvas app** | A focused task-entry screen | Usability and data access need validation |
| **Power Automate** | Notifications after authorized status changes | A flow does not replace approval authority |
| **Power Pages** | A partner-facing experience if justified | External authorization is separate |
| **Copilot Studio** | Authorized informational questions, if needed | Data exposure requires evaluation |
| **Power BI** | An analytical reporting option | A recommendation is not an automatically built report |

At **[23:45 — Unnecessary contractor portal](https://youtu.be/BvRKiWRBNqA?t=1425)**, check whether Power Pages is really necessary. If not, choose **Edit**, request the adjustment using Copilot, inspect the updated recommendations, and use **Looks good** only when appropriate.

**Check your result:** Every retained technology has a clear user or process purpose. A secure internal app and a small notification flow may be enough initially.

**▶️ [Resume at 26:03](https://youtu.be/BvRKiWRBNqA?t=1563)** for the save boundary.

## 9. Save tables — only in an approved practice environment

**⏸️ Pause at [26:03 — Save tables](https://youtu.be/BvRKiWRBNqA?t=1563).**

**This step can create real Dataverse components.** Perform it only if you have permission and want practice objects saved in the selected development environment; otherwise keep watching without saving.

1. Review the chosen environment and your proposed data model once more.
2. Select **Save tables**.
3. Use an appropriate example solution name such as `Solar_Feasibility_Review`.
4. Choose the correct publisher or existing solution for your environment, then select **Save**.
5. Inspect **Objects** to see which components actually exist.

**Naming note:** `SunnyVerse Renewable Learning Publisher` and prefix `svrg` are illustrative. Use those values only if the publisher has actually been configured and selected; never assume they are already present.

**Check your result:** You can distinguish a *suggested table* from a *saved Dataverse object*. Saving tables does not create and publish every suggested application, flow, agent, website, or report.

**▶️ [Resume at 28:20](https://youtu.be/BvRKiWRBNqA?t=1700)** for collaboration.

## 10. Understand sharing and exporting a plan

**👀 Watch [28:20 — Sharing](https://youtu.be/BvRKiWRBNqA?t=1700) and [29:23 — PDF export](https://youtu.be/BvRKiWRBNqA?t=1763).**

If you have a saved practice plan and appropriate permissions, you may inspect these options:

- **Share** allows **Viewer** or **Co-Owner** access within the product's permissions. A user still requires necessary underlying access.
- Multiple participants may view the plan, but only one edits at a time. The documented shared-presence cap discussed in the episode is up to 100.
- **Export as a PDF** produces a readable plan document, not every interactive diagram, and does not grant access to apps or underlying records.

**▶️ [Continue at 29:57](https://youtu.be/BvRKiWRBNqA?t=1797).**

## 11. Understand what Create does

**👀 Watch at [29:57 — Technology Create actions](https://youtu.be/BvRKiWRBNqA?t=1797). No need to build every component here.**

A saved technology tile can expose **Create**. The episode explains what that starts:

- **Canvas app:** a starter in Power Apps Studio; save, test and publish separately.
- **Model-driven app:** a designer using candidate Dataverse tables; inspect navigation, forms, views and permissions.
- **Power Automate:** a flow proposal; verify trigger, actions, connections, conditions and run results.
- **Copilot Studio:** an agent setup with proposed instructions and sources; review identity and access before publishing.
- **Power Pages:** a site designer, potentially requiring additional administrative and Microsoft Entra privileges and separate authorization design.

**Check your understanding:** A generated starting point is not a production-ready application. Detailed app and automation builds are covered in later modules.

**▶️ [Continue at 35:31](https://youtu.be/BvRKiWRBNqA?t=2131).**

## 12. Review existing apps and the Objects view

**👀 Watch [35:31 — Reusing an app](https://youtu.be/BvRKiWRBNqA?t=2131)** to understand **Replace** and **Add technology**. They can reference an existing app without necessarily moving it into the new solution.

**⏸️ At [36:21 — Objects view](https://youtu.be/BvRKiWRBNqA?t=2181)**, pause if you saved a practice plan and want to inspect its components:

1. Open **Objects** and examine the associated solution tabs.
2. Use **Only show objects in this plan** to narrow the view.
3. Turn that filter off to see other contents of associated solutions.
4. If an expected object is missing, save and refresh the view, then inspect the actual solution before assuming the object was lost.

**Check your result:** You understand which objects belong to the plan and which may already exist in other solutions.

**▶️ [Resume at 38:27](https://youtu.be/BvRKiWRBNqA?t=2307).**

## 13. Learn the reverse workflow: plan from an existing solution

**👀 Watch [38:27 — Create a plan from a solution](https://youtu.be/BvRKiWRBNqA?t=2307).**

If you already have a suitable practice solution, you may explore this separate workflow:

1. In **Power Apps**, open **Solutions**.
2. Select **Create plan from a solution**; alternatively select the solution and use **Commands → Create a plan**.
3. Use **Select solution**, choose the solution, and then **Create plan**.
4. Inspect the generated interpretation of requirements, data, and technologies. Save only if appropriate.

The selected solution requires at least **one app and an associated table**. Avoid selecting a broad default solution. For an unmanaged solution, the plan can be saved there; for a managed solution, the documented default is a new unmanaged solution.

**Check your understanding:** A reverse-generated plan describes an existing design; it does not independently verify the original business rules or fix incorrect permissions.

**▶️ [Resume at 43:06](https://youtu.be/BvRKiWRBNqA?t=2586)** for the recap.

## 14. Final review and troubleshooting

**👀 Watch the conclusion from [43:06](https://youtu.be/BvRKiWRBNqA?t=2586) to the end.**

| If you encounter this | Check this first |
|---|---|
| **Start with a plan** is unavailable | Environment, Dataverse, maker rights and regional eligibility |
| Contractor requirements are too broad | Edit the business requirement; implement actual permissions separately |
| Table relationships appear correct but access is uncertain | Relationships do not enforce access rights |
| Too many suggested technologies | Remove or defer those without a clear need |
| A saved object does not appear in Objects view | Save, refresh and check the underlying solution |
| Someone can open a plan but not its data | Plan sharing and data authorization are separate |

**Module 3 complete:** You can explain the sequence from business request → reviewed requirements → proposed data model → reviewed technology choices → optionally saved objects, and recognize the separate reverse-planning workflow.

**Coming next:** Module 4 — Dataverse tables and relationships.

---

### Resources

- [Watch Module 3 — Twinkle & Celestyn](https://youtu.be/BvRKiWRBNqA)
- [Microsoft Learn — Turn business ideas into solutions with Plans](https://learn.microsoft.com/en-us/training/modules/turn-business-ideas-power-platform-solutions-plans/)
- [Power Apps — Create a plan](https://learn.microsoft.com/en-us/power-apps/maker/plan-designer/create-plan)
- [Power Apps — Manage objects in a plan](https://learn.microsoft.com/en-us/power-apps/maker/plan-designer/manage-solution)
- [Power Apps — Create a plan from an existing solution](https://learn.microsoft.com/en-us/power-apps/maker/plan-designer/create-plan-from-solution)
- [SunnyVerse Intelligent Applications course](https://sunnyverse.odoo.com/intelligent-applications)

*© 2026 SunnyVerse AI Labs. Original independent educational material. SunnyVerse Renewable Group and the scenarios here are fictional. Not affiliated with or endorsed by Microsoft. Product interfaces, licensing, permissions and availability can change.*
