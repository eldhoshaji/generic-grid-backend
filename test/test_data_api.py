from fastapi.testclient import TestClient
from app.main import app  # Import your FastAPI app

# Initialize the test client
client = TestClient(app)


# Test for fetch_table_data endpoint (with real API request)
def test_fetch_table_data_success():
    table_name = "users"

    # Simulate the POST request with body params
    response = client.post(
        f"api/v1/data/{table_name}",
        json={
            "search": {"key": "name", "value": "Ashley Bell"},
            "pagination": {"page": 1, "size": 10},
            "sort": {"key": "age", "direction": "asc"}
        }
    )

    # Assert status code
    assert response.status_code == 200

    # Assert response structure
    data = response.json()
    assert "total" in data
    assert "page" in data
    assert "size" in data
    assert "items" in data
    assert isinstance(data["items"], list)

    # Validate the first item in the response
    assert len(data["items"]) > 0  # Ensure at least one item is returned

    # Check if the user is the one with "Ashley Bell" as the name
    assert data["items"][0]["name"] == "Ashley Bell"
    assert data["items"][0]["age"] == 30
    assert data["items"][0]["address"] == "77548 Brian Isle Suite 522, South Corey, KY 50484"
    assert "tags" in data["items"][0]
    assert "friendly" in data["items"][0]["tags"]
    assert "designer" in data["items"][0]["tags"]


def test_fetch_table_data_not_found():
    table_name = "non_existing_table"

    # Simulate the POST request with body params
    response = client.post(
        f"api/v1/data/{table_name}",
        json={
            "search": {"key": "name", "value": "Ashley Bell"},
            "filters": [{"key": "age", "value": 30}],
            "pagination": {"page": 1, "size": 10},
            "sort": {"key": "age", "direction": "asc"}
        }
    )
    # Assert status code and error message
    assert response.status_code == 422
