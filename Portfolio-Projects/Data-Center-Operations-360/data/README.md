# Sample datasets — Data Center Operations 360

All data in this directory is fictional and intended for learning. These files are reference inputs for the [Build Guide](../Build-Guide.md), not records extracted from a real organization.

| Dataset | Rows | Key fields | Build status |
| --- | ---: | --- | --- |
| [departments.csv](./departments.csv) | 6 | Department Code, Department Name | Used in the first published chapter |
| [campuses.csv](./campuses.csv) | 1 | Campus Code, Campus Name | Preview data for a later lesson |
| [data-halls.csv](./data-halls.csv) | 2 | Hall Code, Campus Code | Preview data for a later lesson |

## Working with these files

1. Follow the Build Guide to create and configure the corresponding Dataverse table **before** importing or entering its records.
2. Check required fields, data types, relationships, and choices before loading CSV values.
3. Treat business codes (such as `DC-OPS`) as human-readable source identifiers. They are **not** Dataverse primary GUIDs.
4. For a lookup, choose the referenced record in Dataverse or use a supported import mapping. Do not paste fictional business codes into a GUID field.
5. Save and refresh the data view to verify the records actually persisted.

These CSVs contain no account credentials, real university identities, real facility telemetry, or operational secrets.
