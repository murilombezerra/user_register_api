from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    gender: Gender




