# DC360 — End-to-End Portfolio Demonstration

[Build Guide](../Build-Guide.md#part-16--present-and-verify-the-complete-data-center-operations-360-project) · [Case study](./Case-Study.md) · [Evidence](./Evidence-Matrix.md)

This is a **read-only, evidence-led demonstration route** through the fictional SunnyVerse Renewable Group environment. It is appropriate for a short portfolio walkthrough or interview. It is not a physical-facility operating procedure. Only demonstrate an action as “live” if you actually performed it in the authorized environment during that session.

## Preflight — before any screen recording

- Open the correct authorized **existing** solution; confirm currently published app versions from actual metadata.
- Use fictional source records. Hide tenant addresses, environment identifiers, signed-in profile menus, URLs, connection references, test-recipient values and private local paths.
- Do **not** run Off flows, send messages, change approvals, create incident/work-order rows or submit capacity requests just for the recording.
- Keep the **original unmanaged solution ZIP**, its checksum and private implementation reports outside GitHub/video capture.
- Clear Canvas app and Power BI visual filters before claiming baseline counts.
- If a page cannot be opened, label it **Not demonstrated**, keep the script moving and disclose the limitation.

## Suggested twelve-scene walkthrough (12–18 minutes)

| Scene | Screen / source | Safe action | Evidence / story point | Explicit boundary |
| --- | --- | --- | --- | --- |
| 1 | GitHub project README and Build Guide | Show published learning structure | Reproducible, cumulative source-first engineering | Publishing a guide ≠ deployed app |
| 2 | Architecture diagram | Follow data/trust boundaries | Dataverse operations separate from CSV/Power BI learning telemetry | No live sensor integration |
| 3 | Power Apps solution Overview | Inspect component types and publisher | Shared solution structure and consistent naming | Hide tenant metadata |
| 4 | Data Hall → Asset → Sensor | Open saved fictional parent/child records | Real Dataverse Lookups | No GUID copying into text substitutes |
| 5 | DC Operations Command Center | Open published Home, read existing counts and recent incidents | Incident/alarm operational overview | Counts must be confirmed on the exact version |
| 6 | DC FieldOps | Read existing inspection or assignment screens | Mobile field-engineering workflow | No new evidence, uploads or status writes |
| 7 | DC Asset & Maintenance Manager | Open existing Asset/Work Order records | Record lifecycle and operational context | 500 source CSV rows vs an extra practice record |
| 8 | DC Change & Risk Manager | Read saved change/MOP/risk review record | Workflow governance and audit boundaries | Mock approvals are not real permit signatures |
| 9 | DC Supporting Operations Hub | Inspect inventory/handover and intelligence sections | Supplier/inventory coordination and evidence-linked insights | Reorder flag is manually maintained |
| 10 | DC Capacity Planner | Read two Hall Baselines and existing rack/allocations | 42U rack model, planned headroom, holds and requests | Client-side validation is not a server lock |
| 11 | Power BI Desktop report | Reopen local PBIX if available; clear selections and show five pages | 50,000 samples, 24 sensors, 7 tables, 6 relationships, 20 measures | Not Power BI Service / not real-time |
| 12 | Engineering checklist and case study | Summarize private QA statuses in privacy-safe terms | Transparent release gates and development-source export | Enterprise deployment/import not verified |

**Suggested timing:** 1 minute foundation, 2 minutes architecture and data, 6–8 minutes app walkthrough, 2–3 minutes analytics, 2–3 minutes QA/tradeoffs. This is a guide, not a recorded video: video files should be created only after actual captures and review.

## Metrics you may cite **only in their correct context**

| Metric | Grounded interpretation |
| --- | --- |
| 1 campus / 2 halls | Fixed fictional development landscape |
| 100 assets / 24 sensors | Source register and CSV dimension counts |
| 120 alarms / 200 incidents | Original fictional dataset counts |
| 500 source Work Orders | Original CSV baseline; one extra training row may exist in tenant |
| 20 Rack Plans | Dataverse capacity-planning demonstration |
| 50,000 readings | Static synthetic CSV/Power BI Import dataset |
| 290 High / 193 Low / 49,517 Normal | Fictional threshold flags, **not** actual Alarm events |
| 13 Pass / 5 Not Run | Maker-reported Part 15 private UAT, not a public rerun |
| 143 accessibility findings | Previously reported Canvas capacity-app checker result; needs remediation |

## Demonstration quality gates

Use [the public Part 16 verification checklist](../quality/Part-16-Final-Verification.csv) to check every scene. That public CSV starts **Not Run**; record real tenant-specific execution outcomes only in a private copy. A screenshot taken in Studio while a component is unsaved is not evidence of the **published app**. A successful flow history item is not proof that an email was sent in this session. An unmanaged export is not an import/restore test.

## Suggested closing explanation

“This is a fictional, end-to-end Power Platform portfolio. The major value is a coherent relational data model, multiple purposeful applications, controlled workflows, synthetic operational analytics and transparent engineering evidence. Remaining work—accessibility remediation, least-privilege testing, concurrency-safe capacity booking and target-environment validation—is identified rather than concealed.”

Do not publish recorded material with exposed user identity, institution context or tenant details.
