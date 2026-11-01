# Dataverse Security Roles, Business Units & Teams | AB-410 M06

**SunnyVerse Intelligent Applications · Twinkle & Celestyn — Design & Troubleshooting Lab**  
▶️ **[Watch the Module 6 podcast](https://youtu.be/la3adbbAMtY)** · Runtime: approximately **1:02:21** · Learning path: **Dataverse foundations**

## How to follow this guide

**Start the video from the beginning.** When you reach a **⏸️ Pause & build** moment, pause YouTube, complete the matching actions in an **approved training environment**, check your result, then use **▶️ Resume** to continue. **👀 Watch & understand** sections explain security concepts without requiring configuration. Timestamps take you to the corresponding podcast passage.

> **Access changes are real security changes.** Do not experiment on production users, real employees, or customer data. Creating a role is possible only with appropriate administrative permissions. The examples use fictional SunnyVerse operations and an **existing, authorized organizational test account**. No real user or role change is claimed to have been tested on your tenant.

**What you will learn:** How environment access differs from Dataverse record access; how to prepare a limited `Solar Inspection Operator` role; how to assign it to an approved test user; and how to diagnose access without granting everyone administrator rights.

## Podcast chapter map

| Podcast time | Topic | Action |
|---|---|---|
| [00:00](https://youtu.be/la3adbbAMtY?t=0) | Why the solar inspection app needs security | 👀 Watch |
| [02:07](https://youtu.be/la3adbbAMtY?t=127) | Environments, identities, and Dataverse | 👀 Watch |
| [03:43](https://youtu.be/la3adbbAMtY?t=223) | Environment Admin and Environment Maker | 👀 Watch |
| [06:16](https://youtu.be/la3adbbAMtY?t=376) | Tenant administrator versus Dataverse administrator | 👀 Watch |
| [08:07](https://youtu.be/la3adbbAMtY?t=487) | Built-in roles and least privilege | 👀 Watch |
| [10:49](https://youtu.be/la3adbbAMtY?t=649) | Prerequisites for an authorized test identity | ✅ Check |
| [13:28](https://youtu.be/la3adbbAMtY?t=808) | Open Users in the Power Platform admin center | ⏸️ Pause & check |
| [14:13](https://youtu.be/la3adbbAMtY?t=853) | Add an already-provisioned test user if permitted | ⏸️ Optional |
| [17:57](https://youtu.be/la3adbbAMtY?t=1077) | Eight Dataverse table privileges | 👀 Watch |
| [21:37](https://youtu.be/la3adbbAMtY?t=1297) | Record access depths | 👀 Watch |
| [22:39](https://youtu.be/la3adbbAMtY?t=1359) | Business units are configured, not assumed | 👀 Watch |
| [25:30](https://youtu.be/la3adbbAMtY?t=1530) | Permission presets and other privileges | 👀 Watch |
| [28:33](https://youtu.be/la3adbbAMtY?t=1713) | Begin Solar Inspection Operator exercise | ✅ Check prerequisites |
| [29:47](https://youtu.be/la3adbbAMtY?t=1787) | Create the custom security role | ⏸️ Pause & build |
| [30:35](https://youtu.be/la3adbbAMtY?t=1835) | Business unit and privilege inheritance | ⏸️ Pause & check |
| [31:47](https://youtu.be/la3adbbAMtY?t=1907) | Save role and locate Solar Inspection | ⏸️ Pause & build |
| [32:18](https://youtu.be/la3adbbAMtY?t=1938) | Set the table privileges and narrow access depth | ⏸️ Pause & build |
| [36:26](https://youtu.be/la3adbbAMtY?t=2186) | Save and review the role | ✅ Verify |
| [36:52](https://youtu.be/la3adbbAMtY?t=2212) | Assign the role to Participant A | ⏸️ Pause & build |
| [39:00](https://youtu.be/la3adbbAMtY?t=2340) | Understand expected operator behavior | ✅ Verify |
| [41:13](https://youtu.be/la3adbbAMtY?t=2473) | Permissions from multiple roles add together | 👀 Watch |
| [42:45](https://youtu.be/la3adbbAMtY?t=2565) | Inspect effective roles and the user | ⏸️ Pause & check |
| [43:36](https://youtu.be/la3adbbAMtY?t=2616) | Run diagnostics | ⏸️ Optional |
| [44:26](https://youtu.be/la3adbbAMtY?t=2666) | Record-level Access Checker | ⏸️ Optional |
| [46:35](https://youtu.be/la3adbbAMtY?t=2795) | Owner teams | 👀 Watch |
| [47:26](https://youtu.be/la3adbbAMtY?t=2846) | Access teams | 👀 Watch |
| [48:28](https://youtu.be/la3adbbAMtY?t=2908) | Teams administration | 👀 / Optional |
| [49:48](https://youtu.be/la3adbbAMtY?t=2988) | Microsoft Entra group teams | 👀 Watch |
| [52:37](https://youtu.be/la3adbbAMtY?t=3157) | Team privilege inheritance | 👀 Watch |
| [54:00](https://youtu.be/la3adbbAMtY?t=3240) | Group membership and offboarding | 👀 Watch |
| [56:00](https://youtu.be/la3adbbAMtY?t=3360) | Access scenarios and troubleshooting | 👀 Watch |
| [60:00](https://youtu.be/la3adbbAMtY?t=3600) | Final takeaways and transition | 👀 Watch |

## 1. Prepare your training environment and table

**✅ Check before the practical section at [28:33](https://youtu.be/la3adbbAMtY?t=1713).** You can perform this preparation before playing the episode if you want to work alongside it without interruptions.

### Required starting state

- An **approved development/training Power Platform environment with Dataverse**.
- Administrator or appropriately delegated privileges to **create and assign Dataverse security roles**. Without these, follow the explanation rather than attempting real changes.
- An existing custom Dataverse table named **`Solar Inspection`**, configured with **User or team** ownership for the narrow row-access demonstration.
- An already-provisioned and permitted organizational test account, called **`Participant A`** in the lesson. `Reviewer B` is another illustrative supervisor identity, **not** an account you should invent or create.
- If testing through an app, that app must already exist and be appropriately shared. **This module does not ask you to build the solar inspection app.**

### If you do not have `Solar Inspection`

**One-time preparation, not an activity demonstrated in the podcast:** Modules 4 and 5 used other tables; they did **not** create this particular one. To avoid getting stuck:

1. In [Power Apps](https://make.powerapps.com/), select your **approved learning environment**.
2. Open your suitable learning **solution** (or an approved customizations workspace), then select **New → Table**.
3. Use **Display name:** `Solar Inspection`; **Plural name:** `Solar Inspections`; **Table type:** Standard.
4. Set **Ownership** to **User or team** during creation. This selection is important because ownership type generally cannot be changed later.
5. Keep the default primary name column unless your tenant requires different training conventions. **Save**, then confirm the new table appears.
6. Do **not** invent extra inspection columns, real employee identities, a dedicated solar business unit, or a live app as prerequisites. They are not needed simply to practice configuring the role.

**✅ Check:** The table exists in the right environment and is **User or team-owned**. If it was created as organization-owned, its row-depth choices may not match the podcast example; use an appropriate learning table rather than assuming you can switch ownership in place. The new table uses the actual publisher/schema prefix configured in your solution—do not assume `svrg` applies automatically.

**▶️ [Start the podcast from 00:00](https://youtu.be/la3adbbAMtY?t=0)**, or continue from your current position.

## 2. Understand the access layers

**👀 Watch [02:07](https://youtu.be/la3adbbAMtY?t=127)–[10:49](https://youtu.be/la3adbbAMtY?t=649). No changes required.**

| Layer | What it answers | What it does **not** guarantee |
|---|---|---|
| Microsoft Entra identity and licensing | Is the account valid and eligible to sign in? | Read access to a Solar Inspection row |
| Environment admission and maker/admin roles | May the user enter or build in this environment? | Every Dataverse table privilege |
| Dataverse security role | Which operations and access depths may apply? | Automatic visibility of every specific record |
| Ownership, business unit, sharing, and teams | Which rows qualify for the permitted operation? | The app's screen shows every permitted row |
| App sharing and view configuration | Can the user open and navigate the app? | Underlying data privileges |

**Key point:** Being a tenant-level Power Platform administrator, Environment Maker, or app user does not automatically make someone a Dataverse **System Administrator**. Give an inspection operator only the approved capabilities needed for the job.

## 3. Find an authorized test user

**⏸️ Pause at [13:28 — Users administration](https://youtu.be/la3adbbAMtY?t=808).**

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/) with **authorized administrative permissions**.
2. Open **Manage → Environments**, select the intended **training environment**, and open **Settings**.
3. Expand **Users + permissions → Users**.
4. Find the actual approved test account representing `Participant A`. The displayed name can differ from the fictional label.
5. If the user is not listed and you are authorized, follow the **Add user** flow around **[14:13](https://youtu.be/la3adbbAMtY?t=853)**: search for the **already-provisioned organizational identity**, select it, and confirm **Add**. Eligibility depends on sign-in status, licensing, environment security-group rules, and provisioning.

**✅ Check:** The account appears in the environment's **Users** list. This does **not** mean it can read or write Solar Inspection data.

**▶️ [Resume at 17:57 — Table privileges](https://youtu.be/la3adbbAMtY?t=1077).**

## 4. Know the eight table privileges and access depths

**👀 Watch [17:57](https://youtu.be/la3adbbAMtY?t=1077)–[28:33](https://youtu.be/la3adbbAMtY?t=1713).**

| Privilege | Meaning |
|---|---|
| **Create** | Add records |
| **Read** | View qualifying records |
| **Write** | Update qualifying records |
| **Delete** | Delete qualifying records |
| **Append** | Allow records to be attached to another record |
| **Append To** | Allow other records to be linked to this record |
| **Assign** | Change record ownership |
| **Share** | Grant access to others |

For **user- or team-owned** tables, privilege depths commonly progress from **None → User → Business Unit → Parent:Child Business Units → Organization**. The broader depths can expose more records. **User depth is not automatically the same as “assigned to a particular solar site”**; ownership and sharing still matter.

A business unit is an **actual configured Dataverse security boundary**. The fictional department name *SunnyVerse Solar Operations* does **not** prove that a matching Dataverse business unit exists. If your designer offers presets like **Private, Collaborate, Reference, Full Access**, inspect the resulting granular privileges rather than assuming the preset is sufficient. Other permissions, including export, also deserve review.

## 5. Create `Solar Inspection Operator`

**⏸️ Pause at [29:47 — New security role](https://youtu.be/la3adbbAMtY?t=1787).** This is the main guided configuration.

1. In the **same training environment** in the Power Platform admin center, open **Settings → Users + permissions → Security roles**.
2. Select **New role** (some interfaces show **+ New role**).
3. Enter the exact **Role name**:

   ```text
   Solar Inspection Operator
   ```

4. Enter this description, matching the podcast's stated purpose:

   ```text
   Supports limited inspection entry and review for approved solar operators.
   ```

5. Select the **actual business unit** listed in your training environment. Do **not** create a fictional business unit merely to match the story.
6. Inspect **Member's privilege inheritance**, which may present **Team privileges only** or **Direct User Basic access plus Team privileges**. The lesson intends a direct user assignment; choose with your administrator's direction and note the visible setting. A group-assignment design may behave differently.
7. If your current role editor presents additional optional metadata fields, enter truthful, minimal descriptions. Choose **Save** to establish the role before configuring table permissions.

**✅ Check:** The new role exists, and you can enter its privilege designer.

**▶️ [Resume at 32:18 — Find Solar Inspection](https://youtu.be/la3adbbAMtY?t=1938).**

## 6. Configure table permissions carefully

**⏸️ Pause at [32:18 — Solar Inspection privileges](https://youtu.be/la3adbbAMtY?t=1938).**

1. Search the security-role privilege designer for **`Solar Inspection`** and select the correct custom table (inspect schema details if names collide).
2. For an operator who creates and updates **their own** inspection records, consider the narrowest valid depths for **Create, Read, and Write**. **User** depth can be appropriate for a user/team-owned table with suitable ownership; it is an **example**, not a universal permission specification for every tenant.
3. **Do not grant Delete, Assign, or Share** unless your authorized training scenario explicitly requires them.
4. Configure **Append** and **Append To** only if you are actually connecting related records. Linked tables such as a Solar Asset may also require their own Read or Append To privileges.
5. Check baseline privileges needed to run the specific app. A completely new role can lack minimum platform permissions. An administrator may use a suitable restricted starting role or complementary minimum roles; **do not “fix” app access by granting System Administrator**.
6. Reinspect every selected privilege and access depth, then choose **Save** or **Save and Close** at approximately **[36:26](https://youtu.be/la3adbbAMtY?t=2186)**.

**✅ Check:** `Solar Inspection Operator` exists with deliberately limited privileges. **The podcast does not prescribe one universally exact depth for every permission**, so don't treat a particular setting as verified merely because you selected it. Document the intended ownership rule and have the appropriate administrator confirm it.

**▶️ [Resume at 36:52 — Assign the role](https://youtu.be/la3adbbAMtY?t=2212).**

## 7. Assign the role to the approved test account

**⏸️ Pause at [36:52 — Role membership](https://youtu.be/la3adbbAMtY?t=2212).**

**Route A — From Security roles (where available):**

1. Go back to **Security roles** and find `Solar Inspection Operator`.
2. On the role **row**, choose **More actions (⋯) → Members** if this option is shown. Selecting the role *name* may open its designer instead.
3. Choose **Add people**, find the approved user representing `Participant A`, select and confirm **Add**.

**Route B — From Users (alternate interface):**

1. Go to **Users**, select the approved test account, and choose **Manage security roles**.
2. Select `Solar Inspection Operator` and **Save**.

**✅ Check:** The intended test account has the role in the **correct environment**. If the identity cannot be found, verify that it is provisioned, enabled, licensed, and eligible for the environment—never manufacture an account or assign a real employee's identity for convenience.

**▶️ [Resume at 39:00 — Expected behavior](https://youtu.be/la3adbbAMtY?t=2340).**

## 8. Validate access without assuming a live test passed

**✅ Inspect as you hear [39:00](https://youtu.be/la3adbbAMtY?t=2340)–[44:26](https://youtu.be/la3adbbAMtY?t=2666).**

| Expected condition | What to verify in your environment |
|---|---|
| An operator creates an inspection | Has the account been admitted, assigned a suitable role, and granted needed Create rights? |
| An operator reads or changes a row | Do Read/Write privileges, ownership, sharing, and related tables allow that **specific record**? |
| Another operator's record is not visible | Could it be the expected result of narrow User-depth rights? |
| Delete is not granted by the custom role | **Check all other roles and teams**: absence in one role is not a global deny |
| The app opens but displays no rows | Check sharing, role, ownership, filters, views, and protected columns separately |

**Administrator tools explained in the episode:**

- Around **[42:45](https://youtu.be/la3adbbAMtY?t=2565)**: **Users → select account → Roles / Manage security roles** to inspect the **complete** effective role assignments.
- Around **[43:36](https://youtu.be/la3adbbAMtY?t=2616)**: **Run diagnostics** (where available) for identity, license, group, and role prerequisites.
- Around **[44:26](https://youtu.be/la3adbbAMtY?t=2666)**: **Access Checker** on a suitable model-driven app record can explain access through role privileges, ownership, sharing, or hierarchy when available and authorized.

**No fictional success claim:** The expected effects above must be independently checked in your own training environment. The podcast does not demonstrate that a real tenant test succeeded.

**▶️ [Resume at 46:35 — Teams](https://youtu.be/la3adbbAMtY?t=2795).**

## 9. Understand teams before configuring one

**👀 Watch [46:35](https://youtu.be/la3adbbAMtY?t=2795)–[54:00](https://youtu.be/la3adbbAMtY?t=3240).** This is a feature walkthrough, **not** a requirement to create multiple live teams.

| Team type | Can own records? | Can have Dataverse security roles? | Typical use |
|---|---|---|---|
| **Owner team** | Yes | Yes | Shared ownership and controlled group permissions |
| **Access team** | No | No | Selected-record collaboration through sharing |
| **Microsoft Entra group team** | Yes (owner-team style) | Yes | Membership managed from an existing Entra group |

If your administrator is practicing team configuration, the discussed navigation is **Power Platform admin center → Manage → Environments → [training environment] → Settings → Users + permissions → Teams → Create team**. Choose a legitimate business unit, team type, existing members/Entra group where needed, and only the appropriate security roles. An **Access team cannot receive the `Solar Inspection Operator` role** like an owner team can.

**Membership inheritance matters:** Under **Team privileges only**, team membership alone may not let a member create user-owned records. The alternate **Direct User Basic access plus Team privileges** mode can convey additional user-level privileges from the team role. Test and approve the design rather than changing inheritance blindly.

**▶️ [Resume at 54:00 — Identity lifecycle](https://youtu.be/la3adbbAMtY?t=3240).**

## 10. Review offboarding and three common failures

**👀 Watch [54:00](https://youtu.be/la3adbbAMtY?t=3240) to the end.**

- **Removed from an Entra group, but still has access:** Check other directly assigned roles, team memberships, sharing, licensing, and identity state. A group change alone doesn't prove all access paths are gone.
- **Cannot see a record owned by `Reviewer B`:** Check the operator's Read privilege depth, row owner, business unit, team grants, and explicit sharing. Restricting that record may be the *correct* outcome.
- **Can delete even though the custom role has no Delete:** Roles are **additive**. Review other effective roles and associated grants before assuming the custom role designer failed.
- **Access Checker permits Read but the app view is blank:** Look at app filters, view configuration, column restrictions, and possible refresh problems. Data authorization and what a screen displays are separate questions.

## Completion check

You are ready to move to the next module when you can:

- [ ] Explain why environment membership does not confer Dataverse record access.
- [ ] Identify the actual `Solar Inspection` table and a permitted test identity.
- [ ] Describe the eight privileges and narrow versus broad access depths.
- [ ] Find, create, save, and assign `Solar Inspection Operator` **if authorized**.
- [ ] Explain why a role with Delete unset does not guarantee the user is unable to delete through another role.
- [ ] Distinguish owner teams, access teams, and Microsoft Entra group teams.
- [ ] Identify appropriate diagnostics without simply increasing permissions.

**Next in the course:** Canvas applications (Module 7). Secure data permissions still apply even when an app has a simple interface.

---

### Resources

- [▶️ Module 6 podcast — Twinkle & Celestyn](https://youtu.be/la3adbbAMtY)
- [Microsoft Learn — Dataverse security concepts](https://learn.microsoft.com/en-us/training/modules/get-started-security-concepts/)
- [Microsoft Learn — Create or edit a security role](https://learn.microsoft.com/en-us/power-platform/admin/create-edit-security-role)
- [Microsoft Learn — Security roles, privileges and access levels](https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds)
- [Microsoft Learn — Manage Dataverse teams](https://learn.microsoft.com/en-us/power-platform/admin/manage-teams)
- [SunnyVerse Intelligent Applications course](https://sunnyverse.odoo.com/intelligent-applications)

*© 2026 SunnyVerse AI Labs. Independently authored learner companion. SunnyVerse Renewable Group and sample records are fictional. Not affiliated with or endorsed by Microsoft. Product interfaces, feature availability, licensing, and administrative permissions may change.*