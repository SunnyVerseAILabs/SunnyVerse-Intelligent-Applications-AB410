# DC360 — Portfolio Evidence Matrix

[Project home](../README.md) · [Case study](./Case-Study.md) · [Demonstration](./Demo-Walkthrough.md)

This is a **public, privacy-safe evidence index**. It deliberately distinguishes published reproducible sources from reported implementation observations. It is **not** a mirror of a private test log.

| Evidence ID | Claim / demonstration | Public source link | Evidence class | Safe portfolio wording |
| --- | --- | --- | --- | --- |
| EV-01 | Reproducible step-by-step system design | [Build Guide](../Build-Guide.md) | Published learning source | “Documented through Parts 00–16” |
| EV-02 | Fictional organization and linked equipment | [Source datasets](../data/README.md) | Published synthetic data | “1 campus, 2 halls, 100 equipment assets, 24 sensors” |
| EV-03 | Incident and maintenance baseline | [Incidents](../data/incidents.csv), [Work orders](../data/work-orders.csv) | Published synthetic data | “200 starting incident rows and 500 starting work-order CSV rows” |
| EV-04 | 50,000 reading analytics source | [Monitoring data](../data/monitoring/README.md) | Published synthetic data | “50,000 samples over 24 sensor codes” |
| EV-05 | Reproducible Power BI model source | [PBIP source README](../powerbi/README.md) | Sanitized source artifact | “Seven model tables, six active relationships, twenty measures, five report pages in the reference source” |
| EV-06 | Operational apps and relationships | [Parts 06–12](../Build-Guide.md) | Implementation instructions + maker-supplied completion history | “Three Canvas and three model-driven app experiences were developed; confirm current published state when demonstrating” |
| EV-07 | Rules-based insight workflow | [Part 14](../Build-Guide.md#part-14--build-rules-based-intelligent-operations-and-reviewed-knowledge) | Learning source + prior maker test report | “Demonstrated repeat-run deduplication for one synthetic insight; not atomic under concurrency” |
| EV-08 | Engineering test framework | [Public UAT template](../quality/Part-15-UAT-Matrix.csv) | Unexecuted learner template | “18 reusable UAT checks; private results are deliberately not uploaded” |
| EV-09 | Solution export and ALM review | [Part 15](../Build-Guide.md#part-15--engineer-test-and-prepare-the-solution-for-release) | Documented process + private package evidence | “An unmanaged source export was verified privately; no target import claim” |
| EV-10 | Portfolio end-to-end walkthrough | [Demo walkthrough](./Demo-Walkthrough.md) | Published demonstration instructions | “Execute only approved, reproducible read-only demonstrations” |
| EV-11 | Architecture | [Architecture](./Architecture.md) | Published design artifact | “Shows actual source boundaries and documented trade-offs” |
| EV-12 | Final presentation | [Presentation storyboard](./Presentation-Storyboard.md) | Published presentation content | “Evidence-led deck; live screenshots and runtime tests must be verified separately” |

## Evidence labels for reviewers

- **Published source**: a GitHub file exists and its contents can be inspected. It is not proof a live cloud component runs.
- **Prior maker-reported implementation**: a saved implementation report contains observed tenant results; a fresh reviewer has not independently rerun those actions.
- **Artifact-inspected**: the content/metadata of an uploaded or published file was inspected directly. This does not prove its successful use in a different environment.
- **Not retested / open**: the relevant live action, import, role test or regression did not occur in the final review.
- **Sanitized screenshot pending**: no image should be invented or inserted as if captured from a real app.

## Known limitations to disclose

The previous Part 15 private report recorded **13 Pass, five Not Run and zero Fail** for the eighteen UAT cases; the five not-run cases concern Play-mode navigation, a possibly write-capable capacity validation test and repeat Power BI Desktop checks. A prior solution checker reported **148 Medium findings**, including **143 Capacity Planner accessibility issues**. Two DC08 flow records share a display name. One extra training Work Order can yield **501 current Dataverse rows vs 500 source CSV rows**. Non-admin security testing, a target-environment import and server-side capacity concurrency remain unverified. These are **reported findings**, not evidence that the public GitHub assets automatically passed all validation.

## Safely adding demonstration evidence

1. Capture screenshots only from an authorized demonstration account/session.
2. Crop or redact browser chrome, tenant GUIDs, usernames, real connection records, environment-variable values, addresses and any identifiable account information.
3. Compare every caption and metric with the exact selected filter context.
4. Add a descriptive filename, date, scope and whether it was a saved app, published app, Power BI Desktop model or static mockup.
5. Publish only after an independent privacy review. Keep raw originals outside GitHub.

**No screenshots, private archive, account-specific hashes or private testing documents are required to follow the learner guide.**
