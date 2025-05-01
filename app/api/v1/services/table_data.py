from typing import List
from app.core.mock_db.db import mock_db
from app.schemas.params import PaginationParams, SearchParam, FilterParam, SortParam


def get_data_for_table(
    table_name: str,
    search: SearchParam = None,
    filters: List[FilterParam] = None,
    pagination: PaginationParams = PaginationParams(),
    sort: SortParam = None
):
    data = mock_db.get(table_name)

    if search:
        data = [item for item in data if search.value.lower() in str(item.get(search.key, "")).lower()]

    # Apply additional filters
    if filters:
        for filter in filters:
            data = [item for item in data if str(item.get(filter.key, "")).lower() == filter.value.lower()]

    if sort:
        reverse = sort.direction == 'desc'  # if 'desc', reverse=True
        data.sort(key=lambda x: x.get(sort.key, ""), reverse=reverse)

    # Pagination logic
    start_index = (pagination.page - 1) * pagination.size
    end_index = start_index + pagination.size

    return len(data), data[start_index:end_index]
