from typing import Generic, TypeVar, List
from pydantic import BaseModel
from typing import Literal
from pydantic.generics import GenericModel

class PaginationParams(BaseModel):
    page: int = 1
    size: int = 10

class SearchParam(BaseModel):
    key: str
    value: str

class FilterParam(BaseModel):
    key: str
    value: str
    
class SortParam(BaseModel):
    key: str
    direction: Literal['asc', 'desc'] = 'asc'


T = TypeVar("T")

class PaginatedResponse(GenericModel, Generic[T]):
    total: int
    page: int
    size: int
    items: List[T]

