import random

from fastapi import FastAPI, Response
from pydantic import BaseModel, Field
import random


class PingResponse(BaseModel):
    lucky_number: int = Field(default_factory=random.random)
    weather:str = Field(default=random.choice(['sunny', 'cloudy', 'windy']))


app = FastAPI()


@app.get("/")
def root_response():
    return Response(content="This is the root response", status_code=200)


@app.get("/api/weather")
def ping_response():
    return PingResponse()
