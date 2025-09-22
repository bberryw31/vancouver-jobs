import requests
from bs4 import BeautifulSoup


def fetch_jobs():
    """Fetch jobs from CD Projekt Red"""
    company = "CD Projekt Red"
    url = 'https://www.cdprojektred.com/en/jobs?studio=canada'

    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        jobs = []
        accordion_items = soup.find_all('div', class_='accordion-item')

        for accordion_item in accordion_items:
            # Skip if accordion is hidden (no jobs available)
            if 'hide-offer' in accordion_item.get('class', []):
                continue

            # Get the department name from accordion header
            header = accordion_item.find('h2', class_='accordion-header')
            department = "Unknown Department"
            if header:
                button = header.find('button')
                if button:
                    department = button.get_text().strip()

            # Find all job offers within this accordion
            job_offers = accordion_item.find_all('div', class_='job-offer')

            for job_offer in job_offers:
                # Skip hidden job offers
                if 'hide-offer' in job_offer.get('class', []):
                    continue

                job = self._parse_job_offer(job_offer, department)
                if job:
                    jobs.append(job)

        return

    except Exception as e:
        print(e)