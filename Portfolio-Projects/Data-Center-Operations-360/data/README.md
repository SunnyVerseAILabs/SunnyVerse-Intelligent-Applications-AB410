# Practice dataset library

[Back to the Build Guide](../Build-Guide.md)

This directory will contain **original synthetic practice datasets** as the corresponding learner exercises are published. Each dataset will be linked from its relevant Build Guide section with the expected column names, record counts, validation checks, and import method.

**Available practice data:**

- [Part 01 — departments.csv](./departments.csv): six fictional departments.
- [Part 02 — campuses.csv](./campuses.csv): one fictional campus.
- [Part 02 — data-halls.csv](./data-halls.csv): two fictional data halls linked to that campus.
- [Part 03 — employee-profiles.csv](./employee-profiles.csv): 20 fictional employee profiles for initial import. After creating the records, follow [Part 03](../Build-Guide.md#part-03--build-the-employee-directory-and-reporting-hierarchy) to select the existing Department, Campus and Manager lookup records.

The CSV headers exactly match the **display names** introduced in the [Build Guide](../Build-Guide.md). The guide identifies the intended **svrg-prefixed schema names** separately. Dataverse may suggest field mapping automatically, but always review Choice and lookup values before completing an import. Import the campus before the data halls. If you have entered the same rows manually, do not also import the CSVs.

Do not import datasets from previous experiments, previous Power Platform solutions, or unrelated AB-410 course modules. Every future dataset will be fictional and checked for consistency with the published schema.

Do not upload personal, institutional, tenant or credential information to a public repository.
