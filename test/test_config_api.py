from fastapi.testclient import TestClient
from app.main import app  # Import the FastAPI app

client = TestClient(app)

def test_fetch_table_config_success():
    # Make an actual API request
    response = client.get("api/v1/config/users")
    
    # Check if the status code is 200
    assert response.status_code == 200
    
    # Get the response data as JSON
    data = response.json()
    
   # Assert the 'table_name' is correct
    assert data["table_name"] == "users"
    
    # Assert 'row_style_rules' contains the required fields
    assert len(data["row_style_rules"]) > 0
    row_style_rule = data["row_style_rules"][0]
    assert "field" in row_style_rule
    assert "operator" in row_style_rule
    assert "value" in row_style_rule
    assert "class_name" in row_style_rule
    
    # Assert 'column_configs' contains the required fields
    assert len(data["column_configs"]) > 0
    column_config = data["column_configs"][0]
    assert "key" in column_config
    assert "title" in column_config
    assert "type" in column_config
    assert "filterable" in column_config
    assert "sortable" in column_config
    assert "searchable" in column_config
    assert "filters" in column_config

    # Optionally, check if the values match your expected types or values
    assert isinstance(column_config["key"], str)
    assert isinstance(column_config["title"], str)
    assert isinstance(column_config["type"], str)
    assert isinstance(column_config["filterable"], bool)
    assert isinstance(column_config["sortable"], bool)
    assert isinstance(column_config["searchable"], bool)
    assert isinstance(column_config["filters"], list)
