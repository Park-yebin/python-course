from indeed import get_jobs as get_indeed_jobs
from stockoverflow import get_jobs as get_sto_jobs
from save import save_to_file

indeed_jobs = get_indeed_jobs()
stock_jobs = get_sto_jobs()
jobs = stock_jobs + indeed_jobs
save_to_file(jobs)
