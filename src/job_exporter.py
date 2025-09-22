import json
from datetime import datetime
import os


def save_jobs(all_jobs):
    """Save jobs to GitHub data directory"""
    data_dir = "../.github/data"
    os.makedirs(data_dir, exist_ok=True)

    if not all_jobs:
        print("No jobs to export")
        return

    # Export to JSON
    json_file = os.path.join(data_dir, "vancouver_jobs_latest.json")

    export_data = {
        "export_info": {
            "timestamp": datetime.now().isoformat(),
            "total_jobs": len(all_jobs),
            "companies": list(set(job.get('company', 'Unknown') for job in all_jobs))
        },
        "jobs": all_jobs
    }

    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(export_data, file, indent=2, ensure_ascii=False)

    print(f"Saved {len(all_jobs)} jobs to {json_file}")
