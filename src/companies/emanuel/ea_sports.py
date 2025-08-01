import requests
from bs4 import BeautifulSoup

def fetch_ea_jobs():
    url = f'https://jobs.ea.com/en_US/careers/Home/?4538=%5B10259467%5D&4538_format=3021&listFilterMode=1&jobRecordsPerPage=100'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all(id=lambda x: x and x.startswith("article--"))
    articles = soup.find_all(id=lambda x: x and x.startswith("article--"))
    for a in articles:
        listing = [line.strip() for line in a.text.split() if "senior" not in a.text.lower()]
        print(listing)

