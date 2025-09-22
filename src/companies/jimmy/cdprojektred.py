import requests
from bs4 import BeautifulSoup


def fetch_jobs():
    """Fetch jobs from CD Projekt Red"""
    company = "CD Projekt Red"
    url = 'https://www.cdprojektred.com/en/jobs?studio=canada'
    pass