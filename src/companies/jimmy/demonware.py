from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def fetch_jobs():
    """Fetch jobs from Demonware"""
    company = "Demonware"
    url = 'https://careers.demonware.net/search-results'
    print(f"Scraping {company} jobs...")

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)

        wait = WebDriverWait(driver, 10)
        job_items = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "jobs-list-item"))
        )

        vancouver_jobs = []

        for item in job_items:
            try:
                job_link = item.find_element(By.CSS_SELECTOR, "a[data-ph-at-id='job-link']")

                title = job_link.get_attribute("data-ph-at-job-title-text")
                location = job_link.get_attribute("data-ph-at-job-location-text")
                job_url = job_link.get_attribute("href")

                if location and 'vancouver' in location.lower():
                    job_data = {
                        "company": company,
                        "title": title,
                        "location": location,
                        "url": job_url
                    }
                    vancouver_jobs.append(job_data)
            except:
                continue

        print(f"Found {len(vancouver_jobs)} Vancouver jobs at Demonware")
        return vancouver_jobs

    except Exception as e:
        print(e)
        return []

    finally:
        driver.quit()