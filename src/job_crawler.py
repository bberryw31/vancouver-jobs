import requests
from bs4 import BeautifulSoup


def check_brace_yourself_jobs():
    url = 'https://braceyourselfgames.com/careers/'

    # Get the webpage
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get all the text from the page
    page_text = soup.get_text()

    # Find the "Job Openings" section
    if "Job Openings" in page_text:
        start = page_text.find("Job Openings")
        end = page_text.find("Connect with us:SteamDiscordYouTube")
        job_section = page_text[start:end]
        print("Job section found:")
        print(job_section)
    else:
        print("Job Openings section not found")


if __name__ == "__main__":
    check_brace_yourself_jobs()