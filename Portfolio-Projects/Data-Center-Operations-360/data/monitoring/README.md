# Part 13 — Synthetic monitoring readings

[Back to the Build Guide](../../Build-Guide.md#part-13--build-monitoring-and-operational-intelligence-with-power-bi) · [Dataset library](../README.md)

This directory contains **ten CSV files, each with 5,000 original synthetic sensor readings**, for a **50,000-row** Power BI Desktop exercise. No readings originate from live data center instrumentation. All Sensor Code values resolve to the 24 registered sensors in [sensors.csv](../sensors.csv), which in turn reference existing Assets.

## Files and record counts

| File | Number of data rows |
| --- | ---: |
| monitoring-readings-01.csv | 5,000 |
| monitoring-readings-02.csv | 5,000 |
| monitoring-readings-03.csv | 5,000 |
| monitoring-readings-04.csv | 5,000 |
| monitoring-readings-05.csv | 5,000 |
| monitoring-readings-06.csv | 5,000 |
| monitoring-readings-07.csv | 5,000 |
| monitoring-readings-08.csv | 5,000 |
| monitoring-readings-09.csv | 5,000 |
| monitoring-readings-10.csv | 5,000 |
| **Total** | **50,000** |

All files share the header:
```csv
Reading ID,Recorded At UTC,Sensor Code,Reading Value,Threshold State
```

**Expected unfiltered totals:** Normal 49,517; High 290; Low 193; 483 flagged samples. Readings run from `RDG-000001` at 2026-10-01 00:00:00 to `RDG-050000` at 2026-10-22 16:45:00 (UTC-labelled). There are 24 sensor codes and 2,084 time slots. The readings are 15-minute **educational snapshots**, not a claim of the 60-second interval shown in the sensor inventory. Threshold states are **not** Dataverse Alarm events and should not be used for physical equipment decisions.

## Power BI Desktop import

Download or clone the directory and put **only** the ten `monitoring-readings-*.csv` files in one local monitoring folder. Choose **Get data → Folder → Combine & Transform**. Import the existing [sensors.csv](../sensors.csv), [assets.csv](../assets.csv), and [data-halls.csv](../data-halls.csv) separately as dimensional references, then use the [Part 13 Build Guide](../../Build-Guide.md#part-13--build-monitoring-and-operational-intelligence-with-power-bi) to build the model and measures.

## Regeneration (optional)

To reproduce the same ten source files with standard Python 3 (no third-party packages), run from this folder:

```bash
python generate_monitoring.py --sensors ../sensors.csv --output ./generated
```

Keep the generated files separate from already downloaded files so a Power BI Folder import does not load 100,000 duplicate rows. Verify Source IDs, file headers and total row counts before reporting results. Do not upload real telemetry or private tenant/account values.
