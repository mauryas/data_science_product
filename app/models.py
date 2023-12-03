from typing import List

from pydantic import BaseModel


class PointResponse(BaseModel):
    name: str
    x: int = None
    y: int = None


class PointMapResponse(BaseModel):
    points: List[PointResponse] = []


class Accuracy(BaseModel):
    accuracy: float = None
