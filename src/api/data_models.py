from pydantic import BaseModel


class JobData(BaseModel):
    high: int
    low: int
