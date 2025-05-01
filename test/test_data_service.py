from app.schemas.params import PaginationParams, SearchParam, FilterParam, SortParam
from app.api.v1.services.table_data import get_data_for_table


# Basic test without filters
def test_get_all_users():
    total, items = get_data_for_table("users")
    assert total == 50
    assert len(items) == 10


# Test with search
def test_search_user_by_name():
    total, items = get_data_for_table("users", search=SearchParam(key="name", value="Ashley"))
    assert total == 1
    assert items[0]["name"] == "Ashley Bell"


# Test with filter
def test_filter_user_by_age():
    filters = [FilterParam(key="age", value="34")]
    total, items = get_data_for_table("users", filters=filters)
    assert total == 1
    assert items[0]["name"] == "Cory Acosta"


# Test with sort
def test_sort_by_age_desc():
    sort = SortParam(key="age", direction="desc")
    total, items = get_data_for_table("users", sort=sort)
    assert items[0]["age"] == 85  # Christopher Moore


# Test with pagination
def test_pagination():
    pagination = PaginationParams(page=2, size=2)
    total, items = get_data_for_table("users", pagination=pagination)
    assert total == 50
    assert len(items) == 2
    assert items[0]["id"] == 29
