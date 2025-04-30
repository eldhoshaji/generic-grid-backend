# app/core/config_loader.py
# Dummy version - later replace with DB queries
from app.core.mock_db.db import mock_db

def get_config_for_table(table_name: str):
    
    table_config = next((item for item in mock_db["table_config_db"] if item["table_name"] == table_name), None)

    for field in table_config["column_configs"]:
        if field.get("filterable"):
            key = field["key"]
            table_data = mock_db.get(table_name)

            unique_values = sorted({row[key] for row in table_data if key in row and row[key] is not None})
            field["filters"] = [{"text": val, "value": val} for val in unique_values]

    return table_config
