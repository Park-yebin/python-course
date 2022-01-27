from indeed import get_jobs as get_indeed_jobs
from stockoverflow import get_jobs as get_sto_jobs

indeed_jobs = get_indeed_jobs()
stock_jobs = get_sto_jobs()
jobs = stock_jobs + indeed_jobs
print(jobs)
