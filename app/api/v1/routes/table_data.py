from fastapi import APIRouter, HTTPException, Body
from app.api.v1.services.table_data import get_data_for_table
from app.schemas.params import PaginatedResponse, PaginationParams, FilterParam, SearchParam, SortParam
from app.schemas.table_response import UserResponseModel, ProductResponseModel, PriceComparisonResponseModel
from typing import Any, List, Type, Dict

router = APIRouter()

# Mapping of table names to response models
TABLE_MODEL_MAP: Dict[str, Type] = {
    "users": UserResponseModel,
    "products": ProductResponseModel,
    "product_price_comparison": PriceComparisonResponseModel
}

# Helper function to get the correct model based on the table name
def get_response_model(table_name: str):
    # Default to UserResponseModel if table_name is not found
    return TABLE_MODEL_MAP.get(table_name, UserResponseModel)


@router.post("/{table_name}", response_model=PaginatedResponse)
async def fetch_table_data(
    table_name: str,
    search: SearchParam = Body(None),
    filters: List[FilterParam] = Body(None),
    pagination: PaginationParams = Body(PaginationParams()),
    sort: SortParam = Body(None)
):
    response_model = get_response_model(table_name)

    total, data = get_data_for_table(table_name, search, filters, pagination, sort)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    
    return PaginatedResponse[response_model](
        total=total,
        page=pagination.page,
        size=pagination.size,
        items=[response_model(**item) for item in data]
    )
