from typing import List
from pydantic import BaseModel

# Request model
class UserRequestModel(BaseModel):
    name: str
    age: int
    address: str

# Response model
class UserResponseModel(BaseModel):
    id: int
    name: str
    age: int
    address: str
    tags: List[str]

    # class Config:
    #     # orm_mode = True
    #     from_attributes = True
