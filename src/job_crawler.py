# from companies.emanuel import
from companies.jimmy import brace_yourself_games, demonware
from companies.emanuel import ea_sports
from job_exporter import save_jobs

def run_emanuel():
    """Run Emanuel's crawler"""
    print("🔍 Running Emanuel's job crawler...")
    scrapers = [ea_sports.fetch_ea_jobs()]

    for scraper in scrapers:
        try:
            scraper()
        except Exception as e:
            print(e)


def run_jimmy():
    """Run Jimmy's crawler"""
    print("🔍 Running Jimmy's job crawler...")
    scrapers = [demonware.fetch_jobs]

    collected_jobs = []

    for scraper in scrapers:
        try:
            collected_jobs.extend(scraper())
        except Exception as e:
            print(e)

    return collected_jobs


def main():
    print("🚀 Initiating Vancouver Jobs Monitor")
    print("=" * 50)

    all_collected_jobs = []

    # TODO: Update crawler to use Selenium and return in correct structure
    # Run Emanuel's crawler
    # run_emanuel()
    # print("\n" + "=" * 50)

    # Run Jimmy's crawler
    all_collected_jobs.extend(run_jimmy())

    if all_collected_jobs:
        save_jobs(all_collected_jobs)


if __name__ == "__main__":
    main()