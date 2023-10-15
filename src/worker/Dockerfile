FROM python:3.10
COPY . /app
WORKDIR /app/
RUN pip install -r api/requirements.txt
EXPOSE 6379
ENTRYPOINT ["rq", "worker", "--url", "redis://redis:6379", "default"]