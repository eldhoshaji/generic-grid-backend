from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[int]
    name: str
    age: int
    address: str

    class Config:
        orm_mode = True  # This ensures compatibility with ORM-like data
