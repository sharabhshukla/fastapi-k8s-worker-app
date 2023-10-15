FROM python:3.10
COPY . /app
WORKDIR /app
RUN pip install -r api/requirements.txt
EXPOSE 8090
ENTRYPOINT uvicorn weatherapp.main_app:app --host=0.0.0.0 --port=8090