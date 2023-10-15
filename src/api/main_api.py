from fastapi import FastAPI, Response
from rq import Queue
from redis import Redis
from worker.background_worker import run_job
from api.data_models import JobData
import requests

redis_conn = Redis(host='redis', port=6379, db=0)
queue = Queue(connection=redis_conn, default_timeout=24*60*60)





app = FastAPI()


@app.get("/")
def root():
    return Response(content="This is the root of the api use other routes to access some usefull infomration")


@app.get("/healthz")
def healthz():
    return Response(content="Ok", status_code=200)


@app.post("/dispatch_job")
def enqueue_job(job: JobData):
    job = queue.enqueue(run_job, job)
    return Response(content=f"job dispatched with id {job.id}", status_code=200)


@app.get("/job/{job_id}")
async def read_job_status(job_id: str):
    # Retrieve the job by its ID
    job = queue.fetch_job(job_id)
    if job is None:
        return Response(status_code=404, content="Job not found")
    job_status = job.get_status()

    if job.is_finished:
        # If the job is done, return the result
        job_result = job.return_value()
        return {"status": job_status, "result": job_result}
    if job.is_queued:
        return Response(content=f"Job is queued at position {job.get_position()}")
    else:
        # If the job is still running, return the status
        return {"status": job_status}

@app.get("/ping_weather")
def weather_ping():
    response = requests.get("http://weatherappsvc/api/weather")
    if response.status_code == 200:
        return response.json()
