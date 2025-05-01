from typing import List
from pydantic import BaseModel
from typing import Optional


# Response model
class UserResponseModel(BaseModel):
    id: int
    name: str
    age: int
    address: str
    tags: List[str]


class ProductResponseModel(BaseModel):
    id: int
    name: str
    price: float
    description: str
    purchase_date: str
    product_link: str
    category: List[str]


class PriceComparisonResponseModel(BaseModel):
    name: str
    price_2015: Optional[float] = None
    price_2016: Optional[float] = None
    price_2017: Optional[float] = None
    price_2018: Optional[float] = None
    price_2019: Optional[float] = None
    price_2020: Optional[float] = None
    price_2021: Optional[float] = None
    price_2022: Optional[float] = None
    price_2023: Optional[float] = None
    price_2024: Optional[float] = None
    price_2025: Optional[float] = None
