import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}&radius=25&vjk=e7c8c2b11f24fb43"


def extract_indeed_pages():
    result = requests.get(URL)
# "https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=50&vjk=8f62684fb1d35c1d"
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
# pages = pages[:-1]

    max_page = pages[-1]
    return max_page


def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "job_seen_beacon"})
        print(results)
    return jobs
