import requests
from bs4 import BeautifulSoup

def fetch_ea_jobs():
    url = f'https://jobs.ea.com/en_US/careers/Home/?4538=%5B10259467%5D&4538_format=3021&listFilterMode=1&jobRecordsPerPage=100'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all(id=lambda x: x and x.startswith("article--"))
    articles = soup.find_all(id=lambda x: x and x.startswith("article--"))
    for a in articles:
        title = a.find(class_="title").text.strip()
        if title and "senior" in title.lower():
            continue
        location = a.find(class_="list-item-location").text.strip()
        department = a.find(class_="list-item-department").text.strip()
        listing = {"title":title, "location":location, "department":department}
        print(listing)

