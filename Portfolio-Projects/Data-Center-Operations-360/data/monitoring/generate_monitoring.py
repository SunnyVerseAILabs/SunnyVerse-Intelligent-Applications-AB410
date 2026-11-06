#!/usr/bin/env python3
"""Build ten repeatable 5,000-row synthetic monitoring CSVs for the DC360 learning report.

Usage:
  python generate_monitoring.py --sensors ../sensors.csv --output ./generated
The output folder must be empty of other CSVs before loading with Power BI Folder.
"""
import argparse
import csv
import datetime
import math
from pathlib import Path

parser = argparse.ArgumentParser(description="Generate 50,000 fictional sensor readings.")
parser.add_argument("--sensors", required=True)
parser.add_argument("--output", required=True)
args = parser.parse_args()
with open(args.sensors, encoding="utf-8-sig", newline="") as f:
    sensors = list(csv.DictReader(f))
if len(sensors) != 24 or len({x["Sensor Code"] for x in sensors}) != 24:
    raise ValueError("The reference CSV must contain 24 uniquely coded sensors.")
folder = Path(args.output)
folder.mkdir(parents=True, exist_ok=True)
columns = ["Reading ID", "Recorded At UTC", "Sensor Code", "Reading Value", "Threshold State"]
for batch in range(10):
    filename = folder / f"monitoring-readings-{batch+1:02d}.csv"
    with filename.open("w", encoding="utf-8", newline="") as out:
        writer = csv.writer(out, lineterminator="\n")
        writer.writerow(columns)
        for i in range(batch * 5000, (batch + 1) * 5000):
            sensor = sensors[i % 24]
            minimum = float(sensor["Minimum Acceptable"])
            maximum = float(sensor["Maximum Acceptable"])
            span = maximum - minimum
            slot = i // 24
            timestamp = datetime.datetime(2026, 10, 1, tzinfo=datetime.timezone.utc)
            timestamp += datetime.timedelta(minutes=slot * 15)
            if i % 173 == 0:
                value = maximum + 0.12 * span
                state = "High"
            elif i % 257 == 0:
                value = minimum - 0.08 * span
                state = "Low"
            else:
                value = minimum + span * (0.5 + 0.25 * math.sin((slot + i % 24) * 0.31))
                state = "Normal"
            writer.writerow([
                f"RDG-{i+1:06d}",
                timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                sensor["Sensor Code"],
                f"{value:.2f}",
                state,
            ])
print("Generated 50,000 fictional rows across ten CSV files.")
