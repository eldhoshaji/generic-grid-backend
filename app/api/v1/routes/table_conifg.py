# app/api/config.py
from typing import List
from fastapi import APIRouter, HTTPException
from app.api.v1.services.table_config import get_config_for_table
from app.schemas.table_config import TableConfigResponseModel
import json

router = APIRouter()

@router.get("/{table_name}", response_model=TableConfigResponseModel)
async def fetch_table_config(table_name: str):
    config = get_config_for_table(table_name)
    if not config:
        raise HTTPException(status_code=404, detail="Config not found")
    
    a = json.dumps(config)
    return TableConfigResponseModel(**config)
