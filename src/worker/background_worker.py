import random

from api.data_models import JobData
from time import sleep


def run_job(job: JobData):
    count = 0
    for i in range(job.low, job.high + 1):
        print(i)
        for i in range(i * 1000000):
            x, y = random.random(), random.random()
            if x ** 2 + y ** 2 <= 1:
                count += 1
    print(f"sleeping for {job.high - job.low} seconds")
    sleep(job.high - job.low)
    return {"status": "Ok", "high": job.low, "low": job.low}
