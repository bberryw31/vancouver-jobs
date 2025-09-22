import json
import csv
from datetime import datetime
import os


def save_jobs(all_jobs):
    """Save jobs to GitHub data directory in JSON and CSV formats"""
    data_dir = "../.github/data"
    os.makedirs(data_dir, exist_ok=True)

    if not all_jobs:
        print("No jobs to export")
        return

    timestamp = datetime.now().isoformat()

    # Add timestamp to each job
    for job in all_jobs:
        job['scraped_at'] = timestamp

    # Save JSON
    json_file = os.path.join(data_dir, "vancouver_jobs_latest.json")

    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(all_jobs, file, indent=2, ensure_ascii=False)

    # Save CSV
    csv_file = os.path.join(data_dir, "vancouver_jobs_latest.csv")

    if all_jobs:
        fieldnames = ['company', 'title', 'location', 'url', 'scraped_at']

        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(all_jobs)

    print(f"Saved {len(all_jobs)} jobs")