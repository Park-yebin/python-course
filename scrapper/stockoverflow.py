import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].find("span").string  # or .get_text(strip = True)
    return int(last_page)


def extract_job(html):
    title = html.find("div", {"class": "fl1"}).find("h2").find("a")[
        "title"]  # 바로 위에 있는 애들에서부터 차근 차근 해야할 듯
    company, location = html.find("h3", {"class": "mb4"}).find_all(
        "span", recursive=False)  # 이건 span 안에 span이 있으면 그건 안 가져오게 함 그리고 얘가 똑똑해서 2개의 span이 있으면 변수 2개를 사용하면 각각에 따로 저장해줌
    company = company.get_text(strip=True)
    # strip = True로 불필요한 빈칸 지울 수 있음 그리고 .strip("-")하면 -을 지울 수 있음
    location = location.get_text(strip=True)
    job_id = html['data-jobid']
    return {'title': title, 'company': company, 'location': location, 'apply_link': f"https://stackoverflow.com/jobs/{job_id}"}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrpaaing STOCK: Page {page}")
        result = requests.get(f"{URL}&pg = {page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
