import requests
from bs4 import BeautifulSoup


def fetch_jobs():
    """Fetch jobs from Brace Yourself Games"""
    company = "Brace Yourself Games"
    url = 'https://braceyourselfgames.com/careers/'

    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        jobs = []
        page_text = soup.get_text()

        # Find the "Job Openings" section
        if "Job Openings" in page_text:
            start = page_text.find("Job Openings")
            end = page_text.find("Brace Yourself GamesConnect with us:")
            job_section = page_text[start:end].strip()
            print("Job section found:")
            print(job_section)
            if job_section != "Job Openings":
                print("Job Openings found")

        return

    except Exception as e:
        print(e)