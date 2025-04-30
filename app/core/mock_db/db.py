from app.core.mock_db.products import product_data
from app.core.mock_db.users import user_data
from app.core.mock_db.table_config import table_config
from app.core.mock_db.price_comparison import product_price_comparison_data

mock_db = {
    "table_config_db": table_config,
    "users": user_data,
    "products": product_data,
    "product_price_comparison": product_price_comparison_data
}


