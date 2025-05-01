from fastapi import APIRouter
from app.api.v1.routes import table_conifg, table_data

api_router = APIRouter()
api_router.include_router(table_conifg.router, prefix='/config')
api_router.include_router(table_data.router, prefix='/data')
