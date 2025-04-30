from fastapi import APIRouter

from app.api.v1.routes import table_conifg, table_data
from app.core.config import settings

api_router = APIRouter()
api_router.include_router(table_conifg.router, prefix='/config')
api_router.include_router(table_data.router, prefix='/data')

# if settings.ENVIRONMENT == "local":
#     api_router.include_router(private.router)