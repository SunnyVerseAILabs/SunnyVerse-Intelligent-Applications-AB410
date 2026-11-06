# Power BI — DC360 Operations Intelligence

[Back to the complete Build Guide](../Build-Guide.md#part-13--build-monitoring-and-operational-intelligence-with-power-bi) · [Monitoring dataset](../data/monitoring/) · [Project home](../README.md)

The file [DC360-Operations-Intelligence-PBIP-Source.tar.gz](./DC360-Operations-Intelligence-PBIP-Source.tar.gz) is a **privacy-reviewed, path-sanitized source project** derived from a fictional Power BI Desktop learning report. It contains the `.pbip` launcher, five report-page definitions, seven model table definitions, six model relationships and 20 DAX measures. The source includes the `Sensor Key Mismatches = ... + 0` display correction.

**This is a source archive, not the original PBIX, and not a published Power BI Service report.** The original PBIX remained outside the public repository because its local source configuration contained a Windows user-profile path. This archive intentionally excludes `.pbi/localSettings.json`, cached model data (`cache.abf`), local scripts, and temporary test datasets. The source uses the neutral folder placeholder `C:\DC360-Learning`; every learner must supply their own authorized local file paths and refresh the model.

## How to open on a Windows learning computer

1. Download the `.tar.gz` archive from the GitHub link above.
2. Open PowerShell in your Downloads folder and run:

   `tar -xzf DC360-Operations-Intelligence-PBIP-Source.tar.gz`

3. Download the ten published [`monitoring-readings-*.csv`](../data/monitoring/) files into `C:\DC360-Learning\monitoring`, and the six reference CSVs (`sensors.csv`, `assets.csv`, `data-halls.csv`, `alarms.csv`, `incidents.csv`, `work-orders.csv`) into `C:\DC360-Learning\reference`. If that root is unavailable, replace the example root path in the seven `.tmdl` Power Query sources with your actual authorized local folder before the first refresh.
4. Open the extracted `DC360-Operations-Intelligence.pbip` file in a supported version of Power BI Desktop.
5. Refresh the model. A cold, source-only PBIP opens without the original data cache, so the first refresh may need local file permissions. Recheck expected row counts and DAX measures before saving a new local PBIX.
6. Follow Part 13 to validate the five report pages and historical snapshot totals. Power BI Service publication, credentials, workspaces and sharing are separately controlled and are not included in this exercise.

| Expected unfiltered model verification | Result |
| --- | ---: |
| Fact Monitoring Readings | 50,000 rows |
| Dim Sensor / Dim Asset / Dim Data Hall | 24 / 100 / 2 |
| Fact Alarm / Fact Incident / Fact Work Order | 120 / 200 / 500 |
| Active single-direction dimension-to-fact relationships | 6 |
| DAX measures | 20 |
| Report pages | 5 |
| High / Low / Normal flagged readings | 290 / 193 / 49,517 |
| Sensor key / threshold flag mismatches | 0 / 0 |

The source is fictional; no real telemetry or operational facilities are represented. GitHub publication of the source **does not** make the original saved PBIX, the author's Desktop environment or any Power BI Service dataset publicly accessible.

**Troubleshooting:** If a report card is blank immediately after opening, check whether the initial data refresh has completed. If source files cannot be found, update the neutral `C:\DC360-Learning` references. If a historical screenshot shows different measures after selecting a bar, clear visual cross-highlighting and all slicers. See the [corrected Part 13 guide](../Build-Guide.md#part-13--build-monitoring-and-operational-intelligence-with-power-bi) for tested null/date handling, threshold table and negative tests.

**Microsoft Learn:** [Power BI Desktop projects](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview) · [Semantic model source folders](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-dataset).
