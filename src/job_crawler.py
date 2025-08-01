# from companies.emanuel import
from companies.jimmy import brace_yourself_games
from companies.emanuel import ea_sports

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
    scrapers = [brace_yourself_games.fetch_jobs]

    for scraper in scrapers:
        try:
            scraper()
        except Exception as e:
            print(e)


def main():
    print("🚀 Initiating Vancouver Jobs Monitor")
    print("=" * 50)

    # Run Emanuel's crawler
    run_emanuel()
    print("\n" + "=" * 50)

    # Run Jimmy's crawler
    run_jimmy()
    print("\n" + "=" * 50)

    print(f"🎉 Job monitoring complete!")


if __name__ == "__main__":
    main()