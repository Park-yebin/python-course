import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}&radius=25&vjk=e7c8c2b11f24fb43"


def get_last_page():
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


def extract_job(result):
    title = result.select_one('.jobTitle>span').string
    company = result.find("div", {"class": "company_location"})
    company_span = company.find("span", {"class": "companyName"})
    company_anchor = company.find("a")
    if company_anchor is not None:
        # 빈칸이 있는 경우 company = company.strip() 하면 불필요한 빈칸들이 없어짐
        company = str(company_anchor.string)
    elif company_span is not None:
        company = str(company_span.string)
    else:
        company = "None"
    location = result.find("div", {"class": "companyLocation"}).string
    # 받아온 곳(result)에서의 범위 안에 존재하지 않으면 오류난다. 범위 설정 조심
    job_id = result['data-jk']
    return {'title': title, 'company': company, 'location': location, 'link': f"https://kr.indeed.com/viewjob?jk={job_id}&tk=1fqb29bmvk47h801&from=serp&vjs=3"}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping page {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("a", {"class": "resultWithShelf"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_pages = get_last_page()
    jobs = extract_jobs(last_pages)
    return jobs
