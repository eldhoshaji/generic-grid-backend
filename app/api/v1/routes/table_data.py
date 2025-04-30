from fastapi import APIRouter, HTTPException, Body
from app.api.v1.services.table_data import get_data_for_table
from app.schemas.params import PaginatedResponse, PaginationParams, FilterParam, SearchParam, SortParam
from app.schemas.user import UserResponseModel
from typing import List

router = APIRouter()

@router.post("/{table_name}", response_model=PaginatedResponse[UserResponseModel])
async def fetch_table_data(
    table_name: str,
    search: SearchParam = Body(None),
    filters: List[FilterParam] = Body(None),
    pagination: PaginationParams = Body(PaginationParams()),
    sort: SortParam = Body(None)
):
    total, data = get_data_for_table(table_name, search, filters, pagination, sort)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    
    return PaginatedResponse[UserResponseModel](
        total=total,
        page=pagination.page,
        size=pagination.size,
        items=[UserResponseModel(**item) for item in data]
    )
