FROM python:3.10
COPY . /app
WORKDIR /app
RUN pip install -r api/requirements.txt
EXPOSE 8080
ENTRYPOINT uvicorn api.main_api:app --host=0.0.0.0 --port=8080